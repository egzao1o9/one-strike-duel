from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import random

from bots.base_bot import BaseBot, BattleAction
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
        deck_definitions: dict[str, DeckDefinition] | None = None,
        match_id: str = "match_000001",
        seed: int | None = None,
        shuffle_decks: bool = True,
        max_turns: int = 50,
    ) -> None:
        self.bot_map = {"p1": bot1, "p2": bot2}
        self.rng = random.Random(seed)
        self.cards = load_cards(cards_path)
        self.decks = load_decks(decks_path)
        if deck_definitions:
            self.decks.update(deck_definitions)
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
            deck_metadata=dict(deck.metadata),
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
            player.draw(self.state.initial_hand_size)

    def _run_turn(self) -> None:
        self.logger.start_turn(self.state.turn)
        turn_start_payload = self._start_turn()
        self.logger.record_turn_start(turn_start_payload)
        phase1 = self._run_mulligan_phase("phase1_mulligan", limit=None)
        self.logger.record_phase1(phase1["discarded"], phase1["hand_counts"])
        control_cards, control_ids, control_sources, reveals, control_hand_counts, control_debug = self._run_control_phase()
        self.logger.record_control(control_cards, reveals, control_ids, control_sources, control_hand_counts, control_debug)
        phase3 = self._run_mulligan_phase("phase3_mulligan", limit=2)
        self.logger.record_phase3(phase3["discarded"], phase3["hand_counts"])
        battle_context = self._run_battle_select_phase()
        resolution = resolve_battle(self.state)
        self._record_battle(resolution, battle_context)
        self._end_turn(resolution)

    def _start_turn(self) -> dict[str, object]:
        self.state.phase = "turn_start"
        self.state.acting_player = self.state.battle_starting_player
        payload: dict[str, object] = {
            "starting_player": self.state.battle_starting_player,
            "p1": {},
            "p2": {},
        }
        for player_id, bot in self.bot_map.items():
            player = self.state.players[player_id]
            player.current_control_card = None
            player.set_cards = []
            player.battle_passed = False
            player.current_reveals = []
            player.mulligan1_discarded = 0
            player.mulligan2_discarded = 0

            overflow_discards = self._discard_overflow(player_id, bot)
            draw_bonus = activate_start_of_turn_effects(player)
            base_draw_limit = 0 if self.state.turn == 1 else self.state.turn_draw_limit
            draw_result = self._draw_for_turn_start(player, base_draw_limit + draw_bonus)
            payload[player_id] = {
                "overflow_discarded": [card.name for card in overflow_discards],
                "drawn": [card.name for card in draw_result["drawn"]],
                "draw_count": len(draw_result["drawn"]),
                "reshuffled": draw_result["reshuffled"],
                "draw_shortfall": draw_result["draw_shortfall"],
                "hand_count": len(player.hand),
            }
        return payload

    def _discard_overflow(self, player_id: str, bot: BaseBot) -> list[Card]:
        player = self.state.players[player_id]
        overflow = max(0, len(player.hand) - self.state.hand_limit)
        if overflow == 0:
            return []
        view = self.state.build_view(player_id)
        requested = bot.choose_overflow_discards(view, overflow)
        discarded = self._discard_cards(player, requested[:overflow])
        if len(discarded) < overflow:
            remaining_ids = [card.id for card in list(player.hand)[: overflow - len(discarded)]]
            discarded.extend(self._discard_cards(player, remaining_ids))
        return discarded

    def _draw_for_turn_start(self, player: PlayerState, max_draw: int) -> dict[str, object]:
        drawn: list[Card] = []
        reshuffled = False
        remaining = min(max_draw, max(0, self.state.hand_limit - len(player.hand)))
        while remaining > 0:
            if not player.draw_pile:
                if not player.discard_pile:
                    break
                player.draw_pile = list(player.discard_pile)
                player.discard_pile.clear()
                self.rng.shuffle(player.draw_pile)
                reshuffled = True
                player.reshuffle_count += 1
                player.reshuffle_turns.append(self.state.turn)
            step = min(remaining, len(player.draw_pile))
            if step <= 0:
                break
            drawn.extend(player.draw(step))
            remaining -= step
        draw_shortfall = remaining
        if draw_shortfall > 0:
            player.draw_shortfall_turns.append(self.state.turn)
        return {
            "drawn": drawn,
            "reshuffled": reshuffled,
            "draw_shortfall": draw_shortfall,
        }

    def _run_mulligan_phase(self, phase_name: str, limit: int | None) -> dict[str, object]:
        self.state.phase = phase_name
        discarded_cards: dict[str, list[str]] = {"p1": [], "p2": []}
        hand_counts: dict[str, int] = {}
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
            hand_counts[player_id] = len(player.hand)
        return {
            "discarded": discarded_cards,
            "hand_counts": hand_counts,
            "p1": discarded_cards["p1"],
            "p2": discarded_cards["p2"],
        }

    def _run_control_phase(self) -> tuple[dict[str, str | None], dict[str, str | None], dict[str, str | None], dict[str, list[str]], dict[str, int], dict[str, object]]:
        self.state.phase = "control"
        chosen: dict[str, str | None] = {"p1": None, "p2": None}
        chosen_ids: dict[str, str | None] = {"p1": None, "p2": None}
        chosen_sources: dict[str, str | None] = {"p1": None, "p2": None}
        reveals: dict[str, list[str]] = {"p1": [], "p2": []}
        hand_counts: dict[str, int] = {}
        debug_payload: dict[str, object] = {}
        for player_id, bot in self.bot_map.items():
            player = self.state.players[player_id]
            view = self.state.build_view(player_id)
            selected_id = bot.choose_control_card(view)
            bot_debug = bot.consume_debug_info()
            if bot_debug:
                debug_payload[player_id] = bot_debug.get("control", bot_debug)
            if not selected_id:
                hand_counts[player_id] = len(player.hand)
                continue
            if not any(card.id == selected_id and card.type == "control" for card in player.hand):
                hand_counts[player_id] = len(player.hand)
                continue
            card = player.remove_from_hand(selected_id)
            player.current_control_card = card
            player.used_cards.append(card)
            reveals[player_id] = resolve_information_effects(
                player,
                self.state.players[self.state.opponent_of(player_id)],
                card,
            )
            chosen[player_id] = card.name
            chosen_ids[player_id] = card.id
            chosen_sources[player_id] = card.instance_source or "unknown"
            hand_counts[player_id] = len(player.hand)
        for player_id in ("p1", "p2"):
            hand_counts.setdefault(player_id, len(self.state.players[player_id].hand))
        return chosen, chosen_ids, chosen_sources, reveals, hand_counts, debug_payload

    def _run_battle_select_phase(self) -> dict[str, object]:
        self.state.phase = "battle_select"
        self.state.acting_player = self.state.battle_starting_player
        for player in self.state.players.values():
            player.set_cards = []
            player.battle_passed = False

        action_history: list[dict[str, object]] = []
        first_pass_player: str | None = None

        while not all(player.battle_passed for player in self.state.players.values()):
            player_id = self.state.acting_player
            player = self.state.players[player_id]
            opponent_id = self.state.opponent_of(player_id)

            if player.battle_passed:
                self.state.acting_player = opponent_id
                continue

            view = self.state.build_view(player_id)
            requested = self.bot_map[player_id].choose_battle_action(view)
            debug_info = self.bot_map[player_id].consume_debug_info()
            applied = self._apply_battle_action(player_id, requested, debug_info)
            if applied["became_passed"] and first_pass_player is None:
                first_pass_player = player_id
            action_history.append(applied["history"])
            self.state.acting_player = opponent_id

        return {
            "starting_player": self.state.battle_starting_player,
            "first_pass_player": first_pass_player,
            "actions": action_history,
            "p1_facedown_count": len(self.state.players["p1"].set_cards),
            "p2_facedown_count": len(self.state.players["p2"].set_cards),
            "p1_hand_count_end": len(self.state.players["p1"].hand),
            "p2_hand_count_end": len(self.state.players["p2"].hand),
        }

    def _apply_battle_action(self, player_id: str, requested: BattleAction, debug_info: dict[str, object] | None = None) -> dict[str, object]:
        player = self.state.players[player_id]
        opponent = self.state.players[self.state.opponent_of(player_id)]
        before_counts = {"p1": len(self.state.players["p1"].set_cards), "p2": len(self.state.players["p2"].set_cards)}
        hand_count_before = len(player.hand)

        legal_slots = max(0, len(opponent.set_cards) + 1 - len(player.set_cards))
        chosen_cards: list[Card] = []
        action_type = requested.action_type

        if action_type == "pass" or legal_slots == 0 or not player.has_type_in_hand("battle"):
            player.battle_passed = True
            action_type = "pass"
        else:
            if action_type not in {"set", "set_pass"}:
                action_type = "set_pass"
            max_cards = 1 if action_type == "set_pass" else min(2, legal_slots)
            requested_ids = list(requested.card_ids[:max_cards])
            chosen_cards = self._remove_battle_cards_from_hand(player, requested_ids)
            if len(chosen_cards) < (1 if action_type == "set_pass" else 1):
                fallback_ids = [
                    card.id
                    for card in player.hand
                    if card.type == "battle"
                ][: max_cards - len(chosen_cards)]
                chosen_cards.extend(self._remove_battle_cards_from_hand(player, fallback_ids))
            chosen_cards = chosen_cards[:max_cards]
            if not chosen_cards:
                player.battle_passed = True
                action_type = "pass"
            else:
                player.set_cards.extend(chosen_cards)
                if action_type == "set_pass":
                    player.battle_passed = True

        after_counts = {"p1": len(self.state.players["p1"].set_cards), "p2": len(self.state.players["p2"].set_cards)}
        return {
            "became_passed": player.battle_passed and action_type in {"set_pass", "pass"},
            "history": {
                "player_id": player_id,
                "requested_action_type": requested.action_type,
                "requested_card_ids": list(requested.card_ids),
                "action_type": action_type,
                "action_name": _action_name(action_type),
                "set_count": len(chosen_cards),
                "set_card_ids": [card.id for card in chosen_cards],
                "set_card_names": [card.name for card in chosen_cards],
                "set_card_sources": [card.instance_source or "unknown" for card in chosen_cards],
                "hand_count_before": hand_count_before,
                "hand_count_after": len(player.hand),
                "set_pass_candidate_count": _extract_set_pass_candidate_count(debug_info),
                "counts_before": before_counts,
                "counts_after": after_counts,
                "debug": debug_info or {},
            },
        }

    def _record_battle(self, resolution, context: dict[str, object]) -> None:
        self.state.phase = "battle"
        winner = resolution.winner
        winner_facedown_count = len(self.state.players[winner].set_cards) if winner else None
        loser_id = self.state.opponent_of(winner) if winner else None
        loser_facedown_count = len(self.state.players[loser_id].set_cards) if loser_id else None
        fewer_cards_win = winner_facedown_count < loser_facedown_count if winner else None
        same_cards_win = winner_facedown_count == loser_facedown_count if winner else None
        more_cards_win = winner_facedown_count > loser_facedown_count if winner else None
        battle_payload = {
            "starting_player": context["starting_player"],
            "first_pass_player": context["first_pass_player"],
            "actions": context["actions"],
            "p1_cards": [card.name for card in self.state.players["p1"].set_cards],
            "p1_card_ids": [card.id for card in self.state.players["p1"].set_cards],
            "p1_card_sources": [card.instance_source or "unknown" for card in self.state.players["p1"].set_cards],
            "p2_cards": [card.name for card in self.state.players["p2"].set_cards],
            "p2_card_ids": [card.id for card in self.state.players["p2"].set_cards],
            "p2_card_sources": [card.instance_source or "unknown" for card in self.state.players["p2"].set_cards],
            "p1_facedown_count": context["p1_facedown_count"],
            "p2_facedown_count": context["p2_facedown_count"],
            "p1_hand_count_end": context["p1_hand_count_end"],
            "p2_hand_count_end": context["p2_hand_count_end"],
            "winner_facedown_count": winner_facedown_count,
            "loser_facedown_count": loser_facedown_count,
            "won_with_fewer_cards": fewer_cards_win,
            "won_with_same_cards": same_cards_win,
            "won_with_more_cards": more_cards_win,
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
            "draw_reason": resolution.end_reason,
        }
        self.logger.record_battle(battle_payload)

    def _end_turn(self, resolution) -> None:
        for player in self.state.players.values():
            player.last_battle_cards = list(player.set_cards)
            player.used_cards.extend(player.set_cards)
        if resolution.winner:
            self.state.finished = True
            self.state.winner = resolution.winner
            self.state.end_reason = resolution.end_reason
            return
        if resolution.result == "draw":
            self.state.finished = True
            self.state.winner = None
            self.state.end_reason = resolution.end_reason
            return
        self.state.battle_starting_player = self.state.opponent_of(self.state.battle_starting_player)

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


def _extract_set_pass_candidate_count(debug_info: dict[str, object] | None) -> int | None:
    if not isinstance(debug_info, dict):
        return None
    battle_debug = debug_info.get("battle")
    if isinstance(battle_debug, dict):
        value = battle_debug.get("set_pass_candidate_count")
        return int(value) if isinstance(value, int) else None
    value = debug_info.get("set_pass_candidate_count")
    return int(value) if isinstance(value, int) else None


def _action_name(action_type: str) -> str:
    if action_type == "set":
        return "伏せる"
    if action_type == "set_pass":
        return "伏せてパス"
    return "パス"
