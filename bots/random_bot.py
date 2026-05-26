from __future__ import annotations

import random

from bots.base_bot import BaseBot
from engine.game_state import PlayerView


class RandomBot(BaseBot):
    name = "RandomBot"

    def __init__(self, seed: int | None = None) -> None:
        self.rng = random.Random(seed)

    def choose_mulligan(self, view: PlayerView) -> list[str]:
        if not view.hand:
            return []
        selected: list[str] = []
        for card in view.hand:
            if self.rng.random() < 0.25:
                selected.append(card.id)
        return selected

    def choose_control_card(self, view: PlayerView) -> str | None:
        options = [card.id for card in view.hand if card.type == "control"]
        options.append(None)
        return self.rng.choice(options)

    def choose_battle_card(self, view: PlayerView) -> str | None:
        options = [card.id for card in view.hand if card.type == "battle"]
        if not options:
            return None
        return self.rng.choice(options)

    def choose_battle_cards(self, view: PlayerView) -> list[str]:
        options = [card.id for card in view.hand if card.type == "battle"]
        if not options:
            return []
        selected = [card_id for card_id in options if self.rng.random() < 0.5]
        return selected or [self.rng.choice(options)]
