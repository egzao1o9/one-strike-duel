import { advanceDraftAfterAnimation, applyPlayerDraftPick, createInitialDraftSession } from "../lib/draftSession";
import { advanceBattleReveal, advanceTurnTransition, applyDebugAddCardToHand, applyDebugBattlePreset, applyDebugClearZone, applyDebugPlaceCard, applyDebugPromptOwnSetChoice, applyDebugPromptReorderTopCards, applyDebugPromptRevealedOpponentChoice, applyDebugSetPhase, applyDebugStartReveal, applyPlayerBattleAction, applyPlayerBlessingChoice, applyPlayerControlChoice, applyPlayerDrawPileReorder, applyPlayerMulligan, applyPlayerTriggerChoice, createBattleSessionFromDecks, createBattleSessionFromDraft, createDebugBattleSession } from "../lib/battleSession";
import { buildPresetDeckState } from "../lib/presetDecks";
import type { CardRarity } from "../types/cards";
import type { BattleActionType, BattlePhase } from "../types/prototype";
import type { DebugBattlePreset, DebugBattleZone, PrototypeState, PlayerId } from "../types/prototype";

export type PrototypeAction =
  | { type: "start_prototype"; seed?: number }
  | { type: "start_constructed_select" }
  | { type: "select_constructed_player_deck"; deckId: string }
  | { type: "select_constructed_cpu_deck"; deckId: string }
  | { type: "start_constructed_battle"; seed?: number }
  | { type: "start_debug_battle"; seed?: number }
  | { type: "return_to_title" }
  | { type: "choose_visible_card"; pickKey: string }
  | { type: "take_topdeck"; rarity: CardRarity }
  | { type: "resolve_draft_animation" }
  | { type: "enter_battle" }
  | { type: "choose_mulligan"; handIndexes: number[] }
  | { type: "choose_control"; handIndex: number | null }
  | { type: "choose_battle_action"; actionType: BattleActionType; handIndexes: number[] }
  | { type: "resolve_trigger_choice"; useTrigger: boolean; choiceId?: string | null }
  | { type: "resolve_draw_pile_reorder"; orderedChoiceIds: string[] }
  | { type: "advance_reveal" }
  | { type: "resolve_blessing_choice"; useBlessing: boolean }
  | { type: "advance_turn_transition" }
  | { type: "restart_battle" }
  | { type: "debug_add_card_to_hand"; drawPileIndex: number }
  | { type: "debug_battle_preset"; preset: DebugBattlePreset }
  | { type: "debug_place_card"; playerId: PlayerId; zone: DebugBattleZone; cardId: string }
  | { type: "debug_clear_zone"; playerId: PlayerId; zone: DebugBattleZone }
  | { type: "debug_set_phase"; phase: BattlePhase }
  | { type: "debug_start_reveal" }
  | { type: "debug_prompt_own_set_choice" }
  | { type: "debug_prompt_revealed_opponent_choice" }
  | { type: "debug_prompt_reorder_top_cards"; count?: number };

export const initialPrototypeState: PrototypeState = {
  screen: "title",
  activeSession: null,
  activeBattle: null,
  constructedSetup: null,
};

export function prototypeReducer(state: PrototypeState, action: PrototypeAction): PrototypeState {
  switch (action.type) {
    case "start_prototype":
      return {
        screen: "draft",
        activeSession: createInitialDraftSession(action.seed ?? Date.now()),
        activeBattle: null,
        constructedSetup: null,
      };
    case "start_constructed_select":
      return {
        screen: "constructed_select",
        activeSession: null,
        activeBattle: null,
        constructedSetup: {
          playerDeckId: state.constructedSetup?.playerDeckId ?? "standard_flow",
          cpuDeckId: state.constructedSetup?.cpuDeckId ?? "guard_stance",
        },
      };
    case "select_constructed_player_deck":
      return {
        ...state,
        constructedSetup: {
          playerDeckId: action.deckId,
          cpuDeckId: state.constructedSetup?.cpuDeckId ?? "guard_stance",
        },
      };
    case "select_constructed_cpu_deck":
      return {
        ...state,
        constructedSetup: {
          playerDeckId: state.constructedSetup?.playerDeckId ?? "standard_flow",
          cpuDeckId: action.deckId,
        },
      };
    case "start_constructed_battle":
      if (!state.constructedSetup?.playerDeckId || !state.constructedSetup?.cpuDeckId) {
        return state;
      }
      return {
        ...state,
        screen: "battle",
        activeSession: null,
        activeBattle: createBattleSessionFromDecks(
          buildPresetDeckState(state.constructedSetup.playerDeckId),
          buildPresetDeckState(state.constructedSetup.cpuDeckId),
          action.seed ?? Date.now(),
          "p1",
        ),
      };
    case "return_to_title":
      return initialPrototypeState;
    case "start_debug_battle":
      return {
        screen: "battle",
        activeSession: null,
        activeBattle: createDebugBattleSession(action.seed ?? Date.now()),
        constructedSetup: null,
      };
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
        activeBattle: applyPlayerControlChoice(state.activeBattle, action.handIndex),
      };
    case "choose_mulligan":
      if (!state.activeBattle) {
        return state;
      }
      return {
        ...state,
        activeBattle: applyPlayerMulligan(state.activeBattle, action.handIndexes),
      };
    case "choose_battle_action":
      if (!state.activeBattle) {
        return state;
      }
      return {
        ...state,
        activeBattle: applyPlayerBattleAction(state.activeBattle, action.actionType, action.handIndexes),
      };
    case "resolve_blessing_choice":
      if (!state.activeBattle) {
        return state;
      }
      return {
        ...state,
        activeBattle: applyPlayerBlessingChoice(state.activeBattle, action.useBlessing),
      };
    case "advance_turn_transition":
      if (!state.activeBattle) {
        return state;
      }
      return {
        ...state,
        activeBattle: advanceTurnTransition(state.activeBattle),
      };
    case "restart_battle":
      if (!state.activeBattle) {
        return state;
      }
      return {
        ...state,
        screen: "battle",
        activeBattle: state.activeBattle.debugMode
          ? createDebugBattleSession(state.activeBattle.seed)
          : state.activeSession
            ? createBattleSessionFromDraft(state.activeSession)
            : state.constructedSetup?.playerDeckId && state.constructedSetup?.cpuDeckId
              ? createBattleSessionFromDecks(
                  buildPresetDeckState(state.constructedSetup.playerDeckId),
                  buildPresetDeckState(state.constructedSetup.cpuDeckId),
                  state.activeBattle.seed,
                  "p1",
                )
            : state.activeBattle,
      };
    case "resolve_trigger_choice":
      if (!state.activeBattle) {
        return state;
      }
      return {
        ...state,
        activeBattle: applyPlayerTriggerChoice(state.activeBattle, action.useTrigger, action.choiceId ?? null),
      };
    case "resolve_draw_pile_reorder":
      if (!state.activeBattle) {
        return state;
      }
      return {
        ...state,
        activeBattle: applyPlayerDrawPileReorder(state.activeBattle, action.orderedChoiceIds),
      };
    case "advance_reveal":
      if (!state.activeBattle) {
        return state;
      }
      return {
        ...state,
        activeBattle: advanceBattleReveal(state.activeBattle),
      };
    case "debug_add_card_to_hand":
      if (!state.activeBattle) {
        return state;
      }
      return {
        ...state,
        activeBattle: applyDebugAddCardToHand(state.activeBattle, action.drawPileIndex),
      };
    case "debug_battle_preset":
      if (!state.activeBattle) {
        return state;
      }
      return {
        ...state,
        activeBattle: applyDebugBattlePreset(state.activeBattle, action.preset),
      };
    case "debug_place_card":
      if (!state.activeBattle) {
        return state;
      }
      return {
        ...state,
        activeBattle: applyDebugPlaceCard(state.activeBattle, action.playerId, action.zone, action.cardId),
      };
    case "debug_clear_zone":
      if (!state.activeBattle) {
        return state;
      }
      return {
        ...state,
        activeBattle: applyDebugClearZone(state.activeBattle, action.playerId, action.zone),
      };
    case "debug_set_phase":
      if (!state.activeBattle) {
        return state;
      }
      return {
        ...state,
        activeBattle: applyDebugSetPhase(state.activeBattle, action.phase),
      };
    case "debug_start_reveal":
      if (!state.activeBattle) {
        return state;
      }
      return {
        ...state,
        activeBattle: applyDebugStartReveal(state.activeBattle),
      };
    case "debug_prompt_own_set_choice":
      if (!state.activeBattle) {
        return state;
      }
      return {
        ...state,
        activeBattle: applyDebugPromptOwnSetChoice(state.activeBattle),
      };
    case "debug_prompt_revealed_opponent_choice":
      if (!state.activeBattle) {
        return state;
      }
      return {
        ...state,
        activeBattle: applyDebugPromptRevealedOpponentChoice(state.activeBattle),
      };
    case "debug_prompt_reorder_top_cards":
      if (!state.activeBattle) {
        return state;
      }
      return {
        ...state,
        activeBattle: applyDebugPromptReorderTopCards(state.activeBattle, action.count ?? 3),
      };
    default:
      return state;
  }
}
