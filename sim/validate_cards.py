from __future__ import annotations

import argparse

from sim.card_source import build_cards_payload, iter_card_source_paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate per-card source files and the generated card bundle shape.")
    parser.add_argument("--source-dir", default="data/cards_src")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source_paths = iter_card_source_paths(args.source_dir)
    payload = build_cards_payload(args.source_dir)
    print(args.source_dir)
    print(f"source_files={len(source_paths)}")
    print(f"cards={len(payload)}")
    print("status=ok")


if __name__ == "__main__":
    main()
