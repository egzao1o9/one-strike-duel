from __future__ import annotations

import argparse
from pathlib import Path

from engine.log_formatter import load_match_log, render_match_log_markdown, render_match_log_text


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render a JSON match log into human-readable text.")
    parser.add_argument("--input", default="logs/match_log.json")
    parser.add_argument("--output", default=None)
    parser.add_argument("--format", choices=["text", "markdown"], default="text")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    payload = load_match_log(args.input)
    rendered = render_match_log_markdown(payload) if args.format == "markdown" else render_match_log_text(payload)
    print(rendered, end="")

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()
