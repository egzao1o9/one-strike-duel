import { getAllCards, summarizeByRarity, summarizeByType } from "./cards";
import type { CardDefinition } from "../types/cards";
import type { DraftDeckState } from "../types/prototype";

export interface PresetDeckDefinition {
  id: string;
  name: string;
  description: string;
  starterIds: string[];
  extraCardIds: string[];
}

const cardsById = new Map(getAllCards().map((card) => [card.id, card]));

const STARTER_IDS = ["battle_attack", "battle_defend", "battle_step"];

export const presetDecks: PresetDeckDefinition[] = [
  {
    id: "standard_flow",
    name: "Standard Flow",
    description: "攻守の偏りを抑えた基準デッキ。battle中心で、軽いcontrolと加護を少しだけ混ぜている。",
    starterIds: STARTER_IDS,
    extraCardIds: [
      "battle_probe_guard",
      "battle_check_cut",
      "battle_guard",
      "battle_brace",
      "battle_step_in",
      "battle_still_water",
      "control_focus",
      "control_guard",
      "blessing_guard",
    ],
  },
  {
    id: "quick_press",
    name: "Quick Press",
    description: "速さと押し込みを少し重く見た構築済み。極端な尖りは避けつつ、早期決着を狙いやすい。",
    starterIds: STARTER_IDS,
    extraCardIds: [
      "battle_dash",
      "battle_press",
      "battle_step_in",
      "battle_afterimage",
      "battle_break",
      "battle_probe_guard",
      "control_pressure",
      "control_haste",
      "blessing_speed",
    ],
  },
  {
    id: "guard_stance",
    name: "Guard Stance",
    description: "受けを厚めにした基準デッキ。防御寄りだが、最低限の打点とcontrolで返す形を作りやすい。",
    starterIds: STARTER_IDS,
    extraCardIds: [
      "battle_body_guard",
      "battle_low_guard",
      "battle_guard_step",
      "battle_intercept",
      "battle_still_water",
      "battle_probe_guard",
      "control_brace",
      "control_parry_window",
      "blessing_buckler",
    ],
  },
];

function requireCard(cardId: string): CardDefinition {
  const card = cardsById.get(cardId);
  if (!card) {
    throw new Error(`Unknown preset card: ${cardId}`);
  }
  return card;
}

export function getPresetDeckById(deckId: string) {
  return presetDecks.find((deck) => deck.id === deckId) ?? null;
}

export function buildPresetDeckState(deckId: string): DraftDeckState {
  const deck = getPresetDeckById(deckId);
  if (!deck) {
    throw new Error(`Unknown preset deck: ${deckId}`);
  }
  return {
    starter: deck.starterIds.map(requireCard),
    publicCards: [],
    hiddenCards: deck.extraCardIds.map(requireCard),
    commonSlots: [],
    uncommonSlots: [],
    rareSlots: [],
  };
}

export function listPresetDeckCards(deck: PresetDeckDefinition) {
  return [...deck.starterIds, ...deck.extraCardIds].map(requireCard);
}

export function summarizePresetDeck(deck: PresetDeckDefinition) {
  const cards = listPresetDeckCards(deck);
  return {
    total: cards.length,
    typeCounts: summarizeByType(cards),
    rarityCounts: summarizeByRarity(cards),
  };
}
