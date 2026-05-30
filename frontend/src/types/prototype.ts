import type { CardDefinition, CardRarity } from "./cards";

export type PlayerId = "p1" | "p2";
export type ViewScreen = "title" | "draft" | "deck_review" | "constructed_select" | "battle" | "result" | "log";
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

export type BattlePhase = "mulligan" | "control" | "battle_select" | "trigger_prompt" | "reveal" | "blessing_prompt" | "turn_transition" | "result";
export type BattleActionType = "set" | "set_pass" | "pass" | "retreat";
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
  pendingParryLimit: boolean;
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

export interface BattleParryEvent {
  turn: number;
  attacker: PlayerId;
  defender: PlayerId;
  attackerAttack: number;
  defenderBlock: number;
  margin: number;
  blockDebuffApplied: number;
  nextBattleLimitApplied: boolean;
}

export interface BattleRetreatEvent {
  turn: number;
  player: PlayerId;
  retreatPlayerDiscardedIds: string[];
  opponentReturnedId: string | null;
  opponentDiscardedIds: string[];
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
  mode: "confirm_use" | "choose_option" | "acknowledge" | "reorder_draw_pile";
  choices?: Array<{
    id: string;
    label: string;
    disabled?: boolean;
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
  transitionMessage: string | null;
  pendingBlessingChoice: PendingBlessingChoice | null;
  pendingTriggerChoice: PendingTriggerChoice | null;
  pendingTriggerContinuation: {
    nextActor: PlayerId | null;
    resume?: "battle" | "control_after_player" | "reveal";
    effectAction?:
      | {
          kind: "return_discard_to_hand";
          targetPlayerId: PlayerId;
        }
      | {
          kind: "boost_selected_hand_card";
          targetPlayerId: PlayerId;
          attackDelta: number;
          nextTurnDrawDelta: number;
        }
      | {
          kind: "boost_selected_set_card";
          targetPlayerId: PlayerId;
          attackDelta?: number;
          blockDelta?: number;
          speedDelta?: number;
        }
      | {
          kind: "search_draw_pile_to_hand";
          targetPlayerId: PlayerId;
        }
      | {
          kind: "recover_discard_to_hand";
          targetPlayerId: PlayerId;
        }
        | {
          kind: "reorder_draw_pile";
          targetPlayerId: PlayerId;
          count: number;
        }
      | {
          kind: "retreat_return_set_to_hand";
          targetPlayerId: PlayerId;
          retreatingPlayerId: PlayerId;
          setIndex?: number;
        };
  } | null;
  pendingReveal: PendingRevealState | null;
  battleParryLimitActive: Record<PlayerId, boolean>;
  battleParryLimitCancelledForBoth: boolean;
  parryEvents: BattleParryEvent[];
  retreatEvent: BattleRetreatEvent | null;
}

export interface PrototypeState {
  screen: ViewScreen;
  activeSession: DraftSession | null;
  activeBattle: BattleSession | null;
  constructedSetup: {
    playerDeckId: string | null;
    cpuDeckId: string | null;
  } | null;
}
