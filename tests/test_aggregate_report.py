from pathlib import Path

from sim.render_aggregate_report import build_aggregate_summary, render_aggregate_markdown


def test_aggregate_report_builds_from_existing_logs() -> None:
    summary = build_aggregate_summary(Path("logs"))

    assert summary["inventory"]
    assert summary["draft_reports"]["reports"]

    markdown = render_aggregate_markdown(summary)
    assert "# Aggregate Report" in markdown
    assert "Draft Reports" in markdown
