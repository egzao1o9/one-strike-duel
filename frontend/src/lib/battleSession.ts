import { createSeededRandom } from "./random";
import { getAllCards } from "./cards";
import type { CardDefinition, CardEffect } from "../types/cards";
import type {
  ActiveTurnModifier,
  BattleActionType,
  BattleFinalLine,
  BattlePlayerState,
  BattleRevealStep,
  BattleSession,
  BattleSetCard,
  DebugBattleZone,
  DebugBattlePreset,
  DraftDeckState,
  DraftSession,
  PlayerId,
} from "../types/prototype";

const HAND_LIMIT = 6;
const TURN_DRAW_LIMIT = 4;
const battleCardLibrary = new Map(getAllCards().map((card) => [card.id, card]));

function playerLabel(playerId: PlayerId) {
  return playerId === "p1" ? "プレイヤー" : "CPU";
}

function flattenDraftDeck(deck: DraftDeckState) {
  return [...deck.starter, ...deck.publicCards, ...deck.hiddenCards];
}

function cloneCard(card: CardDefinition): CardDefinition {
  return {
    ...card,
    tags: [...card.tags],
    effects: card.effects.map((effect) => ({ ...effect })),
  };
}

function getBattleCard(cardId: string) {
  const card = battleCardLibrary.get(cardId);
  if (!card) {
    throw new Error(`Unknown battle debug card: ${cardId}`);
  }
  return cloneCard(card);
}

function shuffleCards(cards: CardDefinition[], seed: number) {
  const rng = createSeededRandom(seed);
  const next = [...cards].map(cloneCard);
  for (let index = next.length - 1; index > 0; index -= 1) {
    const swapIndex = rng.int(index + 1);
    [next[index], next[swapIndex]] = [next[swapIndex], next[index]];
  }
  return next;
}

function drawCards(player: BattlePlayerState, count: number) {
  const drawn: CardDefinition[] = [];
  for (let index = 0; index < count; index += 1) {
    if (player.drawPile.length === 0) {
      if (player.discardPile.length === 0) {
        break;
      }
      player.drawPile = shuffleCards(player.discardPile, player.drawPile.length + player.hand.length + index + 1);
      player.discardPile = [];
    }
    const card = player.drawPile.shift();
    if (!card) {
      break;
    }
    drawn.push(card);
  }
  player.hand.push(...drawn);
  return drawn;
}

function mulliganCards(player: BattlePlayerState, cardIds: string[]) {
  const discarded: CardDefinition[] = [];
  for (const cardId of cardIds) {
    const index = player.hand.findIndex((card) => card.id === cardId);
    if (index < 0) {
      continue;
    }
    const [card] = player.hand.splice(index, 1);
    if (card) {
      discarded.push(card);
    }
  }
  player.discardPile.push(...discarded);
  const drawn = drawCards(player, discarded.length);
  return { discarded, drawn };
}

function drawAtTurnStart(player: BattlePlayerState, turn: number) {
  const drawBonus = player.queuedNextTurnDrawDelta;
  player.queuedNextTurnDrawDelta = 0;
  const passiveDrawBonus =
    player.blessingZone && player.blessingFaceUp
      ? player.blessingZone.effects.reduce((sum, effect) => {
          if (effect.trigger === "passive" && effect.effect_type === "modify_rule_value" && effect.stat === "draw_per_turn") {
            return sum + (effect.value ?? 0);
          }
          return sum;
        }, 0)
      : 0;
  const base = turn === 1 ? 0 : TURN_DRAW_LIMIT;
  const drawTarget = Math.max(0, base + drawBonus + passiveDrawBonus);
  const capacity = Math.max(0, HAND_LIMIT - player.hand.length);
  return drawCards(player, Math.min(drawTarget, capacity));
}

function buildBattlePlayerState(deck: DraftDeckState, seed: number): BattlePlayerState {
  const drawPile = shuffleCards(flattenDraftDeck(deck), seed);
  const hand = drawPile.splice(0, 4);
  return {
    drawPile,
    hand,
    topdeckAsHandCardId: null,
    discardPile: [],
    usedCards: [],
    currentControlCard: null,
    blessingZone: null,
    blessingFaceUp: true,
    blessingLockedThisTurn: false,
    queuedNextTurnDrawDelta: 0,
    queuedNextTurnStatDelta: {
      attack: 0,
      block: 0,
      speed: 0,
    },
    activeTurnModifiers: [],
    setCards: [],
    battlePassed: false,
    revealFirstSetThisTurn: false,
  };
}

function chooseCpuMulliganCardIds(player: BattlePlayerState) {
  return player.hand
    .filter((card) => {
      if (card.card_type === "blessing") {
        return true;
      }
      if (card.card_type === "control") {
        return !card.effects.some((effect) => (effect.kind || effect.effect_type) === "draw_cards");
      }
      return card.attack <= 0 && card.speed <= 0;
    })
    .slice(0, 2)
    .map((card) => card.id);
}

function cloneSetCard(item: BattleSetCard): BattleSetCard {
  return { card: cloneCard(item.card), revealed: item.revealed };
}

function clonePlayerState(player: BattlePlayerState): BattlePlayerState {
  return {
    drawPile: player.drawPile.map(cloneCard),
    hand: player.hand.map(cloneCard),
    topdeckAsHandCardId: player.topdeckAsHandCardId,
    discardPile: player.discardPile.map(cloneCard),
    usedCards: player.usedCards.map(cloneCard),
    currentControlCard: player.currentControlCard ? cloneCard(player.currentControlCard) : null,
    blessingZone: player.blessingZone ? cloneCard(player.blessingZone) : null,
    blessingFaceUp: player.blessingFaceUp,
    blessingLockedThisTurn: player.blessingLockedThisTurn,
    queuedNextTurnDrawDelta: player.queuedNextTurnDrawDelta,
    queuedNextTurnStatDelta: { ...player.queuedNextTurnStatDelta },
    activeTurnModifiers: player.activeTurnModifiers.map((modifier) => ({ ...modifier })),
    setCards: player.setCards.map(cloneSetCard),
    battlePassed: player.battlePassed,
    revealFirstSetThisTurn: player.revealFirstSetThisTurn,
  };
}

function cloneBattleSession(session: BattleSession): BattleSession {
  return {
    ...session,
    players: {
      p1: clonePlayerState(session.players.p1),
      p2: clonePlayerState(session.players.p2),
    },
    finalLines: session.finalLines ? { p1: { ...session.finalLines.p1 }, p2: { ...session.finalLines.p2 } } : null,
    revealSteps: session.revealSteps.map((step) => ({ ...step })),
    logs: session.logs.map((entry) => ({ ...entry })),
    effectLogs: session.effectLogs.map((entry) => ({ ...entry })),
    pendingBlessingChoice: session.pendingBlessingChoice
      ? {
          ...session.pendingBlessingChoice,
          previewLines: {
            p1: { ...session.pendingBlessingChoice.previewLines.p1 },
            p2: { ...session.pendingBlessingChoice.previewLines.p2 },
          },
        }
      : null,
    pendingTriggerChoice: session.pendingTriggerChoice
      ? {
          ...session.pendingTriggerChoice,
          choices: session.pendingTriggerChoice.choices?.map((choice) => ({ ...choice })),
        }
      : null,
    pendingTriggerContinuation: session.pendingTriggerContinuation
      ? { ...session.pendingTriggerContinuation }
      : null,
    pendingReveal: session.pendingReveal
      ? {
          nextIndex: session.pendingReveal.nextIndex,
          steps: session.pendingReveal.steps.map((step) => ({ ...step })),
        }
      : null,
  };
}

function pushLog(session: BattleSession, text: string) {
  session.logs.push({ id: `battle-${session.logs.length + 1}`, text });
}

function pushEffectLog(session: BattleSession, playerId: PlayerId, sourceCard: CardDefinition, text: string) {
  session.effectLogs.push({
    id: `effect-${session.effectLogs.length + 1}`,
    playerId,
    sourceCardId: sourceCard.id,
    sourceCardName: sourceCard.name || sourceCard.id,
    text,
  });
  pushLog(session, `[Effect] ${playerLabel(playerId)} ${sourceCard.name || sourceCard.id}: ${text}`);
}

function otherPlayer(playerId: PlayerId): PlayerId {
  return playerId === "p1" ? "p2" : "p1";
}

function countBattleCards(setCards: BattleSetCard[]) {
  return setCards.filter((item) => item.card.card_type === "battle").length;
}

function makeModifier(sourceId: string) {
  return {
    sourceId,
    attack: 0,
    block: 0,
    speed: 0,
    opponentAttack: 0,
    opponentBlock: 0,
    opponentSpeed: 0,
  } satisfies ActiveTurnModifier;
}

function applyStatEffect(modifier: ActiveTurnModifier, effect: CardEffect) {
  const kind = effect.kind;
  const value = effect.value ?? 0;
  if (kind === "modify_self_attack") modifier.attack += value;
  if (kind === "modify_self_block") modifier.block += value;
  if (kind === "modify_self_speed") modifier.speed += value;
  if (kind === "modify_opponent_attack") modifier.opponentAttack -= value;
  if (kind === "modify_opponent_block") modifier.opponentBlock -= value;
  if (kind === "modify_opponent_speed") modifier.opponentSpeed -= value;
  if (effect.effect_type === "modify_total_stat") {
    if (effect.target === "self_total" && effect.stat === "attack") modifier.attack += value;
    if (effect.target === "self_total" && effect.stat === "block") modifier.block += value;
    if (effect.target === "self_total" && effect.stat === "speed") modifier.speed += value;
    if (effect.target === "opponent_total" && effect.stat === "attack") modifier.opponentAttack -= value;
    if (effect.target === "opponent_total" && effect.stat === "block") modifier.opponentBlock -= value;
    if (effect.target === "opponent_total" && effect.stat === "speed") modifier.opponentSpeed -= value;
  }
}

function describeEffect(effect: CardEffect) {
  return effect.display_text || effect.effect_text || effect.kind || effect.effect_type || "effect";
}

function buildAcknowledgeChoices(cards: CardDefinition[], prefix: string) {
  return cards.map((shownCard, index) => ({
    id: `${prefix}:${index}`,
    label: shownCard.name || shownCard.id,
    card: shownCard,
  }));
}

function buildDiscardCardChoices(playerId: PlayerId, cards: CardDefinition[], prefix = "discard") {
  return cards.map((discardCard, index) => ({
    id: `${prefix}:${index}`,
    label: discardCard.name || discardCard.id,
    card: discardCard,
    payload: {
      kind: "discard_card" as const,
      playerId,
      discardIndex: index,
      cardId: discardCard.id,
    },
  }));
}

function buildSetCardChoices(
  playerId: PlayerId,
  setCards: BattleSetCard[],
  options?: { revealedOnly?: boolean; hiddenOnly?: boolean; battleOnly?: boolean; prefix?: string },
) {
  const revealedOnly = options?.revealedOnly ?? false;
  const hiddenOnly = options?.hiddenOnly ?? false;
  const battleOnly = options?.battleOnly ?? false;
  const prefix = options?.prefix ?? "set";

  return setCards
    .map((item, index) => ({ item, index }))
    .filter(({ item }) => {
      if (revealedOnly && !item.revealed) return false;
      if (hiddenOnly && item.revealed) return false;
      if (battleOnly && item.card.card_type !== "battle") return false;
      return true;
    })
    .map(({ item, index }) => ({
      id: `${prefix}:${index}`,
      label: item.card.name || item.card.id,
      card: item.revealed ? item.card : undefined,
      payload: {
        kind: "set_card" as const,
        playerId,
        setIndex: index,
        cardId: item.card.id,
      },
    }));
}

function buildHandCardChoices(
  playerId: PlayerId,
  cards: CardDefinition[],
  options?: { battleOnly?: boolean; prefix?: string },
) {
  const battleOnly = options?.battleOnly ?? false;
  const prefix = options?.prefix ?? "hand";
  return cards
    .map((card, index) => ({ card, index }))
    .filter(({ card }) => (!battleOnly ? true : card.card_type === "battle"))
    .map(({ card, index }) => ({
      id: `${prefix}:${index}`,
      label: card.name || card.id,
      card,
      payload: {
        kind: "hand_card" as const,
        playerId,
        handIndex: index,
        cardId: card.id,
      },
    }));
}

export function buildDrawPileCardChoices(playerId: PlayerId, cards: CardDefinition[], count: number, prefix = "draw") {
  return cards.slice(0, count).map((card, index) => ({
    id: `${prefix}:${index}`,
    label: card.name || card.id,
    card,
    payload: {
      kind: "draw_pile_card" as const,
      playerId,
      drawPileIndex: index,
      cardId: card.id,
    },
  }));
}

export function buildUsedCardChoices(playerId: PlayerId, cards: CardDefinition[], prefix = "used") {
  return cards.map((card, index) => ({
    id: `${prefix}:${index}`,
    label: card.name || card.id,
    card,
    payload: {
      kind: "used_card" as const,
      playerId,
      usedIndex: index,
      cardId: card.id,
    },
  }));
}

function applyImmediateControlEffect(session: BattleSession, playerId: PlayerId, card: CardDefinition, effect: CardEffect) {
  const player = session.players[playerId];
  const opponent = session.players[otherPlayer(playerId)];
  const modifier = makeModifier(card.id);
  const effectKey = effect.kind || effect.effect_type;

  if (
    effectKey === "modify_self_attack" ||
    effectKey === "modify_self_block" ||
    effectKey === "modify_self_speed" ||
    effectKey === "modify_opponent_attack" ||
    effectKey === "modify_opponent_block" ||
    effectKey === "modify_opponent_speed" ||
    effect.effect_type === "modify_total_stat"
  ) {
    applyStatEffect(modifier, effect);
    player.activeTurnModifiers.push(modifier);
    return;
  }

  if (effectKey === "draw_cards") {
    const drawn = drawCards(player, effect.value ?? effect.count ?? 0);
    pushLog(session, playerLabel(playerId) + "は" + drawn.length + "枚引いた。");
    return;
  }

  if (effect.effect_type === "modify_rule_value" && effect.stat === "draw_per_turn") {
    player.queuedNextTurnDrawDelta += effect.value ?? 0;
    return;
  }

  if (effect.effect_type === "reveal_cards") {
    if (effect.target === "opponent_hand" && opponent.hand.length > 0) {
      const shown = opponent.hand[0];
      pushLog(session, playerLabel(playerId) + "は相手の手札を見た: " + (shown.name || shown.id));
    } else if (effect.target === "opponent_deck" && opponent.drawPile.length > 0) {
      const shown = opponent.drawPile[0];
      pushLog(session, playerLabel(playerId) + "は相手の山札トップを見た: " + (shown.name || shown.id));
    } else if (effect.target === "self_deck" && player.drawPile.length > 0) {
      const shown = player.drawPile[0];
      pushLog(session, playerLabel(playerId) + "は自分の山札トップを見た: " + (shown.name || shown.id));
    }
  }
}
void applyImmediateControlEffect;

function applyImmediateControlEffectV2(session: BattleSession, playerId: PlayerId, card: CardDefinition, effect: CardEffect) {
  const player = session.players[playerId];
  const opponent = session.players[otherPlayer(playerId)];
  const modifier = makeModifier(card.id);
  const effectKey = effect.kind || effect.effect_type;

  if (
    effectKey === "modify_self_attack" ||
    effectKey === "modify_self_block" ||
    effectKey === "modify_self_speed" ||
    effectKey === "modify_opponent_attack" ||
    effectKey === "modify_opponent_block" ||
    effectKey === "modify_opponent_speed" ||
    effect.effect_type === "modify_total_stat"
  ) {
    applyStatEffect(modifier, effect);
    player.activeTurnModifiers.push(modifier);
    pushEffectLog(session, playerId, card, describeEffect(effect));
    return;
  }

  if (effect.timing === "next_turn") {
    if (effectKey === "draw_cards") {
      player.queuedNextTurnDrawDelta += effect.value ?? effect.count ?? 0;
      pushEffectLog(session, playerId, card, describeEffect(effect));
      return;
    }
    if (effectKey === "modify_self_attack") {
      player.queuedNextTurnStatDelta.attack += effect.value ?? 0;
      pushEffectLog(session, playerId, card, describeEffect(effect));
      return;
    }
    if (effectKey === "modify_self_block") {
      player.queuedNextTurnStatDelta.block += effect.value ?? 0;
      pushEffectLog(session, playerId, card, describeEffect(effect));
      return;
    }
    if (effectKey === "modify_self_speed") {
      player.queuedNextTurnStatDelta.speed += effect.value ?? 0;
      pushEffectLog(session, playerId, card, describeEffect(effect));
      return;
    }
  }

  if (effectKey === "draw_cards") {
    drawCards(player, effect.value ?? effect.count ?? 0);
    pushEffectLog(session, playerId, card, describeEffect(effect));
    return;
  }

  if (effect.effect_type === "modify_rule_value" && effect.stat === "draw_per_turn") {
    player.queuedNextTurnDrawDelta += effect.value ?? 0;
    pushEffectLog(session, playerId, card, describeEffect(effect));
    return;
  }

  if (effect.effect_type === "reveal_cards") {
    const shownCards: CardDefinition[] = [];
    if (effect.target === "opponent_hand" && opponent.hand.length > 0) {
      const randomIndex = Math.abs(session.seed + session.turn + opponent.hand.length) % opponent.hand.length;
      const shown = opponent.hand[randomIndex];
      if (shown) {
        shownCards.push(shown);
        pushLog(session, playerLabel(playerId) + "は相手の手札を見た: " + (shown.name || shown.id));
      }
    } else if (effect.target === "opponent_deck" && opponent.drawPile.length > 0) {
      const shown = opponent.drawPile[0];
      if (shown) {
        shownCards.push(shown);
        pushLog(session, playerLabel(playerId) + "は相手の山札トップを見た: " + (shown.name || shown.id));
      }
    } else if (effect.target === "self_deck" && player.drawPile.length > 0) {
      const shown = player.drawPile[0];
      if (shown) {
        shownCards.push(shown);
        pushLog(session, playerLabel(playerId) + "は自分の山札トップを見た: " + (shown.name || shown.id));
      }
    }
    if (playerId === "p1" && shownCards.length > 0) {
      session.phase = "trigger_prompt";
      session.pendingTriggerChoice = {
        playerId,
        blessingCardId: card.id,
        blessingName: card.name || card.id,
        promptText: describeEffect(effect),
        mode: "acknowledge",
        choices: buildAcknowledgeChoices(shownCards, "reveal"),
      };
      session.pendingTriggerContinuation = { nextActor: null, resume: "control_after_player" };
    }
    pushEffectLog(session, playerId, card, describeEffect(effect));
  }
}

function applyControlCustom(session: BattleSession, playerId: PlayerId, card: CardDefinition) {
  const player = session.players[playerId];
  const opponent = session.players[otherPlayer(playerId)];

  switch (card.id) {
    case "control_blessing_flip":
      if (opponent.blessingZone && opponent.blessingFaceUp) {
        opponent.blessingFaceUp = false;
        pushEffectLog(session, playerId, card, "相手の加護を裏向きにした。");
      } else if (player.blessingZone && !player.blessingFaceUp) {
        player.blessingFaceUp = true;
        pushEffectLog(session, playerId, card, "自分の裏向き加護を表に戻した。");
      }
      break;
    case "control_blessing_break":
      if (opponent.blessingZone) {
        opponent.discardPile.push(opponent.blessingZone);
        opponent.blessingZone = null;
        opponent.blessingFaceUp = true;
        pushEffectLog(session, playerId, card, "相手の加護を捨てた。");
      }
      break;
    case "control_blessing_lock":
      opponent.blessingLockedThisTurn = true;
      pushEffectLog(session, playerId, card, "このターン相手は加護を使えない。");
      break;
    case "control_defile":
      if (opponent.blessingZone && opponent.blessingFaceUp) {
        opponent.blessingFaceUp = false;
        pushEffectLog(session, playerId, card, "相手の加護を裏向きにした。");
      }
      break;
    case "control_redraw_hand": {
      const redrawCount = player.hand.length;
      player.discardPile.push(...player.hand);
      player.hand = [];
      drawCards(player, redrawCount);
      pushEffectLog(session, playerId, card, "手札を引き直した。(" + redrawCount + "枚)");
      break;
    }
    case "control_topdeck_hand": {
      if (player.drawPile.length > 0) {
        const shown = player.drawPile[0];
        if (shown) {
          player.hand.push(cloneCard(shown));
          player.topdeckAsHandCardId = shown.id;
          pushEffectLog(session, playerId, card, "山札トップを公開し、このターン手札として使える: " + (shown.name || shown.id));
        }
      }
      break;
    }
    case "control_discard_facedown_blessing":
      if (player.blessingZone && !player.blessingFaceUp) {
        player.discardPile.push(player.blessingZone);
        player.blessingZone = null;
        player.blessingFaceUp = true;
        pushEffectLog(session, playerId, card, "自分の裏向き加護を捨てた。");
      }
      break;
    case "control_hand_echo": {
      if (opponent.hand.length > 0) {
        const discardIndex = session.seed % opponent.hand.length;
        const discarded = opponent.hand.splice(discardIndex, 1)[0]!;
        opponent.discardPile.push(discarded);
        const choices = buildDiscardCardChoices(otherPlayer(playerId), opponent.discardPile);
        if (playerId === "p1") {
          if (choices.length > 0) {
            session.phase = "trigger_prompt";
            session.pendingTriggerChoice = {
              playerId,
              blessingCardId: card.id,
              blessingName: card.name || card.id,
              promptText: "相手の捨て札から1枚選び、相手の手札に戻します。",
              mode: "choose_option",
              choices,
            };
            session.pendingTriggerContinuation = { nextActor: null, resume: "control_after_player" };
            pushEffectLog(session, playerId, card, "相手に1枚捨てさせた。戻すカードを選ぶ。");
          } else {
            pushEffectLog(session, playerId, card, "相手に1枚捨てさせたが、戻すカードがない。");
          }
        } else {
          const returned = opponent.discardPile.pop();
          if (returned) {
            opponent.hand.push(returned);
          }
          pushEffectLog(session, playerId, card, "相手に1枚捨てさせ、" + (returned?.name || returned?.id || "1枚") + "を手札に戻した。");
        }
      }
      break;
    }
    case "control_all_in_focus":
      if (playerId === "p1") {
        const choices = buildHandCardChoices(playerId, player.hand, { battleOnly: true });
        if (choices.length > 0) {
          session.phase = "trigger_prompt";
          session.pendingTriggerChoice = {
            playerId,
            blessingCardId: card.id,
            blessingName: card.name || card.id,
            promptText: "攻撃を上げる自分のバトルカードを1枚選ぶ。",
            mode: "choose_option",
            choices,
          };
          session.pendingTriggerContinuation = { nextActor: null, resume: "control_after_player" };
          pushEffectLog(session, playerId, card, "攻撃を上げる自分のカードを選ぶ。");
          break;
        }
      } else {
        const battleCards = player.hand.filter((handCard) => handCard.card_type === "battle");
        const target = [...battleCards].sort((left, right) => (right.attack + right.speed) - (left.attack + left.speed))[0];
        if (target) {
          target.attack += 2;
          player.queuedNextTurnDrawDelta -= 1;
          pushEffectLog(session, playerId, card, (target.name || target.id) + "の攻撃を+2し、次のターンのドロー-1。");
          break;
        }
      }
      player.queuedNextTurnDrawDelta -= 1;
      pushEffectLog(session, playerId, card, "次のターンのドロー-1。");
      break;
    case "control_opening_read":
      opponent.revealFirstSetThisTurn = true;
      pushEffectLog(session, playerId, card, "このターン相手の1枚目のセットを公開にした。");
      break;
    case "control_opening_expose":
      player.revealFirstSetThisTurn = true;
      opponent.revealFirstSetThisTurn = true;
      pushEffectLog(session, playerId, card, "このターンお互いの1枚目のセットを公開にした。");
      break;
  }
}

function chooseCpuControlCard(session: BattleSession, playerId: PlayerId): string | null {
  const player = session.players[playerId];
  const opponent = session.players[otherPlayer(playerId)];
  const controls = player.hand.filter((card) => card.card_type === "control" || (card.card_type === "blessing" && !player.blessingZone));
  if (controls.length === 0) {
    return null;
  }

  const scored = controls
    .map((card) => {
      let score = 0;
      if (card.card_type === "blessing") {
        score += player.blessingZone ? -10 : 2.5;
      }
      for (const effect of card.effects) {
        const key = effect.kind || effect.effect_type;
        if (key === "modify_self_attack") score += 1.2;
        if (key === "modify_self_speed") score += 1.1;
        if (key === "modify_self_block") score += 0.9;
        if (key === "modify_opponent_attack") score += 1.0;
        if (key === "modify_opponent_block") score += 1.0;
        if (key === "modify_opponent_speed") score += 0.8;
        if (key === "draw_cards") score += 0.9;
        if (key === "negate_opponent_first_card") score += 1.2;
      }
      if (card.id === "control_blessing_break" && opponent.blessingZone) score += 2.2;
      if (card.id === "control_blessing_lock" && opponent.blessingZone && opponent.blessingFaceUp) score += 1.8;
      if (card.id === "control_defile" && opponent.blessingZone && opponent.blessingFaceUp) score += 1.6;
      if (card.id === "control_all_in_focus") score += 1.7;
      if (card.id === "control_redraw_hand" && player.hand.length >= 3) score += 1.2;
      if (card.id === "control_topdeck_hand" && player.drawPile.length > 0) score += 0.8;
      if (card.id === "control_hand_echo" && opponent.hand.length > 0) score += 1.1;
      if (card.id === "control_opening_read") score += 0.9;
      if (card.id === "control_opening_expose") score += 0.6;
      return { cardId: card.id, score };
    })
    .sort((left, right) => right.score - left.score);

  return scored[0]?.score && scored[0].score > 0.7 ? scored[0].cardId : null;
}

function removeCardFromHand(player: BattlePlayerState, cardId: string) {
  const index = player.hand.findIndex((card) => card.id === cardId);
  if (index < 0) {
    return null;
  }
  return player.hand.splice(index, 1)[0] ?? null;
}

function applyControlChoice(session: BattleSession, playerId: PlayerId, cardId: string | null) {
  if (!cardId) {
    pushLog(session, playerLabel(playerId) + "はcontrolを使わなかった。");
    return;
  }
  const player = session.players[playerId];
  const card = removeCardFromHand(player, cardId);
  if (!card) {
    pushLog(session, playerLabel(playerId) + "はcontrolを使わなかった。");
    return;
  }

  if (card.card_type === "blessing") {
    if (!player.blessingZone) {
      player.blessingZone = card;
      player.blessingFaceUp = true;
      pushLog(session, playerLabel(playerId) + "は加護を置いた。");
      return;
    }
    player.hand.push(card);
    pushLog(session, playerLabel(playerId) + "は加護を置けなかった。");
    return;
  }

  player.currentControlCard = card;
  player.usedCards.push(card);
  pushLog(session, playerLabel(playerId) + "は" + (card.name || card.id) + "を使った。");
  for (const effect of card.effects) {
    applyImmediateControlEffectV2(session, playerId, card, effect);
  }
  applyControlCustom(session, playerId, card);
}

function legalBattleActions(session: BattleSession, playerId: PlayerId) {
  const player = session.players[playerId];
  const opponent = session.players[otherPlayer(playerId)];
  const legalSlots = Math.max(0, opponent.setCards.length + 1 - player.setCards.length);
  const playable = player.hand.filter((card) => card.card_type === "battle" || card.card_type === "control");
  const actions: Array<{ actionType: BattleActionType; cardIds: string[] }> = [];

  actions.push({ actionType: "pass", cardIds: [] });
  if (legalSlots <= 0 || playable.length === 0) {
    return actions;
  }
  for (const card of playable) {
    actions.push({ actionType: "set", cardIds: [card.id] });
    actions.push({ actionType: "set_pass", cardIds: [card.id] });
  }
  if (legalSlots >= 2) {
    for (let left = 0; left < playable.length; left += 1) {
      for (let right = left + 1; right < playable.length; right += 1) {
        actions.push({ actionType: "set", cardIds: [playable[left].id, playable[right].id] });
        actions.push({ actionType: "set_pass", cardIds: [playable[left].id, playable[right].id] });
      }
    }
  }
  return actions;
}

function estimateActionScore(session: BattleSession, playerId: PlayerId, actionType: BattleActionType, cardIds: string[]) {
  const player = session.players[playerId];
  const opponent = session.players[otherPlayer(playerId)];
  const cards = player.hand.filter((card) => cardIds.includes(card.id));
  const attack = cards.reduce((sum, card) => sum + Math.max(card.attack, 0), 0);
  const block = cards.reduce((sum, card) => sum + Math.max(card.block, 0), 0);
  const speed = cards.reduce((sum, card) => sum + Math.max(card.speed, 0), 0);
  const oppSetPressure = opponent.setCards.length * 0.5;
  let score = attack * 1.0 + block * 0.8 + speed * 0.75 - oppSetPressure;
  for (const card of cards) {
    for (const effect of card.effects) {
      const key = effect.kind || effect.effect_type;
      if (key === "modify_self_attack" || key === "modify_opponent_block") score += 0.7 + Math.abs(effect.value ?? 0) * 0.18;
      if (key === "modify_self_speed" || key === "modify_opponent_speed") score += 0.5 + Math.abs(effect.value ?? 0) * 0.12;
      if (key === "modify_self_block" || key === "modify_opponent_attack") score += 0.55 + Math.abs(effect.value ?? 0) * 0.14;
      if (key === "negate_opponent_first_card") score += 1.0;
    }
  }
  if (actionType === "pass") score -= 2.2;
  if (actionType === "set_pass") score -= 0.2;
  return score;
}

function chooseCpuBattleAction(session: BattleSession, playerId: PlayerId) {
  const actions = legalBattleActions(session, playerId);
  const scored = actions.map((action) => ({
    ...action,
    score: estimateActionScore(session, playerId, action.actionType, action.cardIds),
  }));
  scored.sort((left, right) => right.score - left.score);
  return scored[0] ?? { actionType: "pass" as const, cardIds: [] };
}

function nextBattleActor(session: BattleSession, currentPlayer: PlayerId) {
  const player = session.players[currentPlayer];
  const opponentId = otherPlayer(currentPlayer);
  const opponent = session.players[opponentId];
  if (player.battlePassed && opponent.battlePassed) {
    return null;
  }
  if (opponent.battlePassed) {
    return currentPlayer;
  }
  return opponentId;
}

function applyBattleAction(session: BattleSession, playerId: PlayerId, actionType: BattleActionType, requestedIds: string[]) {
  const player = session.players[playerId];
  const opponent = session.players[otherPlayer(playerId)];
  const legalSlots = Math.max(0, opponent.setCards.length + 1 - player.setCards.length);
  const playable = player.hand.filter((card) => card.card_type === "battle" || card.card_type === "control");

  if (actionType === "pass" || legalSlots <= 0 || playable.length === 0) {
    player.battlePassed = true;
    pushLog(session, playerLabel(playerId) + "はpassした。");
    return;
  }

  const maxCards = Math.min(2, legalSlots);
  const chosen: CardDefinition[] = [];
  for (const cardId of requestedIds.slice(0, maxCards)) {
    const card = removeCardFromHand(player, cardId);
    if (card && (card.card_type === "battle" || card.card_type === "control")) {
      chosen.push(card);
    }
  }
  if (chosen.length === 0) {
    player.battlePassed = true;
    pushLog(session, playerLabel(playerId) + "はpassした。");
    return;
  }

  const shouldRevealFirstSet = player.revealFirstSetThisTurn && player.setCards.length === 0;
  player.setCards.push(
    ...chosen.map((card, index) => ({
      card,
      revealed: shouldRevealFirstSet && index === 0,
    })),
  );
  if (shouldRevealFirstSet) {
    player.revealFirstSetThisTurn = false;
    pushLog(session, playerLabel(playerId) + "の1枚目のセットは公開された。");
  }
  pushLog(session, playerLabel(playerId) + "は" + chosen.length + "枚セットした。");
  if (actionType === "set_pass") {
    player.battlePassed = true;
    pushLog(session, playerLabel(playerId) + "はセットしてpassした。");
  }
}

function applySetTriggeredBlessing(
  session: BattleSession,
  reactingPlayerId: PlayerId,
  actingPlayerId: PlayerId,
  nextActor: PlayerId | null,
) {
  const reactingPlayer = session.players[reactingPlayerId];
  const actingPlayer = session.players[actingPlayerId];
  const blessing = reactingPlayer.blessingZone;

  if (!blessing || !reactingPlayer.blessingFaceUp || reactingPlayer.blessingLockedThisTurn) {
    return false;
  }

  if (blessing.id === "blessing_insight") {
    const hiddenChoices = buildSetCardChoices(actingPlayerId, actingPlayer.setCards, {
      hiddenOnly: true,
      prefix: "set",
    });

    if (hiddenChoices.length === 0) {
      return false;
    }

    if (reactingPlayerId === "p1") {
      session.phase = "trigger_prompt";
      session.pendingTriggerChoice = {
        playerId: reactingPlayerId,
        blessingCardId: blessing.id,
        blessingName: blessing.name || blessing.id,
        promptText: blessing.effect_text || "Reveal one opponent set card.",
        mode: "choose_option",
        choices: hiddenChoices,
      };
      session.pendingTriggerContinuation = { nextActor, resume: "battle" };
      return true;
    }

    const setIndex = hiddenChoices[0]?.payload?.setIndex ?? -1;
    if (setIndex < 0) {
      return false;
    }
    actingPlayer.setCards[setIndex].revealed = true;
    reactingPlayer.blessingFaceUp = false;
    pushEffectLog(session, reactingPlayerId, blessing, blessing.effect_text || "Reveal one opponent set card.");
    return false;
  }

  if (blessing.id === "blessing_range" && actingPlayer.setCards.length >= 4) {
    if (reactingPlayerId === "p1") {
    session.phase = "trigger_prompt";
    session.pendingTriggerChoice = {
        playerId: reactingPlayerId,
        blessingCardId: blessing.id,
        blessingName: blessing.name || blessing.id,
      promptText: blessing.effect_text || "Opponent speed -2 this battle.",
      mode: "confirm_use",
    };
      session.pendingTriggerContinuation = { nextActor, resume: "battle" };
      return true;
    }

    reactingPlayer.activeTurnModifiers.push({
      sourceId: blessing.id,
      attack: 0,
      block: 0,
      speed: 0,
      opponentAttack: 0,
      opponentBlock: 0,
      opponentSpeed: -2,
    });
    reactingPlayer.blessingFaceUp = false;
    pushEffectLog(session, reactingPlayerId, blessing, blessing.effect_text || "Opponent speed -2 this battle.");
  }

  return false;
}

function sumBattleCards(setCards: BattleSetCard[]) {
  const battleCards = setCards.filter((item) => item.card.card_type === "battle");
  return {
    attack: battleCards.reduce((sum, item) => sum + item.card.attack, 0),
    block: battleCards.reduce((sum, item) => sum + item.card.block, 0),
    speed: battleCards.reduce((sum, item) => sum + item.card.speed, 0),
  };
}

function applyModifierPair(lines: Record<PlayerId, BattleFinalLine>, playerId: PlayerId, modifier: ActiveTurnModifier) {
  const opponentId = otherPlayer(playerId);
  lines[playerId].attack += modifier.attack;
  lines[playerId].block += modifier.block;
  lines[playerId].speed += modifier.speed;
  lines[opponentId].attack += modifier.opponentAttack;
  lines[opponentId].block += modifier.opponentBlock;
  lines[opponentId].speed += modifier.opponentSpeed;
}

function applyRevealedCardEffects(
  session: BattleSession,
  ownerId: PlayerId,
  item: BattleSetCard,
  lines: Record<PlayerId, BattleFinalLine>,
) {
  for (const effect of item.card.effects) {
    const key = effect.kind || effect.effect_type;
    if (key === "negate_opponent_first_card") {
      const opponentFirst = session.players[otherPlayer(ownerId)].setCards[0];
      if (opponentFirst?.revealed && opponentFirst.card.card_type === "battle") {
        lines[otherPlayer(ownerId)].attack -= opponentFirst.card.attack;
        lines[otherPlayer(ownerId)].block -= opponentFirst.card.block;
        lines[otherPlayer(ownerId)].speed -= opponentFirst.card.speed;
        pushEffectLog(session, ownerId, item.card, describeEffect(effect));
      }
      continue;
    }
    if (key === "set_self_block_limit") {
      lines[ownerId].block = Math.min(lines[ownerId].block, effect.value ?? 0);
      pushEffectLog(session, ownerId, item.card, describeEffect(effect));
      continue;
    }
    if (effect.effect_type === "modify_card_stat" && effect.target === "opponent_card" && effect.stat === "attack") {
      lines[otherPlayer(ownerId)].attack += effect.value ?? 0;
      pushEffectLog(session, ownerId, item.card, describeEffect(effect));
      continue;
    }
    const modifier = makeModifier(item.card.id);
    applyStatEffect(modifier, effect);
    applyModifierPair(lines, ownerId, modifier);
    pushEffectLog(session, ownerId, item.card, describeEffect(effect));
  }
}

function maybeApplyRevealTriggeredBlessing(
  session: BattleSession,
  reactingPlayerId: PlayerId,
  revealedPlayerId: PlayerId,
  revealedItem: BattleSetCard,
  lines: Record<PlayerId, BattleFinalLine>,
) {
  const reactingPlayer = session.players[reactingPlayerId];
  const blessing = reactingPlayer.blessingZone;
  if (!blessing || !reactingPlayer.blessingFaceUp || reactingPlayer.blessingLockedThisTurn) {
    return;
  }
  if (blessing.id !== "blessing_suppression") {
    return;
  }
  if (revealedPlayerId === reactingPlayerId) {
    return;
  }
  if (revealedItem.card.attack < 5) {
    return;
  }
  lines[revealedPlayerId].attack -= 3;
  reactingPlayer.blessingFaceUp = false;
  pushEffectLog(session, reactingPlayerId, blessing, blessing.effect_text || "相手の攻撃-3");
}

function resolveOutcome(lines: Record<PlayerId, BattleFinalLine>) {
  const p1 = lines.p1;
  const p2 = lines.p2;
  if (p1.speed === p2.speed) {
    const p1Success = p1.attack > 0 && p1.attack > p2.block;
    const p2Success = p2.attack > 0 && p2.attack > p1.block;
    if (p1Success && p2Success) return { winner: null, endReason: "simultaneous_attack" };
    if (p1Success) return { winner: "p1" as PlayerId, endReason: "p1_attack_success" };
    if (p2Success) return { winner: "p2" as PlayerId, endReason: "p2_attack_success" };
    return { winner: null, endReason: null };
  }
  const first: PlayerId = p1.speed > p2.speed ? "p1" : "p2";
  const second: PlayerId = otherPlayer(first);
  if (lines[first].attack > 0 && lines[first].attack > lines[second].block) {
    return { winner: first, endReason: first + "_attack_success" };
  }
  if (lines[second].attack > 0 && lines[second].attack > lines[first].block) {
    return { winner: second, endReason: second + "_attack_success" };
  }
  return { winner: null, endReason: null };
}

function copyLines(lines: Record<PlayerId, BattleFinalLine>) {
  return {
    p1: { ...lines.p1 },
    p2: { ...lines.p2 },
  };
}

function consumeBlessingIfHelpful(session: BattleSession, playerId: PlayerId, lines: Record<PlayerId, BattleFinalLine>, ownBattleCount: number, opponentBattleCount: number) {
  const player = session.players[playerId];
  const blessing = player.blessingZone;
  if (!blessing || !player.blessingFaceUp || player.blessingLockedThisTurn) {
    return;
  }

  const before = resolveOutcome(lines);
  const next = copyLines(lines);

  const applyAndMaybeConsume = (apply: () => void) => {
    apply();
    const after = resolveOutcome(next);
    const beforeLose = before.winner === otherPlayer(playerId);
    const afterWin = after.winner === playerId;
    const afterNotLose = after.winner !== otherPlayer(playerId);
    if ((!before.winner && afterWin) || (beforeLose && afterNotLose) || (before.winner !== playerId && afterWin)) {
      lines.p1 = next.p1;
      lines.p2 = next.p2;
      player.blessingFaceUp = false;
      pushLog(session, playerLabel(playerId) + "の加護が発動した。");
    }
  };

  switch (blessing.id) {
    case "blessing_attack":
      lines[playerId].attack += 1;
      break;
    case "blessing_guard":
      lines[playerId].block += 1;
      break;
    case "blessing_speed":
      lines[playerId].speed += 1;
      break;
    case "blessing_shortblade":
      applyAndMaybeConsume(() => {
        next[playerId].attack += 1;
      });
      break;
    case "blessing_buckler":
    case "blessing_parry":
      applyAndMaybeConsume(() => {
        next[playerId].block += 1;
      });
      break;
    case "blessing_tailwind":
      applyAndMaybeConsume(() => {
        next[playerId].speed += 1;
      });
      break;
    case "blessing_dullness":
      applyAndMaybeConsume(() => {
        next[otherPlayer(playerId)].speed -= 1;
      });
      break;
    case "blessing_offense":
      applyAndMaybeConsume(() => {
        next[playerId].attack += 2;
      });
      break;
    case "blessing_barrier":
    case "blessing_laststand":
      if (blessing.id !== "blessing_laststand" || ownBattleCount <= 2) {
        applyAndMaybeConsume(() => {
          next[playerId].block += blessing.id === "blessing_barrier" ? 2 : 2;
        });
      }
      break;
    case "blessing_slow":
      applyAndMaybeConsume(() => {
        next[otherPlayer(playerId)].speed -= 2;
      });
      break;
    case "blessing_trap_web":
      if (opponentBattleCount >= 3) {
        applyAndMaybeConsume(() => {
          next[otherPlayer(playerId)].attack -= 3;
        });
      }
      break;
    case "blessing_suppression":
      applyAndMaybeConsume(() => {
        next[otherPlayer(playerId)].attack -= 3;
      });
      break;
  }
}

function buildBlessingPreview(
  session: BattleSession,
  playerId: PlayerId,
  baseLines: Record<PlayerId, BattleFinalLine>,
  ownBattleCount: number,
  opponentBattleCount: number,
): { promptText: string; previewLines: Record<PlayerId, BattleFinalLine> } | null {
  const player = session.players[playerId];
  const blessing = player.blessingZone;
  if (!blessing || !player.blessingFaceUp || player.blessingLockedThisTurn) {
    return null;
  }

  const previewLines = copyLines(baseLines);
  const opponentId = otherPlayer(playerId);

  switch (blessing.id) {
    case "blessing_shortblade":
      previewLines[playerId].attack += 1;
      return { promptText: blessing.effect_text || "Attack +1", previewLines };
    case "blessing_offense":
      previewLines[playerId].attack += 2;
      return { promptText: blessing.effect_text || "Attack +2", previewLines };
    case "blessing_buckler":
    case "blessing_barrier":
      previewLines[playerId].block += blessing.id === "blessing_barrier" ? 2 : 1;
      return { promptText: blessing.effect_text || "Block up", previewLines };
    case "blessing_tailwind":
      previewLines[playerId].speed += 1;
      return { promptText: blessing.effect_text || "Speed +1", previewLines };
    case "blessing_dullness":
      previewLines[opponentId].speed -= 1;
      return { promptText: blessing.effect_text || "Opponent speed -1", previewLines };
    case "blessing_slow":
      previewLines[opponentId].speed -= 2;
      return { promptText: blessing.effect_text || "Opponent speed -2", previewLines };
    case "blessing_laststand":
      if (ownBattleCount <= 2) {
        previewLines[playerId].block += 2;
        return { promptText: blessing.effect_text || "Block +2", previewLines };
      }
      return null;
    case "blessing_parry":
      if (baseLines[opponentId].attack === baseLines[playerId].block + 1) {
        previewLines[playerId].block += 1;
        return { promptText: blessing.effect_text || "Parry", previewLines };
      }
      return null;
    case "blessing_trap_web":
      if (opponentBattleCount >= 3) {
        previewLines[opponentId].attack -= 3;
        return { promptText: blessing.effect_text || "Opponent attack -3", previewLines };
      }
      return null;
    case "blessing_suppression": {
      const hasLargeAttackCard = session.players[opponentId].setCards.some(
        (item) => item.revealed && item.card.attack >= 5,
      );
      if (hasLargeAttackCard) {
        previewLines[opponentId].attack -= 3;
        return { promptText: blessing.effect_text || "Suppress strong attack", previewLines };
      }
      return null;
    }
    default:
      return null;
  }
}

function shouldUseBlessingByOutcome(playerId: PlayerId, before: Record<PlayerId, BattleFinalLine>, after: Record<PlayerId, BattleFinalLine>) {
  const beforeOutcome = resolveOutcome(before);
  const afterOutcome = resolveOutcome(after);
  const opponentId = otherPlayer(playerId);
  if (afterOutcome.winner === playerId && beforeOutcome.winner !== playerId) {
    return true;
  }
  if (beforeOutcome.winner === opponentId && afterOutcome.winner !== opponentId) {
    return true;
  }
  return false;
}

function applyOptionalBlessingChoice(
  session: BattleSession,
  playerId: PlayerId,
  baseLines: Record<PlayerId, BattleFinalLine>,
  ownBattleCount: number,
  opponentBattleCount: number,
) {
  const preview = buildBlessingPreview(session, playerId, baseLines, ownBattleCount, opponentBattleCount);
  if (!preview) {
    return { used: false, lines: baseLines };
  }
  if (!shouldUseBlessingByOutcome(playerId, baseLines, preview.previewLines)) {
    return { used: false, lines: baseLines };
  }
  const player = session.players[playerId];
  if (player.blessingZone) {
    player.blessingFaceUp = false;
    pushEffectLog(session, playerId, player.blessingZone, preview.promptText);
  }
  return { used: true, lines: preview.previewLines };
}

function finalizeBattleResolution(session: BattleSession, lines: Record<PlayerId, BattleFinalLine>, revealSteps: BattleRevealStep[]) {
  const outcome = resolveOutcome(lines);
  session.finalLines = lines;
  session.revealSteps = revealSteps;

  if (outcome.winner) {
    session.phase = "result";
    session.winner = outcome.winner;
    session.endReason = outcome.endReason;
    pushLog(session, playerLabel(outcome.winner) + "の勝ち。");
  } else if (outcome.endReason === "simultaneous_attack") {
    session.phase = "result";
    session.winner = null;
    session.endReason = outcome.endReason;
    pushLog(session, "Draw");
  } else {
    pushLog(session, "No decisive hit");
    endTurnAndAdvance(session);
  }
}

function finishBattleAfterReveal(session: BattleSession) {
  const lines = session.finalLines;
  const revealSteps = session.revealSteps;
  if (!lines) {
    return;
  }
  const p1Preview = buildBlessingPreview(
    session,
    "p1",
    lines,
    countBattleCards(session.players.p1.setCards),
    countBattleCards(session.players.p2.setCards),
  );
  if (p1Preview) {
    session.phase = "blessing_prompt";
    session.pendingBlessingChoice = {
      playerId: "p1",
      blessingCardId: session.players.p1.blessingZone!.id,
      blessingName: session.players.p1.blessingZone!.name || session.players.p1.blessingZone!.id,
      promptText: p1Preview.promptText,
      previewLines: p1Preview.previewLines,
    };
    return;
  }

  const cpuResult = applyOptionalBlessingChoice(
    session,
    "p2",
    lines,
    countBattleCards(session.players.p2.setCards),
    countBattleCards(session.players.p1.setCards),
  );

  finalizeBattleResolution(session, cpuResult.lines, revealSteps);
}

function advanceRevealStep(session: BattleSession) {
  const pendingReveal = session.pendingReveal;
  const lines = session.finalLines;
  if (session.phase !== "reveal" || !pendingReveal || !lines) {
    return;
  }
  const step = pendingReveal.steps[pendingReveal.nextIndex];
  if (!step) {
    session.pendingReveal = null;
    finishBattleAfterReveal(session);
    return;
  }

  const item = session.players[step.playerId].setCards[step.index];
  if (!item) {
    pendingReveal.nextIndex += 1;
    if (pendingReveal.nextIndex >= pendingReveal.steps.length) {
      session.pendingReveal = null;
      finishBattleAfterReveal(session);
    }
    return;
  }

  item.revealed = true;
  session.revealSteps.push(step);
  if (item.card.card_type === "battle") {
    lines[step.playerId].attack += item.card.attack;
    lines[step.playerId].block += item.card.block;
    lines[step.playerId].speed += item.card.speed;
  }
  maybeApplyRevealTriggeredBlessing(session, otherPlayer(step.playerId), step.playerId, item, lines);
  const ownerBattleCount = countBattleCards(session.players[step.playerId].setCards);
  if (ownerBattleCount > 0) {
    applyRevealedCardEffects(session, step.playerId, item, lines);
  }

  pendingReveal.nextIndex += 1;
  if (pendingReveal.nextIndex >= pendingReveal.steps.length) {
    session.pendingReveal = null;
    finishBattleAfterReveal(session);
  }
}

function resolveBattleV2(session: BattleSession) {
  const order: PlayerId[] = [session.battleStartingPlayer, otherPlayer(session.battleStartingPlayer)];
  const maxCards = Math.max(session.players.p1.setCards.length, session.players.p2.setCards.length);

  const lines: Record<PlayerId, BattleFinalLine> = {
    p1: { attack: 0, block: 0, speed: 0 },
    p2: { attack: 0, block: 0, speed: 0 },
  };

  for (const playerId of ["p1", "p2"] as PlayerId[]) {
    for (const modifier of session.players[playerId].activeTurnModifiers) {
      applyModifierPair(lines, playerId, modifier);
      const sourceCard = session.players[playerId].currentControlCard ?? session.players[playerId].blessingZone;
      if (sourceCard) {
        pushEffectLog(session, playerId, sourceCard, "Turn modifier applied");
      }
    }
  }

  const revealSteps: BattleRevealStep[] = [];

  for (let index = 0; index < maxCards; index += 1) {
    for (const playerId of order) {
      const item = session.players[playerId].setCards[index];
      if (!item) {
        continue;
      }
      revealSteps.push({
        playerId,
        cardId: item.card.id,
        cardName: item.card.name || item.card.id,
        cardType: item.card.card_type,
        index,
      });
    }
  }
  session.finalLines = lines;
  session.revealSteps = [];
  session.pendingReveal = { steps: revealSteps, nextIndex: 0 };
  session.phase = "reveal";
  pushLog(session, "カード公開を開始する。");
}

function resolveBattle(session: BattleSession) {
  const revealSteps: BattleRevealStep[] = [];
  const order: PlayerId[] = [session.battleStartingPlayer, otherPlayer(session.battleStartingPlayer)];
  const maxCards = Math.max(session.players.p1.setCards.length, session.players.p2.setCards.length);

  for (let index = 0; index < maxCards; index += 1) {
    for (const playerId of order) {
      const item = session.players[playerId].setCards[index];
      if (!item) {
        continue;
      }
      item.revealed = true;
      revealSteps.push({
        playerId,
        cardId: item.card.id,
        cardName: item.card.name || item.card.id,
        cardType: item.card.card_type,
        index,
      });
    }
  }

  const lines: Record<PlayerId, BattleFinalLine> = {
    p1: sumBattleCards(session.players.p1.setCards),
    p2: sumBattleCards(session.players.p2.setCards),
  };

  for (const playerId of ["p1", "p2"] as PlayerId[]) {
    for (const modifier of session.players[playerId].activeTurnModifiers) {
      applyModifierPair(lines, playerId, modifier);
    }
  }

  for (const playerId of ["p1", "p2"] as PlayerId[]) {
    const ownBattleCount = countBattleCards(session.players[playerId].setCards);
    if (ownBattleCount === 0) {
      continue;
    }
    for (const item of session.players[playerId].setCards) {
      for (const effect of item.card.effects) {
        const key = effect.kind || effect.effect_type;
        if (key === "negate_opponent_first_card") {
          const opponentFirst = session.players[otherPlayer(playerId)].setCards[0];
          if (opponentFirst && opponentFirst.card.card_type === "battle") {
            lines[otherPlayer(playerId)].attack -= opponentFirst.card.attack;
            lines[otherPlayer(playerId)].block -= opponentFirst.card.block;
            lines[otherPlayer(playerId)].speed -= opponentFirst.card.speed;
          }
        } else {
          const modifier = makeModifier(item.card.id);
          applyStatEffect(modifier, effect);
          applyModifierPair(lines, playerId, modifier);
        }
      }
    }
  }

  consumeBlessingIfHelpful(session, "p1", lines, countBattleCards(session.players.p1.setCards), countBattleCards(session.players.p2.setCards));
  consumeBlessingIfHelpful(session, "p2", lines, countBattleCards(session.players.p2.setCards), countBattleCards(session.players.p1.setCards));

  const outcome = resolveOutcome(lines);
  session.finalLines = lines;
  session.revealSteps = revealSteps;

  if (outcome.winner) {
    session.phase = "result";
    session.winner = outcome.winner;
    session.endReason = outcome.endReason;
    pushLog(session, playerLabel(outcome.winner) + "の勝ち。");
  } else if (outcome.endReason === "simultaneous_attack") {
    session.phase = "result";
    session.winner = null;
    session.endReason = outcome.endReason;
    pushLog(session, "同時攻撃で引き分け。");
  } else {
    pushLog(session, "このターンは決着せず、次のターンへ。");
    endTurnAndAdvance(session);
  }
}
void resolveBattle;

function endTurnAndAdvance(session: BattleSession) {
  for (const playerId of ["p1", "p2"] as PlayerId[]) {
    const player = session.players[playerId];
    player.topdeckAsHandCardId = null;
    player.usedCards.push(...player.setCards.map((item) => item.card));
    player.discardPile.push(...player.setCards.map((item) => item.card));
    if (player.currentControlCard) {
      player.discardPile.push(player.currentControlCard);
      player.currentControlCard = null;
    }
    player.setCards = [];
    player.battlePassed = false;
    player.activeTurnModifiers = [];
    player.blessingLockedThisTurn = false;
    player.revealFirstSetThisTurn = false;
  }
  session.turn += 1;
  session.battleStartingPlayer = otherPlayer(session.battleStartingPlayer);
  session.actingPlayer = "p1";
  session.phase = "mulligan";
  for (const playerId of ["p1", "p2"] as PlayerId[]) {
    const player = session.players[playerId];
    const queued = player.queuedNextTurnStatDelta;
    if (queued.attack !== 0 || queued.block !== 0 || queued.speed !== 0) {
      player.activeTurnModifiers.push({
        sourceId: "next_turn_queue",
        attack: queued.attack,
        block: queued.block,
        speed: queued.speed,
        opponentAttack: 0,
        opponentBlock: 0,
        opponentSpeed: 0,
      });
      player.queuedNextTurnStatDelta = { attack: 0, block: 0, speed: 0 };
    }
  }
  const p1Drawn = drawAtTurnStart(session.players.p1, session.turn);
  const p2Drawn = drawAtTurnStart(session.players.p2, session.turn);
  pushLog(session, "マリガンフェーズへ。");
  pushLog(session, "ターン" + session.turn + "開始。プレイヤーは" + p1Drawn.length + "枚、CPUは" + p2Drawn.length + "枚引いた。");
}

function continueIfDrawnBattle(session: BattleSession) {
  if (session.phase === "result" && session.winner === null && session.endReason === "simultaneous_attack") {
    session.winner = null;
    session.endReason = null;
    pushLog(session, "同時攻撃で引き分け。次のターンへ。");
    endTurnAndAdvance(session);
  }
}

export function applyDebugBattlePreset(session: BattleSession, preset: DebugBattlePreset) {
  const next = cloneBattleSession(session);

  next.phase = "battle_select";
  next.actingPlayer = "p1";
  next.winner = null;
  next.endReason = null;
  next.finalLines = null;
  next.revealSteps = [];
  next.pendingBlessingChoice = null;
  next.pendingTriggerChoice = null;
  next.pendingTriggerContinuation = null;
  next.pendingReveal = null;

  for (const playerId of ["p1", "p2"] as PlayerId[]) {
    const player = next.players[playerId];
    player.currentControlCard = null;
    player.activeTurnModifiers = [];
    player.blessingLockedThisTurn = false;
    player.setCards = [];
  }

  const p1 = next.players.p1;
  const p2 = next.players.p2;

  p1.battlePassed = false;
  p2.battlePassed = true;
  p1.hand = [];
  p2.hand = [];

  switch (preset) {
    case "draw":
      p1.setCards = [{ card: getBattleCard("battle_attack"), revealed: false }];
      p2.setCards = [{ card: getBattleCard("battle_attack"), revealed: false }];
      pushLog(next, "DEBUG: Draw盤面をセットした。passで解決。");
      break;
    case "no_damage":
      p1.setCards = [{ card: getBattleCard("battle_defend"), revealed: false }];
      p2.setCards = [{ card: getBattleCard("battle_defend"), revealed: false }];
      pushLog(next, "DEBUG: 決着なし盤面をセットした。passで解決。");
      break;
    case "p1_win":
      p1.setCards = [{ card: getBattleCard("battle_all_in"), revealed: false }];
      p2.setCards = [{ card: getBattleCard("battle_defend"), revealed: false }];
      pushLog(next, "DEBUG: プレイヤー勝ち盤面をセットした。passで解決。");
      break;
    case "p2_win":
      p1.setCards = [{ card: getBattleCard("battle_defend"), revealed: false }];
      p2.setCards = [{ card: getBattleCard("battle_all_in"), revealed: false }];
      pushLog(next, "DEBUG: CPU勝ち盤面をセットした。passで解決。");
      break;
  }

  return next;
}

function advanceCpuBattleLoop(session: BattleSession) {
  while (session.phase === "battle_select" && session.actingPlayer === "p2") {
    const choice = chooseCpuBattleAction(session, "p2");
    applyBattleAction(session, "p2", choice.actionType, choice.cardIds);
    const nextActor = nextBattleActor(session, "p2");
    if (applySetTriggeredBlessing(session, "p1", "p2", nextActor)) {
      return;
    }
    if (nextActor === null) {
      resolveBattleV2(session);
      return;
    }
    session.actingPlayer = nextActor;
    if (nextActor === "p2" && session.players.p2.battlePassed) {
      resolveBattleV2(session);
      return;
    }
  }
}

export function createBattleSessionFromDraft(session: DraftSession): BattleSession {
  const p1 = buildBattlePlayerState(session.decks.p1, session.seed + 101);
  const p2 = buildBattlePlayerState(session.decks.p2, session.seed + 202);
  return {
    debugMode: false,
    seed: session.seed,
    turn: 1,
    phase: "mulligan",
    firstPlayer: session.firstPlayer,
    battleStartingPlayer: session.firstPlayer,
    actingPlayer: "p1",
    players: { p1, p2 },
    finalLines: null,
    revealSteps: [],
    winner: null,
    endReason: null,
    logs: [
      { id: "battle-1", text: "対戦準備が完了した。" },
      { id: "battle-2", text: "先手は" + playerLabel(session.firstPlayer) + "。" },
      { id: "battle-3", text: "プレイヤーは初期手札を" + p1.hand.length + "枚引いた。" },
      { id: "battle-4", text: "CPUは初期手札を" + p2.hand.length + "枚引いた。" },
      { id: "battle-5", text: "最初に1回だけマリガンを行う。" },
    ],
    effectLogs: [],
    pendingBlessingChoice: null,
    pendingTriggerChoice: null,
    pendingTriggerContinuation: null,
    pendingReveal: null,
  };
}

export function createDebugBattleSession(seed: number = Date.now()): BattleSession {
  return {
    debugMode: true,
    seed,
    turn: 1,
    phase: "control",
    firstPlayer: "p1",
    battleStartingPlayer: "p1",
    actingPlayer: "p1",
    players: {
      p1: {
        drawPile: [],
        hand: [],
        topdeckAsHandCardId: null,
        discardPile: [],
        usedCards: [],
        currentControlCard: null,
        blessingZone: null,
        blessingFaceUp: true,
        blessingLockedThisTurn: false,
        queuedNextTurnDrawDelta: 0,
        queuedNextTurnStatDelta: { attack: 0, block: 0, speed: 0 },
        activeTurnModifiers: [],
        setCards: [],
        battlePassed: false,
        revealFirstSetThisTurn: false,
      },
      p2: {
        drawPile: [],
        hand: [],
        topdeckAsHandCardId: null,
        discardPile: [],
        usedCards: [],
        currentControlCard: null,
        blessingZone: null,
        blessingFaceUp: true,
        blessingLockedThisTurn: false,
        queuedNextTurnDrawDelta: 0,
        queuedNextTurnStatDelta: { attack: 0, block: 0, speed: 0 },
        activeTurnModifiers: [],
        setCards: [],
        battlePassed: false,
        revealFirstSetThisTurn: false,
      },
    },
    finalLines: null,
    revealSteps: [],
    winner: null,
    endReason: null,
    logs: [{ id: "battle-1", text: "Debug battle session started." }],
    effectLogs: [],
    pendingBlessingChoice: null,
    pendingTriggerChoice: null,
    pendingTriggerContinuation: null,
    pendingReveal: null,
  };
}

export function applyPlayerMulligan(session: BattleSession, handIndexes: number[]) {
  const next = cloneBattleSession(session);
  if (next.phase !== "mulligan") {
    return next;
  }
  const selectedCards = [...handIndexes]
    .sort((left, right) => left - right)
    .map((index) => next.players.p1.hand[index])
    .filter((value): value is CardDefinition => Boolean(value));
  if (
    next.players.p1.topdeckAsHandCardId &&
    selectedCards.some((card) => card.id === next.players.p1.topdeckAsHandCardId)
  ) {
    next.players.p1.topdeckAsHandCardId = null;
  }
  const playerResult = mulliganCards(
    next.players.p1,
    selectedCards.map((card) => card.id),
  );
  pushLog(next, playerResult.discarded.length > 0 ? ("プレイヤーは" + playerResult.discarded.length + "枚をマリガンした。") : "プレイヤーはマリガンしなかった。");
  const cpuIds = chooseCpuMulliganCardIds(next.players.p2);
  const cpuResult = mulliganCards(next.players.p2, cpuIds);
  pushLog(next, cpuResult.discarded.length > 0 ? ("CPUは" + cpuResult.discarded.length + "枚をマリガンした。") : "CPUはマリガンしなかった。");
  next.phase = "control";
  next.actingPlayer = "p1";
  pushLog(next, "controlフェーズ開始。");
  return next;
}

export function applyPlayerControlChoice(session: BattleSession, handIndex: number | null) {
  const next = cloneBattleSession(session);
  if (next.phase !== "control") {
    return next;
  }
  const cardId = handIndex === null ? null : next.players.p1.hand[handIndex]?.id ?? null;
  if (cardId && next.players.p1.topdeckAsHandCardId === cardId) {
    next.players.p1.topdeckAsHandCardId = null;
  }
  applyControlChoice(next, "p1", cardId);
  if (next.pendingTriggerChoice) {
    return next;
  }
  const cpuChoice = chooseCpuControlCard(next, "p2");
  applyControlChoice(next, "p2", cpuChoice);
  next.phase = "battle_select";
  next.actingPlayer = next.battleStartingPlayer;
  pushLog(next, "battleフェーズ開始。");
  if (next.actingPlayer === "p2") {
    advanceCpuBattleLoop(next);
  }
  continueIfDrawnBattle(next);
  return next;
}

export function applyPlayerBattleAction(session: BattleSession, actionType: BattleActionType, handIndexes: number[]) {
  const next = cloneBattleSession(session);
  if (next.phase !== "battle_select" || next.actingPlayer !== "p1") {
    return next;
  }
  const selectedCards = [...handIndexes]
    .sort((left, right) => left - right)
    .map((index) => next.players.p1.hand[index])
    .filter((value): value is CardDefinition => Boolean(value));
  if (
    next.players.p1.topdeckAsHandCardId &&
    selectedCards.some((card) => card.id === next.players.p1.topdeckAsHandCardId)
  ) {
    next.players.p1.topdeckAsHandCardId = null;
  }
  applyBattleAction(
    next,
    "p1",
    actionType,
    selectedCards.map((card) => card.id),
  );
  const nextActor = nextBattleActor(next, "p1");
  if (applySetTriggeredBlessing(next, "p2", "p1", nextActor)) {
    return next;
  }
  if (nextActor === null) {
    resolveBattleV2(next);
    continueIfDrawnBattle(next);
    return next;
  }
  next.actingPlayer = nextActor;
  if (next.actingPlayer === "p2") {
    advanceCpuBattleLoop(next);
  }
  continueIfDrawnBattle(next);
  return next;
}

export function applyPlayerTriggerChoice(session: BattleSession, useTrigger: boolean, choiceId: string | null = null) {
  const next = cloneBattleSession(session);
  const pending = next.pendingTriggerChoice;
  if (next.phase !== "trigger_prompt" || !pending || pending.playerId !== "p1") {
    return next;
  }

  const blessing = next.players.p1.blessingZone;
  const selectedChoice = pending.choices?.find((choice) => choice.id === choiceId);
  if (pending.mode === "acknowledge") {
    useTrigger = false;
  }
  if (useTrigger && blessing) {
    if (pending.blessingCardId === "blessing_insight" && selectedChoice?.payload?.kind === "set_card") {
      const target = next.players[selectedChoice.payload.playerId].setCards[selectedChoice.payload.setIndex ?? -1];
      if (target) {
        target.revealed = true;
        next.players.p1.blessingFaceUp = false;
        pushEffectLog(next, "p1", blessing, pending.promptText);
      }
    } else if (pending.blessingCardId === "blessing_range") {
      next.players.p1.activeTurnModifiers.push({
        sourceId: blessing.id,
        attack: 0,
        block: 0,
        speed: 0,
        opponentAttack: 0,
        opponentBlock: 0,
        opponentSpeed: -2,
      });
      next.players.p1.blessingFaceUp = false;
      pushEffectLog(next, "p1", blessing, pending.promptText);
    }
  }

  if (useTrigger && pending.blessingCardId === "control_hand_echo" && selectedChoice?.payload?.kind === "discard_card") {
    const targetPlayer = next.players[selectedChoice.payload.playerId];
    const discardIndex = selectedChoice.payload.discardIndex ?? -1;
    const [returned] = discardIndex >= 0 ? targetPlayer.discardPile.splice(discardIndex, 1) : [undefined];
    if (returned) {
      targetPlayer.hand.push(returned);
      const sourceCard = next.players.p1.currentControlCard;
      if (sourceCard) {
        pushEffectLog(next, "p1", sourceCard, "相手の捨て札から" + (returned.name || returned.id) + "を手札に戻した。");
      }
    }
  }

  if (useTrigger && pending.blessingCardId === "control_all_in_focus" && selectedChoice?.payload?.kind === "hand_card") {
    const targetPlayer = next.players[selectedChoice.payload.playerId];
    const handIndex = selectedChoice.payload.handIndex ?? -1;
    const targetCard = handIndex >= 0 ? targetPlayer.hand[handIndex] : undefined;
    const sourceCard = next.players.p1.currentControlCard;
    if (targetCard && sourceCard) {
      targetCard.attack += 2;
      targetPlayer.queuedNextTurnDrawDelta -= 1;
      pushEffectLog(next, "p1", sourceCard, (targetCard.name || targetCard.id) + "の攻撃を+2し、次のターンのドロー-1。");
    }
  }

  const continuation = next.pendingTriggerContinuation;
  next.pendingTriggerChoice = null;
  next.pendingTriggerContinuation = null;
  next.phase = "battle_select";

  if (continuation?.resume === "control_after_player") {
    const cpuChoice = chooseCpuControlCard(next, "p2");
    applyControlChoice(next, "p2", cpuChoice);
    if (next.pendingTriggerChoice) {
      return next;
    }
    next.phase = "battle_select";
    next.actingPlayer = next.battleStartingPlayer;
    pushLog(next, "battleフェーズ開始。");
    if (next.actingPlayer === "p2") {
      advanceCpuBattleLoop(next);
    }
    continueIfDrawnBattle(next);
    return next;
  }

  if (!continuation || continuation.nextActor === null) {
    resolveBattleV2(next);
    return next;
  }

  next.actingPlayer = continuation.nextActor;
  if (next.actingPlayer === "p2") {
    advanceCpuBattleLoop(next);
  }
  continueIfDrawnBattle(next);
  return next;
}

export function advanceBattleReveal(session: BattleSession) {
  const next = cloneBattleSession(session);
  advanceRevealStep(next);
  continueIfDrawnBattle(next);
  return next;
}

export function applyPlayerBlessingChoice(session: BattleSession, useBlessing: boolean) {
  const next = cloneBattleSession(session);
  const pending = next.pendingBlessingChoice;
  if (next.phase !== "blessing_prompt" || !pending || !next.finalLines) {
    return next;
  }

  let lines = next.finalLines;
  if (useBlessing && next.players.p1.blessingZone) {
    lines = copyLines(pending.previewLines);
    next.players.p1.blessingFaceUp = false;
    pushEffectLog(next, "p1", next.players.p1.blessingZone, pending.promptText);
  }

  next.pendingBlessingChoice = null;

  const cpuResult = applyOptionalBlessingChoice(
    next,
    "p2",
    lines,
    countBattleCards(next.players.p2.setCards),
    countBattleCards(next.players.p1.setCards),
  );

  finalizeBattleResolution(next, cpuResult.lines, next.revealSteps);
  continueIfDrawnBattle(next);
  return next;
}

export function applyDebugAddCardToHand(session: BattleSession, drawPileIndex: number, playerId: PlayerId = "p1") {
  const next = cloneBattleSession(session);
  const card = next.players[playerId].drawPile[drawPileIndex];
  if (!card) {
    return next;
  }
  next.players[playerId].drawPile.splice(drawPileIndex, 1);
  next.players[playerId].hand.push(card);
  pushLog(next, "[Debug] " + playerLabel(playerId) + " adds " + (card.name || card.id) + " to hand");
  return next;
}

function resetBattleDebugFlow(session: BattleSession) {
  session.winner = null;
  session.endReason = null;
  session.finalLines = null;
  session.revealSteps = [];
  session.pendingBlessingChoice = null;
  session.pendingTriggerChoice = null;
  session.pendingTriggerContinuation = null;
  session.pendingReveal = null;
  if (session.phase !== "mulligan" && session.phase !== "control" && session.phase !== "battle_select") {
    session.phase = "battle_select";
    session.actingPlayer = "p1";
  }
}

function clearSetZoneForDebug(player: BattlePlayerState) {
  player.setCards = [];
  player.battlePassed = false;
}

function clearControlZoneForDebug(player: BattlePlayerState) {
  if (player.currentControlCard) {
    player.discardPile.push(player.currentControlCard);
    player.currentControlCard = null;
  }
}

function isBattlePlacementPhase(phase: BattleSession["phase"]) {
  return phase === "battle_select" || phase === "reveal" || phase === "blessing_prompt" || phase === "result";
}

export function applyDebugPlaceCard(
  session: BattleSession,
  playerId: PlayerId,
  zone: DebugBattleZone,
  cardId: string,
) {
  const next = cloneBattleSession(session);
  const player = next.players[playerId];
  const card = getBattleCard(cardId);

  resetBattleDebugFlow(next);

  if (zone === "set") {
    if (!isBattlePlacementPhase(next.phase)) {
      pushLog(next, `[Debug] ${playerLabel(playerId)} set zone はこのフェーズでは編集できない`);
      return next;
    }
    player.setCards.push({ card, revealed: false });
    player.battlePassed = false;
    pushLog(next, `[Debug] ${playerLabel(playerId)} set zone + ${card.name || card.id}`);
    return next;
  }

  if (zone === "hand") {
    player.hand.push(card);
    pushLog(next, `[Debug] ${playerLabel(playerId)} hand + ${card.name || card.id}`);
    return next;
  }

  if (zone === "draw_pile") {
    player.drawPile.unshift(card);
    pushLog(next, `[Debug] ${playerLabel(playerId)} draw pile + ${card.name || card.id}`);
    return next;
  }

  if (zone === "discard") {
    player.discardPile.push(card);
    pushLog(next, `[Debug] ${playerLabel(playerId)} discard + ${card.name || card.id}`);
    return next;
  }

  if (zone === "control") {
    if (player.currentControlCard) {
      player.discardPile.push(player.currentControlCard);
    }
    player.currentControlCard = card;
    pushLog(next, `[Debug] ${playerLabel(playerId)} control zone = ${card.name || card.id}`);
    return next;
  }

  if (player.blessingZone) {
    player.discardPile.push(player.blessingZone);
  }
  player.blessingZone = card;
  player.blessingFaceUp = true;
  player.blessingLockedThisTurn = false;
  pushLog(next, `[Debug] ${playerLabel(playerId)} blessing zone = ${card.name || card.id}`);
  return next;
}

export function applyDebugClearZone(session: BattleSession, playerId: PlayerId, zone: DebugBattleZone) {
  const next = cloneBattleSession(session);
  const player = next.players[playerId];

  resetBattleDebugFlow(next);

  if (zone === "set") {
    if (player.setCards.length > 0) {
      player.discardPile.push(...player.setCards.map((item) => item.card));
      player.setCards = [];
      pushLog(next, `[Debug] ${playerLabel(playerId)} set zone cleared`);
    }
    return next;
  }

  if (zone === "hand") {
    if (player.hand.length > 0) {
      player.discardPile.push(...player.hand);
      player.hand = [];
      pushLog(next, `[Debug] ${playerLabel(playerId)} hand cleared`);
    }
    return next;
  }

  if (zone === "draw_pile") {
    if (player.drawPile.length > 0) {
      player.drawPile = [];
      pushLog(next, `[Debug] ${playerLabel(playerId)} draw pile cleared`);
    }
    return next;
  }

  if (zone === "discard") {
    if (player.discardPile.length > 0) {
      player.discardPile = [];
      pushLog(next, `[Debug] ${playerLabel(playerId)} discard cleared`);
    }
    return next;
  }

  if (zone === "control") {
    if (player.currentControlCard) {
      player.discardPile.push(player.currentControlCard);
      player.currentControlCard = null;
      pushLog(next, `[Debug] ${playerLabel(playerId)} control zone cleared`);
    }
    return next;
  }

  if (player.blessingZone) {
    player.discardPile.push(player.blessingZone);
    player.blessingZone = null;
    player.blessingFaceUp = true;
    pushLog(next, `[Debug] ${playerLabel(playerId)} blessing zone cleared`);
  }
  return next;
}

export function applyDebugSetPhase(session: BattleSession, phase: BattleSession["phase"]) {
  const next = cloneBattleSession(session);
  resetBattleDebugFlow(next);
  if (!isBattlePlacementPhase(phase)) {
    for (const playerId of ["p1", "p2"] as PlayerId[]) {
      clearSetZoneForDebug(next.players[playerId]);
    }
  }
  if (phase === "mulligan") {
    for (const playerId of ["p1", "p2"] as PlayerId[]) {
      clearControlZoneForDebug(next.players[playerId]);
    }
  }
  next.phase = phase;
  next.actingPlayer = "p1";
  pushLog(next, `[Debug] phase -> ${phase}`);
  return next;
}

export function applyDebugStartReveal(session: BattleSession) {
  const next = cloneBattleSession(session);
  resetBattleDebugFlow(next);
  next.players.p1.battlePassed = true;
  next.players.p2.battlePassed = true;
  resolveBattleV2(next);
  return next;
}
