import json
from pathlib import Path
import tempfile

from sim.card_source import build_cards_payload, write_cards_payload


def test_card_sources_build_generated_bundle() -> None:
    payload = build_cards_payload("data/cards_src")

    assert len(payload) >= 35
    assert payload[0]["card_type"] == "battle"
    assert any(card["id"] == "control_focus" for card in payload)


def test_written_bundle_can_be_loaded_as_json() -> None:
    payload = build_cards_payload("data/cards_src")

    with tempfile.TemporaryDirectory() as tmpdir:
        output = write_cards_payload(payload, Path(tmpdir) / "cards.json")
        loaded = json.loads(output.read_text(encoding="utf-8"))

    assert len(loaded) == len(payload)
    assert loaded[0]["id"] == payload[0]["id"]


def test_disabled_cards_are_excluded_from_runtime_bundle_by_default() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        source_dir = Path(tmpdir) / "cards_src" / "battle"
        source_dir.mkdir(parents=True, exist_ok=True)
        (source_dir / "enabled_card.json").write_text(
            json.dumps(
                {
                    "id": "enabled_card",
                    "name": "Enabled Card",
                    "card_type": "battle",
                    "rarity": "common",
                    "attack": 1,
                    "block": 0,
                    "speed": 0,
                    "enabled": True,
                    "effects": [],
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        (source_dir / "disabled_card.json").write_text(
            json.dumps(
                {
                    "id": "disabled_card",
                    "name": "Disabled Card",
                    "card_type": "battle",
                    "rarity": "common",
                    "attack": 2,
                    "block": 0,
                    "speed": 0,
                    "enabled": False,
                    "effects": [],
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

        runtime_payload = build_cards_payload(Path(tmpdir) / "cards_src")
        full_payload = build_cards_payload(Path(tmpdir) / "cards_src", include_disabled=True)

    assert [card["id"] for card in runtime_payload] == ["enabled_card"]
    assert {card["id"] for card in full_payload} == {"enabled_card", "disabled_card"}
