from pathlib import Path
import json
import tempfile

from sim.run_random_bot_mix import run_random_bot_mix


def test_random_bot_mix_generates_reports() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        summary_md, total_matches = run_random_bot_mix(6, 123, tmpdir, keep_match_logs=3)
        assert total_matches == 6
        assert summary_md.exists()
        summary_json = Path(tmpdir) / "summary.json"
        assert summary_json.exists()
        payload = json.loads(summary_json.read_text(encoding="utf-8"))
        first_bot = next(iter(payload["bots"].values()))
        assert "same_card_win_rate" in first_bot
        assert "more_card_win_rate" in first_bot
        assert "winning_facedown" in first_bot
        assert "losing_facedown" in first_bot
        assert "starting_player_win_rate" in first_bot
        assert "responding_player_win_rate" in first_bot
        matches_dir = Path(tmpdir) / "matches"
        assert matches_dir.exists()
        remaining = list(matches_dir.iterdir())
        assert any(path.suffix == ".md" for path in remaining)
        assert len({path.name.split("_", 2)[1] for path in remaining}) <= 3
