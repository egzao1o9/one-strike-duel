from bots.registry import BOT_REGISTRY, build_bot
from engine.phase_runner import MatchRunner


def test_bot_registry_can_build_all_bots() -> None:
    for index, bot_name in enumerate(sorted(BOT_REGISTRY)):
        bot = build_bot(bot_name, index)
        assert bot.name == bot_name


def test_new_bots_can_finish_matches() -> None:
    bot_names = ["BurstBot", "DisruptBot", "TempoBot", "TurtleBot"]
    for index, bot_name in enumerate(bot_names):
        runner = MatchRunner(
            build_bot(bot_name, 100 + index),
            build_bot("GreedyBot", 200 + index),
            "starter_balanced",
            "starter_speed",
            seed=300 + index,
            max_turns=10,
        )
        result = runner.run()
        assert result.state.finished is True
        assert result.log["turn_count"] >= 1
