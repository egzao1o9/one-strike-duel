# Public-Info Draft Bot Suite

## Configuration

- Matches Per Matchup: 1000
- Seed: 891
- Fast Report: on
- Draft Mode: `full`
- Lean Draft Logging: on
- Save Battle Logs: on
- Workers: 61
- Archetypes: `Standard`, `Aggro`, `Guard`
- Pairings: all combinations with replacement, mirrored by seat
- Per-match records: `match_records.jsonl` in each matchup directory

## Matchups

| Matchup | Matches | Ranking | Draws | Summary | Records |
|---|---:|---|---:|---|---|
| `AggroDraftBot` vs `AggroDraftBot` | 1000 | `Aggro` 45.5% | 90 | [aggro_vs_aggro](./aggro_vs_aggro/summary.md) | [jsonl](./aggro_vs_aggro/match_records.jsonl) |
| `AggroDraftBot` vs `GuardDraftBot` | 1000 | `Aggro` 48.9%, `Guard` 44.3% | 68 | [aggro_vs_guard](./aggro_vs_guard/summary.md) | [jsonl](./aggro_vs_guard/match_records.jsonl) |
| `GuardDraftBot` vs `GuardDraftBot` | 1000 | `Guard` 46.5% | 70 | [guard_vs_guard](./guard_vs_guard/summary.md) | [jsonl](./guard_vs_guard/match_records.jsonl) |
| `StandardDraftBot` vs `AggroDraftBot` | 1000 | `Standard` 46.8%, `Aggro` 45.7% | 75 | [standard_vs_aggro](./standard_vs_aggro/summary.md) | [jsonl](./standard_vs_aggro/match_records.jsonl) |
| `StandardDraftBot` vs `GuardDraftBot` | 1000 | `Guard` 46.9%, `Standard` 46.2% | 69 | [standard_vs_guard](./standard_vs_guard/summary.md) | [jsonl](./standard_vs_guard/match_records.jsonl) |
| `StandardDraftBot` vs `StandardDraftBot` | 1000 | `Standard` 46.7% | 66 | [standard_vs_standard](./standard_vs_standard/summary.md) | [jsonl](./standard_vs_standard/match_records.jsonl) |

## Bot Summary

| Bot | Draft | Play | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Aggro` | `AggroDraftBot` | `AggroBot` | 4000 | 1856 | 1821 | 323 | 46.4% | 43.8% | 24.6% | 33.2% | 42.1% | 46.6% | 46.2% | 70.3% | 2.0% | 27.7% |
| `Guard` | `GuardDraftBot` | `GuardBot` | 4000 | 1842 | 1881 | 277 | 46.1% | 38.7% | 24.3% | 36.3% | 39.4% | 45.3% | 46.8% | 71.1% | 1.8% | 27.1% |
| `Standard` | `StandardDraftBot` | `StandardBot` | 4000 | 1864 | 1860 | 276 | 46.6% | 42.8% | 22.8% | 33.2% | 44.0% | 46.4% | 46.8% | 70.3% | 2.2% | 27.6% |
## Bot Details

### Aggro

- Draft Bot: `AggroDraftBot`
- Play Bot: `AggroBot`
- Win Rate: 46.4%
- First Pass Win Rate: 43.8%
- Starting Player Win Rate: 46.6%
- Responding Player Win Rate: 46.2%
- Action Rates: set=70.3%, set_pass=2.0%, pass=27.7%
- set_pass Candidate Avg / Match: 11.564

| Opponent | Matches | Wins | Losses | Draws | Win Rate |
|---|---:|---:|---:|---:|---:|
| `Aggro` | 2000 | 910 | 910 | 180 | 45.5% |
| `Guard` | 1000 | 489 | 443 | 68 | 48.9% |
| `Standard` | 1000 | 457 | 468 | 75 | 45.7% |

#### Top Picked Cards

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 5289 | 1208 | 486 | 375 |
| 防御 | `battle_defend` | `common` | 4788 | 1056 | 392 | 262 |
| 圧迫 | `control_pressure` | `common` | 4722 | 933 | 401 | 0 |
| ステップ | `battle_step` | `common` | 4682 | 1033 | 405 | 284 |
| 構え | `control_guard` | `common` | 4255 | 555 | 260 | 0 |
| 集中 | `control_focus` | `common` | 4204 | 432 | 183 | 0 |
| 牽制 | `control_disrupt` | `common` | 4060 | 1069 | 492 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 3161 | 961 | 647 | 629 |
| 渾身 | `battle_all_in` | `rare` | 2945 | 919 | 369 | 350 |
| 貫き | `battle_pierce` | `uncommon` | 2715 | 687 | 392 | 367 |
| 崩し | `battle_break` | `uncommon` | 2662 | 691 | 410 | 369 |
| 大振り | `battle_heavy_swing` | `rare` | 2567 | 780 | 342 | 320 |
| 粉砕 | `battle_crush` | `uncommon` | 2338 | 630 | 315 | 286 |
| 残像 | `battle_afterimage` | `rare` | 2095 | 614 | 320 | 258 |
| 返し刃 | `battle_counter` | `uncommon` | 2092 | 599 | 314 | 254 |

### Guard

- Draft Bot: `GuardDraftBot`
- Play Bot: `GuardBot`
- Win Rate: 46.1%
- First Pass Win Rate: 38.7%
- Starting Player Win Rate: 45.3%
- Responding Player Win Rate: 46.8%
- Action Rates: set=71.1%, set_pass=1.8%, pass=27.1%
- set_pass Candidate Avg / Match: 14.752

| Opponent | Matches | Wins | Losses | Draws | Win Rate |
|---|---:|---:|---:|---:|---:|
| `Aggro` | 1000 | 443 | 489 | 68 | 44.3% |
| `Guard` | 2000 | 930 | 930 | 140 | 46.5% |
| `Standard` | 1000 | 469 | 462 | 69 | 46.9% |

#### Top Picked Cards

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 防御 | `battle_defend` | `common` | 4990 | 1231 | 510 | 325 |
| 攻撃 | `battle_attack` | `common` | 4926 | 1120 | 508 | 370 |
| 圧迫 | `control_pressure` | `common` | 4861 | 1139 | 482 | 0 |
| ステップ | `battle_step` | `common` | 4575 | 933 | 343 | 227 |
| 構え | `control_guard` | `common` | 4403 | 616 | 285 | 0 |
| 集中 | `control_focus` | `common` | 4129 | 390 | 160 | 0 |
| 牽制 | `control_disrupt` | `common` | 4116 | 1081 | 524 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 3201 | 1065 | 702 | 678 |
| 渾身 | `battle_all_in` | `rare` | 2666 | 739 | 298 | 281 |
| 崩し | `battle_break` | `uncommon` | 2646 | 775 | 472 | 425 |
| 鉄壁 | `battle_wall` | `rare` | 2646 | 840 | 381 | 153 |
| 貫き | `battle_pierce` | `uncommon` | 2603 | 743 | 436 | 393 |
| 返し刃 | `battle_counter` | `uncommon` | 2207 | 642 | 327 | 256 |
| 十字受け | `battle_cross_guard` | `uncommon` | 2169 | 681 | 282 | 176 |
| 踏ん張り | `battle_brace` | `uncommon` | 2133 | 651 | 297 | 214 |

### Standard

- Draft Bot: `StandardDraftBot`
- Play Bot: `StandardBot`
- Win Rate: 46.6%
- First Pass Win Rate: 42.8%
- Starting Player Win Rate: 46.4%
- Responding Player Win Rate: 46.8%
- Action Rates: set=70.3%, set_pass=2.2%, pass=27.6%
- set_pass Candidate Avg / Match: 12.514

| Opponent | Matches | Wins | Losses | Draws | Win Rate |
|---|---:|---:|---:|---:|---:|
| `Aggro` | 1000 | 468 | 457 | 75 | 46.8% |
| `Guard` | 1000 | 462 | 469 | 69 | 46.2% |
| `Standard` | 2000 | 934 | 934 | 132 | 46.7% |

#### Top Picked Cards

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 5020 | 1199 | 516 | 402 |
| 防御 | `battle_defend` | `common` | 4832 | 1133 | 440 | 257 |
| 圧迫 | `control_pressure` | `common` | 4801 | 984 | 444 | 0 |
| ステップ | `battle_step` | `common` | 4607 | 1067 | 417 | 300 |
| 構え | `control_guard` | `common` | 4451 | 611 | 259 | 0 |
| 集中 | `control_focus` | `common` | 4149 | 402 | 173 | 0 |
| 牽制 | `control_disrupt` | `common` | 4140 | 1092 | 472 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 3155 | 948 | 659 | 627 |
| 渾身 | `battle_all_in` | `rare` | 2728 | 836 | 343 | 327 |
| 崩し | `battle_break` | `uncommon` | 2651 | 735 | 432 | 397 |
| 貫き | `battle_pierce` | `uncommon` | 2645 | 781 | 455 | 408 |
| 大振り | `battle_heavy_swing` | `rare` | 2461 | 786 | 334 | 315 |
| 鉄壁 | `battle_wall` | `rare` | 2303 | 672 | 329 | 142 |
| 返し刃 | `battle_counter` | `uncommon` | 2187 | 619 | 339 | 263 |
| 粉砕 | `battle_crush` | `uncommon` | 2122 | 614 | 320 | 290 |
