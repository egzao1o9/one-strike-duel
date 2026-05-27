from pathlib import Path
import json
import tempfile

from sim.run_draft_bot_suite import run_suite


def test_draft_bot_suite_generates_matchups_and_summary() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        output = run_suite(
            matches_per_matchup=4,
            seed=601,
            output_dir_override=tmpdir,
            keep_match_logs=1,
        )
        assert output["index_path"].exists()
        assert output["summary_path"].exists()
        payload = json.loads(Path(output["summary_path"]).read_text(encoding="utf-8"))
        assert len(payload["matchups"]) == 6
        assert set(payload["bots"]) == {"Standard", "Aggro", "Guard"}
        assert "overall_priority" in payload
