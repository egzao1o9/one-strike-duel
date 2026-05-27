from __future__ import annotations

from engine.drafting import AggroDraftBot, GuardDraftBot, RandomDraftBot, RoleBalanceDraftBot, StandardDraftBot


DRAFT_BOT_REGISTRY = {
    "RandomDraftBot": RandomDraftBot,
    "RoleBalanceDraftBot": RoleBalanceDraftBot,
    "StandardDraftBot": StandardDraftBot,
    "AggroDraftBot": AggroDraftBot,
    "GuardDraftBot": GuardDraftBot,
}


def build_draft_bot(name: str, seed: int):
    bot_class = DRAFT_BOT_REGISTRY[name]
    try:
        return bot_class(seed=seed)
    except TypeError:
        return bot_class()
