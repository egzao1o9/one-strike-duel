from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PLAYER_LABELS = {
    "p1": "P1",
    "p2": "P2",
}

RESULT_LABELS = {
    "win": "Win",
    "draw": "Draw",
    "no_decision": "No Decision",
}

END_REASON_LABELS = {
    None: "No Decision",
    "p1_attack_success": "P1 attack success",
    "p2_attack_success": "P2 attack success",
    "simultaneous_attack": "Simultaneous attack draw",
    "max_turns_reached": "Max turns reached",
}


def load_match_log(path: str | Path) -> dict[str, Any]:
    file_path = Path(path)
    with file_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def render_match_log_text(payload: dict[str, Any]) -> str:
    players = payload["players"]
    winner = payload.get("winner")
    end_reason = payload.get("end_reason")
    lines = [
        f"Match: {payload['match_id']}",
        f"P1: {players['p1']['bot']} / deck={players['p1']['deck']}",
        f"P2: {players['p2']['bot']} / deck={players['p2']['deck']}",
        f"Winner: {PLAYER_LABELS[winner] if winner else 'Draw'}",
        f"End Reason: {END_REASON_LABELS.get(end_reason, str(end_reason))}",
        f"Turns: {payload.get('turn_count', len(payload.get('turns', [])))}",
        "",
    ]

    for turn in payload.get("turns", []):
        lines.extend(_render_turn(turn))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_match_log_markdown(payload: dict[str, Any]) -> str:
    players = payload["players"]
    winner = payload.get("winner")
    end_reason = payload.get("end_reason")
    lines = [
        f"# Match Report: {payload['match_id']}",
        "",
        "## Summary",
        "",
        "| Side | Bot | Deck | Reshuffles | Draw Shortfall Turns |",
        "|---|---|---|---:|---|",
        _render_player_summary_row("p1", players["p1"]),
        _render_player_summary_row("p2", players["p2"]),
        "",
        f"- P1 Blessing: {_render_player_blessing_summary(players['p1'])}",
        f"- P2 Blessing: {_render_player_blessing_summary(players['p2'])}",
        f"- Winner: {PLAYER_LABELS[winner] if winner else 'Draw'}",
        f"- End Reason: {END_REASON_LABELS.get(end_reason, str(end_reason))}",
        f"- Turns: {payload.get('turn_count', len(payload.get('turns', [])))}",
        "",
        "## Turns",
        "",
    ]

    for turn in payload.get("turns", []):
        lines.extend(_render_turn_markdown(turn))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def _render_player_summary_row(player_id: str, player: dict[str, Any]) -> str:
    return (
        f"| {PLAYER_LABELS[player_id]} | {player['bot']} | `{player['deck']}` | "
        f"{player.get('reshuffle_count', 0)} | {', '.join(str(value) for value in player.get('draw_shortfall_turns', [])) or '-'} |"
    )


def _render_turn(turn: dict[str, Any]) -> list[str]:
    turn_start = turn.get("turn_start", {})
    phase1 = turn.get("phase1_mulligan", {})
    control = turn.get("control", {})
    phase3 = turn.get("phase3_mulligan", {})
    battle = turn.get("battle", {})

    lines = [
        f"Turn {turn['turn']}",
        f"- Start: first={PLAYER_LABELS.get(turn_start.get('starting_player'), '?')} / P1 draw={turn_start.get('p1', {}).get('draw_count', 0)} / P2 draw={turn_start.get('p2', {}).get('draw_count', 0)}",
        f"- Mulligan1: P1 {_render_card_list(phase1.get('p1_discarded', []))} / P2 {_render_card_list(phase1.get('p2_discarded', []))}",
        f"- Control: P1 {_render_card_name(control.get('p1'))} / P2 {_render_card_name(control.get('p2'))}",
        f"- Control IDs: P1 {_render_card_name(control.get('ids', {}).get('p1'))} [{_render_card_name(control.get('sources', {}).get('p1'))}] "
        f"/ P2 {_render_card_name(control.get('ids', {}).get('p2'))} [{_render_card_name(control.get('sources', {}).get('p2'))}]",
        f"- Mulligan2: P1 {_render_card_list(phase3.get('p1_discarded', []))} / P2 {_render_card_list(phase3.get('p2_discarded', []))}",
        f"- Hand Counts: start P1={turn_start.get('p1', {}).get('hand_count', '?')} / P2={turn_start.get('p2', {}).get('hand_count', '?')} ; "
        f"m1 P1={phase1.get('hand_counts', {}).get('p1', '?')} / P2={phase1.get('hand_counts', {}).get('p2', '?')} ; "
        f"control P1={control.get('hand_counts', {}).get('p1', '?')} / P2={control.get('hand_counts', {}).get('p2', '?')} ; "
        f"m2 P1={phase3.get('hand_counts', {}).get('p1', '?')} / P2={phase3.get('hand_counts', {}).get('p2', '?')} ; "
        f"battle_end P1={battle.get('p1_hand_count_end', '?')} / P2={battle.get('p2_hand_count_end', '?')}",
    ]

    for side in ("p1", "p2"):
        start_info = turn_start.get(side, {})
        if start_info.get("overflow_discarded"):
            lines.append(f"- Overflow {PLAYER_LABELS[side]}: {_render_card_list(start_info.get('overflow_discarded', []))}")
        if start_info.get("reshuffled"):
            lines.append(f"- Reshuffle: {PLAYER_LABELS[side]}")
        if start_info.get("draw_shortfall"):
            lines.append(f"- Draw Shortfall {PLAYER_LABELS[side]}: {start_info.get('draw_shortfall')}")

    reveals = control.get("reveals", {})
    if reveals.get("p1") or reveals.get("p2"):
        lines.append(f"- Reveals: P1 {_render_card_list(reveals.get('p1', []))} / P2 {_render_card_list(reveals.get('p2', []))}")

    lines.append(
        f"- Battle: P1 {_render_battle_side(battle, 'p1')} vs P2 {_render_battle_side(battle, 'p2')}"
    )
    lines.append(
        f"- Blessing: P1 {_render_blessing_state(battle, 'p1')} / P2 {_render_blessing_state(battle, 'p2')}"
    )
    lines.append(
        f"- Battle IDs: P1 {_render_card_list(battle.get('p1_card_ids', []))} [{_render_card_list(battle.get('p1_card_sources', []))}] "
        f"/ P2 {_render_card_list(battle.get('p2_card_ids', []))} [{_render_card_list(battle.get('p2_card_sources', []))}]"
    )
    lines.append(
        f"- Revealed Set Cards: P1 {_render_face_up_cards(battle, 'p1')} / P2 {_render_face_up_cards(battle, 'p2')}"
    )
    lines.append(f"- Initiative: {_get_initiative_label(battle)}")
    lines.append(f"- Result: {RESULT_LABELS.get(battle.get('result'), battle.get('result', 'unknown'))}")
    if battle.get("actions"):
        for action in battle["actions"]:
            lines.append(
                f"- Action: {PLAYER_LABELS.get(action['player_id'], action['player_id'])} {action.get('action_name', action.get('action_type'))} "
                f"set={action.get('set_count', 0)} ids={action.get('set_card_ids', [])} sources={action.get('set_card_sources', [])} "
                f"set_pass_candidates={action.get('set_pass_candidate_count')} after={action.get('counts_after', {})}"
            )
            if action.get("face_up_card_names"):
                lines.append(f"- Face Up: {_render_card_list(action.get('face_up_card_names', []))}")
            prediction = action.get("prediction") or action.get("debug", {}).get("battle", {}).get("selected", {}).get("prediction")
            if prediction:
                lines.append(
                    f"- Prediction: style={prediction.get('predicted_style')} line={prediction.get('predicted_line')} "
                    f"closing={prediction.get('predicted_closing_style')} plan={prediction.get('response_plan')} mode={prediction.get('mode')}"
                )
            if action.get("debug"):
                lines.append(f"- Debug: {action.get('debug')}")
    if battle.get("reveal_steps"):
        lines.append(f"- Reveal Steps: {battle.get('reveal_steps')}")
    if battle.get("blessing_events"):
        lines.append(f"- Blessing Events: {battle.get('blessing_events')}")
    return lines


def _render_turn_markdown(turn: dict[str, Any]) -> list[str]:
    turn_start = turn.get("turn_start", {})
    phase1 = turn.get("phase1_mulligan", {})
    control = turn.get("control", {})
    phase3 = turn.get("phase3_mulligan", {})
    battle = turn.get("battle", {})

    lines = [
        f"### Turn {turn['turn']}",
        "",
        "| Item | P1 | P2 |",
        "|---|---|---|",
        f"| Start Draw | {_render_start_info(turn_start.get('p1', {}))} | {_render_start_info(turn_start.get('p2', {}))} |",
        f"| Mulligan1 | {_render_card_list(phase1.get('p1_discarded', []))} | {_render_card_list(phase1.get('p2_discarded', []))} |",
        f"| Control | {_render_card_name(control.get('p1'))} | {_render_card_name(control.get('p2'))} |",
        f"| Control IDs | {_render_card_name(control.get('ids', {}).get('p1'))} | {_render_card_name(control.get('ids', {}).get('p2'))} |",
        f"| Control Sources | {_render_card_name(control.get('sources', {}).get('p1'))} | {_render_card_name(control.get('sources', {}).get('p2'))} |",
        f"| Mulligan2 | {_render_card_list(phase3.get('p1_discarded', []))} | {_render_card_list(phase3.get('p2_discarded', []))} |",
        f"| Battle Cards | {_render_played_cards(battle, 'p1')} | {_render_played_cards(battle, 'p2')} |",
        f"| Blessing | {_render_blessing_state(battle, 'p1')} | {_render_blessing_state(battle, 'p2')} |",
        f"| Battle Card IDs | {_render_card_list(battle.get('p1_card_ids', []))} | {_render_card_list(battle.get('p2_card_ids', []))} |",
        f"| Battle Card Sources | {_render_card_list(battle.get('p1_card_sources', []))} | {_render_card_list(battle.get('p2_card_sources', []))} |",
        f"| Revealed Set Cards | {_render_face_up_cards(battle, 'p1')} | {_render_face_up_cards(battle, 'p2')} |",
        f"| Final Stats | {_render_battle_stats(battle, 'p1')} | {_render_battle_stats(battle, 'p2')} |",
        f"| Facedown Count | {battle.get('p1_facedown_count', '-')} | {battle.get('p2_facedown_count', '-')} |",
        f"| Hand Count Flow | {_render_hand_flow(turn, 'p1')} | {_render_hand_flow(turn, 'p2')} |",
        "",
        f"- Starting Player: {PLAYER_LABELS.get(battle.get('starting_player'), PLAYER_LABELS.get(turn_start.get('starting_player'), '?'))}",
        f"- First Pass Player: {PLAYER_LABELS.get(battle.get('first_pass_player'), '-') if battle.get('first_pass_player') else '-'}",
        f"- Initiative: {_get_initiative_label(battle)}",
        f"- Result: {RESULT_LABELS.get(battle.get('result'), battle.get('result', 'unknown'))}",
    ]

    if battle.get("winner_facedown_count") is not None:
        lines.append(
            f"- Winner Card Count: winner={battle.get('winner_facedown_count')} loser={battle.get('loser_facedown_count')} "
            f"/ fewer={battle.get('won_with_fewer_cards')} same={battle.get('won_with_same_cards')} more={battle.get('won_with_more_cards')}"
        )

    reveals = control.get("reveals", {})
    if reveals.get("p1") or reveals.get("p2"):
        lines.append(f"- Reveals: P1 {_render_card_list(reveals.get('p1', []))} / P2 {_render_card_list(reveals.get('p2', []))}")

    if battle.get("actions"):
        lines.extend(["", "| Action Order | Type | Set Count | Card IDs | Sources | set_pass Cand | Counts After |", "|---|---|---:|---|---|---:|---|"])
        for action in battle["actions"]:
            lines.append(
                f"| {PLAYER_LABELS.get(action['player_id'], action['player_id'])} | {action.get('action_name', action.get('action_type'))} | "
                f"{action.get('set_count', 0)} | {_render_card_list(action.get('set_card_ids', []))} | {_render_card_list(action.get('set_card_sources', []))} | "
                f"{action.get('set_pass_candidate_count', '-')} | P1={action.get('counts_after', {}).get('p1', '?')} / P2={action.get('counts_after', {}).get('p2', '?')} |"
            )
            if action.get("face_up_card_names"):
                lines.append(
                    f"| Open | {_render_card_list(action.get('face_up_card_names', []))} | - | - | - | - | - |"
                )
            prediction = action.get("prediction") or action.get("debug", {}).get("battle", {}).get("selected", {}).get("prediction")
            if prediction:
                lines.append(
                    f"| Prediction | `{prediction.get('predicted_style')}` / `{prediction.get('predicted_line')}` / `{prediction.get('response_plan')}` | - | - | - | - | - |"
                )
            if action.get("debug"):
                lines.append(f"| Debug | `{str(action.get('debug'))}` | - | - | - | - | - |")
    if battle.get("reveal_steps"):
        lines.append(f"- Reveal Steps: `{battle.get('reveal_steps')}`")
    if battle.get("blessing_events"):
        lines.append(f"- Blessing Events: `{battle.get('blessing_events')}`")

    return lines


def _render_start_info(info: dict[str, Any]) -> str:
    parts = [f"draw={info.get('draw_count', 0)}", f"hand={info.get('hand_count', '?')}"]
    if info.get("overflow_discarded"):
        parts.append(f"overflow={_render_card_list(info.get('overflow_discarded', []))}")
    if info.get("reshuffled"):
        parts.append("reshuffle")
    if info.get("draw_shortfall"):
        parts.append(f"short={info.get('draw_shortfall')}")
    return " / ".join(parts)


def _render_hand_flow(turn: dict[str, Any], side: str) -> str:
    return (
        f"start={turn.get('turn_start', {}).get(side, {}).get('hand_count', '?')} / "
        f"m1={turn.get('phase1_mulligan', {}).get('hand_counts', {}).get(side, '?')} / "
        f"control={turn.get('control', {}).get('hand_counts', {}).get(side, '?')} / "
        f"m2={turn.get('phase3_mulligan', {}).get('hand_counts', {}).get(side, '?')} / "
        f"end={turn.get('battle', {}).get(f'{side}_hand_count_end', '?')}"
    )


def _get_initiative_label(battle: dict[str, Any]) -> str:
    p1_speed = battle.get("p1_final", {}).get("speed")
    p2_speed = battle.get("p2_final", {}).get("speed")
    if p1_speed is None or p2_speed is None:
        return "Unknown"
    if p1_speed == p2_speed:
        return f"Tie ({p1_speed})"
    faster = "P1" if p1_speed > p2_speed else "P2"
    return f"{faster} First"


def _render_battle_side(battle: dict[str, Any], player_id: str) -> str:
    card_name = _render_played_cards(battle, player_id)
    return f"{card_name} [{_render_battle_stats(battle, player_id)}]"


def _render_battle_stats(battle: dict[str, Any], player_id: str) -> str:
    final = battle.get(f"{player_id}_final", {})
    return f"A={final.get('attack', '?')} B={final.get('block', '?')} S={final.get('speed', '?')}"


def _render_card_name(card_name: str | None) -> str:
    return card_name if card_name else "pass"


def _render_card_list(cards: list[str]) -> str:
    return ", ".join(cards) if cards else "-"


def _render_played_cards(battle: dict[str, Any], player_id: str) -> str:
    cards = battle.get(f"{player_id}_cards")
    if isinstance(cards, list):
        return _render_card_list(cards)
    legacy_card = battle.get(f"{player_id}_card")
    return _render_card_name(legacy_card)


def _render_blessing_state(battle: dict[str, Any], player_id: str) -> str:
    blessing_id = battle.get(f"{player_id}_active_blessing")
    if not blessing_id:
        return "-"
    return f"{blessing_id} ({'up' if battle.get(f'{player_id}_blessing_face_up') else 'down'})"


def _render_face_up_cards(battle: dict[str, Any], player_id: str) -> str:
    cards = battle.get(f"{player_id}_cards", [])
    indexes = battle.get(f"{player_id}_revealed_set_indexes", [])
    if not cards or not indexes:
        return "-"
    revealed = [cards[index] for index in indexes if 0 <= index < len(cards)]
    return _render_card_list(revealed)


def _render_player_blessing_summary(player: dict[str, Any]) -> str:
    blessing_id = player.get("active_blessing")
    if not blessing_id:
        return "-"
    return (
        f"{blessing_id} ({'up' if player.get('blessing_face_up', True) else 'down'}) / "
        f"placed={_render_int_list(player.get('blessing_placed_turns', []))} / "
        f"used={_render_int_list(player.get('blessing_used_turns', []))} / "
        f"down={_render_int_list(player.get('blessing_facedown_turns', []))} / "
        f"pressure={player.get('blessing_pressure_pass_actions', 0)}"
    )


def _render_int_list(values: list[int]) -> str:
    return ", ".join(str(value) for value in values) if values else "-"
