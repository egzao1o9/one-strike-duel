from bots.base_bot import BaseBot
from bots.random_bot import RandomBot
from engine.phase_runner import MatchRunner


def test_random_match_runs_to_completion() -> None:
    runner = MatchRunner(RandomBot(seed=1), RandomBot(seed=2), "starter_attack", "starter_defense", seed=3)
    result = runner.run()

    assert result.state.finished is True
    assert result.log["turn_count"] >= 1
    turn = result.log["turns"][0]
    assert "phase1_mulligan" in turn
    assert "control" in turn
    assert "phase3_mulligan" in turn
    assert "battle" in turn


class FixedBattleBot(BaseBot):
    name = "FixedBattleBot"

    def __init__(self, battle_ids: list[str] | None = None) -> None:
        self.battle_ids = battle_ids or []

    def choose_mulligan(self, view):
        return []

    def choose_battle_cards(self, view):
        return list(self.battle_ids)


def test_simultaneous_attack_does_not_end_match_immediately() -> None:
    runner = MatchRunner(
        FixedBattleBot(["battle_step_in"]),
        FixedBattleBot(["battle_break"]),
        "starter_attack",
        "starter_attack",
        shuffle_decks=False,
        max_turns=1,
    )
    runner.state.players["p1"].hand = [
        runner.cards["battle_step_in"],
        runner.cards["control_focus"],
        runner.cards["control_reserve"],
        runner.cards["control_haste"],
    ]
    runner.state.players["p2"].hand = [
        runner.cards["battle_break"],
        runner.cards["control_focus"],
        runner.cards["control_reserve"],
        runner.cards["control_haste"],
    ]
    runner.state.players["p1"].draw_pile = []
    runner.state.players["p2"].draw_pile = []

    result = runner.run()

    assert result.log["turns"][0]["battle"]["result"] == "draw"
    assert result.state.end_reason == "max_turns_reached"


def test_both_players_stuck_flows_to_next_turn() -> None:
    runner = MatchRunner(
        FixedBattleBot([]),
        FixedBattleBot([]),
        "starter_attack",
        "starter_defense",
        shuffle_decks=False,
        max_turns=1,
    )
    runner.state.players["p1"].hand = []
    runner.state.players["p2"].hand = []
    runner.state.players["p1"].draw_pile = []
    runner.state.players["p2"].draw_pile = []

    result = runner.run()

    assert result.log["turns"][0]["battle"]["result"] == "no_decision"
    assert result.state.end_reason == "max_turns_reached"
