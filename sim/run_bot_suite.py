from __future__ import annotations

import argparse
import json
from pathlib import Path

from bots.registry import BOT_REGISTRY
from sim.run_deck_tournament import run_tournament


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run tournaments for multiple bots and generate a comparison index.")
    parser.add_argument("--bots", nargs="*", default=None, choices=sorted(BOT_REGISTRY))
    parser.add_argument("--matches-per-pair", type=int, default=5)
    parser.add_argument("--seed", type=int, default=41)
    parser.add_argument("--output-dir", default=None)
    parser.add_argument("--keep-match-logs", type=int, default=100)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    bot_names = args.bots or sorted(BOT_REGISTRY)
    root_dir = Path(args.output_dir or f"logs/bot_suite_x{args.matches_per_pair}_seed{args.seed}")
    root_dir.mkdir(parents=True, exist_ok=True)

    summaries: list[dict[str, object]] = []
    for index, bot_name in enumerate(bot_names):
        summary_md, total_matches = run_tournament(
            bot_name,
            args.matches_per_pair,
            args.seed + index * 1000,
            str(root_dir / bot_name),
            args.keep_match_logs,
        )
        summary_json_path = summary_md.with_name("summary.json")
        summary = json.loads(summary_json_path.read_text(encoding="utf-8"))
        summaries.append(
            {
                "bot": bot_name,
                "summary_md": summary_md.relative_to(root_dir).as_posix(),
                "total_matches": total_matches,
                "decks": summary["decks"],
            }
        )

    index_path = root_dir / "index.md"
    index_path.write_text(render_index_markdown(summaries), encoding="utf-8")
    print(index_path)


def render_index_markdown(summaries: list[dict[str, object]]) -> str:
    deck_ids = sorted(next(iter(summaries))["decks"].keys()) if summaries else []
    lines = [
        "# Bot Suite Report",
        "",
        "## Bot Summaries",
        "",
        "| Bot | Matches | Report | " + " | ".join(f"{deck} Win Rate" for deck in deck_ids) + " |",
        "|---|---:|---|" + "|".join(["---:"] * len(deck_ids)) + "|",
    ]
    for summary in summaries:
        deck_columns = []
        for deck_id in deck_ids:
            win_rate = summary["decks"][deck_id]["win_rate"]
            deck_columns.append(f"{win_rate * 100:.1f}%")
        lines.append(
            f"| `{summary['bot']}` | {summary['total_matches']} | [{summary['bot']}]({summary['summary_md']}) | "
            + " | ".join(deck_columns)
            + " |"
        )
    return "\n".join(lines).rstrip() + "\n"


if __name__ == "__main__":
    main()
