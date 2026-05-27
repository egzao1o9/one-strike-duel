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
        draft_mode="full",
    )
    summary = summarize_deck(draft.deck1.all_cards, cards)

    assert summary.total == 20
    assert summary.rarity_counts["common"] == 8
    assert summary.rarity_counts["uncommon"] == 8
    assert summary.rarity_counts["rare"] == 4


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
        draft_mode="full",
    )

    assert len(draft.deck1.all_cards) == 20
    assert len(draft.deck2.all_cards) == 20
    assert len(draft.deck1.hidden_cards) == 10
    assert len(draft.deck2.hidden_cards) == 10
    assert len(draft.deck1.public_cards) == 10
    assert len(draft.deck2.public_cards) == 10
    assert len(draft.deck1.metadata["public_normal_cards"]) == 8
    assert len(draft.deck1.metadata["hidden_normal_cards"]) == 8
    assert len(draft.deck1.metadata["public_rare_cards"]) == 2
    assert len(draft.deck1.metadata["hidden_rare_cards"]) == 2
    assert len(draft.deck2.metadata["public_normal_cards"]) == 8
    assert len(draft.deck2.metadata["hidden_normal_cards"]) == 8
    assert len(draft.deck2.metadata["public_rare_cards"]) == 2
    assert len(draft.deck2.metadata["hidden_rare_cards"]) == 2
    assert draft.deck1.metadata["final_rarity_counts"] == {"common": 8, "uncommon": 8, "rare": 4}
    assert draft.deck2.metadata["final_rarity_counts"] == {"common": 8, "uncommon": 8, "rare": 4}
    assert len(draft.picks) == 16
    assert draft.picks[0].player_id == "p1"
    assert draft.picks[0].visibility == "public"
    assert draft.picks[0].phase == "normal_public"
    assert len(draft.picks[0].selected_card_ids) == 4
    assert draft.picks[1].player_id == "p2"
    assert draft.picks[1].visibility == "hidden"
    assert draft.picks[1].phase == "normal_hidden"
    assert draft.picks[2].player_id == "p2"
    assert draft.picks[2].visibility == "public"
    assert draft.picks[2].pick_position == 2
    assert draft.picks[3].player_id == "p1"
    assert draft.picks[3].visibility == "hidden"
    assert "public_draft_events" in draft.deck1.metadata
    assert "public_draft_events" in draft.deck2.metadata
    assert len(draft.deck1.metadata["public_draft_events"]) > 0


def test_simple_draft_flow_hits_rarity_targets() -> None:
    cards = load_cards("data/cards.json")
    pool = load_card_pool("data/card_pool.json", cards)
    draft = draft_with_bots(
        pool,
        cards,
        random.Random(19),
        RandomDraftBot(),
        StandardDraftBot(seed=20),
        deck_size=20,
        first_player="p1",
        draft_mode="simple",
    )

    assert len(draft.deck1.all_cards) == 20
    assert len(draft.deck2.all_cards) == 20
    assert len(draft.deck1.hidden_cards) == 7
    assert len(draft.deck1.public_cards) == 13
    assert len(draft.deck2.hidden_cards) == 7
    assert len(draft.deck2.public_cards) == 13
    summary1 = summarize_deck(draft.deck1.all_cards, cards)
    summary2 = summarize_deck(draft.deck2.all_cards, cards)
    assert summary1.rarity_counts == {"common": 8, "uncommon": 8, "rare": 4}
    assert summary2.rarity_counts == {"common": 8, "uncommon": 8, "rare": 4}
    assert draft.deck1.metadata["draft_mode"] == "simple"
