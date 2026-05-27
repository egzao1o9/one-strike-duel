from __future__ import annotations

from dataclasses import dataclass

from engine.effects import BattleSide, apply_effect, finalize_side
from engine.game_state import GameState


@dataclass
class BattleResolution:
    result: str
    winner: str | None
    end_reason: str | None
    finals: dict[str, BattleSide]


def resolve_battle(state: GameState) -> BattleResolution:
    players = state.players
    sides = {
        player_id: BattleSide(
            player_id=player_id,
            source_cards=tuple(player.set_cards),
            attack=sum(card.attack for card in player.set_cards),
            block=sum(card.block for card in player.set_cards),
            speed=sum(card.speed for card in player.set_cards),
        )
        for player_id, player in players.items()
    }
    queued_next_turn: list[tuple[str, object]] = []

    for player_id, player in players.items():
        for effect in player.active_turn_effects:
            apply_effect(effect, player_id, sides, queued_next_turn)
        if player.current_control_card:
            for effect in player.current_control_card.effects:
                apply_effect(effect, player_id, sides, queued_next_turn)
        for index, card in enumerate(player.set_cards):
            if index in sides[player_id].invalidated_card_indexes:
                continue
            for effect in card.effects:
                apply_effect(effect, player_id, sides, queued_next_turn)

    for player_id, effect in queued_next_turn:
        players[player_id].queued_next_turn_effects.append(effect)

    for side in sides.values():
        finalize_side(side)

    p1 = sides["p1"]
    p2 = sides["p2"]

    if p1.speed == p2.speed:
        p1_success = p1.attack > 0 and p1.attack > p2.block
        p2_success = p2.attack > 0 and p2.attack > p1.block
        if p1_success and p2_success:
            return BattleResolution("draw", None, "simultaneous_attack", sides)
        if p1_success:
            return BattleResolution("win", "p1", "p1_attack_success", sides)
        if p2_success:
            return BattleResolution("win", "p2", "p2_attack_success", sides)
        return BattleResolution("no_decision", None, None, sides)

    first, second = (p1, p2) if p1.speed > p2.speed else (p2, p1)
    if first.attack > 0 and first.attack > second.block:
        return BattleResolution("win", first.player_id, f"{first.player_id}_attack_success", sides)
    if second.attack > 0 and second.attack > first.block:
        return BattleResolution("win", second.player_id, f"{second.player_id}_attack_success", sides)
    return BattleResolution("no_decision", None, None, sides)
