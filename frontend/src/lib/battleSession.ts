import { createSeededRandom } from "./random";
import type { CardDefinition, CardEffect } from "../types/cards";
import type {
  ActiveTurnModifier,
  BattleActionType,
  BattleFinalLine,
  BattlePlayerState,
  BattleRevealStep,
  BattleSession,
  BattleSetCard,
  DraftDeckState,
  DraftSession,
  PlayerId,
} from "../types/prototype";

const HAND_LIMIT = 6;
const TURN_DRAW_LIMIT = 4;

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

function drawAtTurnStart(player: BattlePlayerState, turn: number) {
  const drawBonus = player.queuedNextTurnDrawDelta;
  player.queuedNextTurnDrawDelta = 0;
  const base = turn === 1 ? 0 : TURN_DRAW_LIMIT;
  const drawTarget = Math.max(0, base + drawBonus);
  const capacity = Math.max(0, HAND_LIMIT - player.hand.length);
  return drawCards(player, Math.min(drawTarget, capacity));
}

function buildBattlePlayerState(deck: DraftDeckState, seed: number): BattlePlayerState {
  const drawPile = shuffleCards(flattenDraftDeck(deck), seed);
  const hand = drawPile.splice(0, 4);
  return {
    drawPile,
    hand,
    discardPile: [],
    usedCards: [],
    currentControlCard: null,
    blessingZone: null,
    blessingFaceUp: true,
    blessingLockedThisTurn: false,
    queuedNextTurnDrawDelta: 0,
    activeTurnModifiers: [],
    setCards: [],
    battlePassed: false,
  };
}

function cloneSetCard(item: BattleSetCard): BattleSetCard {
  return { card: cloneCard(item.card), revealed: item.revealed };
}

function clonePlayerState(player: BattlePlayerState): BattlePlayerState {
  return {
    drawPile: player.drawPile.map(cloneCard),
    hand: player.hand.map(cloneCard),
    discardPile: player.discardPile.map(cloneCard),
    usedCards: player.usedCards.map(cloneCard),
    currentControlCard: player.currentControlCard ? cloneCard(player.currentControlCard) : null,
    blessingZone: player.blessingZone ? cloneCard(player.blessingZone) : null,
    blessingFaceUp: player.blessingFaceUp,
    blessingLockedThisTurn: player.blessingLockedThisTurn,
    queuedNextTurnDrawDelta: player.queuedNextTurnDrawDelta,
    activeTurnModifiers: player.activeTurnModifiers.map((modifier) => ({ ...modifier })),
    setCards: player.setCards.map(cloneSetCard),
    battlePassed: player.battlePassed,
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
  };
}

function pushLog(session: BattleSession, text: string) {
  session.logs.push({ id: `battle-${session.logs.length + 1}`, text });
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
  if (kind === "modify_opponent_attack") modifier.opponentAttack += value;
  if (kind === "modify_opponent_block") modifier.opponentBlock += value;
  if (kind === "modify_opponent_speed") modifier.opponentSpeed += value;
  if (effect.effect_type === "modify_total_stat") {
    if (effect.target === "self_total" && effect.stat === "attack") modifier.attack += value;
    if (effect.target === "self_total" && effect.stat === "block") modifier.block += value;
    if (effect.target === "self_total" && effect.stat === "speed") modifier.speed += value;
    if (effect.target === "opponent_total" && effect.stat === "attack") modifier.opponentAttack += value;
    if (effect.target === "opponent_total" && effect.stat === "block") modifier.opponentBlock += value;
    if (effect.target === "opponent_total" && effect.stat === "speed") modifier.opponentSpeed += value;
  }
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
    pushLog(session, `${playerLabel(playerId)}は${drawn.length}枚引いた。`);
    return;
  }

  if (effect.effect_type === "modify_rule_value" && effect.stat === "draw_per_turn") {
    player.queuedNextTurnDrawDelta += effect.value ?? 0;
    return;
  }

  if (effect.effect_type === "reveal_cards") {
    if (effect.target === "opponent_hand" && opponent.hand.length > 0) {
      const shown = opponent.hand[0];
      pushLog(session, `${playerLabel(playerId)}は相手の手札を見た: ${shown.name || shown.id}`);
    } else if (effect.target === "opponent_deck" && opponent.drawPile.length > 0) {
      const shown = opponent.drawPile[0];
      pushLog(session, `${playerLabel(playerId)}は相手の山札トップを見た: ${shown.name || shown.id}`);
    } else if (effect.target === "self_deck" && player.drawPile.length > 0) {
      const shown = player.drawPile[0];
      pushLog(session, `${playerLabel(playerId)}は自分の山札トップを見た: ${shown.name || shown.id}`);
    }
  }
}

function applyControlCustom(session: BattleSession, playerId: PlayerId, card: CardDefinition) {
  const player = session.players[playerId];
  const opponent = session.players[otherPlayer(playerId)];

  switch (card.id) {
    case "control_blessing_flip":
      if (opponent.blessingZone && opponent.blessingFaceUp) {
        opponent.blessingFaceUp = false;
        pushLog(session, `${playerLabel(playerId)}は相手の加護を裏向きにした。`);
      } else if (player.blessingZone && !player.blessingFaceUp) {
        player.blessingFaceUp = true;
        pushLog(session, `${playerLabel(playerId)}は自分の加護を表向きに戻した。`);
      }
      break;
    case "control_blessing_break":
      if (opponent.blessingZone) {
        opponent.discardPile.push(opponent.blessingZone);
        opponent.blessingZone = null;
        opponent.blessingFaceUp = true;
        pushLog(session, `${playerLabel(playerId)}は相手の加護を捨てさせた。`);
      }
      break;
    case "control_blessing_lock":
      opponent.blessingLockedThisTurn = true;
      pushLog(session, `${playerLabel(playerId)}は相手の加護をこのターン封じた。`);
      break;
    case "control_defile":
      if (opponent.blessingZone && opponent.blessingFaceUp) {
        opponent.blessingFaceUp = false;
        pushLog(session, `${playerLabel(playerId)}は相手の加護を穢した。`);
      }
      break;
    case "control_redraw_hand": {
      const redrawCount = player.hand.length;
      player.discardPile.push(...player.hand);
      player.hand = [];
      drawCards(player, redrawCount);
      pushLog(session, `${playerLabel(playerId)}は手札を引き直した。`);
      break;
    }
    case "control_topdeck_hand": {
      const drawn = drawCards(player, 1);
      if (drawn.length > 0) {
        pushLog(session, `${playerLabel(playerId)}は山札トップを手札に加えた。`);
      }
      break;
    }
    case "control_discard_facedown_blessing":
      if (player.blessingZone && !player.blessingFaceUp) {
        player.discardPile.push(player.blessingZone);
        player.blessingZone = null;
        player.blessingFaceUp = true;
        pushLog(session, `${playerLabel(playerId)}は裏向きの加護を捨てた。`);
      }
      break;
    case "control_hand_echo":
      if (opponent.hand.length > 0) {
        const discarded = opponent.hand.shift()!;
        opponent.discardPile.push(discarded);
        pushLog(session, `${playerLabel(playerId)}は相手の手札に干渉した。`);
      }
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
    pushLog(session, `${playerLabel(playerId)}はcontrolを使わない。`);
    return;
  }
  const player = session.players[playerId];
  const card = removeCardFromHand(player, cardId);
  if (!card) {
    pushLog(session, `${playerLabel(playerId)}はcontrolを使わない。`);
    return;
  }

  if (card.card_type === "blessing") {
    if (!player.blessingZone) {
      player.blessingZone = card;
      player.blessingFaceUp = true;
      pushLog(session, `${playerLabel(playerId)}は加護を置いた。`);
      return;
    }
    player.hand.push(card);
    pushLog(session, `${playerLabel(playerId)}は加護を追加できなかった。`);
    return;
  }

  player.currentControlCard = card;
  player.usedCards.push(card);
  pushLog(session, `${playerLabel(playerId)}は${card.name || card.id}を使った。`);
  for (const effect of card.effects) {
    applyImmediateControlEffect(session, playerId, card, effect);
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
    pushLog(session, `${playerLabel(playerId)}はパスした。`);
    return;
  }

  const maxCards = actionType === "set_pass" ? 1 : Math.min(2, legalSlots);
  const chosen: CardDefinition[] = [];
  for (const cardId of requestedIds.slice(0, maxCards)) {
    const card = removeCardFromHand(player, cardId);
    if (card && (card.card_type === "battle" || card.card_type === "control")) {
      chosen.push(card);
    }
  }
  if (chosen.length === 0) {
    player.battlePassed = true;
    pushLog(session, `${playerLabel(playerId)}はパスした。`);
    return;
  }

  player.setCards.push(...chosen.map((card) => ({ card, revealed: false })));
  pushLog(session, `${playerLabel(playerId)}は${chosen.length}枚伏せた。`);
  if (actionType === "set_pass") {
    player.battlePassed = true;
    pushLog(session, `${playerLabel(playerId)}は伏せてパスした。`);
  }
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
    return { winner: first, endReason: `${first}_attack_success` };
  }
  if (lines[second].attack > 0 && lines[second].attack > lines[first].block) {
    return { winner: second, endReason: `${second}_attack_success` };
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
      pushLog(session, `${playerLabel(playerId)}の加護が発動した。`);
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
    pushLog(session, `${playerLabel(outcome.winner)}の勝ち。`);
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

function endTurnAndAdvance(session: BattleSession) {
  for (const playerId of ["p1", "p2"] as PlayerId[]) {
    const player = session.players[playerId];
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
  }
  session.turn += 1;
  session.battleStartingPlayer = otherPlayer(session.battleStartingPlayer);
  session.actingPlayer = "p1";
  session.phase = "control";
  const p1Drawn = drawAtTurnStart(session.players.p1, session.turn);
  const p2Drawn = drawAtTurnStart(session.players.p2, session.turn);
  pushLog(session, `ターン${session.turn}開始。プレイヤーは${p1Drawn.length}枚、CPUは${p2Drawn.length}枚引いた。`);
}

function advanceCpuBattleLoop(session: BattleSession) {
  while (session.phase === "battle_select" && session.actingPlayer === "p2") {
    const choice = chooseCpuBattleAction(session, "p2");
    applyBattleAction(session, "p2", choice.actionType, choice.cardIds);
    const nextActor = nextBattleActor(session, "p2");
    if (nextActor === null) {
      resolveBattle(session);
      return;
    }
    session.actingPlayer = nextActor;
    if (nextActor === "p2" && session.players.p2.battlePassed) {
      resolveBattle(session);
      return;
    }
  }
}

export function createBattleSessionFromDraft(session: DraftSession): BattleSession {
  const p1 = buildBattlePlayerState(session.decks.p1, session.seed + 101);
  const p2 = buildBattlePlayerState(session.decks.p2, session.seed + 202);
  return {
    seed: session.seed,
    turn: 1,
    phase: "control",
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
      { id: "battle-2", text: `先手は${playerLabel(session.firstPlayer)}。` },
      { id: "battle-3", text: `プレイヤーは初期手札を${p1.hand.length}枚引いた。` },
      { id: "battle-4", text: `CPUは初期手札を${p2.hand.length}枚引いた。` },
      { id: "battle-5", text: "1ターン目は通常ドローなし。controlフェーズから始める。" },
    ],
  };
}

export function applyPlayerControlChoice(session: BattleSession, cardId: string | null) {
  const next = cloneBattleSession(session);
  if (next.phase !== "control") {
    return next;
  }
  applyControlChoice(next, "p1", cardId);
  const cpuChoice = chooseCpuControlCard(next, "p2");
  applyControlChoice(next, "p2", cpuChoice);
  next.phase = "battle_select";
  next.actingPlayer = next.battleStartingPlayer;
  pushLog(next, "battleフェーズ開始。");
  if (next.actingPlayer === "p2") {
    advanceCpuBattleLoop(next);
  }
  return next;
}

export function applyPlayerBattleAction(session: BattleSession, actionType: BattleActionType, cardIds: string[]) {
  const next = cloneBattleSession(session);
  if (next.phase !== "battle_select" || next.actingPlayer !== "p1") {
    return next;
  }
  applyBattleAction(next, "p1", actionType, cardIds);
  const nextActor = nextBattleActor(next, "p1");
  if (nextActor === null) {
    resolveBattle(next);
    return next;
  }
  next.actingPlayer = nextActor;
  if (next.actingPlayer === "p2") {
    advanceCpuBattleLoop(next);
  }
  return next;
}
