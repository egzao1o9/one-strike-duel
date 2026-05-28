from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Any

from bots.base_bot import BaseBot, BattleAction
from engine.analysis import (
    HandProfile,
    StatLine,
    battle_cards,
    build_hand_profile,
    card_line,
    combined_battle_line,
    profile_cards,
    profile_card_ids,
    public_view_profile,
    remaining_public_cards,
)
from engine.card import Card, Effect, load_cards
from engine.card_pool import build_default_card_pool, load_card_pool
from engine.drafting import infer_role_color
from engine.game_state import PlayerView

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

BLESSING_SUPPORT_CONTROL_IDS = {
    "control_discard_facedown_blessing",
    "control_blessing_flip",
    "control_blessing_break",
    "control_blessing_lock",
    "control_defile",
}


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

    def __init__(self, seed: int, cards_path: str = "data/cards.json", pool_path: str = "data/card_pool.json") -> None:
        self.rng = random.Random(seed)
        self.cards_by_id = load_cards(cards_path)
        self._last_debug_info: dict[str, Any] = {}
        try:
            self.card_pool = load_card_pool(pool_path, self.cards_by_id)
        except FileNotFoundError:
            self.card_pool = build_default_card_pool(self.cards_by_id)

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
        controls = [
            card
            for card in view.hand
            if card.type == "control" or (card.type == "blessing" and view.own_blessing_zone is None)
        ]
        if not controls:
            return None
        opponent_profile = public_view_profile(view, self.cards_by_id, owner="opponent")
        hand_profile = build_hand_profile(view.hand)
        scored = [
            (self._score_control_card(view, card, hand_profile, opponent_profile), card.id)
            for card in controls
        ]
        scored.sort(reverse=True)
        best_score, best_id = scored[0]
        self._last_debug_info["control"] = {
            "selected_id": None if best_score <= 0.2 else best_id,
            "selected_score": round(best_score, 4),
            "candidates": [
                {"card_id": card_id, "score": round(score, 4)}
                for score, card_id in scored
            ],
        }
        if best_score <= 0.2:
            return None
        return best_id

    def choose_battle_action(self, view: PlayerView) -> BattleAction:
        actions = self._legal_actions(view)
        if len(actions) == 1:
            return actions[0]
        mode = self._choose_battle_mode(view)
        scored = []
        for action in actions:
            score = self._score_action(view, action, mode)
            noise = self.rng.uniform(-self.style.noise, self.style.noise)
            scored.append((score + noise, action, score, noise))
        self._last_debug_info["battle"] = {
            "mode": mode,
            "set_pass_candidate_count": sum(1 for action in actions if action.action_type == "set_pass"),
            "candidates": [
                {
                    "action_type": action.action_type,
                    "card_ids": list(action.card_ids),
                    "base_score": round(base_score, 4),
                    "noise": round(noise, 4),
                    "final_score": round(final_score, 4),
                }
                for final_score, action, base_score, noise in sorted(scored, key=lambda item: item[0], reverse=True)
            ],
        }
        scored.sort(key=lambda item: item[0], reverse=True)
        chosen = scored[0][1]
        chosen_prediction = self._build_prediction_summary(view, chosen, mode)
        self._last_debug_info["battle"]["selected"] = {
            "action_type": chosen.action_type,
            "card_ids": list(chosen.card_ids),
            "prediction": chosen_prediction,
        }
        return chosen

    def consume_debug_info(self) -> dict[str, Any] | None:
        payload = dict(self._last_debug_info)
        self._last_debug_info.clear()
        return payload or None

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
                score = self._score_control_card(view, card, hand_profile, opponent_profile)
            score += self._archetype_hand_bonus(view, card, hand_profile, opponent_profile)
            scored.append((card.id, round(score, 4)))
        scored.sort(key=lambda item: item[1], reverse=True)
        return scored

    def _score_control_card(self, view: PlayerView, card: Card, hand_profile: HandProfile, opponent_profile) -> float:
        score = self.style.control_weight * 0.35
        score += self._effect_score(card.effects)
        if card.type == "blessing":
            score += 0.8
            if view.own_blessing_zone is None:
                score += 0.25
            else:
                score -= 0.15
        single_card_threat = self._estimate_opponent_threat_line(view, opponent_profile, 1)
        double_card_threat = self._estimate_opponent_threat_line(view, opponent_profile, 2)
        for effect in card.effects:
            effect_key = effect.kind or effect.effect_type
            if effect_key == "draw_cards":
                score += 1.1
            elif effect_key == "reveal_opponent_hand_random":
                score += self.style.reveal_weight
            elif effect_key == "modify_opponent_block" or (
                effect.effect_type == "modify_total_stat" and effect.target == "opponent_total" and effect.stat == "block"
            ):
                score += max(hand_profile.best_attack.attack - opponent_profile.average_block, 0) * 0.45
            elif effect_key == "modify_self_speed" or (
                effect.effect_type == "modify_total_stat" and effect.target == "self_total" and effect.stat == "speed"
            ):
                score += max(hand_profile.best_speed.speed - opponent_profile.average_speed, 0) * 0.3
            elif effect_key == "modify_self_block" or (
                effect.effect_type == "modify_total_stat" and effect.target == "self_total" and effect.stat == "block"
            ):
                score += max(opponent_profile.average_attack - hand_profile.best_block.block, 0) * 0.35
            elif effect_key == "modify_opponent_attack" or (
                effect.effect_type == "modify_total_stat" and effect.target == "opponent_total" and effect.stat == "attack"
            ):
                block_shortfall = max(single_card_threat.attack - hand_profile.best_block.block, 0)
                score += block_shortfall * 0.9
                score += max(double_card_threat.attack - hand_profile.best_block.block, 0) * 0.25
            elif effect_key == "negate_opponent_first_card" or effect.effect_type == "negate_card":
                score += max(single_card_threat.attack, 0) * 0.5
                score += max(single_card_threat.block, 0) * 0.18
                score += max(single_card_threat.speed, 0) * 0.3
                if hand_profile.best_attack.attack > opponent_profile.average_block:
                    score += 0.45
            elif effect.effect_type == "modify_rule_value" and effect.stat == "draw_per_turn":
                score += 1.2 * max(effect.value, 0)
        score += self._custom_control_score(view, card, hand_profile, opponent_profile)
        return round(score, 4)

    def _custom_control_score(self, view: PlayerView, card: Card, hand_profile: HandProfile, opponent_profile) -> float:
        score = 0.0
        if card.id == "control_blessing_flip":
            if view.opponent_blessing_zone is not None and view.opponent_blessing_face_up:
                score += 1.4
            elif view.own_blessing_zone is not None and not view.own_blessing_face_up:
                score += 1.1
        elif card.id == "control_blessing_break":
            if view.opponent_blessing_zone is not None:
                score += 1.6
            elif view.own_blessing_zone is not None and not view.own_blessing_face_up:
                score += 0.8
        elif card.id == "control_topdeck_hand":
            score += 1.4 if len(view.hand) <= 3 else 0.7
        elif card.id == "control_redraw_hand":
            weak_cards = sum(
                1
                for hand_card in view.hand
                if hand_card.type != "control"
                and (hand_card.attack + hand_card.block + hand_card.speed) <= 1
            )
            score += weak_cards * 0.35
        elif card.id == "control_discard_facedown_blessing":
            if view.own_blessing_zone is not None and not view.own_blessing_face_up:
                score += 1.5
        elif card.id == "control_defile":
            if view.opponent_blessing_zone is not None and view.opponent_blessing_face_up:
                score += 1.7
        elif card.id == "control_blessing_lock":
            if view.opponent_blessing_zone is not None and view.opponent_blessing_face_up:
                score += 1.8
        elif card.id == "control_opening_read":
            score += 0.8
        elif card.id == "control_hand_echo":
            score += 0.9 if view.opponent_hand_count > 0 else 0.0
        elif card.id == "control_all_in_focus":
            score += 1.2 if hand_profile.best_attack.attack > opponent_profile.average_block else 0.4
        elif card.id == "control_opening_expose":
            score += 0.7
        elif card.id in {"control_peek_opponent_top", "control_peek_own_top", "control_peek_hand"}:
            score += self.style.reveal_weight * 0.8
        score += self._archetype_control_bonus(view, card, hand_profile, opponent_profile)
        return score

    def _archetype_hand_bonus(self, view: PlayerView, card: Card, hand_profile: HandProfile, opponent_profile) -> float:
        return 0.0

    def _archetype_control_bonus(self, view: PlayerView, card: Card, hand_profile: HandProfile, opponent_profile) -> float:
        return 0.0

    def _legal_actions(self, view: PlayerView) -> list[BattleAction]:
        battles = [card for card in view.hand if card.type in {"battle", "control"}]
        legal_slots = max(0, view.opponent_facedown_count + 1 - view.own_facedown_count)
        actions = [] if self._must_avoid_empty_or_control_only_pass(view) else [BattleAction("pass")]
        if legal_slots <= 0 or not battles:
            return actions or [BattleAction("pass")]
        forbid_set_pass = self._should_forbid_opening_set_pass(view)
        for card in battles:
            if not forbid_set_pass:
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

    def _score_action(self, view: PlayerView, action: BattleAction, mode: str) -> float:
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
        closing_opponent_line = self._estimated_closing_opponent_line(view, opponent_profile, own_after).add(opp_delta)
        attack_margin = own_line.attack - opponent_line.block
        block_margin = own_line.block - opponent_line.attack
        speed_margin = own_line.speed - opponent_line.speed
        remaining = [
            card
            for card in view.hand
            if card.type in {"battle", "control"} and card.id not in action.card_ids
        ]
        future = build_hand_profile(remaining)

        if mode == "attack":
            score = self._score_attack_action(
                view,
                action,
                selected_cards,
                own_line,
                opponent_line,
                closing_opponent_line,
                attack_margin,
                block_margin,
                speed_margin,
                future,
            )
        elif mode == "defense":
            score = self._score_defense_action(
                view,
                action,
                selected_cards,
                own_line,
                opponent_line,
                closing_opponent_line,
                attack_margin,
                block_margin,
                speed_margin,
                future,
            )
        else:
            score = self._score_probe_action(
                view,
                action,
                selected_cards,
                own_line,
                opponent_line,
                closing_opponent_line,
                attack_margin,
                block_margin,
                speed_margin,
                future,
            )
        score += self._archetype_action_bonus(
            view,
            action,
            selected_cards,
            mode,
            own_line,
            opponent_line,
            closing_opponent_line,
            attack_margin,
            block_margin,
            speed_margin,
            future,
        )
        return round(score, 4)

    def _archetype_action_bonus(
        self,
        view: PlayerView,
        action: BattleAction,
        selected_cards: list[Card],
        mode: str,
        own_line: StatLine,
        opponent_line: StatLine,
        closing_opponent_line: StatLine,
        attack_margin: float,
        block_margin: float,
        speed_margin: float,
        future: HandProfile,
    ) -> float:
        return 0.0

    def _choose_battle_mode(self, view: PlayerView) -> str:
        if self._is_probe_state(view):
            return "probe"

        opponent_profile = public_view_profile(view, self.cards_by_id, owner="opponent")
        current_cards = list(view.own_set_cards)
        current_line, opp_delta = combined_battle_line(
            current_cards,
            own_control=view.own_control_card,
            opponent_control=view.opponent_control_card,
        )
        current_opponent_line = self._estimated_opponent_line(view, opponent_profile, len(current_cards), "pass").add(opp_delta)
        hand_profile = build_hand_profile(view.hand)

        can_block_with_hand = current_line.block + hand_profile.best_block.block >= current_opponent_line.attack
        can_attack_with_hand = current_line.attack + hand_profile.best_attack.attack > current_opponent_line.block
        can_speed_with_hand = current_line.speed + hand_profile.best_speed.speed >= current_opponent_line.speed

        if view.opponent_battle_passed:
            return "attack" if can_attack_with_hand and (can_speed_with_hand or current_line.block >= current_opponent_line.attack) else "defense"

        if current_opponent_line.attack > current_line.block and can_block_with_hand:
            return "defense"

        if view.opponent_facedown_count > view.own_facedown_count and can_block_with_hand and not can_attack_with_hand:
            return "defense"

        if can_attack_with_hand and (can_speed_with_hand or hand_profile.best_attack.attack - current_opponent_line.block >= 2):
            if self.style.attack_weight >= self.style.block_weight or current_opponent_line.attack <= current_line.block:
                return "attack"

        if self.style.block_weight > self.style.attack_weight and can_block_with_hand:
            return "defense"
        return "probe"

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
        return self._estimate_opponent_threat_line(view, opponent_profile, final_count)

    def _estimated_closing_opponent_line(self, view: PlayerView, opponent_profile, own_after: int) -> StatLine:
        if view.opponent_battle_passed:
            final_count = view.opponent_facedown_count
        else:
            legal_slots = max(0, own_after + 1 - view.opponent_facedown_count)
            final_count = view.opponent_facedown_count + legal_slots
        return self._estimate_opponent_threat_line(view, opponent_profile, final_count)

    def _build_prediction_summary(self, view: PlayerView, action: BattleAction, mode: str) -> dict[str, Any]:
        selected_cards = [self.cards_by_id[card_id] for card_id in action.card_ids]
        own_after = len(view.own_set_cards) + len(selected_cards)
        opponent_profile = public_view_profile(view, self.cards_by_id, owner="opponent")
        own_line, opp_delta = combined_battle_line(
            list(view.own_set_cards) + selected_cards,
            own_control=view.own_control_card,
            opponent_control=view.opponent_control_card,
        )
        opponent_line = self._estimated_opponent_line(view, opponent_profile, own_after, action.action_type).add(opp_delta)
        closing_line = self._estimated_closing_opponent_line(view, opponent_profile, own_after).add(opp_delta)
        attack_margin = own_line.attack - opponent_line.block
        block_margin = own_line.block - opponent_line.attack
        speed_margin = own_line.speed - opponent_line.speed
        return {
            "predicted_style": self._classify_style(opponent_line),
            "predicted_line": self._line_to_dict(opponent_line),
            "predicted_closing_style": self._classify_style(closing_line),
            "predicted_closing_line": self._line_to_dict(closing_line),
            "public_profile_style": self._classify_profile(opponent_profile),
            "response_plan": self._response_plan(mode, attack_margin, block_margin, speed_margin),
            "mode": mode,
            "own_line": self._line_to_dict(own_line),
            "margins": {
                "attack": round(attack_margin, 2),
                "block": round(block_margin, 2),
                "speed": round(speed_margin, 2),
            },
        }

    def _classify_style(self, line: StatLine) -> str:
        values = {"attack": line.attack, "defense": line.block, "speed": line.speed}
        highest = max(values.values())
        if highest <= 0:
            return "none"
        leaders = [name for name, value in values.items() if value == highest]
        if len(leaders) != 1:
            return "balanced"
        return leaders[0]

    def _classify_profile(self, profile) -> str:
        values = {
            "attack": profile.average_attack,
            "defense": profile.average_block,
            "speed": profile.average_speed,
        }
        highest = max(values.values())
        if highest <= 0:
            return "none"
        leaders = [name for name, value in values.items() if value == highest]
        if len(leaders) != 1:
            return "balanced"
        return leaders[0]

    def _response_plan(self, mode: str, attack_margin: float, block_margin: float, speed_margin: float) -> str:
        if mode == "probe":
            return "probe"
        if mode == "attack":
            if attack_margin > 0 and speed_margin >= 0:
                return "speed_race"
            if attack_margin > 0 and block_margin >= 0:
                return "pressure_with_cover"
            return "attack_push"
        if block_margin >= 0 and attack_margin > -1:
            return "guard_and_counter"
        if block_margin >= 0:
            return "full_guard"
        return "minimal_guard"

    def _line_to_dict(self, line: StatLine) -> dict[str, int]:
        return {"attack": line.attack, "block": line.block, "speed": line.speed}

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
            if self._is_opening_set_pass_penalty_case(view):
                return -3.0
            if attack_margin > 0 and (speed_margin >= 0 or block_margin >= 0):
                return 1.6
            if view.opponent_battle_passed and attack_margin <= 0 and block_margin < 0:
                return -1.5
            return 0.45
        bonus = 0.35
        if self._is_opening_set_case(view, action):
            bonus += 0.9
        if view.opponent_battle_passed and attack_margin > 0:
            bonus -= 0.6
        if view.opponent_facedown_count > view.own_facedown_count:
            bonus += 0.45
        return bonus

    def _score_attack_action(
        self,
        view: PlayerView,
        action: BattleAction,
        selected_cards: list[Card],
        own_line: StatLine,
        opponent_line: StatLine,
        closing_opponent_line: StatLine,
        attack_margin: float,
        block_margin: float,
        speed_margin: float,
        future: HandProfile,
    ) -> float:
        own_after_count = len(view.own_set_cards) + len(selected_cards)
        closing_attack_margin = own_line.attack - closing_opponent_line.block
        closing_block_margin = own_line.block - closing_opponent_line.attack
        closing_speed_margin = own_line.speed - closing_opponent_line.speed
        score = (
            attack_margin * self.style.attack_weight * 1.55
            + speed_margin * self.style.speed_weight * 1.05
            + max(block_margin, 0) * self.style.block_weight * 0.3
        )
        score -= len(selected_cards) * self.style.risk_penalty
        score -= self._selected_card_value(selected_cards) * 0.06
        score += self._action_shape_bonus(view, action, attack_margin, block_margin, speed_margin)
        if action.action_type == "set":
            score += future.best_attack.attack * 0.12 * self.style.continuation_weight
            score += future.best_speed.speed * 0.08 * self.style.continuation_weight
            if own_after_count == view.opponent_facedown_count + 1 and not view.opponent_battle_passed:
                score += 0.7
        if view.opponent_battle_passed and attack_margin > 0:
            score += 1.1
        if action.action_type == "set_pass":
            score += self._set_pass_closing_bonus(
                view,
                own_after_count=own_after_count,
                own_attack=own_line.attack,
                own_block=own_line.block,
                own_speed=own_line.speed,
                closing_attack_margin=closing_attack_margin,
                closing_block_margin=closing_block_margin,
                closing_speed_margin=closing_speed_margin,
            )
        if action.action_type == "pass":
            score += self._pass_closing_bonus(
                view,
                own_attack=own_line.attack,
                own_block=own_line.block,
                own_speed=own_line.speed,
                closing_attack_margin=closing_attack_margin,
                closing_block_margin=closing_block_margin,
                closing_speed_margin=closing_speed_margin,
            )
        return score

    def _score_defense_action(
        self,
        view: PlayerView,
        action: BattleAction,
        selected_cards: list[Card],
        own_line: StatLine,
        opponent_line: StatLine,
        closing_opponent_line: StatLine,
        attack_margin: float,
        block_margin: float,
        speed_margin: float,
        future: HandProfile,
    ) -> float:
        overblock = max(own_line.block - opponent_line.attack, 0)
        own_after_count = len(view.own_set_cards) + len(selected_cards)
        closing_attack_margin = own_line.attack - closing_opponent_line.block
        closing_block_margin = own_line.block - closing_opponent_line.attack
        closing_speed_margin = own_line.speed - closing_opponent_line.speed
        score = block_margin * self.style.block_weight * 1.8
        if block_margin >= 0:
            score += 2.4
        score -= overblock * 0.45
        score -= len(selected_cards) * max(self.style.risk_penalty, 0.55)
        score -= self._selected_card_value(selected_cards) * 0.12
        score += future.best_attack.attack * 0.2 * self.style.continuation_weight
        score += future.best_speed.speed * 0.12 * self.style.continuation_weight
        if action.action_type == "pass":
            score += 1.8 if view.own_facedown_count > 0 and block_margin >= 0 else -2.2
            score += self._pass_closing_bonus(
                view,
                own_attack=own_line.attack,
                own_block=own_line.block,
                own_speed=own_line.speed,
                closing_attack_margin=closing_attack_margin,
                closing_block_margin=closing_block_margin,
                closing_speed_margin=closing_speed_margin,
            )
        if action.action_type == "set_pass" and not view.opponent_battle_passed:
            score -= 1.6
            score += self._set_pass_closing_bonus(
                view,
                own_after_count=own_after_count,
                own_attack=own_line.attack,
                own_block=own_line.block,
                own_speed=own_line.speed,
                closing_attack_margin=closing_attack_margin,
                closing_block_margin=closing_block_margin,
                closing_speed_margin=closing_speed_margin,
            )
        if action.action_type == "set":
            score += 0.55 if len(selected_cards) == 1 else -0.2
            if own_after_count == view.opponent_facedown_count + 1 and not view.opponent_battle_passed:
                score += 0.5
        return score

    def _score_probe_action(
        self,
        view: PlayerView,
        action: BattleAction,
        selected_cards: list[Card],
        own_line: StatLine,
        opponent_line: StatLine,
        closing_opponent_line: StatLine,
        attack_margin: float,
        block_margin: float,
        speed_margin: float,
        future: HandProfile,
    ) -> float:
        score = 0.0
        if action.action_type == "set":
            score += 2.9 if len(selected_cards) == 1 else 1.0
            if len(view.own_set_cards) + len(selected_cards) == view.opponent_facedown_count + 1 and not view.opponent_battle_passed:
                score += 0.8
        elif action.action_type == "set_pass":
            score -= 2.4
        else:
            score -= 2.2
        score -= self._selected_card_value(selected_cards) * 0.08
        score += max(own_line.block, 0) * 0.25
        score += max(own_line.speed, 0) * 0.22
        score += future.best_attack.attack * 0.22 * self.style.continuation_weight
        score += future.best_speed.speed * 0.16 * self.style.continuation_weight
        if view.opponent_battle_passed:
            score -= 0.8
        if action.action_type == "set_pass":
            score += self._set_pass_closing_bonus(
                view,
                own_after_count=len(view.own_set_cards) + len(selected_cards),
                own_attack=own_line.attack,
                own_block=own_line.block,
                own_speed=own_line.speed,
                closing_attack_margin=own_line.attack - closing_opponent_line.block,
                closing_block_margin=own_line.block - closing_opponent_line.attack,
                closing_speed_margin=own_line.speed - closing_opponent_line.speed,
            )
        if action.action_type == "pass":
            score += self._pass_closing_bonus(
                view,
                own_attack=own_line.attack,
                own_block=own_line.block,
                own_speed=own_line.speed,
                closing_attack_margin=own_line.attack - closing_opponent_line.block,
                closing_block_margin=own_line.block - closing_opponent_line.attack,
                closing_speed_margin=own_line.speed - closing_opponent_line.speed,
            )
        return score

    def _should_forbid_opening_set_pass(self, view: PlayerView) -> bool:
        return self._is_opening_set_pass_penalty_case(view)

    def _is_opening_set_pass_penalty_case(self, view: PlayerView) -> bool:
        return (
            view.own_facedown_count == 0
            and view.opponent_facedown_count == 0
            and view.acting_player == view.battle_starting_player
            and view.turn == 1
            and not view.opponent_battle_passed
        )

    def _is_opening_set_case(self, view: PlayerView, action: BattleAction) -> bool:
        return (
            action.action_type == "set"
            and view.own_facedown_count == 0
            and view.opponent_facedown_count == 0
            and view.acting_player == view.battle_starting_player
            and not view.opponent_battle_passed
        )

    def _is_probe_state(self, view: PlayerView) -> bool:
        return (
            view.own_facedown_count == 0
            and view.opponent_facedown_count == 0
            and not view.opponent_battle_passed
        )

    def _selected_card_value(self, cards: list[Card]) -> float:
        value = 0.0
        for card in cards:
            value += max(card.attack, 0) * 0.8
            value += max(card.block, 0) * 0.6
            value += max(card.speed, 0) * 0.55
            value += self._effect_score(card.effects)
        return value

    def _estimate_opponent_threat_line(self, view: PlayerView, opponent_profile, final_count: int) -> StatLine:
        if final_count <= 0:
            return StatLine()
        public_remaining = battle_cards(
            remaining_public_cards(
                view.opponent_public_deck,
                list(view.opponent_used) + list(view.opponent_discard),
                self.cards_by_id,
                current_control=view.opponent_control_card,
            )
        )
        hidden_candidates = self._estimate_opponent_hidden_candidates(view)
        hand_cap = max(0, view.opponent_hand_count - len(public_remaining))

        attack_value = self._estimate_weighted_top_stat(
            public_remaining,
            hidden_candidates,
            stat_name="attack",
            final_count=final_count,
            hidden_cap=hand_cap,
        )
        block_value = self._estimate_weighted_top_stat(
            public_remaining,
            hidden_candidates,
            stat_name="block",
            final_count=final_count,
            hidden_cap=hand_cap,
        )
        speed_value = self._estimate_weighted_top_stat(
            public_remaining,
            hidden_candidates,
            stat_name="speed",
            final_count=final_count,
            hidden_cap=hand_cap,
        )
        return StatLine(
            attack=round(attack_value),
            block=round(block_value),
            speed=round(speed_value),
        )

    def _estimate_opponent_hidden_candidates(self, view: PlayerView) -> list[tuple[Card, float]]:
        pool_counts = {entry.card_id: entry.count for entry in self.card_pool.entries}
        own_counts = {}
        for card_id in view.own_public_deck + view.own_hidden_deck:
            own_counts[card_id] = own_counts.get(card_id, 0) + 1
        opponent_public_counts = {}
        for card_id in view.opponent_public_deck:
            opponent_public_counts[card_id] = opponent_public_counts.get(card_id, 0) + 1

        residual_counts = dict(pool_counts)
        for card_id, count in own_counts.items():
            residual_counts[card_id] = max(0, residual_counts.get(card_id, 0) - count)
        for card_id, count in opponent_public_counts.items():
            residual_counts[card_id] = max(0, residual_counts.get(card_id, 0) - count)

        observed_counts = {}
        for card in list(view.opponent_used) + list(view.opponent_discard):
            observed_counts[card.id] = observed_counts.get(card.id, 0) + 1

        for card_id, observed in observed_counts.items():
            public_seen = min(observed, opponent_public_counts.get(card_id, 0))
            hidden_seen = max(0, observed - public_seen)
            residual_counts[card_id] = max(0, residual_counts.get(card_id, 0) - hidden_seen)

        inferred_total_cards = (
            view.opponent_hand_count
            + view.opponent_deck_count
            + len(view.opponent_discard)
            + len(view.opponent_used)
            + view.opponent_facedown_count
        )
        hidden_slots = max(0, inferred_total_cards - len(view.opponent_public_deck))
        residual_total = sum(residual_counts.values())
        if hidden_slots == 0 or residual_total == 0:
            return []

        expected_scale = hidden_slots / residual_total
        weighted: list[tuple[Card, float]] = []
        for card_id, count in residual_counts.items():
            if count <= 0:
                continue
            card = self.cards_by_id[card_id]
            if card.type != "battle":
                continue
            weight = count * expected_scale
            weight *= self._public_preference_weight(view, card)
            weighted.append((card, weight))
        return weighted

    def _public_preference_weight(self, view: PlayerView, candidate: Card) -> float:
        events = view.opponent_deck_metadata.get("public_draft_events", [])
        if not isinstance(events, list) or not events:
            return 1.0
        weight = 1.0
        candidate_role = infer_role_color(candidate)
        opponent_id = "p2" if view.player_id == "p1" else "p1"
        for event in events:
            if event.get("player_id") != opponent_id:
                continue
            picked_id = event.get("picked_card_id")
            offer_ids = event.get("offer_card_ids", [])
            if not isinstance(picked_id, str) or not isinstance(offer_ids, list):
                continue
            picked_card = self.cards_by_id.get(picked_id)
            if picked_card is None:
                continue
            picked_role = infer_role_color(picked_card)
            if candidate.id == picked_id:
                weight *= 0.7
                continue
            if candidate_role == picked_role:
                weight *= 1.12
            if candidate.type == picked_card.type:
                weight *= 1.05
            if self._shares_preference_axis(candidate, picked_card):
                weight *= 1.08
            if candidate.id in offer_ids:
                weight *= 0.88
            else:
                for declined_id in offer_ids:
                    declined_card = self.cards_by_id.get(declined_id)
                    if declined_card is None or declined_id == picked_id:
                        continue
                    if candidate.id == declined_id:
                        weight *= 0.82
                    elif infer_role_color(declined_card) == candidate_role and candidate.type == declined_card.type:
                        weight *= 0.96
        return max(weight, 0.2)

    def _shares_preference_axis(self, left: Card, right: Card) -> bool:
        if left.attack >= 4 and right.attack >= 4:
            return True
        if left.block >= 3 and right.block >= 3:
            return True
        if left.speed >= 3 and right.speed >= 3:
            return True
        if any(tag in right.tags for tag in left.tags):
            return True
        return False

    def _estimate_weighted_top_stat(
        self,
        public_remaining: list[Card],
        hidden_candidates: list[tuple[Card, float]],
        *,
        stat_name: str,
        final_count: int,
        hidden_cap: int,
    ) -> float:
        score_key = {
            "attack": lambda card: getattr(card, "attack") * 1.2 + card.speed * 0.45 + card.block * 0.15,
            "block": lambda card: getattr(card, "block") * 1.2 + card.speed * 0.3 + card.attack * 0.15,
            "speed": lambda card: getattr(card, "speed") * 1.2 + card.attack * 0.45 + card.block * 0.15,
        }[stat_name]
        exact_cards = sorted(public_remaining, key=score_key, reverse=True)
        remaining_slots = final_count
        total_value = 0.0

        for card in exact_cards[:final_count]:
            total_value += getattr(card, stat_name)
            remaining_slots -= 1
        if remaining_slots <= 0 or hidden_cap <= 0:
            return total_value

        weighted_cards = sorted(hidden_candidates, key=lambda item: score_key(item[0]), reverse=True)
        hidden_used = 0.0
        for card, weight in weighted_cards:
            if hidden_used >= min(remaining_slots, hidden_cap):
                break
            take = min(weight, min(remaining_slots, hidden_cap) - hidden_used)
            total_value += getattr(card, stat_name) * take
            hidden_used += take
        if hidden_used < min(remaining_slots, hidden_cap):
            total_value += (min(remaining_slots, hidden_cap) - hidden_used) * max(getattr(exact_cards[-1], stat_name), 0) if exact_cards else 0
        return total_value

    def _set_pass_closing_bonus(
        self,
        view: PlayerView,
        *,
        own_after_count: int,
        own_attack: int,
        own_block: int,
        own_speed: int,
        closing_attack_margin: float,
        closing_block_margin: float,
        closing_speed_margin: float,
    ) -> float:
        if view.opponent_battle_passed:
            return 1.2 if closing_attack_margin > 0 or closing_block_margin >= 0 else -1.0

        score = 0.0
        if own_after_count <= 2:
            score -= 1.6
            if view.turn == 1:
                score -= 0.8
        elif own_after_count == 3:
            score += 0.2

        if closing_attack_margin > 0 and (closing_speed_margin >= 0 or closing_block_margin >= 0):
            score += 2.2
        elif closing_block_margin >= 0 and closing_speed_margin >= -1:
            score += 1.0
        else:
            score -= 2.0
        attack_risk = self._estimate_opponent_stat_probability(view, "attack", own_block)
        speed_risk = self._estimate_opponent_stat_probability(view, "speed", own_speed)
        block_risk = self._estimate_opponent_stat_probability(view, "block", max(own_attack - 1, 0))
        score -= attack_risk * 1.2
        score -= speed_risk * 0.6
        score -= block_risk * 0.4
        return score

    def _pass_closing_bonus(
        self,
        view: PlayerView,
        *,
        own_attack: int,
        own_block: int,
        own_speed: int,
        closing_attack_margin: float,
        closing_block_margin: float,
        closing_speed_margin: float,
    ) -> float:
        if view.opponent_battle_passed:
            return 1.0 if closing_attack_margin >= 0 or closing_block_margin >= 0 else -0.8

        score = 0.0
        if (
            view.own_facedown_count == 1
            and view.opponent_facedown_count == 1
            and view.turn == 1
            and view.acting_player == view.battle_starting_player
        ):
            score -= 2.2
        if closing_attack_margin > 0 and (closing_speed_margin >= 0 or closing_block_margin >= 0):
            score += 0.7
        elif closing_block_margin >= 0:
            score += 0.2
        else:
            score -= 1.8
        attack_risk = self._estimate_opponent_stat_probability(view, "attack", own_block)
        speed_risk = self._estimate_opponent_stat_probability(view, "speed", own_speed)
        score -= attack_risk * 1.5
        score -= speed_risk * 0.7
        return score

    def _estimate_opponent_stat_probability(self, view: PlayerView, stat_name: str, threshold: int) -> float:
        public_remaining = battle_cards(
            remaining_public_cards(
                view.opponent_public_deck,
                list(view.opponent_used) + list(view.opponent_discard),
                self.cards_by_id,
                current_control=view.opponent_control_card,
            )
        )
        hidden_candidates = self._estimate_opponent_hidden_candidates(view)
        total_weight = len(public_remaining) + sum(weight for _, weight in hidden_candidates)
        if total_weight <= 0 or view.opponent_hand_count <= 0:
            return 0.0
        threat_weight = sum(1 for card in public_remaining if getattr(card, stat_name) > threshold)
        threat_weight += sum(weight for card, weight in hidden_candidates if getattr(card, stat_name) > threshold)
        p = min(max(threat_weight / total_weight, 0.0), 1.0)
        draws = min(view.opponent_hand_count, max(1, round(total_weight)))
        return 1.0 - ((1.0 - p) ** draws)

    def _effect_score(self, effects: tuple[Effect, ...]) -> float:
        score = 0.0
        for effect in effects:
            if effect.kind in {"modify_self_attack", "modify_opponent_block"} or (
                effect.effect_type == "modify_total_stat" and (
                    (effect.target == "self_total" and effect.stat == "attack")
                    or (effect.target == "opponent_total" and effect.stat == "block")
                )
            ):
                score += abs(effect.value) * 0.45
            elif effect.kind in {"modify_self_block", "modify_opponent_attack"} or (
                effect.effect_type == "modify_total_stat" and (
                    (effect.target == "self_total" and effect.stat == "block")
                    or (effect.target == "opponent_total" and effect.stat == "attack")
                )
            ):
                score += abs(effect.value) * 0.45
            elif effect.kind in {"modify_self_speed", "modify_opponent_speed"} or (
                effect.effect_type == "modify_total_stat" and effect.stat == "speed"
            ):
                score += abs(effect.value) * 0.3
            elif effect.kind == "negate_opponent_first_card" or effect.effect_type == "negate_card":
                score += 1.1
            elif effect.kind == "draw_cards" or effect.effect_type == "draw_cards":
                score += 0.9
            elif effect.effect_type == "modify_rule_value" and effect.stat == "draw_per_turn":
                score += abs(effect.value) * 1.0
            elif effect.kind == "reveal_opponent_hand_random":
                score += self.style.reveal_weight
            elif effect.effect_type == "reveal_cards":
                score += self.style.reveal_weight * 0.8
        return score


class StandardBot(PublicInfoBot):
    name = "StandardBot"

    def _archetype_control_bonus(self, view: PlayerView, card: Card, hand_profile: HandProfile, opponent_profile) -> float:
        if card.id in BLESSING_HATE_CONTROL_IDS and view.opponent_blessing_zone is not None:
            return 1.05 if view.opponent_blessing_face_up else 0.7
        return 0.0


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

    def _choose_battle_mode(self, view: PlayerView) -> str:
        mode = super()._choose_battle_mode(view)
        if mode != "probe":
            return mode
        opponent_profile = public_view_profile(view, self.cards_by_id, owner="opponent")
        current_cards = list(view.own_set_cards)
        current_line, opp_delta = combined_battle_line(
            current_cards,
            own_control=view.own_control_card,
            opponent_control=view.opponent_control_card,
        )
        current_opponent_line = self._estimated_opponent_line(view, opponent_profile, len(current_cards), "pass").add(opp_delta)
        hand_profile = build_hand_profile(view.hand)
        can_attack = current_line.attack + hand_profile.best_attack.attack > current_opponent_line.block
        can_speed = current_line.speed + hand_profile.best_speed.speed >= current_opponent_line.speed - 1
        if can_attack and (can_speed or hand_profile.best_attack.attack >= current_opponent_line.block + 1):
            return "attack"
        return mode

    def _archetype_hand_bonus(self, view: PlayerView, card: Card, hand_profile: HandProfile, opponent_profile) -> float:
        score = 0.0
        if card.type == "control" and card.id in AGGRO_PRIORITY_CONTROL_IDS:
            score += 1.1
        if card.type == "control":
            for effect in card.effects:
                if effect.kind in {"modify_self_attack", "modify_self_speed", "modify_opponent_block"}:
                    score += 0.7 + abs(effect.value) * 0.18
        return score

    def _archetype_control_bonus(self, view: PlayerView, card: Card, hand_profile: HandProfile, opponent_profile) -> float:
        score = 0.0
        if card.id in AGGRO_PRIORITY_CONTROL_IDS:
            score += 1.25
        for effect in card.effects:
            if effect.kind in {"modify_self_attack", "modify_self_speed", "modify_opponent_block"}:
                score += 0.95 + abs(effect.value) * 0.22
            elif effect.kind == "modify_opponent_speed":
                score += 0.35 + abs(effect.value) * 0.1
        if card.id in BLESSING_HATE_CONTROL_IDS and view.opponent_blessing_zone is not None:
            score += 0.45 if view.opponent_blessing_face_up else 0.25
        return score

    def _archetype_action_bonus(
        self,
        view: PlayerView,
        action: BattleAction,
        selected_cards: list[Card],
        mode: str,
        own_line: StatLine,
        opponent_line: StatLine,
        closing_opponent_line: StatLine,
        attack_margin: float,
        block_margin: float,
        speed_margin: float,
        future: HandProfile,
    ) -> float:
        score = 0.0
        lethal_line = attack_margin > 0 and (speed_margin >= 0 or block_margin >= 0)
        if mode == "attack":
            score += max(speed_margin, 0) * 0.7
            score += max(attack_margin, 0) * 0.6
            score += max(own_line.speed, 0) * 0.2
            if lethal_line:
                score += 1.8
                score += 0.7 / max(1, len(selected_cards))
        elif mode == "probe" and action.action_type != "pass":
            score += max(own_line.speed, 0) * 0.12
        if any(card.type == "control" for card in selected_cards):
            for card in selected_cards:
                if card.type != "control":
                    continue
                if card.id in AGGRO_PRIORITY_CONTROL_IDS:
                    score += 0.9
                if any(effect.kind in {"modify_self_attack", "modify_self_speed", "modify_opponent_block"} for effect in card.effects):
                    score += 0.8
        if action.action_type == "set" and len(selected_cards) == 2 and mode == "attack":
            score += 0.5
        if action.action_type == "pass":
            score -= 1.5
            if mode in {"attack", "probe"}:
                score -= 2.2
            if view.own_facedown_count == 0 or self._control_only_set_cards(view):
                score -= 2.8
        if mode == "attack" and action.action_type in {"set", "set_pass"} and selected_cards:
            fastest = max(card.speed for card in selected_cards)
            strongest = sum(max(card.attack, 0) for card in selected_cards)
            score += fastest * 0.35
            score += strongest * 0.18
        return score


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

    def _archetype_control_bonus(self, view: PlayerView, card: Card, hand_profile: HandProfile, opponent_profile) -> float:
        if card.id in BLESSING_HATE_CONTROL_IDS and view.opponent_blessing_zone is not None:
            return 1.55 if view.opponent_blessing_face_up else 1.1
        return 0.0


class ControlBot(PublicInfoBot):
    name = "ControlBot"
    style = StyleProfile(
        attack_weight=0.7,
        block_weight=1.1,
        speed_weight=0.9,
        control_weight=1.45,
        reveal_weight=1.15,
        risk_penalty=0.75,
        continuation_weight=0.6,
        noise=0.16,
    )

    def _archetype_hand_bonus(self, view: PlayerView, card: Card, hand_profile: HandProfile, opponent_profile) -> float:
        score = 0.0
        if card.type == "control":
            score += 0.9
            if card.id in CONTROL_FOCUS_IDS:
                score += 0.9
        elif card.type == "battle":
            if card.attack >= 4 and card.block <= 0:
                score -= 0.8
            if card.block >= 2 or card.speed >= 1:
                score += 0.3
        return score

    def _archetype_control_bonus(self, view: PlayerView, card: Card, hand_profile: HandProfile, opponent_profile) -> float:
        score = 0.0
        if card.id in CONTROL_FOCUS_IDS:
            score += 1.15
        if card.id in BLESSING_HATE_CONTROL_IDS and view.opponent_blessing_zone is not None:
            score += 1.0 if view.opponent_blessing_face_up else 0.7
        if any(effect.kind in {"draw_cards", "reveal_opponent_hand_random"} for effect in card.effects):
            score += 0.5
        return score

    def _archetype_action_bonus(
        self,
        view: PlayerView,
        action: BattleAction,
        selected_cards: list[Card],
        mode: str,
        own_line: StatLine,
        opponent_line: StatLine,
        closing_opponent_line: StatLine,
        attack_margin: float,
        block_margin: float,
        speed_margin: float,
        future: HandProfile,
    ) -> float:
        score = 0.0
        battle_count = sum(1 for card in selected_cards if card.type == "battle")
        control_count = sum(1 for card in selected_cards if card.type == "control")
        if control_count > 0 and battle_count > 0:
            score += 0.9
        if control_count > 0 and battle_count == 0:
            score -= 1.2
        if mode == "defense" and control_count > 0:
            score += 0.6
        return score


class BlessingBot(PublicInfoBot):
    name = "BlessingBot"
    style = StyleProfile(
        attack_weight=0.8,
        block_weight=1.0,
        speed_weight=0.85,
        control_weight=1.35,
        reveal_weight=0.9,
        risk_penalty=0.7,
        continuation_weight=0.5,
        noise=0.18,
    )

    def _archetype_hand_bonus(self, view: PlayerView, card: Card, hand_profile: HandProfile, opponent_profile) -> float:
        score = 0.0
        if card.type == "blessing":
            score += 1.6 if view.own_blessing_zone is None else 0.35
        if card.type == "control" and card.id in BLESSING_SUPPORT_CONTROL_IDS:
            score += 1.1
        return score

    def _archetype_control_bonus(self, view: PlayerView, card: Card, hand_profile: HandProfile, opponent_profile) -> float:
        score = 0.0
        if card.type == "blessing":
            score += 1.8 if view.own_blessing_zone is None else 0.2
        if card.id in BLESSING_SUPPORT_CONTROL_IDS:
            score += 1.45
        if card.id in BLESSING_HATE_CONTROL_IDS and view.opponent_blessing_zone is not None:
            score += 0.7 if view.opponent_blessing_face_up else 0.45
        return score

    def _archetype_action_bonus(
        self,
        view: PlayerView,
        action: BattleAction,
        selected_cards: list[Card],
        mode: str,
        own_line: StatLine,
        opponent_line: StatLine,
        closing_opponent_line: StatLine,
        attack_margin: float,
        block_margin: float,
        speed_margin: float,
        future: HandProfile,
    ) -> float:
        score = 0.0
        battle_count = sum(1 for card in selected_cards if card.type == "battle")
        control_count = sum(1 for card in selected_cards if card.type == "control")
        if control_count > 0 and battle_count > 0:
            score += 0.7
        if control_count > 0 and battle_count == 0:
            score -= 1.0
        return score
