from __future__ import annotations

import argparse

from sim.card_csv import import_cards_csv


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Cards / CardEffects の2CSVを cards_src に取り込みます。")
    parser.add_argument("--cards-input", default="data/cards_export.csv")
    parser.add_argument("--effects-input", default="data/card_effects_export.csv")
    parser.add_argument("--source-dir", default="data/cards_src")
    parser.add_argument("--bundle-output", default="data/cards.json")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    count, bundle_path = import_cards_csv(
        args.cards_input,
        args.source_dir,
        args.bundle_output,
        args.effects_input,
    )
    print(args.cards_input)
    print(args.effects_input)
    print(f"cards={count}")
    if bundle_path is not None:
        print(bundle_path)


if __name__ == "__main__":
    main()
