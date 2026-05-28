import type { CardDefinition } from "../types/cards";
import { CardFull } from "./CardFull";

interface CardPreviewOverlayProps {
  card: CardDefinition | null;
  onClose: () => void;
}

export function CardPreviewOverlay({ card, onClose }: CardPreviewOverlayProps) {
  if (!card) {
    return null;
  }

  return (
    <div className="card-overlay-backdrop" onClick={onClose} role="presentation">
      <aside
        className="card-overlay"
        role="dialog"
        aria-modal="true"
        aria-label="カード詳細"
        onClick={(event) => event.stopPropagation()}
      >
        <div className="card-overlay__header">
          <p className="eyebrow">Card Preview</p>
          <button type="button" className="card-overlay__close" onClick={onClose}>
            閉じる
          </button>
        </div>
        <CardFull card={card} />
      </aside>
    </div>
  );
}
