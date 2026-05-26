from pathlib import Path
import tempfile

from sim.run_random_bot_mix import run_random_bot_mix


def test_random_bot_mix_generates_reports() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        summary_md, total_matches = run_random_bot_mix(6, 123, tmpdir, keep_match_logs=3)
        assert total_matches == 6
        assert summary_md.exists()
        summary_json = Path(tmpdir) / "summary.json"
        assert summary_json.exists()
        matches_dir = Path(tmpdir) / "matches"
        assert matches_dir.exists()
        remaining = list(matches_dir.iterdir())
        assert any(path.suffix == ".md" for path in remaining)
        assert len({path.name.split("_", 2)[1] for path in remaining}) <= 3
