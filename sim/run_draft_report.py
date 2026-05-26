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
    parser = argparse.ArgumentParser(description="Run mirrored draft matches and generate role-balance reports.")
    parser.add_argument("--draft-bot1", default="RoleBalanceDraftBot", choices=sorted(DRAFT_BOT_REGISTRY))
    parser.add_argument("--draft-bot2", default="RandomDraftBot", choices=sorted(DRAFT_BOT_REGISTRY))
    parser.add_argument("--bot1", default="GreedyBot", choices=sorted(BOT_REGISTRY))
    parser.add_argument("--bot2", default="GreedyBot", choices=sorted(BOT_REGISTRY))
    parser.add_argument("--rounds", type=int, default=25)
    parser.add_argument("--seed", type=int, default=131)
    parser.add_argument("--cards", default="data/cards.json")
    parser.add_argument("--pool", default="data/card_pool.json")
    parser.add_argument("--output-dir", default=None)
    parser.add_argument("--keep-match-logs", type=int, default=100)
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
        args.output_dir,
        args.keep_match_logs,
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
    output_dir_override: str | None = None,
    keep_match_logs: int = 100,
) -> tuple[Path, int]:
    cards = load_cards(cards_path)
    pool = load_card_pool(pool_path, cards)
    output_dir = Path(
        output_dir_override
        or f"logs/draft_report_{draft_bot1_name.lower()}_vs_{draft_bot2_name.lower()}_{bot1_name.lower()}_{bot2_name.lower()}_r{rounds}_seed{seed}"
    )
    matches_dir = output_dir / "matches"
    matches_dir.mkdir(parents=True, exist_ok=True)

    records: list[dict[str, Any]] = []
    draft_records: list[dict[str, Any]] = []
    match_index = 1

    for round_index in range(1, rounds + 1):
        seat_pairs = (
            (draft_bot1_name, draft_bot2_name, bot1_name, bot2_name),
            (draft_bot2_name, draft_bot1_name, bot2_name, bot1_name),
        )
        for seat_order, (p1_drafter_name, p2_drafter_name, p1_bot_name, p2_bot_name) in enumerate(seat_pairs):
            match_seed = seed + round_index * 101 + seat_order * 11
            rng = random.Random(match_seed)
            draft = draft_with_bots(
                pool,
                cards,
                rng,
                build_draft_bot(p1_drafter_name, match_seed),
                build_draft_bot(p2_drafter_name, match_seed + 1),
                deck_size=20,
                all_public=True,
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

            json_path = matches_dir / f"match_{match_index:04d}_{p1_drafter_name}_vs_{p2_drafter_name}.json"
            md_path = matches_dir / f"match_{match_index:04d}_{p1_drafter_name}_vs_{p2_drafter_name}.md"
            wrapper = {
                "draft": build_draft_payload(draft, cards, p1_drafter_name, p2_drafter_name),
                "match": result.log,
            }
            json_path.write_text(json.dumps(wrapper, ensure_ascii=False, indent=2), encoding="utf-8")
            md_path.write_text(render_draft_match_markdown(draft, cards, result.log), encoding="utf-8")

            record = build_match_record(result.log, md_path.relative_to(output_dir).as_posix())
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
            draft_records.append(wrapper["draft"])
            match_index += 1

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
    }
    summary["draft_records"] = draft_records

    summary_json = output_dir / "summary.json"
    summary_md = output_dir / "summary.md"
    summary_json.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    summary_md.write_text(render_draft_report_markdown(summary), encoding="utf-8")
    prune_match_logs(matches_dir, keep_match_logs)
    return summary_md, len(records)


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
            "picked_cards": Counter(),
            "winning_picked_cards": Counter(),
            "battle_counts": [],
            "control_counts": [],
            "role_red": [],
            "role_blue": [],
            "role_green": [],
            "role_white": [],
            "rarity_common": [],
            "rarity_uncommon": [],
            "rarity_rare": [],
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
    return {
        "drafter": name,
        "matches": stats["matches"],
        "wins": stats["wins"],
        "losses": stats["losses"],
        "draws": stats["draws"],
        "win_rate": stats["wins"] / matches,
        "draw_rate": stats["draws"] / matches,
        "turns": summarize_numbers(stats["turn_counts"]),
        "battle_count": summarize_numbers(stats["battle_counts"]),
        "control_count": summarize_numbers(stats["control_counts"]),
        "role_red": summarize_numbers(stats["role_red"]),
        "role_blue": summarize_numbers(stats["role_blue"]),
        "role_green": summarize_numbers(stats["role_green"]),
        "role_white": summarize_numbers(stats["role_white"]),
        "rarity_common": summarize_numbers(stats["rarity_common"]),
        "rarity_uncommon": summarize_numbers(stats["rarity_uncommon"]),
        "rarity_rare": summarize_numbers(stats["rarity_rare"]),
        "most_picked_cards": stats["picked_cards"].most_common(10),
        "winning_picked_cards": stats["winning_picked_cards"].most_common(10),
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
        "# Draft Role Balance Report",
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
        "",
        "## Drafter Summary",
        "",
        "| Drafter | Matches | Wins | Losses | Draws | Win Rate | Battle Avg | Control Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for name, stats in sorted(summary["drafters"].items()):
        lines.append(
            f"| `{name}` | {stats['matches']} | {stats['wins']} | {stats['losses']} | {stats['draws']} | {format_rate(stats['win_rate'])} | "
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
    lines.append("## Drafter Details")
    lines.append("")

    for name, stats in sorted(summary["drafters"].items()):
        lines.extend(
            [
                f"### {name}",
                "",
                f"- Win Rate: {format_rate(stats['win_rate'])}",
                f"- Draw Rate: {format_rate(stats['draw_rate'])}",
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


def format_rate(value: float) -> str:
    return f"{value * 100:.1f}%"


def fmt(value: float | int | None) -> str:
    return "-" if value is None else str(value)


if __name__ == "__main__":
    main()
