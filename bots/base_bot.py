from __future__ import annotations

from engine.game_state import PlayerView


class BaseBot:
    name = "BaseBot"

    def choose_mulligan(self, view: PlayerView) -> list[str]:
        return []

    def choose_control_card(self, view: PlayerView) -> str | None:
        return None

    def choose_battle_cards(self, view: PlayerView) -> list[str]:
        selected = self.choose_battle_card(view)
        if selected is None:
            return []
        return [selected]

    def choose_battle_card(self, view: PlayerView) -> str | None:
        return next((card.id for card in view.hand if card.type == "battle"), None)
