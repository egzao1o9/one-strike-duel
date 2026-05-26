from __future__ import annotations

import argparse

from sim.build_cards import main as build_cards_main
from sim.render_reference_docs import main as render_reference_docs_main
from sim.sync_card_pool import main as sync_card_pool_main
from sim.validate_cards import main as validate_cards_main


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Refresh generated card artifacts from per-card source files."
    )
    return parser.parse_args()


def main() -> None:
    parse_args()
    validate_cards_main()
    build_cards_main()
    sync_card_pool_main()
    render_reference_docs_main()


if __name__ == "__main__":
    main()
