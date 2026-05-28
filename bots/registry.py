from __future__ import annotations

from bots.attack_bot import AttackBot
from bots.burst_bot import BurstBot
from bots.defense_bot import DefenseBot
from bots.disrupt_bot import DisruptBot
from bots.greedy_bot import GreedyBot
from bots.public_info_bot import AggroBot, BlessingBot, ControlBot, GuardBot, StandardBot
from bots.random_bot import RandomBot
from bots.risk_bot import RiskBot
from bots.tempo_bot import TempoBot
from bots.turtle_bot import TurtleBot


BOT_REGISTRY = {
    "AttackBot": AttackBot,
    "BurstBot": BurstBot,
    "DefenseBot": DefenseBot,
    "DisruptBot": DisruptBot,
    "GreedyBot": GreedyBot,
    "GuardBot": GuardBot,
    "ControlBot": ControlBot,
    "BlessingBot": BlessingBot,
    "RandomBot": RandomBot,
    "RiskBot": RiskBot,
    "StandardBot": StandardBot,
    "TempoBot": TempoBot,
    "TurtleBot": TurtleBot,
    "AggroBot": AggroBot,
}


def build_bot(name: str, seed: int):
    bot_class = BOT_REGISTRY[name]
    try:
        return bot_class(seed=seed)
    except TypeError:
        return bot_class()
