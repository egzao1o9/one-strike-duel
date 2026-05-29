import { useEffect, useLayoutEffect, useMemo, useReducer, useRef, useState, type CSSProperties, type ReactNode } from "react";
import { CardMini } from "./components/CardMini";
import { CardPreviewOverlay } from "./components/CardPreviewOverlay";
import { CardStrip } from "./components/CardStrip";
import { PlayableBattlePanel } from "./components/PlayableBattlePanel";
import { getAllCards, groupCards, summarizeByRarity, summarizeByType } from "./lib/cards";
import { summarizeDraftDeck } from "./lib/draftSession";
import { initialPrototypeState, prototypeReducer } from "./store/prototype";
import type { CardDefinition, CardRarity } from "./types/cards";
import type { BattleSession, DraftDeckState, DraftSession, MarketRowState, PlayerId } from "./types/prototype";

const cards = getAllCards();
const cardsById = new Map(cards.map((card) => [card.id, card]));
const cardsByType = groupCards(cards);
const typeSummary = summarizeByType(cards);
const raritySummary = summarizeByRarity(cards);

const prototypeMilestones = [
  "12枚デッキの市場ドラフトを遊ぶ",
  "Standard CPU と対戦できる形にする",
  "アクション単位のログとリプレイに繋げる",
  "itch.io に載せる検証版へ仕上げる",
];

interface SlotDisplayEntry {
  card: CardDefinition;
  marker: "P" | "S";
  concealed: boolean;
}

interface FlyingDraftCard {
  id: string;
  card: CardDefinition;
  concealed: boolean;
  sourceRect: DOMRect;
  targetRect: DOMRect;
}

function playerLabel(playerId: PlayerId) {
  return playerId === "p1" ? "プレイヤー" : "CPU";
}

function buildSlotVisibilityEntries(
  slotCards: CardDefinition[],
  publicCards: CardDefinition[],
  options: { concealSecret: boolean },
): SlotDisplayEntry[] {
  const { concealSecret } = options;
  const publicCounts = new Map<string, number>();
  publicCards.forEach((card) => {
    publicCounts.set(card.id, (publicCounts.get(card.id) ?? 0) + 1);
  });

  return slotCards.map((card) => {
    const visibleLeft = publicCounts.get(card.id) ?? 0;
    if (visibleLeft > 0) {
      publicCounts.set(card.id, visibleLeft - 1);
      return { card, marker: "P", concealed: false };
    }
    return { card, marker: "S", concealed: concealSecret };
  });
}

function deckTypeCounts(deck: DraftDeckState) {
  const allCards = [...deck.starter, ...deck.publicCards, ...deck.hiddenCards];
  return {
    battle: allCards.filter((card) => card.card_type === "battle").length,
    control: allCards.filter((card) => card.card_type === "control").length,
    blessing: allCards.filter((card) => card.card_type === "blessing").length,
  };
}

function DraftSidebar({ title, subtitle, children }: { title: string; subtitle: string; children: ReactNode }) {
  return (
    <aside className="draft-sidebar">
      <div className="card-section__header">
        <h3>{title}</h3>
        <span>{subtitle}</span>
      </div>
      <div className="draft-sidebar__body">{children}</div>
    </aside>
  );
}

function SlotSummary({
  title,
  entries,
  capacity,
  owner,
}: {
  title: string;
  entries: SlotDisplayEntry[];
  capacity: number;
  owner: PlayerId;
}) {
  const slots = Array.from({ length: capacity }, (_, index) => entries[index] ?? null);
  const slotGroup: "rare" | "uncommon" | "common" =
    title === "Rare" ? "rare" : title === "Uncommon" ? "uncommon" : "common";

  return (
    <section className="strip-section">
      <div className="card-section__header">
        <h4 className="slot-title">{title}</h4>
        <span>
          {entries.length}/{capacity}
        </span>
      </div>
      <div className="slot-strip-grid">
        {slots.map((entry, index) =>
          entry ? (
            <CardStrip
              key={`${title}-${entry.card.id}-${index}`}
              card={entry.card}
              visibilityMarker={entry.marker}
              concealed={entry.concealed}
              animationKey={`slot-${owner}-${slotGroup}-${index}`}
            />
          ) : (
            <div key={`${title}-empty-${index}`} className="slot-strip-placeholder" data-anim-key={`slot-${owner}-${slotGroup}-${index}`} />
          ),
        )}
      </div>
    </section>
  );
}

function MarketRowView({
  row,
  canAct,
  onTakeVisible,
  onTakeTopdeck,
  onSelectCard,
  pendingGapIndex,
}: {
  row: MarketRowState;
  canAct: boolean;
  onTakeVisible: (pickKey: string) => void;
  onTakeTopdeck: (rarity: CardRarity) => void;
  onSelectCard: (card: CardDefinition) => void;
  pendingGapIndex: number | null;
}) {
  const visibleSlots = [...row.visibleCards];
  if (pendingGapIndex !== null && pendingGapIndex >= 0 && pendingGapIndex <= visibleSlots.length) {
    visibleSlots.splice(pendingGapIndex, 0, null as never);
  }

  return (
    <section className={`market-row market-row--${row.rarity}`}>
      <button
        type="button"
        className="market-topdeck"
        onClick={() => onTakeTopdeck(row.rarity)}
        disabled={!canAct || !row.topDeckAvailable}
        data-anim-key={`topdeck-${row.rarity}`}
      >
        <span className="market-topdeck__label">{row.rarity === "rare" ? "Rare" : row.rarity === "uncommon" ? "Uncommon" : "Common"}山札</span>
        <span className="market-topdeck__sub">{row.topDeckAvailable ? "トップを取る" : "残りなし"}</span>
      </button>
      <div className="market-visible-row">
        {Array.from({ length: 3 }, (_, index) => visibleSlots[index] ?? null).map((card, index) =>
          card ? (
            <div key={`${row.rarity}-${index}-${card.id}`} className="market-visible-card">
              <CardMini card={card} onClick={onSelectCard} animationKey={`market-card-${row.rarity}-${index}`} />
              <button type="button" className="draft-pack__select" onClick={() => onTakeVisible(`${row.rarity}:${index}`)} disabled={!canAct}>
                このカードを取る
              </button>
            </div>
          ) : (
            <div key={`${row.rarity}-placeholder-${index}`} className="market-visible-card market-visible-card--empty">
              <div className="market-visible-card__placeholder" />
            </div>
          ),
        )}
      </div>
    </section>
  );
}

function DraftSummaryPanel({
  session,
  onTakeVisible,
  onTakeTopdeck,
  onSelectCard,
}: {
  session: DraftSession;
  onTakeVisible: (pickKey: string) => void;
  onTakeTopdeck: (rarity: CardRarity) => void;
  onSelectCard: (card: CardDefinition) => void;
}) {
  const p1Summary = summarizeDraftDeck(session.decks.p1);
  const p2Summary = summarizeDraftDeck(session.decks.p2);
  const p1Types = deckTypeCounts(session.decks.p1);
  const p2Types = deckTypeCounts(session.decks.p2);
  const isAnimating = session.pendingRefillRarity !== null || session.pendingCpuTurn;
  const isPlayerTurn = session.currentStep.phase === "market" && session.currentStep.actingPlayer === "p1" && !isAnimating;
  const p1PublicKnown = [...session.decks.p1.starter, ...session.decks.p1.publicCards];
  const p2PublicKnown = [...session.decks.p2.starter, ...session.decks.p2.publicCards];
  const p1RareEntries = buildSlotVisibilityEntries(session.decks.p1.rareSlots, p1PublicKnown, { concealSecret: false });
  const p1UncommonEntries = buildSlotVisibilityEntries(session.decks.p1.uncommonSlots, p1PublicKnown, { concealSecret: false });
  const p1CommonEntries = buildSlotVisibilityEntries([...session.decks.p1.starter, ...session.decks.p1.commonSlots], p1PublicKnown, {
    concealSecret: false,
  });
  const p2RareEntries = buildSlotVisibilityEntries(session.decks.p2.rareSlots, p2PublicKnown, { concealSecret: true });
  const p2UncommonEntries = buildSlotVisibilityEntries(session.decks.p2.uncommonSlots, p2PublicKnown, { concealSecret: true });
  const p2CommonEntries = buildSlotVisibilityEntries([...session.decks.p2.starter, ...session.decks.p2.commonSlots], p2PublicKnown, {
    concealSecret: true,
  });

  return (
    <section className="preview-panel">
      <div className="section-heading">
        <div>
          <p className="eyebrow">Draft Session</p>
          <h2>市場ドラフト</h2>
        </div>
        <p className="section-note">取得後は同じ位置が一度グレーになり、演出完了後にその場へ補充されます。</p>
      </div>

      <div className="dashboard-panel dashboard-panel--embedded">
        <div className="summary-card">
          <h2>現在の手番</h2>
          <p className="big-number small">{session.currentStep.phase === "complete" ? "完了" : playerLabel(session.currentStep.actingPlayer)}</p>
          <p>先手: {playerLabel(session.firstPlayer)}</p>
          <p>Pick: {session.currentStep.pickNumber}</p>
          <p>Phase: {session.currentStep.phase}</p>
        </div>
        <div className="summary-card">
          <h2>プレイヤー</h2>
          <ul className="compact-list">
            <li>デッキ枚数: {p1Summary.total}</li>
            <li>公開: {p1Summary.publicCount}</li>
            <li>秘密: {p1Summary.hiddenCount}</li>
            <li>
              Common / Uncommon / Rare: {p1Summary.rarityCounts.common} / {p1Summary.rarityCounts.uncommon} / {p1Summary.rarityCounts.rare}
            </li>
          </ul>
        </div>
        <div className="summary-card">
          <h2>CPU</h2>
          <ul className="compact-list">
            <li>デッキ枚数: {p2Summary.total}</li>
            <li>公開: {p2Summary.publicCount}</li>
            <li>秘密: {p2Summary.hiddenCount}</li>
            <li>
              Common / Uncommon / Rare: {p2Summary.rarityCounts.common} / {p2Summary.rarityCounts.uncommon} / {p2Summary.rarityCounts.rare}
            </li>
          </ul>
        </div>
        <div className="summary-card">
          <h2>プール残数</h2>
          <ul className="compact-list">
            <li>合計: {session.poolSnapshot.remainingTotal}</li>
            <li>Common: {session.poolSnapshot.remainingByRarity.common}</li>
            <li>Uncommon: {session.poolSnapshot.remainingByRarity.uncommon}</li>
            <li>Rare: {session.poolSnapshot.remainingByRarity.rare}</li>
          </ul>
        </div>
      </div>

      <div className="draft-workbench">
        <DraftSidebar title="CPU 情報" subtitle={`B${p2Types.battle} / C${p2Types.control} / BL${p2Types.blessing}`}>
          <SlotSummary title="Rare" entries={p2RareEntries} capacity={2} owner="p2" />
          <SlotSummary title="Uncommon" entries={p2UncommonEntries} capacity={5} owner="p2" />
          <SlotSummary title="Common" entries={p2CommonEntries} capacity={5} owner="p2" />
        </DraftSidebar>

        <section className="draft-center">
          <div className="market-board">
            {(["rare", "uncommon", "common"] as CardRarity[]).map((rarity) => (
              <MarketRowView
                key={rarity}
                row={session.marketRows[rarity]}
                canAct={isPlayerTurn}
                onTakeVisible={onTakeVisible}
                onTakeTopdeck={onTakeTopdeck}
                onSelectCard={onSelectCard}
                pendingGapIndex={session.pendingRefillRarity === rarity ? session.pendingVisibleGapIndex : null}
              />
            ))}
          </div>

          <div className="summary-card summary-card--log">
            <h2>ドラフトログ</h2>
            <ol className="compact-list compact-list--logs">
              {session.logs.slice(-10).map((entry) => (
                <li key={entry.id}>
                  <strong>{entry.kind}</strong>: {entry.text}
                </li>
              ))}
            </ol>
          </div>
        </section>

        <DraftSidebar title="プレイヤー情報" subtitle={`B${p1Types.battle} / C${p1Types.control} / BL${p1Types.blessing}`}>
          <SlotSummary title="Rare" entries={p1RareEntries} capacity={2} owner="p1" />
          <SlotSummary title="Uncommon" entries={p1UncommonEntries} capacity={5} owner="p1" />
          <SlotSummary title="Common" entries={p1CommonEntries} capacity={5} owner="p1" />
        </DraftSidebar>
      </div>
    </section>
  );
}

function DeckReviewPanel({
  session,
  onSelectCard,
  onStartBattle,
}: {
  session: DraftSession;
  onSelectCard: (card: CardDefinition) => void;
  onStartBattle: () => void;
}) {
  const p1Summary = summarizeDraftDeck(session.decks.p1);
  const p2Summary = summarizeDraftDeck(session.decks.p2);
  const p1Types = deckTypeCounts(session.decks.p1);
  const p2Types = deckTypeCounts(session.decks.p2);
  const p1PublicKnown = [...session.decks.p1.starter, ...session.decks.p1.publicCards];
  const p2PublicKnown = [...session.decks.p2.starter, ...session.decks.p2.publicCards];

  const p1RareEntries = buildSlotVisibilityEntries(session.decks.p1.rareSlots, p1PublicKnown, { concealSecret: false });
  const p1UncommonEntries = buildSlotVisibilityEntries(session.decks.p1.uncommonSlots, p1PublicKnown, { concealSecret: false });
  const p1CommonEntries = buildSlotVisibilityEntries([...session.decks.p1.starter, ...session.decks.p1.commonSlots], p1PublicKnown, {
    concealSecret: false,
  });
  const p2RareEntries = buildSlotVisibilityEntries(session.decks.p2.rareSlots, p2PublicKnown, { concealSecret: true });
  const p2UncommonEntries = buildSlotVisibilityEntries(session.decks.p2.uncommonSlots, p2PublicKnown, { concealSecret: true });
  const p2CommonEntries = buildSlotVisibilityEntries([...session.decks.p2.starter, ...session.decks.p2.commonSlots], p2PublicKnown, {
    concealSecret: true,
  });

  return (
    <section className="preview-panel">
      <div className="section-heading">
        <div>
          <p className="eyebrow">Deck Review</p>
          <h2>デッキ確認</h2>
        </div>
        <p className="section-note">公開情報と自分のシークレットを見直してから対戦へ進みます。</p>
      </div>

      <div className="dashboard-panel dashboard-panel--embedded">
        <div className="summary-card">
          <h2>プレイヤー</h2>
          <ul className="compact-list">
            <li>総枚数: {p1Summary.total}</li>
            <li>公開 / 秘密: {p1Summary.publicCount} / {p1Summary.hiddenCount}</li>
            <li>B / C / BL: {p1Types.battle} / {p1Types.control} / {p1Types.blessing}</li>
          </ul>
        </div>
        <div className="summary-card">
          <h2>CPU</h2>
          <ul className="compact-list">
            <li>総枚数: {p2Summary.total}</li>
            <li>公開 / 秘密: {p2Summary.publicCount} / {p2Summary.hiddenCount}</li>
            <li>B / C / BL: {p2Types.battle} / {p2Types.control} / {p2Types.blessing}</li>
          </ul>
        </div>
        <div className="summary-card summary-card--actions">
          <h2>次のステップ</h2>
          <p>StandardBot 戦のバトル画面へ進みます。</p>
          <button type="button" className="primary-button" onClick={onStartBattle}>
            対戦開始
          </button>
        </div>
      </div>

      <div className="draft-workbench">
        <DraftSidebar title="CPU 情報" subtitle={`B${p2Types.battle} / C${p2Types.control} / BL${p2Types.blessing}`}>
          <SlotSummary title="Rare" entries={p2RareEntries} capacity={2} owner="p2" />
          <SlotSummary title="Uncommon" entries={p2UncommonEntries} capacity={5} owner="p2" />
          <SlotSummary title="Common" entries={p2CommonEntries} capacity={5} owner="p2" />
        </DraftSidebar>

        <section className="draft-center">
          <div className="summary-card summary-card--showcase">
            <h2>公開カードの確認</h2>
            <div className="mini-card-grid">
              {session.decks.p1.publicCards.slice(0, 6).map((card) => (
                <CardMini key={`review-public-${card.id}`} card={card} onClick={onSelectCard} />
              ))}
            </div>
          </div>
          <div className="summary-card summary-card--log">
            <h2>ドラフトログ</h2>
            <ol className="compact-list compact-list--logs">
              {session.logs.slice(-12).map((entry) => (
                <li key={entry.id}>
                  <strong>{entry.kind}</strong>: {entry.text}
                </li>
              ))}
            </ol>
          </div>
        </section>

        <DraftSidebar title="プレイヤー情報" subtitle={`B${p1Types.battle} / C${p1Types.control} / BL${p1Types.blessing}`}>
          <SlotSummary title="Rare" entries={p1RareEntries} capacity={2} owner="p1" />
          <SlotSummary title="Uncommon" entries={p1UncommonEntries} capacity={5} owner="p1" />
          <SlotSummary title="Common" entries={p1CommonEntries} capacity={5} owner="p1" />
        </DraftSidebar>
      </div>
    </section>
  );
}

function BattlePanel({
  draftSession,
  battleSession,
  onSelectCard,
}: {
  draftSession: DraftSession;
  battleSession: BattleSession;
  onSelectCard: (card: CardDefinition) => void;
}) {
  const [showLog, setShowLog] = useState(false);
  const p1 = battleSession.players.p1;
  const p2 = battleSession.players.p2;
  const p1Types = deckTypeCounts(draftSession.decks.p1);
  const p2Types = deckTypeCounts(draftSession.decks.p2);

  return (
    <section className="preview-panel">
      <div className="section-heading">
        <div>
          <p className="eyebrow">Battle Prototype</p>
          <h2>対戦画面</h2>
        </div>
        <div className="battle-toolbar">
          <p className="section-note">初期手札4枚、1ターン目ドローなしの開始状態です。次は control / battle の行動処理を入れます。</p>
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
          <p>フェイズ: {battleSession.phase}</p>
        </div>
        <div className="summary-card">
          <h2>プレイヤー</h2>
          <p>手札 {p1.hand.length} / 山札 {p1.drawPile.length}</p>
          <p>捨て札 {p1.discardPile.length} / 使用済み {p1.usedCards.length}</p>
          <p>B / C / BL: {p1Types.battle} / {p1Types.control} / {p1Types.blessing}</p>
        </div>
        <div className="summary-card">
          <h2>CPU</h2>
          <p>手札 {p2.hand.length} / 山札 {p2.drawPile.length}</p>
          <p>捨て札 {p2.discardPile.length} / 使用済み {p2.usedCards.length}</p>
          <p>B / C / BL: {p2Types.battle} / {p2Types.control} / {p2Types.blessing}</p>
        </div>
      </div>

      <div className="battle-table">
        <section className="summary-card battle-lane battle-lane--opponent">
          <div className="battle-lane__header">
            <h2>CPU</h2>
            <span>手札 {p2.hand.length}</span>
          </div>
          <div className="battle-zone-row">
            <div className="battle-zone-card battle-zone-card--hidden">{p2.setCards.length > 0 ? `${p2.setCards.length} set` : "set なし"}</div>
            <div className="battle-zone-card">{p2.currentControlCard ? p2.currentControlCard.name || p2.currentControlCard.id : "control なし"}</div>
            <div className="battle-zone-card">{p2.blessingZone ? p2.blessingZone.name || p2.blessingZone.id : "加護 なし"}</div>
          </div>
        </section>

        <section className="summary-card battle-lane battle-lane--center">
          <div className="battle-emblem">{battleSession.turn}</div>
          <p>Turn</p>
          <p>{playerLabel(battleSession.actingPlayer)} の行動待ち</p>
        </section>

        <section className="summary-card battle-lane battle-lane--player">
          <div className="battle-lane__header">
            <h2>プレイヤー手札</h2>
            <span>{p1.hand.length} 枚</span>
          </div>
          <div className="card-strip-list">
            {p1.hand.map((card, index) => (
              <CardStrip key={`hand-${card.id}-${index}`} card={card} onClick={onSelectCard} />
            ))}
          </div>
          <div className="battle-zone-row">
            <div className="battle-zone-card">{p1.setCards.length > 0 ? `${p1.setCards.length} set` : "set なし"}</div>
            <div className="battle-zone-card">{p1.currentControlCard ? p1.currentControlCard.name || p1.currentControlCard.id : "control なし"}</div>
            <div className="battle-zone-card">{p1.blessingZone ? p1.blessingZone.name || p1.blessingZone.id : "加護 なし"}</div>
          </div>
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

void BattlePanel;

export default function App() {
  const [state, dispatch] = useReducer(prototypeReducer, initialPrototypeState);
  const [selectedCard, setSelectedCard] = useState<CardDefinition | null>(null);
  const [flyingCard, setFlyingCard] = useState<FlyingDraftCard | null>(null);
  const sortedCards = useMemo(() => [...cards].sort((left, right) => left.name.localeCompare(right.name, "ja")), []);
  const currentRectsRef = useRef<Map<string, DOMRect>>(new Map());
  const previousRectsRef = useRef<Map<string, DOMRect>>(new Map());
  const handledDraftLogIdRef = useRef<string | null>(null);

  function collectAnimRects() {
    const nextRects = new Map<string, DOMRect>();
    document.querySelectorAll<HTMLElement>("[data-anim-key]").forEach((element) => {
      const key = element.dataset.animKey;
      if (key) {
        nextRects.set(key, element.getBoundingClientRect());
      }
    });
    currentRectsRef.current = nextRects;
  }

  useLayoutEffect(() => {
    previousRectsRef.current = currentRectsRef.current;
    collectAnimRects();
  });

  useEffect(() => {
    const refreshRects = () => {
      collectAnimRects();
    };
    window.addEventListener("scroll", refreshRects, { passive: true });
    window.addEventListener("resize", refreshRects);
    return () => {
      window.removeEventListener("scroll", refreshRects);
      window.removeEventListener("resize", refreshRects);
    };
  }, []);

  useEffect(() => {
    handledDraftLogIdRef.current = null;
  }, [state.activeSession?.seed]);

  useEffect(() => {
    const lastLog = state.activeSession?.logs.at(-1);
    const event = lastLog?.draftEvent;
    if (!event || handledDraftLogIdRef.current === lastLog.id) {
      return;
    }
    handledDraftLogIdRef.current = lastLog.id;

    const sourceRect = currentRectsRef.current.get(event.sourceKey) ?? previousRectsRef.current.get(event.sourceKey);
    const targetRect = currentRectsRef.current.get(event.targetKey) ?? previousRectsRef.current.get(event.targetKey);
    const card = cardsById.get(event.cardId);

    if (!sourceRect || !targetRect || !card) {
      dispatch({ type: "resolve_draft_animation" });
      return;
    }

    setFlyingCard({
      id: lastLog.id,
      card,
      concealed: event.playerId === "p2" && event.visibility === "hidden",
      sourceRect,
      targetRect,
    });

    const timer = window.setTimeout(() => {
      setFlyingCard((current) => (current?.id === lastLog.id ? null : current));
      dispatch({ type: "resolve_draft_animation" });
    }, 1050);
    return () => window.clearTimeout(timer);
  }, [state.activeSession?.logs]);

  useEffect(() => {
    const session = state.activeSession;
    if (!session || flyingCard) {
      return;
    }
    if (
      session.currentStep.phase !== "market" ||
      session.currentStep.actingPlayer !== "p2" ||
      !session.pendingCpuTurn ||
      session.pendingRefillRarity !== null
    ) {
      return;
    }

    const timer = window.setTimeout(() => {
      dispatch({ type: "resolve_draft_animation" });
    }, 180);

    return () => window.clearTimeout(timer);
  }, [
    flyingCard,
    state.activeSession?.currentStep.phase,
    state.activeSession?.currentStep.actingPlayer,
    state.activeSession?.pendingCpuTurn,
    state.activeSession?.pendingRefillRarity,
  ]);

  return (
    <main className="app-shell">
      <section className="hero-panel">
        <p className="eyebrow">One Strike Duel</p>
        <h1>ブラウザ版プロトタイプ</h1>
        <p className="lead">人間が遊んで面白いかを検証するための CPU 戦プロトタイプです。まずは 12 枚デッキの市場ドラフトから始めます。</p>

        <div className="hero-actions">
          <button type="button" className="primary-button" onClick={() => dispatch({ type: "start_prototype" })}>
            プロトタイプを開始
          </button>
          <button type="button" className="secondary-button" onClick={() => dispatch({ type: "start_debug_battle" })}>
            デバッグ対戦を開始
          </button>
          <button type="button" className="secondary-button" onClick={() => setSelectedCard(sortedCards[0] ?? null)}>
            カード一覧を見る
          </button>
        </div>

        <div className="hero-grid">
          <article className="summary-card">
            <h2>この段階で試したいこと</h2>
            <ol>
              {prototypeMilestones.map((milestone) => (
                <li key={milestone}>{milestone}</li>
              ))}
            </ol>
          </article>

          <article className="summary-card">
            <h2>カードデータ概要</h2>
            <ul className="compact-list">
              <li>総カード数: {cards.length}</li>
              <li>
                battle / control / blessing: {typeSummary.battle} / {typeSummary.control} / {typeSummary.blessing}
              </li>
              <li>
                common / uncommon / rare: {raritySummary.common} / {raritySummary.uncommon} / {raritySummary.rare}
              </li>
            </ul>
          </article>
        </div>
      </section>

      {state.activeSession && state.screen === "draft" ? (
        <DraftSummaryPanel
          session={state.activeSession}
          onTakeVisible={(pickKey) => dispatch({ type: "choose_visible_card", pickKey })}
          onTakeTopdeck={(rarity) => dispatch({ type: "take_topdeck", rarity })}
          onSelectCard={setSelectedCard}
        />
      ) : state.activeSession && state.screen === "deck_review" ? (
        <DeckReviewPanel session={state.activeSession} onSelectCard={setSelectedCard} onStartBattle={() => dispatch({ type: "enter_battle" })} />
) : state.activeBattle && state.screen === "battle" ? (
        <PlayableBattlePanel
          battleSession={state.activeBattle}
          onSelectCard={setSelectedCard}
          onChooseMulligan={(handIndexes) => dispatch({ type: "choose_mulligan", handIndexes })}
          onChooseControl={(handIndex) => dispatch({ type: "choose_control", handIndex })}
          onBattleAction={(actionType, handIndexes) =>
            dispatch({ type: "choose_battle_action", actionType, handIndexes })
          }
          onResolveTriggerChoice={(useTrigger, choiceId) =>
            dispatch({ type: "resolve_trigger_choice", useTrigger, choiceId })
          }
          onAdvanceReveal={() => dispatch({ type: "advance_reveal" })}
          onResolveBlessingChoice={(useBlessing) =>
            dispatch({ type: "resolve_blessing_choice", useBlessing })
          }
          onDebugAddCardToHand={(drawPileIndex) =>
            dispatch({ type: "debug_add_card_to_hand", drawPileIndex })
          }
          onDebugSetup={(preset) => dispatch({ type: "debug_battle_preset", preset })}
          onDebugPlaceCard={(playerId, zone, cardId) =>
            dispatch({ type: "debug_place_card", playerId, zone, cardId })
          }
          onDebugClearZone={(playerId, zone) => dispatch({ type: "debug_clear_zone", playerId, zone })}
          onDebugSetPhase={(phase) => dispatch({ type: "debug_set_phase", phase })}
          onDebugStartReveal={() => dispatch({ type: "debug_start_reveal" })}
        />
      ) : (
        <section className="dashboard-panel">
          {(["battle", "control", "blessing"] as const).map((type) => (
            <article key={type} className="summary-card">
              <h2>{type.toUpperCase()}</h2>
              <div className="mini-card-grid">
                {cardsByType[type].slice(0, 3).map((card) => (
                  <CardMini key={card.id} card={card} onClick={setSelectedCard} />
                ))}
              </div>
            </article>
          ))}
        </section>
      )}

      {flyingCard ? (
        <div
          className={`draft-fly-card rarity-${flyingCard.card.rarity}${flyingCard.concealed ? " draft-fly-card--concealed" : ""}`}
          style={
            {
              left: `${flyingCard.sourceRect.left}px`,
              top: `${flyingCard.sourceRect.top}px`,
              width: `${flyingCard.sourceRect.width}px`,
              height: `${flyingCard.sourceRect.height}px`,
              "--fly-x": `${flyingCard.targetRect.left - flyingCard.sourceRect.left}px`,
              "--fly-y": `${flyingCard.targetRect.top - flyingCard.sourceRect.top}px`,
            } as CSSProperties
          }
        >
          {flyingCard.concealed ? <span className="draft-fly-card__concealed">？</span> : <CardMini card={flyingCard.card} />}
        </div>
      ) : null}

      <CardPreviewOverlay card={selectedCard} onClose={() => setSelectedCard(null)} />
    </main>
  );
}
