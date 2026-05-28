import type { CardDefinition } from "../types/cards";

function battleStatClass(stat: "attack" | "block" | "speed") {
  if (stat === "attack") {
    return "stat-block stat-block--attack";
  }
  if (stat === "block") {
    return "stat-block stat-block--block";
  }
  return "stat-block stat-block--speed";
}

export function CardFull({ card }: { card: CardDefinition }) {
  const showBattleStats = card.card_type === "battle";

  return (
    <article className={`card-full rarity-${card.rarity}`}>
      <header className="card-full__header">
        <p className="card-full__type">{card.card_type}</p>
        <span className="card-full__rarity">{card.rarity}</span>
      </header>

      <h3 className="card-full__name">{card.name || card.id}</h3>

      {showBattleStats ? (
        <div className="card-full__stats">
          <div className={battleStatClass("attack")}>
            <span className="stat-block__label">A</span>
            <strong className="stat-block__value">{card.attack}</strong>
          </div>
          <div className={battleStatClass("block")}>
            <span className="stat-block__label">B</span>
            <strong className="stat-block__value">{card.block}</strong>
          </div>
          <div className={battleStatClass("speed")}>
            <span className="stat-block__label">S</span>
            <strong className="stat-block__value">{card.speed}</strong>
          </div>
        </div>
      ) : null}

      <div className="card-full__body">
        {card.effect_text ? <p className="card-full__effect">{card.effect_text}</p> : null}
        {card.flavor_text ? <p className="card-full__flavor">{card.flavor_text}</p> : null}
      </div>

      <footer className="card-full__footer">
        <p className="card-full__id">{card.id}</p>
      </footer>
    </article>
  );
}
