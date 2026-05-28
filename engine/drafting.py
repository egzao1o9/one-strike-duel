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
    "blessing": 1,
}

AGGRO_PRIORITY_CONTROL_IDS = {
    "control_haste",
    "control_momentum",
    "control_overclock",
    "control_all_in_focus",
    "control_pressure",
    "control_break_momentum",
    "control_parry_window",
}

BLESSING_HATE_CONTROL_IDS = {
    "control_blessing_flip",
    "control_blessing_break",
    "control_blessing_lock",
    "control_defile",
}

CONTROL_FOCUS_IDS = {
    "control_focus",
    "control_cover",
    "control_guard_read",
    "control_opening_read",
    "control_opening_expose",
    "control_peek_hand",
    "control_peek_opponent_top",
    "control_peek_own_top",
    "control_redraw_hand",
    "control_topdeck_hand",
    "control_hand_echo",
}

NORMAL_PUBLIC_PACKS = 3
HIDDEN_PACK_OPTIONS = 3
PUBLIC_RARE_OFFER_SIZE = 5
NORMAL_HALF_TARGET_CARDS = 8
RARE_HALF_TARGET_CARDS = 2
FINAL_NORMAL_CARDS = 16
FINAL_RARE_CARDS = 4
MARKET_DRAFT_MODE = "market_12"
STARTER_CARD_IDS = ("battle_attack", "battle_defend", "battle_step")
MARKET_VISIBLE_COUNT = 3
MARKET_SLOT_CAPS = {
    "common": 2,
    "uncommon": 5,
    "rare": 2,
}
MARKET_DECK_SIZE = 12
MARKET_DRAFTED_CARD_COUNT = 9
MARKET_FINAL_RARITY_COUNTS = {
    "common": 5,
    "uncommon": 5,
    "rare": 2,
}

FULL_DRAFT_PROFILES = {
    "full": {
        "deck_size": 20,
        "public_normal": 8,
        "hidden_normal": 8,
        "public_rare": 2,
        "hidden_rare": 2,
        "rarity_counts": {"common": 8, "uncommon": 8, "rare": 4},
        "rounds": ("normal_first", "rare_first", "normal_second", "rare_second"),
    },
    "full_half": {
        "deck_size": 10,
        "public_normal": 4,
        "hidden_normal": 4,
        "public_rare": 1,
        "hidden_rare": 1,
        "rarity_counts": {"common": 4, "uncommon": 4, "rare": 2},
        "rounds": ("normal_first", "rare_first"),
    },
    "full_12": {
        "deck_size": 12,
        "public_normal": 5,
        "hidden_normal": 5,
        "public_rare": 1,
        "hidden_rare": 1,
        "rarity_counts": {"common": 5, "uncommon": 5, "rare": 2},
        "rounds": ("normal_first", "rare_first", "normal_second", "rare_second"),
        "trim_after_full": True,
    },
    "full_15": {
        "deck_size": 15,
        "public_normal": 6,
        "hidden_normal": 6,
        "public_rare": 1,
        "hidden_rare": 2,
        "rarity_counts": {"common": 6, "uncommon": 6, "rare": 3},
        "rounds": ("normal_first", "rare_first", "normal_second", "rare_second"),
        "trim_after_full": True,
    },
    "full_18": {
        "deck_size": 18,
        "public_normal": 7,
        "hidden_normal": 7,
        "public_rare": 2,
        "hidden_rare": 2,
        "rarity_counts": {"common": 7, "uncommon": 7, "rare": 4},
        "rounds": ("normal_first", "rare_first", "normal_second", "rare_second"),
        "trim_after_full": True,
    },
}


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

    def choose_market_pick(
        self,
        *,
        visible_market: dict[str, tuple[str, ...]],
        topdeck_candidates: dict[str, tuple[str, ...]],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
    ) -> tuple[str, str]:
        return "visible", sorted(next(iter(visible_market.values())))[0]

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

    def choose_market_pick(
        self,
        *,
        visible_market: dict[str, tuple[str, ...]],
        topdeck_candidates: dict[str, tuple[str, ...]],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
    ) -> tuple[str, str]:
        visible_choices = [("visible", card_id) for offer in visible_market.values() for card_id in offer]
        topdeck_choices = [("topdeck", rarity) for rarity, offer in topdeck_candidates.items() if offer]
        return rng.choice(visible_choices + topdeck_choices)

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
            score += self._score_candidate(card, cards, own_summary, own_cards, remaining_picks, visibility=visibility)
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
        cards: dict[str, Card],
        own_summary: DraftDeckSummary,
        own_cards: list[str],
        remaining_picks: int,
        *,
        visibility: str,
    ) -> float:
        role = infer_role_color(card)
        duplicate_count = own_cards.count(card.id)
        if card.type == "battle":
            type_count = own_summary.battle_count
        elif card.type == "blessing":
            type_count = own_summary.blessing_count
        else:
            type_count = own_summary.control_count
        target_type = TARGET_TYPE_COUNTS[card.type]
        role_count = own_summary.role_counts[role]
        target_role = TARGET_ROLE_COUNTS[role]

        score = base_card_score(card)
        score += need_bonus(type_count, target_type, remaining_picks, weight=1.8)
        score += need_bonus(role_count, target_role, remaining_picks, weight=1.4)
        score -= duplicate_count * 1.0
        score += blessing_pick_adjustment(card, own_cards, cards)

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

    def choose_market_pick(
        self,
        *,
        visible_market: dict[str, tuple[str, ...]],
        topdeck_candidates: dict[str, tuple[str, ...]],
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        rng: random.Random,
    ) -> tuple[str, str]:
        scored: list[tuple[float, tuple[str, str]]] = []
        for offer in visible_market.values():
            for card_id in offer:
                score = self._score_market_card(
                    card_id,
                    cards,
                    own_hidden_cards,
                    own_public_cards,
                    opponent_public_cards,
                    visibility="public",
                )
                score += self.rng.uniform(-self.style.noise, self.style.noise)
                scored.append((score, ("visible", card_id)))
        for rarity, offer in topdeck_candidates.items():
            if not offer:
                continue
            candidate_scores = [
                self._score_market_card(
                    card_id,
                    cards,
                    own_hidden_cards,
                    own_public_cards,
                    opponent_public_cards,
                    visibility="hidden",
                )
                for card_id in offer
            ]
            if not candidate_scores:
                continue
            score = sum(candidate_scores) / len(candidate_scores)
            score += self.style.hidden_finisher_bonus * 0.15
            score += self.rng.uniform(-self.style.noise, self.style.noise)
            scored.append((score, ("topdeck", rarity)))
        scored.sort(key=lambda item: (item[0], item[1][1]), reverse=True)
        return scored[0][1]

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
        target_type_counts = self._target_type_counts()
        target_role_counts = self._target_role_counts()

        score = 0.0
        for card_id in bundle:
            card = cards[card_id]
            role = infer_role_color(card)
            score += base_card_score(card)
            score += need_bonus(
                own_summary.battle_count if card.type == "battle" else (own_summary.blessing_count if card.type == "blessing" else own_summary.control_count),
                target_type_counts[card.type],
                remaining_picks,
                weight=1.5,
            )
            score += need_bonus(
                own_summary.role_counts[role],
                target_role_counts[role],
                remaining_picks,
                weight=1.0,
            )
            score -= own_all.count(card.id) * 0.8
            score += blessing_pick_adjustment(card, own_all, cards)
            score += self._style_value(card)
            score += self._counter_value(card, opponent_public_profile)
            if visibility == "hidden":
                score += self._hidden_value(card)
            else:
                score += self._public_value(card, pick_position)
                score += self._denial_value(card, offer_flat, cards, opponent_public_cards)
            score += self._archetype_card_bonus(
                card,
                own_all,
                own_summary,
                cards,
                opponent_public_cards,
                visibility=visibility,
                pick_position=pick_position,
            )
        score += self._bundle_balance_value(bundle, cards, own_all)
        return round(score, 4)

    def _score_market_card(
        self,
        card_id: str,
        cards: dict[str, Card],
        own_hidden_cards: list[str],
        own_public_cards: list[str],
        opponent_public_cards: list[str],
        *,
        visibility: str,
    ) -> float:
        own_all = own_hidden_cards + own_public_cards
        own_summary = summarize_deck(own_all, cards)
        remaining_picks = MARKET_DECK_SIZE - len(own_all)
        opponent_public_profile = profile_card_ids(opponent_public_cards, cards)
        card = cards[card_id]
        role = infer_role_color(card)
        target_type_counts = _scaled_targets(self._target_type_counts(), MARKET_DECK_SIZE)
        target_role_counts = _scaled_targets(self._target_role_counts(), MARKET_DECK_SIZE)

        score = 0.0
        score += base_card_score(card)
        score += need_bonus(
            own_summary.battle_count if card.type == "battle" else (own_summary.blessing_count if card.type == "blessing" else own_summary.control_count),
            target_type_counts[card.type],
            remaining_picks,
            weight=1.4,
        )
        score += need_bonus(
            own_summary.role_counts[role],
            target_role_counts[role],
            remaining_picks,
            weight=0.9,
        )
        score -= own_all.count(card.id) * 0.8
        score += blessing_pick_adjustment(card, own_all, cards)
        score += self._style_value(card)
        score += self._counter_value(card, opponent_public_profile)
        if visibility == "hidden":
            score += self._hidden_value(card)
        else:
            score += self._public_value(card, 1)
            score += self._denial_value(card, tuple(opponent_public_cards), cards, opponent_public_cards)
        score += self._archetype_card_bonus(
            card,
            own_all,
            own_summary,
            cards,
            opponent_public_cards,
            visibility=visibility,
            pick_position=1,
        )
        return round(score, 4)

    def _target_type_counts(self) -> dict[str, int]:
        return TARGET_TYPE_COUNTS

    def _target_role_counts(self) -> dict[str, int]:
        return TARGET_ROLE_COUNTS

    def _archetype_card_bonus(
        self,
        card: Card,
        own_all: list[str],
        own_summary: DraftDeckSummary,
        cards: dict[str, Card],
        opponent_public_cards: list[str],
        *,
        visibility: str,
        pick_position: int,
    ) -> float:
        return 0.0

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

    def _archetype_card_bonus(
        self,
        card: Card,
        own_all: list[str],
        own_summary: DraftDeckSummary,
        cards: dict[str, Card],
        opponent_public_cards: list[str],
        *,
        visibility: str,
        pick_position: int,
    ) -> float:
        if card.id in BLESSING_HATE_CONTROL_IDS and any(cards[card_id].type == "blessing" for card_id in opponent_public_cards):
            return 1.0
        return 0.0


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

    def _target_type_counts(self) -> dict[str, int]:
        return {"battle": 14, "control": 5, "blessing": 1}

    def _target_role_counts(self) -> dict[str, int]:
        return {"red": 8, "blue": 5, "green": 3, "white": 4}

    def _archetype_card_bonus(
        self,
        card: Card,
        own_all: list[str],
        own_summary: DraftDeckSummary,
        cards: dict[str, Card],
        opponent_public_cards: list[str],
        *,
        visibility: str,
        pick_position: int,
    ) -> float:
        score = 0.0
        if card.id in AGGRO_PRIORITY_CONTROL_IDS:
            score += 1.4
        if card.type == "control":
            for effect in card.effects:
                if effect.kind in {"modify_self_attack", "modify_self_speed", "modify_opponent_block"}:
                    score += 1.0 + abs(effect.value) * 0.2
                elif effect.kind == "modify_opponent_speed":
                    score += 0.35
        if card.attack >= 4:
            score += 0.5
        if visibility == "hidden" and card.attack >= 4:
            score += 0.35
        if card.id in BLESSING_HATE_CONTROL_IDS and any(cards[card_id].type == "blessing" for card_id in opponent_public_cards):
            score += 0.4
        return score


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

    def _target_type_counts(self) -> dict[str, int]:
        return {"battle": 12, "control": 7, "blessing": 1}

    def _target_role_counts(self) -> dict[str, int]:
        return {"red": 4, "blue": 3, "green": 7, "white": 6}

    def _archetype_card_bonus(
        self,
        card: Card,
        own_all: list[str],
        own_summary: DraftDeckSummary,
        cards: dict[str, Card],
        opponent_public_cards: list[str],
        *,
        visibility: str,
        pick_position: int,
    ) -> float:
        score = 0.0
        if card.id in BLESSING_HATE_CONTROL_IDS and any(cards[card_id].type == "blessing" for card_id in opponent_public_cards):
            score += 1.6
        return score


class ControlDraftBot(PublicInfoDraftBot):
    name = "ControlDraftBot"
    style = DraftStyle(
        attack_weight=0.75,
        block_weight=1.05,
        speed_weight=0.9,
        control_weight=1.45,
        denial_weight=1.0,
        hidden_finisher_bonus=0.35,
        public_counter_bonus=0.95,
        reveal_penalty=0.4,
        noise=0.14,
    )

    def _target_type_counts(self) -> dict[str, int]:
        return {"battle": 10, "control": 9, "blessing": 1}

    def _target_role_counts(self) -> dict[str, int]:
        return {"red": 3, "blue": 4, "green": 5, "white": 8}

    def _archetype_card_bonus(
        self,
        card: Card,
        own_all: list[str],
        own_summary: DraftDeckSummary,
        cards: dict[str, Card],
        opponent_public_cards: list[str],
        *,
        visibility: str,
        pick_position: int,
    ) -> float:
        score = 0.0
        if card.id in CONTROL_FOCUS_IDS:
            score += 1.4
        if card.type == "control":
            score += 0.75
        if card.type == "battle" and card.attack >= 4 and card.block <= 0:
            score -= 0.6
        if card.id in BLESSING_HATE_CONTROL_IDS and any(cards[card_id].type == "blessing" for card_id in opponent_public_cards):
            score += 1.0
        return score


class BlessingDraftBot(PublicInfoDraftBot):
    name = "BlessingDraftBot"
    style = DraftStyle(
        attack_weight=0.8,
        block_weight=1.0,
        speed_weight=0.9,
        control_weight=1.4,
        denial_weight=0.8,
        hidden_finisher_bonus=0.3,
        public_counter_bonus=0.85,
        reveal_penalty=0.35,
        noise=0.14,
    )

    def _target_type_counts(self) -> dict[str, int]:
        return {"battle": 11, "control": 7, "blessing": 2}

    def _target_role_counts(self) -> dict[str, int]:
        return {"red": 4, "blue": 5, "green": 5, "white": 6}

    def _archetype_card_bonus(
        self,
        card: Card,
        own_all: list[str],
        own_summary: DraftDeckSummary,
        cards: dict[str, Card],
        opponent_public_cards: list[str],
        *,
        visibility: str,
        pick_position: int,
    ) -> float:
        score = 0.0
        if card.type == "blessing":
            blessing_count = sum(1 for card_id in own_all if cards[card_id].type == "blessing")
            score += 1.2 if blessing_count == 0 else 0.5
        if card.id in BLESSING_SUPPORT_IDS:
            score += 1.35
        if card.id in BLESSING_HATE_CONTROL_IDS and any(cards[card_id].type == "blessing" for card_id in opponent_public_cards):
            score += 0.8
        return score


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
    if draft_mode == MARKET_DRAFT_MODE:
        return _draft_with_market_bots(
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
    if draft_mode not in FULL_DRAFT_PROFILES:
        raise ValueError(f"unsupported draft_mode: {draft_mode}")
    profile = FULL_DRAFT_PROFILES[draft_mode]
    if deck_size != profile["deck_size"]:
        raise ValueError(f"{draft_mode} draft flow requires deck_size={profile['deck_size']}")
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

    for round_name in profile["rounds"]:
        if round_name == "normal_first":
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
        elif round_name == "rare_first":
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
        elif round_name == "normal_second":
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
        elif round_name == "rare_second":
            pick_number = _run_rare_half(
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

    if profile.get("trim_after_full"):
        for player_id in ("p1", "p2"):
            _trim_drafted_to_profile(drafted[player_id], cards, profile)

    _validate_final_composition(drafted, cards, profile)

    deck1 = _build_draft_deck(deck1_id, deck1_name, drafted["p1"], picks, draft_mode=draft_mode, profile=profile)
    deck2 = _build_draft_deck(deck2_id, deck2_name, drafted["p2"], picks, draft_mode=draft_mode, profile=profile)
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


BLESSING_SUPPORT_IDS = {"control_discard_facedown_blessing", "control_blessing_break"}


def blessing_pick_adjustment(card: Card, own_cards: list[str], cards: dict[str, Card]) -> float:
    if card.type != "blessing":
        return 0.0
    blessing_count = sum(1 for card_id in own_cards if cards[card_id].type == "blessing")
    support_count = sum(1 for card_id in own_cards if card_id in BLESSING_SUPPORT_IDS)
    if blessing_count == 0:
        return 0.55
    if blessing_count == 1:
        return 0.1
    penalty = 1.0 + (blessing_count - 2) * 0.7
    penalty -= min(support_count, 2) * 0.45
    return -max(penalty, 0.15)


def _scaled_targets(base_counts: dict[str, int], total: int) -> dict[str, int]:
    source_total = sum(base_counts.values())
    if source_total <= 0:
        return {key: 0 for key in base_counts}

    scaled_raw = {key: value * total / source_total for key, value in base_counts.items()}
    scaled = {key: int(scaled_raw[key]) for key in base_counts}
    assigned = sum(scaled.values())
    if assigned < total:
        remainder_order = sorted(
            base_counts,
            key=lambda key: (scaled_raw[key] - scaled[key], base_counts[key]),
            reverse=True,
        )
        for key in remainder_order[: total - assigned]:
            scaled[key] += 1
    elif assigned > total:
        overflow = assigned - total
        reduce_order = sorted(
            (key for key in base_counts if scaled[key] > 0),
            key=lambda key: (scaled_raw[key] - scaled[key], -base_counts[key]),
        )
        for key in reduce_order:
            if overflow <= 0:
                break
            scaled[key] -= 1
            overflow -= 1
    return scaled


def _market_empty_drafted_state() -> dict[str, list[str]]:
    return {
        "starter": list(STARTER_CARD_IDS),
        "public_market": [],
        "hidden_market": [],
        "common_slots": [],
        "uncommon_slots": [],
        "rare_slots": [],
    }


def _market_next_slot_name(card: Card, drafted: dict[str, list[str]]) -> str | None:
    if card.rarity == "rare":
        return "rare_slots" if len(drafted["rare_slots"]) < MARKET_SLOT_CAPS["rare"] else None
    if card.rarity == "uncommon":
        if len(drafted["uncommon_slots"]) < MARKET_SLOT_CAPS["uncommon"]:
            return "uncommon_slots"
        if len(drafted["rare_slots"]) < MARKET_SLOT_CAPS["rare"]:
            return "rare_slots"
        return None
    if len(drafted["common_slots"]) < MARKET_SLOT_CAPS["common"]:
        return "common_slots"
    if len(drafted["uncommon_slots"]) < MARKET_SLOT_CAPS["uncommon"]:
        return "uncommon_slots"
    if len(drafted["rare_slots"]) < MARKET_SLOT_CAPS["rare"]:
        return "rare_slots"
    return None


def _market_can_take_card(card: Card, drafted: dict[str, list[str]]) -> bool:
    return _market_next_slot_name(card, drafted) is not None


def _market_can_take_rarity(rarity: str, cards: dict[str, Card], drafted: dict[str, list[str]]) -> bool:
    for card in cards.values():
        if card.rarity == rarity and _market_can_take_card(card, drafted):
            return True
    return False


def _market_assign_card(
    drafted: dict[str, list[str]],
    card_id: str,
    cards: dict[str, Card],
    *,
    visibility: str,
) -> None:
    card = cards[card_id]
    slot_name = _market_next_slot_name(card, drafted)
    if slot_name is None:
        raise ValueError(f"no legal slot remaining for {card_id}")
    drafted[slot_name].append(card_id)
    if visibility == "public":
        drafted["public_market"].append(card_id)
    else:
        drafted["hidden_market"].append(card_id)


def _market_visible_offer_groups(visible_market: dict[str, list[str]]) -> tuple[tuple[str, ...], ...]:
    return (
        tuple(visible_market["rare"]),
        tuple(visible_market["uncommon"]),
        tuple(visible_market["common"]),
    )


def _market_flat_visible_offer(visible_market: dict[str, list[str]]) -> tuple[str, ...]:
    return tuple(card_id for group in _market_visible_offer_groups(visible_market) for card_id in group)


def _market_topdeck_candidates(
    available: Counter[str],
    cards: dict[str, Card],
    drafted: dict[str, list[str]],
) -> dict[str, tuple[str, ...]]:
    candidates: dict[str, tuple[str, ...]] = {}
    for rarity in ("rare", "uncommon", "common"):
        if not _market_can_take_rarity(rarity, cards, drafted):
            candidates[rarity] = ()
            continue
        candidates[rarity] = tuple(
            sorted(card_id for card_id, count in available.items() if count > 0 and cards[card_id].rarity == rarity)
        )
    return candidates


def _market_find_visible_card_rarity(visible_market: dict[str, list[str]], card_id: str) -> str | None:
    for rarity, row in visible_market.items():
        if card_id in row:
            return rarity
    return None


def _sanitize_market_pick(
    choice: tuple[str, str],
    *,
    visible_market: dict[str, list[str]],
    topdeck_candidates: dict[str, tuple[str, ...]],
    cards: dict[str, Card],
    drafted: dict[str, list[str]],
) -> tuple[str, str]:
    mode, value = choice
    if mode == "visible":
        rarity = _market_find_visible_card_rarity(visible_market, value)
        if rarity is not None and _market_can_take_card(cards[value], drafted):
            return choice
    elif mode == "topdeck":
        offer = topdeck_candidates.get(value, ())
        if offer:
            return choice

    for rarity in ("rare", "uncommon", "common"):
        for card_id in visible_market[rarity]:
            if _market_can_take_card(cards[card_id], drafted):
                return ("visible", card_id)
    for rarity in ("rare", "uncommon", "common"):
        if topdeck_candidates.get(rarity):
            return ("topdeck", rarity)
    raise ValueError("no legal market picks remain")


def _build_market_draft_deck(
    deck_id: str,
    name: str,
    drafted: dict[str, list[str]],
    picks: list[DraftPick],
) -> DeckDefinition:
    public_cards = tuple(drafted["starter"] + drafted["public_market"])
    hidden_cards = tuple(drafted["hidden_market"])
    metadata = {
        "starter_cards": list(drafted["starter"]),
        "public_market_cards": list(drafted["public_market"]),
        "hidden_market_cards": list(drafted["hidden_market"]),
        "common_slot_cards": list(drafted["common_slots"]),
        "uncommon_slot_cards": list(drafted["uncommon_slots"]),
        "rare_slot_cards": list(drafted["rare_slots"]),
        "final_rarity_counts": dict(MARKET_FINAL_RARITY_COUNTS),
        "draft_mode": MARKET_DRAFT_MODE,
        "public_draft_events": _build_public_draft_events(picks),
    }
    return DeckDefinition(
        id=deck_id,
        name=name,
        public_cards=public_cards,
        hidden_cards=hidden_cards,
        metadata=metadata,
    )


def _validate_market_final_composition(
    drafted: dict[str, dict[str, list[str]]],
    cards: dict[str, Card],
) -> None:
    for player_id in ("p1", "p2"):
        player_drafted = drafted[player_id]
        if tuple(player_drafted["starter"]) != STARTER_CARD_IDS:
            raise ValueError(f"{player_id}: invalid starter cards")
        if len(player_drafted["public_market"]) + len(player_drafted["hidden_market"]) != MARKET_DRAFTED_CARD_COUNT:
            raise ValueError(f"{player_id}: invalid drafted market count")
        if len(player_drafted["common_slots"]) != MARKET_SLOT_CAPS["common"]:
            raise ValueError(f"{player_id}: invalid common slot count")
        if len(player_drafted["uncommon_slots"]) != MARKET_SLOT_CAPS["uncommon"]:
            raise ValueError(f"{player_id}: invalid uncommon slot count")
        if len(player_drafted["rare_slots"]) != MARKET_SLOT_CAPS["rare"]:
            raise ValueError(f"{player_id}: invalid rare slot count")
        summary = summarize_deck(
            player_drafted["starter"] + player_drafted["public_market"] + player_drafted["hidden_market"],
            cards,
        )
        if summary.total != MARKET_DECK_SIZE:
            raise ValueError(f"{player_id}: invalid final deck size")
        if summary.rarity_counts != MARKET_FINAL_RARITY_COUNTS:
            raise ValueError(f"{player_id}: invalid rarity composition")


def _draft_with_market_bots(
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
    if deck_size != MARKET_DECK_SIZE:
        raise ValueError(f"{MARKET_DRAFT_MODE} draft flow requires deck_size={MARKET_DECK_SIZE}")
    available = Counter({entry.card_id: entry.count for entry in pool.entries})
    first = first_player or rng.choice(("p1", "p2"))
    bots = {"p1": bot1, "p2": bot2}
    drafted: dict[str, dict[str, list[str]]] = {
        "p1": _market_empty_drafted_state(),
        "p2": _market_empty_drafted_state(),
    }
    picks: list[DraftPick] = []

    visible_market = {
        "rare": list(_draw_cards_by_rarity(available, cards, "rare", MARKET_VISIBLE_COUNT, rng)),
        "uncommon": list(_draw_cards_by_rarity(available, cards, "uncommon", MARKET_VISIBLE_COUNT, rng)),
        "common": list(_draw_cards_by_rarity(available, cards, "common", MARKET_VISIBLE_COUNT, rng)),
    }

    for pick_number in range(1, MARKET_DRAFTED_CARD_COUNT * 2 + 1):
        player_id = first if pick_number % 2 == 1 else _opponent_of(first)
        opponent_id = _opponent_of(player_id)
        topdeck_candidates = _market_topdeck_candidates(available, cards, drafted[player_id])
        choice = bots[player_id].choose_market_pick(
            visible_market={rarity: tuple(cards_in_row) for rarity, cards_in_row in visible_market.items()},
            topdeck_candidates=topdeck_candidates,
            cards=cards,
            own_hidden_cards=list(drafted[player_id]["hidden_market"]),
            own_public_cards=list(drafted[player_id]["starter"] + drafted[player_id]["public_market"]),
            opponent_public_cards=list(drafted[opponent_id]["starter"] + drafted[opponent_id]["public_market"]),
            rng=rng,
        )
        mode, value = _sanitize_market_pick(
            choice,
            visible_market=visible_market,
            topdeck_candidates=topdeck_candidates,
            cards=cards,
            drafted=drafted[player_id],
        )
        round_number = (pick_number + 1) // 2
        if mode == "visible":
            visible_offer_groups = _market_visible_offer_groups(visible_market)
            rarity = _market_find_visible_card_rarity(visible_market, value)
            if rarity is None:
                raise ValueError(f"market visible card missing: {value}")
            visible_market[rarity].remove(value)
            _market_assign_card(drafted[player_id], value, cards, visibility="public")
            picks.append(
                DraftPick(
                    number=pick_number,
                    player_id=player_id,
                    card_id=value,
                    visibility="public",
                    phase="market_public",
                    offer_card_ids=tuple(card_id for group in visible_offer_groups for card_id in group),
                    offer_groups=visible_offer_groups,
                    selected_card_ids=(value,),
                    pick_position=1,
                    round_number=round_number,
                )
            )
            if any(cards[card_id].rarity == rarity for card_id in available):
                visible_market[rarity].extend(_draw_cards_by_rarity(available, cards, rarity, 1, rng))
        else:
            rarity = value
            chosen_card_id = _draw_cards_by_rarity(available, cards, rarity, 1, rng)[0]
            _market_assign_card(drafted[player_id], chosen_card_id, cards, visibility="hidden")
            picks.append(
                DraftPick(
                    number=pick_number,
                    player_id=player_id,
                    card_id=chosen_card_id,
                    visibility="hidden",
                    phase="market_hidden",
                    offer_card_ids=topdeck_candidates.get(rarity, ()),
                    offer_groups=(topdeck_candidates.get(rarity, ()),),
                    selected_card_ids=(chosen_card_id,),
                    pick_position=1,
                    round_number=round_number,
                )
            )

    _validate_market_final_composition(drafted, cards)
    deck1 = _build_market_draft_deck(deck1_id, deck1_name, drafted["p1"], picks)
    deck2 = _build_market_draft_deck(deck2_id, deck2_name, drafted["p2"], picks)
    return DraftResult(
        pool=pool,
        deck1=deck1,
        deck2=deck2,
        picks=tuple(picks),
        first_player=first,
    )


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


def _build_draft_deck(
    deck_id: str,
    name: str,
    drafted: dict[str, list[str]],
    picks: list[DraftPick],
    *,
    draft_mode: str,
    profile: dict[str, object],
) -> DeckDefinition:
    public_cards = tuple(drafted["public_normal"] + drafted["public_rare"])
    hidden_cards = tuple(drafted["hidden_normal"] + drafted["hidden_rare"])
    metadata = {
        "public_normal_cards": list(drafted["public_normal"]),
        "hidden_normal_cards": list(drafted["hidden_normal"]),
        "public_rare_cards": list(drafted["public_rare"]),
        "hidden_rare_cards": list(drafted["hidden_rare"]),
        "final_rarity_counts": dict(profile["rarity_counts"]),
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


def _trim_drafted_to_profile(
    drafted: dict[str, list[str]],
    cards: dict[str, Card],
    profile: dict[str, object],
) -> None:
    rarity_counts = profile["rarity_counts"]
    _trim_normal_zones_to_profile(
        drafted,
        cards,
        public_target=int(profile["public_normal"]),
        hidden_target=int(profile["hidden_normal"]),
        common_target=int(rarity_counts["common"]),
        uncommon_target=int(rarity_counts["uncommon"]),
    )
    drafted["public_rare"] = _trim_card_ids_to_count(drafted["public_rare"], int(profile["public_rare"]), cards)
    drafted["hidden_rare"] = _trim_card_ids_to_count(drafted["hidden_rare"], int(profile["hidden_rare"]), cards)


def _trim_normal_zones_to_profile(
    drafted: dict[str, list[str]],
    cards: dict[str, Card],
    *,
    public_target: int,
    hidden_target: int,
    common_target: int,
    uncommon_target: int,
) -> None:
    zone_cards = {
        "public_common": [card_id for card_id in drafted["public_normal"] if cards[card_id].rarity == "common"],
        "public_uncommon": [card_id for card_id in drafted["public_normal"] if cards[card_id].rarity == "uncommon"],
        "hidden_common": [card_id for card_id in drafted["hidden_normal"] if cards[card_id].rarity == "common"],
        "hidden_uncommon": [card_id for card_id in drafted["hidden_normal"] if cards[card_id].rarity == "uncommon"],
    }
    best_plan: tuple[float, tuple[int, int, int, int]] | None = None
    for public_common_count in range(0, min(len(zone_cards["public_common"]), public_target) + 1):
        public_uncommon_count = public_target - public_common_count
        if public_uncommon_count < 0 or public_uncommon_count > len(zone_cards["public_uncommon"]):
            continue
        hidden_common_count = common_target - public_common_count
        hidden_uncommon_count = uncommon_target - public_uncommon_count
        if hidden_common_count < 0 or hidden_common_count > len(zone_cards["hidden_common"]):
            continue
        if hidden_uncommon_count < 0 or hidden_uncommon_count > len(zone_cards["hidden_uncommon"]):
            continue
        if hidden_common_count + hidden_uncommon_count != hidden_target:
            continue
        plan = (
            public_common_count,
            public_uncommon_count,
            hidden_common_count,
            hidden_uncommon_count,
        )
        score = _zone_keep_score(zone_cards["public_common"], public_common_count, cards)
        score += _zone_keep_score(zone_cards["public_uncommon"], public_uncommon_count, cards)
        score += _zone_keep_score(zone_cards["hidden_common"], hidden_common_count, cards)
        score += _zone_keep_score(zone_cards["hidden_uncommon"], hidden_uncommon_count, cards)
        if best_plan is None or score > best_plan[0]:
            best_plan = (score, plan)
    if best_plan is None:
        raise ValueError("unable to trim normal zones to requested profile")
    public_common_count, public_uncommon_count, hidden_common_count, hidden_uncommon_count = best_plan[1]
    kept_public_common = _trim_card_ids_to_count(zone_cards["public_common"], public_common_count, cards)
    kept_public_uncommon = _trim_card_ids_to_count(zone_cards["public_uncommon"], public_uncommon_count, cards)
    kept_hidden_common = _trim_card_ids_to_count(zone_cards["hidden_common"], hidden_common_count, cards)
    kept_hidden_uncommon = _trim_card_ids_to_count(zone_cards["hidden_uncommon"], hidden_uncommon_count, cards)
    drafted["public_normal"] = _rebuild_zone_in_original_order(
        drafted["public_normal"],
        kept_public_common,
        kept_public_uncommon,
    )
    drafted["hidden_normal"] = _rebuild_zone_in_original_order(
        drafted["hidden_normal"],
        kept_hidden_common,
        kept_hidden_uncommon,
    )


def _zone_keep_score(card_ids: list[str], target: int, cards: dict[str, Card]) -> float:
    if target <= 0:
        return 0.0
    kept = _trim_card_ids_to_count(card_ids, target, cards)
    return sum(base_card_score(cards[card_id]) + len(cards[card_id].effects) * 0.1 for card_id in kept)


def _trim_card_ids_to_count(card_ids: list[str], target: int, cards: dict[str, Card]) -> list[str]:
    if len(card_ids) <= target:
        return list(card_ids)
    scored = [
        (base_card_score(cards[card_id]) + len(cards[card_id].effects) * 0.1, index, card_id)
        for index, card_id in enumerate(card_ids)
    ]
    scored.sort(key=lambda item: (item[0], -item[1]), reverse=True)
    kept_indexes = {index for _, index, _ in scored[:target]}
    return [card_id for index, card_id in enumerate(card_ids) if index in kept_indexes]


def _rebuild_zone_in_original_order(original: list[str], kept_a: list[str], kept_b: list[str]) -> list[str]:
    remaining = Counter(kept_a + kept_b)
    rebuilt: list[str] = []
    for card_id in original:
        if remaining[card_id] > 0:
            rebuilt.append(card_id)
            remaining[card_id] -= 1
    return rebuilt


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


def _validate_final_composition(
    drafted: dict[str, dict[str, list[str]]],
    cards: dict[str, Card],
    profile: dict[str, object],
) -> None:
    expected_public_normal = int(profile["public_normal"])
    expected_hidden_normal = int(profile["hidden_normal"])
    expected_public_rare = int(profile["public_rare"])
    expected_hidden_rare = int(profile["hidden_rare"])
    expected_rarities = profile["rarity_counts"]
    expected_total = int(profile["deck_size"])
    for player_id in ("p1", "p2"):
        public_normal = drafted[player_id]["public_normal"]
        hidden_normal = drafted[player_id]["hidden_normal"]
        public_rare = drafted[player_id]["public_rare"]
        hidden_rare = drafted[player_id]["hidden_rare"]
        if len(public_normal) != expected_public_normal or len(hidden_normal) != expected_hidden_normal:
            raise ValueError(f"{player_id}: invalid normal draft count")
        if len(public_rare) != expected_public_rare or len(hidden_rare) != expected_hidden_rare:
            raise ValueError(f"{player_id}: invalid rare draft count")
        summary = summarize_deck(public_normal + hidden_normal + public_rare + hidden_rare, cards)
        if summary.total != expected_total:
            raise ValueError(f"{player_id}: invalid final deck size")
        if (
            summary.rarity_counts["common"] != expected_rarities["common"]
            or summary.rarity_counts["uncommon"] != expected_rarities["uncommon"]
            or summary.rarity_counts["rare"] != expected_rarities["rare"]
        ):
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
