from __future__ import annotations

from dataclasses import dataclass, field
from dataclasses import replace
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
    metadata: dict[str, object] = field(default_factory=dict)

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
            metadata=dict(item.get("metadata", {})),
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
    source_labels = _build_source_labels(deck)
    pile = [replace(cards[card_id], instance_source=source_labels[index]) for index, card_id in enumerate(deck.all_cards)]
    if shuffle:
        rng.shuffle(pile)
    return pile


def _build_source_labels(deck: DeckDefinition) -> list[str]:
    public_normal = tuple(deck.metadata.get("public_normal_cards", ()))
    hidden_normal = tuple(deck.metadata.get("hidden_normal_cards", ()))
    public_rare = tuple(deck.metadata.get("public_rare_cards", ()))
    hidden_rare = tuple(deck.metadata.get("hidden_rare_cards", ()))
    if public_normal or hidden_normal or public_rare or hidden_rare:
        return (
            ["public"] * len(public_normal)
            + ["public_rare"] * len(public_rare)
            + ["hidden"] * len(hidden_normal)
            + ["hidden_rare"] * len(hidden_rare)
        )
    return ["public"] * len(deck.public_cards) + ["hidden"] * len(deck.hidden_cards)
