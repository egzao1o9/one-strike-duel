from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import random

from engine.card import Card


@dataclass(frozen=True)
class DeckDefinition:
    id: str
    name: str
    public_cards: tuple[str, ...]
    hidden_cards: tuple[str, ...]

    @property
    def all_cards(self) -> tuple[str, ...]:
        return self.public_cards + self.hidden_cards


def load_decks(path: str | Path) -> dict[str, DeckDefinition]:
    file_path = Path(path)
    with file_path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    decks = {
        item["id"]: DeckDefinition(
            id=item["id"],
            name=item["name"],
            public_cards=tuple(item.get("public_cards", [])),
            hidden_cards=tuple(item.get("hidden_cards", [])),
        )
        for item in payload
    }
    if len(decks) != len(payload):
        raise ValueError("duplicate deck id detected")
    return decks


def build_draw_pile(
    deck: DeckDefinition,
    cards: dict[str, Card],
    rng: random.Random,
    *,
    shuffle: bool = True,
) -> list[Card]:
    pile = [cards[card_id] for card_id in deck.all_cards]
    if shuffle:
        rng.shuffle(pile)
    return pile
