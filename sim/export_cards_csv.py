from __future__ import annotations

import argparse

from sim.card_csv import export_cards_csv


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export card sources to a Notion-friendly CSV.")
    parser.add_argument("--source-dir", default="data/cards_src")
    parser.add_argument("--output", default="data/cards_export.csv")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output = export_cards_csv(args.source_dir, args.output)
    print(output)


if __name__ == "__main__":
    main()
