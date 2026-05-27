from pathlib import Path
import json
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
        payload = json.loads(summary_json.read_text(encoding="utf-8"))
        first_drafter = next(iter(payload["drafters"].values()))
        assert "same_card_win_rate" in first_drafter
        assert "more_card_win_rate" in first_drafter
        assert "winning_facedown" in first_drafter
        assert "losing_facedown" in first_drafter
        assert "starting_player_win_rate" in first_drafter
        assert "responding_player_win_rate" in first_drafter
        assert "final_attack" in first_drafter
        assert "losing_attack" in first_drafter
        assert "speed_advantage_losses" in first_drafter
        assert "block_then_win_matches" in first_drafter
        assert "picked_card_stats" in first_drafter
        assert "rarity_play_stats" in first_drafter
        matches_dir = Path(tmpdir) / "matches"
        assert matches_dir.exists()
        remaining = list(matches_dir.iterdir())
        assert any(path.suffix == ".md" for path in remaining)
        assert len({path.name.split("_", 2)[1] for path in remaining}) <= 2


def test_draft_report_fast_mode_skips_match_files() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        summary_md, total_matches = run_draft_report(
            "RoleBalanceDraftBot",
            "RandomDraftBot",
            "GreedyBot",
            "GreedyBot",
            rounds=2,
            seed=152,
            output_dir_override=tmpdir,
            keep_match_logs=2,
            fast_report=True,
        )
        assert total_matches == 4
        assert summary_md.exists()
        payload = json.loads((Path(tmpdir) / "summary.json").read_text(encoding="utf-8"))
        assert payload["config"]["fast_report"] is True
        assert payload["config"]["lean_draft_logging"] is False
        assert not (Path(tmpdir) / "matches").exists()
        match_records = (Path(tmpdir) / "match_records.jsonl").read_text(encoding="utf-8").splitlines()
        assert len(match_records) == 4


def test_draft_report_lean_logging_omits_pick_history() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        summary_md, total_matches = run_draft_report(
            "RoleBalanceDraftBot",
            "RandomDraftBot",
            "GreedyBot",
            "GreedyBot",
            rounds=2,
            seed=153,
            output_dir_override=tmpdir,
            keep_match_logs=2,
            fast_report=True,
            lean_draft_logging=True,
        )
        assert total_matches == 4
        assert summary_md.exists()
        payload = json.loads((Path(tmpdir) / "summary.json").read_text(encoding="utf-8"))
        assert payload["config"]["lean_draft_logging"] is True
        assert "draft_records" not in payload
        first_record = json.loads((Path(tmpdir) / "match_records.jsonl").read_text(encoding="utf-8").splitlines()[0])
        assert "picks" not in first_record
