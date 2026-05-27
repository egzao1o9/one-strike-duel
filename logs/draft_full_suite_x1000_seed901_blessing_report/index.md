# Public-Info Draft Bot Suite

## Configuration

- Matches Per Matchup: 1000
- Seed: 901
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
| `AggroDraftBot` vs `AggroDraftBot` | 1000 | `Aggro` 46.1% | 79 | [aggro_vs_aggro](./aggro_vs_aggro/summary.md) | [jsonl](./aggro_vs_aggro/match_records.jsonl) |
| `AggroDraftBot` vs `GuardDraftBot` | 1000 | `Aggro` 47.8%, `Guard` 45.5% | 67 | [aggro_vs_guard](./aggro_vs_guard/summary.md) | [jsonl](./aggro_vs_guard/match_records.jsonl) |
| `GuardDraftBot` vs `GuardDraftBot` | 1000 | `Guard` 46.8% | 64 | [guard_vs_guard](./guard_vs_guard/summary.md) | [jsonl](./guard_vs_guard/match_records.jsonl) |
| `StandardDraftBot` vs `AggroDraftBot` | 1000 | `Aggro` 47.4%, `Standard` 46.8% | 58 | [standard_vs_aggro](./standard_vs_aggro/summary.md) | [jsonl](./standard_vs_aggro/match_records.jsonl) |
| `StandardDraftBot` vs `GuardDraftBot` | 1000 | `Guard` 46.9%, `Standard` 46.2% | 69 | [standard_vs_guard](./standard_vs_guard/summary.md) | [jsonl](./standard_vs_guard/match_records.jsonl) |
| `StandardDraftBot` vs `StandardDraftBot` | 1000 | `Standard` 46.1% | 78 | [standard_vs_standard](./standard_vs_standard/summary.md) | [jsonl](./standard_vs_standard/match_records.jsonl) |

## Bot Summary

| Bot | Draft | Play | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Aggro` | `AggroDraftBot` | `AggroBot` | 4000 | 1873 | 1844 | 283 | 46.8% | 45.4% | 15.1% | 54.5% | 30.4% | 45.3% | 48.4% | 72.4% | 2.2% | 25.4% |
| `Guard` | `GuardDraftBot` | `GuardBot` | 4000 | 1860 | 1876 | 264 | 46.5% | 41.7% | 15.9% | 55.2% | 28.9% | 44.8% | 48.2% | 72.5% | 1.7% | 25.8% |
| `Standard` | `StandardDraftBot` | `StandardBot` | 4000 | 1852 | 1865 | 283 | 46.3% | 43.2% | 14.0% | 54.9% | 31.1% | 44.0% | 48.6% | 72.3% | 2.1% | 25.6% |
## Bot Details

### Aggro

- Draft Bot: `AggroDraftBot`
- Play Bot: `AggroBot`
- Win Rate: 46.8%
- First Pass Win Rate: 45.4%
- Starting Player Win Rate: 45.3%
- Responding Player Win Rate: 48.4%
- Action Rates: set=72.4%, set_pass=2.2%, pass=25.4%
- set_pass Candidate Avg / Match: 16.411

| Opponent | Matches | Wins | Losses | Draws | Win Rate |
|---|---:|---:|---:|---:|---:|
| `Aggro` | 2000 | 921 | 921 | 158 | 46.1% |
| `Guard` | 1000 | 478 | 455 | 67 | 47.8% |
| `Standard` | 1000 | 474 | 468 | 58 | 47.4% |

#### Top Picked Cards

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 5342 | 1448 | 653 | 454 |
| 防御 | `battle_defend` | `common` | 4863 | 1215 | 481 | 281 |
| ステップ | `battle_step` | `common` | 4774 | 1266 | 510 | 330 |
| 圧迫 | `control_pressure` | `common` | 4645 | 1476 | 620 | 153 |
| 構え | `control_guard` | `common` | 4230 | 1171 | 506 | 144 |
| 集中 | `control_focus` | `common` | 4087 | 1077 | 433 | 137 |
| 牽制 | `control_disrupt` | `common` | 4059 | 1233 | 578 | 49 |
| 貫き | `battle_pierce` | `uncommon` | 2611 | 826 | 534 | 487 |
| 崩し | `battle_break` | `uncommon` | 2579 | 815 | 478 | 425 |
| 粉砕 | `battle_crush` | `uncommon` | 2289 | 745 | 381 | 338 |
| 返し刃 | `battle_counter` | `uncommon` | 2186 | 718 | 373 | 269 |
| 踏ん張り | `battle_brace` | `uncommon` | 2033 | 660 | 320 | 212 |
| 十字受け | `battle_cross_guard` | `uncommon` | 1977 | 601 | 289 | 160 |
| フェイント | `battle_feint` | `uncommon` | 1856 | 571 | 224 | 127 |
| 強撃 | `battle_power_attack` | `uncommon` | 1837 | 564 | 287 | 228 |

#### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 防壁の加護 | `blessing_barrier` | 439 | 46.2% | 445 | 114 | 114 | 25 | 25 | 0 | 0 |
| 防の加護 | `blessing_guard` | 422 | 46.7% | 423 | 96 | 96 | 0 | 0 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 413 | 46.5% | 415 | 140 | 140 | 32 | 32 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 383 | 41.8% | 384 | 76 | 76 | 76 | 0 | 0 | 76 |
| 速の加護 | `blessing_speed` | 377 | 45.6% | 380 | 96 | 96 | 0 | 0 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 367 | 42.8% | 368 | 107 | 107 | 0 | 0 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 355 | 44.5% | 357 | 66 | 66 | 4 | 4 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 337 | 44.5% | 339 | 68 | 68 | 0 | 0 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 328 | 46.0% | 330 | 100 | 100 | 29 | 29 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 312 | 38.5% | 313 | 66 | 66 | 3 | 3 | 0 | 0 |

### Guard

- Draft Bot: `GuardDraftBot`
- Play Bot: `GuardBot`
- Win Rate: 46.5%
- First Pass Win Rate: 41.7%
- Starting Player Win Rate: 44.8%
- Responding Player Win Rate: 48.2%
- Action Rates: set=72.5%, set_pass=1.7%, pass=25.8%
- set_pass Candidate Avg / Match: 19.8373

| Opponent | Matches | Wins | Losses | Draws | Win Rate |
|---|---:|---:|---:|---:|---:|
| `Aggro` | 1000 | 455 | 478 | 67 | 45.5% |
| `Guard` | 2000 | 936 | 936 | 128 | 46.8% |
| `Standard` | 1000 | 469 | 462 | 69 | 46.9% |

#### Top Picked Cards

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 5095 | 1347 | 595 | 427 |
| 防御 | `battle_defend` | `common` | 5077 | 1541 | 675 | 345 |
| 圧迫 | `control_pressure` | `common` | 4822 | 1639 | 699 | 134 |
| ステップ | `battle_step` | `common` | 4628 | 1015 | 394 | 227 |
| 構え | `control_guard` | `common` | 4332 | 1225 | 545 | 147 |
| 集中 | `control_focus` | `common` | 4091 | 1099 | 433 | 141 |
| 牽制 | `control_disrupt` | `common` | 3955 | 1256 | 624 | 64 |
| 崩し | `battle_break` | `uncommon` | 2615 | 858 | 555 | 490 |
| 貫き | `battle_pierce` | `uncommon` | 2575 | 863 | 523 | 461 |
| 返し刃 | `battle_counter` | `uncommon` | 2208 | 749 | 367 | 251 |
| 踏ん張り | `battle_brace` | `uncommon` | 2168 | 772 | 386 | 210 |
| 十字受け | `battle_cross_guard` | `uncommon` | 2120 | 780 | 373 | 212 |
| Bastion | `battle_bastion` | `uncommon` | 2008 | 762 | 333 | 102 |
| 粉砕 | `battle_crush` | `uncommon` | 1965 | 564 | 301 | 264 |
| 踏み込み | `battle_step_in` | `rare` | 1798 | 649 | 463 | 439 |

#### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 速の加護 | `blessing_speed` | 418 | 44.7% | 425 | 114 | 114 | 0 | 0 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 412 | 45.6% | 415 | 149 | 149 | 30 | 30 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 381 | 45.1% | 387 | 76 | 76 | 76 | 0 | 0 | 76 |
| 鈍足の加護 | `blessing_slow` | 373 | 47.2% | 375 | 82 | 82 | 12 | 12 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 369 | 43.1% | 370 | 99 | 99 | 22 | 22 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 368 | 43.8% | 369 | 114 | 114 | 0 | 0 | 0 | 0 |
| 防の加護 | `blessing_guard` | 365 | 47.1% | 366 | 93 | 93 | 0 | 0 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 362 | 47.2% | 364 | 94 | 94 | 29 | 29 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 359 | 39.3% | 360 | 69 | 69 | 6 | 6 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 356 | 48.6% | 357 | 72 | 72 | 0 | 0 | 0 | 0 |

### Standard

- Draft Bot: `StandardDraftBot`
- Play Bot: `StandardBot`
- Win Rate: 46.3%
- First Pass Win Rate: 43.2%
- Starting Player Win Rate: 44.0%
- Responding Player Win Rate: 48.6%
- Action Rates: set=72.3%, set_pass=2.1%, pass=25.6%
- set_pass Candidate Avg / Match: 16.6417

| Opponent | Matches | Wins | Losses | Draws | Win Rate |
|---|---:|---:|---:|---:|---:|
| `Aggro` | 1000 | 468 | 474 | 58 | 46.8% |
| `Guard` | 1000 | 462 | 469 | 69 | 46.2% |
| `Standard` | 2000 | 922 | 922 | 156 | 46.1% |

#### Top Picked Cards

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 5055 | 1399 | 602 | 425 |
| 防御 | `battle_defend` | `common` | 4923 | 1388 | 587 | 300 |
| 圧迫 | `control_pressure` | `common` | 4845 | 1512 | 644 | 125 |
| ステップ | `battle_step` | `common` | 4764 | 1270 | 511 | 317 |
| 構え | `control_guard` | `common` | 4357 | 1247 | 523 | 144 |
| 牽制 | `control_disrupt` | `common` | 4033 | 1192 | 550 | 43 |
| 集中 | `control_focus` | `common` | 4023 | 1107 | 420 | 143 |
| 貫き | `battle_pierce` | `uncommon` | 2701 | 852 | 506 | 462 |
| 崩し | `battle_break` | `uncommon` | 2665 | 828 | 506 | 453 |
| 返し刃 | `battle_counter` | `uncommon` | 2181 | 691 | 365 | 265 |
| 粉砕 | `battle_crush` | `uncommon` | 2078 | 681 | 335 | 284 |
| 踏ん張り | `battle_brace` | `uncommon` | 2063 | 680 | 308 | 199 |
| 十字受け | `battle_cross_guard` | `uncommon` | 2042 | 675 | 350 | 192 |
| Bastion | `battle_bastion` | `uncommon` | 1827 | 594 | 247 | 92 |
| 強撃 | `battle_power_attack` | `uncommon` | 1747 | 539 | 262 | 218 |

#### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 速の加護 | `blessing_speed` | 426 | 49.1% | 429 | 92 | 92 | 0 | 0 | 0 | 0 |
| 防の加護 | `blessing_guard` | 420 | 49.8% | 422 | 100 | 100 | 0 | 0 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 403 | 42.7% | 407 | 105 | 105 | 28 | 28 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 394 | 43.7% | 395 | 110 | 110 | 0 | 0 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 380 | 41.1% | 381 | 118 | 118 | 23 | 23 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 374 | 44.9% | 379 | 74 | 74 | 74 | 0 | 0 | 74 |
| 抑制の加護 | `blessing_suppression` | 368 | 42.9% | 369 | 75 | 75 | 5 | 5 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 356 | 51.1% | 357 | 86 | 86 | 10 | 10 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 346 | 40.8% | 346 | 91 | 91 | 0 | 0 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 327 | 48.3% | 329 | 81 | 81 | 24 | 24 | 0 | 0 |
