from __future__ import annotations

from pathlib import Path


def prune_match_logs(matches_dir: str | Path, keep_latest: int) -> None:
    if keep_latest < 0:
        return
    directory = Path(matches_dir)
    if not directory.exists():
        return

    grouped: dict[str, list[Path]] = {}
    for path in directory.iterdir():
        if not path.is_file():
            continue
        match_prefix = path.name.split("_", 2)
        if len(match_prefix) < 2:
            continue
        match_id = "_".join(match_prefix[:2])
        grouped.setdefault(match_id, []).append(path)

    ordered_match_ids = sorted(grouped.keys(), reverse=True)
    keep_ids = set(ordered_match_ids[:keep_latest])
    for match_id, paths in grouped.items():
        if match_id in keep_ids:
            continue
        for path in paths:
            path.unlink(missing_ok=True)
