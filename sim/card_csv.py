from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

from sim.card_source import (
    build_cards_payload,
    merge_cards_and_effects,
    split_cards_and_effects,
    write_card_sources,
    write_cards_payload,
)

CARDS_CSV_FIELDS = (
    "id",
    "name",
    "rarity",
    "card_type",
    "attack",
    "block",
    "speed",
    "tags",
    "public_text",
    "enabled",
    "play_zone",
    "after_play_zone",
    "slot_type",
    "flavor_text",
    "notes",
)

CARD_EFFECTS_CSV_FIELDS = (
    "id",
    "card_id",
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
    "params_json",
    "timing",
    "kind",
    "notes",
)


def encode_tags(tags: list[str]) -> str:
    return ",".join(tags)


def decode_tags(value: str) -> list[str]:
    if not value.strip():
        return []
    normalized = value.replace("|", ",")
    return [item.strip() for item in normalized.split(",") if item.strip()]


def _to_bool(value: str | bool | None, default: bool = True) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    normalized = str(value).strip().lower()
    if normalized in {"", "none"}:
        return default
    if normalized in {"1", "true", "yes", "on"}:
        return True
    if normalized in {"0", "false", "no", "off"}:
        return False
    return default


def _to_int(value: str | int | None) -> int:
    if isinstance(value, int):
        return value
    if value is None:
        return 0
    raw = str(value).strip()
    if not raw:
        return 0
    return int(raw)


def export_cards_csv(source_dir: str | Path, output_path: str | Path) -> Path:
    cards = build_cards_payload(source_dir, include_disabled=True)
    card_rows, _ = split_cards_and_effects(cards)
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CARDS_CSV_FIELDS)
        writer.writeheader()
        for row in card_rows:
            writer.writerow(
                {
                    "id": row["id"],
                    "name": row["name"],
                    "rarity": row["rarity"],
                    "card_type": row["card_type"],
                    "attack": row["attack"],
                    "block": row["block"],
                    "speed": row["speed"],
                    "tags": encode_tags(row.get("tags", [])),
                    "public_text": row.get("public_text", ""),
                    "enabled": row.get("enabled", True),
                    "play_zone": row.get("play_zone", ""),
                    "after_play_zone": row.get("after_play_zone", ""),
                    "slot_type": row.get("slot_type", ""),
                    "flavor_text": row.get("flavor_text", ""),
                    "notes": row.get("notes", ""),
                }
            )
    return target


def export_card_effects_csv(source_dir: str | Path, output_path: str | Path) -> Path:
    cards = build_cards_payload(source_dir, include_disabled=True)
    _, effect_rows = split_cards_and_effects(cards)
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CARD_EFFECTS_CSV_FIELDS)
        writer.writeheader()
        for row in effect_rows:
            writer.writerow(
                {
                    "id": row.get("id", ""),
                    "card_id": row["card_id"],
                    "seq": row.get("seq", 1),
                    "enabled": row.get("enabled", True),
                    "trigger": row.get("trigger", ""),
                    "priority": row.get("priority", 100),
                    "effect_type": row.get("effect_type", ""),
                    "target": row.get("target", ""),
                    "stat": row.get("stat", ""),
                    "value": row.get("value", 0),
                    "value2": row.get("value2", 0),
                    "count": row.get("count", 0),
                    "duration": row.get("duration", ""),
                    "active_zone": row.get("active_zone", ""),
                    "condition": row.get("condition", ""),
                    "keyword": row.get("keyword", ""),
                    "display_text": row.get("display_text", ""),
                    "params_json": row.get("params_json", ""),
                    "timing": row.get("timing", ""),
                    "kind": row.get("kind", ""),
                    "notes": row.get("notes", ""),
                }
            )
    return target


def export_cards_csv_pair(
    source_dir: str | Path,
    cards_output_path: str | Path,
    effects_output_path: str | Path,
) -> tuple[Path, Path]:
    return (
        export_cards_csv(source_dir, cards_output_path),
        export_card_effects_csv(source_dir, effects_output_path),
    )


def import_cards_csv(
    cards_csv_path: str | Path,
    source_dir: str | Path,
    bundle_output: str | Path | None = None,
    effects_csv_path: str | Path | None = None,
) -> tuple[int, Path | None]:
    cards_file = Path(cards_csv_path)
    card_rows: list[dict[str, Any]] = []
    with cards_file.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        if fieldnames and fieldnames[0].startswith("\ufeff"):
            fieldnames[0] = fieldnames[0].lstrip("\ufeff")
            reader.fieldnames = fieldnames
        missing_fields = [field for field in ("id", "name", "rarity", "card_type", "attack", "block", "speed") if field not in fieldnames]
        if missing_fields:
            raise ValueError(f"missing Cards CSV columns: {missing_fields}")
        for row in reader:
            card_id = str(row.get("id", "")).strip()
            if not card_id:
                continue
            card_rows.append(
                {
                    "id": card_id,
                    "name": row.get("name", ""),
                    "rarity": (row.get("rarity", "") or "common").strip() or "common",
                    "card_type": (row.get("card_type", "") or row.get("type", "")).strip(),
                    "attack": _to_int(row.get("attack")),
                    "block": _to_int(row.get("block")),
                    "speed": _to_int(row.get("speed")),
                    "tags": decode_tags(row.get("tags", "") or ""),
                    "public_text": row.get("public_text", "") or row.get("text", ""),
                    "enabled": _to_bool(row.get("enabled"), True),
                    "play_zone": (row.get("play_zone", "") or "").strip(),
                    "after_play_zone": (row.get("after_play_zone", "") or "").strip(),
                    "slot_type": (row.get("slot_type", "") or "").strip(),
                    "flavor_text": row.get("flavor_text", "") or "",
                    "notes": row.get("notes", "") or "",
                }
            )

    effect_rows: list[dict[str, Any]] = []
    if effects_csv_path:
        effects_file = Path(effects_csv_path)
        with effects_file.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            fieldnames = list(reader.fieldnames or [])
            if fieldnames and fieldnames[0].startswith("\ufeff"):
                fieldnames[0] = fieldnames[0].lstrip("\ufeff")
                reader.fieldnames = fieldnames
            missing_fields = [field for field in ("card_id", "seq", "trigger") if field not in fieldnames]
            if missing_fields:
                raise ValueError(f"missing CardEffects CSV columns: {missing_fields}")
            for row in reader:
                card_id = str(row.get("card_id", "")).strip()
                if not card_id:
                    continue
                effect_rows.append(
                    {
                        "id": str(row.get("id", "")).strip(),
                        "card_id": card_id,
                        "seq": _to_int(row.get("seq") or 1),
                        "enabled": _to_bool(row.get("enabled"), True),
                        "trigger": (row.get("trigger", "") or row.get("timing", "")).strip(),
                        "priority": _to_int(row.get("priority") or 100),
                        "effect_type": (row.get("effect_type", "") or "").strip(),
                        "target": (row.get("target", "") or "").strip(),
                        "stat": (row.get("stat", "") or "").strip(),
                        "value": _to_int(row.get("value")),
                        "value2": _to_int(row.get("value2")),
                        "count": _to_int(row.get("count")),
                        "duration": (row.get("duration", "") or "").strip(),
                        "active_zone": (row.get("active_zone", "") or "").strip(),
                        "condition": (row.get("condition", "") or "").strip(),
                        "keyword": (row.get("keyword", "") or "").strip(),
                        "display_text": row.get("display_text", "") or row.get("text", "") or "",
                        "params_json": row.get("params_json", "") or "",
                        "timing": (row.get("timing", "") or "").strip(),
                        "kind": (row.get("kind", "") or "").strip(),
                        "notes": row.get("notes", "") or "",
                    }
                )

    cards = merge_cards_and_effects(card_rows, effect_rows)
    write_card_sources(cards, source_dir)
    bundle_path = None
    if bundle_output:
        bundle_path = write_cards_payload(cards, bundle_output)
    return len(cards), bundle_path
