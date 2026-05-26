from __future__ import annotations

from bots.base_bot import BaseBot
from engine.game_state import PlayerView


class TempoBot(BaseBot):
    name = "TempoBot"

    def choose_mulligan(self, view: PlayerView) -> list[str]:
        return [card.id for card in view.hand if card.type == "battle" and card.speed < 1 and card.attack <= 0]

    def choose_control_card(self, view: PlayerView) -> str | None:
        priority = ["control_haste", "control_cover", "control_anchor", "control_pressure", "control_momentum"]
        for card_id in priority:
            for card in view.hand:
                if card.id == card_id:
                    return card.id
        return None

    def choose_battle_cards(self, view: PlayerView) -> list[str]:
        battles = [card for card in view.hand if card.type == "battle"]
        if not battles:
            return []
        selected = [card.id for card in battles if card.speed >= 2 and card.attack >= 0]
        if selected:
            return selected
        selected = [card.id for card in battles if card.speed >= 3]
        if selected:
            return selected
        return [max(battles, key=lambda card: (card.speed, card.block, card.attack)).id]
