import rawCards from "../../../data/cards.json";
import type { CardDefinition, CardRarity, CardType } from "../types/cards";
import { debugOnlyCards } from "./debugCards";

const cards = (rawCards as CardDefinition[]).filter((card) => card.enabled);
const debugCards = debugOnlyCards;

export function getAllCards(includeDebug = false): CardDefinition[] {
  return includeDebug ? [...cards, ...debugCards] : cards;
}

export function getDebugOnlyCards(): CardDefinition[] {
  return debugCards;
}

export function summarizeByType(input: CardDefinition[]): Record<CardType, number> {
  return input.reduce<Record<CardType, number>>(
    (acc, card) => {
      acc[card.card_type] += 1;
      return acc;
    },
    { battle: 0, control: 0, blessing: 0 },
  );
}

export function summarizeByRarity(input: CardDefinition[]): Record<CardRarity, number> {
  return input.reduce<Record<CardRarity, number>>(
    (acc, card) => {
      acc[card.rarity] += 1;
      return acc;
    },
    { common: 0, uncommon: 0, rare: 0 },
  );
}

export function groupCards(input: CardDefinition[]): Record<CardType, CardDefinition[]> {
  return {
    battle: input.filter((card) => card.card_type === "battle"),
    control: input.filter((card) => card.card_type === "control"),
    blessing: input.filter((card) => card.card_type === "blessing"),
  };
}
