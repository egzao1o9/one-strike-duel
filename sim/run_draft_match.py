from __future__ import annotations

import argparse
import json
from pathlib import Path
import random

from bots.registry import BOT_REGISTRY, build_bot
from draft.registry import DRAFT_BOT_REGISTRY, build_draft_bot
from engine.card import Card, load_cards
from engine.card_pool import DraftResult, load_card_pool
from engine.drafting import draft_with_bots, summarize_deck
from engine.log_formatter import render_match_log_markdown
from engine.phase_runner import MatchRunner


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run one shared-pool draft match.")
    parser.add_argument("--draft-bot1", default="StandardDraftBot", choices=sorted(DRAFT_BOT_REGISTRY))
    parser.add_argument("--draft-bot2", default="GuardDraftBot", choices=sorted(DRAFT_BOT_REGISTRY))
    parser.add_argument("--bot1", default="StandardBot", choices=sorted(BOT_REGISTRY))
    parser.add_argument("--bot2", default="StandardBot", choices=sorted(BOT_REGISTRY))
    parser.add_argument("--seed", type=int, default=71)
    parser.add_argument("--cards", default="data/cards.json")
    parser.add_argument("--pool", default="data/card_pool.json")
    parser.add_argument("--log-path", default="logs/draft_match.json")
    parser.add_argument("--markdown-path", default="logs/draft_match.md")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cards = load_cards(args.cards)
    pool = load_card_pool(args.pool, cards)
    rng = random.Random(args.seed)
    draft_bot1 = build_draft_bot(args.draft_bot1, args.seed)
    draft_bot2 = build_draft_bot(args.draft_bot2, args.seed + 1)
    draft = draft_with_bots(
        pool,
        cards,
        rng,
        draft_bot1,
        draft_bot2,
        deck_size=20,
    )

    runner = MatchRunner(
        build_bot(args.bot1, args.seed),
        build_bot(args.bot2, args.seed + 1),
        draft.deck1.id,
        draft.deck2.id,
        cards_path=args.cards,
        deck_definitions={draft.deck1.id: draft.deck1, draft.deck2.id: draft.deck2},
        match_id=f"draft_match_seed_{args.seed}",
        seed=args.seed,
    )
    result = runner.run()

    payload = {
        "draft": build_draft_payload(draft, cards, args.draft_bot1, args.draft_bot2),
        "match": result.log,
    }
    log_path = Path(args.log_path)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    markdown_path = Path(args.markdown_path)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text(render_draft_match_markdown(draft, cards, result.log), encoding="utf-8")

    print(f"winner={result.state.winner} reason={result.state.end_reason} turns={result.log['turn_count']}")
    print(log_path)
    print(markdown_path)


def build_draft_payload(
    draft: DraftResult,
    cards: dict[str, Card],
    draft_bot1: str,
    draft_bot2: str,
) -> dict[str, object]:
    return {
        "pool_id": draft.pool.id,
        "pool_name": draft.pool.name,
        "first_player": draft.first_player,
        "draft_bots": {"p1": draft_bot1, "p2": draft_bot2},
        "deck1": list(draft.deck1.all_cards),
        "deck2": list(draft.deck2.all_cards),
        "deck1_public": list(draft.deck1.public_cards),
        "deck1_hidden": list(draft.deck1.hidden_cards),
        "deck2_public": list(draft.deck2.public_cards),
        "deck2_hidden": list(draft.deck2.hidden_cards),
        "picks": [
            {
                "number": pick.number,
                "round": pick.round_number,
                "player": pick.player_id,
                "visibility": pick.visibility,
                "phase": pick.phase,
                "pick_position": pick.pick_position,
                "offer_card_ids": list(pick.offer_card_ids),
                "offer_card_names": [cards[card_id].name for card_id in pick.offer_card_ids],
                "card_id": pick.card_id,
                "card_name": cards[pick.card_id].name,
            }
            for pick in draft.picks
        ],
    }


def render_draft_match_markdown(draft: DraftResult, cards: dict[str, Card], match_log: dict[str, object]) -> str:
    deck1_summary = summarize_deck(draft.deck1.all_cards, cards)
    deck2_summary = summarize_deck(draft.deck2.all_cards, cards)
    lines = [
        "# Draft Match",
        "",
        "## Draft Summary",
        "",
        f"- Pool: `{draft.pool.id}` ({draft.pool.name})",
        f"- First Pick: `{draft.first_player}`",
        f"- Deck Size: {len(draft.deck1.all_cards)}",
        f"- P1 Public / Hidden: {len(draft.deck1.public_cards)} / {len(draft.deck1.hidden_cards)}",
        f"- P2 Public / Hidden: {len(draft.deck2.public_cards)} / {len(draft.deck2.hidden_cards)}",
        "",
        "## Role Balance",
        "",
        "| Deck | Battle | Control | Red | Blue | Green | White | Common | Uncommon | Rare |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        _render_summary_row("P1", deck1_summary),
        _render_summary_row("P2", deck2_summary),
        "",
        "## Drafted Decks",
        "",
    ]
    lines.extend(render_deck_table("P1 Public Deck", draft.deck1.public_cards, cards))
    lines.append("")
    lines.extend(render_deck_table("P1 Hidden Deck", draft.deck1.hidden_cards, cards))
    lines.append("")
    lines.extend(render_deck_table("P2 Public Deck", draft.deck2.public_cards, cards))
    lines.append("")
    lines.extend(render_deck_table("P2 Hidden Deck", draft.deck2.hidden_cards, cards))
    lines.append("")
    lines.extend(
        [
            "## Pick Order",
            "",
            "| Pick | Round | Player | Phase | Position | Card | ID | Rarity | Offer |",
            "|---:|---:|---|---|---:|---|---|---|---|",
        ]
    )
    for pick in draft.picks:
        card = cards[pick.card_id]
        lines.append(
            f"| {pick.number} | {pick.round_number} | `{pick.player_id}` | `{pick.visibility}` | {pick.pick_position} | "
            f"{card.name} | `{card.id}` | `{card.rarity}` | "
            f"{', '.join(cards[card_id].name for card_id in pick.offer_card_ids)} |"
        )
    lines.extend(["", "## Match Log", "", render_match_log_markdown(match_log).rstrip(), ""])
    return "\n".join(lines).rstrip() + "\n"


def render_deck_table(title: str, card_ids: tuple[str, ...], cards: dict[str, Card]) -> list[str]:
    lines = [
        f"### {title}",
        "",
        "| Count | Card | ID | Rarity | Type | A | B | S |",
        "|---:|---|---|---|---|---:|---:|---:|",
    ]
    counts: dict[str, int] = {}
    for card_id in card_ids:
        counts[card_id] = counts.get(card_id, 0) + 1
    for card_id in sorted(counts):
        card = cards[card_id]
        lines.append(
            f"| {counts[card_id]} | {card.name} | `{card.id}` | `{card.rarity}` | `{card.type}` | {card.attack} | {card.block} | {card.speed} |"
        )
    return lines


def _render_summary_row(label: str, summary) -> str:
    return (
        f"| {label} | {summary.battle_count} | {summary.control_count} | "
        f"{summary.role_counts['red']} | {summary.role_counts['blue']} | "
        f"{summary.role_counts['green']} | {summary.role_counts['white']} | "
        f"{summary.rarity_counts['common']} | {summary.rarity_counts['uncommon']} | {summary.rarity_counts['rare']} |"
    )


if __name__ == "__main__":
    main()
