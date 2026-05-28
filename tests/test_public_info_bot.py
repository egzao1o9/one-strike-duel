from bots.public_info_bot import AggroBot, StandardBot
from bots.random_bot import RandomBot
from engine.phase_runner import MatchRunner
from sim.run_draft_bot_suite import resolve_worker_count


def test_standard_bot_forbids_opening_set_pass_on_turn_one() -> None:
    runner = MatchRunner(
        StandardBot(seed=11),
        RandomBot(seed=12),
        "starter_attack",
        "starter_defense",
        shuffle_decks=False,
        seed=13,
        max_turns=1,
    )
    runner.state.turn = 1
    runner.state.phase = "battle_select"
    runner.state.battle_starting_player = "p1"
    runner.state.acting_player = "p1"
    runner.state.players["p1"].hand = [
        runner.cards["battle_press"],
        runner.cards["battle_break"],
        runner.cards["control_focus"],
        runner.cards["control_haste"],
    ]
    runner.state.players["p2"].hand = [
        runner.cards["battle_guard"],
        runner.cards["battle_counter"],
        runner.cards["control_focus"],
        runner.cards["control_haste"],
    ]

    bot = runner.bot_map["p1"]
    actions = bot._legal_actions(runner.state.build_view("p1"))

    assert all(action.action_type != "set_pass" for action in actions)
    assert any(action.action_type == "set" for action in actions)
    assert all(action.action_type != "pass" for action in actions)


def test_standard_bot_keeps_set_pass_as_closing_option() -> None:
    runner = MatchRunner(
        StandardBot(seed=21),
        RandomBot(seed=22),
        "starter_attack",
        "starter_defense",
        shuffle_decks=False,
        seed=23,
        max_turns=1,
    )
    runner.state.turn = 2
    runner.state.phase = "battle_select"
    runner.state.battle_starting_player = "p1"
    runner.state.acting_player = "p1"
    runner.state.players["p2"].battle_passed = True
    runner.state.players["p1"].hand = [
        runner.cards["battle_press"],
        runner.cards["battle_break"],
        runner.cards["control_focus"],
        runner.cards["control_haste"],
    ]
    runner.state.players["p2"].hand = [
        runner.cards["battle_guard"],
        runner.cards["battle_counter"],
        runner.cards["control_focus"],
        runner.cards["control_haste"],
    ]

    bot = runner.bot_map["p1"]
    actions = bot._legal_actions(runner.state.build_view("p1"))

    assert any(action.action_type == "set_pass" for action in actions)


def test_standard_bot_opens_in_probe_mode() -> None:
    runner = MatchRunner(
        StandardBot(seed=31),
        RandomBot(seed=32),
        "starter_attack",
        "starter_defense",
        shuffle_decks=False,
        seed=33,
        max_turns=1,
    )
    runner.state.turn = 1
    runner.state.phase = "battle_select"
    runner.state.battle_starting_player = "p1"
    runner.state.acting_player = "p1"
    runner.state.players["p1"].hand = [
        runner.cards["battle_press"],
        runner.cards["battle_break"],
        runner.cards["control_focus"],
        runner.cards["control_haste"],
    ]
    runner.state.players["p2"].hand = [
        runner.cards["battle_guard"],
        runner.cards["battle_counter"],
        runner.cards["control_focus"],
        runner.cards["control_haste"],
    ]

    bot = runner.bot_map["p1"]
    assert bot._choose_battle_mode(runner.state.build_view("p1")) == "probe"


def test_standard_bot_uses_defense_mode_when_under_pressure() -> None:
    runner = MatchRunner(
        StandardBot(seed=41),
        RandomBot(seed=42),
        "starter_attack",
        "starter_attack",
        shuffle_decks=False,
        seed=43,
        max_turns=1,
    )
    runner.state.turn = 2
    runner.state.phase = "battle_select"
    runner.state.battle_starting_player = "p1"
    runner.state.acting_player = "p1"
    runner.state.players["p2"].set_cards = [runner.cards["battle_press"], runner.cards["battle_counter"]]
    runner.state.players["p1"].hand = [
        runner.cards["battle_wall"],
        runner.cards["battle_wall"],
        runner.cards["control_focus"],
        runner.cards["control_haste"],
    ]
    runner.state.players["p2"].hand = [
        runner.cards["battle_break"],
        runner.cards["battle_dash"],
        runner.cards["control_focus"],
        runner.cards["control_haste"],
    ]

    bot = runner.bot_map["p1"]
    assert bot._choose_battle_mode(runner.state.build_view("p1")) == "defense"


def test_standard_bot_avoids_early_two_card_set_pass() -> None:
    runner = MatchRunner(
        StandardBot(seed=51),
        RandomBot(seed=52),
        "starter_attack",
        "starter_attack",
        shuffle_decks=False,
        seed=53,
        max_turns=1,
    )
    runner.state.turn = 1
    runner.state.phase = "battle_select"
    runner.state.battle_starting_player = "p1"
    runner.state.acting_player = "p1"
    runner.state.players["p1"].set_cards = [runner.cards["battle_press"]]
    runner.state.players["p2"].set_cards = [runner.cards["battle_counter"]]
    runner.state.players["p1"].hand = [
        runner.cards["battle_break"],
        runner.cards["battle_guard"],
        runner.cards["control_focus"],
        runner.cards["control_haste"],
    ]
    runner.state.players["p2"].hand = [
        runner.cards["battle_dash"],
        runner.cards["battle_break"],
        runner.cards["control_focus"],
        runner.cards["control_haste"],
    ]

    bot = runner.bot_map["p1"]
    action = bot.choose_battle_action(runner.state.build_view("p1"))

    assert action.action_type != "set_pass"


def test_standard_bot_avoids_early_one_vs_two_pass() -> None:
    runner = MatchRunner(
        StandardBot(seed=61),
        RandomBot(seed=62),
        "starter_attack",
        "starter_attack",
        shuffle_decks=False,
        seed=63,
        max_turns=1,
    )
    runner.state.turn = 1
    runner.state.phase = "battle_select"
    runner.state.battle_starting_player = "p1"
    runner.state.acting_player = "p1"
    runner.state.players["p1"].set_cards = [runner.cards["battle_press"]]
    runner.state.players["p2"].set_cards = [runner.cards["battle_counter"]]
    runner.state.players["p1"].hand = [
        runner.cards["battle_guard"],
        runner.cards["battle_break"],
        runner.cards["control_focus"],
        runner.cards["control_haste"],
    ]
    runner.state.players["p2"].hand = [
        runner.cards["battle_dash"],
        runner.cards["battle_break"],
        runner.cards["control_focus"],
        runner.cards["control_haste"],
    ]

    bot = runner.bot_map["p1"]
    action = bot.choose_battle_action(runner.state.build_view("p1"))

    assert action.action_type != "pass"


def test_standard_bot_forbids_pass_with_control_only_set_when_playable() -> None:
    runner = MatchRunner(
        StandardBot(seed=64),
        RandomBot(seed=65),
        "starter_attack",
        "starter_attack",
        shuffle_decks=False,
        seed=66,
        max_turns=1,
    )
    runner.state.turn = 2
    runner.state.phase = "battle_select"
    runner.state.battle_starting_player = "p1"
    runner.state.acting_player = "p1"
    runner.state.players["p1"].set_cards = [runner.cards["control_focus"]]
    runner.state.players["p2"].set_cards = [runner.cards["battle_counter"]]
    runner.state.players["p1"].hand = [
        runner.cards["battle_guard"],
        runner.cards["control_haste"],
    ]

    bot = runner.bot_map["p1"]
    actions = bot._legal_actions(runner.state.build_view("p1"))

    assert all(action.action_type != "pass" for action in actions)


def test_aggro_bot_does_not_open_with_empty_pass() -> None:
    runner = MatchRunner(
        AggroBot(seed=67),
        RandomBot(seed=68),
        "starter_attack",
        "starter_attack",
        shuffle_decks=False,
        seed=69,
        max_turns=1,
    )
    runner.state.turn = 1
    runner.state.phase = "battle_select"
    runner.state.battle_starting_player = "p1"
    runner.state.acting_player = "p1"
    runner.state.players["p1"].hand = [
        runner.cards["battle_attack"],
        runner.cards["battle_step"],
        runner.cards["control_haste"],
        runner.cards["control_pressure"],
    ]
    runner.state.players["p2"].hand = [
        runner.cards["battle_guard"],
        runner.cards["battle_counter"],
        runner.cards["control_focus"],
        runner.cards["control_haste"],
    ]

    bot = runner.bot_map["p1"]
    action = bot.choose_battle_action(runner.state.build_view("p1"))

    assert action.action_type != "pass"


def test_standard_bot_values_blank_first_against_large_single_card_threat() -> None:
    runner = MatchRunner(
        StandardBot(seed=71),
        RandomBot(seed=72),
        "starter_attack",
        "starter_attack",
        shuffle_decks=False,
        seed=73,
        max_turns=1,
    )
    runner.state.turn = 1
    runner.state.phase = "control"
    runner.state.players["p1"].hand = [
        runner.cards["control_blank_first"],
        runner.cards["control_focus"],
        runner.cards["battle_guard"],
        runner.cards["battle_counter"],
    ]
    runner.state.players["p2"].public_deck = (
        "battle_step_in",
        "battle_all_in",
        "battle_dash",
        "battle_power_attack",
    )
    runner.state.players["p2"].hidden_deck = (
        "battle_guard",
        "battle_press",
        "battle_break",
        "battle_step",
    )

    bot = runner.bot_map["p1"]
    picked = bot.choose_control_card(runner.state.build_view("p1"))

    assert picked == "control_blank_first"


def test_standard_bot_values_crush_spirit_when_block_is_short() -> None:
    runner = MatchRunner(
        StandardBot(seed=81),
        RandomBot(seed=82),
        "starter_attack",
        "starter_attack",
        shuffle_decks=False,
        seed=83,
        max_turns=1,
    )
    runner.state.turn = 1
    runner.state.phase = "control"
    runner.state.players["p1"].hand = [
        runner.cards["control_crush_spirit"],
        runner.cards["control_focus"],
        runner.cards["battle_attack"],
        runner.cards["battle_step"],
    ]
    runner.state.players["p2"].public_deck = (
        "battle_step_in",
        "battle_all_in",
        "battle_heavy_swing",
        "battle_power_attack",
    )
    runner.state.players["p2"].hidden_deck = (
        "battle_press",
        "battle_break",
        "battle_step",
        "battle_attack",
    )

    bot = runner.bot_map["p1"]
    picked = bot.choose_control_card(runner.state.build_view("p1"))

    assert picked == "control_crush_spirit"


def test_resolve_worker_count_leaves_one_cpu_when_auto() -> None:
    workers = resolve_worker_count(0, 6)

    assert workers >= 1
