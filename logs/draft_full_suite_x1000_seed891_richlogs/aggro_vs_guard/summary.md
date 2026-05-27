# Draft Report

## Configuration

- Draft Bot 1: `AggroDraftBot`
- Draft Bot 2: `GuardDraftBot`
- Play Bot 1: `AggroBot`
- Play Bot 2: `GuardBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 5891
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
| `AggroDraftBot` | 1000 | 489 | 443 | 68 | 48.9% | 45.0% | 21.5% | 32.9% | 45.6% | 2.93 | 2.85 | 48.2% | 49.6% | 70.5% | 2.5% | 27.0% | 13.91 | 6.09 | 7.38 | 3.53 | 2.99 | 6.09 | 8 | 8 | 4 |
| `GuardDraftBot` | 1000 | 443 | 489 | 68 | 44.3% | 41.6% | 29.3% | 35.2% | 35.4% | 2.91 | 2.69 | 43.1% | 45.5% | 71.1% | 1.6% | 27.3% | 13.89 | 6.11 | 6.87 | 3.37 | 3.65 | 6.11 | 8 | 8 | 4 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| AggroDraftBot vs GuardDraftBot | 1000 | 68 | `AggroDraftBot`=489, `GuardDraftBot`=443 | 1.39 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 571 |
| 2 | 防御 | 562 |
| 3 | 牽制 | 523 |
| 4 | 圧迫 | 515 |
| 5 | 踏み込み | 488 |
| 6 | ステップ | 476 |
| 7 | 渾身 | 406 |
| 8 | 崩し | 378 |
| 9 | 大振り | 369 |
| 10 | 貫き | 352 |
| 11 | 鉄壁 | 320 |
| 12 | 返し刃 | 306 |
| 13 | 踏ん張り | 300 |
| 14 | 粉砕 | 295 |
| 15 | 十字受け | 295 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 327 |
| 2 | 牽制 | 255 |
| 3 | 攻撃 | 243 |
| 4 | 崩し | 232 |
| 5 | 貫き | 211 |
| 6 | 防御 | 209 |
| 7 | 圧迫 | 208 |
| 8 | ステップ | 184 |
| 9 | 渾身 | 172 |
| 10 | 返し刃 | 165 |
| 11 | 粉砕 | 159 |
| 12 | 残像 | 156 |
| 13 | 大振り | 154 |
| 14 | 構え | 143 |
| 15 | 鉄壁 | 143 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 316 |
| 2 | 崩し | 206 |
| 3 | 貫き | 189 |
| 4 | 攻撃 | 183 |
| 5 | 渾身 | 167 |
| 6 | 粉砕 | 151 |
| 7 | 大振り | 146 |
| 8 | 防御 | 143 |
| 9 | 返し刃 | 133 |
| 10 | ステップ | 132 |
| 11 | 残像 | 123 |
| 12 | 踏ん張り | 100 |
| 13 | 十字受け | 97 |
| 14 | 強撃 | 94 |
| 15 | 疾走 | 83 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `AggroDraftBot` | 4.43 | 0.71 | 1.55 | 3.76 | 0.78 | 1.06 | 117 (11.7%) | 150 (30.7%) |
| `GuardDraftBot` | 3.45 | 1.13 | 1.67 | 2.63 | 1.35 | 1.33 | 150 (15.0%) | 117 (26.4%) |

## Drafter Details

### AggroDraftBot

- Win Rate: 48.9%
- Draw Rate: 6.8%
- First Pass Win Rate: 45.0%
- Win With Fewer Cards: 21.5%
- Win With Same Cards: 32.9%
- Win With More Cards: 45.6%
- Winner Facedown Avg: 2.93
- Loser Facedown Avg: 2.85
- Starting Player Win Rate: 48.2%
- Responding Player Win Rate: 49.6%
- Final Stats Avg: A=4.43, B=0.71, S=1.55
- Losing Final Stats Avg: A=3.76, B=0.78, S=1.06
- Lost With Speed Advantage: 117 (11.7%)
- Won After Blocking Faster Attack: 150 (30.7%)
- Action Rates: set=70.5%, set_pass=2.5%, pass=27.0%
- set_pass Candidate Avg / Match: 13.22
- Turns: min=1, avg=1.39, max=4
- Battle / Control: avg=13.91 / 6.09
- Role Colors: red=7.38, blue=3.53, green=2.99, white=6.09
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 1316 |
| 2 | 防御 | 1207 |
| 3 | ステップ | 1176 |
| 4 | 圧迫 | 1172 |
| 5 | 構え | 1079 |
| 6 | 集中 | 1046 |
| 7 | 牽制 | 1004 |
| 8 | 踏み込み | 765 |
| 9 | 渾身 | 755 |
| 10 | 貫き | 681 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 652 |
| 2 | 圧迫 | 574 |
| 3 | 防御 | 566 |
| 4 | ステップ | 557 |
| 5 | 構え | 526 |
| 6 | 牽制 | 522 |
| 7 | 集中 | 515 |
| 8 | 踏み込み | 415 |
| 9 | 崩し | 339 |
| 10 | 貫き | 337 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 1316 | 309 | 132 | 100 |
| 防御 | `battle_defend` | `common` | 1207 | 274 | 104 | 71 |
| ステップ | `battle_step` | `common` | 1176 | 252 | 101 | 66 |
| 圧迫 | `control_pressure` | `common` | 1172 | 257 | 110 | 0 |
| 構え | `control_guard` | `common` | 1079 | 143 | 85 | 0 |
| 集中 | `control_focus` | `common` | 1046 | 119 | 50 | 0 |
| 牽制 | `control_disrupt` | `common` | 1004 | 242 | 121 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 765 | 249 | 173 | 166 |
| 渾身 | `battle_all_in` | `rare` | 755 | 257 | 112 | 109 |
| 貫き | `battle_pierce` | `uncommon` | 681 | 176 | 107 | 95 |
| 大振り | `battle_heavy_swing` | `rare` | 674 | 221 | 95 | 87 |
| 崩し | `battle_break` | `uncommon` | 665 | 178 | 110 | 100 |
| 粉砕 | `battle_crush` | `uncommon` | 604 | 167 | 90 | 87 |
| 残像 | `battle_afterimage` | `rare` | 534 | 147 | 79 | 63 |
| 踏ん張り | `battle_brace` | `uncommon` | 515 | 154 | 76 | 53 |
| 返し刃 | `battle_counter` | `uncommon` | 509 | 161 | 90 | 74 |
| フェイント | `battle_feint` | `uncommon` | 495 | 133 | 55 | 40 |
| 十字受け | `battle_cross_guard` | `uncommon` | 490 | 122 | 69 | 52 |
| 強撃 | `battle_power_attack` | `uncommon` | 455 | 113 | 61 | 51 |
| 押し込み | `battle_press` | `uncommon` | 444 | 120 | 56 | 42 |
| 鉄壁 | `battle_wall` | `rare` | 443 | 112 | 49 | 16 |
| 退き足 | `battle_backstep` | `uncommon` | 411 | 120 | 45 | 27 |
| Bastion | `battle_bastion` | `uncommon` | 348 | 104 | 47 | 19 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 339 | 98 | 34 | 12 |
| Bulwark | `battle_bulwark` | `uncommon` | 332 | 85 | 49 | 27 |
| 受け流し | `battle_guard` | `uncommon` | 325 | 102 | 47 | 32 |
| 疾走 | `battle_dash` | `rare` | 318 | 96 | 51 | 42 |
| 受け直し | `control_cover` | `uncommon` | 247 | 45 | 22 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 231 | 43 | 23 | 0 |
| Crush Spirit | `control_crush_spirit` | `rare` | 206 | 59 | 35 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 203 | 29 | 14 | 0 |
| 蓄え | `control_reserve` | `rare` | 196 | 48 | 20 | 0 |
| 補強 | `control_fortify` | `uncommon` | 187 | 41 | 20 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 179 | 30 | 14 | 0 |
| 加速 | `control_haste` | `uncommon` | 174 | 33 | 14 | 0 |
| Blank First | `control_blank_first` | `uncommon` | 166 | 51 | 23 | 0 |
| Tripwire | `battle_tripwire` | `rare` | 109 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 8000 | 1596 | 20.0% | 703 | 44.0% | 237 |
| `uncommon` | 8000 | 2105 | 26.3% | 1066 | 50.6% | 711 |
| `rare` | 4000 | 1189 | 29.7% | 614 | 51.6% | 483 |

#### Match Logs

- [draft_match_0001](matches/match_0001_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0002](matches/match_0002_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0003](matches/match_0003_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0004](matches/match_0004_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0005](matches/match_0005_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0006](matches/match_0006_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0007](matches/match_0007_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0008](matches/match_0008_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0009](matches/match_0009_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0010](matches/match_0010_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0011](matches/match_0011_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0012](matches/match_0012_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0013](matches/match_0013_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0014](matches/match_0014_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0015](matches/match_0015_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0016](matches/match_0016_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0017](matches/match_0017_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0018](matches/match_0018_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0019](matches/match_0019_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0020](matches/match_0020_GuardDraftBot_vs_AggroDraftBot.md)

### GuardDraftBot

- Win Rate: 44.3%
- Draw Rate: 6.8%
- First Pass Win Rate: 41.6%
- Win With Fewer Cards: 29.3%
- Win With Same Cards: 35.2%
- Win With More Cards: 35.4%
- Winner Facedown Avg: 2.91
- Loser Facedown Avg: 2.69
- Starting Player Win Rate: 43.1%
- Responding Player Win Rate: 45.5%
- Final Stats Avg: A=3.45, B=1.13, S=1.67
- Losing Final Stats Avg: A=2.63, B=1.35, S=1.33
- Lost With Speed Advantage: 150 (15.0%)
- Won After Blocking Faster Attack: 117 (26.4%)
- Action Rates: set=71.1%, set_pass=1.6%, pass=27.3%
- set_pass Candidate Avg / Match: 13.22
- Turns: min=1, avg=1.39, max=4
- Battle / Control: avg=13.89 / 6.11
- Role Colors: red=6.87, blue=3.37, green=3.65, white=6.11
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 防御 | 1258 |
| 2 | 攻撃 | 1225 |
| 3 | 圧迫 | 1208 |
| 4 | ステップ | 1119 |
| 5 | 構え | 1105 |
| 6 | 牽制 | 1063 |
| 7 | 集中 | 1022 |
| 8 | 踏み込み | 798 |
| 9 | 鉄壁 | 702 |
| 10 | 崩し | 676 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 防御 | 562 |
| 2 | 攻撃 | 550 |
| 3 | 圧迫 | 526 |
| 4 | 構え | 506 |
| 5 | 牽制 | 494 |
| 6 | ステップ | 475 |
| 7 | 集中 | 431 |
| 8 | 踏み込み | 401 |
| 9 | 崩し | 335 |
| 10 | 鉄壁 | 329 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 防御 | `battle_defend` | `common` | 1258 | 288 | 105 | 72 |
| 攻撃 | `battle_attack` | `common` | 1225 | 262 | 111 | 83 |
| 圧迫 | `control_pressure` | `common` | 1208 | 258 | 98 | 0 |
| ステップ | `battle_step` | `common` | 1119 | 224 | 83 | 66 |
| 構え | `control_guard` | `common` | 1105 | 142 | 58 | 0 |
| 牽制 | `control_disrupt` | `common` | 1063 | 281 | 134 | 0 |
| 集中 | `control_focus` | `common` | 1022 | 101 | 31 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 798 | 239 | 154 | 150 |
| 鉄壁 | `battle_wall` | `rare` | 702 | 208 | 94 | 42 |
| 崩し | `battle_break` | `uncommon` | 676 | 200 | 122 | 106 |
| 渾身 | `battle_all_in` | `rare` | 650 | 149 | 60 | 58 |
| 貫き | `battle_pierce` | `uncommon` | 627 | 176 | 104 | 94 |
| Bastion | `battle_bastion` | `uncommon` | 553 | 170 | 67 | 29 |
| 返し刃 | `battle_counter` | `uncommon` | 548 | 145 | 75 | 59 |
| 踏ん張り | `battle_brace` | `uncommon` | 539 | 146 | 58 | 47 |
| 十字受け | `battle_cross_guard` | `uncommon` | 536 | 173 | 69 | 45 |
| 大振り | `battle_heavy_swing` | `rare` | 512 | 148 | 59 | 59 |
| 粉砕 | `battle_crush` | `uncommon` | 487 | 128 | 69 | 64 |
| 残像 | `battle_afterimage` | `rare` | 479 | 146 | 77 | 60 |
| 退き足 | `battle_backstep` | `uncommon` | 433 | 117 | 38 | 26 |
| 強撃 | `battle_power_attack` | `uncommon` | 408 | 100 | 48 | 43 |
| Bulwark | `battle_bulwark` | `uncommon` | 407 | 137 | 65 | 42 |
| 押し込み | `battle_press` | `uncommon` | 400 | 100 | 47 | 31 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 367 | 101 | 35 | 22 |
| 受け流し | `battle_guard` | `uncommon` | 362 | 97 | 40 | 26 |
| フェイント | `battle_feint` | `uncommon` | 358 | 86 | 31 | 23 |
| 疾走 | `battle_dash` | `rare` | 345 | 95 | 47 | 41 |
| 受け直し | `control_cover` | `uncommon` | 239 | 40 | 14 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 212 | 35 | 19 | 0 |
| 蓄え | `control_reserve` | `rare` | 209 | 55 | 16 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 205 | 29 | 15 | 0 |
| 補強 | `control_fortify` | `uncommon` | 203 | 55 | 30 | 0 |
| Crush Spirit | `control_crush_spirit` | `rare` | 201 | 64 | 34 | 0 |
| Blank First | `control_blank_first` | `uncommon` | 151 | 34 | 20 | 0 |
| 加速 | `control_haste` | `uncommon` | 145 | 32 | 15 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 144 | 20 | 14 | 0 |
| Tripwire | `battle_tripwire` | `rare` | 104 | 2 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 8000 | 1556 | 19.4% | 620 | 39.8% | 221 |
| `uncommon` | 8000 | 2121 | 26.5% | 995 | 46.9% | 657 |
| `rare` | 4000 | 1106 | 27.7% | 541 | 48.9% | 410 |

#### Match Logs

- [draft_match_0001](matches/match_0001_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0002](matches/match_0002_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0003](matches/match_0003_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0004](matches/match_0004_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0005](matches/match_0005_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0006](matches/match_0006_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0007](matches/match_0007_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0008](matches/match_0008_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0009](matches/match_0009_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0010](matches/match_0010_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0011](matches/match_0011_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0012](matches/match_0012_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0013](matches/match_0013_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0014](matches/match_0014_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0015](matches/match_0015_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0016](matches/match_0016_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0017](matches/match_0017_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0018](matches/match_0018_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0019](matches/match_0019_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0020](matches/match_0020_GuardDraftBot_vs_AggroDraftBot.md)
