from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import json
from pathlib import Path
import random

from engine.card import Card
from engine.deck import DeckDefinition


RARITY_POOL_COUNTS = {
    "common": 5,
    "uncommon": 2,
    "rare": 2,
}


@dataclass(frozen=True)
class CardPoolEntry:
    card_id: str
    count: int


@dataclass(frozen=True)
class CardPoolDefinition:
    id: str
    name: str
    entries: tuple[CardPoolEntry, ...]

    @property
    def total_cards(self) -> int:
        return sum(entry.count for entry in self.entries)


@dataclass(frozen=True)
class DraftPick:
    number: int
    player_id: str
    card_id: str = ""
    visibility: str = "public"
    phase: str = "single"
    offer_card_ids: tuple[str, ...] = ()
    offer_groups: tuple[tuple[str, ...], ...] = ()
    selected_card_ids: tuple[str, ...] = ()
    pick_position: int = 1
    round_number: int = 1


@dataclass(frozen=True)
class DraftResult:
    pool: CardPoolDefinition
    deck1: DeckDefinition
    deck2: DeckDefinition
    picks: tuple[DraftPick, ...]
    first_player: str


def load_card_pool(path: str | Path, cards: dict[str, Card]) -> CardPoolDefinition:
    file_path = Path(path)
    with file_path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    entries = tuple(
        CardPoolEntry(card_id=item["card_id"], count=int(item["count"]))
        for item in payload["entries"]
    )
    _validate_pool_entries(entries, cards)
    return CardPoolDefinition(
        id=payload["id"],
        name=payload["name"],
        entries=entries,
    )


def build_default_card_pool(cards: dict[str, Card], *, pool_id: str = "base_pool", name: str = "Base Card Pool") -> CardPoolDefinition:
    entries = tuple(
        CardPoolEntry(card_id=card.id, count=pool_count_for_rarity(card.rarity))
        for card in sorted(cards.values(), key=lambda item: item.id)
    )
    return CardPoolDefinition(id=pool_id, name=name, entries=entries)


def pool_count_for_rarity(rarity: str) -> int:
    try:
        return RARITY_POOL_COUNTS[rarity]
    except KeyError as exc:
        raise ValueError(f"unsupported rarity for card pool: {rarity}") from exc


def build_card_pool_payload(pool: CardPoolDefinition) -> dict[str, object]:
    return {
        "id": pool.id,
        "name": pool.name,
        "entries": [{"card_id": entry.card_id, "count": entry.count} for entry in pool.entries],
    }


def draft_random_decks(
    pool: CardPoolDefinition,
    cards: dict[str, Card],
    rng: random.Random,
    *,
    deck_size: int = 20,
    first_player: str | None = None,
    all_public: bool = True,
) -> DraftResult:
    _validate_pool_entries(pool.entries, cards)
    if pool.total_cards < deck_size * 2:
        raise ValueError("card pool does not contain enough cards for both drafted decks")

    draft_order_first = first_player or rng.choice(("p1", "p2"))
    counts = Counter({entry.card_id: entry.count for entry in pool.entries})
    drafted: dict[str, list[str]] = {"p1": [], "p2": []}
    picks: list[DraftPick] = []

    for pick_number in range(1, deck_size * 2 + 1):
        player_id = _draft_player_for_pick(draft_order_first, pick_number)
        card_id = _pick_random_card_id(counts, rng)
        drafted[player_id].append(card_id)
        counts[card_id] -= 1
        if counts[card_id] == 0:
            del counts[card_id]
        picks.append(DraftPick(number=pick_number, player_id=player_id, card_id=card_id))

    deck1 = build_drafted_deck("draft_p1", "Draft Deck P1", drafted["p1"], all_public=all_public)
    deck2 = build_drafted_deck("draft_p2", "Draft Deck P2", drafted["p2"], all_public=all_public)
    return DraftResult(
        pool=pool,
        deck1=deck1,
        deck2=deck2,
        picks=tuple(picks),
        first_player=draft_order_first,
    )


def build_drafted_deck(deck_id: str, name: str, card_ids: list[str], *, all_public: bool = True) -> DeckDefinition:
    if all_public:
        return DeckDefinition(id=deck_id, name=name, public_cards=tuple(card_ids), hidden_cards=tuple())
    midpoint = len(card_ids) // 2
    return DeckDefinition(
        id=deck_id,
        name=name,
        public_cards=tuple(card_ids[:midpoint]),
        hidden_cards=tuple(card_ids[midpoint:]),
    )


def _draft_player_for_pick(first_player: str, pick_number: int) -> str:
    if pick_number % 2 == 1:
        return first_player
    return "p2" if first_player == "p1" else "p1"


def _pick_random_card_id(counts: Counter[str], rng: random.Random) -> str:
    weighted_ids = [card_id for card_id, count in counts.items() for _ in range(count)]
    return rng.choice(weighted_ids)


def _validate_pool_entries(entries: tuple[CardPoolEntry, ...], cards: dict[str, Card]) -> None:
    seen: set[str] = set()
    for entry in entries:
        if entry.card_id in seen:
            raise ValueError(f"duplicate card id in card pool: {entry.card_id}")
        if entry.card_id not in cards:
            raise ValueError(f"unknown card id in card pool: {entry.card_id}")
        if entry.count <= 0:
            raise ValueError(f"invalid pool count for {entry.card_id}: {entry.count}")
        seen.add(entry.card_id)
