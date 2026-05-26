from __future__ import annotations

from bots.base_bot import BaseBot
from engine.card import Card
from engine.game_state import PlayerView


class AttackBot(BaseBot):
    name = "AttackBot"

    def choose_mulligan(self, view: PlayerView) -> list[str]:
        return [card.id for card in view.hand if card.type == "battle" and card.attack <= 1]

    def choose_control_card(self, view: PlayerView) -> str | None:
        controls = [card for card in view.hand if card.type == "control"]
        if not controls:
            return None
        controls.sort(key=self._control_score, reverse=True)
        return controls[0].id

    def choose_battle_card(self, view: PlayerView) -> str | None:
        battles = [card for card in view.hand if card.type == "battle"]
        if not battles:
            return None
        battles.sort(key=lambda card: (card.attack, card.speed, -card.block), reverse=True)
        return battles[0].id

    def choose_battle_cards(self, view: PlayerView) -> list[str]:
        battles = [card for card in view.hand if card.type == "battle"]
        selected = [card.id for card in battles if card.attack > 0]
        if selected:
            return selected
        return [self.choose_battle_card(view)] if self.choose_battle_card(view) else []

    @staticmethod
    def _control_score(card: Card) -> tuple[int, int]:
        attack_bias = sum(1 for effect in card.effects if effect.kind in {"modify_self_attack", "modify_opponent_block"})
        speed_bias = sum(1 for effect in card.effects if effect.kind == "modify_self_speed")
        return (attack_bias, speed_bias)
