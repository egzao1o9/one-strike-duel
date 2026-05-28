import { advanceDraftAfterAnimation, applyPlayerDraftPick, createInitialDraftSession } from "../lib/draftSession";
import { applyPlayerBattleAction, applyPlayerControlChoice, createBattleSessionFromDraft } from "../lib/battleSession";
import type { CardRarity } from "../types/cards";
import type { BattleActionType } from "../types/prototype";
import type { PrototypeState } from "../types/prototype";

export type PrototypeAction =
  | { type: "start_prototype"; seed?: number }
  | { type: "return_to_title" }
  | { type: "choose_visible_card"; pickKey: string }
  | { type: "take_topdeck"; rarity: CardRarity }
  | { type: "resolve_draft_animation" }
  | { type: "enter_battle" }
  | { type: "choose_control"; cardId: string | null }
  | { type: "choose_battle_action"; actionType: BattleActionType; cardIds: string[] };

export const initialPrototypeState: PrototypeState = {
  screen: "title",
  activeSession: null,
  activeBattle: null,
};

export function prototypeReducer(state: PrototypeState, action: PrototypeAction): PrototypeState {
  switch (action.type) {
    case "start_prototype":
      return {
        screen: "draft",
        activeSession: createInitialDraftSession(action.seed ?? Date.now()),
        activeBattle: null,
      };
    case "return_to_title":
      return initialPrototypeState;
    case "choose_visible_card":
      if (!state.activeSession) {
        return state;
      }
      {
        const activeSession = applyPlayerDraftPick(state.activeSession, { mode: "visible", value: action.pickKey });
        return {
          ...state,
          screen: activeSession.currentStep.phase === "complete" ? "deck_review" : state.screen,
          activeSession,
          activeBattle: state.activeBattle,
        };
      }
    case "take_topdeck":
      if (!state.activeSession) {
        return state;
      }
      {
        const activeSession = applyPlayerDraftPick(state.activeSession, { mode: "topdeck", value: action.rarity });
        return {
          ...state,
          screen: activeSession.currentStep.phase === "complete" ? "deck_review" : state.screen,
          activeSession,
          activeBattle: state.activeBattle,
        };
      }
    case "resolve_draft_animation":
      if (!state.activeSession) {
        return state;
      }
      {
        const activeSession = advanceDraftAfterAnimation(state.activeSession);
        return {
          ...state,
          screen: activeSession.currentStep.phase === "complete" ? "deck_review" : state.screen,
          activeSession,
          activeBattle: state.activeBattle,
        };
      }
    case "enter_battle":
      if (!state.activeSession) {
        return state;
      }
      return {
        ...state,
        screen: "battle",
        activeBattle: createBattleSessionFromDraft(state.activeSession),
      };
    case "choose_control":
      if (!state.activeBattle) {
        return state;
      }
      return {
        ...state,
        activeBattle: applyPlayerControlChoice(state.activeBattle, action.cardId),
      };
    case "choose_battle_action":
      if (!state.activeBattle) {
        return state;
      }
      return {
        ...state,
        activeBattle: applyPlayerBattleAction(state.activeBattle, action.actionType, action.cardIds),
      };
    default:
      return state;
  }
}
