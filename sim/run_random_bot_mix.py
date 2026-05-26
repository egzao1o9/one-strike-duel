from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import random
from statistics import mean
from typing import Any

from bots.registry import BOT_REGISTRY, build_bot
from engine.card import load_cards
from engine.deck import load_decks
from engine.log_formatter import render_match_log_markdown
from engine.phase_runner import MatchRunner
from sim.log_retention import prune_match_logs
from sim.run_deck_tournament import build_match_record, finalize_card_stats, summarize_numbers


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run random mixed-bot matches and generate bot win-rate reports.")
    parser.add_argument("--matches", type=int, default=200)
    parser.add_argument("--seed", type=int, default=101)
    parser.add_argument("--output-dir", default=None)
    parser.add_argument("--keep-match-logs", type=int, default=100)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    summary_md, total_matches = run_random_bot_mix(args.matches, args.seed, args.output_dir, args.keep_match_logs)
    print(summary_md)
    print(f"matches={total_matches}")


def run_random_bot_mix(
    matches: int,
    seed: int,
    output_dir_override: str | None = None,
    keep_match_logs: int = 100,
) -> tuple[Path, int]:
    rng = random.Random(seed)
    cards = load_cards("data/cards.json")
    decks = load_decks("data/decks.json")
    bot_names = sorted(BOT_REGISTRY)
    deck_ids = sorted(decks)

    output_dir = Path(output_dir_override or f"logs/random_bot_mix_{matches}_seed{seed}")
    matches_dir = output_dir / "matches"
    matches_dir.mkdir(parents=True, exist_ok=True)

    records: list[dict[str, Any]] = []
    selections: list[dict[str, str]] = []

    for index in range(1, matches + 1):
        match_id = f"match_{index:04d}"
        p1_bot = rng.choice(bot_names)
        p2_bot = rng.choice(bot_names)
        p1_deck = rng.choice(deck_ids)
        p2_deck = rng.choice(deck_ids)
        match_seed = seed + index * 37

        runner = MatchRunner(
            build_bot(p1_bot, match_seed),
            build_bot(p2_bot, match_seed + 1),
            p1_deck,
            p2_deck,
            match_id=match_id,
            seed=match_seed,
        )
        result = runner.run()
        json_path = matches_dir / f"{match_id}_{p1_bot}_{p1_deck}_vs_{p2_bot}_{p2_deck}.json"
        md_path = matches_dir / f"{match_id}_{p1_bot}_{p1_deck}_vs_{p2_bot}_{p2_deck}.md"
        runner.logger.write_json(json_path)
        md_path.write_text(render_match_log_markdown(result.log), encoding="utf-8")

        record = build_match_record(result.log, md_path.relative_to(output_dir).as_posix())
        record["p1_bot"] = p1_bot
        record["p2_bot"] = p2_bot
        records.append(record)
        selections.append({"p1_bot": p1_bot, "p2_bot": p2_bot, "p1_deck": p1_deck, "p2_deck": p2_deck})

    summary = build_random_mix_summary(records, cards, bot_names, deck_ids)
    summary["config"] = {
        "matches": matches,
        "seed": seed,
        "bot_pool": bot_names,
        "deck_pool": deck_ids,
        "selection_mode": "p1/p2 bot and deck selected independently at random",
    }
    summary["selections"] = selections

    summary_json = output_dir / "summary.json"
    summary_md = output_dir / "summary.md"
    summary_json.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    summary_md.write_text(render_random_mix_markdown(summary), encoding="utf-8")
    prune_match_logs(matches_dir, keep_match_logs)
    return summary_md, len(records)


def build_random_mix_summary(
    records: list[dict[str, Any]],
    cards: dict[str, Any],
    bot_names: list[str],
    deck_ids: list[str],
) -> dict[str, Any]:
    bot_stats: dict[str, dict[str, Any]] = {}
    bot_pair_stats: dict[str, dict[str, Any]] = {}
    deck_stats: dict[str, dict[str, Any]] = {deck_id: {"matches": 0, "wins": 0, "draws": 0} for deck_id in deck_ids}
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

    for bot_name in bot_names:
        bot_stats[bot_name] = {
            "matches": 0,
            "wins": 0,
            "losses": 0,
            "draws": 0,
            "turn_counts": [],
            "winning_attack": [],
            "winning_block": [],
            "winning_speed": [],
            "deck_usage": Counter(),
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
            "winning_facedown_counts": [],
            "losing_facedown_counts": [],
            "match_links": [],
        }

    for record in records:
        for side in ("p1", "p2"):
            bot_name = record[f"{side}_bot"]
            deck_id = record[f"{side}_deck"]
            bot = bot_stats[bot_name]
            bot["matches"] += 1
            bot["turn_counts"].append(record["turn_count"])
            bot["deck_usage"][deck_id] += 1
            bot["used_cards"].update(record["side_usage"][side])
            bot["action_counts"].update(record["action_counts"][side])
            bot["match_links"].append((record["match_id"], record["markdown_path"]))
            deck_stats[deck_id]["matches"] += 1
            if record["first_pass_player"] == side:
                bot["first_pass_matches"] += 1
                if record["winner_side"] == side:
                    bot["first_pass_wins"] += 1
            if record["starting_player"] == side:
                bot["starting_player_matches"] += 1
                if record["winner_side"] == side:
                    bot["starting_player_wins"] += 1
            else:
                bot["responding_player_matches"] += 1
                if record["winner_side"] == side:
                    bot["responding_player_wins"] += 1

        if record["winner_side"] is None:
            bot_stats[record["p1_bot"]]["draws"] += 1
            bot_stats[record["p2_bot"]]["draws"] += 1
            deck_stats[record["p1_deck"]]["draws"] += 1
            deck_stats[record["p2_deck"]]["draws"] += 1
        else:
            winner_side = record["winner_side"]
            loser_side = "p2" if winner_side == "p1" else "p1"
            winner_bot = bot_stats[record[f"{winner_side}_bot"]]
            loser_bot = bot_stats[record[f"{loser_side}_bot"]]
            winner_bot["wins"] += 1
            loser_bot["losses"] += 1
            final_stats = record["winner_final_stats"]
            winner_bot["winning_attack"].append(final_stats["attack"])
            winner_bot["winning_block"].append(final_stats["block"])
            winner_bot["winning_speed"].append(final_stats["speed"])
            winner_bot["winning_used_cards"].update(record["winner_used_cards"])
            winner_bot["lethal_cards"].update(record["winner_decisive_cards"])
            winner_bot["wins_with_fewer_cards"] += int(record["won_with_fewer_cards"])
            winner_bot["wins_with_same_cards"] += int(record["won_with_same_cards"])
            winner_bot["wins_with_more_cards"] += int(record["won_with_more_cards"])
            if record["winner_facedown_count"] is not None:
                winner_bot["winning_facedown_counts"].append(record["winner_facedown_count"])
            if record["loser_facedown_count"] is not None:
                loser_bot["losing_facedown_counts"].append(record["loser_facedown_count"])
            deck_stats[record[f"{winner_side}_deck"]]["wins"] += 1

        pair_key = " vs ".join(sorted((record["p1_bot"], record["p2_bot"])))
        if pair_key not in bot_pair_stats:
            bot_pair_stats[pair_key] = {
                "bots": sorted((record["p1_bot"], record["p2_bot"])),
                "matches": 0,
                "draws": 0,
                "wins": defaultdict(int),
                "turn_counts": [],
            }
        pair = bot_pair_stats[pair_key]
        pair["matches"] += 1
        pair["turn_counts"].append(record["turn_count"])
        if record["winner_side"] is None:
            pair["draws"] += 1
        else:
            pair["wins"][record[f"{record['winner_side']}_bot"]] += 1

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
        "bots": {bot_name: finalize_bot_stats(bot_name, stats) for bot_name, stats in bot_stats.items()},
        "bot_pairs": {pair_key: finalize_bot_pair_stats(pair_key, stats) for pair_key, stats in bot_pair_stats.items()},
        "decks": finalize_random_deck_stats(deck_stats),
        "cards": finalize_card_stats(card_stats),
    }


def finalize_bot_stats(bot_name: str, stats: dict[str, Any]) -> dict[str, Any]:
    matches = stats["matches"] or 1
    wins = stats["wins"]
    total_actions = sum(stats["action_counts"].values()) or 1
    first_pass_matches = stats["first_pass_matches"]
    starting_player_matches = stats["starting_player_matches"]
    responding_player_matches = stats["responding_player_matches"]
    return {
        "bot": bot_name,
        "matches": stats["matches"],
        "wins": stats["wins"],
        "losses": stats["losses"],
        "draws": stats["draws"],
        "win_rate": stats["wins"] / matches,
        "draw_rate": stats["draws"] / matches,
        "turns": summarize_numbers(stats["turn_counts"]),
        "winning_attack": summarize_numbers(stats["winning_attack"]),
        "winning_block": summarize_numbers(stats["winning_block"]),
        "winning_speed": summarize_numbers(stats["winning_speed"]),
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
        "action_counts": dict(stats["action_counts"]),
        "action_rates": {
            "set": stats["action_counts"].get("set", 0) / total_actions,
            "set_pass": stats["action_counts"].get("set_pass", 0) / total_actions,
            "pass": stats["action_counts"].get("pass", 0) / total_actions,
        },
        "deck_usage": stats["deck_usage"].most_common(),
        "most_used_cards": stats["used_cards"].most_common(10),
        "winner_side_cards": stats["winning_used_cards"].most_common(10),
        "lethal_cards": stats["lethal_cards"].most_common(10),
        "match_links": stats["match_links"],
    }


def finalize_bot_pair_stats(pair_key: str, stats: dict[str, Any]) -> dict[str, Any]:
    return {
        "pair_key": pair_key,
        "bots": stats["bots"],
        "matches": stats["matches"],
        "draws": stats["draws"],
        "wins": dict(stats["wins"]),
        "turns": summarize_numbers(stats["turn_counts"]),
    }


def finalize_random_deck_stats(deck_stats: dict[str, dict[str, Any]]) -> dict[str, Any]:
    finalized: dict[str, Any] = {}
    for deck_id, stats in deck_stats.items():
        matches = stats["matches"] or 1
        finalized[deck_id] = {
            "deck_id": deck_id,
            "matches": stats["matches"],
            "wins": stats["wins"],
            "draws": stats["draws"],
            "win_rate": stats["wins"] / matches,
            "draw_rate": stats["draws"] / matches,
        }
    return finalized


def render_random_mix_markdown(summary: dict[str, Any]) -> str:
    config = summary["config"]
    lines = [
        "# Random Bot Mix Report",
        "",
        "## Configuration",
        "",
        f"- Matches: {config['matches']}",
        f"- Seed: {config['seed']}",
        f"- Selection Mode: {config['selection_mode']}",
        f"- Bot Pool: {', '.join(f'`{name}`' for name in config['bot_pool'])}",
        f"- Deck Pool: {', '.join(f'`{name}`' for name in config['deck_pool'])}",
        "",
        "## Bot Win Rates",
        "",
        "| Bot | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Winner Set Avg | Loser Set Avg | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate | Turn Min | Turn Avg | Turn Max | Win A Avg | Win B Avg | Win S Avg |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for bot_name, stats in sorted(summary["bots"].items()):
        lines.append(
            f"| `{bot_name}` | {stats['matches']} | {stats['wins']} | {stats['losses']} | {stats['draws']} | {format_rate(stats['win_rate'])} | "
            f"{format_optional_rate(stats['first_pass_win_rate'])} | {format_optional_rate(stats['fewer_card_win_rate'])} | "
            f"{format_optional_rate(stats['same_card_win_rate'])} | {format_optional_rate(stats['more_card_win_rate'])} | "
            f"{fmt(stats['winning_facedown']['avg'])} | {fmt(stats['losing_facedown']['avg'])} | "
            f"{format_optional_rate(stats['starting_player_win_rate'])} | {format_optional_rate(stats['responding_player_win_rate'])} | "
            f"{format_rate(stats['action_rates']['set'])} | {format_rate(stats['action_rates']['set_pass'])} | {format_rate(stats['action_rates']['pass'])} | "
            f"{fmt(stats['turns']['min'])} | {fmt(stats['turns']['avg'])} | {fmt(stats['turns']['max'])} | "
            f"{fmt(stats['winning_attack']['avg'])} | {fmt(stats['winning_block']['avg'])} | {fmt(stats['winning_speed']['avg'])} |"
        )

    lines.extend(["", "## Bot Pair Summary", "", "| Pair | Matches | Draws | Wins | Turn Min | Turn Avg | Turn Max |", "|---|---:|---:|---|---:|---:|---:|"])
    for pair_key, stats in sorted(summary["bot_pairs"].items()):
        wins_text = ", ".join(f"`{bot}`={count}" for bot, count in sorted(stats["wins"].items()))
        lines.append(
            f"| {pair_key} | {stats['matches']} | {stats['draws']} | {wins_text or '-'} | {fmt(stats['turns']['min'])} | {fmt(stats['turns']['avg'])} | {fmt(stats['turns']['max'])} |"
        )

    lines.extend(["", "## Deck Usage Summary", "", "| Deck | Matches | Wins | Draws | Win Rate |", "|---|---:|---:|---:|---:|"])
    for deck_id, stats in sorted(summary["decks"].items()):
        lines.append(
            f"| `{deck_id}` | {stats['matches']} | {stats['wins']} | {stats['draws']} | {format_rate(stats['win_rate'])} |"
        )

    lines.extend(["", "## Card Highlights", ""])
    lines.extend(render_rank_table("Most Used Cards", summary["cards"]["most_used"]))
    lines.append("")
    lines.extend(render_rank_table("Most Effective Cards", summary["cards"]["most_effective"]))
    lines.append("")
    lines.extend(render_rank_table("Most Lethal Cards", summary["cards"]["most_lethal"]))
    lines.append("")
    lines.append("## Bot Details")
    lines.append("")

    for bot_name, stats in sorted(summary["bots"].items()):
        lines.extend(
            [
                f"### {bot_name}",
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
                f"- Action Rates: set={format_rate(stats['action_rates']['set'])}, set_pass={format_rate(stats['action_rates']['set_pass'])}, pass={format_rate(stats['action_rates']['pass'])}",
                f"- Turn Stats: min={fmt(stats['turns']['min'])}, avg={fmt(stats['turns']['avg'])}, max={fmt(stats['turns']['max'])}",
                f"- Winning Attack Stats: min={fmt(stats['winning_attack']['min'])}, avg={fmt(stats['winning_attack']['avg'])}, max={fmt(stats['winning_attack']['max'])}",
                f"- Winning Block Stats: min={fmt(stats['winning_block']['min'])}, avg={fmt(stats['winning_block']['avg'])}, max={fmt(stats['winning_block']['max'])}",
                f"- Winning Speed Stats: min={fmt(stats['winning_speed']['min'])}, avg={fmt(stats['winning_speed']['avg'])}, max={fmt(stats['winning_speed']['max'])}",
                "",
            ]
        )
        lines.extend(render_rank_table("Deck Usage", stats["deck_usage"]))
        lines.append("")
        lines.extend(render_rank_table("Most Used", stats["most_used_cards"]))
        lines.append("")
        lines.extend(render_rank_table("Winner Side Usage", stats["winner_side_cards"]))
        lines.append("")
        lines.extend(render_rank_table("Lethal Cards", stats["lethal_cards"]))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_rank_table(title: str, items: list[tuple[str, int]]) -> list[str]:
    lines = [f"### {title}", "", "| Rank | Name | Count |", "|---:|---|---:|"]
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
