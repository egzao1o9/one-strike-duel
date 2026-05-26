from engine.card import load_cards
from engine.deck import build_draw_pile, load_decks


def test_cards_and_decks_load() -> None:
    cards = load_cards("data/cards.json")
    decks = load_decks("data/decks.json")

    assert "battle_step_in" in cards
    assert "starter_attack" in decks
    assert cards["control_focus"].type == "control"
    assert cards["control_focus"].rarity == "common"
    assert len(decks["starter_attack"].all_cards) == 20


def test_build_draw_pile_contains_all_cards() -> None:
    import random

    cards = load_cards("data/cards.json")
    decks = load_decks("data/decks.json")
    pile = build_draw_pile(decks["starter_defense"], cards, random.Random(1), shuffle=False)

    assert len(pile) == 20
    assert pile[0].id == decks["starter_defense"].all_cards[0]
