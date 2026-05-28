from __future__ import annotations

import argparse
import json
from pathlib import Path

from bots.registry import BOT_REGISTRY, build_bot
from engine.log_profiles import trim_match_log
from engine.phase_runner import MatchRunner


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run one One Strike Duel match.")
    parser.add_argument("--bot1", default="RandomBot", choices=sorted(BOT_REGISTRY))
    parser.add_argument("--bot2", default="RandomBot", choices=sorted(BOT_REGISTRY))
    parser.add_argument("--deck1", default="starter_attack")
    parser.add_argument("--deck2", default="starter_defense")
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--log-path", default="logs/match_log.json")
    parser.add_argument("--match-log-profile", choices=("minimal", "standard", "full"), default="standard")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    runner = MatchRunner(
        build_bot(args.bot1, args.seed),
        build_bot(args.bot2, args.seed + 1),
        args.deck1,
        args.deck2,
        seed=args.seed,
    )
    result = runner.run()
    log_path = Path(args.log_path)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(json.dumps(trim_match_log(result.log, args.match_log_profile), ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"winner={result.state.winner} reason={result.state.end_reason} turns={result.log['turn_count']}")
    print(log_path)


if __name__ == "__main__":
    main()
