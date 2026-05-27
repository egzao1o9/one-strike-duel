import random

from engine.card import load_cards
from engine.card_pool import load_card_pool
from engine.drafting import RandomDraftBot, RoleBalanceDraftBot, StandardDraftBot, draft_with_bots, infer_role_color, summarize_deck


def test_infer_role_color_maps_expected_cards() -> None:
    cards = load_cards("data/cards.json")

    assert infer_role_color(cards["battle_all_in"]) == "red"
    assert infer_role_color(cards["battle_afterimage"]) == "blue"
    assert infer_role_color(cards["battle_guard"]) == "green"
    assert infer_role_color(cards["control_focus"]) == "white"


def test_role_balance_drafter_builds_balanced_deck() -> None:
    cards = load_cards("data/cards.json")
    pool = load_card_pool("data/card_pool.json", cards)
    draft = draft_with_bots(
        pool,
        cards,
        random.Random(21),
        RoleBalanceDraftBot(),
        RandomDraftBot(),
        deck_size=20,
        first_player="p1",
    )
    summary = summarize_deck(draft.deck1.all_cards, cards)

    assert summary.total == 20
    assert summary.control_count >= 6
    assert summary.role_counts["white"] >= 6


def test_new_draft_flow_tracks_hidden_and_public_picks() -> None:
    cards = load_cards("data/cards.json")
    pool = load_card_pool("data/card_pool.json", cards)
    draft = draft_with_bots(
        pool,
        cards,
        random.Random(17),
        RandomDraftBot(),
        StandardDraftBot(seed=18),
        deck_size=20,
        first_player="p1",
    )

    assert len(draft.deck1.all_cards) == 20
    assert len(draft.deck2.all_cards) == 20
    assert len(draft.deck1.hidden_cards) == 7
    assert len(draft.deck2.hidden_cards) == 7
    assert len(draft.deck1.public_cards) == 13
    assert len(draft.deck2.public_cards) == 13
    assert draft.picks[0].player_id == "p1"
    assert draft.picks[0].visibility == "hidden"
    assert draft.picks[1].player_id == "p2"
    assert draft.picks[1].visibility == "public"
    assert draft.picks[1].pick_position == 1
    assert draft.picks[2].player_id == "p1"
    assert draft.picks[2].visibility == "public"
    assert draft.picks[2].pick_position == 2
    assert draft.picks[3].player_id == "p2"
    assert draft.picks[3].visibility == "hidden"
