from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import combinations

from engine.card import Card, Effect
from engine.game_state import PlayerView


@dataclass(frozen=True)
class StatLine:
    attack: int = 0
    block: int = 0
    speed: int = 0

    def add(self, other: "StatLine") -> "StatLine":
        return StatLine(
            attack=self.attack + other.attack,
            block=self.block + other.block,
            speed=self.speed + other.speed,
        )


@dataclass(frozen=True)
class DeckProfile:
    total_cards: int
    battle_count: int
    control_count: int
    average_attack: float
    average_block: float
    average_speed: float
    max_attack: int
    max_block: int
    max_speed: int


@dataclass(frozen=True)
class HandProfile:
    battle_count: int
    control_count: int
    best_attack: StatLine
    best_block: StatLine
    best_speed: StatLine
    best_attack_combo: tuple[str, ...]
    best_block_combo: tuple[str, ...]
    best_speed_combo: tuple[str, ...]


def battle_cards(cards: list[Card] | tuple[Card, ...]) -> list[Card]:
    return [card for card in cards if card.type == "battle"]


def control_cards(cards: list[Card] | tuple[Card, ...]) -> list[Card]:
    return [card for card in cards if card.type == "control"]


def card_line(card: Card) -> StatLine:
    return StatLine(card.attack, card.block, card.speed)


def effect_line(effects: list[Effect] | tuple[Effect, ...], *, perspective: str = "self") -> StatLine:
    attack = 0
    block = 0
    speed = 0
    prefix = "modify_self_" if perspective == "self" else "modify_opponent_"
    for effect in effects:
        if effect.timing != "battle" or not effect.kind.startswith(prefix):
            continue
        if effect.kind.endswith("attack"):
            attack += effect.value
        elif effect.kind.endswith("block"):
            block += effect.value
        elif effect.kind.endswith("speed"):
            speed += effect.value
    return StatLine(attack, block, speed)


def sum_lines(lines: list[StatLine]) -> StatLine:
    total = StatLine()
    for line in lines:
        total = total.add(line)
    return total


def combined_battle_line(
    cards: list[Card] | tuple[Card, ...],
    *,
    own_control: Card | None = None,
    opponent_control: Card | None = None,
) -> tuple[StatLine, StatLine]:
    own = sum_lines([card_line(card) for card in cards])
    own = own.add(effect_line(tuple(effect for card in cards for effect in card.effects), perspective="self"))
    opp_delta = effect_line(tuple(effect for card in cards for effect in card.effects), perspective="opponent")
    if own_control is not None:
        own = own.add(effect_line(own_control.effects, perspective="self"))
        opp_delta = opp_delta.add(effect_line(own_control.effects, perspective="opponent"))
    if opponent_control is not None:
        own = own.add(effect_line(opponent_control.effects, perspective="opponent"))
        opp_delta = opp_delta.add(effect_line(opponent_control.effects, perspective="self"))
    return own, opp_delta


def enumerate_battle_combos(cards: list[Card] | tuple[Card, ...], *, max_cards: int = 2) -> list[tuple[tuple[Card, ...], StatLine]]:
    battles = battle_cards(cards)
    combos: list[tuple[tuple[Card, ...], StatLine]] = []
    for count in range(1, min(max_cards, len(battles)) + 1):
        for combo in combinations(battles, count):
            combos.append((combo, sum_lines([card_line(card) for card in combo])))
    return combos


def build_hand_profile(cards: list[Card] | tuple[Card, ...]) -> HandProfile:
    battles = battle_cards(cards)
    controls = control_cards(cards)
    best_attack_line = StatLine()
    best_block_line = StatLine()
    best_speed_line = StatLine()
    best_attack_combo: tuple[str, ...] = tuple()
    best_block_combo: tuple[str, ...] = tuple()
    best_speed_combo: tuple[str, ...] = tuple()
    for combo, line in enumerate_battle_combos(battles):
        combo_ids = tuple(card.id for card in combo)
        if (line.attack, line.speed, line.block) > (best_attack_line.attack, best_attack_line.speed, best_attack_line.block):
            best_attack_line = line
            best_attack_combo = combo_ids
        if (line.block, line.speed, line.attack) > (best_block_line.block, best_block_line.speed, best_block_line.attack):
            best_block_line = line
            best_block_combo = combo_ids
        if (line.speed, line.attack, line.block) > (best_speed_line.speed, best_speed_line.attack, best_speed_line.block):
            best_speed_line = line
            best_speed_combo = combo_ids
    return HandProfile(
        battle_count=len(battles),
        control_count=len(controls),
        best_attack=best_attack_line,
        best_block=best_block_line,
        best_speed=best_speed_line,
        best_attack_combo=best_attack_combo,
        best_block_combo=best_block_combo,
        best_speed_combo=best_speed_combo,
    )


def profile_card_ids(card_ids: list[str] | tuple[str, ...], cards_by_id: dict[str, Card]) -> DeckProfile:
    cards = [cards_by_id[card_id] for card_id in card_ids if card_id in cards_by_id]
    return profile_cards(cards)


def profile_cards(cards: list[Card] | tuple[Card, ...]) -> DeckProfile:
    battles = battle_cards(cards)
    controls = control_cards(cards)
    if battles:
        attack_values = [card.attack for card in battles]
        block_values = [card.block for card in battles]
        speed_values = [card.speed for card in battles]
        average_attack = round(sum(attack_values) / len(battles), 2)
        average_block = round(sum(block_values) / len(battles), 2)
        average_speed = round(sum(speed_values) / len(battles), 2)
        max_attack = max(attack_values)
        max_block = max(block_values)
        max_speed = max(speed_values)
    else:
        average_attack = 0.0
        average_block = 0.0
        average_speed = 0.0
        max_attack = 0
        max_block = 0
        max_speed = 0
    return DeckProfile(
        total_cards=len(cards),
        battle_count=len(battles),
        control_count=len(controls),
        average_attack=average_attack,
        average_block=average_block,
        average_speed=average_speed,
        max_attack=max_attack,
        max_block=max_block,
        max_speed=max_speed,
    )


def remaining_public_cards(
    public_ids: tuple[str, ...],
    spent_cards: list[Card] | tuple[Card, ...],
    cards_by_id: dict[str, Card],
    current_control: Card | None = None,
) -> list[Card]:
    counts = Counter(public_ids)
    for card in spent_cards:
        if counts[card.id] > 0:
            counts[card.id] -= 1
    if current_control is not None and counts[current_control.id] > 0:
        counts[current_control.id] -= 1
    remaining: list[Card] = []
    for card_id, count in counts.items():
        remaining.extend(cards_by_id[card_id] for _ in range(max(count, 0)))
    return remaining


def public_view_profile(view: PlayerView, cards_by_id: dict[str, Card], *, owner: str) -> DeckProfile:
    if owner == "self":
        return profile_card_ids(view.own_public_deck, cards_by_id)
    remaining = remaining_public_cards(
        view.opponent_public_deck,
        list(view.opponent_used) + list(view.opponent_discard),
        cards_by_id,
        current_control=view.opponent_control_card,
    )
    return profile_cards(remaining)

