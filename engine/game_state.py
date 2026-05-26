from __future__ import annotations

from dataclasses import dataclass, field
import random

from engine.card import Card, Effect


@dataclass
class PlayerState:
    player_id: str
    deck_id: str
    bot_name: str
    public_deck: tuple[str, ...]
    hidden_deck: tuple[str, ...]
    draw_pile: list[Card]
    hand: list[Card] = field(default_factory=list)
    discard_pile: list[Card] = field(default_factory=list)
    used_cards: list[Card] = field(default_factory=list)
    last_battle_cards: list[Card] = field(default_factory=list)
    queued_next_turn_effects: list[Effect] = field(default_factory=list)
    active_turn_effects: list[Effect] = field(default_factory=list)
    current_control_card: Card | None = None
    set_cards: list[Card] = field(default_factory=list)
    battle_passed: bool = False
    current_reveals: list[str] = field(default_factory=list)
    mulligan1_discarded: int = 0
    mulligan2_discarded: int = 0
    reshuffle_count: int = 0
    reshuffle_turns: list[int] = field(default_factory=list)
    draw_shortfall_turns: list[int] = field(default_factory=list)

    def draw(self, count: int) -> list[Card]:
        drawn: list[Card] = []
        for _ in range(max(count, 0)):
            if not self.draw_pile:
                break
            drawn.append(self.draw_pile.pop(0))
        self.hand.extend(drawn)
        return drawn

    def remove_from_hand(self, card_id: str) -> Card:
        for index, card in enumerate(self.hand):
            if card.id == card_id:
                return self.hand.pop(index)
        raise ValueError(f"card not in hand: {card_id}")

    def has_type_in_hand(self, card_type: str) -> bool:
        return any(card.type == card_type for card in self.hand)

    def visible_last_battle_cards(self) -> tuple[Card, ...]:
        return tuple(self.last_battle_cards)


@dataclass(frozen=True)
class PlayerView:
    player_id: str
    turn: int
    phase: str
    hand: tuple[Card, ...]
    own_public_deck: tuple[str, ...]
    own_hidden_deck: tuple[str, ...]
    own_discard: tuple[Card, ...]
    own_used: tuple[Card, ...]
    opponent_public_deck: tuple[str, ...]
    opponent_discard: tuple[Card, ...]
    opponent_used: tuple[Card, ...]
    opponent_hand_count: int
    opponent_deck_count: int
    opponent_last_battle_cards: tuple[Card, ...]
    opponent_control_card: Card | None
    own_facedown_count: int
    opponent_facedown_count: int
    own_battle_passed: bool
    opponent_battle_passed: bool
    battle_starting_player: str
    acting_player: str


@dataclass
class GameState:
    players: dict[str, PlayerState]
    rng: random.Random
    hand_limit: int = 6
    initial_hand_size: int = 4
    turn_draw_limit: int = 4
    turn: int = 1
    phase: str = "setup"
    winner: str | None = None
    end_reason: str | None = None
    finished: bool = False
    max_turns: int = 50
    battle_starting_player: str = "p1"
    acting_player: str = "p1"

    def opponent_of(self, player_id: str) -> str:
        return "p2" if player_id == "p1" else "p1"

    def build_view(self, player_id: str) -> PlayerView:
        player = self.players[player_id]
        opponent = self.players[self.opponent_of(player_id)]
        return PlayerView(
            player_id=player_id,
            turn=self.turn,
            phase=self.phase,
            hand=tuple(player.hand),
            own_public_deck=player.public_deck,
            own_hidden_deck=player.hidden_deck,
            own_discard=tuple(player.discard_pile),
            own_used=tuple(player.used_cards),
            opponent_public_deck=opponent.public_deck,
            opponent_discard=tuple(opponent.discard_pile),
            opponent_used=tuple(opponent.used_cards),
            opponent_hand_count=len(opponent.hand),
            opponent_deck_count=len(opponent.draw_pile),
            opponent_last_battle_cards=opponent.visible_last_battle_cards(),
            opponent_control_card=opponent.current_control_card,
            own_facedown_count=len(player.set_cards),
            opponent_facedown_count=len(opponent.set_cards),
            own_battle_passed=player.battle_passed,
            opponent_battle_passed=opponent.battle_passed,
            battle_starting_player=self.battle_starting_player,
            acting_player=self.acting_player,
        )
