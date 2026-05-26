import json
from pathlib import Path
import tempfile

from sim.card_source import build_cards_payload, write_cards_payload


def test_card_sources_build_generated_bundle() -> None:
    payload = build_cards_payload("data/cards_src")

    assert len(payload) == 28
    assert payload[0]["type"] == "battle"
    assert any(card["id"] == "control_focus" for card in payload)


def test_written_bundle_can_be_loaded_as_json() -> None:
    payload = build_cards_payload("data/cards_src")

    with tempfile.TemporaryDirectory() as tmpdir:
        output = write_cards_payload(payload, Path(tmpdir) / "cards.json")
        loaded = json.loads(output.read_text(encoding="utf-8"))

    assert len(loaded) == len(payload)
    assert loaded[0]["id"] == payload[0]["id"]
