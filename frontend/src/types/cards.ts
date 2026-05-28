export type CardType = "battle" | "control" | "blessing";
export type CardRarity = "common" | "uncommon" | "rare";

export interface CardEffect {
  id?: string;
  seq?: number;
  timing?: string;
  kind?: string;
  value?: number;
  value2?: number;
  count?: number;
  enabled?: boolean;
  effect_type?: string;
  target?: string;
  stat?: string;
  priority?: number;
}

export interface CardDefinition {
  id: string;
  name: string;
  card_type: CardType;
  rarity: CardRarity;
  attack: number;
  block: number;
  speed: number;
  tags: string[];
  effect_text: string;
  enabled: boolean;
  play_zone: string;
  after_play_zone: string;
  slot_type: string;
  flavor_text: string;
  effects: CardEffect[];
  notes: string;
}
