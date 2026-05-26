from __future__ import annotations

from dataclasses import dataclass, field
import json
from pathlib import Path
from typing import Any

CARD_TYPES = ("battle", "control")
CARD_RARITIES = ("common", "uncommon", "rare")
CARD_TOP_LEVEL_KEYS = {
    "id",
    "name",
    "type",
    "rarity",
    "attack",
    "block",
    "speed",
    "tags",
    "effects",
    "notes",
}
EFFECT_TIMINGS = ("battle", "next_turn")
EFFECT_KINDS = (
    "modify_self_attack",
    "modify_self_block",
    "modify_self_speed",
    "modify_opponent_attack",
    "modify_opponent_block",
    "modify_opponent_speed",
    "set_self_block_limit",
    "draw_cards",
    "reveal_opponent_hand_random",
)
EFFECT_KEYS = {"timing", "kind", "value"}


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
    rarity: str
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
            rarity=payload.get("rarity", "common"),
            attack=int(payload.get("attack", 0)),
            block=int(payload.get("block", 0)),
            speed=int(payload.get("speed", 0)),
            tags=tuple(payload.get("tags", [])),
            effects=tuple(Effect.from_dict(item) for item in payload.get("effects", [])),
            notes=payload.get("notes", ""),
        )


def validate_effect_payload(payload: dict[str, Any], *, source: str = "effect") -> None:
    unknown_keys = set(payload) - EFFECT_KEYS
    if unknown_keys:
        raise ValueError(f"{source}: unknown effect keys: {sorted(unknown_keys)}")
    timing = payload.get("timing")
    kind = payload.get("kind")
    if timing not in EFFECT_TIMINGS:
        raise ValueError(f"{source}: unsupported effect timing: {timing!r}")
    if kind not in EFFECT_KINDS:
        raise ValueError(f"{source}: unsupported effect kind: {kind!r}")
    value = payload.get("value", 0)
    if not isinstance(value, int):
        raise ValueError(f"{source}: effect value must be int")


def validate_card_payload(payload: dict[str, Any], *, source: str = "card") -> None:
    unknown_keys = set(payload) - CARD_TOP_LEVEL_KEYS
    if unknown_keys:
        raise ValueError(f"{source}: unknown card keys: {sorted(unknown_keys)}")

    for key in ("id", "name", "type"):
        if key not in payload:
            raise ValueError(f"{source}: missing required key: {key}")
    if not isinstance(payload["id"], str) or not payload["id"]:
        raise ValueError(f"{source}: id must be non-empty string")
    if not isinstance(payload["name"], str) or not payload["name"]:
        raise ValueError(f"{source}: name must be non-empty string")
    if payload["type"] not in CARD_TYPES:
        raise ValueError(f"{source}: unsupported card type: {payload['type']!r}")

    rarity = payload.get("rarity", "common")
    if rarity not in CARD_RARITIES:
        raise ValueError(f"{source}: unsupported rarity: {rarity!r}")

    for stat_key in ("attack", "block", "speed"):
        value = payload.get(stat_key, 0)
        if not isinstance(value, int):
            raise ValueError(f"{source}: {stat_key} must be int")

    tags = payload.get("tags", [])
    if not isinstance(tags, list) or any(not isinstance(tag, str) or not tag for tag in tags):
        raise ValueError(f"{source}: tags must be a list of non-empty strings")

    effects = payload.get("effects", [])
    if not isinstance(effects, list):
        raise ValueError(f"{source}: effects must be a list")
    for index, effect_payload in enumerate(effects):
        if not isinstance(effect_payload, dict):
            raise ValueError(f"{source}: effect at index {index} must be an object")
        validate_effect_payload(effect_payload, source=f"{source} effect[{index}]")

    notes = payload.get("notes", "")
    if not isinstance(notes, str):
        raise ValueError(f"{source}: notes must be string")


def validate_cards_payload(payload: list[dict[str, Any]], *, source: str = "cards payload") -> None:
    seen_ids: set[str] = set()
    for index, card_payload in enumerate(payload):
        if not isinstance(card_payload, dict):
            raise ValueError(f"{source}: card at index {index} must be an object")
        validate_card_payload(card_payload, source=f"{source} card[{index}]")
        card_id = card_payload["id"]
        if card_id in seen_ids:
            raise ValueError(f"{source}: duplicate card id detected: {card_id}")
        seen_ids.add(card_id)


def load_cards(path: str | Path) -> dict[str, Card]:
    file_path = Path(path)
    with file_path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, list):
        raise ValueError("cards file must contain a list")
    validate_cards_payload(payload, source=str(file_path))
    cards = {item["id"]: Card.from_dict(item) for item in payload}
    if len(cards) != len(payload):
        raise ValueError("duplicate card id detected")
    return cards
