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
        return next((card.id for card in view.hand if card.type == "battle"), None)

    def consume_debug_info(self) -> dict[str, Any] | None:
        return None
