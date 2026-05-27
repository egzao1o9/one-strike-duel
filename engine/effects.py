from __future__ import annotations

from dataclasses import dataclass, field

from engine.card import Card, Effect
from engine.game_state import PlayerState


@dataclass
class BattleSide:
    player_id: str
    source_cards: tuple[Card, ...]
    attack: int
    block: int
    speed: int
    block_limit: int | None = None
    invalidated_card_indexes: set[int] = field(default_factory=set)
    applied_effects: list[str] = field(default_factory=list)


def queue_next_turn_effects(player: PlayerState, card: Card) -> None:
    for effect in card.effects:
        if effect.timing == "next_turn":
            player.queued_next_turn_effects.append(effect)


def activate_start_of_turn_effects(player: PlayerState) -> int:
    draw_bonus = 0
    player.active_turn_effects = []
    for effect in player.queued_next_turn_effects:
        if effect.kind == "draw_cards":
            draw_bonus += effect.value
        else:
            player.active_turn_effects.append(Effect(timing="battle", kind=effect.kind, value=effect.value))
    player.queued_next_turn_effects.clear()
    return draw_bonus


def resolve_information_effects(player: PlayerState, opponent: PlayerState, card: Card) -> list[str]:
    revealed: list[str] = []
    for effect in card.effects:
        if effect.kind != "reveal_opponent_hand_random":
            continue
        if opponent.hand:
            target = opponent.hand[0]
            revealed.append(target.name)
    player.current_reveals.extend(revealed)
    return revealed


def apply_effect(effect: Effect, actor_id: str, sides: dict[str, BattleSide], queued: list[tuple[str, Effect]]) -> None:
    actor = sides[actor_id]
    opponent_id = "p2" if actor_id == "p1" else "p1"
    opponent = sides[opponent_id]

    if effect.timing == "next_turn":
        queued.append((actor_id, effect))
        return

    if effect.kind == "modify_self_attack":
        actor.attack += effect.value
    elif effect.kind == "modify_self_block":
        actor.block += effect.value
    elif effect.kind == "modify_self_speed":
        actor.speed += effect.value
    elif effect.kind == "modify_opponent_attack":
        opponent.attack -= effect.value
    elif effect.kind == "modify_opponent_block":
        opponent.block -= effect.value
    elif effect.kind == "modify_opponent_speed":
        opponent.speed -= effect.value
    elif effect.kind == "negate_opponent_first_card":
        if 0 not in opponent.invalidated_card_indexes and opponent.source_cards:
            card = opponent.source_cards[0]
            opponent.attack -= card.attack
            opponent.block -= card.block
            opponent.speed -= card.speed
            opponent.invalidated_card_indexes.add(0)
    elif effect.kind == "set_self_block_limit":
        actor.block_limit = effect.value if actor.block_limit is None else min(actor.block_limit, effect.value)
    else:
        return

    actor.applied_effects.append(f"{effect.kind}:{effect.value}")


def finalize_side(side: BattleSide) -> None:
    if side.block_limit is not None:
        side.block = min(side.block, side.block_limit)
    side.block = max(side.block, 0)
