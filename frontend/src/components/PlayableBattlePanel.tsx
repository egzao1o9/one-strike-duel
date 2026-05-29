import { useEffect, useMemo, useState } from "react";
import { getAllCards } from "../lib/cards";
import type { CardDefinition } from "../types/cards";
import type {
  BattleActionType,
  BattlePhase,
  BattleSession,
  BattleSetCard,
  DebugBattlePreset,
  DebugBattleZone,
  PlayerId,
} from "../types/prototype";
import { CardFull } from "./CardFull";
import { CardMini } from "./CardMini";
import { CardStrip } from "./CardStrip";

interface PlayableBattlePanelProps {
  battleSession: BattleSession;
  onSelectCard: (card: CardDefinition) => void;
  onChooseMulligan: (handIndexes: number[]) => void;
  onChooseControl: (handIndex: number | null) => void;
  onBattleAction: (actionType: BattleActionType, handIndexes: number[]) => void;
  onResolveTriggerChoice: (useTrigger: boolean, choiceId?: string | null) => void;
  onAdvanceReveal: () => void;
  onResolveBlessingChoice: (useBlessing: boolean) => void;
  onDebugAddCardToHand: (drawPileIndex: number) => void;
  onDebugSetup: (preset: DebugBattlePreset) => void;
  onDebugPlaceCard: (playerId: PlayerId, zone: DebugBattleZone, cardId: string) => void;
  onDebugClearZone: (playerId: PlayerId, zone: DebugBattleZone) => void;
  onDebugSetPhase: (phase: BattlePhase) => void;
  onDebugStartReveal: () => void;
}

const allCards = getAllCards().sort((left, right) => left.name.localeCompare(right.name, "ja"));

function labelForPlayer(playerId: PlayerId) {
  return playerId === "p1" ? "Player" : "CPU";
}

function isBattlePlacementPhase(phase: BattlePhase) {
  return phase === "battle_select" || phase === "reveal" || phase === "blessing_prompt" || phase === "result";
}

function selectionCap(session: BattleSession) {
  const own = session.players.p1.setCards.length;
  const opp = session.players.p2.setCards.length;
  if (own > opp) return 0;
  return Math.min(2, Math.max(0, opp + 1 - own));
}

function topdeckPreview(session: BattleSession, playerId: PlayerId) {
  const player = session.players[playerId];
  if (!player.topdeckAsHandCardId) return null;
  const top = player.drawPile[0];
  return top && top.id === player.topdeckAsHandCardId ? top : null;
}

function BattleSetRow({
  cards,
  onSelectCard,
}: {
  cards: BattleSetCard[];
  onSelectCard: (card: CardDefinition) => void;
}) {
  if (cards.length === 0) {
    return <div className="battle-set-row battle-set-row--empty" />;
  }
  return (
    <div className="battle-set-row">
      {cards.map((item, index) =>
        item.revealed ? (
          <div key={`set-${item.card.id}-${index}`} className="battle-zone-mini">
            <CardMini card={item.card} onClick={onSelectCard} />
          </div>
        ) : (
          <div key={`set-${item.card.id}-${index}`} className="battle-zone-mini battle-zone-mini--hidden">
            <div className="battle-zone-mini__hidden-mark">?</div>
          </div>
        ),
      )}
    </div>
  );
}

function ZoneMiniCard({
  card,
  label,
  onSelectCard,
}: {
  card: CardDefinition | null;
  label: string;
  onSelectCard: (card: CardDefinition) => void;
}) {
  if (!card) {
    return (
      <div className="battle-zone-slot">
        <span className="battle-zone-slot__label">{label}</span>
      </div>
    );
  }
  return (
    <div className="battle-zone-slot battle-zone-slot--filled">
      <CardMini card={card} onClick={onSelectCard} />
    </div>
  );
}

function PileGroup({
  side,
  drawPileCount,
  discardCount,
  topdeckCard,
  onPreviewTopdeck,
  onOpenDiscard,
}: {
  side: "player" | "cpu";
  drawPileCount: number;
  discardCount: number;
  topdeckCard: CardDefinition | null;
  onPreviewTopdeck: (card: CardDefinition) => void;
  onOpenDiscard: () => void;
}) {
  return (
    <div className={`battle-pile-group battle-pile-group--${side}`}>
      <div className="battle-pile-stack">
        {topdeckCard ? (
          <div className="battle-pile-preview">
            <CardMini card={topdeckCard} onClick={onPreviewTopdeck} className="card-mini--topdeck-preview" />
          </div>
        ) : null}
        <div className="battle-pile battle-pile--deck" title={`Deck ${drawPileCount}`}>
          <span className="battle-pile__label">Deck</span>
          <strong className="battle-pile__count">{drawPileCount}</strong>
        </div>
      </div>
      <button type="button" className="battle-pile battle-pile--discard" onClick={onOpenDiscard} title={`Discard ${discardCount}`}>
        <span className="battle-pile__label">Discard</span>
        <strong className="battle-pile__count">{discardCount}</strong>
      </button>
    </div>
  );
}

export function PlayableBattlePanel({
  battleSession,
  onSelectCard,
  onChooseMulligan,
  onChooseControl,
  onBattleAction,
  onResolveTriggerChoice,
  onAdvanceReveal,
  onResolveBlessingChoice,
  onDebugAddCardToHand,
  onDebugSetup,
  onDebugPlaceCard,
  onDebugClearZone,
  onDebugSetPhase,
  onDebugStartReveal,
}: PlayableBattlePanelProps) {
  const [selectedHandIndexes, setSelectedHandIndexes] = useState<number[]>([]);
  const [selectedControlIndex, setSelectedControlIndex] = useState<number | null>(null);
  const [showLog, setShowLog] = useState(false);
  const [showDiscardFor, setShowDiscardFor] = useState<PlayerId | null>(null);
  const [showDebugDeck, setShowDebugDeck] = useState(false);
  const [showDebugBoard, setShowDebugBoard] = useState(false);
  const [debugBoardTarget, setDebugBoardTarget] = useState<{ playerId: PlayerId; zone: DebugBattleZone }>({
    playerId: "p1",
    zone: "set",
  });

  const p1 = battleSession.players.p1;
  const p2 = battleSession.players.p2;
  const maxSelect = selectionCap(battleSession);
  const debugAllowsSetPlacement = isBattlePlacementPhase(battleSession.phase);
  const p1TopdeckCard = topdeckPreview(battleSession, "p1");
  const p2TopdeckCard = topdeckPreview(battleSession, "p2");
  const p1TopdeckHighlightIndex =
    p1.topdeckAsHandCardId === null ? -1 : p1.hand.map((card) => card.id).lastIndexOf(p1.topdeckAsHandCardId);

  const discardViewerPlayer = showDiscardFor ? battleSession.players[showDiscardFor] : null;
  const debugBoardCards = useMemo(() => {
    switch (debugBoardTarget.zone) {
      case "control":
        return allCards.filter((card) => card.card_type === "control");
      case "blessing":
        return allCards.filter((card) => card.card_type === "blessing");
      default:
        return allCards;
    }
  }, [debugBoardTarget.zone]);

  useEffect(() => {
    setSelectedHandIndexes([]);
    setSelectedControlIndex(null);
  }, [battleSession.phase, battleSession.turn, battleSession.logs.length]);

  const selectedBattleCards = selectedHandIndexes
    .map((index) => p1.hand[index])
    .filter((card): card is CardDefinition => Boolean(card));

  function toggleHandIndex(index: number) {
    const card = p1.hand[index];
    if (!card) return;

    if (battleSession.phase === "mulligan") {
      setSelectedHandIndexes((current) =>
        current.includes(index) ? current.filter((value) => value !== index) : [...current, index].sort((a, b) => a - b),
      );
      return;
    }

    if (battleSession.phase === "control" && battleSession.actingPlayer === "p1") {
      if (card.card_type !== "control" && card.card_type !== "blessing") return;
      setSelectedControlIndex((current) => (current === index ? null : index));
      return;
    }

    if (battleSession.phase !== "battle_select" || battleSession.actingPlayer !== "p1" || maxSelect === 0) return;

    setSelectedHandIndexes((current) => {
      if (current.includes(index)) return current.filter((value) => value !== index);
      if (current.length >= maxSelect) return current;
      return [...current, index];
    });
  }

  function renderPlayerHandCard(card: CardDefinition, index: number) {
    const selectedOrder = selectedHandIndexes.indexOf(index);
    const isControlSelected = selectedControlIndex === index;
    const classes = [
      "battle-hand-card",
      selectedOrder >= 0 || isControlSelected ? "battle-hand-card--selected" : "",
      index === p1TopdeckHighlightIndex ? "battle-hand-card--topdeck-preview" : "",
    ]
      .filter(Boolean)
      .join(" ");

    return (
      <div key={`hand-${card.id}-${index}`} className={classes}>
        {selectedOrder >= 0 ? <span className="battle-hand-order-badge">{selectedOrder + 1}</span> : null}
        <CardMini
          card={card}
          onClick={() => toggleHandIndex(index)}
          className={index === p1TopdeckHighlightIndex ? "card-mini--topdeck-preview" : ""}
        />
      </div>
    );
  }

  return (
    <section className="preview-panel">
      <div className="section-heading">
        <div>
          <p className="eyebrow">Battle</p>
          <h2>Battle Screen</h2>
        </div>
        <div className="battle-toolbar">
          <p className="section-note">
            Turn {battleSession.turn} / {battleSession.phase} / Acting: {labelForPlayer(battleSession.actingPlayer)}
          </p>
          <button type="button" className="battle-log-button" onClick={() => setShowLog(true)} aria-label="Open battle log">
            Log
          </button>
          <button type="button" className="battle-log-button" onClick={() => setShowDebugDeck(true)} aria-label="Open debug deck">
            Debug Deck
          </button>
          <button type="button" className="battle-log-button" onClick={() => setShowDebugBoard(true)} aria-label="Open debug board">
            Debug Board
          </button>
        </div>
      </div>

      <div className="battle-surface">
        <section className="battle-hand-zone battle-hand-zone--opponent">
          <div className="battle-hand-strip">{p2.hand.map((_, index) => <div key={`cpu-hand-${index}`} className="battle-hand-placeholder" />)}</div>
        </section>

        <div className="battle-zone-grid battle-zone-grid--opponent">
          <PileGroup
            side="cpu"
            drawPileCount={p2.drawPile.length}
            discardCount={p2.discardPile.length}
            topdeckCard={p2TopdeckCard}
            onPreviewTopdeck={onSelectCard}
            onOpenDiscard={() => setShowDiscardFor("p2")}
          />
          <div className="battle-zone-cluster">
            <ZoneMiniCard card={p2.blessingZone} label="Blessing" onSelectCard={onSelectCard} />
            <ZoneMiniCard card={p2.currentControlCard} label="Control" onSelectCard={onSelectCard} />
          </div>
        </div>

        <div className="battle-center-column">
          <BattleSetRow cards={p2.setCards} onSelectCard={onSelectCard} />

          <div className="battle-center-info">
            {(battleSession.phase === "reveal" || battleSession.phase === "blessing_prompt" || battleSession.phase === "result") &&
            battleSession.finalLines ? (
              <div className="battle-scoreboard">
                <div className="battle-scoreboard__side">
                  <strong>CPU</strong>
                  <span>
                    A {battleSession.finalLines.p2.attack} / B {battleSession.finalLines.p2.block} / S {battleSession.finalLines.p2.speed}
                  </span>
                </div>
                <div className="battle-scoreboard__side">
                  <strong>Player</strong>
                  <span>
                    A {battleSession.finalLines.p1.attack} / B {battleSession.finalLines.p1.block} / S {battleSession.finalLines.p1.speed}
                  </span>
                </div>
              </div>
            ) : (
              <div className="battle-scoreboard battle-scoreboard--compact">
                <strong>Turn {battleSession.turn}</strong>
                <span>{battleSession.phase}</span>
              </div>
            )}

            {battleSession.phase === "reveal" ? (
              <button type="button" className="primary-button" onClick={onAdvanceReveal}>
                Reveal Next
              </button>
            ) : null}
          </div>

          <BattleSetRow cards={p1.setCards} onSelectCard={onSelectCard} />
        </div>

        <div className="battle-zone-grid battle-zone-grid--player">
          <div className="battle-zone-cluster">
            <ZoneMiniCard card={p1.currentControlCard} label="Control" onSelectCard={onSelectCard} />
            <ZoneMiniCard card={p1.blessingZone} label="Blessing" onSelectCard={onSelectCard} />
          </div>
          <PileGroup
            side="player"
            drawPileCount={p1.drawPile.length}
            discardCount={p1.discardPile.length}
            topdeckCard={p1TopdeckCard}
            onPreviewTopdeck={onSelectCard}
            onOpenDiscard={() => setShowDiscardFor("p1")}
          />
        </div>

        <section className="battle-hand-zone battle-hand-zone--player">
          <div className="battle-hand-strip">{p1.hand.map((card, index) => renderPlayerHandCard(card, index))}</div>
        </section>
      </div>

      {battleSession.phase === "mulligan" ? (
        <div className="battle-action-panel">
          <p className="battle-action-caption">Choose cards to mulligan.</p>
          <div className="battle-action-row">
            <button type="button" className="primary-button" onClick={() => onChooseMulligan(selectedHandIndexes)}>
              {selectedHandIndexes.length > 0 ? `Mulligan ${selectedHandIndexes.length}` : "Keep Hand"}
            </button>
          </div>
        </div>
      ) : null}

      {battleSession.phase === "control" && battleSession.actingPlayer === "p1" ? (
        <div className="battle-action-panel">
          <p className="battle-action-caption">Use one control or blessing card, or skip.</p>
          <div className="battle-action-row">
            <button type="button" className="primary-button" onClick={() => onChooseControl(selectedControlIndex)} disabled={selectedControlIndex === null}>
              Use Selected
            </button>
            <button type="button" className="secondary-button" onClick={() => onChooseControl(null)}>
              Skip
            </button>
          </div>
        </div>
      ) : null}

      {battleSession.phase === "battle_select" && battleSession.actingPlayer === "p1" ? (
        <div className="battle-action-panel">
          <p className="battle-action-caption">
            {maxSelect === 0 ? "No more cards can be set now. Pass only." : `You may choose up to ${maxSelect} card(s).`}
          </p>
          <div className="battle-action-row">
            <button type="button" className="primary-button" disabled={selectedBattleCards.length === 0 || maxSelect === 0} onClick={() => onBattleAction("set", selectedHandIndexes)}>
              set
            </button>
            <button
              type="button"
              className="secondary-button"
              disabled={selectedBattleCards.length === 0 || maxSelect === 0}
              onClick={() => onBattleAction("set_pass", selectedHandIndexes)}
            >
              set_pass
            </button>
            <button type="button" className="secondary-button" onClick={() => onBattleAction("pass", [])}>
              pass
            </button>
          </div>
        </div>
      ) : null}

      {battleSession.phase === "trigger_prompt" &&
      battleSession.pendingTriggerChoice &&
      battleSession.pendingTriggerChoice.mode !== "acknowledge" &&
      !(
        battleSession.pendingTriggerChoice.mode === "choose_option" &&
        battleSession.pendingTriggerChoice.choices?.length &&
        battleSession.pendingTriggerChoice.choices.every((choice) => Boolean(choice.card))
      ) ? (
        <div className="battle-action-panel">
          {battleSession.pendingTriggerChoice.blessingName ? (
            <p className="battle-action-caption">Effect: {battleSession.pendingTriggerChoice.blessingName}</p>
          ) : null}
          <p className="battle-action-caption">{battleSession.pendingTriggerChoice.promptText}</p>
          {battleSession.pendingTriggerChoice.mode === "choose_option" && battleSession.pendingTriggerChoice.choices ? (
            <div className="battle-action-row">
              {battleSession.pendingTriggerChoice.choices.map((choice) =>
                choice.card ? (
                  <div key={`trigger-choice-${choice.id}`} className="debug-card-picker-item">
                    <CardStrip card={choice.card} onClick={() => onResolveTriggerChoice(true, choice.id)} onPreview={onSelectCard} />
                  </div>
                ) : (
                  <button key={`trigger-choice-${choice.id}`} type="button" className="secondary-button" onClick={() => onResolveTriggerChoice(true, choice.id)}>
                    {choice.label}
                  </button>
                ),
              )}
            </div>
          ) : (
            <div className="battle-action-row">
              <button type="button" className="primary-button" onClick={() => onResolveTriggerChoice(true, null)}>
                Continue
              </button>
            </div>
          )}
        </div>
      ) : null}

      {battleSession.phase === "blessing_prompt" && battleSession.pendingBlessingChoice ? (
        <div className="battle-action-panel">
          <p className="battle-action-caption">Blessing: {battleSession.pendingBlessingChoice.blessingName}</p>
          <p className="battle-action-caption">{battleSession.pendingBlessingChoice.promptText}</p>
          <div className="battle-result-grid">
            <div className="battle-result-card">
              <strong>Current</strong>
              <span>
                A {battleSession.finalLines?.p1.attack ?? 0} / B {battleSession.finalLines?.p1.block ?? 0} / S {battleSession.finalLines?.p1.speed ?? 0}
              </span>
              <span>
                CPU A {battleSession.finalLines?.p2.attack ?? 0} / B {battleSession.finalLines?.p2.block ?? 0} / S {battleSession.finalLines?.p2.speed ?? 0}
              </span>
            </div>
            <div className="battle-result-card">
              <strong>After Use</strong>
              <span>
                A {battleSession.pendingBlessingChoice.previewLines.p1.attack} / B {battleSession.pendingBlessingChoice.previewLines.p1.block} / S {battleSession.pendingBlessingChoice.previewLines.p1.speed}
              </span>
              <span>
                CPU A {battleSession.pendingBlessingChoice.previewLines.p2.attack} / B {battleSession.pendingBlessingChoice.previewLines.p2.block} / S {battleSession.pendingBlessingChoice.previewLines.p2.speed}
              </span>
            </div>
          </div>
          <div className="battle-action-row">
            <button type="button" className="primary-button" onClick={() => onResolveBlessingChoice(true)}>
              Use
            </button>
            <button type="button" className="secondary-button" onClick={() => onResolveBlessingChoice(false)}>
              Skip
            </button>
          </div>
        </div>
      ) : null}

      {battleSession.phase === "result" && battleSession.finalLines ? (
        <div className="battle-result-panel">
          <p className="battle-result-headline">{battleSession.winner ? `${labelForPlayer(battleSession.winner)} wins` : "Draw"}</p>
          <div className="battle-result-grid">
            <div className="battle-result-card">
              <strong>Player</strong>
              <em>{battleSession.winner === "p1" ? "Win" : battleSession.winner === "p2" ? "Lose" : "Draw"}</em>
              <span>
                A {battleSession.finalLines.p1.attack} / B {battleSession.finalLines.p1.block} / S {battleSession.finalLines.p1.speed}
              </span>
            </div>
            <div className="battle-result-card">
              <strong>CPU</strong>
              <em>{battleSession.winner === "p2" ? "Win" : battleSession.winner === "p1" ? "Lose" : "Draw"}</em>
              <span>
                A {battleSession.finalLines.p2.attack} / B {battleSession.finalLines.p2.block} / S {battleSession.finalLines.p2.speed}
              </span>
            </div>
          </div>
        </div>
      ) : null}

      {battleSession.phase === "trigger_prompt" &&
      battleSession.pendingTriggerChoice?.mode === "choose_option" &&
      battleSession.pendingTriggerChoice.choices?.length &&
      battleSession.pendingTriggerChoice.choices.every((choice) => Boolean(choice.card)) ? (
        <div className="card-overlay-backdrop" role="presentation">
          <aside className="card-overlay battle-log-overlay debug-card-picker-overlay" role="dialog" aria-modal="true" aria-label="Choose card" onClick={(event) => event.stopPropagation()}>
            <div className="card-overlay__header">
              <p className="eyebrow">Choose</p>
            </div>
            <p className="battle-action-caption">{battleSession.pendingTriggerChoice.promptText}</p>
            <div className="debug-card-picker-list">
              {battleSession.pendingTriggerChoice.choices.map((choice) =>
                choice.card ? (
                  <div key={`choose-${choice.id}`} className="debug-card-picker-item">
                    <CardStrip card={choice.card} onClick={() => onResolveTriggerChoice(true, choice.id)} onPreview={onSelectCard} />
                  </div>
                ) : null,
              )}
            </div>
          </aside>
        </div>
      ) : null}

      {battleSession.phase === "trigger_prompt" &&
      battleSession.pendingTriggerChoice?.mode === "acknowledge" &&
      battleSession.pendingTriggerChoice.choices ? (
        <div className="card-overlay-backdrop" role="presentation">
          <aside className="card-overlay battle-log-overlay acknowledge-overlay" role="dialog" aria-modal="true" aria-label="Reveal cards" onClick={(event) => event.stopPropagation()}>
            <div className="card-overlay__header">
              <p className="eyebrow">Reveal</p>
              <button type="button" className="card-overlay__close" onClick={() => onResolveTriggerChoice(true, null)}>
                Close
              </button>
            </div>
            <p className="battle-action-caption">{battleSession.pendingTriggerChoice.promptText}</p>
            <div className="acknowledge-overlay__cards">
              {battleSession.pendingTriggerChoice.choices.map((choice) =>
                choice.card ? (
                  <div key={`ack-${choice.id}`} className="acknowledge-overlay__card">
                    <CardFull card={choice.card} />
                  </div>
                ) : null,
              )}
            </div>
            <div className="battle-action-row">
              <button type="button" className="primary-button" onClick={() => onResolveTriggerChoice(true, null)}>
                Continue
              </button>
            </div>
          </aside>
        </div>
      ) : null}

      {showLog ? (
        <div className="card-overlay-backdrop" onClick={() => setShowLog(false)} role="presentation">
          <aside className="card-overlay battle-log-overlay" role="dialog" aria-modal="true" aria-label="Battle log" onClick={(event) => event.stopPropagation()}>
            <div className="card-overlay__header">
              <p className="eyebrow">Battle Log</p>
              <button type="button" className="card-overlay__close" onClick={() => setShowLog(false)}>
                Close
              </button>
            </div>
            <ol className="compact-list compact-list--logs">
              {battleSession.logs.map((entry) => (
                <li key={entry.id}>{entry.text}</li>
              ))}
            </ol>
            {battleSession.effectLogs.length > 0 ? (
              <>
                <p className="eyebrow">Effect Log</p>
                <ol className="compact-list compact-list--logs">
                  {battleSession.effectLogs.map((entry) => (
                    <li key={entry.id}>
                      {labelForPlayer(entry.playerId)} / {entry.sourceCardName}: {entry.text}
                    </li>
                  ))}
                </ol>
              </>
            ) : null}
          </aside>
        </div>
      ) : null}

      {showDebugDeck ? (
        <div className="card-overlay-backdrop" onClick={() => setShowDebugDeck(false)} role="presentation">
          <aside className="card-overlay battle-log-overlay debug-card-picker-overlay" role="dialog" aria-modal="true" aria-label="Debug deck" onClick={(event) => event.stopPropagation()}>
            <div className="card-overlay__header">
              <p className="eyebrow">Debug Deck</p>
              <button type="button" className="card-overlay__close" onClick={() => setShowDebugDeck(false)}>
                Close
              </button>
            </div>
            <p className="battle-action-caption">Take any card from your deck into your hand.</p>
            <div className="debug-card-picker-list">
              {p1.drawPile.map((card, index) => (
                <div key={`debug-card-${card.id}-${index}`} className="debug-card-picker-item">
                  <CardStrip
                    card={card}
                    onClick={() => {
                      onDebugAddCardToHand(index);
                      setShowDebugDeck(false);
                    }}
                    onPreview={onSelectCard}
                  />
                </div>
              ))}
            </div>
          </aside>
        </div>
      ) : null}

      {showDebugBoard ? (
        <div className="card-overlay-backdrop" onClick={() => setShowDebugBoard(false)} role="presentation">
          <aside className="card-overlay battle-log-overlay debug-card-picker-overlay" role="dialog" aria-modal="true" aria-label="Debug board" onClick={(event) => event.stopPropagation()}>
            <div className="card-overlay__header">
              <p className="eyebrow">Debug Board</p>
              <button type="button" className="card-overlay__close" onClick={() => setShowDebugBoard(false)}>
                Close
              </button>
            </div>

            <p className="battle-action-caption">Select a target zone, then place or clear cards.</p>

            <div className="debug-target-grid">
              {([
                { playerId: "p1" as const, zone: "hand" as const, label: "P1 Hand" },
                { playerId: "p1" as const, zone: "set" as const, label: "P1 Set" },
                { playerId: "p1" as const, zone: "control" as const, label: "P1 Control" },
                { playerId: "p1" as const, zone: "blessing" as const, label: "P1 Blessing" },
                { playerId: "p1" as const, zone: "draw_pile" as const, label: "P1 Deck" },
                { playerId: "p1" as const, zone: "discard" as const, label: "P1 Discard" },
                { playerId: "p2" as const, zone: "hand" as const, label: "CPU Hand" },
                { playerId: "p2" as const, zone: "set" as const, label: "CPU Set" },
                { playerId: "p2" as const, zone: "control" as const, label: "CPU Control" },
                { playerId: "p2" as const, zone: "blessing" as const, label: "CPU Blessing" },
                { playerId: "p2" as const, zone: "draw_pile" as const, label: "CPU Deck" },
                { playerId: "p2" as const, zone: "discard" as const, label: "CPU Discard" },
              ]).map((target) => {
                const active = debugBoardTarget.playerId === target.playerId && debugBoardTarget.zone === target.zone;
                return (
                  <button
                    key={`${target.playerId}-${target.zone}`}
                    type="button"
                    className={active ? "primary-button debug-target-button" : "secondary-button debug-target-button"}
                    onClick={() => setDebugBoardTarget({ playerId: target.playerId, zone: target.zone })}
                    disabled={target.zone === "set" && !debugAllowsSetPlacement}
                  >
                    {target.label}
                  </button>
                );
              })}
            </div>

            <p className="battle-action-caption">Phase</p>
            <div className="battle-action-row battle-action-row--debug">
              {(["mulligan", "control", "battle_select"] as BattlePhase[]).map((phase) => (
                <button key={phase} type="button" className="secondary-button" onClick={() => onDebugSetPhase(phase)}>
                  {phase}
                </button>
              ))}
            </div>

            <p className="battle-action-caption">Simulation</p>
            <div className="battle-action-row battle-action-row--debug">
              <button type="button" className="secondary-button" onClick={() => onDebugStartReveal()}>
                Start Reveal
              </button>
              <button type="button" className="secondary-button" onClick={() => onDebugSetup("draw")}>
                Debug Draw
              </button>
              <button type="button" className="secondary-button" onClick={() => onDebugSetup("no_damage")}>
                Debug No Damage
              </button>
              <button type="button" className="secondary-button" onClick={() => onDebugSetup("p1_win")}>
                Debug P1 Win
              </button>
              <button type="button" className="secondary-button" onClick={() => onDebugSetup("p2_win")}>
                Debug P2 Win
              </button>
            </div>

            <div className="battle-action-row battle-action-row--debug">
              <button type="button" className="secondary-button" onClick={() => onDebugClearZone(debugBoardTarget.playerId, debugBoardTarget.zone)}>
                Clear Zone Cards
              </button>
            </div>

            <div className="debug-card-picker-list">
              <div className="debug-card-picker-item">
                <button
                  type="button"
                  className="debug-random-card"
                  onClick={() => {
                    if (debugBoardCards.length === 0) return;
                    const randomCard = debugBoardCards[Math.floor(Math.random() * debugBoardCards.length)];
                    if (randomCard) {
                      onDebugPlaceCard(debugBoardTarget.playerId, debugBoardTarget.zone, randomCard.id);
                    }
                  }}
                >
                  <span className="debug-random-card__marker" />
                  <span className="debug-random-card__label">Random</span>
                </button>
              </div>
              {debugBoardCards.map((card, index) => (
                <div key={`debug-board-card-${card.id}-${index}`} className="debug-card-picker-item">
                  <CardStrip card={card} onClick={() => onDebugPlaceCard(debugBoardTarget.playerId, debugBoardTarget.zone, card.id)} onPreview={onSelectCard} />
                </div>
              ))}
            </div>
          </aside>
        </div>
      ) : null}

      {showDiscardFor && discardViewerPlayer ? (
        <div className="card-overlay-backdrop" onClick={() => setShowDiscardFor(null)} role="presentation">
          <aside className="card-overlay battle-log-overlay debug-card-picker-overlay" role="dialog" aria-modal="true" aria-label="Discard list" onClick={(event) => event.stopPropagation()}>
            <div className="card-overlay__header">
              <p className="eyebrow">Discard</p>
              <button type="button" className="card-overlay__close" onClick={() => setShowDiscardFor(null)}>
                Close
              </button>
            </div>
            <p className="battle-action-caption">{labelForPlayer(showDiscardFor)} discard pile</p>
            <div className="debug-card-picker-list">
              {[...discardViewerPlayer.discardPile].reverse().map((card, index) => (
                <div key={`discard-${showDiscardFor}-${card.id}-${index}`} className="debug-card-picker-item">
                  <CardStrip card={card} onClick={onSelectCard} onPreview={onSelectCard} />
                </div>
              ))}
            </div>
          </aside>
        </div>
      ) : null}
    </section>
  );
}
