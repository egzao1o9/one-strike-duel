from engine.log_formatter import render_match_log_markdown, render_match_log_text


def make_payload():
    return {
        "match_id": "match_000001",
        "players": {
            "p1": {
                "bot": "RandomBot",
                "deck": "starter_attack",
                "reshuffle_count": 1,
                "draw_shortfall_turns": [2],
            },
            "p2": {
                "bot": "DefenseBot",
                "deck": "starter_defense",
                "reshuffle_count": 0,
                "draw_shortfall_turns": [],
            },
        },
        "turns": [
            {
                "turn": 1,
                "turn_start": {
                    "starting_player": "p1",
                    "p1": {
                        "overflow_discarded": [],
                        "drawn": ["押し込み", "崩し"],
                        "draw_count": 2,
                        "reshuffled": False,
                        "draw_shortfall": 0,
                        "hand_count": 6,
                    },
                    "p2": {
                        "overflow_discarded": ["受け流し"],
                        "drawn": [],
                        "draw_count": 0,
                        "reshuffled": True,
                        "draw_shortfall": 1,
                        "hand_count": 6,
                    },
                },
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
                    "starting_player": "p1",
                    "first_pass_player": "p2",
                    "actions": [
                        {
                            "player_id": "p1",
                            "action_type": "set",
                            "action_name": "伏せる",
                            "set_count": 1,
                            "counts_after": {"p1": 1, "p2": 0},
                        },
                        {
                            "player_id": "p2",
                            "action_type": "set_pass",
                            "action_name": "伏せてパス",
                            "set_count": 1,
                            "counts_after": {"p1": 1, "p2": 1},
                        },
                    ],
                    "p1_cards": ["渾身"],
                    "p2_cards": ["受け流し"],
                    "p1_facedown_count": 1,
                    "p2_facedown_count": 1,
                    "winner_facedown_count": 1,
                    "loser_facedown_count": 1,
                    "won_with_fewer_cards": False,
                    "won_with_same_cards": True,
                    "won_with_more_cards": False,
                    "p1_final": {"attack": 4, "block": 0, "speed": -1},
                    "p2_final": {"attack": 0, "block": 3, "speed": 1},
                    "result": "win",
                },
            }
        ],
        "winner": "p1",
        "end_reason": "p1_attack_success",
        "turn_count": 1,
    }


def test_render_match_log_text_contains_human_readable_sections() -> None:
    rendered = render_match_log_text(make_payload())

    assert "Match: match_000001" in rendered
    assert "Winner: P1" in rendered
    assert "Turn 1" in rendered
    assert "- Start: first=P1 / P1 draw=2 / P2 draw=0" in rendered
    assert "- Overflow P2: 受け流し" in rendered
    assert "- Reshuffle: P2" in rendered
    assert "- Draw Shortfall P2: 1" in rendered
    assert "- Control: P1 pass / P2 構え" in rendered
    assert "- Battle: P1 渾身 [A=4 B=0 S=-1] vs P2 受け流し [A=0 B=3 S=1]" in rendered
    assert "- Action: P1 伏せる set=1 after={'p1': 1, 'p2': 0}" in rendered


def test_render_match_log_markdown_contains_sections_and_action_table() -> None:
    rendered = render_match_log_markdown(make_payload())

    assert "# Match Report: match_000001" in rendered
    assert "## Summary" in rendered
    assert "| Side | Bot | Deck | Reshuffles | Draw Shortfall Turns |" in rendered
    assert "### Turn 1" in rendered
    assert "| Start Draw | draw=2 / hand=6 | draw=0 / hand=6 / overflow=受け流し / reshuffle / short=1 |" in rendered
    assert "| Battle Cards | 渾身 | 受け流し |" in rendered
    assert "- Starting Player: P1" in rendered
    assert "| Action Order | Type | Set Count | Counts After |" in rendered
    assert "| P2 | 伏せてパス | 1 | P1=1 / P2=1 |" in rendered
