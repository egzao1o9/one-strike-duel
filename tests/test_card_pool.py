from collections import Counter
import random

from engine.card import load_cards
from engine.card_pool import build_default_card_pool, draft_random_decks, load_card_pool


def test_card_pool_loads_with_expected_copy_rules() -> None:
    cards = load_cards("data/cards.json")
    pool = load_card_pool("data/card_pool.json", cards)
    counts = {entry.card_id: entry.count for entry in pool.entries}

    assert counts["control_focus"] == 4
    assert counts["control_haste"] == 3
    assert counts["battle_step_in"] == 2
    assert counts["battle_all_in"] == 2
    assert counts["battle_bulwark"] == 3


def test_default_pool_builder_matches_rarity_rules() -> None:
    cards = load_cards("data/cards.json")
    pool = build_default_card_pool(cards)
    counts = {entry.card_id: entry.count for entry in pool.entries}

    assert counts["control_focus"] == 4
    assert counts["control_haste"] == 3
    assert counts["battle_heavy_swing"] == 2


def test_random_draft_respects_pool_counts() -> None:
    cards = load_cards("data/cards.json")
    pool = load_card_pool("data/card_pool.json", cards)

    draft = draft_random_decks(pool, cards, random.Random(9), deck_size=20, first_player="p1")
    combined = Counter(draft.deck1.all_cards + draft.deck2.all_cards)
    pool_counts = {entry.card_id: entry.count for entry in pool.entries}

    assert len(draft.deck1.all_cards) == 20
    assert len(draft.deck2.all_cards) == 20
    assert len(draft.picks) == 40
    assert draft.first_player == "p1"
    assert len(draft.deck1.hidden_cards) == 0
    assert len(draft.deck2.hidden_cards) == 0
    for card_id, count in combined.items():
        assert count <= pool_counts[card_id]
