from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from sim.card_source import build_cards_payload, write_cards_payload

CSV_FIELDS = (
    "id",
    "name",
    "type",
    "rarity",
    "attack",
    "block",
    "speed",
    "tags",
    "effects_json",
    "notes",
)


def encode_tags(tags: list[str]) -> str:
    return "|".join(tags)


def decode_tags(value: str) -> list[str]:
    if not value.strip():
        return []
    normalized = value.replace("|", ",")
    return [item.strip() for item in normalized.split(",") if item.strip()]


def encode_effects(effects: list[dict[str, Any]]) -> str:
    return json.dumps(effects, ensure_ascii=False)


def decode_effects(value: str) -> list[dict[str, Any]]:
    if not value.strip():
        return []
    payload = json.loads(value)
    if not isinstance(payload, list):
        raise ValueError("effects_json must decode to a list")
    return payload


def export_cards_csv(source_dir: str | Path, output_path: str | Path) -> Path:
    cards = build_cards_payload(source_dir)
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for card in cards:
            writer.writerow(
                {
                    "id": card["id"],
                    "name": card["name"],
                    "type": card["type"],
                    "rarity": card.get("rarity", "common"),
                    "attack": card.get("attack", 0),
                    "block": card.get("block", 0),
                    "speed": card.get("speed", 0),
                    "tags": encode_tags(card.get("tags", [])),
                    "effects_json": encode_effects(card.get("effects", [])),
                    "notes": card.get("notes", ""),
                }
            )
    return target


def import_cards_csv(csv_path: str | Path, source_dir: str | Path, bundle_output: str | Path | None = None) -> tuple[int, Path | None]:
    csv_file = Path(csv_path)
    root = Path(source_dir)
    root.mkdir(parents=True, exist_ok=True)
    cards: list[dict[str, Any]] = []
    with csv_file.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        if fieldnames and fieldnames[0].startswith("\ufeff"):
            fieldnames[0] = fieldnames[0].lstrip("\ufeff")
            reader.fieldnames = fieldnames
        missing_fields = [field for field in CSV_FIELDS if field not in fieldnames]
        if missing_fields:
            raise ValueError(f"missing CSV columns: {missing_fields}")
        for row in reader:
            if not row["id"].strip():
                continue
            card = {
                "id": row["id"].strip(),
                "name": row["name"],
                "type": row["type"].strip(),
                "rarity": row["rarity"].strip() or "common",
                "attack": int(row["attack"]),
                "block": int(row["block"]),
                "speed": int(row["speed"]),
                "tags": decode_tags(row.get("tags", "")),
                "effects": decode_effects(row.get("effects_json", "")),
                "notes": row.get("notes", ""),
            }
            cards.append(card)

    for existing in root.rglob("*.json"):
        existing.unlink()

    for card in cards:
        folder = root / card["type"]
        folder.mkdir(parents=True, exist_ok=True)
        target = folder / f"{card['id']}.json"
        target.write_text(json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    bundle_path = None
    if bundle_output:
        bundle_path = write_cards_payload(sorted(cards, key=lambda item: (item["type"], item["id"])), bundle_output)
    return len(cards), bundle_path
