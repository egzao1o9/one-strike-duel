from pathlib import Path
import json
import tempfile

from sim.run_draft_bot_suite import run_suite, should_save_battle_logs_for_matchup


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
        assert len(payload["matchups"]) == 15
        assert set(payload["bots"]) == {"Standard", "Aggro", "Guard", "Control", "Blessing"}
        assert "overall_priority" in payload
        first_bot = next(iter(payload["bots"].values()))
        assert "prediction_hit_rate" in first_bot


def test_draft_bot_suite_fast_mode_marks_summary() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        output = run_suite(
            matches_per_matchup=4,
            seed=602,
            output_dir_override=tmpdir,
            keep_match_logs=1,
            fast_report=True,
            workers=1,
        )
        payload = json.loads(Path(output["summary_path"]).read_text(encoding="utf-8"))
        assert payload["config"]["fast_report"] is True
        assert payload["config"]["workers"] == 1


def test_draft_bot_suite_lean_logging_omits_priority() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        output = run_suite(
            matches_per_matchup=4,
            seed=603,
            output_dir_override=tmpdir,
            keep_match_logs=1,
            fast_report=True,
            lean_draft_logging=True,
        )
        payload = json.loads(Path(output["summary_path"]).read_text(encoding="utf-8"))
        assert payload["config"]["lean_draft_logging"] is True
        assert payload["overall_priority"] is None
        first_bot = next(iter(payload["bots"].values()))
        assert first_bot["priority"] is None


def test_draft_bot_suite_parallel_workers_summary() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        output = run_suite(
            matches_per_matchup=4,
            seed=604,
            output_dir_override=tmpdir,
            keep_match_logs=0,
            fast_report=True,
            lean_draft_logging=True,
            workers=2,
        )
        payload = json.loads(Path(output["summary_path"]).read_text(encoding="utf-8"))
        assert payload["config"]["workers"] == 2


def test_should_save_battle_logs_for_matchup_respects_filter() -> None:
    assert should_save_battle_logs_for_matchup(global_save=False, filter_labels=None, matchup_labels=("Aggro", "Guard")) is False
    assert should_save_battle_logs_for_matchup(global_save=True, filter_labels=None, matchup_labels=("Aggro", "Guard")) is True
    assert should_save_battle_logs_for_matchup(global_save=False, filter_labels=["Aggro"], matchup_labels=("Aggro", "Guard")) is True
    assert should_save_battle_logs_for_matchup(global_save=False, filter_labels=["Control"], matchup_labels=("Aggro", "Guard")) is False
