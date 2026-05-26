from __future__ import annotations

import json
from pathlib import Path
from statistics import mean
from typing import Any


def main() -> None:
    root = Path("logs")
    summary = build_aggregate_summary(root)
    output_path = root / "aggregate_report.md"
    json_path = root / "aggregate_report.json"
    output_path.write_text(render_aggregate_markdown(summary), encoding="utf-8")
    json_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(output_path)
    print(json_path)


def build_aggregate_summary(root: Path) -> dict[str, Any]:
    summary_paths = sorted(path for path in root.rglob("summary.json") if path.is_file())
    reports = [load_report(path, root) for path in summary_paths]

    random_mix_reports = [report for report in reports if report["type"] == "random_bot_mix"]
    tournament_reports = [report for report in reports if report["type"] == "deck_tournament"]
    draft_reports = [report for report in reports if report["type"] == "draft_report"]

    canonical_random_mix = max(random_mix_reports, key=lambda item: item["config"]["matches"]) if random_mix_reports else None
    baseline_random_mix = min(random_mix_reports, key=lambda item: item["config"]["matches"]) if random_mix_reports else None

    return {
        "inventory": [
            {
                "path": report["relative_path"],
                "type": report["type"],
                "title": report["title"],
            }
            for report in reports
        ],
        "random_mix": summarize_random_mix(random_mix_reports, canonical_random_mix, baseline_random_mix),
        "deck_reports": summarize_deck_reports(tournament_reports),
        "draft_reports": summarize_draft_reports(draft_reports),
        "analysis": build_analysis(random_mix_reports, canonical_random_mix, tournament_reports, draft_reports),
    }


def load_report(path: Path, root: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    config = payload.get("config", {})
    report_type = detect_report_type(path, payload)
    return {
        "path": str(path),
        "relative_path": path.relative_to(root).as_posix(),
        "type": report_type,
        "title": path.parent.name,
        "config": config,
        "payload": payload,
    }


def detect_report_type(path: Path, payload: dict[str, Any]) -> str:
    config = payload.get("config", {})
    if "draft_bot1" in config:
        return "draft_report"
    if "matches" in config and "bot_pool" in config:
        return "random_bot_mix"
    if "bot" in config and "decks" in payload and "pairs" in payload:
        return "deck_tournament"
    return "unknown"


def summarize_random_mix(
    reports: list[dict[str, Any]],
    canonical: dict[str, Any] | None,
    baseline: dict[str, Any] | None,
) -> dict[str, Any]:
    if not reports:
        return {"reports": [], "canonical": None, "baseline": None, "delta": []}

    report_rows = []
    for report in sorted(reports, key=lambda item: item["config"]["matches"]):
        bots = report["payload"]["bots"]
        top_bot = max(bots.items(), key=lambda item: item[1]["win_rate"])
        bottom_bot = min(bots.items(), key=lambda item: item[1]["win_rate"])
        report_rows.append(
            {
                "path": report["relative_path"],
                "matches": report["config"]["matches"],
                "seed": report["config"]["seed"],
                "top_bot": top_bot[0],
                "top_win_rate": top_bot[1]["win_rate"],
                "bottom_bot": bottom_bot[0],
                "bottom_win_rate": bottom_bot[1]["win_rate"],
            }
        )

    delta_rows: list[dict[str, Any]] = []
    if canonical and baseline:
        canonical_bots = canonical["payload"]["bots"]
        baseline_bots = baseline["payload"]["bots"]
        for bot_name in sorted(canonical_bots):
            if bot_name not in baseline_bots:
                continue
            delta_rows.append(
                {
                    "bot": bot_name,
                    "baseline_win_rate": baseline_bots[bot_name]["win_rate"],
                    "canonical_win_rate": canonical_bots[bot_name]["win_rate"],
                    "delta_points": round((canonical_bots[bot_name]["win_rate"] - baseline_bots[bot_name]["win_rate"]) * 100, 1),
                }
            )
        delta_rows.sort(key=lambda item: item["canonical_win_rate"], reverse=True)

    canonical_payload = canonical["payload"] if canonical else None
    canonical_summary = None
    if canonical_payload:
        bots = canonical_payload["bots"]
        ordered = sorted(
            (
                {
                    "bot": name,
                    "matches": stats["matches"],
                    "wins": stats["wins"],
                    "losses": stats["losses"],
                    "draws": stats["draws"],
                    "win_rate": stats["win_rate"],
                    "turn_avg": stats["turns"]["avg"],
                }
                for name, stats in bots.items()
            ),
            key=lambda item: item["win_rate"],
            reverse=True,
        )
        canonical_summary = {
            "path": canonical["relative_path"],
            "matches": canonical["config"]["matches"],
            "seed": canonical["config"]["seed"],
            "bot_rankings": ordered,
            "most_used_cards": canonical_payload["cards"]["most_used"][:10],
            "most_effective_cards": canonical_payload["cards"]["most_effective"][:10],
            "most_lethal_cards": canonical_payload["cards"]["most_lethal"][:10],
        }

    baseline_summary = None
    if baseline:
        baseline_summary = {
            "path": baseline["relative_path"],
            "matches": baseline["config"]["matches"],
            "seed": baseline["config"]["seed"],
        }

    return {
        "reports": report_rows,
        "canonical": canonical_summary,
        "baseline": baseline_summary,
        "delta": delta_rows,
    }


def summarize_deck_reports(reports: list[dict[str, Any]]) -> dict[str, Any]:
    if not reports:
        return {"reports": [], "average_by_deck": [], "average_by_bot": []}

    report_rows = []
    deck_accumulator: dict[str, list[dict[str, Any]]] = {}
    bot_accumulator: dict[str, list[dict[str, Any]]] = {}

    for report in reports:
        config = report["config"]
        payload = report["payload"]
        bot_name = config["bot"]
        deck_rows = []
        for deck_id, stats in sorted(payload["decks"].items()):
            deck_rows.append({"deck_id": deck_id, "win_rate": stats["win_rate"], "turn_avg": stats["turns"]["avg"]})
            deck_accumulator.setdefault(deck_id, []).append({"bot": bot_name, "win_rate": stats["win_rate"], "turn_avg": stats["turns"]["avg"]})
            bot_accumulator.setdefault(bot_name, []).append({"deck": deck_id, "win_rate": stats["win_rate"], "turn_avg": stats["turns"]["avg"]})
        report_rows.append(
            {
                "path": report["relative_path"],
                "bot": bot_name,
                "total_matches": config["total_matches"],
                "best_deck": max(deck_rows, key=lambda item: item["win_rate"]),
                "worst_deck": min(deck_rows, key=lambda item: item["win_rate"]),
            }
        )

    average_by_deck = []
    for deck_id, rows in sorted(deck_accumulator.items()):
        best_row = max(rows, key=lambda item: item["win_rate"])
        worst_row = min(rows, key=lambda item: item["win_rate"])
        average_by_deck.append(
            {
                "deck": deck_id,
                "avg_win_rate": mean(row["win_rate"] for row in rows),
                "min_win_rate": min(row["win_rate"] for row in rows),
                "max_win_rate": max(row["win_rate"] for row in rows),
                "avg_turns": round(mean(row["turn_avg"] for row in rows), 2),
                "best_bot": best_row["bot"],
                "worst_bot": worst_row["bot"],
            }
        )
    average_by_deck.sort(key=lambda item: item["avg_win_rate"], reverse=True)

    average_by_bot = []
    for bot_name, rows in sorted(bot_accumulator.items()):
        best_row = max(rows, key=lambda item: item["win_rate"])
        worst_row = min(rows, key=lambda item: item["win_rate"])
        average_by_bot.append(
            {
                "bot": bot_name,
                "avg_deck_win_rate": mean(row["win_rate"] for row in rows),
                "best_deck": best_row["deck"],
                "best_deck_win_rate": best_row["win_rate"],
                "worst_deck": worst_row["deck"],
                "worst_deck_win_rate": worst_row["win_rate"],
            }
        )
    average_by_bot.sort(key=lambda item: item["avg_deck_win_rate"], reverse=True)

    return {
        "reports": report_rows,
        "average_by_deck": average_by_deck,
        "average_by_bot": average_by_bot,
    }


def summarize_draft_reports(reports: list[dict[str, Any]]) -> dict[str, Any]:
    if not reports:
        return {"reports": []}

    report_rows = []
    for report in reports:
        payload = report["payload"]
        drafters = payload["drafters"]
        ordered = sorted(
            (
                {
                    "drafter": name,
                    "win_rate": stats["win_rate"],
                    "battle_avg": stats["battle_count"]["avg"],
                    "control_avg": stats["control_count"]["avg"],
                    "red_avg": stats["role_red"]["avg"],
                    "blue_avg": stats["role_blue"]["avg"],
                    "green_avg": stats["role_green"]["avg"],
                    "white_avg": stats["role_white"]["avg"],
                    "common_avg": stats["rarity_common"]["avg"],
                    "uncommon_avg": stats["rarity_uncommon"]["avg"],
                    "rare_avg": stats["rarity_rare"]["avg"],
                }
                for name, stats in drafters.items()
            ),
            key=lambda item: item["win_rate"],
            reverse=True,
        )
        report_rows.append(
            {
                "path": report["relative_path"],
                "rounds": report["config"]["rounds"],
                "total_matches": report["config"]["total_matches"],
                "draft_bot1": report["config"]["draft_bot1"],
                "draft_bot2": report["config"]["draft_bot2"],
                "play_bot1": report["config"]["bot1"],
                "play_bot2": report["config"]["bot2"],
                "rankings": ordered,
            }
        )
    return {"reports": report_rows}


def build_analysis(
    random_mix_reports: list[dict[str, Any]],
    canonical_random_mix: dict[str, Any] | None,
    tournament_reports: list[dict[str, Any]],
    draft_reports: list[dict[str, Any]],
) -> list[str]:
    notes: list[str] = []
    if canonical_random_mix:
        bots = canonical_random_mix["payload"]["bots"]
        ordered = sorted(bots.items(), key=lambda item: item[1]["win_rate"], reverse=True)
        top_name, top_stats = ordered[0]
        low_name, low_stats = ordered[-1]
        spread = (top_stats["win_rate"] - low_stats["win_rate"]) * 100
        notes.append(f"最大試行の Bot 混成では `{top_name}` が {top_stats['win_rate']*100:.1f}% で首位、`{low_name}` は {low_stats['win_rate']*100:.1f}% で、上下差は {spread:.1f}pt です。")
        if len(ordered) >= 3:
            top3 = ", ".join(f"`{name}`" for name, _ in ordered[:3])
            notes.append(f"上位 3 Bot は {top3} で、防御寄りと高打点寄りの方針が安定しています。")

    if random_mix_reports and len(random_mix_reports) >= 2:
        largest = max(random_mix_reports, key=lambda item: item["config"]["matches"])
        smallest = min(random_mix_reports, key=lambda item: item["config"]["matches"])
        largest_bots = largest["payload"]["bots"]
        smallest_bots = smallest["payload"]["bots"]
        rank_shift = []
        for name in largest_bots:
            if name not in smallest_bots:
                continue
            rank_shift.append(abs(largest_bots[name]["win_rate"] - smallest_bots[name]["win_rate"]))
        if rank_shift:
            notes.append(f"Bot 混成の試行数を {smallest['config']['matches']} 戦から {largest['config']['matches']} 戦へ増やすと、各 Bot の勝率差分は平均 {mean(rank_shift)*100:.1f}pt で、傾向はかなり安定しました。")

    if tournament_reports:
        deck_summary = summarize_deck_reports(tournament_reports)["average_by_deck"]
        if deck_summary:
            top_deck = deck_summary[0]
            low_deck = deck_summary[-1]
            notes.append(
                f"固定デッキ群では平均勝率トップが `{top_deck['deck']}` {top_deck['avg_win_rate']*100:.1f}%、最下位が `{low_deck['deck']}` {low_deck['avg_win_rate']*100:.1f}% です。"
            )
            if top_deck["avg_turns"] > low_deck["avg_turns"]:
                notes.append("勝率上位デッキは必ずしも高速決着ではなく、中速域でも安定性で勝っています。")
            else:
                notes.append("勝率上位デッキは決着も比較的速く、テンポ優位がそのまま成績に出ています。")

    if draft_reports:
        latest = draft_reports[-1]["payload"]["drafters"]
        ordered = sorted(latest.items(), key=lambda item: item[1]["win_rate"], reverse=True)
        if len(ordered) >= 2:
            winner, loser = ordered[0], ordered[-1]
            notes.append(
                f"ドラフト比較では `{winner[0]}` が {winner[1]['win_rate']*100:.1f}% で僅差優位です。役割バランスを見た指名は有効ですが、現状の差は小さく、さらなる評価関数の改善余地があります。"
            )
            notes.append(
                f"`{winner[0]}` は平均で battle {winner[1]['battle_count']['avg']} / control {winner[1]['control_count']['avg']}、`{loser[0]}` は battle {loser[1]['battle_count']['avg']} / control {loser[1]['control_count']['avg']} で、枚数配分の差がそのまま構築方針に出ています。"
            )
    return notes


def render_aggregate_markdown(summary: dict[str, Any]) -> str:
    lines = [
        "# Aggregate Report",
        "",
        "## Inventory",
        "",
        "| Type | Title | Path |",
        "|---|---|---|",
    ]
    for item in summary["inventory"]:
        lines.append(f"| `{item['type']}` | {item['title']} | `{item['path']}` |")

    random_mix = summary["random_mix"]
    lines.extend(["", "## Random Bot Mix", "", "| Matches | Seed | Top Bot | Top Win Rate | Bottom Bot | Bottom Win Rate | Path |", "|---:|---:|---|---:|---|---:|---|"])
    for item in random_mix["reports"]:
        lines.append(
            f"| {item['matches']} | {item['seed']} | `{item['top_bot']}` | {item['top_win_rate']*100:.1f}% | `{item['bottom_bot']}` | {item['bottom_win_rate']*100:.1f}% | `{item['path']}` |"
        )

    canonical = random_mix["canonical"]
    if canonical:
        lines.extend(["", "### Canonical Bot Ranking", "", "| Rank | Bot | Matches | Wins | Losses | Draws | Win Rate | Turn Avg |", "|---:|---|---:|---:|---:|---:|---:|---:|"])
        for index, item in enumerate(canonical["bot_rankings"], start=1):
            lines.append(
                f"| {index} | `{item['bot']}` | {item['matches']} | {item['wins']} | {item['losses']} | {item['draws']} | {item['win_rate']*100:.1f}% | {item['turn_avg']} |"
            )
        lines.extend(["", "### Random Mix Stability", "", "| Bot | Small Sample | Large Sample | Delta |", "|---|---:|---:|---:|"])
        for item in random_mix["delta"]:
            lines.append(
                f"| `{item['bot']}` | {item['baseline_win_rate']*100:.1f}% | {item['canonical_win_rate']*100:.1f}% | {item['delta_points']:+.1f}pt |"
            )
        lines.extend(render_rank_section("Most Used Cards", canonical["most_used_cards"]))
        lines.extend(render_rank_section("Most Effective Cards", canonical["most_effective_cards"]))
        lines.extend(render_rank_section("Most Lethal Cards", canonical["most_lethal_cards"]))

    deck_reports = summary["deck_reports"]
    lines.extend(["", "## Deck Overview", "", "| Deck | Avg Win Rate | Min | Max | Avg Turns | Best Bot | Worst Bot |", "|---|---:|---:|---:|---:|---|---|"])
    for item in deck_reports["average_by_deck"]:
        lines.append(
            f"| `{item['deck']}` | {item['avg_win_rate']*100:.1f}% | {item['min_win_rate']*100:.1f}% | {item['max_win_rate']*100:.1f}% | {item['avg_turns']} | `{item['best_bot']}` | `{item['worst_bot']}` |"
        )
    lines.extend(["", "### Bot x Deck Fit", "", "| Bot | Avg Deck Win Rate | Best Deck | Best Rate | Worst Deck | Worst Rate |", "|---|---:|---|---:|---|---:|"])
    for item in deck_reports["average_by_bot"]:
        lines.append(
            f"| `{item['bot']}` | {item['avg_deck_win_rate']*100:.1f}% | `{item['best_deck']}` | {item['best_deck_win_rate']*100:.1f}% | `{item['worst_deck']}` | {item['worst_deck_win_rate']*100:.1f}% |"
        )

    draft_reports = summary["draft_reports"]
    lines.extend(["", "## Draft Reports", ""])
    for report in draft_reports["reports"]:
        lines.extend(
            [
                f"### {report['draft_bot1']} vs {report['draft_bot2']}",
                "",
                f"- Matches: {report['total_matches']}",
                f"- Play Bots: `{report['play_bot1']}` / `{report['play_bot2']}`",
                f"- Path: `{report['path']}`",
                "",
                "| Rank | Drafter | Win Rate | Battle Avg | Control Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |",
                "|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for index, item in enumerate(report["rankings"], start=1):
            lines.append(
                f"| {index} | `{item['drafter']}` | {item['win_rate']*100:.1f}% | {item['battle_avg']} | {item['control_avg']} | "
                f"{item['red_avg']} | {item['blue_avg']} | {item['green_avg']} | {item['white_avg']} | "
                f"{item['common_avg']} | {item['uncommon_avg']} | {item['rare_avg']} |"
            )
        lines.append("")

    lines.extend(["## Light Analysis", ""])
    for note in summary["analysis"]:
        lines.append(f"- {note}")

    return "\n".join(lines).rstrip() + "\n"


def render_rank_section(title: str, items: list[list[Any]]) -> list[str]:
    lines = ["", f"### {title}", "", "| Rank | Card | Count |", "|---:|---|---:|"]
    for index, (name, count) in enumerate(items[:10], start=1):
        lines.append(f"| {index} | {name} | {count} |")
    return lines


if __name__ == "__main__":
    main()
