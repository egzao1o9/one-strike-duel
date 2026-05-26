from engine.log_formatter import render_match_log_markdown, render_match_log_text


def test_render_match_log_text_contains_human_readable_sections() -> None:
    payload = {
        "match_id": "match_000001",
        "players": {
            "p1": {"bot": "RandomBot", "deck": "starter_attack"},
            "p2": {"bot": "DefenseBot", "deck": "starter_defense"},
        },
        "turns": [
            {
                "turn": 1,
                "phase1_mulligan": {
                    "p1_discarded": ["押し込み"],
                    "p2_discarded": [],
                },
                "control": {
                    "p1": None,
                    "p2": "構え",
                    "reveals": {"p1": [], "p2": []},
                },
                "phase3_mulligan": {
                    "p1_discarded": [],
                    "p2_discarded": ["崩し"],
                },
                "battle": {
                    "p1_cards": ["渾身", "フェイント"],
                    "p2_cards": ["押し込み"],
                    "p1_final": {"attack": 4, "block": 0, "speed": 0},
                    "p2_final": {"attack": 2, "block": 2, "speed": 2},
                    "result": "win",
                },
            }
        ],
        "winner": "p2",
        "end_reason": "p2_attack_success",
        "turn_count": 1,
    }

    rendered = render_match_log_text(payload)

    assert "Match: match_000001" in rendered
    assert "Winner: P2" in rendered
    assert "Turn 1" in rendered
    assert "- Mulligan1: P1 押し込み / P2 なし" in rendered
    assert "- Control: P1 pass / P2 構え" in rendered
    assert "- Battle: P1 渾身, フェイント [A=4 B=0 S=0] vs P2 押し込み [A=2 B=2 S=2]" in rendered
    assert "- Initiative: P2 先制" in rendered


def test_render_match_log_markdown_contains_sections_and_table() -> None:
    payload = {
        "match_id": "match_000001",
        "players": {
            "p1": {"bot": "RandomBot", "deck": "starter_attack"},
            "p2": {"bot": "DefenseBot", "deck": "starter_defense"},
        },
        "turns": [
            {
                "turn": 1,
                "phase1_mulligan": {
                    "p1_discarded": ["押し込み"],
                    "p2_discarded": [],
                },
                "control": {
                    "p1": None,
                    "p2": "構え",
                    "reveals": {"p1": [], "p2": []},
                },
                "phase3_mulligan": {
                    "p1_discarded": [],
                    "p2_discarded": ["崩し"],
                },
                "battle": {
                    "p1_cards": ["渾身", "フェイント"],
                    "p2_cards": ["押し込み"],
                    "p1_final": {"attack": 4, "block": 0, "speed": 0},
                    "p2_final": {"attack": 2, "block": 2, "speed": 2},
                    "result": "win",
                },
            }
        ],
        "winner": "p2",
        "end_reason": "p2_attack_success",
        "turn_count": 1,
    }

    rendered = render_match_log_markdown(payload)

    assert "# Match Report: match_000001" in rendered
    assert "## Summary" in rendered
    assert "| Side | Bot | Deck |" in rendered
    assert "### Turn 1" in rendered
    assert "| Mulligan1 | 押し込み | なし |" in rendered
    assert "| Battle Cards | 渾身, フェイント | 押し込み |" in rendered
    assert "- Initiative: P2 先制" in rendered
