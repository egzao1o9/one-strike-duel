from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import random
from statistics import mean
from typing import Any

from bots.registry import BOT_REGISTRY, build_bot
from draft.registry import DRAFT_BOT_REGISTRY, build_draft_bot
from engine.card import load_cards
from engine.card_pool import load_card_pool
from engine.drafting import draft_with_bots, summarize_deck
from engine.log_formatter import render_match_log_markdown
from engine.phase_runner import MatchRunner
from sim.log_retention import prune_match_logs
from sim.run_deck_tournament import build_match_record, finalize_card_stats, summarize_numbers
from sim.run_draft_match import build_draft_payload, render_draft_match_markdown


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run mirrored draft matches and generate public-info draft reports.")
    parser.add_argument("--draft-bot1", default="StandardDraftBot", choices=sorted(DRAFT_BOT_REGISTRY))
    parser.add_argument("--draft-bot2", default="GuardDraftBot", choices=sorted(DRAFT_BOT_REGISTRY))
    parser.add_argument("--bot1", default="StandardBot", choices=sorted(BOT_REGISTRY))
    parser.add_argument("--bot2", default="StandardBot", choices=sorted(BOT_REGISTRY))
    parser.add_argument("--rounds", type=int, default=25)
    parser.add_argument("--seed", type=int, default=131)
    parser.add_argument("--cards", default="data/cards.json")
    parser.add_argument("--pool", default="data/card_pool.json")
    parser.add_argument("--draft-mode", choices=("simple", "full"), default="simple")
    parser.add_argument("--output-dir", default=None)
    parser.add_argument("--keep-match-logs", type=int, default=100)
    parser.add_argument("--fast-report", action="store_true")
    parser.add_argument("--lean-draft-logging", action="store_true")
    parser.add_argument("--save-battle-logs", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    summary_md, total_matches = run_draft_report(
        args.draft_bot1,
        args.draft_bot2,
        args.bot1,
        args.bot2,
        args.rounds,
        args.seed,
        args.cards,
        args.pool,
        args.draft_mode,
        args.output_dir,
        args.keep_match_logs,
        args.fast_report,
        args.lean_draft_logging,
        args.save_battle_logs,
    )
    print(summary_md)
    print(f"matches={total_matches}")


def run_draft_report(
    draft_bot1_name: str,
    draft_bot2_name: str,
    bot1_name: str,
    bot2_name: str,
    rounds: int,
    seed: int,
    cards_path: str = "data/cards.json",
    pool_path: str = "data/card_pool.json",
    draft_mode: str = "simple",
    output_dir_override: str | None = None,
    keep_match_logs: int = 100,
    fast_report: bool = False,
    lean_draft_logging: bool = False,
    save_battle_logs: bool = False,
) -> tuple[Path, int]:
    output_dir = Path(
        output_dir_override
        or f"logs/draft_report_{draft_bot1_name.lower()}_vs_{draft_bot2_name.lower()}_{bot1_name.lower()}_{bot2_name.lower()}_r{rounds}_seed{seed}"
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    matches_dir = output_dir / "matches"
    if not fast_report or save_battle_logs:
        matches_dir.mkdir(parents=True, exist_ok=True)

    chunk_result = run_draft_report_chunk(
        draft_bot1_name=draft_bot1_name,
        draft_bot2_name=draft_bot2_name,
        bot1_name=bot1_name,
        bot2_name=bot2_name,
        round_start=1,
        round_end=rounds,
        seed=seed,
        cards_path=cards_path,
        pool_path=pool_path,
        draft_mode=draft_mode,
        output_dir=output_dir.as_posix(),
        fast_report=fast_report,
        lean_draft_logging=lean_draft_logging,
        save_battle_logs=save_battle_logs,
    )
    cards = load_cards(cards_path)
    pool = load_card_pool(pool_path, cards)
    records = chunk_result["records"]
    draft_records = chunk_result["draft_records"]
    exported_match_records = sorted(chunk_result["exported_match_records"], key=lambda item: item["match_id"])

    summary = build_draft_summary(records, cards, [draft_bot1_name, draft_bot2_name])
    summary["config"] = {
        "draft_bot1": draft_bot1_name,
        "draft_bot2": draft_bot2_name,
        "bot1": bot1_name,
        "bot2": bot2_name,
        "rounds": rounds,
        "total_matches": len(records),
        "seed": seed,
        "pool_id": pool.id,
        "pool_total_cards": pool.total_cards,
        "pairing_mode": "mirrored seats per round",
        "draft_mode": draft_mode,
        "fast_report": fast_report,
        "lean_draft_logging": lean_draft_logging,
        "save_battle_logs": save_battle_logs,
    }
    if not lean_draft_logging:
        summary["draft_records"] = draft_records

    summary_json = output_dir / "summary.json"
    summary_md = output_dir / "summary.md"
    match_records_path = output_dir / "match_records.jsonl"
    summary_json.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    summary_md.write_text(render_draft_report_markdown(summary), encoding="utf-8")
    match_records_path.write_text(
        "\n".join(json.dumps(item, ensure_ascii=False) for item in exported_match_records) + ("\n" if exported_match_records else ""),
        encoding="utf-8",
    )
    if not fast_report or save_battle_logs:
        prune_match_logs(matches_dir, keep_match_logs)
    return summary_md, len(records)


def run_draft_report_chunk(
    *,
    draft_bot1_name: str,
    draft_bot2_name: str,
    bot1_name: str,
    bot2_name: str,
    round_start: int,
    round_end: int,
    seed: int,
    cards_path: str = "data/cards.json",
    pool_path: str = "data/card_pool.json",
    draft_mode: str = "simple",
    output_dir: str | None = None,
    fast_report: bool = False,
    lean_draft_logging: bool = False,
    save_battle_logs: bool = False,
) -> dict[str, Any]:
    cards = load_cards(cards_path)
    pool = load_card_pool(pool_path, cards)
    output_dir_path = Path(output_dir) if output_dir is not None else None
    matches_dir = output_dir_path / "matches" if output_dir_path is not None else None
    if matches_dir is not None and (not fast_report or save_battle_logs):
        matches_dir.mkdir(parents=True, exist_ok=True)

    records: list[dict[str, Any]] = []
    draft_records: list[dict[str, Any]] = []
    exported_match_records: list[dict[str, Any]] = []

    for round_index in range(round_start, round_end + 1):
        seat_pairs = (
            (draft_bot1_name, draft_bot2_name, bot1_name, bot2_name),
            (draft_bot2_name, draft_bot1_name, bot2_name, bot1_name),
        )
        for seat_order, (p1_drafter_name, p2_drafter_name, p1_bot_name, p2_bot_name) in enumerate(seat_pairs):
            match_index = (round_index - 1) * 2 + seat_order + 1
            match_seed = seed + round_index * 101 + seat_order * 11
            rng = random.Random(match_seed)
            draft = draft_with_bots(
                pool,
                cards,
                rng,
                build_draft_bot(p1_drafter_name, match_seed),
                build_draft_bot(p2_drafter_name, match_seed + 1),
                deck_size=20,
                draft_mode=draft_mode,
                deck1_id=f"draft_{match_index:04d}_p1",
                deck2_id=f"draft_{match_index:04d}_p2",
                deck1_name=f"{p1_drafter_name} Deck",
                deck2_name=f"{p2_drafter_name} Deck",
            )

            runner = MatchRunner(
                build_bot(p1_bot_name, match_seed + 2),
                build_bot(p2_bot_name, match_seed + 3),
                draft.deck1.id,
                draft.deck2.id,
                cards_path=cards_path,
                deck_definitions={draft.deck1.id: draft.deck1, draft.deck2.id: draft.deck2},
                match_id=f"draft_match_{match_index:04d}",
                seed=match_seed + 4,
            )
            result = runner.run()

            draft_payload = build_draft_payload(draft, cards, p1_drafter_name, p2_drafter_name)
            wrapper = {"draft": draft_payload, "match": result.log}
            markdown_rel_path = ""
            if matches_dir is not None:
                json_path = matches_dir / f"match_{match_index:04d}_{p1_drafter_name}_vs_{p2_drafter_name}.json"
                md_path = matches_dir / f"match_{match_index:04d}_{p1_drafter_name}_vs_{p2_drafter_name}.md"
                if not fast_report:
                    json_path.write_text(json.dumps(wrapper, ensure_ascii=False, indent=2), encoding="utf-8")
                    md_path.write_text(render_draft_match_markdown(draft, cards, result.log), encoding="utf-8")
                    markdown_rel_path = md_path.relative_to(output_dir_path).as_posix() if output_dir_path else md_path.name
                elif save_battle_logs:
                    json_path.write_text(json.dumps(result.log, ensure_ascii=False, indent=2), encoding="utf-8")
                    md_path.write_text(render_match_log_markdown(result.log), encoding="utf-8")
                    markdown_rel_path = md_path.relative_to(output_dir_path).as_posix() if output_dir_path else md_path.name

            record = build_match_record(result.log, markdown_rel_path)
            record["p1_drafter"] = p1_drafter_name
            record["p2_drafter"] = p2_drafter_name
            record["p1_play_bot"] = p1_bot_name
            record["p2_play_bot"] = p2_bot_name
            record["draft_first_player"] = draft.first_player
            record["p1_deck_cards"] = list(draft.deck1.all_cards)
            record["p2_deck_cards"] = list(draft.deck2.all_cards)
            record["p1_deck_summary"] = summary_to_dict(summarize_deck(draft.deck1.all_cards, cards))
            record["p2_deck_summary"] = summary_to_dict(summarize_deck(draft.deck2.all_cards, cards))
            records.append(record)
            if not lean_draft_logging:
                draft_records.append(draft_payload)
            exported_match_records.append(
                {
                    "match_id": record["match_id"],
                    "winner_side": record["winner_side"],
                    "turn_count": record["turn_count"],
                    "end_reason": record["end_reason"],
                    "p1_drafter": p1_drafter_name,
                    "p2_drafter": p2_drafter_name,
                    "p1_play_bot": p1_bot_name,
                    "p2_play_bot": p2_bot_name,
                    "draft_first_player": draft.first_player,
                    "markdown_path": markdown_rel_path,
                    "set_pass_candidate_count": record.get("set_pass_candidate_count", 0),
                    "hand_count_trace": record.get("hand_count_trace", []),
                    "side_usage_details": record.get("side_usage_details", {}),
                    "winner_used_card_details": record.get("winner_used_card_details", []),
                    "winner_decisive_card_details": record.get("winner_decisive_card_details", []),
                    "p1_public_cards": list(draft.deck1.public_cards),
                    "p1_hidden_cards": list(draft.deck1.hidden_cards),
                    "p1_public_normal_cards": list(draft.deck1.metadata.get("public_normal_cards", [])),
                    "p1_hidden_normal_cards": list(draft.deck1.metadata.get("hidden_normal_cards", [])),
                    "p1_public_rare_cards": list(draft.deck1.metadata.get("public_rare_cards", [])),
                    "p1_hidden_rare_cards": list(draft.deck1.metadata.get("hidden_rare_cards", [])),
                    "p2_public_cards": list(draft.deck2.public_cards),
                    "p2_hidden_cards": list(draft.deck2.hidden_cards),
                    "p2_public_normal_cards": list(draft.deck2.metadata.get("public_normal_cards", [])),
                    "p2_hidden_normal_cards": list(draft.deck2.metadata.get("hidden_normal_cards", [])),
                    "p2_public_rare_cards": list(draft.deck2.metadata.get("public_rare_cards", [])),
                    "p2_hidden_rare_cards": list(draft.deck2.metadata.get("hidden_rare_cards", [])),
                    "p1_rarity_counts": dict(draft.deck1.metadata.get("final_rarity_counts", {})),
                    "p2_rarity_counts": dict(draft.deck2.metadata.get("final_rarity_counts", {})),
                    **({} if lean_draft_logging else {"picks": draft_payload["picks"]}),
                }
            )

    return {
        "records": records,
        "draft_records": draft_records,
        "exported_match_records": exported_match_records,
        "pool_id": pool.id,
        "pool_total_cards": pool.total_cards,
    }


def summary_to_dict(summary) -> dict[str, Any]:
    return {
        "total": summary.total,
        "battle_count": summary.battle_count,
        "control_count": summary.control_count,
        "role_counts": summary.role_counts,
        "rarity_counts": summary.rarity_counts,
    }


def build_draft_summary(records: list[dict[str, Any]], cards: dict[str, Any], drafter_names: list[str]) -> dict[str, Any]:
    drafter_stats: dict[str, dict[str, Any]] = {}
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

    for name in drafter_names:
        drafter_stats[name] = {
            "matches": 0,
            "wins": 0,
            "losses": 0,
            "draws": 0,
            "turn_counts": [],
            "final_attack": [],
            "final_block": [],
            "final_speed": [],
            "losing_attack": [],
            "losing_block": [],
            "losing_speed": [],
            "picked_cards": Counter(),
            "winning_picked_cards": Counter(),
            "picked_card_stats": {
                card.name: {
                    "id": card.id,
                    "type": card.type,
                    "rarity": card.rarity,
                    "picked_count": 0,
                    "used_count": 0,
                    "winner_usage_count": 0,
                    "lethal_count": 0,
                }
                for card in cards.values()
            },
            "rarity_play_stats": {
                rarity: {
                    "picked_count": 0,
                    "used_count": 0,
                    "winner_usage_count": 0,
                    "lethal_count": 0,
                }
                for rarity in ("common", "uncommon", "rare")
            },
            "battle_counts": [],
            "control_counts": [],
            "role_red": [],
            "role_blue": [],
            "role_green": [],
            "role_white": [],
            "rarity_common": [],
            "rarity_uncommon": [],
            "rarity_rare": [],
            "action_counts": Counter(),
            "set_pass_candidate_total": 0,
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
        pair_key = " vs ".join(sorted((record["p1_drafter"], record["p2_drafter"])))
        if pair_key not in pair_stats:
            pair_stats[pair_key] = {
                "matches": 0,
                "draws": 0,
                "wins": defaultdict(int),
                "turn_counts": [],
            }
        pair = pair_stats[pair_key]
        pair["matches"] += 1
        pair["turn_counts"].append(record["turn_count"])

        for side in ("p1", "p2"):
            drafter_name = record[f"{side}_drafter"]
            summary = record[f"{side}_deck_summary"]
            stats = drafter_stats[drafter_name]
            stats["matches"] += 1
            stats["turn_counts"].append(record["turn_count"])
            stats["picked_cards"].update(cards[card_id].name for card_id in record[f"{side}_deck_cards"])
            if record[f"{side}_final_stats"] is not None:
                stats["final_attack"].append(record[f"{side}_final_stats"]["attack"])
                stats["final_block"].append(record[f"{side}_final_stats"]["block"])
                stats["final_speed"].append(record[f"{side}_final_stats"]["speed"])
            stats["action_counts"].update(record["action_counts"][side])
            stats["set_pass_candidate_total"] += int(record.get("set_pass_candidate_count", 0))
            stats["battle_counts"].append(summary["battle_count"])
            stats["control_counts"].append(summary["control_count"])
            stats["role_red"].append(summary["role_counts"]["red"])
            stats["role_blue"].append(summary["role_counts"]["blue"])
            stats["role_green"].append(summary["role_counts"]["green"])
            stats["role_white"].append(summary["role_counts"]["white"])
            stats["rarity_common"].append(summary["rarity_counts"]["common"])
            stats["rarity_uncommon"].append(summary["rarity_counts"]["uncommon"])
            stats["rarity_rare"].append(summary["rarity_counts"]["rare"])
            stats["match_links"].append((record["match_id"], record["markdown_path"]))
            picked_counter = Counter(record[f"{side}_deck_cards"])
            for card_id, count in picked_counter.items():
                card = cards[card_id]
                stats["picked_card_stats"][card.name]["picked_count"] += count
                stats["rarity_play_stats"][card.rarity]["picked_count"] += count
            for card_name in record["side_usage"][side]:
                card = cards[name_to_id(card_name, cards)]
                stats["picked_card_stats"][card.name]["used_count"] += 1
                stats["rarity_play_stats"][card.rarity]["used_count"] += 1
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
            pair["draws"] += 1
            drafter_stats[record["p1_drafter"]]["draws"] += 1
            drafter_stats[record["p2_drafter"]]["draws"] += 1
        else:
            winner_side = record["winner_side"]
            loser_side = "p2" if winner_side == "p1" else "p1"
            winner_name = record[f"{winner_side}_drafter"]
            loser_name = record[f"{loser_side}_drafter"]
            drafter_stats[winner_name]["wins"] += 1
            drafter_stats[loser_name]["losses"] += 1
            drafter_stats[winner_name]["winning_picked_cards"].update(
                cards[card_id].name for card_id in record[f"{winner_side}_deck_cards"]
            )
            drafter_stats[winner_name]["wins_with_fewer_cards"] += int(record["won_with_fewer_cards"])
            drafter_stats[winner_name]["wins_with_same_cards"] += int(record["won_with_same_cards"])
            drafter_stats[winner_name]["wins_with_more_cards"] += int(record["won_with_more_cards"])
            if record["p1_final_stats"] is not None and winner_side == "p2":
                drafter_stats[record["p1_drafter"]]["losing_attack"].append(record["p1_final_stats"]["attack"])
                drafter_stats[record["p1_drafter"]]["losing_block"].append(record["p1_final_stats"]["block"])
                drafter_stats[record["p1_drafter"]]["losing_speed"].append(record["p1_final_stats"]["speed"])
            if record["p2_final_stats"] is not None and winner_side == "p1":
                drafter_stats[record["p2_drafter"]]["losing_attack"].append(record["p2_final_stats"]["attack"])
                drafter_stats[record["p2_drafter"]]["losing_block"].append(record["p2_final_stats"]["block"])
                drafter_stats[record["p2_drafter"]]["losing_speed"].append(record["p2_final_stats"]["speed"])
            if record["winner_facedown_count"] is not None:
                drafter_stats[winner_name]["winning_facedown_counts"].append(record["winner_facedown_count"])
            if record["loser_facedown_count"] is not None:
                drafter_stats[loser_name]["losing_facedown_counts"].append(record["loser_facedown_count"])
            for card_name in record["winner_used_cards"]:
                card = cards[name_to_id(card_name, cards)]
                drafter_stats[winner_name]["picked_card_stats"][card.name]["winner_usage_count"] += 1
                drafter_stats[winner_name]["rarity_play_stats"][card.rarity]["winner_usage_count"] += 1
            for card_name in record["winner_decisive_cards"]:
                card = cards[name_to_id(card_name, cards)]
                drafter_stats[winner_name]["picked_card_stats"][card.name]["lethal_count"] += 1
                drafter_stats[winner_name]["rarity_play_stats"][card.rarity]["lethal_count"] += 1
            pair["wins"][winner_name] += 1

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
        "drafters": {name: finalize_drafter_stats(name, stats) for name, stats in drafter_stats.items()},
        "pairs": {key: finalize_pair_stats(key, stats) for key, stats in pair_stats.items()},
        "cards": finalize_card_stats(card_stats),
    }


def finalize_drafter_stats(name: str, stats: dict[str, Any]) -> dict[str, Any]:
    matches = stats["matches"] or 1
    wins = stats["wins"]
    total_actions = sum(stats["action_counts"].values()) or 1
    first_pass_matches = stats["first_pass_matches"]
    starting_player_matches = stats["starting_player_matches"]
    responding_player_matches = stats["responding_player_matches"]
    return {
        "drafter": name,
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
        "losing_attack": summarize_numbers(stats["losing_attack"]),
        "losing_block": summarize_numbers(stats["losing_block"]),
        "losing_speed": summarize_numbers(stats["losing_speed"]),
        "battle_count": summarize_numbers(stats["battle_counts"]),
        "control_count": summarize_numbers(stats["control_counts"]),
        "role_red": summarize_numbers(stats["role_red"]),
        "role_blue": summarize_numbers(stats["role_blue"]),
        "role_green": summarize_numbers(stats["role_green"]),
        "role_white": summarize_numbers(stats["role_white"]),
        "rarity_common": summarize_numbers(stats["rarity_common"]),
        "rarity_uncommon": summarize_numbers(stats["rarity_uncommon"]),
        "rarity_rare": summarize_numbers(stats["rarity_rare"]),
        "winning_facedown": summarize_numbers(stats["winning_facedown_counts"]),
        "losing_facedown": summarize_numbers(stats["losing_facedown_counts"]),
        "first_pass_matches": first_pass_matches,
        "first_pass_wins": stats["first_pass_wins"],
        "first_pass_win_rate": stats["first_pass_wins"] / first_pass_matches if first_pass_matches else None,
        "starting_player_matches": starting_player_matches,
        "starting_player_wins": stats["starting_player_wins"],
        "starting_player_win_rate": stats["starting_player_wins"] / starting_player_matches if starting_player_matches else None,
        "responding_player_matches": responding_player_matches,
        "responding_player_wins": stats["responding_player_wins"],
        "responding_player_win_rate": stats["responding_player_wins"] / responding_player_matches if responding_player_matches else None,
        "wins_with_fewer_cards": stats["wins_with_fewer_cards"],
        "wins_with_same_cards": stats["wins_with_same_cards"],
        "wins_with_more_cards": stats["wins_with_more_cards"],
        "fewer_card_win_rate": (stats["wins_with_fewer_cards"] / wins) if wins else None,
        "same_card_win_rate": (stats["wins_with_same_cards"] / wins) if wins else None,
        "more_card_win_rate": (stats["wins_with_more_cards"] / wins) if wins else None,
        "speed_advantage_losses": stats["speed_advantage_losses"],
        "speed_advantage_loss_rate": stats["speed_advantage_losses"] / matches,
        "block_then_win_matches": stats["block_then_win_matches"],
        "block_then_win_rate": (stats["block_then_win_matches"] / wins) if wins else None,
        "action_counts": dict(stats["action_counts"]),
        "set_pass_candidate_total": stats["set_pass_candidate_total"],
        "set_pass_candidate_avg_per_match": round(stats["set_pass_candidate_total"] / matches, 2),
        "action_rates": {
            "set": stats["action_counts"].get("set", 0) / total_actions,
            "set_pass": stats["action_counts"].get("set_pass", 0) / total_actions,
            "pass": stats["action_counts"].get("pass", 0) / total_actions,
        },
        "most_picked_cards": stats["picked_cards"].most_common(10),
        "winning_picked_cards": stats["winning_picked_cards"].most_common(10),
        "picked_card_stats": finalize_picked_card_stats(stats["picked_card_stats"]),
        "rarity_play_stats": finalize_rarity_play_stats(stats["rarity_play_stats"]),
        "match_links": stats["match_links"],
    }


def finalize_pair_stats(pair_key: str, stats: dict[str, Any]) -> dict[str, Any]:
    return {
        "pair_key": pair_key,
        "matches": stats["matches"],
        "draws": stats["draws"],
        "wins": dict(stats["wins"]),
        "turns": summarize_numbers(stats["turn_counts"]),
    }


def render_draft_report_markdown(summary: dict[str, Any]) -> str:
    config = summary["config"]
    lines = [
        "# Draft Report",
        "",
        "## Configuration",
        "",
        f"- Draft Bot 1: `{config['draft_bot1']}`",
        f"- Draft Bot 2: `{config['draft_bot2']}`",
        f"- Play Bot 1: `{config['bot1']}`",
        f"- Play Bot 2: `{config['bot2']}`",
        f"- Rounds: {config['rounds']}",
        f"- Total Matches: {config['total_matches']}",
        f"- Seed: {config['seed']}",
        f"- Pool: `{config['pool_id']}` ({config['pool_total_cards']} copies)",
        f"- Pairing Mode: {config['pairing_mode']}",
        f"- Draft Mode: `{config.get('draft_mode', 'unknown')}`",
        f"- Fast Report: {'on' if config.get('fast_report') else 'off'}",
        f"- Lean Draft Logging: {'on' if config.get('lean_draft_logging') else 'off'}",
        f"- Save Battle Logs: {'on' if config.get('save_battle_logs') else 'off'}",
        f"- Draft Flow: {'hidden 3->1 + public 5 rarity-balanced' if config.get('draft_mode') == 'simple' else 'normal public pack + normal hidden pack, then public rare + hidden rare, with order swapped in second half'}",
        "",
        "## Drafter Summary",
        "",
        "| Drafter | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Winner Set Avg | Loser Set Avg | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate | Battle Avg | Control Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for name, stats in sorted(summary["drafters"].items()):
        lines.append(
            f"| `{name}` | {stats['matches']} | {stats['wins']} | {stats['losses']} | {stats['draws']} | {format_rate(stats['win_rate'])} | "
            f"{format_optional_rate(stats['first_pass_win_rate'])} | {format_optional_rate(stats['fewer_card_win_rate'])} | "
            f"{format_optional_rate(stats['same_card_win_rate'])} | {format_optional_rate(stats['more_card_win_rate'])} | "
            f"{fmt(stats['winning_facedown']['avg'])} | {fmt(stats['losing_facedown']['avg'])} | "
            f"{format_optional_rate(stats['starting_player_win_rate'])} | {format_optional_rate(stats['responding_player_win_rate'])} | "
            f"{format_rate(stats['action_rates']['set'])} | {format_rate(stats['action_rates']['set_pass'])} | {format_rate(stats['action_rates']['pass'])} | "
            f"{fmt(stats['battle_count']['avg'])} | {fmt(stats['control_count']['avg'])} | "
            f"{fmt(stats['role_red']['avg'])} | {fmt(stats['role_blue']['avg'])} | {fmt(stats['role_green']['avg'])} | {fmt(stats['role_white']['avg'])} | "
            f"{fmt(stats['rarity_common']['avg'])} | {fmt(stats['rarity_uncommon']['avg'])} | {fmt(stats['rarity_rare']['avg'])} |"
        )

    lines.extend(["", "## Pair Summary", "", "| Pair | Matches | Draws | Wins | Turn Avg |", "|---|---:|---:|---|---:|"])
    for pair_key, stats in sorted(summary["pairs"].items()):
        wins_text = ", ".join(f"`{name}`={count}" for name, count in sorted(stats["wins"].items()))
        lines.append(f"| {pair_key} | {stats['matches']} | {stats['draws']} | {wins_text or '-'} | {fmt(stats['turns']['avg'])} |")

    lines.extend(["", "## Match Card Highlights", ""])
    lines.extend(render_rank_table("Most Used Cards", summary["cards"]["most_used"]))
    lines.append("")
    lines.extend(render_rank_table("Most Effective Cards", summary["cards"]["most_effective"]))
    lines.append("")
    lines.extend(render_rank_table("Most Lethal Cards", summary["cards"]["most_lethal"]))
    lines.append("")
    lines.extend(
        [
            "## Drafter Pattern Metrics",
            "",
            "| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for name, stats in sorted(summary["drafters"].items()):
        lines.append(
            f"| `{name}` | {fmt(stats['final_attack']['avg'])} | {fmt(stats['final_block']['avg'])} | {fmt(stats['final_speed']['avg'])} | "
            f"{fmt(stats['losing_attack']['avg'])} | {fmt(stats['losing_block']['avg'])} | {fmt(stats['losing_speed']['avg'])} | "
            f"{stats['speed_advantage_losses']} ({format_rate(stats['speed_advantage_loss_rate'])}) | "
            f"{stats['block_then_win_matches']} ({format_optional_rate(stats['block_then_win_rate'])}) |"
        )
    lines.append("")
    lines.append("## Drafter Details")
    lines.append("")

    for name, stats in sorted(summary["drafters"].items()):
        lines.extend(
            [
                f"### {name}",
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
                f"- set_pass Candidate Avg / Match: {fmt(stats['set_pass_candidate_avg_per_match'])}",
                f"- Turns: min={fmt(stats['turns']['min'])}, avg={fmt(stats['turns']['avg'])}, max={fmt(stats['turns']['max'])}",
                f"- Battle / Control: avg={fmt(stats['battle_count']['avg'])} / {fmt(stats['control_count']['avg'])}",
                f"- Role Colors: red={fmt(stats['role_red']['avg'])}, blue={fmt(stats['role_blue']['avg'])}, green={fmt(stats['role_green']['avg'])}, white={fmt(stats['role_white']['avg'])}",
                f"- Rarities: common={fmt(stats['rarity_common']['avg'])}, uncommon={fmt(stats['rarity_uncommon']['avg'])}, rare={fmt(stats['rarity_rare']['avg'])}",
                "",
            ]
        )
        lines.extend(render_rank_table("Most Picked Cards", stats["most_picked_cards"]))
        lines.append("")
        lines.extend(render_rank_table("Winning Deck Usage", stats["winning_picked_cards"]))
        lines.append("")
        lines.extend(render_draft_card_stat_table("Draft Card Stats", stats["picked_card_stats"]))
        lines.append("")
        lines.extend(render_rarity_play_table("Rarity Play Stats", stats["rarity_play_stats"]))
        lines.append("")
        lines.append("#### Match Logs")
        lines.append("")
        for match_id, match_path in stats["match_links"][:20]:
            lines.append(f"- [{match_id}]({match_path})")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_rank_table(title: str, items: list[tuple[str, int]]) -> list[str]:
    lines = [f"### {title}", "", "| Rank | Name | Count |", "|---:|---|---:|"]
    for index, (name, count) in enumerate(items[:15], start=1):
        lines.append(f"| {index} | {name} | {count} |")
    if not items:
        lines.append("| 1 | - | 0 |")
    return lines


def render_draft_card_stat_table(title: str, items: list[dict[str, Any]]) -> list[str]:
    lines = [
        f"### {title}",
        "",
        "| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |",
        "|---|---|---|---:|---:|---:|---:|",
    ]
    for item in items:
        if item["picked_count"] == 0 and item["used_count"] == 0 and item["winner_usage_count"] == 0 and item["lethal_count"] == 0:
            continue
        lines.append(
            f"| {item['name']} | `{item['id']}` | `{item['rarity']}` | {item['picked_count']} | {item['used_count']} | {item['winner_usage_count']} | {item['lethal_count']} |"
        )
    if len(lines) == 4:
        lines.append("| - | - | - | 0 | 0 | 0 | 0 |")
    return lines


def render_rarity_play_table(title: str, items: list[dict[str, Any]]) -> list[str]:
    lines = [
        f"### {title}",
        "",
        "| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for item in items:
        lines.append(
            f"| `{item['rarity']}` | {item['picked_count']} | {item['used_count']} | {format_optional_rate(item['usage_rate'])} | "
            f"{item['winner_usage_count']} | {format_optional_rate(item['winner_contribution_rate'])} | {item['lethal_count']} |"
        )
    return lines


def finalize_picked_card_stats(card_stats: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for name, stats in sorted(
        card_stats.items(),
        key=lambda item: (
            -item[1]["picked_count"],
            -item[1]["used_count"],
            -item[1]["winner_usage_count"],
            -item[1]["lethal_count"],
            item[0],
        ),
    ):
        rows.append({"name": name, **stats})
    return rows


def finalize_rarity_play_stats(rarity_stats: dict[str, dict[str, int]]) -> list[dict[str, Any]]:
    rows = []
    for rarity in ("common", "uncommon", "rare"):
        stats = rarity_stats[rarity]
        picked_count = stats["picked_count"]
        used_count = stats["used_count"]
        rows.append(
            {
                "rarity": rarity,
                "picked_count": picked_count,
                "used_count": used_count,
                "usage_rate": (used_count / picked_count) if picked_count else None,
                "winner_usage_count": stats["winner_usage_count"],
                "winner_contribution_rate": (stats["winner_usage_count"] / used_count) if used_count else None,
                "lethal_count": stats["lethal_count"],
            }
        )
    return rows


def name_to_id(card_name: str, cards: dict[str, Any]) -> str:
    for card_id, card in cards.items():
        if card.name == card_name:
            return card_id
    raise KeyError(card_name)


def format_rate(value: float) -> str:
    return f"{value * 100:.1f}%"


def format_optional_rate(value: float | None) -> str:
    return "-" if value is None else format_rate(value)


def fmt(value: float | int | None) -> str:
    return "-" if value is None else str(value)


if __name__ == "__main__":
    main()
