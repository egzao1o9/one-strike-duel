from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import random

from engine.analysis import profile_card_ids
from engine.card import Card
from engine.card_pool import CardPoolDefinition, DraftPick, DraftResult
from engine.deck import DeckDefinition


ROLE_LABELS = {
    "red": "attack",
    "blue": "speed",
    "green": "defense",
    "white": "control",
}

RARITY_SCORES = {
    "common": 0.0,
    "uncommon": 1.3,
    "rare": 2.5,
}

TARGET_ROLE_COUNTS = {
    "red": 6,
    "blue": 4,
    "green": 4,
    "white": 6,
}

TARGET_TYPE_COUNTS = {
    "battle": 13,
    "control": 7,
}


@dataclass(frozen=True)
class DraftDeckSummary:
    total: int
    battle_count: int
    control_count: int
    role_counts: dict[str, int]
    rarity_counts: dict[str, int]


@dataclass(frozen=True)
class DraftStyle:
    attack_weight: float
    block_weight: float
    speed_weight: float
    control_weight: float
    denial_weight: float
    hidden_finisher_bonus: float
    public_counter_bonus: float
    reveal_penalty: float
    noise: float


class BaseDraftBot:
    name = "BaseDraftBot"

    def choose_hidden_pick(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
    ) -> str:
        return sorted(offer)[0]

    def choose_public_pick(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
        *,
        pick_position: int,
    ) -> str:
        return sorted(offer)[0]


class RandomDraftBot(BaseDraftBot):
    name = "RandomDraftBot"

    def choose_hidden_pick(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
    ) -> str:
        return rng.choice(offer)

    def choose_public_pick(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
        *,
        pick_position: int,
    ) -> str:
        return rng.choice(offer)


class RoleBalanceDraftBot(BaseDraftBot):
    name = "RoleBalanceDraftBot"

    def __init__(self, seed: int | None = None) -> None:
        self.rng = random.Random(seed)

    def choose_hidden_pick(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
    ) -> str:
        return self._choose_best(offer, cards, own_hidden_cards, own_public_cards, opponent_public_cards, visibility="hidden")

    def choose_public_pick(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
        *,
        pick_position: int,
    ) -> str:
        return self._choose_best(offer, cards, own_hidden_cards, own_public_cards, opponent_public_cards, visibility="public")

    def _choose_best(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        *,
        visibility: str,
    ) -> str:
        own_cards = own_hidden_cards + own_public_cards
        own_summary = summarize_deck(own_cards, cards)
        remaining_picks = 20 - len(own_cards)
        best_score: float | None = None
        best_ids: list[str] = []
        for card_id in offer:
            score = self._score_candidate(
                cards[card_id],
                own_summary,
                own_cards,
                remaining_picks,
                visibility=visibility,
            )
            if best_score is None or score > best_score:
                best_score = score
                best_ids = [card_id]
            elif score == best_score:
                best_ids.append(card_id)
        return sorted(best_ids)[0]

    def _score_candidate(
        self,
        card: Card,
        own_summary: DraftDeckSummary,
        own_cards: list[str],
        remaining_picks: int,
        *,
        visibility: str,
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
        score -= duplicate_count * 1.0

        if card.type == "battle":
            score += max(card.attack, 0) * 0.3
            score += max(card.block, 0) * 0.25
            score += max(card.speed, 0) * 0.22
        else:
            score += 0.45 + len(card.effects) * 0.35
        if visibility == "hidden" and card.attack >= 4:
            score += 0.45
        if visibility == "public" and card.speed <= 0 and card.attack >= 4:
            score -= 0.25
        return round(score, 4)


class PublicInfoDraftBot(BaseDraftBot):
    name = "PublicInfoDraftBot"
    style = DraftStyle(
        attack_weight=1.0,
        block_weight=1.0,
        speed_weight=0.9,
        control_weight=1.0,
        denial_weight=0.7,
        hidden_finisher_bonus=0.9,
        public_counter_bonus=0.8,
        reveal_penalty=0.35,
        noise=0.18,
    )

    def __init__(self, seed: int) -> None:
        self.rng = random.Random(seed)

    def choose_hidden_pick(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
    ) -> str:
        return self._choose_best(
            offer,
            cards,
            own_hidden_cards,
            own_public_cards,
            opponent_public_cards,
            visibility="hidden",
            pick_position=1,
        )

    def choose_public_pick(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
        *,
        pick_position: int,
    ) -> str:
        return self._choose_best(
            offer,
            cards,
            own_hidden_cards,
            own_public_cards,
            opponent_public_cards,
            visibility="public",
            pick_position=pick_position,
        )

    def _choose_best(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        *,
        visibility: str,
        pick_position: int,
    ) -> str:
        scored: list[tuple[float, str]] = []
        for card_id in offer:
            score = self._score_candidate(
                cards[card_id],
                cards,
                offer,
                own_hidden_cards,
                own_public_cards,
                opponent_public_cards,
                visibility=visibility,
                pick_position=pick_position,
            )
            score += self.rng.uniform(-self.style.noise, self.style.noise)
            scored.append((score, card_id))
        scored.sort(key=lambda item: (item[0], item[1]), reverse=True)
        return scored[0][1]

    def _score_candidate(
        self,
        card: Card,
        cards: dict[str, Card],
        offer: tuple[str, ...],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        *,
        visibility: str,
        pick_position: int,
    ) -> float:
        own_all = own_hidden_cards + own_public_cards
        own_summary = summarize_deck(own_all, cards)
        remaining_picks = 20 - len(own_all)
        opponent_public_profile = profile_card_ids(opponent_public_cards, cards)
        role = infer_role_color(card)

        score = base_card_score(card)
        score += need_bonus(
            own_summary.battle_count if card.type == "battle" else own_summary.control_count,
            TARGET_TYPE_COUNTS[card.type],
            remaining_picks,
            weight=1.5,
        )
        score += need_bonus(
            own_summary.role_counts[role],
            TARGET_ROLE_COUNTS[role],
            remaining_picks,
            weight=1.0,
        )
        score -= own_all.count(card.id) * 0.8
        score += self._style_value(card)
        score += self._counter_value(card, opponent_public_profile)
        if visibility == "hidden":
            score += self._hidden_value(card)
        else:
            score += self._public_value(card, pick_position)
            score += self._denial_value(card, offer, cards, opponent_public_cards)
        return round(score, 4)

    def _style_value(self, card: Card) -> float:
        return (
            max(card.attack, 0) * self.style.attack_weight * 0.4
            + max(card.block, 0) * self.style.block_weight * 0.34
            + max(card.speed, 0) * self.style.speed_weight * 0.28
            + len(card.effects) * self.style.control_weight * 0.22
        )

    def _counter_value(self, card: Card, opponent_public_profile) -> float:
        score = 0.0
        if opponent_public_profile.battle_count == 0:
            return score
        if card.block >= opponent_public_profile.average_attack:
            score += self.style.public_counter_bonus * 0.5
        if card.speed >= opponent_public_profile.average_speed:
            score += self.style.public_counter_bonus * 0.4
        if card.attack > opponent_public_profile.average_block:
            score += self.style.public_counter_bonus * 0.45
        for effect in card.effects:
            if effect.kind == "modify_opponent_block":
                score += self.style.public_counter_bonus * 0.5
            elif effect.kind == "modify_opponent_speed":
                score += self.style.public_counter_bonus * 0.35
            elif effect.kind == "modify_self_block":
                score += self.style.public_counter_bonus * 0.25
        return score

    def _hidden_value(self, card: Card) -> float:
        score = 0.0
        if card.attack >= 4 or card.speed >= 3:
            score += self.style.hidden_finisher_bonus
        if any(effect.kind == "modify_opponent_block" for effect in card.effects):
            score += self.style.hidden_finisher_bonus * 0.4
        return score

    def _public_value(self, card: Card, pick_position: int) -> float:
        score = 0.0
        if card.type == "control":
            score += self.style.control_weight * 0.35
        if card.attack >= 4 and card.block <= 0:
            score -= self.style.reveal_penalty
        if pick_position == 1:
            score += 0.12
        return score

    def _denial_value(
        self,
        card: Card,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        opponent_public_cards: list[str],
    ) -> float:
        opponent_profile = profile_card_ids(opponent_public_cards, cards)
        danger = self._counter_value(card, opponent_profile)
        if len(offer) <= 1:
            return danger * self.style.denial_weight
        other_best = max(
            (self._counter_value(cards[candidate_id], opponent_profile) for candidate_id in offer if candidate_id != card.id),
            default=0.0,
        )
        return (danger - other_best * 0.4) * self.style.denial_weight


class StandardDraftBot(PublicInfoDraftBot):
    name = "StandardDraftBot"


class AggroDraftBot(PublicInfoDraftBot):
    name = "AggroDraftBot"
    style = DraftStyle(
        attack_weight=1.35,
        block_weight=0.7,
        speed_weight=1.1,
        control_weight=0.7,
        denial_weight=0.55,
        hidden_finisher_bonus=1.2,
        public_counter_bonus=0.55,
        reveal_penalty=0.2,
        noise=0.22,
    )


class GuardDraftBot(PublicInfoDraftBot):
    name = "GuardDraftBot"
    style = DraftStyle(
        attack_weight=0.8,
        block_weight=1.35,
        speed_weight=0.85,
        control_weight=1.15,
        denial_weight=0.85,
        hidden_finisher_bonus=0.45,
        public_counter_bonus=1.0,
        reveal_penalty=0.45,
        noise=0.16,
    )


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
    first = first_player or rng.choice(("p1", "p2"))
    hidden_player = first
    bots = {"p1": bot1, "p2": bot2}
    drafted_public: dict[str, list[str]] = {"p1": [], "p2": []}
    drafted_hidden: dict[str, list[str]] = {"p1": [], "p2": []}
    picks: list[DraftPick] = []
    pick_number = 1
    round_number = 1

    while len(drafted_public["p1"]) + len(drafted_hidden["p1"]) < deck_size or len(drafted_public["p2"]) + len(drafted_hidden["p2"]) < deck_size:
        if _deck_count(drafted_public, drafted_hidden, hidden_player) < deck_size:
            hidden_offer = _sample_offer(available, 3, rng)
            hidden_choice = bots[hidden_player].choose_hidden_pick(
                hidden_offer,
                cards,
                drafted_hidden[hidden_player],
                drafted_public[hidden_player],
                drafted_public[_opponent_of(hidden_player)],
                rng,
            )
            hidden_choice = _sanitize_pick(hidden_offer, hidden_choice)
            drafted_hidden[hidden_player].append(hidden_choice)
            _consume_card(available, hidden_choice)
            picks.append(
                DraftPick(
                    number=pick_number,
                    player_id=hidden_player,
                    card_id=hidden_choice,
                    visibility="hidden",
                    phase="hidden",
                    offer_card_ids=tuple(hidden_offer),
                    pick_position=1,
                    round_number=round_number,
                )
            )
            pick_number += 1

        public_offer = list(_sample_offer(available, 5, rng))
        public_order = (_opponent_of(hidden_player), hidden_player)
        for pick_position, player_id in enumerate(public_order, start=1):
            if _deck_count(drafted_public, drafted_hidden, player_id) >= deck_size or not public_offer:
                continue
            visible_offer = tuple(public_offer)
            choice = bots[player_id].choose_public_pick(
                visible_offer,
                cards,
                drafted_hidden[player_id],
                drafted_public[player_id],
                drafted_public[_opponent_of(player_id)],
                rng,
                pick_position=pick_position,
            )
            choice = _sanitize_pick(visible_offer, choice)
            drafted_public[player_id].append(choice)
            public_offer.remove(choice)
            _consume_card(available, choice)
            picks.append(
                DraftPick(
                    number=pick_number,
                    player_id=player_id,
                    card_id=choice,
                    visibility="public",
                    phase="public",
                    offer_card_ids=visible_offer,
                    pick_position=pick_position,
                    round_number=round_number,
                )
            )
            pick_number += 1

        hidden_player = _opponent_of(hidden_player)
        round_number += 1

    return DraftResult(
        pool=pool,
        deck1=DeckDefinition(
            id=deck1_id,
            name=deck1_name,
            public_cards=tuple(drafted_public["p1"]),
            hidden_cards=tuple(drafted_hidden["p1"]),
        ),
        deck2=DeckDefinition(
            id=deck2_id,
            name=deck2_name,
            public_cards=tuple(drafted_public["p2"]),
            hidden_cards=tuple(drafted_hidden["p2"]),
        ),
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
    score += max(card.block, 0) * 0.85
    score += max(card.speed, 0) * 0.72
    score -= max(-card.attack, 0) * 0.5
    score -= max(-card.block, 0) * 0.35
    score -= max(-card.speed, 0) * 0.25
    score += len(card.effects) * 0.45
    return score


def need_bonus(current: int, target: int, remaining_picks: int, *, weight: float) -> float:
    deficit = target - current
    if deficit <= 0:
        return -0.25 * max(current - target, 0)
    urgency = 1.0
    if remaining_picks <= deficit:
        urgency = 1.75
    elif remaining_picks <= deficit + 2:
        urgency = 1.35
    return deficit * weight * urgency / max(remaining_picks, 1)


def _sample_offer(available: Counter[str], offer_size: int, rng: random.Random) -> tuple[str, ...]:
    weighted_ids = [card_id for card_id, count in available.items() for _ in range(count)]
    sample_size = min(offer_size, len(weighted_ids))
    sampled = rng.sample(weighted_ids, sample_size)
    return tuple(sampled)


def _sanitize_pick(offer: tuple[str, ...], choice: str) -> str:
    if choice in offer:
        return choice
    return sorted(offer)[0]


def _consume_card(available: Counter[str], card_id: str) -> None:
    available[card_id] -= 1
    if available[card_id] <= 0:
        del available[card_id]


def _deck_count(drafted_public: dict[str, list[str]], drafted_hidden: dict[str, list[str]], player_id: str) -> int:
    return len(drafted_public[player_id]) + len(drafted_hidden[player_id])


def _opponent_of(player_id: str) -> str:
    return "p2" if player_id == "p1" else "p1"

