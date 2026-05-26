from __future__ import annotations

from bots.base_bot import BaseBot
from engine.game_state import PlayerView


class DisruptBot(BaseBot):
    name = "DisruptBot"

    def choose_mulligan(self, view: PlayerView) -> list[str]:
        return [card.id for card in view.hand if card.type == "battle" and card.attack < 0 and card.block <= 1]

    def choose_control_card(self, view: PlayerView) -> str | None:
        priority = ["control_anchor", "control_pressure", "control_disrupt", "control_haste"]
        for card_id in priority:
            for card in view.hand:
                if card.id == card_id:
                    return card.id
        return None

    def choose_battle_cards(self, view: PlayerView) -> list[str]:
        battles = [card for card in view.hand if card.type == "battle"]
        if not battles:
            return []
        selected: list[str] = []
        for card in battles:
            lowers_block = any(effect.kind == "modify_opponent_block" for effect in card.effects)
            if lowers_block or (card.attack > 0 and card.speed >= 2):
                selected.append(card.id)
        if selected:
            return selected
        return [max(battles, key=lambda card: (card.speed, card.attack, card.block)).id]
