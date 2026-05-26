from __future__ import annotations

import argparse

from sim.card_source import build_cards_payload, write_cards_payload


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build data/cards.json from per-card source files.")
    parser.add_argument("--source-dir", default="data/cards_src")
    parser.add_argument("--output", default="data/cards.json")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    payload = build_cards_payload(args.source_dir)
    output_path = write_cards_payload(payload, args.output)
    print(output_path)
    print(f"cards={len(payload)}")


if __name__ == "__main__":
    main()
