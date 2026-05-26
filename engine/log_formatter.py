from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PLAYER_LABELS = {
    "p1": "P1",
    "p2": "P2",
}

RESULT_LABELS = {
    "win": "勝敗決着",
    "draw": "引き分け",
    "no_decision": "決着なし",
}

END_REASON_LABELS = {
    None: "未決着",
    "p1_attack_success": "P1 の攻撃成功",
    "p2_attack_success": "P2 の攻撃成功",
    "simultaneous_attack": "同速相打ち",
    "both_players_stuck": "両者行動不能",
    "max_turns_reached": "最大ターン到達",
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
        "| Side | Bot | Deck |",
        "|---|---|---|",
        f"| P1 | {players['p1']['bot']} | `{players['p1']['deck']}` |",
        f"| P2 | {players['p2']['bot']} | `{players['p2']['deck']}` |",
        "",
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


def _render_turn(turn: dict[str, Any]) -> list[str]:
    phase1 = turn.get("phase1_mulligan", {})
    control = turn.get("control", {})
    phase3 = turn.get("phase3_mulligan", {})
    battle = turn.get("battle", {})

    p1_speed = battle.get("p1_final", {}).get("speed")
    p2_speed = battle.get("p2_final", {}).get("speed")
    if p1_speed is None or p2_speed is None:
        initiative = "不明"
    elif p1_speed == p2_speed:
        initiative = f"同速 ({p1_speed})"
    else:
        faster = "P1" if p1_speed > p2_speed else "P2"
        initiative = f"{faster} 先制"

    lines = [
        f"Turn {turn['turn']}",
        f"- Mulligan1: P1 {_render_card_list(phase1.get('p1_discarded', []))} / P2 {_render_card_list(phase1.get('p2_discarded', []))}",
        f"- Control: P1 {_render_card_name(control.get('p1'))} / P2 {_render_card_name(control.get('p2'))}",
        f"- Mulligan2: P1 {_render_card_list(phase3.get('p1_discarded', []))} / P2 {_render_card_list(phase3.get('p2_discarded', []))}",
    ]

    reveals = control.get("reveals", {})
    if reveals.get("p1") or reveals.get("p2"):
        lines.append(f"- Reveals: P1 {_render_card_list(reveals.get('p1', []))} / P2 {_render_card_list(reveals.get('p2', []))}")

    lines.extend(
        [
            f"- Battle: P1 {_render_battle_side(battle, 'p1')} vs P2 {_render_battle_side(battle, 'p2')}",
            f"- Initiative: {initiative}",
            f"- Result: {RESULT_LABELS.get(battle.get('result'), battle.get('result', 'unknown'))}",
        ]
    )
    return lines


def _render_turn_markdown(turn: dict[str, Any]) -> list[str]:
    phase1 = turn.get("phase1_mulligan", {})
    control = turn.get("control", {})
    phase3 = turn.get("phase3_mulligan", {})
    battle = turn.get("battle", {})
    initiative = _get_initiative_label(battle)

    lines = [
        f"### Turn {turn['turn']}",
        "",
        "| Item | P1 | P2 |",
        "|---|---|---|",
        f"| Mulligan1 | {_render_card_list(phase1.get('p1_discarded', []))} | {_render_card_list(phase1.get('p2_discarded', []))} |",
        f"| Control | {_render_card_name(control.get('p1'))} | {_render_card_name(control.get('p2'))} |",
        f"| Mulligan2 | {_render_card_list(phase3.get('p1_discarded', []))} | {_render_card_list(phase3.get('p2_discarded', []))} |",
        f"| Battle Cards | {_render_played_cards(battle, 'p1')} | {_render_played_cards(battle, 'p2')} |",
        f"| Final Stats | {_render_battle_stats(battle, 'p1')} | {_render_battle_stats(battle, 'p2')} |",
        "",
        f"- Initiative: {initiative}",
        f"- Result: {RESULT_LABELS.get(battle.get('result'), battle.get('result', 'unknown'))}",
    ]

    reveals = control.get("reveals", {})
    if reveals.get("p1") or reveals.get("p2"):
        lines.append(f"- Reveals: P1 {_render_card_list(reveals.get('p1', []))} / P2 {_render_card_list(reveals.get('p2', []))}")

    return lines


def _get_initiative_label(battle: dict[str, Any]) -> str:
    p1_speed = battle.get("p1_final", {}).get("speed")
    p2_speed = battle.get("p2_final", {}).get("speed")
    if p1_speed is None or p2_speed is None:
        return "不明"
    if p1_speed == p2_speed:
        return f"同速 ({p1_speed})"
    faster = "P1" if p1_speed > p2_speed else "P2"
    return f"{faster} 先制"


def _render_battle_side(battle: dict[str, Any], player_id: str) -> str:
    card_name = _render_played_cards(battle, player_id)
    return (
        f"{card_name} "
        f"[{_render_battle_stats(battle, player_id)}]"
    )


def _render_battle_stats(battle: dict[str, Any], player_id: str) -> str:
    final = battle.get(f"{player_id}_final", {})
    return f"A={final.get('attack', '?')} B={final.get('block', '?')} S={final.get('speed', '?')}"


def _render_card_name(card_name: str | None) -> str:
    return card_name if card_name else "pass"


def _render_card_list(cards: list[str]) -> str:
    return ", ".join(cards) if cards else "なし"


def _render_played_cards(battle: dict[str, Any], player_id: str) -> str:
    cards = battle.get(f"{player_id}_cards")
    if isinstance(cards, list):
        return _render_card_list(cards)
    legacy_card = battle.get(f"{player_id}_card")
    return _render_card_name(legacy_card)
