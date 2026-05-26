from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from engine.card import validate_card_payload, validate_cards_payload


def iter_card_source_paths(source_dir: str | Path) -> list[Path]:
    root = Path(source_dir)
    return sorted(path for path in root.rglob("*.json") if path.is_file())


def load_card_source_file(path: str | Path) -> dict[str, Any]:
    file_path = Path(path)
    payload = json.loads(file_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{file_path}: card source must be a single object")
    validate_card_payload(payload, source=str(file_path))
    return payload


def load_card_sources(source_dir: str | Path) -> list[dict[str, Any]]:
    paths = iter_card_source_paths(source_dir)
    cards = [load_card_source_file(path) for path in paths]
    validate_cards_payload(cards, source=str(Path(source_dir)))
    return cards


def build_cards_payload(source_dir: str | Path) -> list[dict[str, Any]]:
    cards = load_card_sources(source_dir)
    return sorted(cards, key=lambda item: (item["type"], item["id"]))


def write_cards_payload(payload: list[dict[str, Any]], output_path: str | Path) -> Path:
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return target
