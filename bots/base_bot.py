from __future__ import annotations

from typing import Any

from dataclasses import dataclass, field

from engine.game_state import PlayerView


@dataclass(frozen=True)
class BattleAction:
    action_type: str
    card_ids: tuple[str, ...] = field(default_factory=tuple)


class BaseBot:
    name = "BaseBot"

    def choose_mulligan(self, view: PlayerView) -> list[str]:
        return []

    def choose_overflow_discards(self, view: PlayerView, overflow_count: int) -> list[str]:
        requested = self.choose_mulligan(view)
        return requested[:overflow_count]

    def choose_control_card(self, view: PlayerView) -> str | None:
        return None

    def choose_battle_action(self, view: PlayerView) -> BattleAction:
        selected = tuple(self.choose_battle_cards(view))
        if not selected:
            if self._must_avoid_empty_or_control_only_pass(view):
                fallback = self._fallback_set_card_id(view)
                if fallback is not None:
                    return BattleAction("set", (fallback,))
            return BattleAction("pass")
        if view.opponent_battle_passed or len(selected) == 1:
            return BattleAction("set_pass", selected[:1])
        return BattleAction("set", selected[:2])

    def choose_battle_cards(self, view: PlayerView) -> list[str]:
        selected = self.choose_battle_card(view)
        if selected is None:
            return []
        return [selected]

    def choose_battle_card(self, view: PlayerView) -> str | None:
        return next((card.id for card in view.hand if card.type in {"battle", "control"}), None)

    def consume_debug_info(self) -> dict[str, Any] | None:
        return None

    def _playable_battle_or_control_cards(self, view: PlayerView) -> list:
        return [card for card in view.hand if card.type in {"battle", "control"}]

    def _playable_battle_cards(self, view: PlayerView) -> list:
        return [card for card in view.hand if card.type == "battle"]

    def _control_only_set_cards(self, view: PlayerView) -> bool:
        return bool(view.own_set_cards) and all(card.type == "control" for card in view.own_set_cards)

    def _must_avoid_empty_or_control_only_pass(self, view: PlayerView) -> bool:
        legal_slots = max(0, view.opponent_facedown_count + 1 - view.own_facedown_count)
        if legal_slots <= 0:
            return False
        playable = self._playable_battle_or_control_cards(view)
        if not playable:
            return False
        if view.own_facedown_count == 0:
            return True
        if self._control_only_set_cards(view):
            return True
        return False

    def _fallback_set_card_id(self, view: PlayerView) -> str | None:
        battle = self._playable_battle_cards(view)
        if battle:
            return battle[0].id
        playable = self._playable_battle_or_control_cards(view)
        if playable:
            return playable[0].id
        return None
