# Draft Report

## Configuration

- Draft Bot 1: `StandardDraftBot`
- Draft Bot 2: `GuardDraftBot`
- Play Bot 1: `StandardBot`
- Play Bot 2: `GuardBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 3891
- Pool: `base_pool` (95 copies)
- Pairing Mode: mirrored seats per round
- Draft Mode: `full`
- Fast Report: on
- Lean Draft Logging: on
- Save Battle Logs: on
- Draft Flow: normal public pack + normal hidden pack, then public rare + hidden rare, with order swapped in second half

## Drafter Summary

| Drafter | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Winner Set Avg | Loser Set Avg | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate | Battle Avg | Control Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `GuardDraftBot` | 1000 | 469 | 462 | 69 | 46.9% | 39.3% | 24.7% | 36.5% | 38.8% | 3 | 2.73 | 46.0% | 47.8% | 71.2% | 2.0% | 26.8% | 13.86 | 6.14 | 6.89 | 3.44 | 3.53 | 6.14 | 8 | 8 | 4 |
| `StandardDraftBot` | 1000 | 462 | 469 | 69 | 46.2% | 41.6% | 20.8% | 35.9% | 43.3% | 2.95 | 2.86 | 46.0% | 46.4% | 70.4% | 2.3% | 27.2% | 13.83 | 6.17 | 7.14 | 3.38 | 3.31 | 6.17 | 8 | 8 | 4 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| GuardDraftBot vs StandardDraftBot | 1000 | 69 | `GuardDraftBot`=469, `StandardDraftBot`=462 | 1.43 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 604 |
| 2 | 防御 | 599 |
| 3 | 圧迫 | 544 |
| 4 | 牽制 | 508 |
| 5 | 踏み込み | 497 |
| 6 | ステップ | 477 |
| 7 | 渾身 | 388 |
| 8 | 崩し | 379 |
| 9 | 鉄壁 | 377 |
| 10 | 大振り | 377 |
| 11 | 貫き | 360 |
| 12 | 返し刃 | 325 |
| 13 | 踏ん張り | 306 |
| 14 | 残像 | 301 |
| 15 | 構え | 297 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 334 |
| 2 | 防御 | 259 |
| 3 | 攻撃 | 258 |
| 4 | 牽制 | 250 |
| 5 | 圧迫 | 239 |
| 6 | 崩し | 230 |
| 7 | 貫き | 200 |
| 8 | 鉄壁 | 184 |
| 9 | ステップ | 180 |
| 10 | 渾身 | 171 |
| 11 | 返し刃 | 169 |
| 12 | 大振り | 168 |
| 13 | 残像 | 159 |
| 14 | 踏ん張り | 150 |
| 15 | 粉砕 | 143 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 315 |
| 2 | 崩し | 215 |
| 3 | 攻撃 | 196 |
| 4 | 貫き | 183 |
| 5 | 防御 | 163 |
| 6 | 渾身 | 161 |
| 7 | 大振り | 156 |
| 8 | 残像 | 130 |
| 9 | 粉砕 | 130 |
| 10 | 返し刃 | 128 |
| 11 | ステップ | 122 |
| 12 | 踏ん張り | 106 |
| 13 | 強撃 | 95 |
| 14 | 疾走 | 94 |
| 15 | 鉄壁 | 84 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `GuardDraftBot` | 3.7 | 1.04 | 1.69 | 2.84 | 1.29 | 1.22 | 140 (14.0%) | 131 (27.9%) |
| `StandardDraftBot` | 4.19 | 0.91 | 1.53 | 3.55 | 0.94 | 1.17 | 131 (13.1%) | 140 (30.3%) |

## Drafter Details

### GuardDraftBot

- Win Rate: 46.9%
- Draw Rate: 6.9%
- First Pass Win Rate: 39.3%
- Win With Fewer Cards: 24.7%
- Win With Same Cards: 36.5%
- Win With More Cards: 38.8%
- Winner Facedown Avg: 3
- Loser Facedown Avg: 2.73
- Starting Player Win Rate: 46.0%
- Responding Player Win Rate: 47.8%
- Final Stats Avg: A=3.7, B=1.04, S=1.69
- Losing Final Stats Avg: A=2.84, B=1.29, S=1.22
- Lost With Speed Advantage: 140 (14.0%)
- Won After Blocking Faster Attack: 131 (27.9%)
- Action Rates: set=71.2%, set_pass=2.0%, pass=26.8%
- set_pass Candidate Avg / Match: 13.87
- Turns: min=1, avg=1.43, max=4
- Battle / Control: avg=13.86 / 6.14
- Role Colors: red=6.89, blue=3.44, green=3.53, white=6.14
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 1251 |
| 2 | 防御 | 1239 |
| 3 | 圧迫 | 1237 |
| 4 | ステップ | 1133 |
| 5 | 構え | 1105 |
| 6 | 集中 | 1018 |
| 7 | 牽制 | 1017 |
| 8 | 踏み込み | 805 |
| 9 | 鉄壁 | 679 |
| 10 | 渾身 | 660 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 607 |
| 2 | 防御 | 591 |
| 3 | 圧迫 | 570 |
| 4 | ステップ | 523 |
| 5 | 構え | 515 |
| 6 | 牽制 | 486 |
| 7 | 集中 | 460 |
| 8 | 踏み込み | 415 |
| 9 | 崩し | 328 |
| 10 | 貫き | 306 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 1251 | 302 | 139 | 105 |
| 防御 | `battle_defend` | `common` | 1239 | 319 | 151 | 98 |
| 圧迫 | `control_pressure` | `common` | 1237 | 283 | 129 | 0 |
| ステップ | `battle_step` | `common` | 1133 | 222 | 88 | 58 |
| 構え | `control_guard` | `common` | 1105 | 152 | 73 | 0 |
| 集中 | `control_focus` | `common` | 1018 | 80 | 38 | 0 |
| 牽制 | `control_disrupt` | `common` | 1017 | 244 | 120 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 805 | 257 | 177 | 172 |
| 鉄壁 | `battle_wall` | `rare` | 679 | 212 | 105 | 45 |
| 渾身 | `battle_all_in` | `rare` | 660 | 174 | 76 | 73 |
| 崩し | `battle_break` | `uncommon` | 656 | 192 | 120 | 113 |
| 貫き | `battle_pierce` | `uncommon` | 649 | 169 | 99 | 93 |
| 返し刃 | `battle_counter` | `uncommon` | 558 | 156 | 81 | 64 |
| 十字受け | `battle_cross_guard` | `uncommon` | 556 | 163 | 71 | 43 |
| 踏ん張り | `battle_brace` | `uncommon` | 530 | 163 | 85 | 60 |
| 粉砕 | `battle_crush` | `uncommon` | 526 | 143 | 69 | 63 |
| Bastion | `battle_bastion` | `uncommon` | 504 | 163 | 64 | 29 |
| 大振り | `battle_heavy_swing` | `rare` | 481 | 149 | 64 | 60 |
| 残像 | `battle_afterimage` | `rare` | 480 | 147 | 80 | 65 |
| 退き足 | `battle_backstep` | `uncommon` | 439 | 114 | 51 | 35 |
| 押し込み | `battle_press` | `uncommon` | 401 | 112 | 52 | 39 |
| Bulwark | `battle_bulwark` | `uncommon` | 399 | 111 | 39 | 26 |
| フェイント | `battle_feint` | `uncommon` | 382 | 89 | 45 | 31 |
| 強撃 | `battle_power_attack` | `uncommon` | 374 | 85 | 46 | 37 |
| 受け流し | `battle_guard` | `uncommon` | 358 | 103 | 42 | 32 |
| 疾走 | `battle_dash` | `rare` | 355 | 102 | 60 | 49 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 348 | 80 | 31 | 17 |
| 受け直し | `control_cover` | `uncommon` | 278 | 64 | 25 | 0 |
| 蓄え | `control_reserve` | `rare` | 235 | 61 | 25 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 234 | 44 | 23 | 0 |
| Crush Spirit | `control_crush_spirit` | `rare` | 207 | 60 | 27 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 192 | 27 | 11 | 0 |
| 補強 | `control_fortify` | `uncommon` | 183 | 49 | 27 | 0 |
| 加速 | `control_haste` | `uncommon` | 158 | 31 | 11 | 0 |
| Blank First | `control_blank_first` | `uncommon` | 139 | 39 | 24 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 136 | 24 | 8 | 0 |
| Tripwire | `battle_tripwire` | `rare` | 98 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 8000 | 1602 | 20.0% | 738 | 46.1% | 261 |
| `uncommon` | 8000 | 2121 | 26.5% | 1024 | 48.3% | 682 |
| `rare` | 4000 | 1162 | 29.0% | 614 | 52.8% | 464 |

#### Match Logs

- [draft_match_0001](matches/match_0001_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0002](matches/match_0002_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0003](matches/match_0003_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0004](matches/match_0004_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0005](matches/match_0005_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0006](matches/match_0006_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0007](matches/match_0007_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0008](matches/match_0008_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0009](matches/match_0009_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0010](matches/match_0010_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0011](matches/match_0011_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0012](matches/match_0012_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0013](matches/match_0013_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0014](matches/match_0014_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0015](matches/match_0015_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0016](matches/match_0016_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0017](matches/match_0017_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0018](matches/match_0018_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0019](matches/match_0019_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0020](matches/match_0020_GuardDraftBot_vs_StandardDraftBot.md)

### StandardDraftBot

- Win Rate: 46.2%
- Draw Rate: 6.9%
- First Pass Win Rate: 41.6%
- Win With Fewer Cards: 20.8%
- Win With Same Cards: 35.9%
- Win With More Cards: 43.3%
- Winner Facedown Avg: 2.95
- Loser Facedown Avg: 2.86
- Starting Player Win Rate: 46.0%
- Responding Player Win Rate: 46.4%
- Final Stats Avg: A=4.19, B=0.91, S=1.53
- Losing Final Stats Avg: A=3.55, B=0.94, S=1.17
- Lost With Speed Advantage: 131 (13.1%)
- Won After Blocking Faster Attack: 140 (30.3%)
- Action Rates: set=70.4%, set_pass=2.3%, pass=27.2%
- set_pass Candidate Avg / Match: 13.87
- Turns: min=1, avg=1.43, max=4
- Battle / Control: avg=13.83 / 6.17
- Role Colors: red=7.14, blue=3.38, green=3.31, white=6.17
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 防御 | 1235 |
| 2 | 攻撃 | 1233 |
| 3 | 圧迫 | 1218 |
| 4 | ステップ | 1138 |
| 5 | 構え | 1091 |
| 6 | 牽制 | 1051 |
| 7 | 集中 | 1034 |
| 8 | 踏み込み | 792 |
| 9 | 渾身 | 684 |
| 10 | 崩し | 663 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 防御 | 576 |
| 2 | 攻撃 | 568 |
| 3 | 圧迫 | 558 |
| 4 | 構え | 515 |
| 5 | ステップ | 513 |
| 6 | 牽制 | 495 |
| 7 | 集中 | 471 |
| 8 | 踏み込み | 403 |
| 9 | 崩し | 327 |
| 10 | 貫き | 303 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 防御 | `battle_defend` | `common` | 1235 | 280 | 108 | 65 |
| 攻撃 | `battle_attack` | `common` | 1233 | 302 | 119 | 91 |
| 圧迫 | `control_pressure` | `common` | 1218 | 261 | 110 | 0 |
| ステップ | `battle_step` | `common` | 1138 | 255 | 92 | 64 |
| 構え | `control_guard` | `common` | 1091 | 145 | 67 | 0 |
| 牽制 | `control_disrupt` | `common` | 1051 | 264 | 130 | 0 |
| 集中 | `control_focus` | `common` | 1034 | 111 | 44 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 792 | 240 | 157 | 143 |
| 渾身 | `battle_all_in` | `rare` | 684 | 214 | 95 | 88 |
| 崩し | `battle_break` | `uncommon` | 663 | 187 | 110 | 102 |
| 大振り | `battle_heavy_swing` | `rare` | 654 | 228 | 104 | 96 |
| 貫き | `battle_pierce` | `uncommon` | 654 | 191 | 101 | 90 |
| 鉄壁 | `battle_wall` | `rare` | 550 | 165 | 79 | 39 |
| 粉砕 | `battle_crush` | `uncommon` | 549 | 149 | 74 | 67 |
| 返し刃 | `battle_counter` | `uncommon` | 534 | 169 | 88 | 64 |
| 十字受け | `battle_cross_guard` | `uncommon` | 508 | 128 | 63 | 34 |
| 残像 | `battle_afterimage` | `rare` | 507 | 154 | 79 | 65 |
| 踏ん張り | `battle_brace` | `uncommon` | 495 | 143 | 65 | 46 |
| 強撃 | `battle_power_attack` | `uncommon` | 453 | 127 | 66 | 58 |
| Bastion | `battle_bastion` | `uncommon` | 443 | 130 | 59 | 33 |
| 押し込み | `battle_press` | `uncommon` | 425 | 126 | 61 | 45 |
| フェイント | `battle_feint` | `uncommon` | 407 | 117 | 45 | 29 |
| 退き足 | `battle_backstep` | `uncommon` | 407 | 113 | 46 | 31 |
| Bulwark | `battle_bulwark` | `uncommon` | 384 | 108 | 39 | 17 |
| 受け流し | `battle_guard` | `uncommon` | 371 | 104 | 46 | 36 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 331 | 85 | 39 | 17 |
| 疾走 | `battle_dash` | `rare` | 305 | 98 | 50 | 45 |
| 受け直し | `control_cover` | `uncommon` | 258 | 55 | 23 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 223 | 48 | 24 | 0 |
| 蓄え | `control_reserve` | `rare` | 217 | 49 | 13 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 213 | 37 | 21 | 0 |
| 補強 | `control_fortify` | `uncommon` | 195 | 35 | 21 | 0 |
| Crush Spirit | `control_crush_spirit` | `rare` | 179 | 53 | 35 | 0 |
| 加速 | `control_haste` | `uncommon` | 168 | 27 | 11 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 160 | 24 | 7 | 0 |
| Blank First | `control_blank_first` | `uncommon` | 159 | 58 | 20 | 0 |
| Tripwire | `battle_tripwire` | `rare` | 112 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 8000 | 1618 | 20.2% | 670 | 41.4% | 220 |
| `uncommon` | 8000 | 2161 | 27.0% | 1029 | 47.6% | 669 |
| `rare` | 4000 | 1201 | 30.0% | 612 | 51.0% | 476 |

#### Match Logs

- [draft_match_0001](matches/match_0001_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0002](matches/match_0002_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0003](matches/match_0003_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0004](matches/match_0004_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0005](matches/match_0005_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0006](matches/match_0006_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0007](matches/match_0007_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0008](matches/match_0008_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0009](matches/match_0009_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0010](matches/match_0010_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0011](matches/match_0011_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0012](matches/match_0012_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0013](matches/match_0013_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0014](matches/match_0014_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0015](matches/match_0015_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0016](matches/match_0016_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0017](matches/match_0017_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0018](matches/match_0018_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0019](matches/match_0019_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0020](matches/match_0020_GuardDraftBot_vs_StandardDraftBot.md)
