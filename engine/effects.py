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
        if effect.trigger == "next_turn" or effect.timing == "next_turn":
            player.queued_next_turn_effects.append(effect)


def activate_start_of_turn_effects(player: PlayerState) -> int:
    draw_bonus = 0
    player.active_turn_effects = []
    for effect in player.queued_next_turn_effects:
        if effect.kind == "draw_cards":
            draw_bonus += effect.value
        elif effect.effect_type == "modify_rule_value" and effect.stat == "draw_per_turn":
            draw_bonus += effect.value
        else:
            player.active_turn_effects.append(effect)
    player.queued_next_turn_effects.clear()

    blessing = player.blessing_zone
    if blessing and player.blessing_face_up:
        for effect in blessing.effects:
            if not effect.enabled or not effect.is_active_in_zone("blessing_zone"):
                continue
            if effect.effect_type == "modify_rule_value" and effect.stat == "draw_per_turn":
                draw_bonus += effect.value
            elif effect.effect_type == "draw_cards" and effect.trigger == "on_draw_step":
                draw_bonus += effect.count or effect.value
    return draw_bonus


def resolve_information_effects(player: PlayerState, opponent: PlayerState, card: Card, rng=None) -> list[str]:
    revealed: list[str] = []
    for effect in card.effects:
        legacy_kind = effect.legacy_key()
        if legacy_kind == "reveal_opponent_hand_random":
            if opponent.hand:
                chooser = rng.choice if rng is not None else (lambda items: items[0])
                target = chooser(opponent.hand)
                revealed.append(target.name)
            continue
        if effect.effect_type != "reveal_cards":
            continue
        count = max(1, effect.count or 1)
        if effect.target == "opponent_hand":
            pool = list(opponent.hand)
            if not pool:
                continue
            chooser = rng.sample if rng is not None else (lambda items, k: items[:k])
            for target in chooser(pool, min(count, len(pool))):
                revealed.append(target.name)
        elif effect.target == "self_deck":
            for target in list(player.draw_pile)[:count]:
                revealed.append(target.name)
        elif effect.target == "opponent_deck":
            for target in list(opponent.draw_pile)[:count]:
                revealed.append(target.name)
    player.current_reveals.extend(revealed)
    return revealed


def apply_effect(effect: Effect, actor_id: str, sides: dict[str, BattleSide], queued: list[tuple[str, Effect]], source_zone: str = "") -> None:
    actor = sides[actor_id]
    opponent_id = "p2" if actor_id == "p1" else "p1"
    opponent = sides[opponent_id]

    if effect.trigger == "next_turn" or effect.timing == "next_turn":
        queued.append((actor_id, effect))
        return

    if effect.is_legacy():
        _apply_legacy_effect(effect, actor, opponent)
        return

    if effect.effect_type == "modify_total_stat":
        target_side = _select_target_side(effect.target, actor, opponent)
        if target_side is None:
            return
        _modify_stat(target_side, effect.stat, effect.value)
        target_side.applied_effects.append(_effect_log_line(effect, source_zone))
        return

    if effect.effect_type == "modify_rule_value":
        actor.applied_effects.append(_effect_log_line(effect, source_zone))
        return

    if effect.effect_type == "draw_cards":
        actor.applied_effects.append(_effect_log_line(effect, source_zone))
        return

    if effect.effect_type == "negate_card" and effect.target == "opponent_card":
        if 0 not in opponent.invalidated_card_indexes and opponent.source_cards:
            card = opponent.source_cards[0]
            opponent.attack -= card.attack
            opponent.block -= card.block
            opponent.speed -= card.speed
            opponent.invalidated_card_indexes.add(0)
            actor.applied_effects.append(_effect_log_line(effect, source_zone))


def _select_target_side(target: str, actor: BattleSide, opponent: BattleSide) -> BattleSide | None:
    if target in {"self_total", "self_player"}:
        return actor
    if target in {"opponent_total", "opponent_player"}:
        return opponent
    return None


def _modify_stat(side: BattleSide, stat: str, value: int) -> None:
    if stat == "attack":
        side.attack += value
    elif stat == "block":
        side.block += value
    elif stat == "speed":
        side.speed += value


def _effect_log_line(effect: Effect, source_zone: str) -> str:
    zone_label = source_zone or effect.active_zone or "unknown"
    if effect.effect_type:
        return f"{zone_label}:{effect.effect_type}:{effect.target}:{effect.stat}:{effect.value}"
    return f"{zone_label}:{effect.kind}:{effect.value}"


def _apply_legacy_effect(effect: Effect, actor: BattleSide, opponent: BattleSide) -> None:
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
