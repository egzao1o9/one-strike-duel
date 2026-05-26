from __future__ import annotations

import argparse

from bots.registry import BOT_REGISTRY, build_bot
from engine.phase_runner import MatchRunner


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a batch of One Strike Duel matches.")
    parser.add_argument("--bot1", default="RandomBot", choices=sorted(BOT_REGISTRY))
    parser.add_argument("--bot2", default="RandomBot", choices=sorted(BOT_REGISTRY))
    parser.add_argument("--deck1", default="starter_attack")
    parser.add_argument("--deck2", default="starter_defense")
    parser.add_argument("--matches", type=int, default=100)
    parser.add_argument("--seed", type=int, default=7)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    wins = {"p1": 0, "p2": 0, "draw": 0}
    turn_total = 0
    for index in range(args.matches):
        runner = MatchRunner(
            build_bot(args.bot1, args.seed + index * 2),
            build_bot(args.bot2, args.seed + index * 2 + 1),
            args.deck1,
            args.deck2,
            seed=args.seed + index,
        )
        result = runner.run()
        if result.state.winner is None:
            wins["draw"] += 1
        else:
            wins[result.state.winner] += 1
        turn_total += int(result.log["turn_count"])
    print(f"matches={args.matches}")
    print(f"p1_wins={wins['p1']} p2_wins={wins['p2']} draws={wins['draw']}")
    print(f"avg_turns={turn_total / args.matches:.2f}")


if __name__ == "__main__":
    main()
