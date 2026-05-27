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
                        "drawn": ["A", "B"],
                        "draw_count": 2,
                        "reshuffled": False,
                        "draw_shortfall": 0,
                        "hand_count": 6,
                    },
                    "p2": {
                        "overflow_discarded": ["Guard"],
                        "drawn": [],
                        "draw_count": 0,
                        "reshuffled": True,
                        "draw_shortfall": 1,
                        "hand_count": 6,
                    },
                },
                "phase1_mulligan": {
                    "p1_discarded": ["A"],
                    "p2_discarded": [],
                    "hand_counts": {"p1": 5, "p2": 6},
                },
                "control": {
                    "p1": None,
                    "p2": "Guard Up",
                    "ids": {"p1": None, "p2": "control_guard"},
                    "sources": {"p1": None, "p2": "public"},
                    "hand_counts": {"p1": 5, "p2": 5},
                    "reveals": {"p1": [], "p2": []},
                },
                "phase3_mulligan": {
                    "p1_discarded": [],
                    "p2_discarded": ["B"],
                    "hand_counts": {"p1": 5, "p2": 5},
                },
                "battle": {
                    "starting_player": "p1",
                    "first_pass_player": "p2",
                    "actions": [
                        {
                            "player_id": "p1",
                            "action_type": "set",
                            "action_name": "Set",
                            "set_count": 1,
                            "set_card_ids": ["battle_all_in"],
                            "set_card_sources": ["hidden_rare"],
                            "set_pass_candidate_count": 1,
                            "counts_after": {"p1": 1, "p2": 0},
                        },
                        {
                            "player_id": "p2",
                            "action_type": "set_pass",
                            "action_name": "Set Pass",
                            "set_count": 1,
                            "set_card_ids": ["battle_guard"],
                            "set_card_sources": ["public"],
                            "set_pass_candidate_count": 1,
                            "counts_after": {"p1": 1, "p2": 1},
                        },
                    ],
                    "p1_cards": ["All In"],
                    "p1_card_ids": ["battle_all_in"],
                    "p1_card_sources": ["hidden_rare"],
                    "p2_cards": ["Guard"],
                    "p2_card_ids": ["battle_guard"],
                    "p2_card_sources": ["public"],
                    "p1_facedown_count": 1,
                    "p2_facedown_count": 1,
                    "p1_hand_count_end": 4,
                    "p2_hand_count_end": 4,
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
    assert "- Overflow P2: Guard" in rendered
    assert "- Reshuffle: P2" in rendered
    assert "- Draw Shortfall P2: 1" in rendered
    assert "- Control: P1 pass / P2 Guard Up" in rendered
    assert "- Control IDs: P1 pass [pass] / P2 control_guard [public]" in rendered
    assert "- Battle: P1 All In [A=4 B=0 S=-1] vs P2 Guard [A=0 B=3 S=1]" in rendered
    assert "- Battle IDs: P1 battle_all_in [hidden_rare] / P2 battle_guard [public]" in rendered
    assert "- Action: P1 Set set=1 ids=['battle_all_in'] sources=['hidden_rare'] set_pass_candidates=1 after={'p1': 1, 'p2': 0}" in rendered


def test_render_match_log_markdown_contains_sections_and_action_table() -> None:
    rendered = render_match_log_markdown(make_payload())

    assert "# Match Report: match_000001" in rendered
    assert "## Summary" in rendered
    assert "| Side | Bot | Deck | Reshuffles | Draw Shortfall Turns |" in rendered
    assert "### Turn 1" in rendered
    assert "| Start Draw | draw=2 / hand=6 | draw=0 / hand=6 / overflow=Guard / reshuffle / short=1 |" in rendered
    assert "| Control Sources | pass | public |" in rendered
    assert "| Battle Cards | All In | Guard |" in rendered
    assert "| Battle Card IDs | battle_all_in | battle_guard |" in rendered
    assert "| Hand Count Flow | start=6 / m1=5 / control=5 / m2=5 / end=4 | start=6 / m1=6 / control=5 / m2=5 / end=4 |" in rendered
    assert "- Starting Player: P1" in rendered
    assert "| Action Order | Type | Set Count | Card IDs | Sources | set_pass Cand | Counts After |" in rendered
    assert "| P2 | Set Pass | 1 | battle_guard | public | 1 | P1=1 / P2=1 |" in rendered
