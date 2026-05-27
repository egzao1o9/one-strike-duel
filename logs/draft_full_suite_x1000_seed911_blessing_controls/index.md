# Public-Info Draft Bot Suite

## Configuration

- Matches Per Matchup: 1000
- Seed: 911
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
| `AggroDraftBot` vs `AggroDraftBot` | 1000 | `Aggro` 46.6% | 68 | [aggro_vs_aggro](./aggro_vs_aggro/summary.md) | [jsonl](./aggro_vs_aggro/match_records.jsonl) |
| `AggroDraftBot` vs `GuardDraftBot` | 1000 | `Aggro` 49.4%, `Guard` 44.7% | 59 | [aggro_vs_guard](./aggro_vs_guard/summary.md) | [jsonl](./aggro_vs_guard/match_records.jsonl) |
| `GuardDraftBot` vs `GuardDraftBot` | 1000 | `Guard` 47.4% | 52 | [guard_vs_guard](./guard_vs_guard/summary.md) | [jsonl](./guard_vs_guard/match_records.jsonl) |
| `StandardDraftBot` vs `AggroDraftBot` | 1000 | `Aggro` 47.5%, `Standard` 47.3% | 52 | [standard_vs_aggro](./standard_vs_aggro/summary.md) | [jsonl](./standard_vs_aggro/match_records.jsonl) |
| `StandardDraftBot` vs `GuardDraftBot` | 1000 | `Guard` 47.9%, `Standard` 46.4% | 57 | [standard_vs_guard](./standard_vs_guard/summary.md) | [jsonl](./standard_vs_guard/match_records.jsonl) |
| `StandardDraftBot` vs `StandardDraftBot` | 1000 | `Standard` 47.6% | 48 | [standard_vs_standard](./standard_vs_standard/summary.md) | [jsonl](./standard_vs_standard/match_records.jsonl) |

## Bot Summary

| Bot | Draft | Play | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Aggro` | `AggroDraftBot` | `AggroBot` | 4000 | 1901 | 1852 | 247 | 47.5% | 49.1% | 16.4% | 52.2% | 31.4% | 47.5% | 47.5% | 70.5% | 2.8% | 26.7% |
| `Guard` | `GuardDraftBot` | `GuardBot` | 4000 | 1874 | 1906 | 220 | 46.9% | 44.5% | 16.8% | 52.6% | 30.6% | 47.0% | 46.7% | 71.1% | 2.1% | 26.8% |
| `Standard` | `StandardDraftBot` | `StandardBot` | 4000 | 1889 | 1906 | 205 | 47.2% | 48.8% | 14.8% | 53.0% | 32.2% | 47.0% | 47.5% | 70.8% | 2.6% | 26.6% |
## Bot Details

### Aggro

- Draft Bot: `AggroDraftBot`
- Play Bot: `AggroBot`
- Win Rate: 47.5%
- First Pass Win Rate: 49.1%
- Starting Player Win Rate: 47.5%
- Responding Player Win Rate: 47.5%
- Action Rates: set=70.5%, set_pass=2.8%, pass=26.7%
- set_pass Candidate Avg / Match: 15.264

| Opponent | Matches | Wins | Losses | Draws | Win Rate |
|---|---:|---:|---:|---:|---:|
| `Aggro` | 2000 | 932 | 932 | 136 | 46.6% |
| `Guard` | 1000 | 494 | 447 | 59 | 49.4% |
| `Standard` | 1000 | 475 | 473 | 52 | 47.5% |

#### Top Picked Cards

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 4166 | 1263 | 584 | 416 |
| 防御 | `battle_defend` | `common` | 3801 | 1117 | 476 | 252 |
| ステップ | `battle_step` | `common` | 3762 | 1068 | 480 | 287 |
| 圧迫 | `control_pressure` | `common` | 3217 | 989 | 465 | 110 |
| 見定め | `control_peek_own_top` | `common` | 2895 | 871 | 334 | 83 |
| 集中 | `control_focus` | `common` | 2885 | 760 | 293 | 121 |
| 構え | `control_guard` | `common` | 2875 | 811 | 348 | 118 |
| 牽制 | `control_disrupt` | `common` | 2874 | 918 | 440 | 33 |
| 遠眼 | `control_peek_opponent_top` | `common` | 2819 | 799 | 328 | 102 |
| 公開勝負 | `control_opening_expose` | `common` | 2706 | 794 | 324 | 121 |
| 崩し | `battle_break` | `uncommon` | 1789 | 586 | 384 | 361 |
| 貫き | `battle_pierce` | `uncommon` | 1720 | 550 | 379 | 335 |
| 踏み込み | `battle_step_in` | `rare` | 1567 | 560 | 424 | 397 |
| 粉砕 | `battle_crush` | `uncommon` | 1561 | 533 | 299 | 270 |
| 返し刃 | `battle_counter` | `uncommon` | 1516 | 502 | 300 | 218 |

#### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 受け流しの加護 | `blessing_parry` | 570 | 43.2% | 580 | 142 | 140 | 23 | 23 | 0 | 0 |
| 小太刀の加護 | `blessing_shortblade` | 566 | 48.6% | 576 | 92 | 91 | 14 | 14 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 566 | 43.6% | 570 | 99 | 97 | 6 | 6 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 550 | 43.1% | 559 | 132 | 132 | 47 | 47 | 0 | 0 |
| 追風の加護 | `blessing_tailwind` | 527 | 45.5% | 541 | 124 | 124 | 4 | 4 | 0 | 0 |
| 鈍りの加護 | `blessing_dullness` | 525 | 49.1% | 534 | 102 | 102 | 5 | 5 | 0 | 0 |
| 小盾の加護 | `blessing_buckler` | 520 | 47.5% | 525 | 96 | 96 | 14 | 14 | 0 | 0 |
| 間合いの加護 | `blessing_range` | 520 | 47.3% | 527 | 88 | 87 | 13 | 13 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 518 | 45.6% | 520 | 111 | 108 | 0 | 0 | 0 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | 490 | 48.2% | 498 | 137 | 136 | 26 | 26 | 0 | 0 |
| 速の加護 | `blessing_speed` | 483 | 43.9% | 488 | 112 | 109 | 2 | 2 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 477 | 47.0% | 479 | 148 | 146 | 27 | 27 | 0 | 0 |
| 防の加護 | `blessing_guard` | 468 | 50.9% | 470 | 104 | 103 | 3 | 3 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 464 | 45.7% | 469 | 121 | 118 | 28 | 28 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 435 | 44.1% | 436 | 87 | 84 | 6 | 6 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 413 | 42.9% | 415 | 65 | 63 | 64 | 64 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 241 | 45.6% | 241 | 76 | 76 | 1 | 1 | 0 | 0 |

### Guard

- Draft Bot: `GuardDraftBot`
- Play Bot: `GuardBot`
- Win Rate: 46.9%
- First Pass Win Rate: 44.5%
- Starting Player Win Rate: 47.0%
- Responding Player Win Rate: 46.7%
- Action Rates: set=71.1%, set_pass=2.1%, pass=26.8%
- set_pass Candidate Avg / Match: 17.2542

| Opponent | Matches | Wins | Losses | Draws | Win Rate |
|---|---:|---:|---:|---:|---:|
| `Aggro` | 1000 | 447 | 494 | 59 | 44.7% |
| `Guard` | 2000 | 948 | 948 | 104 | 47.4% |
| `Standard` | 1000 | 479 | 464 | 57 | 47.9% |

#### Top Picked Cards

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 4077 | 1163 | 521 | 375 |
| 防御 | `battle_defend` | `common` | 3948 | 1293 | 551 | 275 |
| ステップ | `battle_step` | `common` | 3551 | 922 | 370 | 222 |
| 圧迫 | `control_pressure` | `common` | 3220 | 1031 | 472 | 97 |
| 構え | `control_guard` | `common` | 3071 | 918 | 393 | 153 |
| 遠眼 | `control_peek_opponent_top` | `common` | 2921 | 992 | 401 | 96 |
| 見定め | `control_peek_own_top` | `common` | 2837 | 977 | 408 | 86 |
| 集中 | `control_focus` | `common` | 2802 | 756 | 311 | 144 |
| 公開勝負 | `control_opening_expose` | `common` | 2794 | 777 | 322 | 124 |
| 牽制 | `control_disrupt` | `common` | 2779 | 862 | 432 | 29 |
| 貫き | `battle_pierce` | `uncommon` | 1730 | 547 | 367 | 346 |
| 崩し | `battle_break` | `uncommon` | 1699 | 543 | 363 | 336 |
| 十字受け | `battle_cross_guard` | `uncommon` | 1582 | 610 | 317 | 150 |
| 踏み込み | `battle_step_in` | `rare` | 1510 | 531 | 398 | 368 |
| 踏ん張り | `battle_brace` | `uncommon` | 1500 | 580 | 311 | 205 |

#### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 攻勢の加護 | `blessing_offense` | 568 | 45.1% | 575 | 170 | 168 | 67 | 67 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 557 | 48.3% | 573 | 125 | 125 | 0 | 0 | 0 | 0 |
| 受け流しの加護 | `blessing_parry` | 552 | 44.6% | 561 | 135 | 133 | 18 | 18 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 551 | 45.4% | 554 | 50 | 49 | 3 | 3 | 0 | 0 |
| 間合いの加護 | `blessing_range` | 547 | 44.8% | 557 | 50 | 50 | 9 | 9 | 0 | 0 |
| 鈍りの加護 | `blessing_dullness` | 535 | 44.9% | 543 | 104 | 103 | 7 | 7 | 0 | 0 |
| 追風の加護 | `blessing_tailwind` | 533 | 47.1% | 541 | 127 | 125 | 12 | 12 | 0 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | 524 | 46.4% | 536 | 146 | 142 | 28 | 28 | 0 | 0 |
| 小盾の加護 | `blessing_buckler` | 506 | 45.7% | 510 | 134 | 134 | 30 | 30 | 0 | 0 |
| 小太刀の加護 | `blessing_shortblade` | 501 | 47.3% | 512 | 109 | 108 | 26 | 26 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 490 | 45.7% | 493 | 136 | 131 | 36 | 36 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 469 | 44.1% | 478 | 61 | 61 | 64 | 64 | 0 | 0 |
| 速の加護 | `blessing_speed` | 461 | 43.6% | 465 | 105 | 104 | 1 | 1 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 454 | 54.0% | 461 | 125 | 124 | 16 | 16 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 450 | 44.4% | 455 | 93 | 88 | 9 | 9 | 0 | 0 |
| 防の加護 | `blessing_guard` | 420 | 47.9% | 422 | 97 | 95 | 2 | 2 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 212 | 47.2% | 212 | 65 | 64 | 3 | 3 | 0 | 0 |

### Standard

- Draft Bot: `StandardDraftBot`
- Play Bot: `StandardBot`
- Win Rate: 47.2%
- First Pass Win Rate: 48.8%
- Starting Player Win Rate: 47.0%
- Responding Player Win Rate: 47.5%
- Action Rates: set=70.8%, set_pass=2.6%, pass=26.6%
- set_pass Candidate Avg / Match: 14.8522

| Opponent | Matches | Wins | Losses | Draws | Win Rate |
|---|---:|---:|---:|---:|---:|
| `Aggro` | 1000 | 473 | 475 | 52 | 47.3% |
| `Guard` | 1000 | 464 | 479 | 57 | 46.4% |
| `Standard` | 2000 | 952 | 952 | 96 | 47.6% |

#### Top Picked Cards

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 4047 | 1172 | 541 | 393 |
| 防御 | `battle_defend` | `common` | 3822 | 1117 | 506 | 255 |
| ステップ | `battle_step` | `common` | 3659 | 1067 | 448 | 271 |
| 圧迫 | `control_pressure` | `common` | 3299 | 1014 | 469 | 99 |
| 構え | `control_guard` | `common` | 3042 | 900 | 430 | 158 |
| 集中 | `control_focus` | `common` | 2911 | 793 | 358 | 161 |
| 公開勝負 | `control_opening_expose` | `common` | 2841 | 845 | 325 | 118 |
| 遠眼 | `control_peek_opponent_top` | `common` | 2833 | 864 | 350 | 91 |
| 見定め | `control_peek_own_top` | `common` | 2823 | 902 | 347 | 88 |
| 牽制 | `control_disrupt` | `common` | 2723 | 850 | 412 | 36 |
| 崩し | `battle_break` | `uncommon` | 1719 | 538 | 355 | 314 |
| 貫き | `battle_pierce` | `uncommon` | 1717 | 557 | 376 | 340 |
| 返し刃 | `battle_counter` | `uncommon` | 1546 | 496 | 284 | 218 |
| 渾身 | `battle_all_in` | `rare` | 1520 | 540 | 259 | 251 |
| 粉砕 | `battle_crush` | `uncommon` | 1515 | 510 | 300 | 267 |

#### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 間合いの加護 | `blessing_range` | 560 | 45.5% | 568 | 56 | 55 | 9 | 9 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 555 | 45.0% | 568 | 122 | 119 | 1 | 1 | 0 | 0 |
| 小太刀の加護 | `blessing_shortblade` | 547 | 43.9% | 558 | 117 | 115 | 17 | 17 | 0 | 0 |
| 受け流しの加護 | `blessing_parry` | 541 | 49.7% | 552 | 124 | 123 | 25 | 25 | 0 | 0 |
| 小盾の加護 | `blessing_buckler` | 538 | 44.8% | 547 | 120 | 116 | 18 | 18 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 538 | 43.7% | 544 | 74 | 73 | 2 | 2 | 0 | 0 |
| 追風の加護 | `blessing_tailwind` | 531 | 46.5% | 536 | 94 | 94 | 3 | 3 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 522 | 44.6% | 525 | 130 | 127 | 37 | 37 | 0 | 0 |
| 鈍りの加護 | `blessing_dullness` | 515 | 43.9% | 521 | 84 | 84 | 4 | 4 | 0 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | 514 | 44.6% | 524 | 132 | 128 | 25 | 25 | 0 | 0 |
| 防の加護 | `blessing_guard` | 492 | 47.6% | 496 | 102 | 100 | 0 | 0 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 477 | 48.6% | 480 | 139 | 137 | 20 | 20 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 458 | 44.3% | 463 | 69 | 68 | 68 | 68 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 453 | 49.4% | 458 | 127 | 126 | 41 | 41 | 0 | 0 |
| 速の加護 | `blessing_speed` | 450 | 50.7% | 453 | 96 | 95 | 1 | 1 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 449 | 49.7% | 452 | 107 | 107 | 19 | 19 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 232 | 47.4% | 232 | 65 | 63 | 1 | 1 | 0 | 0 |
