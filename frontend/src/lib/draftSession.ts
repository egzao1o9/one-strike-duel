import { getBasePoolEntries, summarizePoolByRarity } from "./cardPool";
import { getAllCards } from "./cards";
import { createSeededRandom } from "./random";
import { chooseStandardMarketPick } from "./standardDraftBot";
import type { CardDefinition, CardRarity } from "../types/cards";
import type { DraftDeckState, DraftPoolSnapshot, DraftSession, DraftSlotGroup, PlayerId, PrototypeLogEntry } from "../types/prototype";

interface AvailablePool {
  cardsById: Map<string, CardDefinition>;
  counts: Map<string, number>;
}

const STARTER_CARD_IDS = ["battle_attack", "battle_defend", "battle_step"] as const;
const MARKET_VISIBLE_COUNT = 3;
const MARKET_SLOT_CAPS = {
  common: 2,
  uncommon: 5,
  rare: 2,
} as const;

function cloneDeckState(starterCards: CardDefinition[]): DraftDeckState {
  return {
    starter: [...starterCards],
    publicCards: [],
    hiddenCards: [],
    commonSlots: [],
    uncommonSlots: [],
    rareSlots: [],
  };
}

function cloneDeck(deck: DraftDeckState): DraftDeckState {
  return {
    starter: [...deck.starter],
    publicCards: [...deck.publicCards],
    hiddenCards: [...deck.hiddenCards],
    commonSlots: [...deck.commonSlots],
    uncommonSlots: [...deck.uncommonSlots],
    rareSlots: [...deck.rareSlots],
  };
}

function flattenDeck(deck: DraftDeckState) {
  return [...deck.starter, ...deck.publicCards, ...deck.hiddenCards];
}

function countDeck(deck: DraftDeckState) {
  return flattenDeck(deck).length;
}

function summarizeDeckRarity(deck: DraftDeckState) {
  return flattenDeck(deck).reduce<Record<CardRarity, number>>(
    (acc, card) => {
      acc[card.rarity] += 1;
      return acc;
    },
    { common: 0, uncommon: 0, rare: 0 },
  );
}

function buildAvailablePool(): AvailablePool {
  const entries = getBasePoolEntries();
  return {
    cardsById: new Map(entries.map((entry) => [entry.card.id, entry.card])),
    counts: new Map(entries.map((entry) => [entry.card.id, entry.count])),
  };
}

function hydratePool(session: DraftSession): AvailablePool {
  const base = buildAvailablePool();
  return {
    cardsById: base.cardsById,
    counts: new Map(Object.entries(session.poolCounts).filter(([, count]) => count > 0)),
  };
}

function serializePool(pool: AvailablePool) {
  return Object.fromEntries(pool.counts.entries());
}

function cloneSession(session: DraftSession): DraftSession {
  return {
    ...session,
    currentStep: { ...session.currentStep },
    decks: {
      p1: cloneDeck(session.decks.p1),
      p2: cloneDeck(session.decks.p2),
    },
    poolCounts: { ...session.poolCounts },
    marketRows: {
      common: { ...session.marketRows.common, visibleCards: [...session.marketRows.common.visibleCards] },
      uncommon: { ...session.marketRows.uncommon, visibleCards: [...session.marketRows.uncommon.visibleCards] },
      rare: { ...session.marketRows.rare, visibleCards: [...session.marketRows.rare.visibleCards] },
    },
    logs: [...session.logs],
    poolSnapshot: {
      remainingTotal: session.poolSnapshot.remainingTotal,
      remainingByRarity: { ...session.poolSnapshot.remainingByRarity },
    },
    pendingRefillRarity: session.pendingRefillRarity,
    pendingVisibleGapIndex: session.pendingVisibleGapIndex,
    pendingCpuTurn: session.pendingCpuTurn,
  };
}

function consumeCard(pool: AvailablePool, cardId: string) {
  const current = pool.counts.get(cardId) ?? 0;
  if (current <= 0) {
    throw new Error(`Pool exhaustion: ${cardId}`);
  }
  if (current === 1) {
    pool.counts.delete(cardId);
  } else {
    pool.counts.set(cardId, current - 1);
  }
}

function drawCardsByRarity(pool: AvailablePool, rarity: CardRarity, count: number, rng: ReturnType<typeof createSeededRandom>) {
  const weightedIds: string[] = [];
  for (const [cardId, copies] of pool.counts.entries()) {
    const card = pool.cardsById.get(cardId);
    if (!card || card.rarity !== rarity) {
      continue;
    }
    for (let index = 0; index < copies; index += 1) {
      weightedIds.push(cardId);
    }
  }

  if (weightedIds.length < count) {
    throw new Error(`Not enough ${rarity} cards left in pool.`);
  }

  const pickedIds: string[] = [];
  while (pickedIds.length < count) {
    const pickedIndex = rng.int(weightedIds.length);
    const pickedId = weightedIds[pickedIndex];
    pickedIds.push(pickedId);
    weightedIds.splice(pickedIndex, 1);
  }

  pickedIds.forEach((cardId) => consumeCard(pool, cardId));
  return pickedIds.map((cardId) => pool.cardsById.get(cardId)!);
}

function buildPoolSnapshot(pool: AvailablePool): DraftPoolSnapshot {
  return {
    remainingTotal: [...pool.counts.values()].reduce((sum, count) => sum + count, 0),
    remainingByRarity: summarizePoolByRarity(
      [...pool.counts.entries()].flatMap(([cardId, count]) => {
        const card = pool.cardsById.get(cardId);
        return card ? [{ card, count }] : [];
      }),
    ),
  };
}

function starterCards() {
  const cardsById = new Map(getAllCards().map((card) => [card.id, card]));
  return STARTER_CARD_IDS.map((cardId) => {
    const card = cardsById.get(cardId);
    if (!card) {
      throw new Error(`Missing starter card: ${cardId}`);
    }
    return card;
  });
}

function pushLog(
  session: DraftSession,
  kind: PrototypeLogEntry["kind"],
  text: string,
  draftEvent?: PrototypeLogEntry["draftEvent"],
) {
  session.logs.push({
    id: `log-${session.logs.length + 1}`,
    kind,
    text,
    draftEvent,
  });
}

function playerLabel(playerId: PlayerId) {
  return playerId === "p1" ? "プレイヤー" : "CPU";
}

function rarityLabel(rarity: CardRarity) {
  return rarity === "rare" ? "Rare" : rarity === "uncommon" ? "Uncommon" : "Common";
}

function nextSlotName(card: CardDefinition, deck: DraftDeckState) {
  if (card.rarity === "rare") {
    return deck.rareSlots.length < MARKET_SLOT_CAPS.rare ? "rareSlots" : null;
  }
  if (card.rarity === "uncommon") {
    if (deck.uncommonSlots.length < MARKET_SLOT_CAPS.uncommon) {
      return "uncommonSlots";
    }
    return deck.rareSlots.length < MARKET_SLOT_CAPS.rare ? "rareSlots" : null;
  }
  if (deck.commonSlots.length < MARKET_SLOT_CAPS.common) {
    return "commonSlots";
  }
  if (deck.uncommonSlots.length < MARKET_SLOT_CAPS.uncommon) {
    return "uncommonSlots";
  }
  return deck.rareSlots.length < MARKET_SLOT_CAPS.rare ? "rareSlots" : null;
}

function canTakeCard(card: CardDefinition, deck: DraftDeckState) {
  return nextSlotName(card, deck) !== null;
}

function canTakeRarity(rarity: CardRarity, deck: DraftDeckState) {
  if (rarity === "rare") {
    return deck.rareSlots.length < MARKET_SLOT_CAPS.rare;
  }
  if (rarity === "uncommon") {
    return deck.uncommonSlots.length < MARKET_SLOT_CAPS.uncommon || deck.rareSlots.length < MARKET_SLOT_CAPS.rare;
  }
  return (
    deck.commonSlots.length < MARKET_SLOT_CAPS.common ||
    deck.uncommonSlots.length < MARKET_SLOT_CAPS.uncommon ||
    deck.rareSlots.length < MARKET_SLOT_CAPS.rare
  );
}

function assignCard(deck: DraftDeckState, card: CardDefinition, visibility: "public" | "hidden") {
  const slotName = nextSlotName(card, deck);
  if (!slotName) {
    throw new Error(`No legal slot for ${card.id}`);
  }

  deck[slotName].push(card);
  const slotIndex = deck[slotName].length - 1;
  if (visibility === "public") {
    deck.publicCards.push(card);
  } else {
    deck.hiddenCards.push(card);
  }

  const slotGroup: DraftSlotGroup =
    slotName === "commonSlots" ? "common" : slotName === "uncommonSlots" ? "uncommon" : "rare";
  return { slotGroup, slotIndex };
}

function hiddenCandidatesForRarity(pool: AvailablePool, rarity: CardRarity) {
  return [...pool.counts.entries()]
    .filter(([cardId, count]) => count > 0 && pool.cardsById.get(cardId)?.rarity === rarity)
    .map(([cardId]) => pool.cardsById.get(cardId)!)
    .sort((left, right) => left.name.localeCompare(right.name, "ja"));
}

function refillVisibleRow(
  session: DraftSession,
  pool: AvailablePool,
  rarity: CardRarity,
  insertIndex: number | null,
  rng: ReturnType<typeof createSeededRandom>,
) {
  if (session.marketRows[rarity].visibleCards.length >= MARKET_VISIBLE_COUNT) {
    session.marketRows[rarity].topDeckAvailable = hiddenCandidatesForRarity(pool, rarity).length > 0;
    return;
  }
  const candidates = hiddenCandidatesForRarity(pool, rarity);
  if (candidates.length === 0) {
    session.marketRows[rarity].topDeckAvailable = false;
    return;
  }
  const [replacement] = drawCardsByRarity(pool, rarity, 1, rng);
  if (insertIndex === null || insertIndex < 0 || insertIndex > session.marketRows[rarity].visibleCards.length) {
    session.marketRows[rarity].visibleCards.push(replacement);
  } else {
    session.marketRows[rarity].visibleCards.splice(insertIndex, 0, replacement);
  }
  session.marketRows[rarity].topDeckAvailable = hiddenCandidatesForRarity(pool, rarity).length > 0;
}

function syncSession(session: DraftSession, pool: AvailablePool, rng: ReturnType<typeof createSeededRandom>) {
  (["common", "uncommon", "rare"] as CardRarity[]).forEach((rarity) => {
    if (session.marketRows[rarity].visibleCards.length > MARKET_VISIBLE_COUNT) {
      session.marketRows[rarity].visibleCards = session.marketRows[rarity].visibleCards.slice(0, MARKET_VISIBLE_COUNT);
    }
    session.marketRows[rarity].topDeckAvailable = hiddenCandidatesForRarity(pool, rarity).length > 0;
  });
  session.poolCounts = serializePool(pool);
  session.poolSnapshot = buildPoolSnapshot(pool);
  session.rngState = rng.getState();
}

function maybeCompleteDraft(session: DraftSession) {
  if (countDeck(session.decks.p1) >= 12 && countDeck(session.decks.p2) >= 12) {
    session.currentStep.phase = "complete";
    pushLog(session, "system", "ドラフトが完了しました。次はバトル画面へ進みます。");
    return true;
  }
  return false;
}

function applyPick(
  session: DraftSession,
  mode: "visible" | "topdeck",
  value: string,
  actingPlayer: PlayerId,
  pool: AvailablePool,
  rng: ReturnType<typeof createSeededRandom>,
) {
  const deck = session.decks[actingPlayer];

  if (mode === "visible") {
    const [rarityPart, indexPart] = value.split(":");
    const rarity = rarityPart as CardRarity;
    const index = Number(indexPart);
    if (!["rare", "uncommon", "common"].includes(rarity) || !Number.isInteger(index)) {
      throw new Error(`Unknown visible market card: ${value}`);
    }
    const pickedCard = session.marketRows[rarity].visibleCards[index];
    if (!pickedCard) {
      throw new Error(`Unknown visible market card: ${value}`);
    }
    session.marketRows[rarity].visibleCards.splice(index, 1);
    const slotPlacement = assignCard(deck, pickedCard, "public");
    pushLog(
      session,
      "draft",
      `${playerLabel(actingPlayer)} が ${rarityLabel(rarity)} から「${pickedCard.name || pickedCard.id}」を取得しました。`,
      {
        playerId: actingPlayer,
        cardId: pickedCard.id,
        cardName: pickedCard.name || pickedCard.id,
        rarity,
        mode: "visible",
        visibility: "public",
        slotGroup: slotPlacement.slotGroup,
        slotIndex: slotPlacement.slotIndex,
        sourceKey: `market-card-${rarity}-${index}`,
        targetKey: `slot-${actingPlayer}-${slotPlacement.slotGroup}-${slotPlacement.slotIndex}`,
      },
    );
    session.pendingRefillRarity = rarity;
    session.pendingVisibleGapIndex = index;
    return;
  }

  const rarity = value as CardRarity;
  const hiddenOffer = hiddenCandidatesForRarity(pool, rarity);
  if (hiddenOffer.length === 0) {
    throw new Error(`No hidden candidates for ${rarity}`);
  }

  const [pickedCard] = drawCardsByRarity(pool, rarity, 1, rng);
  const slotPlacement = assignCard(deck, pickedCard, "hidden");
  pushLog(
    session,
    "draft",
    `${playerLabel(actingPlayer)} が ${rarityLabel(rarity)} 山札のトップを取得しました。`,
    {
      playerId: actingPlayer,
      cardId: pickedCard.id,
      cardName: pickedCard.name || pickedCard.id,
      rarity,
      mode: "topdeck",
      visibility: "hidden",
      slotGroup: slotPlacement.slotGroup,
      slotIndex: slotPlacement.slotIndex,
      sourceKey: `topdeck-${rarity}`,
      targetKey: `slot-${actingPlayer}-${slotPlacement.slotGroup}-${slotPlacement.slotIndex}`,
    },
  );
}

function advanceCpu(session: DraftSession, pool: AvailablePool, rng: ReturnType<typeof createSeededRandom>) {
  const choice = chooseStandardMarketPick(
    session.marketRows,
    session.decks.p2,
    [...session.decks.p1.starter, ...session.decks.p1.publicCards],
    {
      common: hiddenCandidatesForRarity(pool, "common"),
      uncommon: hiddenCandidatesForRarity(pool, "uncommon"),
      rare: hiddenCandidatesForRarity(pool, "rare"),
    },
  );
  applyPick(session, choice.mode, choice.value, "p2", pool, rng);
}

export function summarizeDraftDeck(deck: DraftDeckState) {
  const allCards = flattenDeck(deck);
  return {
    total: allCards.length,
    publicCount: deck.starter.length + deck.publicCards.length,
    hiddenCount: deck.hiddenCards.length,
    rarityCounts: summarizeDeckRarity(deck),
  };
}

export function createInitialDraftSession(seed = 71): DraftSession {
  const rng = createSeededRandom(seed);
  const pool = buildAvailablePool();
  const starters = starterCards();
  const firstPlayer: PlayerId = rng.next() < 0.5 ? "p1" : "p2";

  const session: DraftSession = {
    seed,
    rngState: rng.getState(),
    currentStep: {
      phase: "market",
      actingPlayer: firstPlayer,
      pickNumber: 1,
    },
    firstPlayer,
    decks: {
      p1: cloneDeckState(starters),
      p2: cloneDeckState(starters),
    },
    poolCounts: {},
    marketRows: {
      rare: { rarity: "rare", visibleCards: drawCardsByRarity(pool, "rare", MARKET_VISIBLE_COUNT, rng), topDeckAvailable: false },
      uncommon: { rarity: "uncommon", visibleCards: drawCardsByRarity(pool, "uncommon", MARKET_VISIBLE_COUNT, rng), topDeckAvailable: false },
      common: { rarity: "common", visibleCards: drawCardsByRarity(pool, "common", MARKET_VISIBLE_COUNT, rng), topDeckAvailable: false },
    },
    logs: [
      { id: "log-1", kind: "system", text: `ドラフトを開始しました。先手は ${playerLabel(firstPlayer)} です。` },
      { id: "log-2", kind: "draft", text: "両プレイヤーは初期デッキとして「攻撃 / 防御 / ステップ」を持っています。" },
    ],
    poolSnapshot: { remainingTotal: 0, remainingByRarity: { common: 0, uncommon: 0, rare: 0 } },
    pendingRefillRarity: null,
    pendingVisibleGapIndex: null,
    pendingCpuTurn: false,
  };

  syncSession(session, pool, rng);
  if (firstPlayer === "p2") {
    advanceCpu(session, pool, rng);
    if (session.pendingRefillRarity) {
      refillVisibleRow(session, pool, session.pendingRefillRarity, session.pendingVisibleGapIndex, rng);
      session.pendingRefillRarity = null;
      session.pendingVisibleGapIndex = null;
    }
    if (!maybeCompleteDraft(session)) {
      session.currentStep.actingPlayer = "p1";
      session.currentStep.pickNumber += 1;
    }
    syncSession(session, pool, rng);
  }
  return session;
}

export function applyPlayerDraftPick(session: DraftSession, pick: { mode: "visible" | "topdeck"; value: string }) {
  const nextSession = cloneSession(session);
  const pool = hydratePool(nextSession);
  const rng = createSeededRandom(nextSession.rngState);

  if (nextSession.currentStep.phase !== "market" || nextSession.currentStep.actingPlayer !== "p1") {
    return nextSession;
  }

  if (pick.mode === "visible") {
    const [rarityPart, indexPart] = pick.value.split(":");
    const rarity = rarityPart as CardRarity;
    const index = Number(indexPart);
    const card = ["rare", "uncommon", "common"].includes(rarity) && Number.isInteger(index) ? nextSession.marketRows[rarity].visibleCards[index] : null;
    if (!card || !canTakeCard(card, nextSession.decks.p1)) {
      return nextSession;
    }
  } else if (!canTakeRarity(pick.value as CardRarity, nextSession.decks.p1)) {
    return nextSession;
  }

  applyPick(nextSession, pick.mode, pick.value, "p1", pool, rng);
  if (!maybeCompleteDraft(nextSession)) {
    nextSession.currentStep.actingPlayer = "p2";
    nextSession.currentStep.pickNumber += 1;
    nextSession.pendingCpuTurn = true;
  }
  syncSession(nextSession, pool, rng);
  return nextSession;
}

export function advanceDraftAfterAnimation(session: DraftSession) {
  const nextSession = cloneSession(session);
  const pool = hydratePool(nextSession);
  const rng = createSeededRandom(nextSession.rngState);

  if (nextSession.pendingRefillRarity) {
    refillVisibleRow(nextSession, pool, nextSession.pendingRefillRarity, nextSession.pendingVisibleGapIndex, rng);
    nextSession.pendingRefillRarity = null;
    nextSession.pendingVisibleGapIndex = null;
    syncSession(nextSession, pool, rng);
    return nextSession;
  }

  if (nextSession.currentStep.phase !== "market") {
    syncSession(nextSession, pool, rng);
    return nextSession;
  }

  if (nextSession.pendingCpuTurn) {
    nextSession.pendingCpuTurn = false;
    advanceCpu(nextSession, pool, rng);
    if (!maybeCompleteDraft(nextSession)) {
      nextSession.currentStep.actingPlayer = "p1";
      nextSession.currentStep.pickNumber += 1;
    }
  }

  syncSession(nextSession, pool, rng);
  return nextSession;
}
