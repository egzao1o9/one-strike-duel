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
    "blessing": 2,
}

NORMAL_PUBLIC_PACKS = 3
HIDDEN_PACK_OPTIONS = 3
PUBLIC_RARE_OFFER_SIZE = 5
NORMAL_HALF_TARGET_CARDS = 8
RARE_HALF_TARGET_CARDS = 2
FINAL_NORMAL_CARDS = 16
FINAL_RARE_CARDS = 4


@dataclass(frozen=True)
class DraftDeckSummary:
    total: int
    battle_count: int
    control_count: int
    blessing_count: int
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

    def choose_hidden_pack(
        self,
        offer_packs: tuple[tuple[str, ...], ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
        *,
        phase: str,
        half: int,
    ) -> int:
        return 0

    def choose_public_pack(
        self,
        offer_packs: tuple[tuple[str, ...], ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
        *,
        phase: str,
        half: int,
        pick_position: int,
    ) -> int:
        return 0

    def choose_hidden_rare(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
        *,
        half: int,
    ) -> str:
        return sorted(offer)[0]

    def choose_public_rare(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
        *,
        half: int,
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

    def choose_hidden_pack(
        self,
        offer_packs: tuple[tuple[str, ...], ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
        *,
        phase: str,
        half: int,
    ) -> int:
        return rng.randrange(len(offer_packs))

    def choose_public_pack(
        self,
        offer_packs: tuple[tuple[str, ...], ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
        *,
        phase: str,
        half: int,
        pick_position: int,
    ) -> int:
        return rng.randrange(len(offer_packs))

    def choose_hidden_rare(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
        *,
        half: int,
    ) -> str:
        return rng.choice(offer)

    def choose_public_rare(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
        *,
        half: int,
        pick_position: int,
    ) -> str:
        return rng.choice(offer)


class RoleBalanceDraftBot(BaseDraftBot):
    name = "RoleBalanceDraftBot"

    def __init__(self, seed: int | None = None) -> None:
        self.rng = random.Random(seed)

    def choose_hidden_pack(
        self,
        offer_packs: tuple[tuple[str, ...], ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
        *,
        phase: str,
        half: int,
    ) -> int:
        return self._choose_best_pack(offer_packs, cards, own_hidden_cards, own_public_cards, opponent_public_cards, visibility="hidden")

    def choose_hidden_pick(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
    ) -> str:
        return self._choose_best_rare(offer, cards, own_hidden_cards, own_public_cards, opponent_public_cards, visibility="hidden")

    def choose_public_pack(
        self,
        offer_packs: tuple[tuple[str, ...], ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
        *,
        phase: str,
        half: int,
        pick_position: int,
    ) -> int:
        return self._choose_best_pack(offer_packs, cards, own_hidden_cards, own_public_cards, opponent_public_cards, visibility="public")

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
        return self._choose_best_rare(offer, cards, own_hidden_cards, own_public_cards, opponent_public_cards, visibility="public")

    def choose_hidden_rare(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
        *,
        half: int,
    ) -> str:
        return self._choose_best_rare(offer, cards, own_hidden_cards, own_public_cards, opponent_public_cards, visibility="hidden")

    def choose_public_rare(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
        *,
        half: int,
        pick_position: int,
    ) -> str:
        return self._choose_best_rare(offer, cards, own_hidden_cards, own_public_cards, opponent_public_cards, visibility="public")

    def _choose_best_pack(
        self,
        offer_packs: tuple[tuple[str, ...], ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        *,
        visibility: str,
    ) -> int:
        best_score: float | None = None
        best_indexes: list[int] = []
        for index, pack in enumerate(offer_packs):
            score = self._score_bundle(pack, cards, own_hidden_cards, own_public_cards, opponent_public_cards, visibility=visibility)
            if best_score is None or score > best_score:
                best_score = score
                best_indexes = [index]
            elif score == best_score:
                best_indexes.append(index)
        return min(best_indexes)

    def _choose_best_rare(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        *,
        visibility: str,
    ) -> str:
        best_score: float | None = None
        best_ids: list[str] = []
        for card_id in offer:
            score = self._score_bundle((card_id,), cards, own_hidden_cards, own_public_cards, opponent_public_cards, visibility=visibility)
            if best_score is None or score > best_score:
                best_score = score
                best_ids = [card_id]
            elif score == best_score:
                best_ids.append(card_id)
        return sorted(best_ids)[0]

    def _score_bundle(
        self,
        bundle: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        *,
        visibility: str,
    ) -> float:
        own_cards = own_hidden_cards + own_public_cards
        own_summary = summarize_deck(own_cards, cards)
        remaining_picks = 20 - len(own_cards)
        bundle_cards = [cards[card_id] for card_id in bundle]
        score = 0.0
        for card in bundle_cards:
            score += self._score_candidate(card, own_summary, own_cards, remaining_picks, visibility=visibility)
        result_cards = own_cards + list(bundle)
        result_summary = summarize_deck(result_cards, cards)
        score += self._summary_balance_bonus(result_summary)
        if visibility == "hidden":
            score += sum(0.25 for card in bundle_cards if card.rarity == "rare" or card.attack >= 4)
        else:
            score -= sum(0.12 for card in bundle_cards if card.attack >= 4 and card.block <= 0)
        return round(score, 4)

    def _summary_balance_bonus(self, summary: DraftDeckSummary) -> float:
        score = 0.0
        for rarity, target in (("common", 8), ("uncommon", 8), ("rare", 4)):
            diff = abs(summary.rarity_counts[rarity] - target)
            score -= diff * 0.16
        return score

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
            if card.type == "blessing":
                score += 0.25
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

    def choose_hidden_pack(
        self,
        offer_packs: tuple[tuple[str, ...], ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
        *,
        phase: str,
        half: int,
        ) -> int:
        return self._choose_best_pack(
            offer_packs,
            cards,
            own_hidden_cards,
            own_public_cards,
            opponent_public_cards,
            visibility="hidden",
            pick_position=1,
        )

    def choose_hidden_pick(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
    ) -> str:
        return self._choose_best_rare(
            offer,
            cards,
            own_hidden_cards,
            own_public_cards,
            opponent_public_cards,
            visibility="hidden",
            pick_position=1,
        )

    def choose_public_pack(
        self,
        offer_packs: tuple[tuple[str, ...], ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
        *,
        phase: str,
        half: int,
        pick_position: int,
        ) -> int:
        return self._choose_best_pack(
            offer_packs,
            cards,
            own_hidden_cards,
            own_public_cards,
            opponent_public_cards,
            visibility="public",
            pick_position=pick_position,
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
        return self._choose_best_rare(
            offer,
            cards,
            own_hidden_cards,
            own_public_cards,
            opponent_public_cards,
            visibility="public",
            pick_position=pick_position,
        )

    def choose_hidden_rare(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
        *,
        half: int,
    ) -> str:
        return self._choose_best_rare(
            offer,
            cards,
            own_hidden_cards,
            own_public_cards,
            opponent_public_cards,
            visibility="hidden",
            pick_position=1,
        )

    def choose_public_rare(
        self,
        offer: tuple[str, ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
        *,
        half: int,
        pick_position: int,
    ) -> str:
        return self._choose_best_rare(
            offer,
            cards,
            own_hidden_cards,
            own_public_cards,
            opponent_public_cards,
            visibility="public",
            pick_position=pick_position,
        )

    def _choose_best_pack(
        self,
        offer_packs: tuple[tuple[str, ...], ...],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        *,
        visibility: str,
        pick_position: int,
    ) -> int:
        scored: list[tuple[float, int]] = []
        for index, pack in enumerate(offer_packs):
            score = self._score_bundle(
                pack,
                cards,
                offer_packs,
                own_hidden_cards,
                own_public_cards,
                opponent_public_cards,
                visibility=visibility,
                pick_position=pick_position,
            )
            score += self.rng.uniform(-self.style.noise, self.style.noise)
            scored.append((score, index))
        scored.sort(key=lambda item: (item[0], -item[1]), reverse=True)
        return scored[0][1]

    def _choose_best_rare(
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
        offer_packs = tuple((card_id,) for card_id in offer)
        for card_id in offer:
            score = self._score_bundle(
                (card_id,),
                cards,
                offer_packs,
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

    def _score_bundle(
        self,
        bundle: tuple[str, ...],
        cards: dict[str, Card],
        offer_packs: tuple[tuple[str, ...], ...],
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
        offer_flat = tuple(card_id for pack in offer_packs for card_id in pack)

        score = 0.0
        for card_id in bundle:
            card = cards[card_id]
            role = infer_role_color(card)
            score += base_card_score(card)
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
                score += self._denial_value(card, offer_flat, cards, opponent_public_cards)
        score += self._bundle_balance_value(bundle, cards, own_all)
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
        if card.type in {"control", "blessing"}:
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

    def _bundle_balance_value(self, bundle: tuple[str, ...], cards: dict[str, Card], own_all: list[str]) -> float:
        summary = summarize_deck(own_all + list(bundle), cards)
        score = 0.0
        score -= abs(summary.rarity_counts["common"] - 8) * 0.08
        score -= abs(summary.rarity_counts["uncommon"] - 8) * 0.08
        score -= abs(summary.rarity_counts["rare"] - 4) * 0.14
        return score


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
    draft_mode: str = "full",
) -> DraftResult:
    if draft_mode == "simple":
        return _draft_with_simple_bots(
            pool,
            cards,
            rng,
            bot1,
            bot2,
            deck_size=deck_size,
            first_player=first_player,
            deck1_id=deck1_id,
            deck2_id=deck2_id,
            deck1_name=deck1_name,
            deck2_name=deck2_name,
        )
    if draft_mode != "full":
        raise ValueError(f"unsupported draft_mode: {draft_mode}")
    if deck_size != 20:
        raise ValueError("new draft flow requires deck_size=20")
    if pool.total_cards < deck_size * 2:
        raise ValueError("card pool does not contain enough cards for both drafted decks")

    available = Counter({entry.card_id: entry.count for entry in pool.entries})
    first = first_player or rng.choice(("p1", "p2"))
    second = _opponent_of(first)
    bots = {"p1": bot1, "p2": bot2}
    drafted: dict[str, dict[str, list[str]]] = {
        "p1": {"public_normal": [], "hidden_normal": [], "public_rare": [], "hidden_rare": []},
        "p2": {"public_normal": [], "hidden_normal": [], "public_rare": [], "hidden_rare": []},
    }
    picks: list[DraftPick] = []
    pick_number = 1

    pick_number = _run_normal_half(
        available,
        cards,
        rng,
        bots,
        drafted,
        leader=first,
        round_number=1,
        pick_number=pick_number,
        picks=picks,
    )
    pick_number = _run_rare_half(
        available,
        cards,
        rng,
        bots,
        drafted,
        leader=first,
        round_number=2,
        pick_number=pick_number,
        picks=picks,
    )
    pick_number = _run_normal_half(
        available,
        cards,
        rng,
        bots,
        drafted,
        leader=second,
        round_number=3,
        pick_number=pick_number,
        picks=picks,
    )
    _run_rare_half(
        available,
        cards,
        rng,
        bots,
        drafted,
        leader=second,
        round_number=4,
        pick_number=pick_number,
        picks=picks,
    )

    _validate_final_composition(drafted, cards)

    deck1 = _build_draft_deck(deck1_id, deck1_name, drafted["p1"], picks, draft_mode="full")
    deck2 = _build_draft_deck(deck2_id, deck2_name, drafted["p2"], picks, draft_mode="full")
    return DraftResult(
        pool=pool,
        deck1=deck1,
        deck2=deck2,
        picks=tuple(picks),
        first_player=first,
    )


def _draft_with_simple_bots(
    pool: CardPoolDefinition,
    cards: dict[str, Card],
    rng: random.Random,
    bot1: BaseDraftBot,
    bot2: BaseDraftBot,
    *,
    deck_size: int,
    first_player: str | None,
    deck1_id: str,
    deck2_id: str,
    deck1_name: str,
    deck2_name: str,
) -> DraftResult:
    if deck_size != 20:
        raise ValueError("simple draft flow requires deck_size=20")
    available = Counter({entry.card_id: entry.count for entry in pool.entries})
    first = first_player or rng.choice(("p1", "p2"))
    hidden_player = first
    bots = {"p1": bot1, "p2": bot2}
    drafted_public: dict[str, list[str]] = {"p1": [], "p2": []}
    drafted_hidden: dict[str, list[str]] = {"p1": [], "p2": []}
    picks: list[DraftPick] = []
    pick_number = 1
    round_number = 1

    while _simple_deck_count(drafted_public, drafted_hidden, "p1") < deck_size or _simple_deck_count(drafted_public, drafted_hidden, "p2") < deck_size:
        if _simple_deck_count(drafted_public, drafted_hidden, hidden_player) < deck_size:
            hidden_offer = _sample_simple_hidden_offer(
                available,
                cards,
                _remaining_rarity_need(drafted_public[hidden_player] + drafted_hidden[hidden_player], cards),
                rng,
            )
            hidden_choice = bots[hidden_player].choose_hidden_pick(
                hidden_offer,
                cards,
                drafted_hidden[hidden_player],
                drafted_public[hidden_player],
                drafted_public[_opponent_of(hidden_player)],
                rng,
            )
            hidden_choice = _sanitize_simple_pick(
                hidden_offer,
                hidden_choice,
                cards,
                _remaining_rarity_need(drafted_public[hidden_player] + drafted_hidden[hidden_player], cards),
            )
            drafted_hidden[hidden_player].append(hidden_choice)
            _consume_card(available, hidden_choice)
            picks.append(
                DraftPick(
                    number=pick_number,
                    player_id=hidden_player,
                    card_id=hidden_choice,
                    visibility="hidden",
                    phase="simple_hidden",
                    offer_card_ids=hidden_offer,
                    selected_card_ids=(hidden_choice,),
                    pick_position=1,
                    round_number=round_number,
                )
            )
            pick_number += 1

        public_offer = list(
            _sample_simple_public_offer(
                available,
                cards,
                _remaining_rarity_need(drafted_public["p1"] + drafted_hidden["p1"], cards),
                _remaining_rarity_need(drafted_public["p2"] + drafted_hidden["p2"], cards),
                rng,
            )
        )
        public_order = (_opponent_of(hidden_player), hidden_player)
        for pick_position, player_id in enumerate(public_order, start=1):
            if _simple_deck_count(drafted_public, drafted_hidden, player_id) >= deck_size or not public_offer:
                continue
            need = _remaining_rarity_need(drafted_public[player_id] + drafted_hidden[player_id], cards)
            visible_offer = tuple(card_id for card_id in public_offer if need[cards[card_id].rarity] > 0)
            if not visible_offer:
                topup = _sample_simple_offer(available, cards, need, 3, rng)
                public_offer.extend(card_id for card_id in topup if card_id not in public_offer or public_offer.count(card_id) < available.get(card_id, 0))
                visible_offer = tuple(card_id for card_id in public_offer if need[cards[card_id].rarity] > 0) or tuple(public_offer)
            choice = bots[player_id].choose_public_pick(
                visible_offer,
                cards,
                drafted_hidden[player_id],
                drafted_public[player_id],
                drafted_public[_opponent_of(player_id)],
                rng,
                pick_position=pick_position,
            )
            choice = _sanitize_simple_pick(visible_offer, choice, cards, need)
            drafted_public[player_id].append(choice)
            public_offer.remove(choice)
            _consume_card(available, choice)
            picks.append(
                DraftPick(
                    number=pick_number,
                    player_id=player_id,
                    card_id=choice,
                    visibility="public",
                    phase="simple_public",
                    offer_card_ids=visible_offer,
                    selected_card_ids=(choice,),
                    pick_position=pick_position,
                    round_number=round_number,
                )
            )
            pick_number += 1

        hidden_player = _opponent_of(hidden_player)
        round_number += 1

    _validate_simple_final_composition(drafted_public, drafted_hidden, cards)
    deck1 = _build_simple_draft_deck(deck1_id, deck1_name, drafted_public["p1"], drafted_hidden["p1"], picks, cards)
    deck2 = _build_simple_draft_deck(deck2_id, deck2_name, drafted_public["p2"], drafted_hidden["p2"], picks, cards)
    return DraftResult(
        pool=pool,
        deck1=deck1,
        deck2=deck2,
        picks=tuple(picks),
        first_player=first,
    )


def summarize_deck(card_ids: list[str] | tuple[str, ...], cards: dict[str, Card]) -> DraftDeckSummary:
    role_counts = Counter({role: 0 for role in ROLE_LABELS})
    rarity_counts = Counter()
    battle_count = 0
    control_count = 0
    blessing_count = 0
    for card_id in card_ids:
        card = cards[card_id]
        role_counts[infer_role_color(card)] += 1
        rarity_counts[card.rarity] += 1
        if card.type == "battle":
            battle_count += 1
        elif card.type == "blessing":
            blessing_count += 1
        else:
            control_count += 1
    return DraftDeckSummary(
        total=len(card_ids),
        battle_count=battle_count,
        control_count=control_count,
        blessing_count=blessing_count,
        role_counts={role: role_counts[role] for role in ROLE_LABELS},
        rarity_counts={rarity: rarity_counts[rarity] for rarity in ("common", "uncommon", "rare")},
    )


def infer_role_color(card: Card) -> str:
    if card.type == "control":
        return "white"
    if card.type == "blessing":
        if "speed" in card.tags or "trick" in card.tags or card.speed >= 4:
            return "blue"
        if "defense" in card.tags or card.block >= 3:
            return "green"
        if "draw" in card.tags or "support" in card.tags:
            return "white"
        return "red"
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


def _run_normal_half(
    available: Counter[str],
    cards: dict[str, Card],
    rng: random.Random,
    bots: dict[str, BaseDraftBot],
    drafted: dict[str, dict[str, list[str]]],
    *,
    leader: str,
    round_number: int,
    pick_number: int,
    picks: list[DraftPick],
) -> int:
    follower = _opponent_of(leader)
    public_packs = [_draw_normal_pack(available, cards, rng) for _ in range(NORMAL_PUBLIC_PACKS)]

    pick_number = _public_pack_pick(
        available,
        cards,
        rng,
        bots[leader],
        drafted,
        player_id=leader,
        opponent_id=follower,
        public_packs=public_packs,
        round_number=round_number,
        pick_number=pick_number,
        picks=picks,
        pick_position=1,
    )
    pick_number = _hidden_pack_pick(
        available,
        cards,
        rng,
        bots[follower],
        drafted,
        player_id=follower,
        opponent_id=leader,
        round_number=round_number,
        pick_number=pick_number,
        picks=picks,
        phase="normal_hidden",
    )
    pick_number = _public_pack_pick(
        available,
        cards,
        rng,
        bots[follower],
        drafted,
        player_id=follower,
        opponent_id=leader,
        public_packs=public_packs,
        round_number=round_number,
        pick_number=pick_number,
        picks=picks,
        pick_position=2,
    )
    pick_number = _hidden_pack_pick(
        available,
        cards,
        rng,
        bots[leader],
        drafted,
        player_id=leader,
        opponent_id=follower,
        round_number=round_number,
        pick_number=pick_number,
        picks=picks,
        phase="normal_hidden",
    )

    for pack in public_packs:
        _return_cards(available, pack)
    return pick_number


def _run_rare_half(
    available: Counter[str],
    cards: dict[str, Card],
    rng: random.Random,
    bots: dict[str, BaseDraftBot],
    drafted: dict[str, dict[str, list[str]]],
    *,
    leader: str,
    round_number: int,
    pick_number: int,
    picks: list[DraftPick],
) -> int:
    follower = _opponent_of(leader)
    public_offer = list(_draw_cards_by_rarity(available, cards, "rare", PUBLIC_RARE_OFFER_SIZE, rng))

    pick_number = _public_rare_pick(
        cards,
        rng,
        bots[leader],
        drafted,
        player_id=leader,
        opponent_id=follower,
        public_offer=public_offer,
        round_number=round_number,
        pick_number=pick_number,
        picks=picks,
        pick_position=1,
    )
    pick_number = _hidden_rare_pick(
        available,
        cards,
        rng,
        bots[follower],
        drafted,
        player_id=follower,
        opponent_id=leader,
        round_number=round_number,
        pick_number=pick_number,
        picks=picks,
    )
    pick_number = _public_rare_pick(
        cards,
        rng,
        bots[follower],
        drafted,
        player_id=follower,
        opponent_id=leader,
        public_offer=public_offer,
        round_number=round_number,
        pick_number=pick_number,
        picks=picks,
        pick_position=2,
    )
    pick_number = _hidden_rare_pick(
        available,
        cards,
        rng,
        bots[leader],
        drafted,
        player_id=leader,
        opponent_id=follower,
        round_number=round_number,
        pick_number=pick_number,
        picks=picks,
    )

    _return_cards(available, public_offer)
    return pick_number


def _public_pack_pick(
    available: Counter[str],
    cards: dict[str, Card],
    rng: random.Random,
    bot: BaseDraftBot,
    drafted: dict[str, dict[str, list[str]]],
    *,
    player_id: str,
    opponent_id: str,
    public_packs: list[tuple[str, ...]],
    round_number: int,
    pick_number: int,
    picks: list[DraftPick],
    pick_position: int,
) -> int:
    offer_packs = tuple(public_packs)
    chosen_index = bot.choose_public_pack(
        offer_packs,
        cards,
        drafted[player_id]["hidden_normal"] + drafted[player_id]["hidden_rare"],
        drafted[player_id]["public_normal"] + drafted[player_id]["public_rare"],
        drafted[opponent_id]["public_normal"] + drafted[opponent_id]["public_rare"],
        rng,
        phase="normal_public",
        half=1 if round_number <= 2 else 2,
        pick_position=pick_position,
    )
    chosen_index = _sanitize_pack_index(offer_packs, chosen_index)
    chosen_pack = public_packs.pop(chosen_index)
    drafted[player_id]["public_normal"].extend(chosen_pack)
    picks.append(
        DraftPick(
            number=pick_number,
            player_id=player_id,
            card_id=chosen_pack[0],
            visibility="public",
            phase="normal_public",
            offer_card_ids=tuple(card_id for pack in offer_packs for card_id in pack),
            offer_groups=offer_packs,
            selected_card_ids=chosen_pack,
            pick_position=pick_position,
            round_number=round_number,
        )
    )
    public_packs.append(_draw_normal_pack(available, cards, rng))
    return pick_number + 1


def _hidden_pack_pick(
    available: Counter[str],
    cards: dict[str, Card],
    rng: random.Random,
    bot: BaseDraftBot,
    drafted: dict[str, dict[str, list[str]]],
    *,
    player_id: str,
    opponent_id: str,
    round_number: int,
    pick_number: int,
    picks: list[DraftPick],
    phase: str,
) -> int:
    offer_packs = tuple(_draw_normal_pack(available, cards, rng) for _ in range(HIDDEN_PACK_OPTIONS))
    chosen_index = bot.choose_hidden_pack(
        offer_packs,
        cards,
        drafted[player_id]["hidden_normal"] + drafted[player_id]["hidden_rare"],
        drafted[player_id]["public_normal"] + drafted[player_id]["public_rare"],
        drafted[opponent_id]["public_normal"] + drafted[opponent_id]["public_rare"],
        rng,
        phase=phase,
        half=1 if round_number <= 2 else 2,
    )
    chosen_index = _sanitize_pack_index(offer_packs, chosen_index)
    chosen_pack = offer_packs[chosen_index]
    drafted[player_id]["hidden_normal"].extend(chosen_pack)
    picks.append(
        DraftPick(
            number=pick_number,
            player_id=player_id,
            card_id=chosen_pack[0],
            visibility="hidden",
            phase=phase,
            offer_card_ids=tuple(card_id for pack in offer_packs for card_id in pack),
            offer_groups=offer_packs,
            selected_card_ids=chosen_pack,
            pick_position=1,
            round_number=round_number,
        )
    )
    for index, pack in enumerate(offer_packs):
        if index != chosen_index:
            _return_cards(available, pack)
    return pick_number + 1


def _public_rare_pick(
    cards: dict[str, Card],
    rng: random.Random,
    bot: BaseDraftBot,
    drafted: dict[str, dict[str, list[str]]],
    *,
    player_id: str,
    opponent_id: str,
    public_offer: list[str],
    round_number: int,
    pick_number: int,
    picks: list[DraftPick],
    pick_position: int,
) -> int:
    offer = tuple(public_offer)
    chosen_card_id = bot.choose_public_rare(
        offer,
        cards,
        drafted[player_id]["hidden_normal"] + drafted[player_id]["hidden_rare"],
        drafted[player_id]["public_normal"] + drafted[player_id]["public_rare"],
        drafted[opponent_id]["public_normal"] + drafted[opponent_id]["public_rare"],
        rng,
        half=1 if round_number <= 2 else 2,
        pick_position=pick_position,
    )
    chosen_card_id = _sanitize_card_pick(offer, chosen_card_id)
    public_offer.remove(chosen_card_id)
    drafted[player_id]["public_rare"].append(chosen_card_id)
    picks.append(
        DraftPick(
            number=pick_number,
            player_id=player_id,
            card_id=chosen_card_id,
            visibility="public",
            phase="rare_public",
            offer_card_ids=offer,
            offer_groups=tuple((card_id,) for card_id in offer),
            selected_card_ids=(chosen_card_id,),
            pick_position=pick_position,
            round_number=round_number,
        )
    )
    return pick_number + 1


def _hidden_rare_pick(
    available: Counter[str],
    cards: dict[str, Card],
    rng: random.Random,
    bot: BaseDraftBot,
    drafted: dict[str, dict[str, list[str]]],
    *,
    player_id: str,
    opponent_id: str,
    round_number: int,
    pick_number: int,
    picks: list[DraftPick],
) -> int:
    offer = _draw_cards_by_rarity(available, cards, "rare", 2, rng)
    chosen_card_id = bot.choose_hidden_rare(
        offer,
        cards,
        drafted[player_id]["hidden_normal"] + drafted[player_id]["hidden_rare"],
        drafted[player_id]["public_normal"] + drafted[player_id]["public_rare"],
        drafted[opponent_id]["public_normal"] + drafted[opponent_id]["public_rare"],
        rng,
        half=1 if round_number <= 2 else 2,
    )
    chosen_card_id = _sanitize_card_pick(offer, chosen_card_id)
    drafted[player_id]["hidden_rare"].append(chosen_card_id)
    picks.append(
        DraftPick(
            number=pick_number,
            player_id=player_id,
            card_id=chosen_card_id,
            visibility="hidden",
            phase="rare_hidden",
            offer_card_ids=offer,
            offer_groups=tuple((card_id,) for card_id in offer),
            selected_card_ids=(chosen_card_id,),
            pick_position=1,
            round_number=round_number,
        )
    )
    for card_id in offer:
        if card_id != chosen_card_id:
            _return_cards(available, (card_id,))
    return pick_number + 1


def _build_draft_deck(deck_id: str, name: str, drafted: dict[str, list[str]], picks: list[DraftPick], *, draft_mode: str) -> DeckDefinition:
    public_cards = tuple(drafted["public_normal"] + drafted["public_rare"])
    hidden_cards = tuple(drafted["hidden_normal"] + drafted["hidden_rare"])
    metadata = {
        "public_normal_cards": list(drafted["public_normal"]),
        "hidden_normal_cards": list(drafted["hidden_normal"]),
        "public_rare_cards": list(drafted["public_rare"]),
        "hidden_rare_cards": list(drafted["hidden_rare"]),
        "final_rarity_counts": {
            "common": 8,
            "uncommon": 8,
            "rare": 4,
        },
        "draft_mode": draft_mode,
        "public_draft_events": _build_public_draft_events(picks),
    }
    return DeckDefinition(
        id=deck_id,
        name=name,
        public_cards=public_cards,
        hidden_cards=hidden_cards,
        metadata=metadata,
    )


def _build_simple_draft_deck(
    deck_id: str,
    name: str,
    public_cards_list: list[str],
    hidden_cards_list: list[str],
    picks: list[DraftPick],
    cards: dict[str, Card],
) -> DeckDefinition:
    public_normal_cards = [card_id for card_id in public_cards_list if cards[card_id].rarity != "rare"]
    hidden_normal_cards = [card_id for card_id in hidden_cards_list if cards[card_id].rarity != "rare"]
    public_rare_cards = [card_id for card_id in public_cards_list if cards[card_id].rarity == "rare"]
    hidden_rare_cards = [card_id for card_id in hidden_cards_list if cards[card_id].rarity == "rare"]
    metadata = {
        "public_normal_cards": public_normal_cards,
        "hidden_normal_cards": hidden_normal_cards,
        "public_rare_cards": public_rare_cards,
        "hidden_rare_cards": hidden_rare_cards,
        "final_rarity_counts": {
            "common": 8,
            "uncommon": 8,
            "rare": 4,
        },
        "draft_mode": "simple",
        "public_draft_events": _build_public_draft_events(picks),
    }
    return DeckDefinition(
        id=deck_id,
        name=name,
        public_cards=tuple(public_cards_list),
        hidden_cards=tuple(hidden_cards_list),
        metadata=metadata,
    )


def _remaining_rarity_need(card_ids: list[str], cards: dict[str, Card]) -> dict[str, int]:
    counts = Counter(cards[card_id].rarity for card_id in card_ids)
    return {
        "common": max(0, 8 - counts["common"]),
        "uncommon": max(0, 8 - counts["uncommon"]),
        "rare": max(0, 4 - counts["rare"]),
    }


def _sample_simple_hidden_offer(
    available: Counter[str],
    cards: dict[str, Card],
    need: dict[str, int],
    rng: random.Random,
) -> tuple[str, ...]:
    return _sample_simple_offer(available, cards, need, 3, rng)


def _sample_simple_public_offer(
    available: Counter[str],
    cards: dict[str, Card],
    need_left: dict[str, int],
    need_right: dict[str, int],
    rng: random.Random,
) -> tuple[str, ...]:
    combined_need = {
        rarity: need_left[rarity] + need_right[rarity]
        for rarity in ("common", "uncommon", "rare")
    }
    return _sample_simple_offer(available, cards, combined_need, 5, rng)


def _sample_simple_offer(
    available: Counter[str],
    cards: dict[str, Card],
    need: dict[str, int],
    offer_size: int,
    rng: random.Random,
) -> tuple[str, ...]:
    weighted_ids = [
        card_id
        for card_id, count in available.items()
        for _ in range(count)
        if need.get(cards[card_id].rarity, 0) > 0
    ]
    if not weighted_ids:
        weighted_ids = [card_id for card_id, count in available.items() for _ in range(count)]
    sample_size = min(offer_size, len(weighted_ids))
    return tuple(rng.sample(weighted_ids, sample_size))


def _sanitize_simple_pick(
    offer: tuple[str, ...],
    choice: str,
    cards: dict[str, Card],
    need: dict[str, int],
) -> str:
    legal_offer = tuple(card_id for card_id in offer if need.get(cards[card_id].rarity, 0) > 0)
    if choice in legal_offer:
        return choice
    if legal_offer:
        return sorted(legal_offer)[0]
    return _sanitize_card_pick(offer, choice)


def _simple_deck_count(drafted_public: dict[str, list[str]], drafted_hidden: dict[str, list[str]], player_id: str) -> int:
    return len(drafted_public[player_id]) + len(drafted_hidden[player_id])


def _build_public_draft_events(picks: list[DraftPick]) -> list[dict[str, object]]:
    events: list[dict[str, object]] = []
    for pick in picks:
        if pick.visibility != "public":
            continue
        flattened_offer = list(pick.offer_card_ids)
        for selected_card_id in pick.selected_card_ids or ((pick.card_id,) if pick.card_id else tuple()):
            events.append(
                {
                    "round_number": pick.round_number,
                    "player_id": pick.player_id,
                    "pick_position": pick.pick_position,
                    "phase": pick.phase,
                    "offer_card_ids": flattened_offer,
                    "picked_card_id": selected_card_id,
                }
            )
    return events


def _draw_normal_pack(available: Counter[str], cards: dict[str, Card], rng: random.Random) -> tuple[str, ...]:
    commons = list(_draw_cards_by_rarity(available, cards, "common", 2, rng))
    uncommons = list(_draw_cards_by_rarity(available, cards, "uncommon", 2, rng))
    pack = commons + uncommons
    rng.shuffle(pack)
    return tuple(pack)


def _draw_cards_by_rarity(
    available: Counter[str],
    cards: dict[str, Card],
    rarity: str,
    count: int,
    rng: random.Random,
) -> tuple[str, ...]:
    weighted_ids = [
        card_id
        for card_id, copies in available.items()
        for _ in range(copies)
        if cards[card_id].rarity == rarity
    ]
    if len(weighted_ids) < count:
        raise ValueError(f"not enough {rarity} cards available for draft step")
    sampled = rng.sample(weighted_ids, count)
    for card_id in sampled:
        _consume_card(available, card_id)
    return tuple(sampled)


def _return_cards(available: Counter[str], card_ids: list[str] | tuple[str, ...]) -> None:
    for card_id in card_ids:
        available[card_id] += 1


def _consume_card(available: Counter[str], card_id: str) -> None:
    available[card_id] -= 1
    if available[card_id] <= 0:
        del available[card_id]


def _sanitize_pack_index(offer_packs: tuple[tuple[str, ...], ...], choice: int) -> int:
    if 0 <= choice < len(offer_packs):
        return choice
    return 0


def _sanitize_card_pick(offer: tuple[str, ...], choice: str) -> str:
    if choice in offer:
        return choice
    return sorted(offer)[0]


def _opponent_of(player_id: str) -> str:
    return "p2" if player_id == "p1" else "p1"


def _validate_final_composition(drafted: dict[str, dict[str, list[str]]], cards: dict[str, Card]) -> None:
    for player_id in ("p1", "p2"):
        public_normal = drafted[player_id]["public_normal"]
        hidden_normal = drafted[player_id]["hidden_normal"]
        public_rare = drafted[player_id]["public_rare"]
        hidden_rare = drafted[player_id]["hidden_rare"]
        if len(public_normal) != 8 or len(hidden_normal) != 8:
            raise ValueError(f"{player_id}: invalid normal draft count")
        if len(public_rare) != 2 or len(hidden_rare) != 2:
            raise ValueError(f"{player_id}: invalid rare draft count")
        summary = summarize_deck(public_normal + hidden_normal + public_rare + hidden_rare, cards)
        if summary.total != 20:
            raise ValueError(f"{player_id}: invalid final deck size")
        if summary.rarity_counts["common"] != 8 or summary.rarity_counts["uncommon"] != 8 or summary.rarity_counts["rare"] != 4:
            raise ValueError(f"{player_id}: invalid rarity composition")


def _validate_simple_final_composition(
    drafted_public: dict[str, list[str]],
    drafted_hidden: dict[str, list[str]],
    cards: dict[str, Card],
) -> None:
    for player_id in ("p1", "p2"):
        summary = summarize_deck(drafted_public[player_id] + drafted_hidden[player_id], cards)
        if summary.total != 20:
            raise ValueError(f"{player_id}: invalid final deck size")
        if summary.rarity_counts["common"] != 8 or summary.rarity_counts["uncommon"] != 8 or summary.rarity_counts["rare"] != 4:
            raise ValueError(f"{player_id}: invalid rarity composition")
