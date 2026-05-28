import { useEffect, useState } from "react";
import { CardMini } from "./CardMini";
import { CardStrip } from "./CardStrip";
import type { CardDefinition } from "../types/cards";
import type { BattleSession, BattleSetCard, DebugBattlePreset, PlayerId } from "../types/prototype";

function playerLabel(playerId: PlayerId) {
  return playerId === "p1" ? "プレイヤー" : "CPU";
}

function HiddenMiniCard() {
  return (
    <div className="battle-hidden-mini">
      <span>?</span>
    </div>
  );
}

function EmptyZoneMini() {
  return <div className="battle-empty-mini" />;
}

function ZoneMiniCard({
  card,
  onPreview,
}: {
  card: CardDefinition;
  onPreview: (card: CardDefinition) => void;
}) {
  return (
    <div className="battle-zone-mini-card">
      <CardMini card={card} onClick={onPreview} />
    </div>
  );
}

function SetMiniCard({
  item,
  onPreview,
}: {
  item: BattleSetCard;
  onPreview: (card: CardDefinition) => void;
}) {
  if (!item.revealed) {
    return <HiddenMiniCard />;
  }
  return <ZoneMiniCard card={item.card} onPreview={onPreview} />;
}

interface PlayableBattlePanelProps {
  battleSession: BattleSession;
  onSelectCard: (card: CardDefinition) => void;
  onChooseMulligan: (handIndexes: number[]) => void;
  onChooseControl: (handIndex: number | null) => void;
  onBattleAction: (actionType: "set" | "set_pass" | "pass", handIndexes: number[]) => void;
  onResolveTriggerChoice: (useTrigger: boolean, setIndex?: number | null) => void;
  onResolveBlessingChoice: (useBlessing: boolean) => void;
  onDebugAddCardToHand: (drawPileIndex: number) => void;
  onDebugSetup: (preset: DebugBattlePreset) => void;
}

function PileGroup({
  side,
  drawPileCount,
  discardCount,
  onOpenDiscard,
}: {
  side: "player" | "opponent";
  drawPileCount: number;
  discardCount: number;
  onOpenDiscard: () => void;
}) {
  return (
    <div className={`battle-pile-group battle-pile-group--${side}`}>
      {side === "opponent" ? (
        <>
          <button
            type="button"
            className="battle-pile battle-pile--discard"
            onClick={onOpenDiscard}
            aria-label={`捨て札 ${discardCount} 枚`}
          >
            <span className="battle-pile__label">捨て札</span>
            <span className="battle-pile__count">{discardCount}</span>
          </button>
          <button
            type="button"
            className="battle-pile battle-pile--deck"
            title={`残り ${drawPileCount} 枚`}
            aria-label={`山札 残り ${drawPileCount} 枚`}
          >
            <span className="battle-pile__label">山札</span>
          </button>
        </>
      ) : (
        <>
          <button
            type="button"
            className="battle-pile battle-pile--deck"
            title={`残り ${drawPileCount} 枚`}
            aria-label={`山札 残り ${drawPileCount} 枚`}
          >
            <span className="battle-pile__label">山札</span>
          </button>
          <button
            type="button"
            className="battle-pile battle-pile--discard"
            onClick={onOpenDiscard}
            aria-label={`捨て札 ${discardCount} 枚`}
          >
            <span className="battle-pile__label">捨て札</span>
            <span className="battle-pile__count">{discardCount}</span>
          </button>
        </>
      )}
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
  onResolveBlessingChoice,
  onDebugAddCardToHand,
  onDebugSetup,
}: PlayableBattlePanelProps) {
  const [showLog, setShowLog] = useState(false);
  const [showDebugCardPicker, setShowDebugCardPicker] = useState(false);
  const [showDiscardFor, setShowDiscardFor] = useState<"p1" | "p2" | null>(null);
  const [selectedHandIndexes, setSelectedHandIndexes] = useState<number[]>([]);

  const p1 = battleSession.players.p1;
  const p2 = battleSession.players.p2;
  const discardViewerPlayer = showDiscardFor ? battleSession.players[showDiscardFor] : null;

  const selectableControlIndexes = p1.hand
    .map((card, index) => ({ card, index }))
    .filter(({ card }) => card.card_type === "control" || (card.card_type === "blessing" && !p1.blessingZone));

  const selectableBattleIndexes = p1.hand
    .map((card, index) => ({ card, index }))
    .filter(({ card }) => card.card_type === "battle" || card.card_type === "control");

  const selectedControlCard =
    selectableControlIndexes.find(({ index }) => selectedHandIndexes.includes(index))?.card ?? null;

  const selectedBattleCards = selectableBattleIndexes
    .filter(({ index }) => selectedHandIndexes.includes(index))
    .map(({ card }) => card);

  const maxSelectableBattleCards = Math.min(2, Math.max(0, p2.setCards.length + 1 - p1.setCards.length));
  const canSetCards = maxSelectableBattleCards > 0 && selectableBattleIndexes.length > 0;

  const playerOutcome = battleSession.winner === null ? "Draw" : battleSession.winner === "p1" ? "Win" : "Lose";
  const cpuOutcome = battleSession.winner === null ? "Draw" : battleSession.winner === "p2" ? "Win" : "Lose";

  useEffect(() => {
    setSelectedHandIndexes([]);
  }, [battleSession.phase, battleSession.turn, p1.hand.length]);

  function toggleHandCard(card: CardDefinition, handIndex: number) {
    if (battleSession.phase === "control") {
      if (!(card.card_type === "control" || (card.card_type === "blessing" && !p1.blessingZone))) {
        return;
      }
      setSelectedHandIndexes((current) => (current[0] === handIndex ? [] : [handIndex]));
      return;
    }

    if (battleSession.phase === "mulligan") {
      setSelectedHandIndexes((current) =>
        current.includes(handIndex) ? current.filter((index) => index !== handIndex) : [...current, handIndex],
      );
      return;
    }

    if (battleSession.phase === "battle_select") {
      if (maxSelectableBattleCards <= 0) {
        return;
      }
      if (!(card.card_type === "battle" || card.card_type === "control")) {
        return;
      }

      setSelectedHandIndexes((current) => {
        if (current.includes(handIndex)) {
          return current.filter((index) => index !== handIndex);
        }
        if (current.length >= maxSelectableBattleCards) {
          if (maxSelectableBattleCards <= 1) {
            return [handIndex];
          }
          return [current[1], handIndex];
        }
        return [...current, handIndex];
      });
    }
  }

  return (
    <section className="preview-panel">
      <div className="section-heading">
        <div>
          <p className="eyebrow">Battle Prototype</p>
          <h2>対戦画面</h2>
        </div>
        <div className="battle-toolbar">
          <p className="section-note">マリガン、control、battle、加護確認までを試せるプロトタイプです。</p>
          <div className="battle-debug-actions">
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
          <button type="button" className="battle-log-button" onClick={() => setShowLog(true)} aria-label="ログを開く">
            Log
          </button>
        </div>
      </div>

      <div className="dashboard-panel dashboard-panel--embedded battle-dashboard">
        <div className="summary-card">
          <h2>進行</h2>
          <p className="big-number small">{playerLabel(battleSession.actingPlayer)}</p>
          <p>先手: {playerLabel(battleSession.firstPlayer)}</p>
          <p>ターン: {battleSession.turn}</p>
          <p>フェーズ: {battleSession.phase}</p>
        </div>
        <div className="summary-card">
          <h2>プレイヤー</h2>
          <div className="battle-summary-debug">
            <button type="button" className="secondary-button" onClick={() => setShowDebugCardPicker(true)}>
              Debug Deck
            </button>
          </div>
          <p>手札 {p1.hand.length} / 山札 {p1.drawPile.length}</p>
          <p>捨て札 {p1.discardPile.length} / 使用済み {p1.usedCards.length}</p>
          <p>加護: {p1.blessingZone ? `${p1.blessingZone.name || p1.blessingZone.id}${p1.blessingFaceUp ? " 表" : " 裏"}` : "なし"}</p>
        </div>
        <div className="summary-card">
          <h2>CPU</h2>
          <p>手札 {p2.hand.length} / 山札 {p2.drawPile.length}</p>
          <p>捨て札 {p2.discardPile.length} / 使用済み {p2.usedCards.length}</p>
          <p>加護: {p2.blessingZone ? `${p2.blessingZone.name || p2.blessingZone.id}${p2.blessingFaceUp ? " 表" : " 裏"}` : "なし"}</p>
        </div>
      </div>

      <div className="battle-layout">
        <section className="summary-card battle-side battle-side--opponent">
          <div className="battle-side__header">
            <h2>CPU 手札</h2>
            <span>{p2.hand.length} 枚</span>
          </div>
          <div className="battle-opponent-hand">
            {Array.from({ length: p2.hand.length }, (_, index) => (
              <div key={`cpu-hand-${index}`} className="battle-opponent-hand-slot" />
            ))}
          </div>

          <div className="battle-zone-grid battle-zone-grid--opponent">
            <PileGroup
              side="opponent"
              drawPileCount={p2.drawPile.length}
              discardCount={p2.discardPile.length}
              onOpenDiscard={() => setShowDiscardFor("p2")}
            />
            <div className="battle-zone-cluster">
              <div className="battle-zone-panel">
                <div className="battle-zone-panel__label">加護ゾーン</div>
                <div className="battle-zone-mini-row">
                  {p2.blessingZone ? <ZoneMiniCard card={p2.blessingZone} onPreview={onSelectCard} /> : <EmptyZoneMini />}
                </div>
              </div>
              <div className="battle-zone-panel">
                <div className="battle-zone-panel__label">コントロールゾーン</div>
                <div className="battle-zone-mini-row">
                  {p2.currentControlCard ? <ZoneMiniCard card={p2.currentControlCard} onPreview={onSelectCard} /> : <EmptyZoneMini />}
                </div>
              </div>
            </div>
          </div>
        </section>

        <section className="summary-card battle-mid">
          <div className="battle-mid__status">
            <div className="battle-mid__turn">T{battleSession.turn}</div>
            <div className="battle-mid__phase">{battleSession.phase}</div>
          </div>

          <div className="battle-arena battle-arena--opponent">
            <div className="battle-arena__label">CPU バトルゾーン</div>
            <div className="battle-set-row">
              {p2.setCards.length > 0
                ? p2.setCards.map((item, index) => (
                    <SetMiniCard key={`cpu-set-${index}-${item.card.id}`} item={item} onPreview={onSelectCard} />
                  ))
                : null}
            </div>
          </div>

          <div className="battle-divider" />

          <div className="battle-arena battle-arena--player">
            <div className="battle-arena__label">プレイヤー バトルゾーン</div>
            <div className="battle-set-row">
              {p1.setCards.length > 0
                ? p1.setCards.map((item, index) => (
                    <SetMiniCard key={`p1-set-${index}-${item.card.id}`} item={item} onPreview={onSelectCard} />
                  ))
                : null}
            </div>
          </div>
        </section>

        <section className="summary-card battle-side battle-side--player">
          <div className="battle-zone-grid battle-zone-grid--player">
            <div className="battle-zone-cluster">
              <div className="battle-zone-panel">
                <div className="battle-zone-panel__label">コントロールゾーン</div>
                <div className="battle-zone-mini-row">
                  {p1.currentControlCard ? <ZoneMiniCard card={p1.currentControlCard} onPreview={onSelectCard} /> : <EmptyZoneMini />}
                </div>
              </div>
              <div className="battle-zone-panel">
                <div className="battle-zone-panel__label">加護ゾーン</div>
                <div className="battle-zone-mini-row">
                  {p1.blessingZone ? <ZoneMiniCard card={p1.blessingZone} onPreview={onSelectCard} /> : <EmptyZoneMini />}
                </div>
              </div>
            </div>
            <PileGroup
              side="player"
              drawPileCount={p1.drawPile.length}
              discardCount={p1.discardPile.length}
              onOpenDiscard={() => setShowDiscardFor("p1")}
            />
          </div>

          <div className="battle-side__header">
            <h2>プレイヤー手札</h2>
            <span>{p1.hand.length} 枚</span>
          </div>
          <div className="battle-hand-row">
            {p1.hand.map((card, index) => (
              <div
                key={`hand-${card.id}-${index}`}
                className={`battle-hand-card${selectedHandIndexes.includes(index) ? " battle-hand-card--selected" : ""}`}
              >
                {selectedHandIndexes.includes(index) ? (
                  <div className="battle-hand-order-badge">{selectedHandIndexes.indexOf(index) + 1}</div>
                ) : null}
                <CardMini card={card} onClick={() => toggleHandCard(card, index)} />
                <button
                  type="button"
                  className="battle-hand-preview-button"
                  onClick={() => onSelectCard(card)}
                  aria-label={`${card.name || card.id} を拡大表示`}
                >
                  👁
                </button>
              </div>
            ))}
          </div>

          {battleSession.phase === "mulligan" ? (
            <div className="battle-action-panel">
              <p className="battle-action-caption">マリガン: 引き直したいカードを選んでください。</p>
              <div className="battle-action-row">
                <button type="button" className="primary-button" onClick={() => onChooseMulligan(selectedHandIndexes)}>
                  選択カードをマリガン
                </button>
                <button type="button" className="secondary-button" onClick={() => onChooseMulligan([])}>
                  このまま開始
                </button>
              </div>
            </div>
          ) : null}

          {battleSession.phase === "control" ? (
            <div className="battle-action-panel">
              <p className="battle-action-caption">control フェーズ: control または blessing を使うか選んでください。</p>
              <div className="battle-action-row">
                <button
                  type="button"
                  className="primary-button"
                  disabled={!selectedControlCard}
                  onClick={() => onChooseControl(selectedHandIndexes[0] ?? null)}
                >
                  選択カードを使う
                </button>
                <button type="button" className="secondary-button" onClick={() => onChooseControl(null)}>
                  使わない
                </button>
              </div>
            </div>
          ) : null}

          {battleSession.phase === "battle_select" ? (
            <div className="battle-action-panel">
              <p className="battle-action-caption">battle フェーズ: battle / control カードを伏せます。</p>
              <p className="battle-action-caption">この場面で選べる枚数: 最大 {maxSelectableBattleCards} 枚</p>
              {!canSetCards ? (
                <p className="battle-action-caption">この場面では追加でセットできません。pass のみ可能です。</p>
              ) : null}
              <div className="battle-action-row">
                <button
                  type="button"
                  className="primary-button"
                  disabled={selectedBattleCards.length === 0 || !canSetCards}
                  onClick={() => onBattleAction("set", selectedHandIndexes)}
                >
                  set
                </button>
                <button
                  type="button"
                  className="secondary-button"
                  disabled={selectedBattleCards.length === 0 || !canSetCards}
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

          {battleSession.phase === "trigger_prompt" && battleSession.pendingTriggerChoice ? (
            <div className="battle-action-panel">
              <p className="battle-action-caption">加護確認: {battleSession.pendingTriggerChoice.blessingName}</p>
              <p className="battle-action-caption">{battleSession.pendingTriggerChoice.promptText}</p>
              {battleSession.pendingTriggerChoice.mode === "choose_set_card" && battleSession.pendingTriggerChoice.choices ? (
                <div className="battle-action-row">
                  {battleSession.pendingTriggerChoice.choices.map((choice) => (
                    <button
                      key={`trigger-choice-${choice.setIndex}`}
                      type="button"
                      className="secondary-button"
                      onClick={() => onResolveTriggerChoice(true, choice.setIndex)}
                    >
                      {choice.label}
                    </button>
                  ))}
                  <button type="button" className="secondary-button" onClick={() => onResolveTriggerChoice(false, null)}>
                    使わない
                  </button>
                </div>
              ) : (
                <div className="battle-action-row">
                  <button type="button" className="primary-button" onClick={() => onResolveTriggerChoice(true, null)}>
                    使う
                  </button>
                  <button type="button" className="secondary-button" onClick={() => onResolveTriggerChoice(false, null)}>
                    使わない
                  </button>
                </div>
              )}
            </div>
          ) : null}

          {battleSession.phase === "blessing_prompt" && battleSession.pendingBlessingChoice ? (
            <div className="battle-action-panel">
              <p className="battle-action-caption">加護確認: {battleSession.pendingBlessingChoice.blessingName}</p>
              <p className="battle-action-caption">{battleSession.pendingBlessingChoice.promptText}</p>
              <div className="battle-result-grid">
                <div className="battle-result-card">
                  <strong>現在</strong>
                  <span>
                    A {battleSession.finalLines?.p1.attack ?? 0} / B {battleSession.finalLines?.p1.block ?? 0} / S{" "}
                    {battleSession.finalLines?.p1.speed ?? 0}
                  </span>
                  <span>
                    CPU A {battleSession.finalLines?.p2.attack ?? 0} / B {battleSession.finalLines?.p2.block ?? 0} / S{" "}
                    {battleSession.finalLines?.p2.speed ?? 0}
                  </span>
                </div>
                <div className="battle-result-card">
                  <strong>使用後</strong>
                  <span>
                    A {battleSession.pendingBlessingChoice.previewLines.p1.attack} / B{" "}
                    {battleSession.pendingBlessingChoice.previewLines.p1.block} / S{" "}
                    {battleSession.pendingBlessingChoice.previewLines.p1.speed}
                  </span>
                  <span>
                    CPU A {battleSession.pendingBlessingChoice.previewLines.p2.attack} / B{" "}
                    {battleSession.pendingBlessingChoice.previewLines.p2.block} / S{" "}
                    {battleSession.pendingBlessingChoice.previewLines.p2.speed}
                  </span>
                </div>
              </div>
              <div className="battle-action-row">
                <button type="button" className="primary-button" onClick={() => onResolveBlessingChoice(true)}>
                  使う
                </button>
                <button type="button" className="secondary-button" onClick={() => onResolveBlessingChoice(false)}>
                  使わない
                </button>
              </div>
            </div>
          ) : null}

          {battleSession.phase === "result" && battleSession.finalLines ? (
            <div className="battle-result-panel">
              <p className="battle-result-headline">
                {battleSession.winner ? `${playerLabel(battleSession.winner)} の勝ち` : "引き分け"}
              </p>
              <div className="battle-result-grid">
                <div className="battle-result-card">
                  <strong>プレイヤー</strong>
                  <em>{playerOutcome}</em>
                  <span>
                    A {battleSession.finalLines.p1.attack} / B {battleSession.finalLines.p1.block} / S{" "}
                    {battleSession.finalLines.p1.speed}
                  </span>
                </div>
                <div className="battle-result-card">
                  <strong>CPU</strong>
                  <em>{cpuOutcome}</em>
                  <span>
                    A {battleSession.finalLines.p2.attack} / B {battleSession.finalLines.p2.block} / S{" "}
                    {battleSession.finalLines.p2.speed}
                  </span>
                </div>
              </div>
            </div>
          ) : null}
        </section>
      </div>

      {showLog ? (
        <div className="card-overlay-backdrop" onClick={() => setShowLog(false)} role="presentation">
          <aside className="card-overlay battle-log-overlay" role="dialog" aria-modal="true" aria-label="対戦ログ" onClick={(event) => event.stopPropagation()}>
            <div className="card-overlay__header">
              <p className="eyebrow">Battle Log</p>
              <button type="button" className="card-overlay__close" onClick={() => setShowLog(false)}>
                閉じる
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
                      {playerLabel(entry.playerId)} / {entry.sourceCardName}: {entry.text}
                    </li>
                  ))}
                </ol>
              </>
            ) : null}
          </aside>
        </div>
      ) : null}

      {showDebugCardPicker ? (
        <div className="card-overlay-backdrop" onClick={() => setShowDebugCardPicker(false)} role="presentation">
          <aside
            className="card-overlay battle-log-overlay debug-card-picker-overlay"
            role="dialog"
            aria-modal="true"
            aria-label="Debug card picker"
            onClick={(event) => event.stopPropagation()}
          >
            <div className="card-overlay__header">
              <p className="eyebrow">Debug</p>
              <button type="button" className="card-overlay__close" onClick={() => setShowDebugCardPicker(false)}>
                閉じる
              </button>
            </div>
            <p className="battle-action-caption">山札の中身を確認して、選んだ1枚を山札から手札へ移動します。</p>
            <div className="debug-card-picker-list">
              {p1.drawPile.map((card, index) => (
                <button
                  key={`debug-card-${card.id}-${index}`}
                  type="button"
                  className="debug-card-picker-item"
                  onClick={() => {
                    onDebugAddCardToHand(index);
                    setShowDebugCardPicker(false);
                  }}
                >
                  <CardStrip card={card} />
                </button>
              ))}
            </div>
          </aside>
        </div>
      ) : null}

      {showDiscardFor && discardViewerPlayer ? (
        <div className="card-overlay-backdrop" onClick={() => setShowDiscardFor(null)} role="presentation">
          <aside
            className="card-overlay battle-log-overlay debug-card-picker-overlay"
            role="dialog"
            aria-modal="true"
            aria-label="Discard pile"
            onClick={(event) => event.stopPropagation()}
          >
            <div className="card-overlay__header">
              <p className="eyebrow">Discard</p>
              <button type="button" className="card-overlay__close" onClick={() => setShowDiscardFor(null)}>
                閉じる
              </button>
            </div>
            <p className="battle-action-caption">{playerLabel(showDiscardFor)} の捨て札</p>
            <div className="debug-card-picker-list">
              {[...discardViewerPlayer.discardPile].reverse().map((card, index) => (
                <button
                  key={`discard-${showDiscardFor}-${card.id}-${index}`}
                  type="button"
                  className="debug-card-picker-item"
                  onClick={() => onSelectCard(card)}
                >
                  <CardStrip card={card} />
                </button>
              ))}
            </div>
          </aside>
        </div>
      ) : null}
    </section>
  );
}
