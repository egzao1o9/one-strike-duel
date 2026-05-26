from __future__ import annotations

from dataclasses import dataclass, field
import json
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Effect:
    timing: str
    kind: str
    value: int = 0

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "Effect":
        return cls(
            timing=payload["timing"],
            kind=payload["kind"],
            value=int(payload.get("value", 0)),
        )


@dataclass(frozen=True)
class Card:
    id: str
    name: str
    type: str
    attack: int
    block: int
    speed: int
    tags: tuple[str, ...] = field(default_factory=tuple)
    effects: tuple[Effect, ...] = field(default_factory=tuple)
    notes: str = ""

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "Card":
        return cls(
            id=payload["id"],
            name=payload["name"],
            type=payload["type"],
            attack=int(payload.get("attack", 0)),
            block=int(payload.get("block", 0)),
            speed=int(payload.get("speed", 0)),
            tags=tuple(payload.get("tags", [])),
            effects=tuple(Effect.from_dict(item) for item in payload.get("effects", [])),
            notes=payload.get("notes", ""),
        )


def load_cards(path: str | Path) -> dict[str, Card]:
    file_path = Path(path)
    with file_path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    cards = {item["id"]: Card.from_dict(item) for item in payload}
    if len(cards) != len(payload):
        raise ValueError("duplicate card id detected")
    return cards
