import csv
from pathlib import Path
import tempfile

from sim.card_csv import export_cards_csv, import_cards_csv


def test_export_cards_csv_writes_expected_headers() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        output = export_cards_csv("data/cards_src", Path(tmpdir) / "cards.csv")
        with output.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            row = next(reader)

    assert "effects_json" in reader.fieldnames
    assert row["id"]
    assert row["type"] in {"battle", "control"}


def test_import_cards_csv_recreates_sources_and_bundle() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        csv_path = export_cards_csv("data/cards_src", Path(tmpdir) / "cards.csv")
        source_dir = Path(tmpdir) / "cards_src"
        bundle_path = Path(tmpdir) / "cards.json"
        count, built = import_cards_csv(csv_path, source_dir, bundle_path)
        assert (source_dir / "battle" / "battle_all_in.json").exists()

    assert count >= 28
    assert built == bundle_path
