from __future__ import annotations

from bots.base_bot import BaseBot
from engine.game_state import PlayerView


class GreedyBot(BaseBot):
    name = "GreedyBot"

    def choose_control_card(self, view: PlayerView) -> str | None:
        for card in view.hand:
            if card.type == "control" and any(effect.kind == "modify_opponent_block" for effect in card.effects):
                return card.id
        return None

    def choose_battle_card(self, view: PlayerView) -> str | None:
        battles = [card for card in view.hand if card.type == "battle"]
        if not battles:
            return None
        estimated_block = max((card.block for card in view.opponent_used if card.type == "battle"), default=2)
        winning_cards = [card for card in battles if card.attack > estimated_block]
        if winning_cards:
            winning_cards.sort(key=lambda card: (card.attack, card.speed), reverse=True)
            return winning_cards[0].id
        battles.sort(key=lambda card: (card.attack + card.speed, card.attack), reverse=True)
        return battles[0].id

    def choose_battle_cards(self, view: PlayerView) -> list[str]:
        battles = [card for card in view.hand if card.type == "battle"]
        if not battles:
            return []
        estimated_block = max((card.block for card in view.opponent_used if card.type == "battle"), default=2)
        total_attack = 0
        selected: list[str] = []
        for card in sorted(battles, key=lambda item: (item.attack, item.speed), reverse=True):
            selected.append(card.id)
            total_attack += card.attack
            if total_attack > estimated_block:
                return selected
        return selected
