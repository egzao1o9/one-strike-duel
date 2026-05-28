from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import random

from bots.registry import BOT_REGISTRY, build_bot
from draft.registry import DRAFT_BOT_REGISTRY, build_draft_bot
from engine.card import Card, load_cards
from engine.card_pool import DraftResult, load_card_pool
from engine.drafting import draft_with_bots, summarize_deck
from engine.log_formatter import render_match_log_markdown
from engine.log_profiles import trim_match_log
from engine.phase_runner import MatchRunner


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run one shared-pool draft match.")
    parser.add_argument("--draft-bot1", default="StandardDraftBot", choices=sorted(DRAFT_BOT_REGISTRY))
    parser.add_argument("--draft-bot2", default="GuardDraftBot", choices=sorted(DRAFT_BOT_REGISTRY))
    parser.add_argument("--bot1", default="StandardBot", choices=sorted(BOT_REGISTRY))
    parser.add_argument("--bot2", default="StandardBot", choices=sorted(BOT_REGISTRY))
    parser.add_argument("--seed", type=int, default=71)
    parser.add_argument("--cards", default="data/cards.json")
    parser.add_argument("--pool", default="data/card_pool.json")
    parser.add_argument("--draft-mode", choices=("simple", "full", "market_12", "full_half", "full_12", "full_15", "full_18"), default="simple")
    parser.add_argument("--log-path", default="logs/draft_match.json")
    parser.add_argument("--markdown-path", default="logs/draft_match.md")
    parser.add_argument("--match-log-profile", choices=("minimal", "standard", "full"), default="standard")
    return parser.parse_args()


def draft_mode_deck_size(draft_mode: str) -> int:
    return {
        "market_12": 12,
        "full_half": 10,
        "full_12": 12,
        "full_15": 15,
        "full_18": 18,
    }.get(draft_mode, 20)


def main() -> None:
    args = parse_args()
    cards = load_cards(args.cards)
    pool = load_card_pool(args.pool, cards)
    rng = random.Random(args.seed)
    draft_bot1 = build_draft_bot(args.draft_bot1, args.seed)
    draft_bot2 = build_draft_bot(args.draft_bot2, args.seed + 1)
    draft = draft_with_bots(
        pool,
        cards,
        rng,
        draft_bot1,
        draft_bot2,
        deck_size=draft_mode_deck_size(args.draft_mode),
        draft_mode=args.draft_mode,
    )

    runner = MatchRunner(
        build_bot(args.bot1, args.seed),
        build_bot(args.bot2, args.seed + 1),
        draft.deck1.id,
        draft.deck2.id,
        cards_path=args.cards,
        deck_definitions={draft.deck1.id: draft.deck1, draft.deck2.id: draft.deck2},
        match_id=f"draft_match_seed_{args.seed}",
        seed=args.seed,
    )
    result = runner.run()

    trimmed_match_log = trim_match_log(result.log, args.match_log_profile)
    payload = {
        "draft": build_draft_payload(draft, cards, args.draft_bot1, args.draft_bot2),
        "match": trimmed_match_log,
    }
    log_path = Path(args.log_path)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    markdown_path = Path(args.markdown_path)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text(render_draft_match_markdown(draft, cards, trimmed_match_log), encoding="utf-8")

    print(f"winner={result.state.winner} reason={result.state.end_reason} turns={result.log['turn_count']}")
    print(log_path)
    print(markdown_path)


def build_draft_payload(
    draft: DraftResult,
    cards: dict[str, Card],
    draft_bot1: str,
    draft_bot2: str,
) -> dict[str, object]:
    return {
        "pool_id": draft.pool.id,
        "pool_name": draft.pool.name,
        "first_player": draft.first_player,
        "draft_mode": draft.deck1.metadata.get("draft_mode", "unknown"),
        "draft_bots": {"p1": draft_bot1, "p2": draft_bot2},
        "deck1": list(draft.deck1.all_cards),
        "deck2": list(draft.deck2.all_cards),
        "deck1_public": list(draft.deck1.public_cards),
        "deck1_hidden": list(draft.deck1.hidden_cards),
        "deck1_public_normal": list(draft.deck1.metadata.get("public_normal_cards", [])),
        "deck1_hidden_normal": list(draft.deck1.metadata.get("hidden_normal_cards", [])),
        "deck1_public_rare": list(draft.deck1.metadata.get("public_rare_cards", [])),
        "deck1_hidden_rare": list(draft.deck1.metadata.get("hidden_rare_cards", [])),
        "deck1_starter": list(draft.deck1.metadata.get("starter_cards", [])),
        "deck1_public_market": list(draft.deck1.metadata.get("public_market_cards", [])),
        "deck1_hidden_market": list(draft.deck1.metadata.get("hidden_market_cards", [])),
        "deck1_common_slots": list(draft.deck1.metadata.get("common_slot_cards", [])),
        "deck1_uncommon_slots": list(draft.deck1.metadata.get("uncommon_slot_cards", [])),
        "deck1_rare_slots": list(draft.deck1.metadata.get("rare_slot_cards", [])),
        "deck2_public": list(draft.deck2.public_cards),
        "deck2_hidden": list(draft.deck2.hidden_cards),
        "deck2_public_normal": list(draft.deck2.metadata.get("public_normal_cards", [])),
        "deck2_hidden_normal": list(draft.deck2.metadata.get("hidden_normal_cards", [])),
        "deck2_public_rare": list(draft.deck2.metadata.get("public_rare_cards", [])),
        "deck2_hidden_rare": list(draft.deck2.metadata.get("hidden_rare_cards", [])),
        "deck2_starter": list(draft.deck2.metadata.get("starter_cards", [])),
        "deck2_public_market": list(draft.deck2.metadata.get("public_market_cards", [])),
        "deck2_hidden_market": list(draft.deck2.metadata.get("hidden_market_cards", [])),
        "deck2_common_slots": list(draft.deck2.metadata.get("common_slot_cards", [])),
        "deck2_uncommon_slots": list(draft.deck2.metadata.get("uncommon_slot_cards", [])),
        "deck2_rare_slots": list(draft.deck2.metadata.get("rare_slot_cards", [])),
        "deck1_rarity_counts": dict(draft.deck1.metadata.get("final_rarity_counts", {})),
        "deck2_rarity_counts": dict(draft.deck2.metadata.get("final_rarity_counts", {})),
        "picks": [
            {
                "number": pick.number,
                "round": pick.round_number,
                "player": pick.player_id,
                "visibility": pick.visibility,
                "phase": pick.phase,
                "pick_position": pick.pick_position,
                "offer_card_ids": list(pick.offer_card_ids),
                "offer_card_names": [cards[card_id].name for card_id in pick.offer_card_ids],
                "offer_groups": [list(group) for group in pick.offer_groups],
                "offer_group_names": [[cards[card_id].name for card_id in group] for group in pick.offer_groups],
                "selected_card_ids": list(pick.selected_card_ids or ((pick.card_id,) if pick.card_id else tuple())),
                "selected_card_names": [cards[card_id].name for card_id in (pick.selected_card_ids or ((pick.card_id,) if pick.card_id else tuple()))],
                "card_id": pick.card_id,
                "card_name": cards[pick.card_id].name if pick.card_id else "",
            }
            for pick in draft.picks
        ],
    }


def render_draft_match_markdown(draft: DraftResult, cards: dict[str, Card], match_log: dict[str, object]) -> str:
    deck1_summary = summarize_deck(draft.deck1.all_cards, cards)
    deck2_summary = summarize_deck(draft.deck2.all_cards, cards)
    lines = [
        "# Draft Match",
        "",
        "## Draft Summary",
        "",
        f"- Pool: `{draft.pool.id}` ({draft.pool.name})",
        f"- First Pick: `{draft.first_player}`",
        f"- Draft Mode: `{draft.deck1.metadata.get('draft_mode', 'unknown')}`",
        f"- Deck Size: {len(draft.deck1.all_cards)}",
        f"- P1 Public / Hidden: {len(draft.deck1.public_cards)} / {len(draft.deck1.hidden_cards)}",
        f"- P2 Public / Hidden: {len(draft.deck2.public_cards)} / {len(draft.deck2.hidden_cards)}",
        "",
        "## Role Balance",
        "",
        "| Deck | Battle | Control | Blessing | Red | Blue | Green | White | Common | Uncommon | Rare |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        _render_summary_row("P1", deck1_summary),
        _render_summary_row("P2", deck2_summary),
        "",
        "## Drafted Decks",
        "",
    ]
    if draft.deck1.metadata.get("starter_cards"):
        lines[8:8] = [
            f"- P1 Starter / Public Market / Hidden Market: {len(draft.deck1.metadata.get('starter_cards', []))} / {len(draft.deck1.metadata.get('public_market_cards', []))} / {len(draft.deck1.metadata.get('hidden_market_cards', []))}",
            f"- P2 Starter / Public Market / Hidden Market: {len(draft.deck2.metadata.get('starter_cards', []))} / {len(draft.deck2.metadata.get('public_market_cards', []))} / {len(draft.deck2.metadata.get('hidden_market_cards', []))}",
        ]
        lines.extend(render_deck_table("P1 Starter", tuple(draft.deck1.metadata.get("starter_cards", [])), cards))
        lines.append("")
        lines.extend(render_deck_table("P1 Public Market", tuple(draft.deck1.metadata.get("public_market_cards", [])), cards))
        lines.append("")
        lines.extend(render_deck_table("P1 Hidden Market", tuple(draft.deck1.metadata.get("hidden_market_cards", [])), cards))
        lines.append("")
        lines.extend(render_deck_table("P1 Common Slots", tuple(draft.deck1.metadata.get("common_slot_cards", [])), cards))
        lines.append("")
        lines.extend(render_deck_table("P1 Uncommon Slots", tuple(draft.deck1.metadata.get("uncommon_slot_cards", [])), cards))
        lines.append("")
        lines.extend(render_deck_table("P1 Rare Slots", tuple(draft.deck1.metadata.get("rare_slot_cards", [])), cards))
        lines.append("")
        lines.extend(render_deck_table("P2 Starter", tuple(draft.deck2.metadata.get("starter_cards", [])), cards))
        lines.append("")
        lines.extend(render_deck_table("P2 Public Market", tuple(draft.deck2.metadata.get("public_market_cards", [])), cards))
        lines.append("")
        lines.extend(render_deck_table("P2 Hidden Market", tuple(draft.deck2.metadata.get("hidden_market_cards", [])), cards))
        lines.append("")
        lines.extend(render_deck_table("P2 Common Slots", tuple(draft.deck2.metadata.get("common_slot_cards", [])), cards))
        lines.append("")
        lines.extend(render_deck_table("P2 Uncommon Slots", tuple(draft.deck2.metadata.get("uncommon_slot_cards", [])), cards))
        lines.append("")
        lines.extend(render_deck_table("P2 Rare Slots", tuple(draft.deck2.metadata.get("rare_slot_cards", [])), cards))
        lines.append("")
    else:
        lines[8:8] = [
            f"- P1 Normal Public / Hidden: {len(draft.deck1.metadata.get('public_normal_cards', []))} / {len(draft.deck1.metadata.get('hidden_normal_cards', []))}",
            f"- P1 Rare Public / Hidden: {len(draft.deck1.metadata.get('public_rare_cards', []))} / {len(draft.deck1.metadata.get('hidden_rare_cards', []))}",
            f"- P2 Normal Public / Hidden: {len(draft.deck2.metadata.get('public_normal_cards', []))} / {len(draft.deck2.metadata.get('hidden_normal_cards', []))}",
            f"- P2 Rare Public / Hidden: {len(draft.deck2.metadata.get('public_rare_cards', []))} / {len(draft.deck2.metadata.get('hidden_rare_cards', []))}",
        ]
        lines.extend(render_deck_table("P1 Public Normal", tuple(draft.deck1.metadata.get("public_normal_cards", [])), cards))
        lines.append("")
        lines.extend(render_deck_table("P1 Hidden Normal", tuple(draft.deck1.metadata.get("hidden_normal_cards", [])), cards))
        lines.append("")
        lines.extend(render_deck_table("P1 Public Rare", tuple(draft.deck1.metadata.get("public_rare_cards", [])), cards))
        lines.append("")
        lines.extend(render_deck_table("P1 Hidden Rare", tuple(draft.deck1.metadata.get("hidden_rare_cards", [])), cards))
        lines.append("")
        lines.extend(render_deck_table("P2 Public Normal", tuple(draft.deck2.metadata.get("public_normal_cards", [])), cards))
        lines.append("")
        lines.extend(render_deck_table("P2 Hidden Normal", tuple(draft.deck2.metadata.get("hidden_normal_cards", [])), cards))
        lines.append("")
        lines.extend(render_deck_table("P2 Public Rare", tuple(draft.deck2.metadata.get("public_rare_cards", [])), cards))
        lines.append("")
        lines.extend(render_deck_table("P2 Hidden Rare", tuple(draft.deck2.metadata.get("hidden_rare_cards", [])), cards))
        lines.append("")
    lines.extend(
        [
            "## Pick Order",
            "",
            "| Pick | Round | Player | Phase | Position | Selected | Rarity Mix | Offer |",
            "|---:|---:|---|---|---:|---|---|---|",
        ]
    )
    for pick in draft.picks:
        selected_ids = pick.selected_card_ids or ((pick.card_id,) if pick.card_id else tuple())
        selected_text = ", ".join(cards[card_id].name for card_id in selected_ids)
        rarity_mix = Counter(cards[card_id].rarity for card_id in selected_ids)
        rarity_text = ", ".join(f"{rarity}:{count}" for rarity, count in sorted(rarity_mix.items()))
        if pick.offer_groups:
            offer_text = " / ".join(", ".join(cards[card_id].name for card_id in group) for group in pick.offer_groups)
        else:
            offer_text = ", ".join(cards[card_id].name for card_id in pick.offer_card_ids)
        lines.append(
            f"| {pick.number} | {pick.round_number} | `{pick.player_id}` | `{pick.phase}` | {pick.pick_position} | "
            f"{selected_text} | {rarity_text} | {offer_text} |"
        )
    lines.extend(["", "## Match Log", "", render_match_log_markdown(match_log).rstrip(), ""])
    return "\n".join(lines).rstrip() + "\n"


def render_deck_table(title: str, card_ids: tuple[str, ...], cards: dict[str, Card]) -> list[str]:
    lines = [
        f"### {title}",
        "",
        "| Count | Card | ID | Rarity | Type | A | B | S |",
        "|---:|---|---|---|---|---:|---:|---:|",
    ]
    counts: dict[str, int] = {}
    for card_id in card_ids:
        counts[card_id] = counts.get(card_id, 0) + 1
    for card_id in sorted(counts):
        card = cards[card_id]
        lines.append(
            f"| {counts[card_id]} | {card.name} | `{card.id}` | `{card.rarity}` | `{card.type}` | {card.attack} | {card.block} | {card.speed} |"
        )
    return lines


def _render_summary_row(label: str, summary) -> str:
    return (
        f"| {label} | {summary.battle_count} | {summary.control_count} | {summary.blessing_count} | "
        f"{summary.role_counts['red']} | {summary.role_counts['blue']} | "
        f"{summary.role_counts['green']} | {summary.role_counts['white']} | "
        f"{summary.rarity_counts['common']} | {summary.rarity_counts['uncommon']} | {summary.rarity_counts['rare']} |"
    )


if __name__ == "__main__":
    main()
