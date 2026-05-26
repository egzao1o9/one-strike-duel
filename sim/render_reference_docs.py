from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

from engine.card import Card, load_cards
from engine.deck import DeckDefinition, load_decks


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render card and deck reference markdown files.")
    parser.add_argument("--cards", default="data/cards.json")
    parser.add_argument("--decks", default="data/decks.json")
    parser.add_argument("--cards-output", default="docs/cards_reference.md")
    parser.add_argument("--decks-output", default="docs/decks_reference.md")
    return parser.parse_args()


def render_cards_markdown(cards: dict[str, Card]) -> str:
    battle_cards = [card for card in cards.values() if card.type == "battle"]
    control_cards = [card for card in cards.values() if card.type == "control"]

    lines = [
        "# Cards Reference",
        "",
        "## Summary",
        "",
        f"- Total Cards: {len(cards)}",
        f"- Battle Cards: {len(battle_cards)}",
        f"- Control Cards: {len(control_cards)}",
        "",
        "## Card List",
        "",
        "| ID | Name | Type | Attack | Block | Speed | Tags |",
        "|---|---|---|---:|---:|---:|---|",
    ]

    for card in sorted(cards.values(), key=lambda item: (item.type, item.id)):
        tags = ", ".join(card.tags) if card.tags else "-"
        lines.append(
            f"| `{card.id}` | {card.name} | `{card.type}` | {card.attack} | {card.block} | {card.speed} | {tags} |"
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
        f"- Stats: `A={card.attack} / B={card.block} / S={card.speed}`",
        f"- Tags: {tags}",
        f"- Notes: {card.notes or '-'}",
    ]
    if card.effects:
        lines.append("- Effects:")
        for effect in card.effects:
            lines.append(f"  - `{effect.timing}` / `{effect.kind}` / value={effect.value}")
    else:
        lines.append("- Effects: なし")
    return lines


def render_decks_markdown(decks: dict[str, DeckDefinition], cards: dict[str, Card]) -> str:
    lines = [
        "# Decks Reference",
        "",
        "## Summary",
        "",
        "| ID | Name | Total | Public | Hidden | Battle | Control |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]

    for deck in sorted(decks.values(), key=lambda item: item.id):
        battle_count = sum(1 for card_id in deck.all_cards if cards[card_id].type == "battle")
        control_count = sum(1 for card_id in deck.all_cards if cards[card_id].type == "control")
        lines.append(
            f"| `{deck.id}` | {deck.name} | {len(deck.all_cards)} | {len(deck.public_cards)} | {len(deck.hidden_cards)} | {battle_count} | {control_count} |"
        )

    lines.extend(["", "## Details", ""])

    for deck in sorted(decks.values(), key=lambda item: item.id):
        lines.extend(_render_deck_detail(deck, cards))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def _render_deck_detail(deck: DeckDefinition, cards: dict[str, Card]) -> list[str]:
    all_counter = Counter(deck.all_cards)
    public_counter = Counter(deck.public_cards)
    hidden_counter = Counter(deck.hidden_cards)
    battle_count = sum(1 for card_id in deck.all_cards if cards[card_id].type == "battle")
    control_count = sum(1 for card_id in deck.all_cards if cards[card_id].type == "control")

    lines = [
        f"### {deck.name}",
        "",
        f"- ID: `{deck.id}`",
        f"- Total Cards: {len(deck.all_cards)}",
        f"- Public Cards: {len(deck.public_cards)}",
        f"- Hidden Cards: {len(deck.hidden_cards)}",
        f"- Battle / Control: {battle_count} / {control_count}",
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
        "| Count | Name | ID | Type | A | B | S |",
        "|---:|---|---|---|---:|---:|---:|",
    ]
    for card_id, count in sorted(counter.items(), key=lambda item: (cards[item[0]].type, item[0])):
        card = cards[card_id]
        lines.append(
            f"| {count} | {card.name} | `{card.id}` | `{card.type}` | {card.attack} | {card.block} | {card.speed} |"
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
    cards_markdown = render_cards_markdown(cards)
    decks_markdown = render_decks_markdown(decks, cards)
    write_text(args.cards_output, cards_markdown)
    write_text(args.decks_output, decks_markdown)
    print(args.cards_output)
    print(args.decks_output)


if __name__ == "__main__":
    main()
