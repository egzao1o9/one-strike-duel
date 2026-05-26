from pathlib import Path
import tempfile

from sim.run_draft_report import run_draft_report


def test_draft_report_generates_outputs() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        summary_md, total_matches = run_draft_report(
            "RoleBalanceDraftBot",
            "RandomDraftBot",
            "GreedyBot",
            "GreedyBot",
            rounds=2,
            seed=151,
            output_dir_override=tmpdir,
            keep_match_logs=2,
        )
        assert total_matches == 4
        assert summary_md.exists()
        summary_json = Path(tmpdir) / "summary.json"
        assert summary_json.exists()
        matches_dir = Path(tmpdir) / "matches"
        assert matches_dir.exists()
        remaining = list(matches_dir.iterdir())
        assert any(path.suffix == ".md" for path in remaining)
        assert len({path.name.split("_", 2)[1] for path in remaining}) <= 2
