from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from engine.card import Card, Effect
from engine.effects import BattleSide, apply_effect, finalize_side
from engine.game_state import GameState, PlayerState


@dataclass
class RevealedCardState:
    player_id: str
    index: int
    card: Card
    attack: int
    block: int
    speed: int


@dataclass
class BattleResolution:
    result: str
    winner: str | None
    end_reason: str | None
    finals: dict[str, BattleSide]
    reveal_steps: list[dict[str, Any]] = field(default_factory=list)
    blessing_events: list[dict[str, Any]] = field(default_factory=list)


def resolve_battle(state: GameState) -> BattleResolution:
    players = state.players
    set_cards = {player_id: list(player.set_cards) for player_id, player in players.items()}
    revealed_steps: list[dict[str, Any]] = []
    blessing_events: list[dict[str, Any]] = []
    revealed_card_states: dict[str, list[RevealedCardState]] = {"p1": [], "p2": []}
    player_has_battle = {
        player_id: any(card.type == "battle" for card in cards)
        for player_id, cards in set_cards.items()
    }

    _apply_pre_reveal_blessings(state, set_cards, blessing_events, revealed_steps)

    reveal_order = [state.battle_starting_player, state.opponent_of(state.battle_starting_player)]
    max_cards = max(len(set_cards["p1"]), len(set_cards["p2"]))
    for index in range(max_cards):
        for player_id in reveal_order:
            if index >= len(set_cards[player_id]):
                continue
            card = set_cards[player_id][index]
            card_state = RevealedCardState(
                player_id=player_id,
                index=index,
                card=card,
                attack=card.attack,
                block=card.block,
                speed=card.speed,
            )
            revealed_card_states[player_id].append(card_state)
            revealed_steps.append(
                {
                    "step": len(revealed_steps) + 1,
                    "player_id": player_id,
                    "card_id": card.id,
                    "card_name": card.name,
                    "card_type": card.type,
                    "index": index,
                    "source": card.instance_source or "unknown",
                }
            )
            _apply_on_reveal_effects(
                state,
                player_id,
                card_state,
                revealed_card_states,
                player_has_battle,
                blessing_events,
            )

    sides = {
        player_id: _build_side_from_revealed(player_id, set_cards[player_id], revealed_card_states[player_id])
        for player_id in ("p1", "p2")
    }
    queued_next_turn: list[tuple[str, Effect]] = []

    for player_id, player in players.items():
        for effect in player.active_turn_effects:
            apply_effect(effect, player_id, sides, queued_next_turn)

        if player.current_control_card:
            for effect in player.current_control_card.effects:
                apply_effect(effect, player_id, sides, queued_next_turn, source_zone="control_zone")

        if player.blessing_zone and player.blessing_face_up:
            _apply_blessing_battle_effects(
                state,
                player_id,
                sides,
                revealed_card_states,
                blessing_events,
            )

    for player_id in ("p1", "p2"):
        for card_state in revealed_card_states[player_id]:
            if card_state.index in sides[player_id].invalidated_card_indexes:
                continue
            card = card_state.card
            if card.type == "control" and not player_has_battle[player_id]:
                continue
            for effect in card.effects:
                if _should_skip_reveal_only_effect(effect):
                    continue
                apply_effect(effect, player_id, sides, queued_next_turn, source_zone="set")

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
            return BattleResolution("draw", None, "simultaneous_attack", sides, revealed_steps, blessing_events)
        if p1_success:
            return BattleResolution("win", "p1", "p1_attack_success", sides, revealed_steps, blessing_events)
        if p2_success:
            return BattleResolution("win", "p2", "p2_attack_success", sides, revealed_steps, blessing_events)
        return BattleResolution("no_decision", None, None, sides, revealed_steps, blessing_events)

    first, second = (p1, p2) if p1.speed > p2.speed else (p2, p1)
    if first.attack > 0 and first.attack > second.block:
        return BattleResolution("win", first.player_id, f"{first.player_id}_attack_success", sides, revealed_steps, blessing_events)
    if second.attack > 0 and second.attack > first.block:
        return BattleResolution("win", second.player_id, f"{second.player_id}_attack_success", sides, revealed_steps, blessing_events)
    return BattleResolution("no_decision", None, None, sides, revealed_steps, blessing_events)


def _build_side_from_revealed(player_id: str, all_set_cards: list[Card], revealed_states: list[RevealedCardState]) -> BattleSide:
    battle_states = [card for card in revealed_states if card.card.type == "battle"]
    return BattleSide(
        player_id=player_id,
        source_cards=tuple(all_set_cards),
        attack=sum(card.attack for card in battle_states),
        block=sum(card.block for card in battle_states),
        speed=sum(card.speed for card in battle_states),
    )


def _apply_pre_reveal_blessings(
    state: GameState,
    set_cards: dict[str, list[Card]],
    blessing_events: list[dict[str, Any]],
    revealed_steps: list[dict[str, Any]],
) -> None:
    return


def _apply_on_reveal_effects(
    state: GameState,
    player_id: str,
    card_state: RevealedCardState,
    revealed_card_states: dict[str, list[RevealedCardState]],
    player_has_battle: dict[str, bool],
    blessing_events: list[dict[str, Any]],
) -> None:
    card = card_state.card
    if card.type == "control" and not player_has_battle[player_id]:
        return

    opponent_id = state.opponent_of(player_id)
    player = state.players[player_id]
    opponent = state.players[opponent_id]

    for effect in card.effects:
        effect_key = effect.kind or effect.effect_type
        if effect_key == "negate_opponent_first_card":
            target = _find_revealed_card(revealed_card_states[opponent_id], lambda item: item.index == 0)
            if target is None:
                continue
            target.attack -= target.card.attack
            target.block -= target.card.block
            target.speed -= target.card.speed

def _apply_blessing_battle_effects(
    state: GameState,
    player_id: str,
    sides: dict[str, BattleSide],
    revealed_card_states: dict[str, list[RevealedCardState]],
    blessing_events: list[dict[str, Any]],
) -> None:
    player = state.players[player_id]
    blessing = player.blessing_zone
    if blessing is None or not player.blessing_face_up or player.blessing_locked_this_turn:
        return
    opponent_id = state.opponent_of(player_id)
    own_side = sides[player_id]
    opponent_side = sides[opponent_id]

    if blessing.id == "blessing_attack":
        own_side.attack += 1
        own_side.applied_effects.append("blessing_zone:modify_total_stat:self_total:attack:1")
        return
    if blessing.id == "blessing_guard":
        own_side.block += 1
        own_side.applied_effects.append("blessing_zone:modify_total_stat:self_total:block:1")
        return
    if blessing.id == "blessing_speed":
        own_side.speed += 1
        own_side.applied_effects.append("blessing_zone:modify_total_stat:self_total:speed:1")
        return
    if blessing.id == "blessing_shortblade":
        before = _resolve_current_outcome(player_id, own_side, opponent_side)
        boosted_own = _copy_side(own_side)
        boosted_own.attack += 1
        after = _resolve_current_outcome(player_id, boosted_own, opponent_side)
        if before != "win" and after == "win":
            own_side.attack += 1
            _consume_blessing(state, player_id)
            own_side.applied_effects.append("blessing_zone:modify_total_stat:self_total:attack:1")
            blessing_events.append({"player_id": player_id, "blessing_id": blessing.id, "event": "battle_calculate", "value": 1})
        return
    if blessing.id == "blessing_buckler":
        before = _resolve_current_outcome(player_id, own_side, opponent_side)
        boosted_own = _copy_side(own_side)
        boosted_own.block += 1
        after = _resolve_current_outcome(player_id, boosted_own, opponent_side)
        if before == "lose" and after != "lose":
            own_side.block += 1
            _consume_blessing(state, player_id)
            own_side.applied_effects.append("blessing_zone:modify_total_stat:self_total:block:1")
            blessing_events.append({"player_id": player_id, "blessing_id": blessing.id, "event": "battle_calculate", "value": 1})
        return
    if blessing.id == "blessing_tailwind":
        before = _resolve_current_outcome(player_id, own_side, opponent_side)
        boosted_own = _copy_side(own_side)
        boosted_own.speed += 1
        after = _resolve_current_outcome(player_id, boosted_own, opponent_side)
        if before != "win" and after == "win":
            own_side.speed += 1
            _consume_blessing(state, player_id)
            own_side.applied_effects.append("blessing_zone:modify_total_stat:self_total:speed:1")
            blessing_events.append({"player_id": player_id, "blessing_id": blessing.id, "event": "battle_calculate", "value": 1})
        return
    if blessing.id == "blessing_dullness":
        before = _resolve_current_outcome(player_id, own_side, opponent_side)
        slowed_opponent = _copy_side(opponent_side)
        slowed_opponent.speed -= 1
        after = _resolve_current_outcome(player_id, own_side, slowed_opponent)
        if before != "win" and after == "win":
            opponent_side.speed -= 1
            _consume_blessing(state, player_id)
            own_side.applied_effects.append("blessing_zone:modify_total_stat:opponent_total:speed:-1")
            blessing_events.append({"player_id": player_id, "blessing_id": blessing.id, "event": "battle_calculate", "value": -1})
        return
    if blessing.id == "blessing_parry":
        if opponent_side.attack == own_side.block + 1:
            before = _resolve_current_outcome(player_id, own_side, opponent_side)
            boosted_own = _copy_side(own_side)
            boosted_own.block += 1
            after = _resolve_current_outcome(player_id, boosted_own, opponent_side)
            if before == "lose" and after != "lose":
                own_side.block += 1
                _consume_blessing(state, player_id)
                own_side.applied_effects.append("blessing_zone:modify_total_stat:self_total:block:1")
                blessing_events.append({"player_id": player_id, "blessing_id": blessing.id, "event": "battle_calculate", "value": 1})
        return
    if blessing.id == "blessing_laststand":
        own_battle_count = sum(1 for item in revealed_card_states[player_id] if item.card.type == "battle")
        if own_battle_count <= 2:
            before = _resolve_current_outcome(player_id, own_side, opponent_side)
            boosted_own = _copy_side(own_side)
            boosted_own.block += 2
            after = _resolve_current_outcome(player_id, boosted_own, opponent_side)
            if before == "lose" and after != "lose":
                own_side.block += 2
                _consume_blessing(state, player_id)
                own_side.applied_effects.append("blessing_zone:modify_total_stat:self_total:block:2")
                blessing_events.append({"player_id": player_id, "blessing_id": blessing.id, "event": "battle_calculate", "value": 2})
        return

    if blessing.id == "blessing_offense":
        before = _resolve_current_outcome(player_id, own_side, opponent_side)
        boosted_own = _copy_side(own_side)
        boosted_own.attack += 2
        after = _resolve_current_outcome(player_id, boosted_own, opponent_side)
        if before != "win" and after == "win":
            own_side.attack += 2
            _consume_blessing(state, player_id)
            own_side.applied_effects.append("blessing_zone:modify_total_stat:self_total:attack:2")
            blessing_events.append({"player_id": player_id, "blessing_id": blessing.id, "event": "battle_calculate", "value": 2})
        return
    if blessing.id == "blessing_barrier":
        before = _resolve_current_outcome(player_id, own_side, opponent_side)
        boosted_own = _copy_side(own_side)
        boosted_own.block += 2
        after = _resolve_current_outcome(player_id, boosted_own, opponent_side)
        if before == "lose" and after != "lose":
            own_side.block += 2
            _consume_blessing(state, player_id)
            own_side.applied_effects.append("blessing_zone:modify_total_stat:self_total:block:2")
            blessing_events.append({"player_id": player_id, "blessing_id": blessing.id, "event": "battle_calculate", "value": 2})
        return
    if blessing.id == "blessing_slow":
        before = _resolve_current_outcome(player_id, own_side, opponent_side)
        slowed_opponent = _copy_side(opponent_side)
        slowed_opponent.speed -= 2
        after = _resolve_current_outcome(player_id, own_side, slowed_opponent)
        if before != "win" and after == "win":
            opponent_side.speed -= 2
            _consume_blessing(state, player_id)
            own_side.applied_effects.append("blessing_zone:modify_total_stat:opponent_total:speed:-2")
            blessing_events.append({"player_id": player_id, "blessing_id": blessing.id, "event": "battle_calculate", "value": -2})
        return
    if blessing.id == "blessing_trap_web":
        opponent_battle_count = sum(1 for item in revealed_card_states[opponent_id] if item.card.type == "battle")
        if opponent_battle_count < 3:
            return
        before = _resolve_current_outcome(player_id, own_side, opponent_side)
        weakened_opponent = _copy_side(opponent_side)
        weakened_opponent.attack -= 3
        after = _resolve_current_outcome(player_id, own_side, weakened_opponent)
        if before == "lose" and after != "lose":
            opponent_side.attack -= 3
            _consume_blessing(state, player_id)
            own_side.applied_effects.append("blessing_zone:modify_total_stat:opponent_total:attack:-3")
            blessing_events.append({"player_id": player_id, "blessing_id": blessing.id, "event": "battle_calculate", "value": -3})
        return
    if blessing.id == "blessing_suppression":
        target = _find_revealed_card(
            revealed_card_states[opponent_id],
            lambda item: item.card.type == "battle" and item.attack >= 5,
        )
        if target is None:
            return
        before = _resolve_current_outcome(player_id, own_side, opponent_side)
        weakened_opponent = _copy_side(opponent_side)
        weakened_opponent.attack -= 3
        after = _resolve_current_outcome(player_id, own_side, weakened_opponent)
        if before == "lose" and after != "lose":
            opponent_side.attack -= 3
            _consume_blessing(state, player_id)
            own_side.applied_effects.append("blessing_zone:modify_total_stat:opponent_total:attack:-3")
            blessing_events.append(
                {
                    "player_id": player_id,
                    "blessing_id": blessing.id,
                    "event": "battle_calculate",
                    "target_player_id": opponent_id,
                    "target_card_id": target.card.id,
                    "value": -3,
                }
            )


def _find_revealed_card(cards: list[RevealedCardState], predicate) -> RevealedCardState | None:
    for item in cards:
        if predicate(item):
            return item
    return None


def _should_skip_reveal_only_effect(effect: Effect) -> bool:
    effect_key = effect.kind or effect.effect_type
    return effect_key in {"negate_opponent_first_card", "modify_card_stat"}


def _consume_blessing(state: GameState, player_id: str) -> None:
    player = state.players[player_id]
    if not player.blessing_face_up:
        return
    player.blessing_face_up = False
    player.blessing_used_turns.append(state.turn)
    player.blessing_facedown_turns.append(state.turn)


def _copy_side(side: BattleSide) -> BattleSide:
    return BattleSide(
        player_id=side.player_id,
        source_cards=side.source_cards,
        attack=side.attack,
        block=side.block,
        speed=side.speed,
        block_limit=side.block_limit,
        invalidated_card_indexes=set(side.invalidated_card_indexes),
        applied_effects=list(side.applied_effects),
    )


def _resolve_current_outcome(player_id: str, own_side: BattleSide, opponent_side: BattleSide) -> str:
    if own_side.speed == opponent_side.speed:
        own_success = own_side.attack > 0 and own_side.attack > opponent_side.block
        opponent_success = opponent_side.attack > 0 and opponent_side.attack > own_side.block
        if own_success and not opponent_success:
            return "win"
        if opponent_success and not own_success:
            return "lose"
        if own_success and opponent_success:
            return "draw"
        return "no_decision"

    own_first = own_side.speed > opponent_side.speed
    if own_first:
        if own_side.attack > 0 and own_side.attack > opponent_side.block:
            return "win"
        if opponent_side.attack > 0 and opponent_side.attack > own_side.block:
            return "lose"
        return "no_decision"

    if opponent_side.attack > 0 and opponent_side.attack > own_side.block:
        return "lose"
    if own_side.attack > 0 and own_side.attack > opponent_side.block:
        return "win"
    return "no_decision"
