from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
from statistics import mean
from typing import Any

from bots.registry import BOT_REGISTRY, build_bot
from engine.card import load_cards
from engine.deck import load_decks
from engine.log_formatter import render_match_log_markdown
from engine.phase_runner import MatchRunner
from sim.log_retention import prune_match_logs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a round-robin deck tournament and generate markdown reports.")
    parser.add_argument("--bot", default="GreedyBot", choices=sorted(BOT_REGISTRY))
    parser.add_argument("--matches-per-pair", type=int, default=5)
    parser.add_argument("--seed", type=int, default=31)
    parser.add_argument("--output-dir", default=None)
    parser.add_argument("--keep-match-logs", type=int, default=100)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    summary_md, total_matches = run_tournament(
        args.bot,
        args.matches_per_pair,
        args.seed,
        args.output_dir,
        args.keep_match_logs,
    )
    print(summary_md)
    print(f"matches={total_matches}")


def run_tournament(
    bot_name: str,
    matches_per_pair: int,
    seed: int,
    output_dir_override: str | None = None,
    keep_match_logs: int = 100,
) -> tuple[Path, int]:
    cards = load_cards("data/cards.json")
    decks = load_decks("data/decks.json")
    output_dir = Path(
        output_dir_override or f"logs/deck_tournament_{bot_name.lower()}_x{matches_per_pair}_seed{seed}"
    )
    matches_dir = output_dir / "matches"
    matches_dir.mkdir(parents=True, exist_ok=True)

    records: list[dict[str, Any]] = []
    match_index = 1
    deck_ids = sorted(decks)

    for left_index in range(len(deck_ids)):
        for right_index in range(left_index + 1, len(deck_ids)):
            deck_a = deck_ids[left_index]
            deck_b = deck_ids[right_index]
            for repeat in range(matches_per_pair):
                for seat_order, (p1_deck, p2_deck) in enumerate(((deck_a, deck_b), (deck_b, deck_a))):
                    match_id = f"match_{match_index:04d}"
                    match_seed = seed + match_index * 17 + seat_order + repeat
                    runner = MatchRunner(
                        build_bot(bot_name, match_seed),
                        build_bot(bot_name, match_seed + 1),
                        p1_deck,
                        p2_deck,
                        match_id=match_id,
                        seed=match_seed,
                    )
                    result = runner.run()
                    json_path = matches_dir / f"{match_id}_{p1_deck}_vs_{p2_deck}.json"
                    md_path = matches_dir / f"{match_id}_{p1_deck}_vs_{p2_deck}.md"
                    runner.logger.write_json(json_path)
                    md_path.write_text(render_match_log_markdown(result.log), encoding="utf-8")
                    records.append(build_match_record(result.log, md_path.relative_to(output_dir).as_posix()))
                    match_index += 1

    summary = build_tournament_summary(records, cards)
    summary["config"] = {
        "bot": bot_name,
        "matches_per_pair": matches_per_pair,
        "pairing_mode": "unordered pairings with mirrored seats",
        "total_matches": len(records),
        "seed": seed,
    }

    summary_json = output_dir / "summary.json"
    summary_md = output_dir / "summary.md"
    summary_json.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    summary_md.write_text(render_tournament_markdown(summary), encoding="utf-8")
    prune_match_logs(matches_dir, keep_match_logs)
    return summary_md, len(records)


def build_match_record(payload: dict[str, Any], markdown_path: str) -> dict[str, Any]:
    players = payload["players"]
    p1_deck = players["p1"]["deck"]
    p2_deck = players["p2"]["deck"]
    winner_side = payload.get("winner")
    winner_deck = players[winner_side]["deck"] if winner_side else None
    final_turn = payload["turns"][-1]
    battle = final_turn["battle"]

    side_usage = {
        "p1": collect_used_cards(payload, "p1"),
        "p2": collect_used_cards(payload, "p2"),
    }
    decisive_cards = {
        "p1": list(battle.get("p1_cards", [])),
        "p2": list(battle.get("p2_cards", [])),
    }
    action_counts = {
        "p1": collect_action_counts(payload, "p1"),
        "p2": collect_action_counts(payload, "p2"),
    }
    final_stats = {
        "p1": battle.get("p1_final"),
        "p2": battle.get("p2_final"),
    }
    speed_advantage_losses = {
        "p1": lost_with_speed_advantage("p1", winner_side, final_stats),
        "p2": lost_with_speed_advantage("p2", winner_side, final_stats),
    }
    block_then_win = {
        "p1": won_after_blocking_faster_attack("p1", winner_side, final_stats),
        "p2": won_after_blocking_faster_attack("p2", winner_side, final_stats),
    }

    record: dict[str, Any] = {
        "match_id": payload["match_id"],
        "markdown_path": markdown_path,
        "p1_deck": p1_deck,
        "p2_deck": p2_deck,
        "winner_side": winner_side,
        "winner_deck": winner_deck,
        "end_reason": payload.get("end_reason"),
        "turn_count": int(payload.get("turn_count", len(payload.get("turns", [])))),
        "final_turn": int(final_turn["turn"]),
        "battle_result": battle.get("result"),
        "battle": battle,
        "side_usage": side_usage,
        "decisive_cards": decisive_cards,
        "action_counts": action_counts,
        "p1_final_stats": final_stats["p1"],
        "p2_final_stats": final_stats["p2"],
        "starting_player": battle.get("starting_player"),
        "first_pass_player": battle.get("first_pass_player"),
        "first_pass_won": winner_side is not None and battle.get("first_pass_player") == winner_side,
        "starting_player_won": winner_side is not None and battle.get("starting_player") == winner_side,
        "responding_player_won": winner_side is not None and battle.get("starting_player") != winner_side,
        "winner_facedown_count": battle.get("winner_facedown_count"),
        "loser_facedown_count": battle.get("loser_facedown_count"),
        "p1_lost_with_speed_advantage": speed_advantage_losses["p1"],
        "p2_lost_with_speed_advantage": speed_advantage_losses["p2"],
        "p1_block_then_win": block_then_win["p1"],
        "p2_block_then_win": block_then_win["p2"],
        "won_with_fewer_cards": bool(battle.get("won_with_fewer_cards")),
        "won_with_same_cards": bool(battle.get("won_with_same_cards")),
        "won_with_more_cards": bool(battle.get("won_with_more_cards")),
    }
    if winner_side:
        record["winner_final_stats"] = battle[f"{winner_side}_final"]
        record["winner_decisive_cards"] = decisive_cards[winner_side]
        record["winner_used_cards"] = side_usage[winner_side]
    else:
        record["winner_final_stats"] = None
        record["winner_decisive_cards"] = []
        record["winner_used_cards"] = []
    return record


def lost_with_speed_advantage(
    side: str,
    winner_side: str | None,
    final_stats: dict[str, dict[str, int] | None],
) -> bool:
    if winner_side is None or winner_side == side:
        return False
    other = "p2" if side == "p1" else "p1"
    own_final = final_stats.get(side)
    other_final = final_stats.get(other)
    if own_final is None or other_final is None:
        return False
    return own_final["speed"] > other_final["speed"]


def won_after_blocking_faster_attack(
    side: str,
    winner_side: str | None,
    final_stats: dict[str, dict[str, int] | None],
) -> bool:
    if winner_side != side:
        return False
    other = "p2" if side == "p1" else "p1"
    own_final = final_stats.get(side)
    other_final = final_stats.get(other)
    if own_final is None or other_final is None:
        return False
    if own_final["speed"] >= other_final["speed"]:
        return False
    return other_final["attack"] <= own_final["block"] and own_final["attack"] > other_final["block"]


def collect_used_cards(payload: dict[str, Any], side: str) -> list[str]:
    cards: list[str] = []
    for turn in payload.get("turns", []):
        control_card = turn.get("control", {}).get(side)
        if control_card:
            cards.append(control_card)
        battle_cards = turn.get("battle", {}).get(f"{side}_cards", [])
        cards.extend(battle_cards)
    return cards


def collect_action_counts(payload: dict[str, Any], side: str) -> Counter[str]:
    counts: Counter[str] = Counter()
    for turn in payload.get("turns", []):
        for action in turn.get("battle", {}).get("actions", []):
            if action.get("player_id") == side:
                counts[action.get("action_type", "unknown")] += 1
    return counts


def build_tournament_summary(records: list[dict[str, Any]], cards: dict[str, Any]) -> dict[str, Any]:
    deck_stats: dict[str, dict[str, Any]] = {}
    pair_stats: dict[str, dict[str, Any]] = {}
    card_stats: dict[str, dict[str, Any]] = {
        card.name: {
            "id": card.id,
            "type": card.type,
            "usage_count": 0,
            "usage_match_count": 0,
            "winner_usage_count": 0,
            "winner_match_count": 0,
            "lethal_count": 0,
        }
        for card in cards.values()
    }

    all_decks = sorted({record["p1_deck"] for record in records} | {record["p2_deck"] for record in records})
    for deck_id in all_decks:
        deck_stats[deck_id] = {
            "matches": 0,
            "wins": 0,
            "losses": 0,
            "draws": 0,
            "turn_counts": [],
            "final_attack": [],
            "final_block": [],
            "final_speed": [],
            "winning_attack": [],
            "winning_block": [],
            "winning_speed": [],
            "losing_attack": [],
            "losing_block": [],
            "losing_speed": [],
            "used_cards": Counter(),
            "winning_used_cards": Counter(),
            "lethal_cards": Counter(),
            "action_counts": Counter(),
            "first_pass_matches": 0,
            "first_pass_wins": 0,
            "starting_player_matches": 0,
            "starting_player_wins": 0,
            "responding_player_matches": 0,
            "responding_player_wins": 0,
            "wins_with_fewer_cards": 0,
            "wins_with_same_cards": 0,
            "wins_with_more_cards": 0,
            "speed_advantage_losses": 0,
            "block_then_win_matches": 0,
            "winning_facedown_counts": [],
            "losing_facedown_counts": [],
            "match_links": [],
        }

    for record in records:
        for deck_id, side in ((record["p1_deck"], "p1"), (record["p2_deck"], "p2")):
            stats = deck_stats[deck_id]
            stats["matches"] += 1
            stats["turn_counts"].append(record["turn_count"])
            stats["used_cards"].update(record["side_usage"][side])
            stats["action_counts"].update(record["action_counts"][side])
            if record[f"{side}_final_stats"] is not None:
                stats["final_attack"].append(record[f"{side}_final_stats"]["attack"])
                stats["final_block"].append(record[f"{side}_final_stats"]["block"])
                stats["final_speed"].append(record[f"{side}_final_stats"]["speed"])
            stats["match_links"].append((record["match_id"], record["markdown_path"]))
            if record["first_pass_player"] == side:
                stats["first_pass_matches"] += 1
                if record["winner_side"] == side:
                    stats["first_pass_wins"] += 1
            if record["starting_player"] == side:
                stats["starting_player_matches"] += 1
                if record["winner_side"] == side:
                    stats["starting_player_wins"] += 1
            else:
                stats["responding_player_matches"] += 1
                if record["winner_side"] == side:
                    stats["responding_player_wins"] += 1
            stats["speed_advantage_losses"] += int(record[f"{side}_lost_with_speed_advantage"])
            stats["block_then_win_matches"] += int(record[f"{side}_block_then_win"])

        if record["winner_side"] is None:
            deck_stats[record["p1_deck"]]["draws"] += 1
            deck_stats[record["p2_deck"]]["draws"] += 1
        else:
            loser_deck = record["p2_deck"] if record["winner_side"] == "p1" else record["p1_deck"]
            winner_deck = record["winner_deck"]
            winner_stats = deck_stats[winner_deck]
            loser_stats = deck_stats[loser_deck]
            winner_stats["wins"] += 1
            loser_stats["losses"] += 1
            final_stats = record["winner_final_stats"]
            winner_stats["winning_attack"].append(final_stats["attack"])
            winner_stats["winning_block"].append(final_stats["block"])
            winner_stats["winning_speed"].append(final_stats["speed"])
            winner_stats["winning_used_cards"].update(record["winner_used_cards"])
            winner_stats["lethal_cards"].update(record["winner_decisive_cards"])
            winner_stats["wins_with_fewer_cards"] += int(record["won_with_fewer_cards"])
            winner_stats["wins_with_same_cards"] += int(record["won_with_same_cards"])
            winner_stats["wins_with_more_cards"] += int(record["won_with_more_cards"])
            if record["winner_facedown_count"] is not None:
                winner_stats["winning_facedown_counts"].append(record["winner_facedown_count"])
            if record["loser_facedown_count"] is not None:
                loser_stats["losing_facedown_counts"].append(record["loser_facedown_count"])
            if record["p1_final_stats"] is not None and record["winner_side"] == "p2":
                deck_stats[record["p1_deck"]]["losing_attack"].append(record["p1_final_stats"]["attack"])
                deck_stats[record["p1_deck"]]["losing_block"].append(record["p1_final_stats"]["block"])
                deck_stats[record["p1_deck"]]["losing_speed"].append(record["p1_final_stats"]["speed"])
            if record["p2_final_stats"] is not None and record["winner_side"] == "p1":
                deck_stats[record["p2_deck"]]["losing_attack"].append(record["p2_final_stats"]["attack"])
                deck_stats[record["p2_deck"]]["losing_block"].append(record["p2_final_stats"]["block"])
                deck_stats[record["p2_deck"]]["losing_speed"].append(record["p2_final_stats"]["speed"])

        pair_key = " vs ".join(sorted((record["p1_deck"], record["p2_deck"])))
        if pair_key not in pair_stats:
            pair_stats[pair_key] = {
                "decks": sorted((record["p1_deck"], record["p2_deck"])),
                "matches": 0,
                "turn_counts": [],
                "wins": defaultdict(int),
                "draws": 0,
            }
        pair = pair_stats[pair_key]
        pair["matches"] += 1
        pair["turn_counts"].append(record["turn_count"])
        if record["winner_deck"] is None:
            pair["draws"] += 1
        else:
            pair["wins"][record["winner_deck"]] += 1

        seen_in_match: set[str] = set()
        seen_in_winner_match: set[str] = set()
        for side in ("p1", "p2"):
            for card_name in record["side_usage"][side]:
                card_stats[card_name]["usage_count"] += 1
                seen_in_match.add(card_name)
        if record["winner_side"] is not None:
            for card_name in record["winner_used_cards"]:
                card_stats[card_name]["winner_usage_count"] += 1
                seen_in_winner_match.add(card_name)
            for card_name in record["winner_decisive_cards"]:
                card_stats[card_name]["lethal_count"] += 1
        for card_name in seen_in_match:
            card_stats[card_name]["usage_match_count"] += 1
        for card_name in seen_in_winner_match:
            card_stats[card_name]["winner_match_count"] += 1

    return {
        "decks": {deck_id: finalize_deck_stats(deck_id, stats) for deck_id, stats in deck_stats.items()},
        "pairs": {pair_key: finalize_pair_stats(pair_key, stats) for pair_key, stats in pair_stats.items()},
        "cards": finalize_card_stats(card_stats),
    }


def finalize_deck_stats(deck_id: str, stats: dict[str, Any]) -> dict[str, Any]:
    matches = stats["matches"] or 1
    wins = stats["wins"]
    total_actions = sum(stats["action_counts"].values()) or 1
    first_pass_matches = stats["first_pass_matches"]
    starting_player_matches = stats["starting_player_matches"]
    responding_player_matches = stats["responding_player_matches"]
    return {
        "deck_id": deck_id,
        "matches": stats["matches"],
        "wins": stats["wins"],
        "losses": stats["losses"],
        "draws": stats["draws"],
        "win_rate": stats["wins"] / matches,
        "draw_rate": stats["draws"] / matches,
        "turns": summarize_numbers(stats["turn_counts"]),
        "final_attack": summarize_numbers(stats["final_attack"]),
        "final_block": summarize_numbers(stats["final_block"]),
        "final_speed": summarize_numbers(stats["final_speed"]),
        "winning_attack": summarize_numbers(stats["winning_attack"]),
        "winning_block": summarize_numbers(stats["winning_block"]),
        "winning_speed": summarize_numbers(stats["winning_speed"]),
        "losing_attack": summarize_numbers(stats["losing_attack"]),
        "losing_block": summarize_numbers(stats["losing_block"]),
        "losing_speed": summarize_numbers(stats["losing_speed"]),
        "winning_facedown": summarize_numbers(stats["winning_facedown_counts"]),
        "losing_facedown": summarize_numbers(stats["losing_facedown_counts"]),
        "first_pass_matches": first_pass_matches,
        "first_pass_win_rate": stats["first_pass_wins"] / first_pass_matches if first_pass_matches else None,
        "starting_player_matches": starting_player_matches,
        "starting_player_win_rate": stats["starting_player_wins"] / starting_player_matches if starting_player_matches else None,
        "responding_player_matches": responding_player_matches,
        "responding_player_win_rate": stats["responding_player_wins"] / responding_player_matches if responding_player_matches else None,
        "fewer_card_win_rate": (stats["wins_with_fewer_cards"] / wins) if wins else None,
        "same_card_win_rate": (stats["wins_with_same_cards"] / wins) if wins else None,
        "more_card_win_rate": (stats["wins_with_more_cards"] / wins) if wins else None,
        "speed_advantage_losses": stats["speed_advantage_losses"],
        "speed_advantage_loss_rate": stats["speed_advantage_losses"] / matches,
        "block_then_win_matches": stats["block_then_win_matches"],
        "block_then_win_rate": (stats["block_then_win_matches"] / wins) if wins else None,
        "action_counts": dict(stats["action_counts"]),
        "action_rates": {
            "set": stats["action_counts"].get("set", 0) / total_actions,
            "set_pass": stats["action_counts"].get("set_pass", 0) / total_actions,
            "pass": stats["action_counts"].get("pass", 0) / total_actions,
        },
        "most_used_cards": stats["used_cards"].most_common(10),
        "winner_side_cards": stats["winning_used_cards"].most_common(10),
        "lethal_cards": stats["lethal_cards"].most_common(10),
        "match_links": stats["match_links"],
    }


def finalize_pair_stats(pair_key: str, stats: dict[str, Any]) -> dict[str, Any]:
    return {
        "pair_key": pair_key,
        "decks": stats["decks"],
        "matches": stats["matches"],
        "draws": stats["draws"],
        "wins": dict(stats["wins"]),
        "turns": summarize_numbers(stats["turn_counts"]),
    }


def finalize_card_stats(card_stats: dict[str, dict[str, Any]]) -> dict[str, Any]:
    sorted_items = sorted(
        card_stats.items(),
        key=lambda item: (
            -item[1]["usage_count"],
            -item[1]["winner_usage_count"],
            -item[1]["lethal_count"],
            item[0],
        ),
    )
    effective_items = sorted(
        card_stats.items(),
        key=lambda item: (
            -item[1]["winner_usage_count"],
            -item[1]["winner_match_count"],
            -item[1]["lethal_count"],
            item[0],
        ),
    )
    lethal_items = sorted(
        card_stats.items(),
        key=lambda item: (-item[1]["lethal_count"], -item[1]["winner_usage_count"], item[0]),
    )
    return {
        "all": {name: payload for name, payload in sorted_items},
        "most_used": [(name, payload["usage_count"]) for name, payload in sorted_items[:15]],
        "most_effective": [(name, payload["winner_usage_count"]) for name, payload in effective_items[:15]],
        "most_lethal": [(name, payload["lethal_count"]) for name, payload in lethal_items[:15]],
    }


def summarize_numbers(values: list[int]) -> dict[str, float | int | None]:
    if not values:
        return {"min": None, "avg": None, "max": None}
    return {
        "min": min(values),
        "avg": round(mean(values), 2),
        "max": max(values),
    }


def render_tournament_markdown(summary: dict[str, Any]) -> str:
    config = summary["config"]
    lines = [
        "# Deck Tournament Report",
        "",
        "## Configuration",
        "",
        f"- Bot: `{config['bot']}`",
        f"- Matches Per Pair: {config['matches_per_pair']}",
        f"- Pairing Mode: {config['pairing_mode']}",
        f"- Total Matches: {config['total_matches']}",
        f"- Seed: {config['seed']}",
        "",
        "## Deck Summary",
        "",
        "| Deck | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Winner Set Avg | Loser Set Avg | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate | Turn Min | Turn Avg | Turn Max |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for deck_id, stats in sorted(summary["decks"].items()):
        lines.append(
            f"| `{deck_id}` | {stats['matches']} | {stats['wins']} | {stats['losses']} | {stats['draws']} | {format_rate(stats['win_rate'])} | "
            f"{format_optional_rate(stats['first_pass_win_rate'])} | {format_optional_rate(stats['fewer_card_win_rate'])} | "
            f"{format_optional_rate(stats['same_card_win_rate'])} | {format_optional_rate(stats['more_card_win_rate'])} | "
            f"{fmt(stats['winning_facedown']['avg'])} | {fmt(stats['losing_facedown']['avg'])} | "
            f"{format_optional_rate(stats['starting_player_win_rate'])} | {format_optional_rate(stats['responding_player_win_rate'])} | "
            f"{format_rate(stats['action_rates']['set'])} | {format_rate(stats['action_rates']['set_pass'])} | {format_rate(stats['action_rates']['pass'])} | "
            f"{fmt(stats['turns']['min'])} | {fmt(stats['turns']['avg'])} | {fmt(stats['turns']['max'])} |"
        )

    lines.extend(["", "## Pair Summary", "", "| Pair | Matches | Draws | Wins | Turn Min | Turn Avg | Turn Max |", "|---|---:|---:|---|---:|---:|---:|"])
    for pair_key, stats in sorted(summary["pairs"].items()):
        wins_text = ", ".join(f"`{deck}`={count}" for deck, count in sorted(stats["wins"].items()))
        lines.append(
            f"| {pair_key} | {stats['matches']} | {stats['draws']} | {wins_text or '-'} | {fmt(stats['turns']['min'])} | {fmt(stats['turns']['avg'])} | {fmt(stats['turns']['max'])} |"
        )

    lines.extend(["", "## Card Highlights", ""])
    lines.extend(render_rank_table("Most Used Cards", summary["cards"]["most_used"]))
    lines.append("")
    lines.extend(render_rank_table("Most Effective Cards", summary["cards"]["most_effective"]))
    lines.append("")
    lines.extend(render_rank_table("Most Lethal Cards", summary["cards"]["most_lethal"]))
    lines.append("")
    lines.append("## Deck Details")
    lines.append("")

    for deck_id, stats in sorted(summary["decks"].items()):
        lines.extend(
            [
                f"### {deck_id}",
                "",
                f"- Win Rate: {format_rate(stats['win_rate'])}",
                f"- Draw Rate: {format_rate(stats['draw_rate'])}",
                f"- First Pass Win Rate: {format_optional_rate(stats['first_pass_win_rate'])}",
                f"- Win With Fewer Cards: {format_optional_rate(stats['fewer_card_win_rate'])}",
                f"- Win With Same Cards: {format_optional_rate(stats['same_card_win_rate'])}",
                f"- Win With More Cards: {format_optional_rate(stats['more_card_win_rate'])}",
                f"- Winner Facedown Avg: {fmt(stats['winning_facedown']['avg'])}",
                f"- Loser Facedown Avg: {fmt(stats['losing_facedown']['avg'])}",
                f"- Starting Player Win Rate: {format_optional_rate(stats['starting_player_win_rate'])}",
                f"- Responding Player Win Rate: {format_optional_rate(stats['responding_player_win_rate'])}",
                f"- Final Stats Avg: A={fmt(stats['final_attack']['avg'])}, B={fmt(stats['final_block']['avg'])}, S={fmt(stats['final_speed']['avg'])}",
                f"- Losing Final Stats Avg: A={fmt(stats['losing_attack']['avg'])}, B={fmt(stats['losing_block']['avg'])}, S={fmt(stats['losing_speed']['avg'])}",
                f"- Lost With Speed Advantage: {stats['speed_advantage_losses']} ({format_rate(stats['speed_advantage_loss_rate'])})",
                f"- Won After Blocking Faster Attack: {stats['block_then_win_matches']} ({format_optional_rate(stats['block_then_win_rate'])})",
                f"- Action Rates: set={format_rate(stats['action_rates']['set'])}, set_pass={format_rate(stats['action_rates']['set_pass'])}, pass={format_rate(stats['action_rates']['pass'])}",
                f"- Turn Stats: min={fmt(stats['turns']['min'])}, avg={fmt(stats['turns']['avg'])}, max={fmt(stats['turns']['max'])}",
                f"- Winning Attack Stats: min={fmt(stats['winning_attack']['min'])}, avg={fmt(stats['winning_attack']['avg'])}, max={fmt(stats['winning_attack']['max'])}",
                f"- Winning Block Stats: min={fmt(stats['winning_block']['min'])}, avg={fmt(stats['winning_block']['avg'])}, max={fmt(stats['winning_block']['max'])}",
                f"- Winning Speed Stats: min={fmt(stats['winning_speed']['min'])}, avg={fmt(stats['winning_speed']['avg'])}, max={fmt(stats['winning_speed']['max'])}",
                "",
            ]
        )
        lines.extend(render_rank_table("Most Used", stats["most_used_cards"]))
        lines.append("")
        lines.extend(render_rank_table("Winner Side Usage", stats["winner_side_cards"]))
        lines.append("")
        lines.extend(render_rank_table("Lethal Cards", stats["lethal_cards"]))
        lines.append("")
        lines.append("#### Match Logs")
        lines.append("")
        for match_id, match_path in stats["match_links"]:
            lines.append(f"- [{match_id}]({match_path})")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_rank_table(title: str, items: list[tuple[str, int]]) -> list[str]:
    lines = [f"### {title}", "", "| Rank | Card | Count |", "|---:|---|---:|"]
    for index, (name, count) in enumerate(items[:15], start=1):
        lines.append(f"| {index} | {name} | {count} |")
    if not items:
        lines.append("| 1 | - | 0 |")
    return lines


def format_rate(value: float) -> str:
    return f"{value * 100:.1f}%"


def format_optional_rate(value: float | None) -> str:
    return "-" if value is None else format_rate(value)


def fmt(value: float | int | None) -> str:
    return "-" if value is None else str(value)


if __name__ == "__main__":
    main()
