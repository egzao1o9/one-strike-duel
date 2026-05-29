import type { CardDefinition } from "../types/cards";

interface CardStripProps {
  card: CardDefinition;
  onClick?: (card: CardDefinition) => void;
  onPreview?: (card: CardDefinition) => void;
  compact?: boolean;
  visibilityMarker?: "P" | "S";
  concealed?: boolean;
  animationKey?: string;
}

function statClass(stat: "attack" | "block" | "speed") {
  return `card-strip__stat card-strip__stat--${stat}`;
}

export function CardStrip({
  card,
  onClick,
  onPreview,
  compact = false,
  visibilityMarker,
  concealed = false,
  animationKey,
}: CardStripProps) {
  const showStats = card.card_type === "battle";
  const canPreview = Boolean(onPreview) && !concealed;

  return (
    <div className={`card-strip-row${compact ? " card-strip-row--compact" : ""}`} data-anim-key={animationKey}>
      {visibilityMarker ? (
        <span className={`card-strip__marker card-strip__marker--${visibilityMarker.toLowerCase()}`}>{visibilityMarker}</span>
      ) : (
        <span className="card-strip__marker-spacer" />
      )}
      <button
        type="button"
        className={`card-strip rarity-${card.rarity}${compact ? " card-strip--compact" : ""}${concealed ? " card-strip--concealed" : ""}`}
        onClick={() => {
          if (!concealed) {
            onClick?.(card);
          }
        }}
      >
        {concealed ? (
          <span className="card-strip__concealed-mark">？</span>
        ) : (
          <>
            <span className="card-strip__name">{card.name || card.id}</span>
            {showStats ? (
              <span className="card-strip__stats">
                <span className={statClass("attack")}>{card.attack}</span>
                <span className={statClass("block")}>{card.block}</span>
                <span className={statClass("speed")}>{card.speed}</span>
              </span>
            ) : (
              <span className="card-strip__type">{card.card_type}</span>
            )}
            {card.effect_text ? <span className="card-strip__effect">{card.effect_text}</span> : null}
          </>
        )}
      </button>
      {canPreview ? (
        <button
          type="button"
          className="card-strip__preview-button"
          onClick={() => onPreview?.(card)}
          aria-label={`${card.name || card.id} を拡大表示`}
        >
          👁
        </button>
      ) : null}
    </div>
  );
}
