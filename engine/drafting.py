from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import random

from engine.card import Card
from engine.card_pool import CardPoolDefinition, DraftPick, DraftResult, build_drafted_deck


ROLE_LABELS = {
    "red": "attack",
    "blue": "speed",
    "green": "defense",
    "white": "control",
}

RARITY_SCORES = {
    "common": 0.0,
    "uncommon": 1.5,
    "rare": 3.0,
}

TARGET_ROLE_COUNTS = {
    "red": 6,
    "blue": 3,
    "green": 3,
    "white": 8,
}

TARGET_TYPE_COUNTS = {
    "battle": 12,
    "control": 8,
}


@dataclass(frozen=True)
class DraftDeckSummary:
    total: int
    battle_count: int
    control_count: int
    role_counts: dict[str, int]
    rarity_counts: dict[str, int]


class BaseDraftBot:
    name = "BaseDraftBot"

    def choose_pick(
        self,
        available: dict[str, int],
        cards: dict[str, Card],
        own_cards: list[str],
        opponent_cards: list[str],
        rng: random.Random,
    ) -> str:
        return next(iter(sorted(available)))


class RandomDraftBot(BaseDraftBot):
    name = "RandomDraftBot"

    def choose_pick(
        self,
        available: dict[str, int],
        cards: dict[str, Card],
        own_cards: list[str],
        opponent_cards: list[str],
        rng: random.Random,
    ) -> str:
        weighted = [card_id for card_id, count in available.items() for _ in range(count)]
        return rng.choice(weighted)


class RoleBalanceDraftBot(BaseDraftBot):
    name = "RoleBalanceDraftBot"

    def choose_pick(
        self,
        available: dict[str, int],
        cards: dict[str, Card],
        own_cards: list[str],
        opponent_cards: list[str],
        rng: random.Random,
    ) -> str:
        own_summary = summarize_deck(own_cards, cards)
        remaining_picks = 20 - len(own_cards)
        best_score: float | None = None
        best_ids: list[str] = []

        for card_id in sorted(available):
            score = self._score_candidate(cards[card_id], own_summary, own_cards, remaining_picks)
            if best_score is None or score > best_score:
                best_score = score
                best_ids = [card_id]
            elif score == best_score:
                best_ids.append(card_id)

        return rng.choice(best_ids)

    def _score_candidate(
        self,
        card: Card,
        own_summary: DraftDeckSummary,
        own_cards: list[str],
        remaining_picks: int,
    ) -> float:
        role = infer_role_color(card)
        duplicate_count = own_cards.count(card.id)
        type_count = own_summary.battle_count if card.type == "battle" else own_summary.control_count
        target_type = TARGET_TYPE_COUNTS[card.type]
        role_count = own_summary.role_counts[role]
        target_role = TARGET_ROLE_COUNTS[role]

        score = base_card_score(card)
        score += need_bonus(type_count, target_type, remaining_picks, weight=1.8)
        score += need_bonus(role_count, target_role, remaining_picks, weight=1.4)
        score -= duplicate_count * 1.2

        if card.type == "battle":
            if role == "red":
                score += max(card.attack, 0) * 0.35
            elif role == "blue":
                score += max(card.speed, 0) * 0.25
            elif role == "green":
                score += max(card.block, 0) * 0.3
        else:
            score += 0.5 + len(card.effects) * 0.4

        if card.rarity == "rare" and role_count >= target_role:
            score -= 0.6
        return round(score, 4)


def draft_with_bots(
    pool: CardPoolDefinition,
    cards: dict[str, Card],
    rng: random.Random,
    bot1: BaseDraftBot,
    bot2: BaseDraftBot,
    *,
    deck_size: int = 20,
    first_player: str | None = None,
    all_public: bool = True,
    deck1_id: str = "draft_p1",
    deck2_id: str = "draft_p2",
    deck1_name: str = "Draft Deck P1",
    deck2_name: str = "Draft Deck P2",
) -> DraftResult:
    if pool.total_cards < deck_size * 2:
        raise ValueError("card pool does not contain enough cards for both drafted decks")

    available = Counter({entry.card_id: entry.count for entry in pool.entries})
    drafted: dict[str, list[str]] = {"p1": [], "p2": []}
    picks: list[DraftPick] = []
    first = first_player or rng.choice(("p1", "p2"))
    bots = {"p1": bot1, "p2": bot2}

    for pick_number in range(1, deck_size * 2 + 1):
        player_id = first if pick_number % 2 == 1 else ("p2" if first == "p1" else "p1")
        opponent_id = "p2" if player_id == "p1" else "p1"
        card_id = bots[player_id].choose_pick(dict(available), cards, drafted[player_id], drafted[opponent_id], rng)
        if card_id not in available:
            card_id = sorted(available)[0]
        drafted[player_id].append(card_id)
        available[card_id] -= 1
        if available[card_id] == 0:
            del available[card_id]
        picks.append(DraftPick(number=pick_number, player_id=player_id, card_id=card_id))

    return DraftResult(
        pool=pool,
        deck1=build_drafted_deck(deck1_id, deck1_name, drafted["p1"], all_public=all_public),
        deck2=build_drafted_deck(deck2_id, deck2_name, drafted["p2"], all_public=all_public),
        picks=tuple(picks),
        first_player=first,
    )


def summarize_deck(card_ids: list[str] | tuple[str, ...], cards: dict[str, Card]) -> DraftDeckSummary:
    role_counts = Counter({role: 0 for role in ROLE_LABELS})
    rarity_counts = Counter()
    battle_count = 0
    control_count = 0
    for card_id in card_ids:
        card = cards[card_id]
        role_counts[infer_role_color(card)] += 1
        rarity_counts[card.rarity] += 1
        if card.type == "battle":
            battle_count += 1
        else:
            control_count += 1
    return DraftDeckSummary(
        total=len(card_ids),
        battle_count=battle_count,
        control_count=control_count,
        role_counts={role: role_counts[role] for role in ROLE_LABELS},
        rarity_counts={rarity: rarity_counts[rarity] for rarity in ("common", "uncommon", "rare")},
    )


def infer_role_color(card: Card) -> str:
    if card.type == "control":
        return "white"
    if "speed" in card.tags or "trick" in card.tags or card.speed >= 4:
        return "blue"
    if "defense" in card.tags or card.block >= 3:
        return "green"
    return "red"


def base_card_score(card: Card) -> float:
    score = RARITY_SCORES.get(card.rarity, 0.0)
    score += max(card.attack, 0) * 1.0
    score += max(card.block, 0) * 0.9
    score += max(card.speed, 0) * 0.7
    score -= max(-card.attack, 0) * 0.5
    score -= max(-card.block, 0) * 0.3
    score -= max(-card.speed, 0) * 0.2
    score += len(card.effects) * 0.5
    return score


def need_bonus(current: int, target: int, remaining_picks: int, *, weight: float) -> float:
    deficit = target - current
    if deficit <= 0:
        return -0.3 * max(current - target, 0)
    urgency = 1.0
    if remaining_picks <= deficit:
        urgency = 1.8
    elif remaining_picks <= deficit + 2:
        urgency = 1.4
    return deficit * weight * urgency / max(remaining_picks, 1)
