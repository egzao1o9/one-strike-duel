from bots.base_bot import BaseBot, BattleAction
from bots.random_bot import RandomBot
from engine.card_pool import build_default_card_pool, draft_random_decks
from engine.phase_runner import MatchRunner


def test_random_match_runs_to_completion() -> None:
    runner = MatchRunner(RandomBot(seed=1), RandomBot(seed=2), "starter_attack", "starter_defense", seed=3)
    result = runner.run()

    assert result.state.finished is True
    assert result.log["turn_count"] >= 1
    turn = result.log["turns"][0]
    assert "turn_start" in turn
    assert "phase1_mulligan" in turn
    assert "control" in turn
    assert "phase3_mulligan" in turn
    assert "battle" in turn


class ScriptedBattleBot(BaseBot):
    name = "ScriptedBattleBot"

    def __init__(
        self,
        actions: list[BattleAction] | None = None,
        overflow_discards: list[str] | None = None,
        mulligan: list[str] | None = None,
    ) -> None:
        self.actions = list(actions or [])
        self.overflow_discards = list(overflow_discards or [])
        self.mulligan = list(mulligan or [])

    def choose_mulligan(self, view):
        return list(self.mulligan)

    def choose_overflow_discards(self, view, overflow_count: int):
        return list(self.overflow_discards[:overflow_count])

    def choose_battle_action(self, view):
        if self.actions:
            return self.actions.pop(0)
        return BattleAction("pass")


def test_initial_hand_starts_at_four() -> None:
    runner = MatchRunner(RandomBot(seed=1), RandomBot(seed=2), "starter_attack", "starter_defense", seed=3)

    runner._initial_draw()

    assert len(runner.state.players["p1"].hand) == 4
    assert len(runner.state.players["p2"].hand) == 4


def test_turn_start_refills_only_up_to_hand_limit_six() -> None:
    runner = MatchRunner(RandomBot(seed=1), RandomBot(seed=2), "starter_attack", "starter_defense", shuffle_decks=False, seed=3)
    runner.state.players["p1"].hand = [runner.cards["battle_press"], runner.cards["control_focus"]]
    runner.state.players["p1"].draw_pile = [
        runner.cards["battle_break"],
        runner.cards["battle_guard"],
        runner.cards["battle_counter"],
        runner.cards["control_haste"],
        runner.cards["battle_feint"],
    ]

    payload = runner._start_turn()

    assert len(runner.state.players["p1"].hand) == 6
    assert payload["p1"]["draw_count"] == 4


def test_turn_start_discards_overflow_before_drawing() -> None:
    bot = ScriptedBattleBot(overflow_discards=["battle_press"])
    runner = MatchRunner(bot, RandomBot(seed=2), "starter_attack", "starter_defense", shuffle_decks=False, seed=3)
    runner.state.players["p1"].hand = [
        runner.cards["battle_press"],
        runner.cards["battle_break"],
        runner.cards["battle_guard"],
        runner.cards["battle_counter"],
        runner.cards["control_focus"],
        runner.cards["control_haste"],
        runner.cards["control_guard"],
    ]
    runner.state.players["p1"].draw_pile = [runner.cards["battle_feint"], runner.cards["battle_dash"]]

    payload = runner._start_turn()

    assert len(runner.state.players["p1"].hand) == 6
    assert runner.state.players["p1"].discard_pile[0].id == "battle_press"
    assert payload["p1"]["overflow_discarded"] == ["押し込み"]
    assert payload["p1"]["draw_count"] == 0


def test_battle_actions_alternate_from_starting_player() -> None:
    p1 = ScriptedBattleBot([BattleAction("set", ("battle_press",)), BattleAction("pass")])
    p2 = ScriptedBattleBot([BattleAction("set_pass", ("battle_guard",))])
    runner = MatchRunner(p1, p2, "starter_attack", "starter_defense", shuffle_decks=False, seed=3, max_turns=1)
    runner.state.players["p1"].hand = [runner.cards["battle_press"], runner.cards["battle_break"], runner.cards["control_focus"], runner.cards["control_haste"]]
    runner.state.players["p2"].hand = [runner.cards["battle_guard"], runner.cards["battle_counter"], runner.cards["control_focus"], runner.cards["control_haste"]]
    runner.state.players["p1"].draw_pile = []
    runner.state.players["p2"].draw_pile = []

    result = runner.run()
    actions = result.log["turns"][0]["battle"]["actions"]

    assert [action["player_id"] for action in actions] == ["p1", "p2", "p1"]


def test_set_action_can_place_two_cards_when_legal() -> None:
    p1 = ScriptedBattleBot([BattleAction("set", ("battle_press", "battle_break")), BattleAction("pass")])
    p2 = ScriptedBattleBot([BattleAction("set", ("battle_guard",)), BattleAction("pass")])
    runner = MatchRunner(p1, p2, "starter_attack", "starter_defense", shuffle_decks=False, seed=3, max_turns=1)
    runner.state.battle_starting_player = "p2"
    runner.state.players["p1"].hand = [
        runner.cards["battle_press"],
        runner.cards["battle_break"],
        runner.cards["battle_counter"],
        runner.cards["control_focus"],
    ]
    runner.state.players["p2"].hand = [
        runner.cards["battle_guard"],
        runner.cards["battle_counter"],
        runner.cards["control_focus"],
        runner.cards["control_haste"],
    ]
    runner.state.players["p1"].draw_pile = []
    runner.state.players["p2"].draw_pile = []

    result = runner.run()
    actions = result.log["turns"][0]["battle"]["actions"]

    assert actions[1]["action_type"] == "set"
    assert actions[1]["set_count"] == 2


def test_set_pass_places_one_card_and_prevents_more_actions() -> None:
    p1 = ScriptedBattleBot([BattleAction("set_pass", ("battle_press",)), BattleAction("set", ("battle_break",))])
    p2 = ScriptedBattleBot([BattleAction("pass")])
    runner = MatchRunner(p1, p2, "starter_attack", "starter_defense", shuffle_decks=False, seed=3, max_turns=1)
    runner.state.players["p1"].hand = [runner.cards["battle_press"], runner.cards["battle_break"], runner.cards["control_focus"], runner.cards["control_haste"]]
    runner.state.players["p2"].hand = [runner.cards["battle_guard"], runner.cards["control_focus"], runner.cards["control_haste"], runner.cards["control_guard"]]
    runner.state.players["p1"].draw_pile = []
    runner.state.players["p2"].draw_pile = []

    result = runner.run()
    actions = result.log["turns"][0]["battle"]["actions"]

    assert actions[0]["action_type"] == "set_pass"
    assert actions[0]["set_count"] == 1
    assert [action["player_id"] for action in actions].count("p1") == 1


def test_pass_places_no_card_and_ends_future_actions_for_that_player() -> None:
    p1 = ScriptedBattleBot([BattleAction("pass"), BattleAction("set", ("battle_press",))])
    p2 = ScriptedBattleBot([BattleAction("set_pass", ("battle_guard",))])
    runner = MatchRunner(p1, p2, "starter_attack", "starter_defense", shuffle_decks=False, seed=3, max_turns=1)
    runner.state.players["p1"].hand = [runner.cards["battle_press"], runner.cards["battle_break"], runner.cards["control_focus"], runner.cards["control_haste"]]
    runner.state.players["p2"].hand = [runner.cards["battle_guard"], runner.cards["battle_counter"], runner.cards["control_focus"], runner.cards["control_haste"]]
    runner.state.players["p1"].draw_pile = []
    runner.state.players["p2"].draw_pile = []

    result = runner.run()
    actions = result.log["turns"][0]["battle"]["actions"]

    assert actions[0]["action_type"] == "pass"
    assert actions[0]["set_count"] == 0
    assert [action["player_id"] for action in actions].count("p1") == 1


def test_facedown_count_cannot_exceed_opponent_plus_one() -> None:
    p1 = ScriptedBattleBot([BattleAction("set", ("battle_press", "battle_break"))])
    p2 = ScriptedBattleBot([BattleAction("pass")])
    runner = MatchRunner(p1, p2, "starter_attack", "starter_defense", shuffle_decks=False, seed=3, max_turns=1)
    runner.state.players["p1"].hand = [runner.cards["battle_press"], runner.cards["battle_break"], runner.cards["control_focus"], runner.cards["control_haste"]]
    runner.state.players["p2"].hand = [runner.cards["battle_guard"], runner.cards["control_focus"], runner.cards["control_haste"], runner.cards["control_guard"]]
    runner.state.players["p1"].draw_pile = []
    runner.state.players["p2"].draw_pile = []

    result = runner.run()

    assert result.log["turns"][0]["battle"]["p1_facedown_count"] == 1
    assert result.log["turns"][0]["battle"]["actions"][0]["set_count"] == 1


def test_both_players_passing_reveals_cards_and_resolves_battle() -> None:
    p1 = ScriptedBattleBot([BattleAction("set_pass", ("battle_all_in",))])
    p2 = ScriptedBattleBot([BattleAction("set_pass", ("battle_guard",))])
    runner = MatchRunner(p1, p2, "starter_attack", "starter_defense", shuffle_decks=False, seed=3, max_turns=1)
    runner.state.players["p1"].hand = [runner.cards["battle_all_in"], runner.cards["control_focus"], runner.cards["control_haste"], runner.cards["control_guard"]]
    runner.state.players["p2"].hand = [runner.cards["battle_guard"], runner.cards["control_focus"], runner.cards["control_haste"], runner.cards["control_guard"]]
    runner.state.players["p1"].draw_pile = []
    runner.state.players["p2"].draw_pile = []

    result = runner.run()
    battle = result.log["turns"][0]["battle"]

    assert battle["p1_cards"] == ["渾身"]
    assert battle["p2_cards"] == ["受け流し"]
    assert battle["result"] == "win"


def test_simultaneous_attack_is_a_draw() -> None:
    p1 = ScriptedBattleBot([BattleAction("set_pass", ("battle_step_in",))])
    p2 = ScriptedBattleBot([BattleAction("set_pass", ("battle_break",))])
    runner = MatchRunner(p1, p2, "starter_attack", "starter_attack", shuffle_decks=False, seed=3, max_turns=1)
    runner.state.players["p1"].hand = [runner.cards["battle_step_in"], runner.cards["control_focus"], runner.cards["control_reserve"], runner.cards["control_haste"]]
    runner.state.players["p2"].hand = [runner.cards["battle_break"], runner.cards["control_focus"], runner.cards["control_reserve"], runner.cards["control_haste"]]
    runner.state.players["p1"].draw_pile = []
    runner.state.players["p2"].draw_pile = []

    result = runner.run()

    assert result.log["turns"][0]["battle"]["result"] == "draw"
    assert result.state.end_reason == "simultaneous_attack"


def test_reshuffle_happens_only_during_turn_start_draw() -> None:
    runner = MatchRunner(RandomBot(seed=1), RandomBot(seed=2), "starter_attack", "starter_defense", shuffle_decks=False, seed=3)
    runner.state.players["p1"].hand = [runner.cards["battle_press"], runner.cards["control_focus"]]
    runner.state.players["p1"].draw_pile = []
    runner.state.players["p1"].discard_pile = [runner.cards["battle_break"], runner.cards["battle_guard"]]

    payload = runner._start_turn()

    assert payload["p1"]["reshuffled"] is True
    assert runner.state.players["p1"].reshuffle_count == 1
    assert runner.state.players["p1"].reshuffle_turns == [1]


def test_mulligan_draw_does_not_reshuffle_discard_pile() -> None:
    bot = ScriptedBattleBot(mulligan=["battle_press"])
    runner = MatchRunner(bot, RandomBot(seed=2), "starter_attack", "starter_defense", shuffle_decks=False, seed=3)
    runner.state.players["p1"].hand = [runner.cards["battle_press"], runner.cards["control_focus"], runner.cards["control_haste"], runner.cards["control_guard"]]
    runner.state.players["p1"].draw_pile = []
    runner.state.players["p1"].discard_pile = [runner.cards["battle_break"], runner.cards["battle_guard"]]

    discarded = runner._run_mulligan_phase("phase1_mulligan", limit=None)

    assert discarded["p1"] == ["押し込み"]
    assert runner.state.players["p1"].reshuffle_count == 0
    assert all(card.id != "battle_break" for card in runner.state.players["p1"].hand)


def test_dynamic_draft_decks_can_run() -> None:
    runner = MatchRunner(RandomBot(seed=1), RandomBot(seed=2), "starter_attack", "starter_defense", seed=3)
    pool = build_default_card_pool(runner.cards)
    draft = draft_random_decks(pool, runner.cards, runner.rng, deck_size=20, first_player="p1")

    draft_runner = MatchRunner(
        RandomBot(seed=4),
        RandomBot(seed=5),
        draft.deck1.id,
        draft.deck2.id,
        deck_definitions={draft.deck1.id: draft.deck1, draft.deck2.id: draft.deck2},
        seed=6,
    )
    result = draft_runner.run()

    assert result.state.finished is True
    assert len(draft_runner.state.players["p1"].public_deck) == 20
    assert len(draft_runner.state.players["p2"].public_deck) == 20
