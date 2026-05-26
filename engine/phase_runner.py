from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import random

from bots.base_bot import BaseBot
from engine.card import Card, load_cards
from engine.deck import DeckDefinition, build_draw_pile, load_decks
from engine.effects import activate_start_of_turn_effects, resolve_information_effects
from engine.game_state import GameState, PlayerState
from engine.logger import MatchLogger
from engine.resolver import resolve_battle


@dataclass
class MatchResult:
    state: GameState
    log: dict[str, object]


class MatchRunner:
    def __init__(
        self,
        bot1: BaseBot,
        bot2: BaseBot,
        deck1_id: str,
        deck2_id: str,
        *,
        cards_path: str | Path = "data/cards.json",
        decks_path: str | Path = "data/decks.json",
        match_id: str = "match_000001",
        seed: int | None = None,
        shuffle_decks: bool = True,
        max_turns: int = 50,
    ) -> None:
        self.bot_map = {"p1": bot1, "p2": bot2}
        self.rng = random.Random(seed)
        self.cards = load_cards(cards_path)
        self.decks = load_decks(decks_path)
        self.state = GameState(
            players={
                "p1": self._build_player_state("p1", deck1_id, bot1.name, shuffle_decks),
                "p2": self._build_player_state("p2", deck2_id, bot2.name, shuffle_decks),
            },
            rng=self.rng,
            max_turns=max_turns,
        )
        self.logger = MatchLogger(match_id, self.state)

    def _build_player_state(self, player_id: str, deck_id: str, bot_name: str, shuffle_decks: bool) -> PlayerState:
        deck = self.decks[deck_id]
        return PlayerState(
            player_id=player_id,
            deck_id=deck.id,
            bot_name=bot_name,
            public_deck=deck.public_cards,
            hidden_deck=deck.hidden_cards,
            draw_pile=build_draw_pile(deck, self.cards, self.rng, shuffle=shuffle_decks),
        )

    def run(self) -> MatchResult:
        self._initial_draw()
        while not self.state.finished:
            if self.state.turn > self.state.max_turns:
                self.state.finished = True
                self.state.end_reason = "max_turns_reached"
                break
            self._run_turn()
            if not self.state.finished:
                self.state.turn += 1
        payload = self.logger.finish(self.state)
        return MatchResult(state=self.state, log=payload)

    def _initial_draw(self) -> None:
        for player in self.state.players.values():
            if len(player.hand) < self.state.hand_limit:
                player.draw(self.state.hand_limit - len(player.hand))

    def _run_turn(self) -> None:
        self.logger.start_turn(self.state.turn)
        self._start_turn()
        phase1 = self._run_mulligan_phase("phase1_mulligan", limit=None)
        self.logger.record_phase1(phase1)
        control_cards, reveals = self._run_control_phase()
        self.logger.record_control(control_cards, reveals)
        phase3 = self._run_mulligan_phase("phase3_mulligan", limit=2)
        self.logger.record_phase3(phase3)
        self._run_battle_select_phase()
        resolution = resolve_battle(self.state)
        self._record_battle(resolution)
        self._end_turn(resolution)

    def _start_turn(self) -> None:
        for player in self.state.players.values():
            player.current_control_card = None
            player.set_cards = []
            player.current_reveals = []
            player.mulligan1_discarded = 0
            player.mulligan2_discarded = 0
            draw_bonus = activate_start_of_turn_effects(player)
            target = self.state.hand_limit + draw_bonus
            if len(player.hand) < target:
                player.draw(target - len(player.hand))

    def _run_mulligan_phase(self, phase_name: str, limit: int | None) -> dict[str, list[str]]:
        self.state.phase = phase_name
        discarded_cards: dict[str, list[str]] = {"p1": [], "p2": []}
        for player_id, bot in self.bot_map.items():
            player = self.state.players[player_id]
            view = self.state.build_view(player_id)
            requested = bot.choose_mulligan(view)
            if limit is not None:
                requested = requested[:limit]
            actual = self._discard_cards(player, requested)
            if phase_name == "phase1_mulligan":
                player.mulligan1_discarded = len(actual)
            else:
                player.mulligan2_discarded = len(actual)
            player.draw(len(actual))
            discarded_cards[player_id] = [card.name for card in actual]
        return discarded_cards

    def _run_control_phase(self) -> tuple[dict[str, str | None], dict[str, list[str]]]:
        self.state.phase = "control"
        chosen: dict[str, str | None] = {"p1": None, "p2": None}
        reveals: dict[str, list[str]] = {"p1": [], "p2": []}
        for player_id, bot in self.bot_map.items():
            player = self.state.players[player_id]
            view = self.state.build_view(player_id)
            selected_id = bot.choose_control_card(view)
            if not selected_id:
                continue
            if not any(card.id == selected_id and card.type == "control" for card in player.hand):
                continue
            card = player.remove_from_hand(selected_id)
            player.current_control_card = card
            player.used_cards.append(card)
            reveals[player_id] = resolve_information_effects(player, self.state.players[self.state.opponent_of(player_id)], card)
            chosen[player_id] = card.name
        return chosen, reveals

    def _run_battle_select_phase(self) -> None:
        self.state.phase = "battle_select"
        for player_id, bot in self.bot_map.items():
            player = self.state.players[player_id]
            if not player.has_type_in_hand("battle"):
                continue
            view = self.state.build_view(player_id)
            selected_ids = bot.choose_battle_cards(view)
            if not selected_ids:
                continue
            selected_cards = self._remove_battle_cards_from_hand(player, selected_ids)
            if not selected_cards:
                fallback = next((card.id for card in player.hand if card.type == "battle"), None)
                if fallback is None:
                    continue
                selected_cards = self._remove_battle_cards_from_hand(player, [fallback])
            player.set_cards = selected_cards
            player.used_cards.extend(selected_cards)

    def _record_battle(self, resolution) -> None:
        self.state.phase = "battle"
        battle_payload = {
            "p1_cards": [card.name for card in self.state.players["p1"].set_cards],
            "p2_cards": [card.name for card in self.state.players["p2"].set_cards],
            "p1_final": {
                "attack": resolution.finals["p1"].attack,
                "block": resolution.finals["p1"].block,
                "speed": resolution.finals["p1"].speed,
            },
            "p2_final": {
                "attack": resolution.finals["p2"].attack,
                "block": resolution.finals["p2"].block,
                "speed": resolution.finals["p2"].speed,
            },
            "result": resolution.result,
        }
        self.logger.record_battle(battle_payload)

    def _end_turn(self, resolution) -> None:
        for player in self.state.players.values():
            player.last_battle_cards = list(player.set_cards)
        if resolution.winner:
            self.state.finished = True
            self.state.winner = resolution.winner
            self.state.end_reason = resolution.end_reason
            return

    def _both_players_stuck(self) -> bool:
        for player in self.state.players.values():
            if player.hand or player.draw_pile:
                return False
        return True

    def _discard_cards(self, player: PlayerState, requested_ids: list[str]) -> list[Card]:
        discarded: list[Card] = []
        for card_id in requested_ids:
            try:
                card = player.remove_from_hand(card_id)
            except ValueError:
                continue
            player.discard_pile.append(card)
            discarded.append(card)
        return discarded

    def _remove_battle_cards_from_hand(self, player: PlayerState, requested_ids: list[str]) -> list[Card]:
        selected: list[Card] = []
        for card_id in requested_ids:
            try:
                card = player.remove_from_hand(card_id)
            except ValueError:
                continue
            if card.type != "battle":
                player.hand.append(card)
                continue
            selected.append(card)
        return selected
