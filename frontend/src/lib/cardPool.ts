import rawPool from "../../../data/card_pool.json";
import { getAllCards } from "./cards";
import type { CardDefinition, CardRarity } from "../types/cards";

interface CardPoolEntry {
  card_id: string;
  count: number;
}

interface CardPoolDefinition {
  id: string;
  name: string;
  entries: CardPoolEntry[];
}

const cardsById = new Map<string, CardDefinition>(getAllCards().map((card) => [card.id, card]));
const basePool = rawPool as CardPoolDefinition;

export interface PoolCardEntry {
  card: CardDefinition;
  count: number;
}

export function getBasePoolEntries(): PoolCardEntry[] {
  return basePool.entries.flatMap((entry) => {
    const card = cardsById.get(entry.card_id);
    if (!card || !card.enabled) {
      return [];
    }
    return [{ card, count: entry.count }];
  });
}

export function summarizePoolByRarity(entries: PoolCardEntry[]): Record<CardRarity, number> {
  return entries.reduce<Record<CardRarity, number>>(
    (acc, entry) => {
      acc[entry.card.rarity] += entry.count;
      return acc;
    },
    { common: 0, uncommon: 0, rare: 0 },
  );
}
