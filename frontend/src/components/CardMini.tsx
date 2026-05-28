import type { CardDefinition } from "../types/cards";

interface CardMiniProps {
  card: CardDefinition;
  onClick?: (card: CardDefinition) => void;
  animationKey?: string;
}

function miniStatClass(stat: "attack" | "block" | "speed") {
  if (stat === "attack") {
    return "mini-stat mini-stat--attack";
  }
  if (stat === "block") {
    return "mini-stat mini-stat--block";
  }
  return "mini-stat mini-stat--speed";
}

export function CardMini({ card, onClick, animationKey }: CardMiniProps) {
  const showBattleStats = card.card_type === "battle";
  const className = `card-mini rarity-${card.rarity}${onClick ? " card-mini--interactive" : ""}`;

  const content = (
    <>
      <div className="card-mini__topline">
        <span className="card-mini__type">{card.card_type}</span>
      </div>

      <h4 className="card-mini__name">{card.name || card.id}</h4>

      {showBattleStats ? (
        <div className="card-mini__stats">
          <span className={miniStatClass("attack")}>{card.attack}</span>
          <span className={miniStatClass("block")}>{card.block}</span>
          <span className={miniStatClass("speed")}>{card.speed}</span>
        </div>
      ) : null}

      {card.effect_text ? <p className="card-mini__effect">{card.effect_text}</p> : null}
    </>
  );

  if (!onClick) {
    return (
      <div className={className} data-anim-key={animationKey}>
        {content}
      </div>
    );
  }

  return (
    <button
      type="button"
      className={className}
      onClick={() => onClick?.(card)}
      data-anim-key={animationKey}
    >
      {content}
    </button>
  );
}
