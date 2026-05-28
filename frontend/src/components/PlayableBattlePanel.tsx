import { useEffect, useState } from "react";
import { CardMini } from "./CardMini";
import type { CardDefinition } from "../types/cards";
import type { BattleSession } from "../types/prototype";

function playerLabel(playerId: "p1" | "p2") {
  return playerId === "p1" ? "プレイヤー" : "CPU";
}

function zoneLabel(card: CardDefinition | null, empty: string) {
  return card ? card.name || card.id : empty;
}

interface PlayableBattlePanelProps {
  battleSession: BattleSession;
  onSelectCard: (card: CardDefinition) => void;
  onChooseControl: (cardId: string | null) => void;
  onBattleAction: (actionType: "set" | "set_pass" | "pass", cardIds: string[]) => void;
}

export function PlayableBattlePanel({
  battleSession,
  onSelectCard,
  onChooseControl,
  onBattleAction,
}: PlayableBattlePanelProps) {
  const [showLog, setShowLog] = useState(false);
  const [selectedHandIds, setSelectedHandIds] = useState<string[]>([]);
  const p1 = battleSession.players.p1;
  const p2 = battleSession.players.p2;
  const selectableControlCards = p1.hand.filter((card) => card.card_type === "control" || (card.card_type === "blessing" && !p1.blessingZone));
  const selectableBattleCards = p1.hand.filter((card) => card.card_type === "battle" || card.card_type === "control");
  const selectedControlCard = selectableControlCards.find((card) => selectedHandIds.includes(card.id)) ?? null;
  const selectedBattleCards = selectableBattleCards.filter((card) => selectedHandIds.includes(card.id));

  useEffect(() => {
    setSelectedHandIds([]);
  }, [battleSession.phase, battleSession.turn, p1.hand.length]);

  function toggleHandCard(card: CardDefinition) {
    if (battleSession.phase === "control") {
      if (!(card.card_type === "control" || (card.card_type === "blessing" && !p1.blessingZone))) {
        onSelectCard(card);
        return;
      }
      setSelectedHandIds((current) => (current[0] === card.id ? [] : [card.id]));
      return;
    }

    if (battleSession.phase === "battle_select") {
      if (!(card.card_type === "battle" || card.card_type === "control")) {
        onSelectCard(card);
        return;
      }
      setSelectedHandIds((current) => {
        if (current.includes(card.id)) {
          return current.filter((id) => id !== card.id);
        }
        if (current.length >= 2) {
          return [current[1], card.id];
        }
        return [...current, card.id];
      });
      return;
    }

    onSelectCard(card);
  }

  return (
    <section className="preview-panel">
      <div className="section-heading">
        <div>
          <p className="eyebrow">Battle Prototype</p>
          <h2>対戦画面</h2>
        </div>
        <div className="battle-toolbar">
          <p className="section-note">対戦処理の最小版です。まずは control と battle の入力を最後まで通せる状態を目指しています。</p>
          <button type="button" className="battle-log-button" onClick={() => setShowLog(true)} aria-label="対戦ログを開く">
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
          <p>手札 {p1.hand.length} / 山札 {p1.drawPile.length}</p>
          <p>捨て札 {p1.discardPile.length} / 使用済み {p1.usedCards.length}</p>
          <p>加護: {p1.blessingZone ? `${p1.blessingZone.name || p1.blessingZone.id}${p1.blessingFaceUp ? " 表" : " 裏"}` : "なし"}</p>
        </div>
        <div className="summary-card">
          <h2>CPU</h2>
          <p>手札 {p2.hand.length} / 山札 {p2.drawPile.length}</p>
          <p>捨て札 {p2.discardPile.length} / 使用済み {p2.usedCards.length}</p>
          <p>加護: {p2.blessingZone ? `${p2.blessingFaceUp ? "表向き" : "裏向き"} 1枚` : "なし"}</p>
        </div>
      </div>

      <div className="battle-table">
        <section className="summary-card battle-lane battle-lane--opponent">
          <div className="battle-lane__header">
            <h2>CPU</h2>
            <span>手札 {p2.hand.length}</span>
          </div>
          <div className="battle-opponent-hand">
            {Array.from({ length: p2.hand.length }, (_, index) => (
              <div key={`cpu-hand-${index}`} className="battle-opponent-hand-slot" />
            ))}
          </div>
          <div className="battle-zone-row">
            <div className="battle-zone-card battle-zone-card--hidden">{p2.setCards.length > 0 ? `${p2.setCards.length} set` : "set なし"}</div>
            <div className="battle-zone-card">{zoneLabel(p2.currentControlCard, "control なし")}</div>
            <div className="battle-zone-card">{zoneLabel(p2.blessingZone, "加護 なし")}</div>
          </div>
        </section>

        <section className="summary-card battle-lane battle-lane--center">
          <div className="battle-emblem">{battleSession.turn}</div>
          <p>Turn</p>
          <p>{playerLabel(battleSession.actingPlayer)} の行動中</p>
        </section>

        <section className="summary-card battle-lane battle-lane--player">
          <div className="battle-lane__header">
            <h2>プレイヤー手札</h2>
            <span>{p1.hand.length} 枚</span>
          </div>
          <div className="battle-hand-row">
            {p1.hand.map((card, index) => (
              <div key={`hand-${card.id}-${index}`} className={`battle-hand-card${selectedHandIds.includes(card.id) ? " battle-hand-card--selected" : ""}`}>
                <CardMini card={card} onClick={toggleHandCard} />
              </div>
            ))}
          </div>
          <div className="battle-zone-row">
            <div className="battle-zone-card">{p1.setCards.length > 0 ? `${p1.setCards.length} set` : "set なし"}</div>
            <div className="battle-zone-card">{zoneLabel(p1.currentControlCard, "control なし")}</div>
            <div className="battle-zone-card">{zoneLabel(p1.blessingZone, "加護 なし")}</div>
          </div>

          {battleSession.phase === "control" ? (
            <div className="battle-action-panel">
              <p className="battle-action-caption">control フェーズ: control か blessing を1枚使うか、何もしないかを選びます。</p>
              <div className="battle-action-row">
                <button type="button" className="primary-button" disabled={!selectedControlCard} onClick={() => onChooseControl(selectedControlCard?.id ?? null)}>
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
              <p className="battle-action-caption">battle フェーズ: battle / control を0〜2枚選び、set / set_pass / pass を行います。</p>
              <div className="battle-action-row">
                <button type="button" className="primary-button" disabled={selectedBattleCards.length === 0} onClick={() => onBattleAction("set", selectedBattleCards.map((card) => card.id))}>
                  set
                </button>
                <button type="button" className="secondary-button" disabled={selectedBattleCards.length === 0} onClick={() => onBattleAction("set_pass", selectedBattleCards.map((card) => card.id).slice(0, 1))}>
                  set_pass
                </button>
                <button type="button" className="secondary-button" onClick={() => onBattleAction("pass", [])}>
                  pass
                </button>
              </div>
            </div>
          ) : null}

          {battleSession.phase === "result" && battleSession.finalLines ? (
            <div className="battle-result-panel">
              <p className="battle-result-headline">{battleSession.winner ? `${playerLabel(battleSession.winner)} の勝ち` : "引き分け"}</p>
              <div className="battle-result-grid">
                <div className="battle-result-card">
                  <strong>プレイヤー</strong>
                  <span>A {battleSession.finalLines.p1.attack} / B {battleSession.finalLines.p1.block} / S {battleSession.finalLines.p1.speed}</span>
                </div>
                <div className="battle-result-card">
                  <strong>CPU</strong>
                  <span>A {battleSession.finalLines.p2.attack} / B {battleSession.finalLines.p2.block} / S {battleSession.finalLines.p2.speed}</span>
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
          </aside>
        </div>
      ) : null}
    </section>
  );
}
