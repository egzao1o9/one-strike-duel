from __future__ import annotations

from bots.base_bot import BaseBot
from engine.game_state import PlayerView


class BurstBot(BaseBot):
    name = "BurstBot"

    def choose_mulligan(self, view: PlayerView) -> list[str]:
        return [card.id for card in view.hand if card.type == "battle" and card.attack <= 0]

    def choose_control_card(self, view: PlayerView) -> str | None:
        priority = ["control_overclock", "control_pressure", "control_focus", "control_haste"]
        for card_id in priority:
            for card in view.hand:
                if card.id == card_id:
                    return card.id
        return None

    def choose_battle_cards(self, view: PlayerView) -> list[str]:
        battles = [card for card in view.hand if card.type == "battle"]
        if not battles:
            return []
        selected = [card.id for card in battles if card.attack >= 3]
        if selected:
            return selected
        selected = [card.id for card in battles if card.attack > 0 and card.speed >= 1]
        if selected:
            return selected
        best = max(battles, key=lambda card: (card.attack, card.speed, -card.block))
        return [best.id]
