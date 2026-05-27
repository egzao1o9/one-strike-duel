import csv
import json
from pathlib import Path
import tempfile

from sim.card_csv import export_card_effects_csv, export_cards_csv, import_cards_csv


def test_export_cards_csv_writes_expected_headers() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        output = export_cards_csv("data/cards_src", Path(tmpdir) / "cards.csv")
        with output.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            row = next(reader)

    assert "card_type" in reader.fieldnames
    assert "public_text" in reader.fieldnames
    assert "play_zone" in reader.fieldnames
    assert row["id"]
    assert row["card_type"] in {"battle", "control", "blessing"}


def test_export_card_effects_csv_writes_expected_headers() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        output = export_card_effects_csv("data/cards_src", Path(tmpdir) / "card_effects.csv")
        with output.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            row = next(reader)

    assert "card_id" in reader.fieldnames
    assert "trigger" in reader.fieldnames
    assert "effect_type" in reader.fieldnames
    assert row["card_id"]


def test_import_cards_csv_recreates_sources_and_bundle() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        cards_csv_path = export_cards_csv("data/cards_src", Path(tmpdir) / "cards.csv")
        effects_csv_path = export_card_effects_csv("data/cards_src", Path(tmpdir) / "card_effects.csv")
        source_dir = Path(tmpdir) / "cards_src"
        bundle_path = Path(tmpdir) / "cards.json"
        count, built = import_cards_csv(cards_csv_path, source_dir, bundle_path, effects_csv_path)
        assert (source_dir / "battle" / "battle_all_in.json").exists()
        assert (source_dir / "blessing" / "blessing_guard.json").exists()

    assert count >= 35
    assert built == bundle_path


def test_import_cards_csv_accepts_split_effect_rows() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        cards_csv_path = Path(tmpdir) / "cards.csv"
        effects_csv_path = Path(tmpdir) / "card_effects.csv"
        with cards_csv_path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=[
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
                ],
            )
            writer.writeheader()
            writer.writerow(
                {
                    "id": "blessing_test_flat",
                    "name": "Test Blessing",
                    "rarity": "rare",
                    "card_type": "blessing",
                    "attack": "0",
                    "block": "0",
                    "speed": "0",
                    "tags": "blessing,draw",
                    "public_text": "場にある限り、通常ドロー+1。",
                    "enabled": "true",
                    "play_zone": "blessing_zone",
                    "after_play_zone": "blessing_zone",
                    "slot_type": "blessing",
                    "flavor_text": "",
                    "notes": "split import",
                }
            )
        with effects_csv_path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=[
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
                ],
            )
            writer.writeheader()
            writer.writerow(
                {
                    "id": "blessing_test_flat_01",
                    "card_id": "blessing_test_flat",
                    "seq": "1",
                    "enabled": "true",
                    "trigger": "passive",
                    "priority": "100",
                    "effect_type": "modify_rule_value",
                    "target": "self_player",
                    "stat": "draw_per_turn",
                    "value": "1",
                    "value2": "0",
                    "count": "0",
                    "duration": "while_in_zone",
                    "active_zone": "blessing_zone",
                    "condition": "",
                    "keyword": "",
                    "display_text": "場にある限り、通常ドロー+1。",
                    "params_json": "",
                    "timing": "",
                    "kind": "",
                    "notes": "",
                }
            )
        source_dir = Path(tmpdir) / "cards_src"
        bundle_path = Path(tmpdir) / "cards.json"
        count, built = import_cards_csv(cards_csv_path, source_dir, bundle_path, effects_csv_path)
        payload = bundle_path.read_text(encoding="utf-8")

    assert count == 1
    assert built == bundle_path
    assert "modify_rule_value" in payload
    assert "draw_per_turn" in payload


def test_export_cards_csv_includes_disabled_cards_for_editing() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        source_dir = Path(tmpdir) / "cards_src" / "battle"
        source_dir.mkdir(parents=True, exist_ok=True)
        (source_dir / "disabled_card.json").write_text(
            json.dumps(
                {
                    "id": "disabled_card",
                    "name": "Disabled Card",
                    "card_type": "battle",
                    "rarity": "common",
                    "attack": 1,
                    "block": 0,
                    "speed": 0,
                    "enabled": False,
                    "effects": [],
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        output = export_cards_csv(Path(tmpdir) / "cards_src", Path(tmpdir) / "cards.csv")
        with output.open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))

    assert len(rows) == 1
    assert rows[0]["id"] == "disabled_card"
    assert rows[0]["enabled"].lower() == "false"
