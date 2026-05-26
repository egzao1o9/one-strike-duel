from bots.base_bot import BaseBot
from engine.phase_runner import MatchRunner


class EffectBot(BaseBot):
    name = "EffectBot"

    def __init__(self, control: str | None, battle: str | None) -> None:
        self.control = control
        self.battle = battle

    def choose_mulligan(self, view):
        return []

    def choose_control_card(self, view):
        return self.control

    def choose_battle_card(self, view):
        return self.battle


def test_next_turn_draw_bonus_is_applied() -> None:
    bot1 = EffectBot("control_reserve", "battle_guard")
    bot2 = EffectBot(None, "battle_guard")
    runner = MatchRunner(bot1, bot2, "starter_defense", "starter_defense", shuffle_decks=False, max_turns=2)

    runner.state.players["p1"].hand = [
        runner.cards["control_reserve"],
        runner.cards["battle_guard"],
        runner.cards["battle_press"],
        runner.cards["battle_counter"],
    ]
    runner.state.players["p2"].hand = [
        runner.cards["battle_guard"],
        runner.cards["battle_press"],
        runner.cards["battle_counter"],
        runner.cards["battle_wall"],
    ]
    runner.state.players["p1"].draw_pile = [runner.cards["battle_feint"], runner.cards["battle_dash"]]
    runner.state.players["p2"].draw_pile = [runner.cards["battle_feint"]]

    runner.run()

    remaining_ids = {card.id for card in runner.state.players["p1"].hand}
    assert "battle_feint" in remaining_ids
    assert "battle_dash" in remaining_ids
