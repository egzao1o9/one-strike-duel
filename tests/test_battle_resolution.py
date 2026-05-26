from engine.card import Card, load_cards
from engine.game_state import GameState, PlayerState
from engine.resolver import resolve_battle
import random


def make_state():
    return GameState(
        players={
            "p1": PlayerState("p1", "d1", "TestBot", tuple(), tuple(), []),
            "p2": PlayerState("p2", "d2", "TestBot", tuple(), tuple(), []),
        },
        rng=random.Random(1),
    )


def test_faster_player_wins_before_counterattack() -> None:
    cards = load_cards("data/cards.json")
    state = make_state()
    state.players["p1"].set_cards = [cards["battle_step_in"]]
    state.players["p2"].set_cards = [cards["battle_all_in"]]

    resolution = resolve_battle(state)

    assert resolution.winner == "p1"
    assert resolution.end_reason == "p1_attack_success"


def test_equal_speed_can_draw() -> None:
    cards = load_cards("data/cards.json")
    state = make_state()
    state.players["p1"].set_cards = [cards["battle_step_in"]]
    state.players["p2"].set_cards = [cards["battle_break"]]

    resolution = resolve_battle(state)

    assert resolution.result == "draw"


def test_block_limit_effect_zeroes_block_gain() -> None:
    cards = load_cards("data/cards.json")
    state = make_state()
    state.players["p1"].set_cards = [cards["battle_step_in"]]
    state.players["p1"].current_control_card = cards["control_guard"]
    state.players["p2"].set_cards = [cards["battle_guard"]]

    resolution = resolve_battle(state)

    assert resolution.finals["p1"].block == 0


def test_multiple_battle_cards_are_summed() -> None:
    cards = load_cards("data/cards.json")
    state = make_state()
    state.players["p1"].set_cards = [cards["battle_step_in"], cards["battle_press"]]
    state.players["p2"].set_cards = [cards["battle_guard"]]

    resolution = resolve_battle(state)

    assert resolution.finals["p1"].attack == 5
    assert resolution.finals["p1"].block == 0
    assert resolution.finals["p1"].speed == 4
    assert resolution.winner == "p1"


def test_negative_speed_is_kept_and_compared_as_is() -> None:
    state = make_state()
    slow_card = Card(id="slow", name="鈍重", type="battle", attack=2, block=0, speed=-1)
    fast_card = Card(id="fast", name="軽打", type="battle", attack=1, block=0, speed=0)
    state.players["p1"].set_cards = [slow_card]
    state.players["p2"].set_cards = [fast_card]

    resolution = resolve_battle(state)

    assert resolution.finals["p1"].speed == -1
    assert resolution.finals["p2"].speed == 0
    assert resolution.winner == "p2"
