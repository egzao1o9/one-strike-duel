# Public-Info Draft Bot Suite

## Configuration

- Matches Per Matchup: 1000
- Seed: 541
- Archetypes: `Standard`, `Aggro`, `Guard`
- Pairings: all combinations with replacement, mirrored by seat
- Per-match records: `match_records.jsonl` in each matchup directory

## Matchups

| Matchup | Matches | Ranking | Draws | Summary | Records |
|---|---:|---|---:|---|---|
| `AggroDraftBot` vs `AggroDraftBot` | 1000 | `Aggro` 43.7% | 126 | [aggro_vs_aggro](./aggro_vs_aggro/summary.md) | [jsonl](./aggro_vs_aggro/match_records.jsonl) |
| `AggroDraftBot` vs `GuardDraftBot` | 1000 | `Aggro` 45.1%, `Guard` 43.8% | 111 | [aggro_vs_guard](./aggro_vs_guard/summary.md) | [jsonl](./aggro_vs_guard/match_records.jsonl) |
| `GuardDraftBot` vs `GuardDraftBot` | 1000 | `Guard` 45.9% | 83 | [guard_vs_guard](./guard_vs_guard/summary.md) | [jsonl](./guard_vs_guard/match_records.jsonl) |
| `StandardDraftBot` vs `AggroDraftBot` | 1000 | `Aggro` 45.0%, `Standard` 43.9% | 111 | [standard_vs_aggro](./standard_vs_aggro/summary.md) | [jsonl](./standard_vs_aggro/match_records.jsonl) |
| `StandardDraftBot` vs `GuardDraftBot` | 1000 | `Guard` 44.9%, `Standard` 44.6% | 105 | [standard_vs_guard](./standard_vs_guard/summary.md) | [jsonl](./standard_vs_guard/match_records.jsonl) |
| `StandardDraftBot` vs `StandardDraftBot` | 1000 | `Standard` 44.9% | 102 | [standard_vs_standard](./standard_vs_standard/summary.md) | [jsonl](./standard_vs_standard/match_records.jsonl) |

## Bot Summary

| Bot | Draft | Play | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Aggro` | `AggroDraftBot` | `AggroBot` | 4000 | 1775 | 1751 | 474 | 44.4% | 35.4% | 38.0% | 0.6% | 61.4% | 35.5% | 52.6% | 34.0% | 32.6% | 33.4% |
| `Guard` | `GuardDraftBot` | `GuardBot` | 4000 | 1804 | 1814 | 382 | 45.1% | 32.4% | 36.4% | 1.3% | 62.4% | 32.4% | 58.4% | 32.5% | 34.4% | 33.2% |
| `Standard` | `StandardDraftBot` | `StandardBot` | 4000 | 1783 | 1797 | 420 | 44.6% | 35.1% | 40.0% | 0.4% | 59.6% | 35.3% | 54.2% | 33.0% | 34.1% | 33.0% |

## Global Priority Picks

#### Most Picked Overall

| Rank | Card ID | Count |
|---:|---|---:|
| 1 | `battle_pierce` | 10995 |
| 2 | `battle_break` | 10984 |
| 3 | `battle_cross_guard` | 10647 |
| 4 | `battle_counter` | 10625 |
| 5 | `battle_brace` | 10537 |
| 6 | `battle_crush` | 10515 |
| 7 | `battle_backstep` | 9966 |
| 8 | `battle_guard` | 9713 |
| 9 | `control_cover` | 9680 |
| 10 | `battle_feint` | 9668 |
| 11 | `battle_low_stance` | 9613 |
| 12 | `battle_power_attack` | 9388 |
| 13 | `battle_press` | 9309 |
| 14 | `control_overclock` | 9248 |
| 15 | `control_anchor` | 8782 |

#### Hidden Pick Priority

| Rank | Card ID | Offered | Picked | Pick Rate |
|---:|---|---:|---:|---:|
| 1 | `battle_step_in` | 2208 | 2208 | 100.0% |
| 2 | `battle_all_in` | 2165 | 2120 | 97.9% |
| 3 | `battle_heavy_swing` | 2256 | 2154 | 95.5% |
| 4 | `battle_afterimage` | 2218 | 2042 | 92.1% |
| 5 | `battle_wall` | 2284 | 2100 | 91.9% |
| 6 | `battle_break` | 4622 | 3933 | 85.1% |
| 7 | `battle_pierce` | 4643 | 3950 | 85.1% |
| 8 | `battle_dash` | 2368 | 1935 | 81.7% |
| 9 | `battle_crush` | 5112 | 3615 | 70.7% |
| 10 | `battle_counter` | 5186 | 3533 | 68.1% |
| 11 | `battle_brace` | 5126 | 3413 | 66.6% |
| 12 | `battle_cross_guard` | 5372 | 3532 | 65.8% |
| 13 | `battle_feint` | 6114 | 3755 | 61.4% |
| 14 | `battle_backstep` | 6039 | 3162 | 52.4% |
| 15 | `control_reserve` | 3256 | 1635 | 50.2% |

#### Public First-Pick Priority

| Rank | Card ID | Offered | Picked | Pick Rate |
|---:|---|---:|---:|---:|
| 1 | `battle_step_in` | 3419 | 3419 | 100.0% |
| 2 | `battle_all_in` | 3481 | 3317 | 95.3% |
| 3 | `battle_heavy_swing` | 3425 | 3141 | 91.7% |
| 4 | `battle_wall` | 3501 | 3101 | 88.6% |
| 5 | `battle_afterimage` | 3593 | 2816 | 78.4% |
| 6 | `battle_break` | 7233 | 5434 | 75.1% |
| 7 | `battle_pierce` | 7230 | 5416 | 74.9% |
| 8 | `battle_dash` | 3687 | 2578 | 69.9% |
| 9 | `battle_counter` | 8058 | 4187 | 52.0% |
| 10 | `battle_crush` | 7962 | 4063 | 51.0% |
| 11 | `battle_brace` | 8254 | 4136 | 50.1% |
| 12 | `battle_cross_guard` | 8385 | 3942 | 47.0% |
| 13 | `battle_backstep` | 9387 | 3002 | 32.0% |
| 14 | `battle_power_attack` | 9456 | 2850 | 30.1% |
| 15 | `control_reserve` | 5237 | 1534 | 29.3% |

#### Public Second-Pick Priority

| Rank | Card ID | Offered | Picked | Pick Rate |
|---:|---|---:|---:|---:|
| 1 | `battle_all_in` | 164 | 162 | 98.8% |
| 2 | `battle_wall` | 400 | 389 | 97.2% |
| 3 | `battle_heavy_swing` | 284 | 276 | 97.2% |
| 4 | `battle_afterimage` | 777 | 715 | 92.0% |
| 5 | `battle_break` | 1799 | 1617 | 89.9% |
| 6 | `battle_pierce` | 1814 | 1629 | 89.8% |
| 7 | `battle_dash` | 1109 | 940 | 84.8% |
| 8 | `battle_counter` | 3871 | 2905 | 75.0% |
| 9 | `battle_crush` | 3899 | 2837 | 72.8% |
| 10 | `battle_brace` | 4118 | 2988 | 72.6% |
| 11 | `battle_cross_guard` | 4443 | 3173 | 71.4% |
| 12 | `battle_backstep` | 6385 | 3802 | 59.6% |
| 13 | `battle_power_attack` | 6606 | 3561 | 53.9% |
| 14 | `battle_press` | 6863 | 3641 | 53.0% |
| 15 | `battle_guard` | 7775 | 4027 | 51.8% |

## Bot Details

### Aggro

- Draft Bot: `AggroDraftBot`
- Play Bot: `AggroBot`
- Win Rate: 44.4%
- First Pass Win Rate: 35.4%
- Starting Player Win Rate: 35.5%
- Responding Player Win Rate: 52.6%
- Action Rates: set=34.0%, set_pass=32.6%, pass=33.4%

| Opponent | Matches | Wins | Losses | Draws | Win Rate |
|---|---:|---:|---:|---:|---:|
| `Aggro` | 2000 | 874 | 874 | 252 | 43.7% |
| `Guard` | 1000 | 451 | 438 | 111 | 45.1% |
| `Standard` | 1000 | 450 | 439 | 111 | 45.0% |

#### Most Picked

| Rank | Card ID | Count |
|---:|---|---:|
| 1 | `battle_crush` | 3717 |
| 2 | `battle_pierce` | 3704 |
| 3 | `battle_break` | 3603 |
| 4 | `battle_counter` | 3508 |
| 5 | `battle_feint` | 3451 |
| 6 | `battle_cross_guard` | 3383 |
| 7 | `battle_brace` | 3376 |
| 8 | `battle_power_attack` | 3266 |
| 9 | `battle_backstep` | 3264 |
| 10 | `battle_guard` | 3252 |
| 11 | `control_cover` | 3131 |
| 12 | `control_overclock` | 3077 |
| 13 | `battle_press` | 3059 |
| 14 | `battle_low_stance` | 2991 |
| 15 | `control_anchor` | 2819 |

#### Hidden Priority

| Rank | Card ID | Offered | Picked | Pick Rate |
|---:|---|---:|---:|---:|
| 1 | `battle_step_in` | 746 | 746 | 100.0% |
| 2 | `battle_all_in` | 698 | 685 | 98.1% |
| 3 | `battle_heavy_swing` | 791 | 765 | 96.7% |
| 4 | `battle_afterimage` | 731 | 682 | 93.3% |
| 5 | `battle_wall` | 776 | 710 | 91.5% |
| 6 | `battle_pierce` | 1553 | 1330 | 85.6% |
| 7 | `battle_break` | 1614 | 1358 | 84.1% |
| 8 | `battle_dash` | 800 | 660 | 82.5% |
| 9 | `battle_crush` | 1629 | 1209 | 74.2% |
| 10 | `battle_feint` | 1976 | 1362 | 68.9% |
| 11 | `battle_counter` | 1748 | 1173 | 67.1% |
| 12 | `battle_brace` | 1722 | 1084 | 62.9% |
| 13 | `battle_cross_guard` | 1783 | 1069 | 60.0% |
| 14 | `control_reserve` | 1078 | 548 | 50.8% |
| 15 | `battle_backstep` | 2040 | 1023 | 50.1% |

#### Public First-Pick Priority

| Rank | Card ID | Offered | Picked | Pick Rate |
|---:|---|---:|---:|---:|
| 1 | `battle_step_in` | 1118 | 1118 | 100.0% |
| 2 | `battle_all_in` | 1174 | 1128 | 96.1% |
| 3 | `battle_heavy_swing` | 1115 | 1031 | 92.5% |
| 4 | `battle_wall` | 1176 | 1009 | 85.8% |
| 5 | `battle_afterimage` | 1186 | 994 | 83.8% |
| 6 | `battle_pierce` | 2471 | 1850 | 74.9% |
| 7 | `battle_break` | 2353 | 1714 | 72.8% |
| 8 | `battle_dash` | 1213 | 874 | 72.0% |
| 9 | `battle_crush` | 2650 | 1518 | 57.3% |
| 10 | `battle_counter` | 2706 | 1391 | 51.4% |
| 11 | `battle_brace` | 2811 | 1309 | 46.6% |
| 12 | `battle_cross_guard` | 2901 | 1225 | 42.2% |
| 13 | `battle_power_attack` | 3074 | 1027 | 33.4% |
| 14 | `battle_backstep` | 3189 | 979 | 30.7% |
| 15 | `control_reserve` | 1772 | 543 | 30.6% |

#### Top Picked Cards

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 粉砕 | `battle_crush` | `uncommon` | 3717 | 1215 | 494 | 484 |
| 貫き | `battle_pierce` | `uncommon` | 3704 | 292 | 175 | 175 |
| 崩し | `battle_break` | `uncommon` | 3603 | 319 | 193 | 191 |
| 返し刃 | `battle_counter` | `uncommon` | 3508 | 600 | 352 | 340 |
| フェイント | `battle_feint` | `uncommon` | 3451 | 4 | 1 | 1 |
| 十字受け | `battle_cross_guard` | `uncommon` | 3383 | 83 | 54 | 50 |
| 踏ん張り | `battle_brace` | `uncommon` | 3376 | 80 | 39 | 38 |
| 強撃 | `battle_power_attack` | `uncommon` | 3266 | 604 | 284 | 278 |
| 退き足 | `battle_backstep` | `uncommon` | 3264 | 4 | 1 | 1 |
| 受け流し | `battle_guard` | `uncommon` | 3252 | 7 | 2 | 2 |
| 受け直し | `control_cover` | `uncommon` | 3131 | 505 | 279 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 3077 | 618 | 338 | 0 |
| 押し込み | `battle_press` | `uncommon` | 3059 | 118 | 55 | 53 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 2991 | 1 | 0 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 2819 | 151 | 95 | 0 |

### Guard

- Draft Bot: `GuardDraftBot`
- Play Bot: `GuardBot`
- Win Rate: 45.1%
- First Pass Win Rate: 32.4%
- Starting Player Win Rate: 32.4%
- Responding Player Win Rate: 58.4%
- Action Rates: set=32.5%, set_pass=34.4%, pass=33.2%

| Opponent | Matches | Wins | Losses | Draws | Win Rate |
|---|---:|---:|---:|---:|---:|
| `Aggro` | 1000 | 438 | 451 | 111 | 43.8% |
| `Guard` | 2000 | 917 | 917 | 166 | 45.9% |
| `Standard` | 1000 | 449 | 446 | 105 | 44.9% |

#### Most Picked

| Rank | Card ID | Count |
|---:|---|---:|
| 1 | `battle_break` | 3730 |
| 2 | `battle_cross_guard` | 3727 |
| 3 | `battle_brace` | 3668 |
| 4 | `battle_pierce` | 3608 |
| 5 | `battle_counter` | 3596 |
| 6 | `battle_low_stance` | 3439 |
| 7 | `battle_backstep` | 3345 |
| 8 | `battle_guard` | 3274 |
| 9 | `battle_crush` | 3271 |
| 10 | `control_cover` | 3270 |
| 11 | `battle_press` | 3197 |
| 12 | `control_overclock` | 3062 |
| 13 | `battle_feint` | 3008 |
| 14 | `control_anchor` | 2975 |
| 15 | `battle_power_attack` | 2948 |

#### Hidden Priority

| Rank | Card ID | Offered | Picked | Pick Rate |
|---:|---|---:|---:|---:|
| 1 | `battle_step_in` | 771 | 771 | 100.0% |
| 2 | `battle_all_in` | 754 | 736 | 97.6% |
| 3 | `battle_heavy_swing` | 739 | 702 | 95.0% |
| 4 | `battle_wall` | 742 | 685 | 92.3% |
| 5 | `battle_afterimage` | 727 | 650 | 89.4% |
| 6 | `battle_pierce` | 1585 | 1334 | 84.2% |
| 7 | `battle_break` | 1519 | 1275 | 83.9% |
| 8 | `battle_dash` | 805 | 659 | 81.9% |
| 9 | `battle_cross_guard` | 1762 | 1245 | 70.7% |
| 10 | `battle_brace` | 1701 | 1189 | 69.9% |
| 11 | `battle_counter` | 1720 | 1183 | 68.8% |
| 12 | `battle_crush` | 1794 | 1210 | 67.5% |
| 13 | `battle_backstep` | 1987 | 1080 | 54.4% |
| 14 | `battle_feint` | 2140 | 1156 | 54.0% |
| 15 | `control_reserve` | 1119 | 545 | 48.7% |

#### Public First-Pick Priority

| Rank | Card ID | Offered | Picked | Pick Rate |
|---:|---|---:|---:|---:|
| 1 | `battle_step_in` | 1153 | 1153 | 100.0% |
| 2 | `battle_all_in` | 1121 | 1053 | 93.9% |
| 3 | `battle_wall` | 1161 | 1054 | 90.8% |
| 4 | `battle_heavy_swing` | 1132 | 1023 | 90.4% |
| 5 | `battle_break` | 2448 | 1896 | 77.5% |
| 6 | `battle_pierce` | 2340 | 1743 | 74.5% |
| 7 | `battle_afterimage` | 1176 | 874 | 74.3% |
| 8 | `battle_dash` | 1212 | 860 | 71.0% |
| 9 | `battle_brace` | 2688 | 1454 | 54.1% |
| 10 | `battle_counter` | 2721 | 1443 | 53.0% |
| 11 | `battle_cross_guard` | 2749 | 1412 | 51.4% |
| 12 | `battle_crush` | 2678 | 1168 | 43.6% |
| 13 | `battle_backstep` | 3070 | 1019 | 33.2% |
| 14 | `battle_press` | 3235 | 991 | 30.6% |
| 15 | `control_reserve` | 1733 | 489 | 28.2% |

#### Top Picked Cards

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 崩し | `battle_break` | `uncommon` | 3730 | 47 | 32 | 32 |
| 十字受け | `battle_cross_guard` | `uncommon` | 3727 | 959 | 482 | 366 |
| 踏ん張り | `battle_brace` | `uncommon` | 3668 | 775 | 356 | 283 |
| 貫き | `battle_pierce` | `uncommon` | 3608 | 53 | 36 | 35 |
| 返し刃 | `battle_counter` | `uncommon` | 3596 | 774 | 425 | 367 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 3439 | 99 | 44 | 30 |
| 退き足 | `battle_backstep` | `uncommon` | 3345 | 19 | 7 | 3 |
| 受け流し | `battle_guard` | `uncommon` | 3274 | 77 | 28 | 21 |
| 粉砕 | `battle_crush` | `uncommon` | 3271 | 227 | 99 | 93 |
| 受け直し | `control_cover` | `uncommon` | 3270 | 570 | 297 | 0 |
| 押し込み | `battle_press` | `uncommon` | 3197 | 205 | 97 | 86 |
| 前のめり | `control_overclock` | `uncommon` | 3062 | 678 | 382 | 0 |
| フェイント | `battle_feint` | `uncommon` | 3008 | 0 | 0 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 2975 | 172 | 84 | 0 |
| 強撃 | `battle_power_attack` | `uncommon` | 2948 | 119 | 54 | 52 |

### Standard

- Draft Bot: `StandardDraftBot`
- Play Bot: `StandardBot`
- Win Rate: 44.6%
- First Pass Win Rate: 35.1%
- Starting Player Win Rate: 35.3%
- Responding Player Win Rate: 54.2%
- Action Rates: set=33.0%, set_pass=34.1%, pass=33.0%

| Opponent | Matches | Wins | Losses | Draws | Win Rate |
|---|---:|---:|---:|---:|---:|
| `Aggro` | 1000 | 439 | 450 | 111 | 43.9% |
| `Guard` | 1000 | 446 | 449 | 105 | 44.6% |
| `Standard` | 2000 | 898 | 898 | 204 | 44.9% |

#### Most Picked

| Rank | Card ID | Count |
|---:|---|---:|
| 1 | `battle_pierce` | 3683 |
| 2 | `battle_break` | 3651 |
| 3 | `battle_cross_guard` | 3537 |
| 4 | `battle_crush` | 3527 |
| 5 | `battle_counter` | 3521 |
| 6 | `battle_brace` | 3493 |
| 7 | `battle_backstep` | 3357 |
| 8 | `control_cover` | 3279 |
| 9 | `battle_feint` | 3209 |
| 10 | `battle_guard` | 3187 |
| 11 | `battle_low_stance` | 3183 |
| 12 | `battle_power_attack` | 3174 |
| 13 | `control_overclock` | 3109 |
| 14 | `battle_press` | 3053 |
| 15 | `control_anchor` | 2988 |

#### Hidden Priority

| Rank | Card ID | Offered | Picked | Pick Rate |
|---:|---|---:|---:|---:|
| 1 | `battle_step_in` | 691 | 691 | 100.0% |
| 2 | `battle_all_in` | 713 | 699 | 98.0% |
| 3 | `battle_heavy_swing` | 726 | 687 | 94.6% |
| 4 | `battle_afterimage` | 760 | 710 | 93.4% |
| 5 | `battle_wall` | 766 | 705 | 92.0% |
| 6 | `battle_break` | 1489 | 1300 | 87.3% |
| 7 | `battle_pierce` | 1505 | 1286 | 85.5% |
| 8 | `battle_dash` | 763 | 616 | 80.7% |
| 9 | `battle_crush` | 1689 | 1196 | 70.8% |
| 10 | `battle_counter` | 1718 | 1177 | 68.5% |
| 11 | `battle_brace` | 1703 | 1140 | 66.9% |
| 12 | `battle_cross_guard` | 1827 | 1218 | 66.7% |
| 13 | `battle_feint` | 1998 | 1237 | 61.9% |
| 14 | `battle_backstep` | 2012 | 1059 | 52.6% |
| 15 | `battle_power_attack` | 1981 | 1024 | 51.7% |

#### Public First-Pick Priority

| Rank | Card ID | Offered | Picked | Pick Rate |
|---:|---|---:|---:|---:|
| 1 | `battle_step_in` | 1148 | 1148 | 100.0% |
| 2 | `battle_all_in` | 1186 | 1136 | 95.8% |
| 3 | `battle_heavy_swing` | 1178 | 1087 | 92.3% |
| 4 | `battle_wall` | 1164 | 1038 | 89.2% |
| 5 | `battle_afterimage` | 1231 | 948 | 77.0% |
| 6 | `battle_pierce` | 2419 | 1823 | 75.4% |
| 7 | `battle_break` | 2432 | 1824 | 75.0% |
| 8 | `battle_dash` | 1262 | 844 | 66.9% |
| 9 | `battle_crush` | 2634 | 1377 | 52.3% |
| 10 | `battle_counter` | 2631 | 1353 | 51.4% |
| 11 | `battle_brace` | 2755 | 1373 | 49.8% |
| 12 | `battle_cross_guard` | 2735 | 1305 | 47.7% |
| 13 | `battle_backstep` | 3128 | 1004 | 32.1% |
| 14 | `battle_power_attack` | 3200 | 947 | 29.6% |
| 15 | `control_reserve` | 1732 | 502 | 29.0% |

#### Top Picked Cards

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 貫き | `battle_pierce` | `uncommon` | 3683 | 94 | 66 | 64 |
| 崩し | `battle_break` | `uncommon` | 3651 | 96 | 62 | 62 |
| 十字受け | `battle_cross_guard` | `uncommon` | 3537 | 501 | 254 | 215 |
| 粉砕 | `battle_crush` | `uncommon` | 3527 | 1012 | 421 | 404 |
| 返し刃 | `battle_counter` | `uncommon` | 3521 | 858 | 460 | 415 |
| 踏ん張り | `battle_brace` | `uncommon` | 3493 | 300 | 137 | 103 |
| 退き足 | `battle_backstep` | `uncommon` | 3357 | 2 | 2 | 2 |
| 受け直し | `control_cover` | `uncommon` | 3279 | 533 | 273 | 0 |
| フェイント | `battle_feint` | `uncommon` | 3209 | 2 | 0 | 0 |
| 受け流し | `battle_guard` | `uncommon` | 3187 | 15 | 9 | 7 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 3183 | 1 | 0 | 0 |
| 強撃 | `battle_power_attack` | `uncommon` | 3174 | 324 | 152 | 145 |
| 前のめり | `control_overclock` | `uncommon` | 3109 | 684 | 376 | 0 |
| 押し込み | `battle_press` | `uncommon` | 3053 | 100 | 54 | 45 |
| 重心落とし | `control_anchor` | `uncommon` | 2988 | 148 | 85 | 0 |
