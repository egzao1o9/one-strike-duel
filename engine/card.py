from __future__ import annotations

from dataclasses import dataclass, field
import json
from pathlib import Path
from typing import Any

CARD_TYPES = ("battle", "control", "blessing")
CARD_RARITIES = ("common", "uncommon", "rare")
CARD_ZONES = ("set", "instant", "discard", "hand", "deck", "blessing_zone")
CARD_SLOT_TYPES = ("", "blessing")
CARD_TOP_LEVEL_KEYS = {
    "id",
    "name",
    "type",
    "card_type",
    "rarity",
    "attack",
    "block",
    "speed",
    "tags",
    "effects",
    "notes",
    "public_text",
    "text",
    "enabled",
    "play_zone",
    "after_play_zone",
    "slot_type",
    "flavor_text",
    "base",
    "zones",
}
LEGACY_EFFECT_TIMINGS = ("battle", "next_turn")
LEGACY_EFFECT_KINDS = (
    "modify_self_attack",
    "modify_self_block",
    "modify_self_speed",
    "modify_opponent_attack",
    "modify_opponent_block",
    "modify_opponent_speed",
    "negate_opponent_first_card",
    "set_self_block_limit",
    "draw_cards",
    "reveal_opponent_hand_random",
)
EFFECT_TRIGGERS = (
    "passive",
    "on_reveal",
    "on_battle_start",
    "on_battle_calculate",
    "on_battle_resolve",
    "on_turn_start",
    "on_draw_step",
    "on_turn_end",
    "on_play",
    "on_discard",
    "on_mulligan",
    "next_turn",
)
EFFECT_TYPES = (
    "modify_total_stat",
    "modify_card_stat",
    "modify_rule_value",
    "draw_cards",
    "discard_cards",
    "reveal_cards",
    "negate_card",
    "adjust_mulligan",
    "adjust_draw_limit",
    "replace_zone_card",
    "custom",
)
EFFECT_TARGETS = (
    "self_player",
    "opponent_player",
    "both_players",
    "self_total",
    "opponent_total",
    "self_card",
    "opponent_card",
    "self_set_cards",
    "opponent_set_cards",
    "self_hand",
    "opponent_hand",
    "self_deck",
    "opponent_deck",
    "self_discard",
    "opponent_discard",
    "self_blessing_zone",
    "opponent_blessing_zone",
)
EFFECT_STATS = (
    "",
    "attack",
    "block",
    "speed",
    "draw_per_turn",
    "hand_limit",
    "mulligan_count",
    "battle_card_limit",
)
EFFECT_DURATIONS = (
    "",
    "instant",
    "current_battle",
    "current_turn",
    "next_turn",
    "while_in_zone",
    "until_used",
    "permanent",
)
EFFECT_ACTIVE_ZONES = ("", "set", "hand", "deck", "discard", "blessing_zone")
EFFECT_KEYS = {
    "id",
    "seq",
    "enabled",
    "trigger",
    "priority",
    "effect_type",
    "target",
    "stat",
    "value",
    "value2",
    "count",
    "duration",
    "active_zone",
    "condition",
    "keyword",
    "display_text",
    "text",
    "params_json",
    "notes",
    "timing",
    "kind",
}


def _normalize_card_type(payload: dict[str, Any]) -> str:
    return str(payload.get("card_type") or payload.get("type") or "").strip()


def _normalize_base_value(payload: dict[str, Any], key: str) -> int:
    if key in payload:
        return int(payload.get(key, 0))
    base = payload.get("base", {})
    if isinstance(base, dict):
        return int(base.get(key, 0))
    return 0


def _normalize_zone_value(payload: dict[str, Any], key: str, default: str = "") -> str:
    if key in payload:
        return str(payload.get(key, default) or default)
    zones = payload.get("zones", {})
    if isinstance(zones, dict):
        return str(zones.get(key, default) or default)
    return default


def default_play_zone(card_type: str) -> str:
    if card_type == "battle":
        return "set"
    if card_type == "control":
        return "instant"
    if card_type == "blessing":
        return "blessing_zone"
    return ""


def default_after_play_zone(card_type: str) -> str:
    if card_type == "battle":
        return "discard"
    if card_type == "control":
        return "discard"
    if card_type == "blessing":
        return "blessing_zone"
    return ""


def default_slot_type(card_type: str) -> str:
    return "blessing" if card_type == "blessing" else ""


@dataclass(frozen=True)
class Effect:
    trigger: str
    effect_type: str = ""
    target: str = ""
    stat: str = ""
    value: int = 0
    value2: int = 0
    count: int = 0
    duration: str = ""
    active_zone: str = ""
    condition: str = ""
    keyword: str = ""
    display_text: str = ""
    params_json: str = ""
    notes: str = ""
    id: str = ""
    seq: int = 1
    enabled: bool = True
    priority: int = 100
    timing: str = ""
    kind: str = ""

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "Effect":
        trigger = str(payload.get("trigger") or payload.get("timing") or "").strip()
        display_text = str(payload.get("display_text") or payload.get("text") or "").strip()
        return cls(
            id=str(payload.get("id", "") or ""),
            seq=int(payload.get("seq", 1) or 1),
            enabled=bool(payload.get("enabled", True)),
            trigger=trigger,
            priority=int(payload.get("priority", 100) or 100),
            effect_type=str(payload.get("effect_type", "") or ""),
            target=str(payload.get("target", "") or ""),
            stat=str(payload.get("stat", "") or ""),
            value=int(payload.get("value", 0) or 0),
            value2=int(payload.get("value2", 0) or 0),
            count=int(payload.get("count", 0) or 0),
            duration=str(payload.get("duration", "") or ""),
            active_zone=str(payload.get("active_zone", "") or ""),
            condition=str(payload.get("condition", "") or ""),
            keyword=str(payload.get("keyword", "") or ""),
            display_text=display_text,
            params_json=str(payload.get("params_json", "") or ""),
            notes=str(payload.get("notes", "") or ""),
            timing=str(payload.get("timing", "") or ""),
            kind=str(payload.get("kind", "") or ""),
        )

    def is_legacy(self) -> bool:
        return bool(self.kind)

    def is_active_in_zone(self, zone_name: str) -> bool:
        if self.duration != "while_in_zone":
            return True
        return self.active_zone == zone_name

    def legacy_key(self) -> str:
        return self.kind or ""


@dataclass(frozen=True)
class Card:
    id: str
    name: str
    card_type: str
    rarity: str
    attack: int
    block: int
    speed: int
    tags: tuple[str, ...] = field(default_factory=tuple)
    effects: tuple[Effect, ...] = field(default_factory=tuple)
    public_text: str = ""
    enabled: bool = True
    play_zone: str = ""
    after_play_zone: str = ""
    slot_type: str = ""
    flavor_text: str = ""
    notes: str = ""
    instance_source: str = ""

    @property
    def type(self) -> str:
        return self.card_type

    @property
    def text(self) -> str:
        return self.public_text

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "Card":
        card_type = _normalize_card_type(payload)
        return cls(
            id=payload["id"],
            name=payload["name"],
            card_type=card_type,
            rarity=payload.get("rarity", "common"),
            attack=_normalize_base_value(payload, "attack"),
            block=_normalize_base_value(payload, "block"),
            speed=_normalize_base_value(payload, "speed"),
            tags=tuple(payload.get("tags", [])),
            effects=tuple(Effect.from_dict(item) for item in payload.get("effects", [])),
            public_text=str(payload.get("public_text") or payload.get("text") or ""),
            enabled=bool(payload.get("enabled", True)),
            play_zone=_normalize_zone_value(payload, "play_zone", default_play_zone(card_type)),
            after_play_zone=_normalize_zone_value(payload, "after_play_zone", default_after_play_zone(card_type)),
            slot_type=_normalize_zone_value(payload, "slot_type", default_slot_type(card_type)),
            flavor_text=str(payload.get("flavor_text", "") or ""),
            notes=payload.get("notes", ""),
        )


def validate_effect_payload(payload: dict[str, Any], *, source: str = "effect") -> None:
    unknown_keys = set(payload) - EFFECT_KEYS
    if unknown_keys:
        raise ValueError(f"{source}: unknown effect keys: {sorted(unknown_keys)}")
    trigger = str(payload.get("trigger") or payload.get("timing") or "").strip()
    effect_type = str(payload.get("effect_type", "") or "").strip()
    kind = str(payload.get("kind", "") or "").strip()
    if not trigger:
        raise ValueError(f"{source}: missing trigger/timing")
    if effect_type:
        if trigger not in EFFECT_TRIGGERS:
            raise ValueError(f"{source}: unsupported trigger: {trigger!r}")
        if effect_type not in EFFECT_TYPES:
            raise ValueError(f"{source}: unsupported effect_type: {effect_type!r}")
        target = str(payload.get("target", "") or "")
        if target and target not in EFFECT_TARGETS:
            raise ValueError(f"{source}: unsupported target: {target!r}")
        stat = str(payload.get("stat", "") or "")
        if stat not in EFFECT_STATS:
            raise ValueError(f"{source}: unsupported stat: {stat!r}")
        duration = str(payload.get("duration", "") or "")
        if duration and duration not in EFFECT_DURATIONS:
            raise ValueError(f"{source}: unsupported duration: {duration!r}")
        active_zone = str(payload.get("active_zone", "") or "")
        if active_zone and active_zone not in EFFECT_ACTIVE_ZONES:
            raise ValueError(f"{source}: unsupported active_zone: {active_zone!r}")
        if duration == "while_in_zone" and not active_zone:
            raise ValueError(f"{source}: active_zone is required for while_in_zone")
    else:
        if trigger not in LEGACY_EFFECT_TIMINGS:
            raise ValueError(f"{source}: unsupported legacy timing: {trigger!r}")
        if kind not in LEGACY_EFFECT_KINDS:
            raise ValueError(f"{source}: unsupported legacy kind: {kind!r}")
    for key in ("value", "value2", "count", "seq", "priority"):
        if key in payload and payload[key] not in ("", None) and not isinstance(payload[key], int):
            raise ValueError(f"{source}: {key} must be int")


def validate_card_payload(payload: dict[str, Any], *, source: str = "card") -> None:
    unknown_keys = set(payload) - CARD_TOP_LEVEL_KEYS
    if unknown_keys:
        raise ValueError(f"{source}: unknown card keys: {sorted(unknown_keys)}")

    for key in ("id", "name"):
        if key not in payload:
            raise ValueError(f"{source}: missing required key: {key}")
    if not isinstance(payload["id"], str) or not payload["id"]:
        raise ValueError(f"{source}: id must be non-empty string")
    if not isinstance(payload["name"], str) or not payload["name"]:
        raise ValueError(f"{source}: name must be non-empty string")

    card_type = _normalize_card_type(payload)
    if card_type not in CARD_TYPES:
        raise ValueError(f"{source}: unsupported card type: {card_type!r}")

    rarity = payload.get("rarity", "common")
    if rarity not in CARD_RARITIES:
        raise ValueError(f"{source}: unsupported rarity: {rarity!r}")

    for stat_key in ("attack", "block", "speed"):
        try:
            _normalize_base_value(payload, stat_key)
        except Exception as exc:  # noqa: BLE001
            raise ValueError(f"{source}: {stat_key} must be int") from exc

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

    public_text = payload.get("public_text", payload.get("text", ""))
    if not isinstance(public_text, str):
        raise ValueError(f"{source}: public_text must be string")
    if "enabled" in payload and not isinstance(payload["enabled"], bool):
        raise ValueError(f"{source}: enabled must be bool")

    play_zone = _normalize_zone_value(payload, "play_zone", default_play_zone(card_type))
    after_play_zone = _normalize_zone_value(payload, "after_play_zone", default_after_play_zone(card_type))
    slot_type = _normalize_zone_value(payload, "slot_type", default_slot_type(card_type))
    if play_zone not in CARD_ZONES:
        raise ValueError(f"{source}: unsupported play_zone: {play_zone!r}")
    if after_play_zone not in CARD_ZONES:
        raise ValueError(f"{source}: unsupported after_play_zone: {after_play_zone!r}")
    if slot_type not in CARD_SLOT_TYPES:
        raise ValueError(f"{source}: unsupported slot_type: {slot_type!r}")
    if card_type == "blessing":
        if play_zone != "blessing_zone":
            raise ValueError(f"{source}: blessing play_zone must be blessing_zone")
        if after_play_zone != "blessing_zone":
            raise ValueError(f"{source}: blessing after_play_zone must be blessing_zone")
        if slot_type != "blessing":
            raise ValueError(f"{source}: blessing slot_type must be blessing")

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
