from bots.base_bot import BaseBot
from engine.phase_runner import MatchRunner


class ScriptedBot(BaseBot):
    name = "ScriptedBot"

    def __init__(self, mulligan: list[str], battle: str | None = None) -> None:
        self.mulligan = mulligan
        self.battle = battle

    def choose_mulligan(self, view):
        return list(self.mulligan)

    def choose_battle_card(self, view):
        return self.battle or super().choose_battle_card(view)


def test_mulligan_discards_are_public() -> None:
    runner = MatchRunner(ScriptedBot(["battle_step_in"]), ScriptedBot([]), "starter_attack", "starter_defense", shuffle_decks=False, max_turns=1)
    runner.state.players["p1"].hand = [runner.cards["battle_step_in"], runner.cards["battle_press"], runner.cards["battle_feint"], runner.cards["control_focus"]]
    runner.state.players["p1"].draw_pile = [runner.cards["battle_break"]] + runner.state.players["p1"].draw_pile

    result = runner.run()

    assert runner.state.players["p1"].discard_pile[0].id == "battle_step_in"
    assert "踏み込み" in result.log["turns"][0]["phase1_mulligan"]["p1_discarded"]
    assert any(card.id == "battle_break" for card in runner.state.players["p1"].hand)
