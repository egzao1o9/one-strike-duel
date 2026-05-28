from engine.log_profiles import export_match_record, trim_match_log


def make_payload() -> dict:
    return {
        "match_id": "m1",
        "players": {
            "p1": {"bot": "A", "deck": "d1"},
            "p2": {"bot": "B", "deck": "d2"},
        },
        "turns": [
            {
                "turn": 1,
                "turn_start": {
                    "starting_player": "p1",
                    "p1": {"drawn": ["x"], "hand_count": 4, "overflow_discarded": ["y"]},
                    "p2": {"drawn": ["z"], "hand_count": 4},
                },
                "phase1_mulligan": {"hand_counts": {"p1": 4, "p2": 4}},
                "control": {
                    "hand_counts": {"p1": 3, "p2": 3},
                    "debug": {"selected_id": "c1"},
                    "blessing_changes": {"p1": "placed"},
                },
                "phase3_mulligan": {"hand_counts": {"p1": 3, "p2": 3}},
                "battle": {
                    "p1_hand_count_end": 2,
                    "p2_hand_count_end": 2,
                    "reveal_steps": [{"step": 1}],
                    "blessing_events": [{"kind": "use"}],
                    "actions": [
                        {
                            "player_id": "p1",
                            "debug": {"battle": {"selected": {"prediction": {"predicted_style": "attack"}}}},
                            "hand_count_before": 3,
                            "hand_count_after": 2,
                        }
                    ],
                },
            }
        ],
    }


def test_trim_match_log_standard_keeps_prediction_but_drops_debug() -> None:
    trimmed = trim_match_log(make_payload(), "standard")
    action = trimmed["turns"][0]["battle"]["actions"][0]
    assert "debug" not in action
    assert action["prediction"]["predicted_style"] == "attack"
    assert "hand_count_before" in action


def test_trim_match_log_minimal_drops_verbose_sections() -> None:
    trimmed = trim_match_log(make_payload(), "minimal")
    turn = trimmed["turns"][0]
    assert "drawn" not in turn["turn_start"]["p1"]
    assert "hand_counts" not in turn["phase1_mulligan"]
    assert "debug" not in turn["control"]
    assert "reveal_steps" not in turn["battle"]
    assert "blessing_events" not in turn["battle"]


def test_export_match_record_minimal_drops_heavy_fields() -> None:
    record = {
        "match_id": "m1",
        "battle": {"result": "win"},
        "side_usage_details": {"p1": []},
        "winner_used_card_details": [],
        "winner_decisive_card_details": [],
        "decisive_card_details": {"p1": []},
        "hand_count_trace": [],
        "prediction_analysis": {"p1": {}},
        "blessing_analysis": {"p1": {}},
    }
    exported = export_match_record(record, "minimal")
    assert "battle" not in exported
    assert "prediction_analysis" not in exported
    assert "blessing_analysis" not in exported
