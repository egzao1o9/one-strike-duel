import type { CardDefinition, CardRarity } from "../types/cards";
import type { DraftDeckState, MarketRowState } from "../types/prototype";

const TARGET_TYPE_COUNTS = {
  battle: 7,
  control: 4,
  blessing: 1,
} as const;

const TARGET_ROLE_COUNTS = {
  red: 4,
  blue: 2,
  green: 3,
  white: 3,
} as const;

const RARITY_SCORES: Record<CardRarity, number> = {
  common: 0,
  uncommon: 1.3,
  rare: 2.5,
};

const MARKET_SLOT_CAPS = {
  common: 2,
  uncommon: 5,
  rare: 2,
} as const;

const BLESSING_HATE_CONTROL_IDS = new Set([
  "control_blessing_flip",
  "control_blessing_break",
  "control_blessing_lock",
  "control_defile",
]);

interface DeckSummary {
  total: number;
  battleCount: number;
  controlCount: number;
  blessingCount: number;
  rarityCounts: Record<CardRarity, number>;
  roleCounts: Record<keyof typeof TARGET_ROLE_COUNTS, number>;
}

export interface MarketPickChoice {
  mode: "visible" | "topdeck";
  value: string;
}

function flattenDeck(deck: DraftDeckState) {
  return [...deck.starter, ...deck.publicCards, ...deck.hiddenCards];
}

function inferRoleColor(card: CardDefinition): keyof typeof TARGET_ROLE_COUNTS {
  if (card.card_type === "control") {
    return "white";
  }
  if (card.card_type === "blessing") {
    if (card.tags.includes("speed") || card.tags.includes("trick") || card.speed >= 4) {
      return "blue";
    }
    if (card.tags.includes("defense") || card.block >= 3) {
      return "green";
    }
    if (card.tags.includes("draw") || card.tags.includes("support")) {
      return "white";
    }
    return "red";
  }
  if (card.tags.includes("speed") || card.tags.includes("trick") || card.speed >= 4) {
    return "blue";
  }
  if (card.tags.includes("defense") || card.block >= 3) {
    return "green";
  }
  return "red";
}

function summarizeDeck(cards: CardDefinition[]): DeckSummary {
  const summary: DeckSummary = {
    total: cards.length,
    battleCount: 0,
    controlCount: 0,
    blessingCount: 0,
    rarityCounts: { common: 0, uncommon: 0, rare: 0 },
    roleCounts: { red: 0, blue: 0, green: 0, white: 0 },
  };
  cards.forEach((card) => {
    summary.rarityCounts[card.rarity] += 1;
    summary.roleCounts[inferRoleColor(card)] += 1;
    if (card.card_type === "battle") {
      summary.battleCount += 1;
    } else if (card.card_type === "blessing") {
      summary.blessingCount += 1;
    } else {
      summary.controlCount += 1;
    }
  });
  return summary;
}

function needBonus(current: number, target: number, remainingPicks: number, weight: number) {
  const deficit = target - current;
  if (deficit <= 0) {
    return -0.2 * Math.max(current - target, 0);
  }
  let urgency = 1;
  if (remainingPicks <= deficit) {
    urgency = 1.7;
  } else if (remainingPicks <= deficit + 1) {
    urgency = 1.35;
  }
  return (deficit * weight * urgency) / Math.max(remainingPicks, 1);
}

function blessingPickAdjustment(card: CardDefinition, ownCards: CardDefinition[]) {
  if (card.card_type !== "blessing") {
    return 0;
  }
  const blessingCount = ownCards.filter((candidate) => candidate.card_type === "blessing").length;
  const recycleCount = ownCards.filter((candidate) => candidate.id === "control_discard_facedown_blessing").length;
  if (blessingCount === 0) {
    return 0.5;
  }
  if (blessingCount === 1) {
    return 0.1;
  }
  return -Math.max(0.9 - recycleCount * 0.35, 0.15);
}

function baseCardScore(card: CardDefinition) {
  return (
    RARITY_SCORES[card.rarity] +
    Math.max(card.attack, 0) * 1 +
    Math.max(card.block, 0) * 0.85 +
    Math.max(card.speed, 0) * 0.72 -
    Math.max(-card.attack, 0) * 0.5 -
    Math.max(-card.block, 0) * 0.35 -
    Math.max(-card.speed, 0) * 0.25 +
    (card.effects?.length ?? 0) * 0.45
  );
}

function canPlaceRarity(rarity: CardRarity, deck: DraftDeckState) {
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

function counterValue(card: CardDefinition, opponentPublicCards: CardDefinition[]) {
  const battles = opponentPublicCards.filter((candidate) => candidate.card_type === "battle");
  if (battles.length === 0) {
    return 0;
  }
  const averageAttack = battles.reduce((sum, candidate) => sum + candidate.attack, 0) / battles.length;
  const averageBlock = battles.reduce((sum, candidate) => sum + candidate.block, 0) / battles.length;
  const averageSpeed = battles.reduce((sum, candidate) => sum + candidate.speed, 0) / battles.length;
  let score = 0;
  if (card.block >= averageAttack) {
    score += 0.42;
  }
  if (card.speed >= averageSpeed) {
    score += 0.32;
  }
  if (card.attack > averageBlock) {
    score += 0.38;
  }
  for (const effect of card.effects ?? []) {
    if (effect.kind === "modify_opponent_block") {
      score += 0.4;
    } else if (effect.kind === "modify_opponent_speed") {
      score += 0.28;
    } else if (effect.kind === "modify_self_block") {
      score += 0.2;
    }
  }
  return score;
}

function publicValue(card: CardDefinition) {
  let score = 0;
  if (card.card_type !== "battle") {
    score += 0.32;
  }
  if (card.attack >= 4 && card.block <= 0) {
    score -= 0.24;
  }
  return score;
}

function hiddenValue(card: CardDefinition) {
  let score = 0;
  if (card.attack >= 4 || card.speed >= 3) {
    score += 0.72;
  }
  if ((card.effects ?? []).some((effect) => effect.kind === "modify_opponent_block")) {
    score += 0.28;
  }
  return score;
}

function scoreCard(card: CardDefinition, ownDeck: DraftDeckState, opponentPublicCards: CardDefinition[], visibility: "public" | "hidden") {
  const ownCards = flattenDeck(ownDeck);
  const ownSummary = summarizeDeck(ownCards);
  const remainingPicks = 12 - ownCards.length;
  const role = inferRoleColor(card);

  let score = baseCardScore(card);
  score += needBonus(
    card.card_type === "battle" ? ownSummary.battleCount : card.card_type === "blessing" ? ownSummary.blessingCount : ownSummary.controlCount,
    TARGET_TYPE_COUNTS[card.card_type],
    remainingPicks,
    1.2,
  );
  score += needBonus(ownSummary.roleCounts[role], TARGET_ROLE_COUNTS[role], remainingPicks, 0.9);
  score -= ownCards.filter((candidate) => candidate.id === card.id).length * 0.8;
  score += blessingPickAdjustment(card, ownCards);
  score += counterValue(card, opponentPublicCards);
  if (visibility === "hidden") {
    score += hiddenValue(card);
  } else {
    score += publicValue(card);
  }
  if (BLESSING_HATE_CONTROL_IDS.has(card.id) && opponentPublicCards.some((candidate) => candidate.card_type === "blessing")) {
    score += 0.9;
  }
  if (!canPlaceRarity(card.rarity, ownDeck)) {
    score -= 999;
  }
  return score;
}

export function chooseStandardMarketPick(
  rows: Record<CardRarity, MarketRowState>,
  ownDeck: DraftDeckState,
  opponentPublicCards: CardDefinition[],
  hiddenCandidates: Record<CardRarity, CardDefinition[]>,
): MarketPickChoice {
  const scored: Array<{ score: number; choice: MarketPickChoice }> = [];

  (["rare", "uncommon", "common"] as CardRarity[]).forEach((rarity) => {
    rows[rarity].visibleCards.forEach((card, index) => {
      scored.push({
        score: scoreCard(card, ownDeck, opponentPublicCards, "public"),
        choice: { mode: "visible", value: `${rarity}:${index}` },
      });
    });

    if (rows[rarity].topDeckAvailable && canPlaceRarity(rarity, ownDeck) && hiddenCandidates[rarity].length > 0) {
      const averageScore =
        hiddenCandidates[rarity].reduce((sum, card) => sum + scoreCard(card, ownDeck, opponentPublicCards, "hidden"), 0) /
        hiddenCandidates[rarity].length;
      scored.push({
        score: averageScore + 0.08,
        choice: { mode: "topdeck", value: rarity },
      });
    }
  });

  scored.sort((left, right) => {
    if (right.score !== left.score) {
      return right.score - left.score;
    }
    return left.choice.value.localeCompare(right.choice.value, "ja");
  });

  return scored[0]?.choice ?? { mode: "visible", value: "common:0" };
}
