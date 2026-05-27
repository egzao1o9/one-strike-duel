from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed
from itertools import combinations_with_replacement
import json
import math
import os
from pathlib import Path
from typing import Any

from engine.card import load_cards
from sim.log_retention import prune_match_logs
from sim.run_draft_report import (
    build_draft_summary,
    render_draft_report_markdown,
    run_draft_report_chunk,
)


ARCHETYPES = (
    {"label": "Standard", "draft_bot": "StandardDraftBot", "play_bot": "StandardBot"},
    {"label": "Aggro", "draft_bot": "AggroDraftBot", "play_bot": "AggroBot"},
    {"label": "Guard", "draft_bot": "GuardDraftBot", "play_bot": "GuardBot"},
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the public-info draft bot suite across all archetype pairings.")
    parser.add_argument("--matches-per-matchup", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=541)
    parser.add_argument("--output-dir", default=None)
    parser.add_argument("--keep-match-logs", type=int, default=100)
    parser.add_argument("--fast-report", action="store_true")
    parser.add_argument("--draft-mode", choices=("simple", "full"), default="simple")
    parser.add_argument("--lean-draft-logging", action="store_true")
    parser.add_argument("--save-battle-logs", action="store_true")
    parser.add_argument("--workers", type=int, default=0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output = run_suite(
        matches_per_matchup=args.matches_per_matchup,
        seed=args.seed,
        output_dir_override=args.output_dir,
        keep_match_logs=args.keep_match_logs,
        fast_report=args.fast_report,
        draft_mode=args.draft_mode,
        lean_draft_logging=args.lean_draft_logging,
        save_battle_logs=args.save_battle_logs,
        workers=args.workers,
    )
    print(output["index_path"])
    print(output["summary_path"])


def run_suite(
    *,
    matches_per_matchup: int,
    seed: int,
    output_dir_override: str | None = None,
    keep_match_logs: int = 100,
    fast_report: bool = False,
    draft_mode: str = "simple",
    lean_draft_logging: bool = False,
    save_battle_logs: bool = False,
    workers: int = 0,
) -> dict[str, Path]:
    if matches_per_matchup % 2 != 0:
        raise ValueError("matches_per_matchup must be even because matchups are mirrored by seat")

    rounds = matches_per_matchup // 2
    output_dir = Path(output_dir_override or f"logs/draft_public_info_suite_x{matches_per_matchup}_seed{seed}")
    output_dir.mkdir(parents=True, exist_ok=True)
    cards = load_cards("data/cards.json")

    draft_to_label = {item["draft_bot"]: item["label"] for item in ARCHETYPES}
    label_to_meta = {item["label"]: item for item in ARCHETYPES}
    matchup_summaries: list[dict[str, Any]] = []
    bot_aggregate = init_bot_aggregate(label_to_meta)
    overall_priority = init_priority_aggregate()
    matchup_tasks = []
    for pair_index, (left, right) in enumerate(combinations_with_replacement(ARCHETYPES, 2), start=1):
        matchup_slug = f"{left['label'].lower()}_vs_{right['label'].lower()}"
        matchup_dir = output_dir / matchup_slug
        matchup_tasks.append(
            {
                "matchup_slug": matchup_slug,
                "matchup_dir": str(matchup_dir),
                "draft_bot1": left["draft_bot"],
                "draft_bot2": right["draft_bot"],
                "play_bot1": left["play_bot"],
                "play_bot2": right["play_bot"],
                "rounds": rounds,
                "seed": seed + pair_index * 1000,
                "keep_match_logs": keep_match_logs,
                "fast_report": fast_report,
                "draft_mode": draft_mode,
                "lean_draft_logging": lean_draft_logging,
                "save_battle_logs": save_battle_logs,
            }
        )

    max_workers = resolve_worker_count(workers, len(matchup_tasks))
    chunk_tasks = build_chunk_tasks(matchup_tasks, max_workers)
    if max_workers == 1:
        results = [_run_suite_chunk(task) for task in chunk_tasks]
    else:
        results = []
        with ProcessPoolExecutor(max_workers=min(max_workers, len(chunk_tasks))) as executor:
            future_map = {executor.submit(_run_suite_chunk, task): task for task in chunk_tasks}
            for future in as_completed(future_map):
                results.append(future.result())

    grouped_results: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for result in results:
        grouped_results[result["matchup_slug"]].append(result)

    for matchup in sorted(matchup_tasks, key=lambda item: item["matchup_slug"]):
        matchup_slug = matchup["matchup_slug"]
        matchup_dir = Path(matchup["matchup_dir"])
        matchup_dir.mkdir(parents=True, exist_ok=True)
        merged_records: list[dict[str, Any]] = []
        merged_draft_records: list[dict[str, Any]] = []
        merged_exported_records: list[dict[str, Any]] = []
        for chunk in sorted(grouped_results[matchup_slug], key=lambda item: item["round_start"]):
            merged_records.extend(chunk["records"])
            if not lean_draft_logging:
                merged_draft_records.extend(chunk["draft_records"])
            merged_exported_records.extend(chunk["exported_match_records"])
        merged_exported_records.sort(key=lambda item: item["match_id"])

        summary_payload = build_draft_summary(
            merged_records,
            cards,
            [matchup["draft_bot1"], matchup["draft_bot2"]],
        )
        summary_payload["config"] = {
            "draft_bot1": matchup["draft_bot1"],
            "draft_bot2": matchup["draft_bot2"],
            "bot1": matchup["play_bot1"],
            "bot2": matchup["play_bot2"],
            "rounds": rounds,
            "total_matches": len(merged_records),
            "seed": matchup["seed"],
            "pool_id": grouped_results[matchup_slug][0]["pool_id"],
            "pool_total_cards": grouped_results[matchup_slug][0]["pool_total_cards"],
            "pairing_mode": "mirrored seats per round",
            "draft_mode": draft_mode,
            "fast_report": fast_report,
            "lean_draft_logging": lean_draft_logging,
            "save_battle_logs": save_battle_logs,
        }
        if not lean_draft_logging:
            summary_payload["draft_records"] = merged_draft_records

        summary_path = matchup_dir / "summary.json"
        summary_md_path = matchup_dir / "summary.md"
        summary_path.write_text(json.dumps(summary_payload, ensure_ascii=False, indent=2), encoding="utf-8")
        summary_md_path.write_text(render_draft_report_markdown(summary_payload), encoding="utf-8")
        (matchup_dir / "match_records.jsonl").write_text(
            "\n".join(json.dumps(item, ensure_ascii=False) for item in merged_exported_records)
            + ("\n" if merged_exported_records else ""),
            encoding="utf-8",
        )
        if not fast_report or save_battle_logs:
            prune_match_logs(matchup_dir / "matches", keep_match_logs)

        matchup_summary = summarize_matchup(summary_payload, merged_exported_records, draft_to_label, matchup_slug)
        matchup_summaries.append(matchup_summary)
        fold_summary_into_bot_aggregate(bot_aggregate, summary_payload, draft_to_label, matchup_summary)
        if not lean_draft_logging:
            fold_match_records_into_priority(overall_priority, bot_aggregate, merged_exported_records, draft_to_label)

    summary = build_suite_summary(
        matches_per_matchup=matches_per_matchup,
        seed=seed,
        output_dir=output_dir,
        matchup_summaries=matchup_summaries,
        bot_aggregate=bot_aggregate,
        overall_priority=overall_priority,
        fast_report=fast_report,
        draft_mode=draft_mode,
        lean_draft_logging=lean_draft_logging,
        save_battle_logs=save_battle_logs,
        workers=max_workers,
    )
    summary_path = output_dir / "summary.json"
    index_path = output_dir / "index.md"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    index_path.write_text(render_suite_markdown(summary), encoding="utf-8")
    return {"summary_path": summary_path, "index_path": index_path}


def init_bot_aggregate(label_to_meta: dict[str, dict[str, str]]) -> dict[str, dict[str, Any]]:
    aggregate: dict[str, dict[str, Any]] = {}
    for label, meta in label_to_meta.items():
        aggregate[label] = {
            "label": label,
            "draft_bot": meta["draft_bot"],
            "play_bot": meta["play_bot"],
            "matches": 0,
            "wins": 0,
            "losses": 0,
            "draws": 0,
            "first_pass_matches": 0,
            "first_pass_wins": 0,
            "starting_player_matches": 0,
            "starting_player_wins": 0,
            "responding_player_matches": 0,
            "responding_player_wins": 0,
            "wins_with_fewer_cards": 0,
            "wins_with_same_cards": 0,
            "wins_with_more_cards": 0,
            "set_pass_candidate_total": 0,
            "action_counts": Counter(),
            "picked_card_stats": defaultdict(
                lambda: {
                    "picked_count": 0,
                    "used_count": 0,
                    "winner_usage_count": 0,
                    "lethal_count": 0,
                    "rarity": None,
                    "id": None,
                }
            ),
            "rarity_play_stats": {
                rarity: {
                    "picked_count": 0,
                    "used_count": 0,
                    "winner_usage_count": 0,
                    "lethal_count": 0,
                }
                for rarity in ("common", "uncommon", "rare")
            },
            "matchups": defaultdict(lambda: {"matches": 0, "wins": 0, "losses": 0, "draws": 0}),
            "priority": init_priority_aggregate(),
        }
    return aggregate


def _run_suite_chunk(task: dict[str, Any]) -> dict[str, Any]:
    chunk = run_draft_report_chunk(
        draft_bot1_name=task["draft_bot1"],
        draft_bot2_name=task["draft_bot2"],
        bot1_name=task["play_bot1"],
        bot2_name=task["play_bot2"],
        round_start=task["round_start"],
        round_end=task["round_end"],
        seed=task["seed"],
        draft_mode=task["draft_mode"],
        output_dir=task["matchup_dir"],
        fast_report=task["fast_report"],
        lean_draft_logging=task["lean_draft_logging"],
        save_battle_logs=task["save_battle_logs"],
    )
    return {
        "matchup_slug": task["matchup_slug"],
        "matchup_dir": task["matchup_dir"],
        "round_start": task["round_start"],
        "records": chunk["records"],
        "draft_records": chunk["draft_records"],
        "exported_match_records": chunk["exported_match_records"],
        "pool_id": chunk["pool_id"],
        "pool_total_cards": chunk["pool_total_cards"],
    }


def init_priority_aggregate() -> dict[str, Any]:
    return {
        "overall_picks": Counter(),
        "hidden_offers": Counter(),
        "hidden_picks": Counter(),
        "public_first_offers": Counter(),
        "public_first_picks": Counter(),
        "public_second_offers": Counter(),
        "public_second_picks": Counter(),
    }


def resolve_worker_count(requested_workers: int, task_count: int) -> int:
    windows_process_pool_cap = 61
    if task_count <= 0:
        return 1
    if requested_workers > 0:
        return max(1, min(requested_workers, windows_process_pool_cap))
    cpu_total = os.cpu_count() or 2
    return max(1, min(cpu_total - 1, windows_process_pool_cap))


def build_chunk_tasks(matchup_tasks: list[dict[str, Any]], max_workers: int) -> list[dict[str, Any]]:
    if not matchup_tasks:
        return []
    chunks_per_matchup = max(1, min(matchup_tasks[0]["rounds"], math.ceil(max_workers / len(matchup_tasks))))
    tasks: list[dict[str, Any]] = []
    for matchup in matchup_tasks:
        for round_start, round_end in split_rounds(matchup["rounds"], chunks_per_matchup):
            tasks.append(
                {
                    **matchup,
                    "round_start": round_start,
                    "round_end": round_end,
                }
            )
    return tasks


def split_rounds(total_rounds: int, chunk_count: int) -> list[tuple[int, int]]:
    if total_rounds <= 0:
        return []
    chunk_count = max(1, min(chunk_count, total_rounds))
    base = total_rounds // chunk_count
    extra = total_rounds % chunk_count
    ranges: list[tuple[int, int]] = []
    start = 1
    for index in range(chunk_count):
        size = base + (1 if index < extra else 0)
        end = start + size - 1
        ranges.append((start, end))
        start = end + 1
    return ranges


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def summarize_matchup(
    summary_payload: dict[str, Any],
    match_records: list[dict[str, Any]],
    draft_to_label: dict[str, str],
    matchup_slug: str,
) -> dict[str, Any]:
    config = summary_payload["config"]
    rows = []
    for draft_bot, stats in summary_payload["drafters"].items():
        rows.append(
            {
                "label": draft_to_label[draft_bot],
                "draft_bot": draft_bot,
                "play_bot": config["bot1"] if config["draft_bot1"] == draft_bot else config["bot2"],
                "matches": stats["matches"],
                "wins": stats["wins"],
                "losses": stats["losses"],
                "draws": stats["draws"],
                "win_rate": stats["win_rate"],
            }
        )
    rows.sort(key=lambda item: (item["win_rate"], item["label"]), reverse=True)
    return {
        "slug": matchup_slug,
        "draft_bot1": config["draft_bot1"],
        "draft_bot2": config["draft_bot2"],
        "play_bot1": config["bot1"],
        "play_bot2": config["bot2"],
        "total_matches": config["total_matches"],
        "rounds": config["rounds"],
        "draws": sum(1 for item in match_records if item.get("winner_side") is None),
        "rankings": rows,
        "summary_path": f"./{matchup_slug}/summary.md",
        "records_path": f"./{matchup_slug}/match_records.jsonl",
    }


def fold_summary_into_bot_aggregate(
    bot_aggregate: dict[str, dict[str, Any]],
    summary_payload: dict[str, Any],
    draft_to_label: dict[str, str],
    matchup_summary: dict[str, Any],
) -> None:
    config = summary_payload["config"]
    for draft_bot, stats in summary_payload["drafters"].items():
        label = draft_to_label[draft_bot]
        aggregate = bot_aggregate[label]
        aggregate["matches"] += stats["matches"]
        aggregate["wins"] += stats["wins"]
        aggregate["losses"] += stats["losses"]
        aggregate["draws"] += stats["draws"]
        aggregate["first_pass_matches"] += stats["first_pass_matches"]
        aggregate["first_pass_wins"] += stats["first_pass_wins"]
        aggregate["starting_player_matches"] += stats["starting_player_matches"]
        aggregate["starting_player_wins"] += stats["starting_player_wins"]
        aggregate["responding_player_matches"] += stats["responding_player_matches"]
        aggregate["responding_player_wins"] += stats["responding_player_wins"]
        aggregate["wins_with_fewer_cards"] += stats["wins_with_fewer_cards"]
        aggregate["wins_with_same_cards"] += stats["wins_with_same_cards"]
        aggregate["wins_with_more_cards"] += stats["wins_with_more_cards"]
        aggregate["set_pass_candidate_total"] += stats.get("set_pass_candidate_total", 0)
        aggregate["action_counts"].update(stats["action_counts"])
        for item in stats["picked_card_stats"]:
            card = aggregate["picked_card_stats"][item["name"]]
            card["picked_count"] += item["picked_count"]
            card["used_count"] += item["used_count"]
            card["winner_usage_count"] += item["winner_usage_count"]
            card["lethal_count"] += item["lethal_count"]
            card["rarity"] = item["rarity"]
            card["id"] = item["id"]
        for rarity_row in stats["rarity_play_stats"]:
            rarity = rarity_row["rarity"]
            aggregate["rarity_play_stats"][rarity]["picked_count"] += rarity_row["picked_count"]
            aggregate["rarity_play_stats"][rarity]["used_count"] += rarity_row["used_count"]
            aggregate["rarity_play_stats"][rarity]["winner_usage_count"] += rarity_row["winner_usage_count"]
            aggregate["rarity_play_stats"][rarity]["lethal_count"] += rarity_row["lethal_count"]

    if config["draft_bot1"] == config["draft_bot2"]:
        label = draft_to_label[config["draft_bot1"]]
        same_stats = next(iter(summary_payload["drafters"].values()))
        matchup = bot_aggregate[label]["matchups"][label]
        matchup["matches"] += same_stats["matches"]
        matchup["wins"] += same_stats["wins"]
        matchup["losses"] += same_stats["losses"]
        matchup["draws"] += same_stats["draws"]
        return

    left_label = draft_to_label[config["draft_bot1"]]
    right_label = draft_to_label[config["draft_bot2"]]
    left_stats = summary_payload["drafters"][config["draft_bot1"]]
    right_stats = summary_payload["drafters"][config["draft_bot2"]]
    left_matchup = bot_aggregate[left_label]["matchups"][right_label]
    left_matchup["matches"] += left_stats["matches"]
    left_matchup["wins"] += left_stats["wins"]
    left_matchup["losses"] += left_stats["losses"]
    left_matchup["draws"] += left_stats["draws"]
    right_matchup = bot_aggregate[right_label]["matchups"][left_label]
    right_matchup["matches"] += right_stats["matches"]
    right_matchup["wins"] += right_stats["wins"]
    right_matchup["losses"] += right_stats["losses"]
    right_matchup["draws"] += right_stats["draws"]


def fold_match_records_into_priority(
    overall_priority: dict[str, Any],
    bot_aggregate: dict[str, dict[str, Any]],
    match_records: list[dict[str, Any]],
    draft_to_label: dict[str, str],
) -> None:
    for record in match_records:
        player_to_label = {
            "p1": draft_to_label[record["p1_drafter"]],
            "p2": draft_to_label[record["p2_drafter"]],
        }
        for pick in record["picks"]:
            label = player_to_label[pick["player"]]
            overall_offers, overall_picks = resolve_priority_buckets(overall_priority, pick["visibility"], pick["pick_position"])
            bot_offers, bot_picks = resolve_priority_buckets(bot_aggregate[label]["priority"], pick["visibility"], pick["pick_position"])
            for offered_card_id in pick["offer_card_ids"]:
                overall_offers[offered_card_id] += 1
                bot_offers[offered_card_id] += 1
            selected_ids = pick.get("selected_card_ids") or ([pick["card_id"]] if pick.get("card_id") else [])
            for selected_card_id in selected_ids:
                overall_picks[selected_card_id] += 1
                bot_picks[selected_card_id] += 1
                overall_priority["overall_picks"][selected_card_id] += 1
                bot_aggregate[label]["priority"]["overall_picks"][selected_card_id] += 1


def resolve_priority_buckets(
    priority: dict[str, Any],
    visibility: str,
    pick_position: int,
) -> tuple[Counter, Counter]:
    if visibility == "hidden":
        return priority["hidden_offers"], priority["hidden_picks"]
    if pick_position == 1:
        return priority["public_first_offers"], priority["public_first_picks"]
    return priority["public_second_offers"], priority["public_second_picks"]


def build_suite_summary(
    *,
    matches_per_matchup: int,
    seed: int,
    output_dir: Path,
    matchup_summaries: list[dict[str, Any]],
    bot_aggregate: dict[str, dict[str, Any]],
    overall_priority: dict[str, Any],
    fast_report: bool,
    draft_mode: str,
    lean_draft_logging: bool,
    save_battle_logs: bool,
    workers: int,
) -> dict[str, Any]:
    ordered_matchups = sorted(
        matchup_summaries,
        key=lambda item: item["slug"],
    )
    bot_rows = {}
    for label, stats in sorted(bot_aggregate.items()):
        row = finalize_bot_row(label, stats)
        if lean_draft_logging:
            row["priority"] = None
        bot_rows[label] = row
    return {
        "config": {
            "matches_per_matchup": matches_per_matchup,
            "seed": seed,
            "archetypes": list(ARCHETYPES),
            "fast_report": fast_report,
            "draft_mode": draft_mode,
            "lean_draft_logging": lean_draft_logging,
            "save_battle_logs": save_battle_logs,
            "workers": workers,
        },
        "matchups": ordered_matchups,
        "bots": bot_rows,
        "overall_priority": None if lean_draft_logging else finalize_priority_section(overall_priority, min_offered=50),
        "output_dir": output_dir.as_posix(),
    }


def finalize_bot_row(label: str, stats: dict[str, Any]) -> dict[str, Any]:
    matches = stats["matches"] or 1
    wins = stats["wins"]
    total_actions = sum(stats["action_counts"].values()) or 1
    rarity_rows = []
    for rarity, rarity_stats in stats["rarity_play_stats"].items():
        used = rarity_stats["used_count"]
        rarity_rows.append(
            {
                "rarity": rarity,
                "picked_count": rarity_stats["picked_count"],
                "used_count": used,
                "winner_usage_count": rarity_stats["winner_usage_count"],
                "lethal_count": rarity_stats["lethal_count"],
                "usage_rate": round(used / rarity_stats["picked_count"], 4) if rarity_stats["picked_count"] else None,
                "winner_contribution_rate": round(rarity_stats["winner_usage_count"] / used, 4) if used else None,
            }
        )
    card_rows = []
    for name, item in sorted(
        stats["picked_card_stats"].items(),
        key=lambda pair: (
            -pair[1]["picked_count"],
            -pair[1]["winner_usage_count"],
            -pair[1]["lethal_count"],
            pair[0],
        ),
    ):
        card_rows.append({"name": name, **item})
    return {
        "label": label,
        "draft_bot": stats["draft_bot"],
        "play_bot": stats["play_bot"],
        "matches": stats["matches"],
        "wins": stats["wins"],
        "losses": stats["losses"],
        "draws": stats["draws"],
        "win_rate": round(stats["wins"] / matches, 4),
        "first_pass_win_rate": round(stats["first_pass_wins"] / stats["first_pass_matches"], 4) if stats["first_pass_matches"] else None,
        "starting_player_win_rate": round(stats["starting_player_wins"] / stats["starting_player_matches"], 4) if stats["starting_player_matches"] else None,
        "responding_player_win_rate": round(stats["responding_player_wins"] / stats["responding_player_matches"], 4) if stats["responding_player_matches"] else None,
        "fewer_card_win_rate": round(stats["wins_with_fewer_cards"] / wins, 4) if wins else None,
        "same_card_win_rate": round(stats["wins_with_same_cards"] / wins, 4) if wins else None,
        "more_card_win_rate": round(stats["wins_with_more_cards"] / wins, 4) if wins else None,
        "set_pass_candidate_total": stats["set_pass_candidate_total"],
        "set_pass_candidate_avg_per_match": round(stats["set_pass_candidate_total"] / matches, 4),
        "action_counts": dict(stats["action_counts"]),
        "action_rates": {
            "set": round(stats["action_counts"].get("set", 0) / total_actions, 4),
            "set_pass": round(stats["action_counts"].get("set_pass", 0) / total_actions, 4),
            "pass": round(stats["action_counts"].get("pass", 0) / total_actions, 4),
        },
        "matchups": {
            opponent: {
                **row,
                "win_rate": round(row["wins"] / row["matches"], 4) if row["matches"] else None,
            }
            for opponent, row in sorted(stats["matchups"].items())
        },
        "picked_card_stats": card_rows,
        "rarity_play_stats": rarity_rows,
        "priority": finalize_priority_section(stats["priority"], min_offered=20),
    }


def finalize_priority_section(priority: dict[str, Any], *, min_offered: int) -> dict[str, Any]:
    return {
        "most_picked": finalize_counter_rows(priority["overall_picks"]),
        "hidden_priority": finalize_priority_rows(priority["hidden_offers"], priority["hidden_picks"], min_offered=min_offered),
        "public_first_priority": finalize_priority_rows(priority["public_first_offers"], priority["public_first_picks"], min_offered=min_offered),
        "public_second_priority": finalize_priority_rows(priority["public_second_offers"], priority["public_second_picks"], min_offered=min_offered),
    }


def finalize_counter_rows(counter: Counter[str], limit: int = 15) -> list[dict[str, Any]]:
    rows = []
    for card_id, count in counter.most_common(limit):
        rows.append({"card_id": card_id, "count": count})
    return rows


def finalize_priority_rows(offers: Counter[str], picks: Counter[str], *, min_offered: int, limit: int = 15) -> list[dict[str, Any]]:
    rows = []
    for card_id, offered_count in offers.items():
        if offered_count < min_offered:
            continue
        picked_count = picks.get(card_id, 0)
        rows.append(
            {
                "card_id": card_id,
                "offered_count": offered_count,
                "picked_count": picked_count,
                "pick_rate": round(picked_count / offered_count, 4) if offered_count else 0.0,
            }
        )
    rows.sort(key=lambda item: (-item["pick_rate"], -item["picked_count"], item["card_id"]))
    return rows[:limit]


def render_suite_markdown(summary: dict[str, Any]) -> str:
    config = summary["config"]
    lines = [
        "# Public-Info Draft Bot Suite",
        "",
        "## Configuration",
        "",
        f"- Matches Per Matchup: {config['matches_per_matchup']}",
        f"- Seed: {config['seed']}",
        f"- Fast Report: {'on' if config.get('fast_report') else 'off'}",
        f"- Draft Mode: `{config.get('draft_mode', 'unknown')}`",
        f"- Lean Draft Logging: {'on' if config.get('lean_draft_logging') else 'off'}",
        f"- Save Battle Logs: {'on' if config.get('save_battle_logs') else 'off'}",
        f"- Workers: {config.get('workers', 1)}",
        "- Archetypes: `Standard`, `Aggro`, `Guard`",
        "- Pairings: all combinations with replacement, mirrored by seat",
        "- Per-match records: `match_records.jsonl` in each matchup directory",
        "",
        "## Matchups",
        "",
        "| Matchup | Matches | Ranking | Draws | Summary | Records |",
        "|---|---:|---|---:|---|---|",
    ]
    for matchup in summary["matchups"]:
        ranking_text = ", ".join(
            f"`{row['label']}` {row['win_rate']*100:.1f}%"
            for row in matchup["rankings"]
        )
        lines.append(
            f"| `{matchup['draft_bot1']}` vs `{matchup['draft_bot2']}` | {matchup['total_matches']} | {ranking_text} | {matchup['draws']} | [{matchup['slug']}]({matchup['summary_path']}) | [jsonl]({matchup['records_path']}) |"
        )

    lines.extend([
        "",
        "## Bot Summary",
        "",
        "| Bot | Draft | Play | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ])
    for label, stats in sorted(summary["bots"].items()):
        lines.append(
            f"| `{label}` | `{stats['draft_bot']}` | `{stats['play_bot']}` | {stats['matches']} | {stats['wins']} | {stats['losses']} | {stats['draws']} | "
            f"{format_optional_rate(stats['win_rate'])} | {format_optional_rate(stats['first_pass_win_rate'])} | {format_optional_rate(stats['fewer_card_win_rate'])} | "
            f"{format_optional_rate(stats['same_card_win_rate'])} | {format_optional_rate(stats['more_card_win_rate'])} | {format_optional_rate(stats['starting_player_win_rate'])} | "
            f"{format_optional_rate(stats['responding_player_win_rate'])} | {format_optional_rate(stats['action_rates']['set'])} | {format_optional_rate(stats['action_rates']['set_pass'])} | {format_optional_rate(stats['action_rates']['pass'])} |"
        )

    if summary["overall_priority"] is not None:
        lines.extend(["", "## Global Priority Picks", ""])
        lines.extend(render_priority_table("Most Picked Overall", summary["overall_priority"]["most_picked"], count_only=True))
        lines.append("")
        lines.extend(render_priority_table("Hidden Pick Priority", summary["overall_priority"]["hidden_priority"]))
        lines.append("")
        lines.extend(render_priority_table("Public First-Pick Priority", summary["overall_priority"]["public_first_priority"]))
        lines.append("")
        lines.extend(render_priority_table("Public Second-Pick Priority", summary["overall_priority"]["public_second_priority"]))
        lines.append("")
    lines.append("## Bot Details")
    lines.append("")

    for label, stats in sorted(summary["bots"].items()):
        lines.extend(
            [
                f"### {label}",
                "",
                f"- Draft Bot: `{stats['draft_bot']}`",
                f"- Play Bot: `{stats['play_bot']}`",
                f"- Win Rate: {format_optional_rate(stats['win_rate'])}",
                f"- First Pass Win Rate: {format_optional_rate(stats['first_pass_win_rate'])}",
                f"- Starting Player Win Rate: {format_optional_rate(stats['starting_player_win_rate'])}",
                f"- Responding Player Win Rate: {format_optional_rate(stats['responding_player_win_rate'])}",
                f"- Action Rates: set={format_optional_rate(stats['action_rates']['set'])}, set_pass={format_optional_rate(stats['action_rates']['set_pass'])}, pass={format_optional_rate(stats['action_rates']['pass'])}",
                f"- set_pass Candidate Avg / Match: {stats['set_pass_candidate_avg_per_match']}",
                "",
                "| Opponent | Matches | Wins | Losses | Draws | Win Rate |",
                "|---|---:|---:|---:|---:|---:|",
            ]
        )
        for opponent, row in stats["matchups"].items():
            lines.append(
                f"| `{opponent}` | {row['matches']} | {row['wins']} | {row['losses']} | {row['draws']} | {format_optional_rate(row['win_rate'])} |"
            )
        lines.append("")
        if stats["priority"] is not None:
            lines.extend(render_priority_table("Most Picked", stats["priority"]["most_picked"], count_only=True))
            lines.append("")
            lines.extend(render_priority_table("Hidden Priority", stats["priority"]["hidden_priority"]))
            lines.append("")
            lines.extend(render_priority_table("Public First-Pick Priority", stats["priority"]["public_first_priority"]))
            lines.append("")
        lines.extend(render_priority_table("Top Picked Cards", stats["picked_card_stats"], card_stats=True))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_priority_table(
    title: str,
    rows: list[dict[str, Any]],
    *,
    count_only: bool = False,
    card_stats: bool = False,
) -> list[str]:
    if count_only:
        lines = [f"#### {title}", "", "| Rank | Card ID | Count |", "|---:|---|---:|"]
        for index, row in enumerate(rows[:15], start=1):
            lines.append(f"| {index} | `{row['card_id']}` | {row['count']} |")
        if len(lines) == 4:
            lines.append("| 1 | - | 0 |")
        return lines
    if card_stats:
        lines = [f"#### {title}", "", "| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |", "|---|---|---|---:|---:|---:|---:|"]
        for row in rows[:15]:
            lines.append(
                f"| {row['name']} | `{row['id']}` | `{row['rarity']}` | {row['picked_count']} | {row['used_count']} | {row['winner_usage_count']} | {row['lethal_count']} |"
            )
        if len(lines) == 4:
            lines.append("| - | - | - | 0 | 0 | 0 | 0 |")
        return lines
    lines = [f"#### {title}", "", "| Rank | Card ID | Offered | Picked | Pick Rate |", "|---:|---|---:|---:|---:|"]
    for index, row in enumerate(rows[:15], start=1):
        lines.append(
            f"| {index} | `{row['card_id']}` | {row['offered_count']} | {row['picked_count']} | {format_optional_rate(row['pick_rate'])} |"
        )
    if len(lines) == 4:
        lines.append("| 1 | - | 0 | 0 | - |")
    return lines


def format_optional_rate(value: float | None) -> str:
    if value is None:
        return "-"
    return f"{value * 100:.1f}%"


if __name__ == "__main__":
    main()
