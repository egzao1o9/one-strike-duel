from __future__ import annotations

from bots.base_bot import BaseBot
from engine.game_state import PlayerView


class RiskBot(BaseBot):
    name = "RiskBot"

    def choose_control_card(self, view: PlayerView) -> str | None:
        for card in view.hand:
            if card.type == "control" and any(effect.kind == "modify_self_block" for effect in card.effects):
                return card.id
        for card in view.hand:
            if card.type == "control" and any(effect.kind == "modify_opponent_attack" for effect in card.effects):
                return card.id
        return None

    def choose_battle_card(self, view: PlayerView) -> str | None:
        battles = [card for card in view.hand if card.type == "battle"]
        if not battles:
            return None
        aggressive_public = sum(1 for card_id in view.opponent_public_deck if "step_in" in card_id or "all_in" in card_id)
        if aggressive_public >= 2:
            battles.sort(key=lambda card: (card.block, card.speed, card.attack), reverse=True)
        else:
            battles.sort(key=lambda card: (card.block + card.attack, card.speed), reverse=True)
        return battles[0].id

    def choose_battle_cards(self, view: PlayerView) -> list[str]:
        battles = [card for card in view.hand if card.type == "battle"]
        if not battles:
            return []
        aggressive_public = sum(1 for card_id in view.opponent_public_deck if "step_in" in card_id or "all_in" in card_id)
        if aggressive_public >= 2:
            selected = [card.id for card in battles if card.block > 0]
        else:
            selected = [card.id for card in battles if card.block + card.attack >= 3]
        if selected:
            return selected
        return [self.choose_battle_card(view)] if self.choose_battle_card(view) else []
