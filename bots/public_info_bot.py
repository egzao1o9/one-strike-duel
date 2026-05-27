from __future__ import annotations

from dataclasses import dataclass
import random

from bots.base_bot import BaseBot, BattleAction
from engine.analysis import (
    HandProfile,
    StatLine,
    battle_cards,
    build_hand_profile,
    card_line,
    combined_battle_line,
    profile_card_ids,
    public_view_profile,
)
from engine.card import Card, Effect, load_cards
from engine.game_state import PlayerView


@dataclass(frozen=True)
class StyleProfile:
    attack_weight: float
    block_weight: float
    speed_weight: float
    control_weight: float
    reveal_weight: float
    risk_penalty: float
    continuation_weight: float
    noise: float


class PublicInfoBot(BaseBot):
    name = "PublicInfoBot"
    style = StyleProfile(
        attack_weight=1.0,
        block_weight=1.0,
        speed_weight=0.9,
        control_weight=1.0,
        reveal_weight=0.7,
        risk_penalty=0.7,
        continuation_weight=0.45,
        noise=0.2,
    )

    def __init__(self, seed: int, cards_path: str = "data/cards.json") -> None:
        self.rng = random.Random(seed)
        self.cards_by_id = load_cards(cards_path)

    def choose_mulligan(self, view: PlayerView) -> list[str]:
        scored = self._score_hand_cards(view)
        if len(view.hand) <= 4:
            weak = [card_id for card_id, score in scored if score < 0.7]
            max_discards = max(0, len(view.hand) - 2)
            return weak[: min(2, max_discards)]
        target_keep = 4 if view.phase == "phase1_mulligan" else max(4, len(view.hand) - 2)
        return [card_id for card_id, _ in scored[target_keep:]]

    def choose_overflow_discards(self, view: PlayerView, overflow_count: int) -> list[str]:
        scored = self._score_hand_cards(view)
        return [card_id for card_id, _ in scored[-overflow_count:]]

    def choose_control_card(self, view: PlayerView) -> str | None:
        controls = [card for card in view.hand if card.type == "control"]
        if not controls:
            return None
        opponent_profile = public_view_profile(view, self.cards_by_id, owner="opponent")
        hand_profile = build_hand_profile(view.hand)
        scored = sorted(
            ((self._score_control_card(card, hand_profile, opponent_profile), card.id) for card in controls),
            reverse=True,
        )
        best_score, best_id = scored[0]
        if best_score <= 0.2:
            return None
        return best_id

    def choose_battle_action(self, view: PlayerView) -> BattleAction:
        actions = self._legal_actions(view)
        if len(actions) == 1:
            return actions[0]
        scored = []
        for action in actions:
            score = self._score_action(view, action)
            score += self.rng.uniform(-self.style.noise, self.style.noise)
            scored.append((score, action))
        scored.sort(key=lambda item: item[0], reverse=True)
        return scored[0][1]

    def _score_hand_cards(self, view: PlayerView) -> list[tuple[str, float]]:
        own_profile = profile_card_ids(view.own_public_deck + view.own_hidden_deck, self.cards_by_id)
        opponent_profile = public_view_profile(view, self.cards_by_id, owner="opponent")
        hand_profile = build_hand_profile(view.hand)
        scored: list[tuple[str, float]] = []
        for card in view.hand:
            if card.type == "battle":
                line = card_line(card)
                score = (
                    max(line.attack, 0) * self.style.attack_weight
                    + max(line.block, 0) * self.style.block_weight * 0.9
                    + max(line.speed, 0) * self.style.speed_weight * 0.8
                    - max(-line.attack, 0) * 0.5
                    - max(-line.block, 0) * 0.35
                    - max(-line.speed, 0) * 0.3
                )
                score += self._effect_score(card.effects)
                if card.id in hand_profile.best_attack_combo:
                    score += 0.7
                if card.id in hand_profile.best_block_combo:
                    score += 0.6
                if card.id in hand_profile.best_speed_combo:
                    score += 0.5
                if own_profile.control_count > own_profile.battle_count and card.attack > opponent_profile.average_block:
                    score += 0.5
            else:
                score = self._score_control_card(card, hand_profile, opponent_profile)
            scored.append((card.id, round(score, 4)))
        scored.sort(key=lambda item: item[1], reverse=True)
        return scored

    def _score_control_card(self, card: Card, hand_profile: HandProfile, opponent_profile) -> float:
        score = self.style.control_weight * 0.35
        score += self._effect_score(card.effects)
        for effect in card.effects:
            if effect.kind == "draw_cards":
                score += 1.1
            elif effect.kind == "reveal_opponent_hand_random":
                score += self.style.reveal_weight
            elif effect.kind == "modify_opponent_block":
                score += max(hand_profile.best_attack.attack - opponent_profile.average_block, 0) * 0.45
            elif effect.kind == "modify_self_speed":
                score += max(hand_profile.best_speed.speed - opponent_profile.average_speed, 0) * 0.3
            elif effect.kind == "modify_self_block":
                score += max(opponent_profile.average_attack - hand_profile.best_block.block, 0) * 0.35
        return round(score, 4)

    def _legal_actions(self, view: PlayerView) -> list[BattleAction]:
        battles = [card for card in view.hand if card.type == "battle"]
        legal_slots = max(0, view.opponent_facedown_count + 1 - view.own_facedown_count)
        actions = [BattleAction("pass")]
        if legal_slots <= 0 or not battles:
            return actions
        for card in battles:
            actions.append(BattleAction("set_pass", (card.id,)))
            actions.append(BattleAction("set", (card.id,)))
        if legal_slots >= 2:
            for left_index in range(len(battles)):
                for right_index in range(left_index + 1, len(battles)):
                    combo = (battles[left_index].id, battles[right_index].id)
                    actions.append(BattleAction("set", combo))
        unique: dict[tuple[str, tuple[str, ...]], BattleAction] = {}
        for action in actions:
            unique[(action.action_type, action.card_ids)] = action
        return list(unique.values())

    def _score_action(self, view: PlayerView, action: BattleAction) -> float:
        selected_cards = [self.cards_by_id[card_id] for card_id in action.card_ids]
        current_cards = list(view.own_set_cards)
        own_after = len(current_cards) + len(selected_cards)
        opponent_profile = public_view_profile(view, self.cards_by_id, owner="opponent")
        own_line, opp_delta = combined_battle_line(
            current_cards + selected_cards,
            own_control=view.own_control_card,
            opponent_control=view.opponent_control_card,
        )
        opponent_line = self._estimated_opponent_line(view, opponent_profile, own_after, action.action_type).add(opp_delta)
        attack_margin = own_line.attack - opponent_line.block
        block_margin = own_line.block - opponent_line.attack
        speed_margin = own_line.speed - opponent_line.speed

        score = (
            attack_margin * self.style.attack_weight * 1.35
            + block_margin * self.style.block_weight * 0.9
            + speed_margin * self.style.speed_weight * 0.85
        )
        score -= len(selected_cards) * self.style.risk_penalty
        score += self._action_shape_bonus(view, action, attack_margin, block_margin, speed_margin)

        if action.action_type == "set":
            remaining = [
                card
                for card in view.hand
                if card.type == "battle" and card.id not in action.card_ids
            ]
            future = build_hand_profile(remaining)
            score += future.best_attack.attack * 0.18 * self.style.continuation_weight
            score += future.best_speed.speed * 0.14 * self.style.continuation_weight
        return round(score, 4)

    def _estimated_opponent_line(self, view: PlayerView, opponent_profile, own_after: int, action_type: str) -> StatLine:
        if view.opponent_battle_passed:
            final_count = view.opponent_facedown_count
        else:
            legal_slots = max(0, own_after + 1 - view.opponent_facedown_count)
            typical_add = min(2, legal_slots)
            if action_type == "pass":
                typical_add = 0
            elif action_type == "set_pass":
                typical_add = min(1, typical_add)
            elif view.opponent_hand_count <= 1:
                typical_add = min(1, typical_add)
            final_count = view.opponent_facedown_count + typical_add
        return StatLine(
            attack=round(opponent_profile.average_attack * final_count),
            block=round(opponent_profile.average_block * final_count),
            speed=round(opponent_profile.average_speed * final_count),
        )

    def _action_shape_bonus(
        self,
        view: PlayerView,
        action: BattleAction,
        attack_margin: float,
        block_margin: float,
        speed_margin: float,
    ) -> float:
        if action.action_type == "pass":
            return 1.2 if view.own_facedown_count > 0 and attack_margin >= 0 and block_margin >= -1 else -1.1
        if action.action_type == "set_pass":
            if attack_margin > 0 and (speed_margin >= 0 or block_margin >= 0):
                return 1.6
            if view.opponent_battle_passed and attack_margin <= 0 and block_margin < 0:
                return -1.5
            return 0.45
        bonus = 0.35
        if view.opponent_battle_passed and attack_margin > 0:
            bonus -= 0.6
        if view.opponent_facedown_count > view.own_facedown_count:
            bonus += 0.45
        return bonus

    def _effect_score(self, effects: tuple[Effect, ...]) -> float:
        score = 0.0
        for effect in effects:
            if effect.kind in {"modify_self_attack", "modify_opponent_block"}:
                score += abs(effect.value) * 0.45
            elif effect.kind in {"modify_self_block", "modify_opponent_attack"}:
                score += abs(effect.value) * 0.35
            elif effect.kind in {"modify_self_speed", "modify_opponent_speed"}:
                score += abs(effect.value) * 0.3
            elif effect.kind == "draw_cards":
                score += 0.9
            elif effect.kind == "reveal_opponent_hand_random":
                score += self.style.reveal_weight
        return score


class StandardBot(PublicInfoBot):
    name = "StandardBot"


class AggroBot(PublicInfoBot):
    name = "AggroBot"
    style = StyleProfile(
        attack_weight=1.35,
        block_weight=0.7,
        speed_weight=1.05,
        control_weight=0.8,
        reveal_weight=0.55,
        risk_penalty=0.4,
        continuation_weight=0.55,
        noise=0.28,
    )


class GuardBot(PublicInfoBot):
    name = "GuardBot"
    style = StyleProfile(
        attack_weight=0.85,
        block_weight=1.35,
        speed_weight=0.75,
        control_weight=1.15,
        reveal_weight=0.8,
        risk_penalty=0.85,
        continuation_weight=0.35,
        noise=0.18,
    )

