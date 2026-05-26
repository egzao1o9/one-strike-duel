from __future__ import annotations

from engine.drafting import RandomDraftBot, RoleBalanceDraftBot


DRAFT_BOT_REGISTRY = {
    "RandomDraftBot": RandomDraftBot,
    "RoleBalanceDraftBot": RoleBalanceDraftBot,
}


def build_draft_bot(name: str, seed: int):
    bot_class = DRAFT_BOT_REGISTRY[name]
    try:
        return bot_class(seed=seed)
    except TypeError:
        return bot_class()
