from __future__ import annotations

import argparse
import json
from pathlib import Path

from engine.card import load_cards
from engine.card_pool import build_card_pool_payload, build_default_card_pool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build card_pool.json from current card rarities.")
    parser.add_argument("--cards", default="data/cards.json")
    parser.add_argument("--output", default="data/card_pool.json")
    parser.add_argument("--pool-id", default="base_pool")
    parser.add_argument("--pool-name", default="Base Card Pool")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cards = load_cards(args.cards)
    pool = build_default_card_pool(cards, pool_id=args.pool_id, name=args.pool_name)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(build_card_pool_payload(pool), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(output_path)


if __name__ == "__main__":
    main()
