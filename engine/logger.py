from __future__ import annotations

import json
from pathlib import Path

from engine.game_state import GameState


class MatchLogger:
    def __init__(self, match_id: str, state: GameState) -> None:
        self.payload: dict[str, object] = {
            "match_id": match_id,
            "players": {
                player_id: {
                    "bot": player.bot_name,
                    "deck": player.deck_id,
                }
                for player_id, player in state.players.items()
            },
            "turns": [],
        }
        self._current_turn: dict[str, object] | None = None

    def start_turn(self, turn: int) -> None:
        self._current_turn = {"turn": turn}
        self.payload["turns"].append(self._current_turn)

    def record_turn_start(self, payload: dict[str, object]) -> None:
        assert self._current_turn is not None
        self._current_turn["turn_start"] = payload

    def record_phase1(self, discarded: dict[str, list[str]], hand_counts: dict[str, int] | None = None) -> None:
        assert self._current_turn is not None
        self._current_turn["phase1_mulligan"] = {
            "p1_discarded": discarded["p1"],
            "p2_discarded": discarded["p2"],
            "hand_counts": hand_counts or {},
        }

    def record_control(
        self,
        cards: dict[str, str | None],
        reveals: dict[str, list[str]],
        card_ids: dict[str, str | None] | None = None,
        card_sources: dict[str, str | None] | None = None,
        hand_counts: dict[str, int] | None = None,
        debug: dict[str, object] | None = None,
        blessing_changes: dict[str, object] | None = None,
    ) -> None:
        assert self._current_turn is not None
        self._current_turn["control"] = {
            "p1": cards["p1"],
            "p2": cards["p2"],
            "reveals": reveals,
            "ids": card_ids or {},
            "sources": card_sources or {},
            "hand_counts": hand_counts or {},
            "debug": debug or {},
            "blessing_changes": blessing_changes or {},
        }

    def record_phase3(self, discarded: dict[str, list[str]], hand_counts: dict[str, int] | None = None) -> None:
        assert self._current_turn is not None
        self._current_turn["phase3_mulligan"] = {
            "p1_discarded": discarded["p1"],
            "p2_discarded": discarded["p2"],
            "hand_counts": hand_counts or {},
        }

    def record_battle(self, battle_payload: dict[str, object]) -> None:
        assert self._current_turn is not None
        self._current_turn["battle"] = battle_payload

    def finish(self, state: GameState) -> dict[str, object]:
        self.payload["players"] = {
            player_id: {
                "bot": player.bot_name,
                "deck": player.deck_id,
                "reshuffle_count": player.reshuffle_count,
                "reshuffle_turns": list(player.reshuffle_turns),
                "deck_exhaustion_count": player.deck_exhaustion_count,
                "deck_exhaustion_turns": list(player.deck_exhaustion_turns),
                "draw_shortfall_turns": list(player.draw_shortfall_turns),
                "remaining_draw_pile_count": len(player.draw_pile),
                "remaining_discard_pile_count": len(player.discard_pile),
                "remaining_hand_count": len(player.hand),
                "active_blessing": None if player.blessing_zone is None else player.blessing_zone.id,
                "blessing_face_up": player.blessing_face_up,
                "blessing_placed_turns": list(player.blessing_placed_turns),
                "blessing_used_turns": list(player.blessing_used_turns),
                "blessing_facedown_turns": list(player.blessing_facedown_turns),
                "blessing_pressure_pass_actions": player.blessing_pressure_pass_actions,
            }
            for player_id, player in state.players.items()
        }
        self.payload["winner"] = state.winner
        self.payload["end_reason"] = state.end_reason
        self.payload["turn_count"] = len(self.payload["turns"])
        return self.payload

    def write_json(self, path: str | Path) -> None:
        file_path = Path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open("w", encoding="utf-8") as handle:
            json.dump(self.payload, handle, ensure_ascii=False, indent=2)
