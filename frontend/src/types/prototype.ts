import type { CardDefinition, CardRarity } from "./cards";

export type PlayerId = "p1" | "p2";
export type ViewScreen = "title" | "draft" | "deck_review" | "battle" | "result" | "log";
export type DraftPhase = "market" | "complete";
export type DraftPickMode = "visible" | "topdeck";
export type DraftSlotGroup = "common" | "uncommon" | "rare";

export interface DraftDeckState {
  starter: CardDefinition[];
  publicCards: CardDefinition[];
  hiddenCards: CardDefinition[];
  commonSlots: CardDefinition[];
  uncommonSlots: CardDefinition[];
  rareSlots: CardDefinition[];
}

export interface PrototypeLogEntry {
  id: string;
  kind: "system" | "draft";
  text: string;
  draftEvent?: {
    playerId: PlayerId;
    cardId: string;
    cardName: string;
    rarity: CardRarity;
    mode: DraftPickMode;
    visibility: "public" | "hidden";
    slotGroup: DraftSlotGroup;
    slotIndex: number;
    sourceKey: string;
    targetKey: string;
  };
}

export interface DraftStepState {
  phase: DraftPhase;
  actingPlayer: PlayerId;
  pickNumber: number;
}

export interface DraftPoolSnapshot {
  remainingTotal: number;
  remainingByRarity: Record<CardRarity, number>;
}

export interface MarketRowState {
  rarity: CardRarity;
  visibleCards: CardDefinition[];
  topDeckAvailable: boolean;
}

export interface DraftSession {
  seed: number;
  rngState: number;
  currentStep: DraftStepState;
  firstPlayer: PlayerId;
  decks: Record<PlayerId, DraftDeckState>;
  poolCounts: Record<string, number>;
  marketRows: Record<CardRarity, MarketRowState>;
  logs: PrototypeLogEntry[];
  poolSnapshot: DraftPoolSnapshot;
  pendingRefillRarity: CardRarity | null;
  pendingVisibleGapIndex: number | null;
  pendingCpuTurn: boolean;
}

export type BattlePhase = "mulligan" | "control" | "battle_select" | "trigger_prompt" | "reveal" | "blessing_prompt" | "result";
export type BattleActionType = "set" | "set_pass" | "pass";
export type DebugBattlePreset = "draw" | "no_damage" | "p1_win" | "p2_win";
export type DebugBattleZone = "set" | "control" | "blessing" | "hand" | "draw_pile" | "discard";

export interface BattleSetCard {
  card: CardDefinition;
  revealed: boolean;
}

export interface ActiveTurnModifier {
  sourceId: string;
  attack: number;
  block: number;
  speed: number;
  opponentAttack: number;
  opponentBlock: number;
  opponentSpeed: number;
  lockBlessing?: boolean;
  nextTurnDrawDelta?: number;
}

export interface BattlePlayerState {
  drawPile: CardDefinition[];
  hand: CardDefinition[];
  topdeckAsHandCardId: string | null;
  discardPile: CardDefinition[];
  usedCards: CardDefinition[];
  currentControlCard: CardDefinition | null;
  blessingZone: CardDefinition | null;
  blessingFaceUp: boolean;
  blessingLockedThisTurn: boolean;
  queuedNextTurnDrawDelta: number;
  queuedNextTurnStatDelta: {
    attack: number;
    block: number;
    speed: number;
  };
  activeTurnModifiers: ActiveTurnModifier[];
  setCards: BattleSetCard[];
  battlePassed: boolean;
  revealFirstSetThisTurn: boolean;
}

export interface BattleLogEntry {
  id: string;
  text: string;
}

export interface BattleEffectLogEntry {
  id: string;
  playerId: PlayerId;
  sourceCardId: string;
  sourceCardName: string;
  text: string;
}

export interface BattleRevealStep {
  playerId: PlayerId;
  cardId: string;
  cardName: string;
  cardType: string;
  index: number;
}

export interface BattleFinalLine {
  attack: number;
  block: number;
  speed: number;
}

export interface PendingBlessingChoice {
  playerId: PlayerId;
  blessingCardId: string;
  blessingName: string;
  promptText: string;
  previewLines: Record<PlayerId, BattleFinalLine>;
}

export interface PendingTriggerChoice {
  playerId: PlayerId;
  blessingCardId: string;
  blessingName: string;
  promptText: string;
  mode: "confirm_use" | "choose_option" | "acknowledge";
  choices?: Array<{
    id: string;
    label: string;
    card?: CardDefinition;
    payload?: {
      kind: "set_card" | "discard_card" | "hand_card" | "draw_pile_card" | "used_card";
      playerId: PlayerId;
      setIndex?: number;
      discardIndex?: number;
      handIndex?: number;
      drawPileIndex?: number;
      usedIndex?: number;
      cardId?: string;
    };
  }>;
}

export interface PendingRevealState {
  steps: BattleRevealStep[];
  nextIndex: number;
}

export interface BattleSession {
  debugMode: boolean;
  seed: number;
  turn: number;
  phase: BattlePhase;
  firstPlayer: PlayerId;
  battleStartingPlayer: PlayerId;
  actingPlayer: PlayerId;
  players: Record<PlayerId, BattlePlayerState>;
  finalLines: Record<PlayerId, BattleFinalLine> | null;
  revealSteps: BattleRevealStep[];
  winner: PlayerId | null;
  endReason: string | null;
  logs: BattleLogEntry[];
  effectLogs: BattleEffectLogEntry[];
  pendingBlessingChoice: PendingBlessingChoice | null;
  pendingTriggerChoice: PendingTriggerChoice | null;
  pendingTriggerContinuation: {
    nextActor: PlayerId | null;
    resume?: "battle" | "control_after_player";
  } | null;
  pendingReveal: PendingRevealState | null;
}

export interface PrototypeState {
  screen: ViewScreen;
  activeSession: DraftSession | null;
  activeBattle: BattleSession | null;
}
