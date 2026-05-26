from __future__ import annotations

from bots.base_bot import BaseBot
from engine.game_state import PlayerView


class TurtleBot(BaseBot):
    name = "TurtleBot"

    def choose_mulligan(self, view: PlayerView) -> list[str]:
        return [card.id for card in view.hand if card.type == "battle" and card.block <= 0]

    def choose_control_card(self, view: PlayerView) -> str | None:
        priority = ["control_fortify", "control_guard", "control_cover", "control_reserve", "control_disrupt"]
        for card_id in priority:
            for card in view.hand:
                if card.id == card_id:
                    return card.id
        return None

    def choose_battle_cards(self, view: PlayerView) -> list[str]:
        battles = [card for card in view.hand if card.type == "battle"]
        if not battles:
            return []
        selected = [card.id for card in battles if card.block >= 2]
        if selected:
            return selected
        return [max(battles, key=lambda card: (card.block, card.speed, card.attack)).id]
