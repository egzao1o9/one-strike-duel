export interface RandomSource {
  next(): number;
  int(maxExclusive: number): number;
  getState(): number;
}

export function createSeededRandom(seed: number): RandomSource {
  let value = seed >>> 0;

  const next = () => {
    value += 0x6d2b79f5;
    let t = value;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };

  return {
    next,
    int(maxExclusive: number) {
      return Math.floor(next() * maxExclusive);
    },
    getState() {
      return value >>> 0;
    },
  };
}
