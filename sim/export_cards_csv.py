from __future__ import annotations

import argparse

from sim.card_csv import export_cards_csv_pair


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="カード定義を Cards / CardEffects の2CSVへ書き出します。")
    parser.add_argument("--source-dir", default="data/cards_src")
    parser.add_argument("--cards-output", default="data/cards_export.csv")
    parser.add_argument("--effects-output", default="data/card_effects_export.csv")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cards_output, effects_output = export_cards_csv_pair(
        args.source_dir,
        args.cards_output,
        args.effects_output,
    )
    print(cards_output)
    print(effects_output)


if __name__ == "__main__":
    main()
