from __future__ import annotations

from copy import deepcopy
from typing import Any


MATCH_LOG_PROFILES = {"minimal", "standard", "full"}
RECORD_PROFILES = {"minimal", "standard", "full"}


def normalize_match_log_profile(profile: str | None) -> str:
    value = (profile or "standard").lower()
    if value not in MATCH_LOG_PROFILES:
        raise ValueError(f"unsupported match_log_profile: {profile}")
    return value


def normalize_record_profile(profile: str | None) -> str:
    value = (profile or "standard").lower()
    if value not in RECORD_PROFILES:
        raise ValueError(f"unsupported record_profile: {profile}")
    return value


def trim_match_log(payload: dict[str, Any], profile: str | None) -> dict[str, Any]:
    mode = normalize_match_log_profile(profile)
    if mode == "full":
        return deepcopy(payload)

    trimmed = deepcopy(payload)
    for turn in trimmed.get("turns", []):
        if mode == "minimal":
            turn_start = turn.get("turn_start", {})
            for side in ("p1", "p2"):
                if side in turn_start:
                    turn_start[side].pop("drawn", None)
                    turn_start[side].pop("overflow_discarded", None)
                    turn_start[side].pop("hand_count", None)
            if "phase1_mulligan" in turn:
                turn["phase1_mulligan"].pop("hand_counts", None)
            if "phase3_mulligan" in turn:
                turn["phase3_mulligan"].pop("hand_counts", None)
            if "control" in turn:
                turn["control"].pop("hand_counts", None)
                turn["control"].pop("debug", None)
                turn["control"].pop("blessing_changes", None)
            if "battle" in turn:
                battle = turn["battle"]
                battle.pop("reveal_steps", None)
                battle.pop("blessing_events", None)
                battle.pop("p1_hand_count_end", None)
                battle.pop("p2_hand_count_end", None)
                for action in battle.get("actions", []):
                    action.pop("debug", None)
                    action.pop("hand_count_before", None)
                    action.pop("hand_count_after", None)
        elif mode == "standard":
            if "control" in turn:
                turn["control"].pop("debug", None)
            if "battle" in turn:
                battle = turn["battle"]
                for action in battle.get("actions", []):
                    prediction = action.get("debug", {}).get("battle", {}).get("selected", {}).get("prediction")
                    if prediction:
                        action["prediction"] = prediction
                    action.pop("debug", None)
    return trimmed


def export_match_record(record: dict[str, Any], profile: str | None) -> dict[str, Any]:
    mode = normalize_record_profile(profile)
    exported = deepcopy(record)
    if mode == "full":
        return exported

    if mode == "standard":
        exported.pop("battle", None)
        return exported

    exported.pop("battle", None)
    exported.pop("side_usage_details", None)
    exported.pop("winner_used_card_details", None)
    exported.pop("winner_decisive_card_details", None)
    exported.pop("decisive_card_details", None)
    exported.pop("hand_count_trace", None)
    exported.pop("prediction_analysis", None)
    exported.pop("blessing_analysis", None)
    return exported
