from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from engine.card import (
    default_after_play_zone,
    default_play_zone,
    default_slot_type,
    validate_card_payload,
    validate_cards_payload,
    validate_effect_payload,
)


def iter_card_source_paths(source_dir: str | Path) -> list[Path]:
    root = Path(source_dir)
    return sorted(path for path in root.rglob("*.json") if path.is_file())


def load_card_source_file(path: str | Path) -> dict[str, Any]:
    file_path = Path(path)
    payload = json.loads(file_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{file_path}: card source must be a single object")
    validate_card_payload(payload, source=str(file_path))
    return normalize_card_payload(payload)


def load_card_sources(source_dir: str | Path, *, include_disabled: bool = False) -> list[dict[str, Any]]:
    paths = iter_card_source_paths(source_dir)
    cards = [load_card_source_file(path) for path in paths]
    if not include_disabled:
        cards = [card for card in cards if bool(card.get("enabled", True))]
    validate_cards_payload(cards, source=str(Path(source_dir)))
    return cards


def normalize_card_payload(payload: dict[str, Any]) -> dict[str, Any]:
    card_type = str(payload.get("card_type") or payload.get("type") or "").strip()
    attack = int(payload.get("attack", payload.get("base", {}).get("attack", 0)))
    block = int(payload.get("block", payload.get("base", {}).get("block", 0)))
    speed = int(payload.get("speed", payload.get("base", {}).get("speed", 0)))
    play_zone = str(payload.get("play_zone") or payload.get("zones", {}).get("play_zone") or default_play_zone(card_type))
    after_play_zone = str(payload.get("after_play_zone") or payload.get("zones", {}).get("after_play_zone") or default_after_play_zone(card_type))
    slot_type = str(payload.get("slot_type") or payload.get("zones", {}).get("slot_type") or default_slot_type(card_type))
    return {
        "id": payload["id"],
        "name": payload["name"],
        "card_type": card_type,
        "rarity": payload.get("rarity", "common"),
        "attack": attack,
        "block": block,
        "speed": speed,
        "tags": list(payload.get("tags", [])),
        "public_text": str(payload.get("public_text") or payload.get("text") or ""),
        "enabled": bool(payload.get("enabled", True)),
        "play_zone": play_zone,
        "after_play_zone": after_play_zone,
        "slot_type": slot_type,
        "flavor_text": str(payload.get("flavor_text", "") or ""),
        "effects": sorted(
            [normalize_effect_payload(effect_payload, payload["id"], index + 1) for index, effect_payload in enumerate(payload.get("effects", []))],
            key=lambda item: (item.get("seq", 1), item.get("id", "")),
        ),
        "notes": str(payload.get("notes", "") or ""),
    }


def normalize_effect_payload(payload: dict[str, Any], card_id: str, seq: int) -> dict[str, Any]:
    validate_effect_payload(payload, source=f"{card_id} effect[{seq}]")
    normalized = dict(payload)
    normalized.setdefault("id", f"{card_id}_{seq:02d}")
    normalized.setdefault("seq", seq)
    normalized.setdefault("enabled", True)
    normalized.setdefault("priority", 100)
    normalized.setdefault("value", 0)
    normalized.setdefault("value2", 0)
    normalized.setdefault("count", 0)
    if "display_text" not in normalized and "text" in normalized:
        normalized["display_text"] = str(normalized.get("text", ""))
    return normalized


def build_cards_payload(source_dir: str | Path, *, include_disabled: bool = False) -> list[dict[str, Any]]:
    cards = load_card_sources(source_dir, include_disabled=include_disabled)
    return sorted(cards, key=lambda item: (item["card_type"], item["id"]))


def split_cards_and_effects(cards: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    card_rows: list[dict[str, Any]] = []
    effect_rows: list[dict[str, Any]] = []
    for card in cards:
        card_rows.append(
            {
                "id": card["id"],
                "name": card["name"],
                "rarity": card["rarity"],
                "card_type": card["card_type"],
                "attack": card["attack"],
                "block": card["block"],
                "speed": card["speed"],
                "tags": list(card.get("tags", [])),
                "public_text": card.get("public_text", ""),
                "enabled": bool(card.get("enabled", True)),
                "play_zone": card.get("play_zone", ""),
                "after_play_zone": card.get("after_play_zone", ""),
                "slot_type": card.get("slot_type", ""),
                "flavor_text": card.get("flavor_text", ""),
                "notes": card.get("notes", ""),
            }
        )
        for effect in card.get("effects", []):
            effect_rows.append({"card_id": card["id"], **effect})
    effect_rows.sort(key=lambda item: (item["card_id"], int(item.get("seq", 1)), item.get("id", "")))
    return card_rows, effect_rows


def merge_cards_and_effects(card_rows: list[dict[str, Any]], effect_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    card_map: dict[str, dict[str, Any]] = {}
    for row in card_rows:
        card_id = str(row["id"]).strip()
        payload = normalize_card_payload(
            {
                "id": card_id,
                "name": row["name"],
                "card_type": row.get("card_type") or row.get("type"),
                "rarity": row.get("rarity", "common"),
                "attack": int(row.get("attack", 0) or 0),
                "block": int(row.get("block", 0) or 0),
                "speed": int(row.get("speed", 0) or 0),
                "tags": list(row.get("tags", [])),
                "public_text": row.get("public_text", ""),
                "enabled": bool(row.get("enabled", True)),
                "play_zone": row.get("play_zone", ""),
                "after_play_zone": row.get("after_play_zone", ""),
                "slot_type": row.get("slot_type", ""),
                "flavor_text": row.get("flavor_text", ""),
                "notes": row.get("notes", ""),
                "effects": [],
            }
        )
        payload["effects"] = []
        card_map[card_id] = payload

    for row in effect_rows:
        card_id = str(row["card_id"]).strip()
        if card_id not in card_map:
            raise ValueError(f"unknown card_id in effects: {card_id}")
        effect_payload = normalize_effect_payload(
            {key: value for key, value in row.items() if key != "card_id"},
            card_id,
            int(row.get("seq", 1) or 1),
        )
        card_map[card_id]["effects"].append(effect_payload)

    cards = sorted(card_map.values(), key=lambda item: (item["card_type"], item["id"]))
    validate_cards_payload(cards, source="merged card/effect rows")
    return cards


def write_card_sources(cards: list[dict[str, Any]], source_dir: str | Path) -> list[Path]:
    root = Path(source_dir)
    root.mkdir(parents=True, exist_ok=True)
    for existing in root.rglob("*.json"):
        existing.unlink()
    written: list[Path] = []
    for card in cards:
        folder = root / card["card_type"]
        folder.mkdir(parents=True, exist_ok=True)
        target = folder / f"{card['id']}.json"
        target.write_text(json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        written.append(target)
    return written


def write_cards_payload(payload: list[dict[str, Any]], output_path: str | Path) -> Path:
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return target
