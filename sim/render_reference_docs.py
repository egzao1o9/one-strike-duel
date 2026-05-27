from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

from engine.card import Card, load_cards
from engine.card_pool import CardPoolDefinition, load_card_pool
from engine.deck import DeckDefinition, load_decks


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render card and deck reference markdown files.")
    parser.add_argument("--cards", default="data/cards.json")
    parser.add_argument("--decks", default="data/decks.json")
    parser.add_argument("--pool", default="data/card_pool.json")
    parser.add_argument("--cards-output", default="docs/cards_reference.md")
    parser.add_argument("--decks-output", default="docs/decks_reference.md")
    parser.add_argument("--pool-output", default="docs/card_pool_reference.md")
    return parser.parse_args()


def render_cards_markdown(cards: dict[str, Card]) -> str:
    battle_cards = [card for card in cards.values() if card.type == "battle"]
    control_cards = [card for card in cards.values() if card.type == "control"]
    blessing_cards = [card for card in cards.values() if card.type == "blessing"]

    lines = [
        "# Cards Reference",
        "",
        "## Summary",
        "",
        f"- Total Cards: {len(cards)}",
        f"- Battle Cards: {len(battle_cards)}",
        f"- Control Cards: {len(control_cards)}",
        f"- Blessing Cards: {len(blessing_cards)}",
        "",
        "## Card List",
        "",
        "| ID | Name | Type | Rarity | Attack | Block | Speed | Tags | Text |",
        "|---|---|---|---|---:|---:|---:|---|---|",
    ]

    for card in sorted(cards.values(), key=lambda item: (item.type, item.id)):
        tags = ", ".join(card.tags) if card.tags else "-"
        lines.append(
            f"| `{card.id}` | {card.name} | `{card.type}` | `{card.rarity}` | {card.attack} | {card.block} | {card.speed} | {tags} | {card.public_text or '-'} |"
        )

    lines.extend(["", "## Details", ""])

    for card in sorted(cards.values(), key=lambda item: (item.type, item.id)):
        lines.extend(_render_card_detail(card))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def _render_card_detail(card: Card) -> list[str]:
    tags = ", ".join(card.tags) if card.tags else "-"
    lines = [
        f"### {card.name}",
        "",
        f"- ID: `{card.id}`",
        f"- Type: `{card.type}`",
        f"- Rarity: `{card.rarity}`",
        f"- Stats: `A={card.attack} / B={card.block} / S={card.speed}`",
        f"- Tags: {tags}",
        f"- Text: {card.public_text or '-'}",
        f"- Zones: `play={card.play_zone} / after={card.after_play_zone} / slot={card.slot_type or '-'} `",
        f"- Notes: {card.notes or '-'}",
    ]
    if card.effects:
        lines.append("- Effects:")
        for effect in card.effects:
            if effect.effect_type:
                lines.append(
                    f"  - `{effect.trigger}` / `{effect.effect_type}` / target=`{effect.target}` / stat=`{effect.stat}` / value={effect.value} / duration=`{effect.duration or '-'} ` / active_zone=`{effect.active_zone or '-'} `"
                )
            else:
                lines.append(f"  - `{effect.timing}` / `{effect.kind}` / value={effect.value}")
    else:
        lines.append("- Effects: none")
    return lines


def render_decks_markdown(decks: dict[str, DeckDefinition], cards: dict[str, Card]) -> str:
    lines = [
        "# Decks Reference",
        "",
        "## Summary",
        "",
        "| ID | Name | Total | Public | Hidden | Battle | Control | Blessing |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]

    for deck in sorted(decks.values(), key=lambda item: item.id):
        battle_count = sum(1 for card_id in deck.all_cards if cards[card_id].type == "battle")
        control_count = sum(1 for card_id in deck.all_cards if cards[card_id].type == "control")
        blessing_count = sum(1 for card_id in deck.all_cards if cards[card_id].type == "blessing")
        lines.append(
            f"| `{deck.id}` | {deck.name} | {len(deck.all_cards)} | {len(deck.public_cards)} | {len(deck.hidden_cards)} | {battle_count} | {control_count} | {blessing_count} |"
        )

    lines.extend(["", "## Details", ""])

    for deck in sorted(decks.values(), key=lambda item: item.id):
        lines.extend(_render_deck_detail(deck, cards))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_pool_markdown(pool: CardPoolDefinition, cards: dict[str, Card]) -> str:
    lines = [
        "# Card Pool Reference",
        "",
        "## Summary",
        "",
        f"- Pool ID: `{pool.id}`",
        f"- Pool Name: {pool.name}",
        f"- Total Copies: {pool.total_cards}",
        "",
        "| Card | ID | Rarity | Copies | Type | A | B | S |",
        "|---|---|---|---:|---|---:|---:|---:|",
    ]
    for entry in sorted(pool.entries, key=lambda item: (cards[item.card_id].rarity, cards[item.card_id].type, item.card_id)):
        card = cards[entry.card_id]
        lines.append(
            f"| {card.name} | `{card.id}` | `{card.rarity}` | {entry.count} | `{card.type}` | {card.attack} | {card.block} | {card.speed} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def _render_deck_detail(deck: DeckDefinition, cards: dict[str, Card]) -> list[str]:
    all_counter = Counter(deck.all_cards)
    public_counter = Counter(deck.public_cards)
    hidden_counter = Counter(deck.hidden_cards)
    battle_count = sum(1 for card_id in deck.all_cards if cards[card_id].type == "battle")
    control_count = sum(1 for card_id in deck.all_cards if cards[card_id].type == "control")
    blessing_count = sum(1 for card_id in deck.all_cards if cards[card_id].type == "blessing")

    lines = [
        f"### {deck.name}",
        "",
        f"- ID: `{deck.id}`",
        f"- Total Cards: {len(deck.all_cards)}",
        f"- Public Cards: {len(deck.public_cards)}",
        f"- Hidden Cards: {len(deck.hidden_cards)}",
        f"- Battle / Control / Blessing: {battle_count} / {control_count} / {blessing_count}",
        "",
        "#### Public Cards",
        "",
    ]

    lines.extend(_render_deck_card_table(public_counter, cards))
    lines.extend(["", "#### Hidden Cards", ""])
    lines.extend(_render_deck_card_table(hidden_counter, cards))
    lines.extend(["", "#### Full Composition", ""])
    lines.extend(_render_deck_card_table(all_counter, cards))
    return lines


def _render_deck_card_table(counter: Counter[str], cards: dict[str, Card]) -> list[str]:
    lines = [
        "| Count | Name | ID | Type | Rarity | A | B | S |",
        "|---:|---|---|---|---|---:|---:|---:|",
    ]
    for card_id, count in sorted(counter.items(), key=lambda item: (cards[item[0]].type, item[0])):
        card = cards[card_id]
        lines.append(
            f"| {count} | {card.name} | `{card.id}` | `{card.type}` | `{card.rarity}` | {card.attack} | {card.block} | {card.speed} |"
        )
    return lines


def write_text(path: str | Path, text: str) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(text, encoding="utf-8")


def main() -> None:
    args = parse_args()
    cards = load_cards(args.cards)
    decks = load_decks(args.decks)
    pool = load_card_pool(args.pool, cards)
    cards_markdown = render_cards_markdown(cards)
    decks_markdown = render_decks_markdown(decks, cards)
    pool_markdown = render_pool_markdown(pool, cards)
    write_text(args.cards_output, cards_markdown)
    write_text(args.decks_output, decks_markdown)
    write_text(args.pool_output, pool_markdown)
    print(args.cards_output)
    print(args.decks_output)
    print(args.pool_output)


if __name__ == "__main__":
    main()
