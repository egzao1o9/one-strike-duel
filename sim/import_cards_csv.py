from __future__ import annotations

import argparse

from sim.card_csv import import_cards_csv


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import cards from a CSV export back into cards_src.")
    parser.add_argument("--input", default="data/cards_export.csv")
    parser.add_argument("--source-dir", default="data/cards_src")
    parser.add_argument("--bundle-output", default="data/cards.json")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    count, bundle_path = import_cards_csv(args.input, args.source_dir, args.bundle_output)
    print(args.input)
    print(f"cards={count}")
    if bundle_path is not None:
        print(bundle_path)


if __name__ == "__main__":
    main()
