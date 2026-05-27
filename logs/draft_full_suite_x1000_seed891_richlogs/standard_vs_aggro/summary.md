# Draft Report

## Configuration

- Draft Bot 1: `StandardDraftBot`
- Draft Bot 2: `AggroDraftBot`
- Play Bot 1: `StandardBot`
- Play Bot 2: `AggroBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 2891
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
| `AggroDraftBot` | 1000 | 457 | 468 | 75 | 45.7% | 44.1% | 29.5% | 30.4% | 40.0% | 2.83 | 2.75 | 46.4% | 45.1% | 70.0% | 2.0% | 28.0% | 13.9 | 6.1 | 7.39 | 3.4 | 3.11 | 6.1 | 8 | 8 | 4 |
| `StandardDraftBot` | 1000 | 468 | 457 | 75 | 46.8% | 45.8% | 25.4% | 33.8% | 40.8% | 2.91 | 2.72 | 47.2% | 46.4% | 70.0% | 2.2% | 27.8% | 13.84 | 6.16 | 7.05 | 3.46 | 3.33 | 6.16 | 8 | 8 | 4 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| AggroDraftBot vs StandardDraftBot | 1000 | 75 | `AggroDraftBot`=457, `StandardDraftBot`=468 | 1.35 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 615 |
| 2 | 牽制 | 559 |
| 3 | ステップ | 530 |
| 4 | 防御 | 514 |
| 5 | 踏み込み | 469 |
| 6 | 圧迫 | 467 |
| 7 | 渾身 | 413 |
| 8 | 貫き | 376 |
| 9 | 崩し | 355 |
| 10 | 大振り | 348 |
| 11 | 粉砕 | 316 |
| 12 | 残像 | 312 |
| 13 | 鉄壁 | 299 |
| 14 | 構え | 290 |
| 15 | 踏ん張り | 288 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 321 |
| 2 | 攻撃 | 264 |
| 3 | 牽制 | 249 |
| 4 | 圧迫 | 220 |
| 5 | 貫き | 211 |
| 6 | 崩し | 210 |
| 7 | ステップ | 203 |
| 8 | 防御 | 189 |
| 9 | 粉砕 | 177 |
| 10 | 残像 | 165 |
| 11 | 渾身 | 161 |
| 12 | 返し刃 | 154 |
| 13 | 大振り | 140 |
| 14 | 鉄壁 | 136 |
| 15 | 十字受け | 132 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 313 |
| 2 | 攻撃 | 206 |
| 3 | 貫き | 195 |
| 4 | 崩し | 194 |
| 5 | 粉砕 | 154 |
| 6 | 渾身 | 151 |
| 7 | ステップ | 142 |
| 8 | 大振り | 129 |
| 9 | 返し刃 | 125 |
| 10 | 残像 | 124 |
| 11 | 防御 | 111 |
| 12 | 強撃 | 100 |
| 13 | 踏ん張り | 99 |
| 14 | 十字受け | 96 |
| 15 | フェイント | 73 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `AggroDraftBot` | 4.03 | 0.85 | 1.57 | 3.48 | 0.93 | 1.18 | 118 (11.8%) | 147 (32.2%) |
| `StandardDraftBot` | 3.73 | 0.89 | 1.73 | 2.99 | 1.0 | 1.26 | 147 (14.7%) | 118 (25.2%) |

## Drafter Details

### AggroDraftBot

- Win Rate: 45.7%
- Draw Rate: 7.5%
- First Pass Win Rate: 44.1%
- Win With Fewer Cards: 29.5%
- Win With Same Cards: 30.4%
- Win With More Cards: 40.0%
- Winner Facedown Avg: 2.83
- Loser Facedown Avg: 2.75
- Starting Player Win Rate: 46.4%
- Responding Player Win Rate: 45.1%
- Final Stats Avg: A=4.03, B=0.85, S=1.57
- Losing Final Stats Avg: A=3.48, B=0.93, S=1.18
- Lost With Speed Advantage: 118 (11.8%)
- Won After Blocking Faster Attack: 147 (32.2%)
- Action Rates: set=70.0%, set_pass=2.0%, pass=28.0%
- set_pass Candidate Avg / Match: 11.46
- Turns: min=1, avg=1.35, max=4
- Battle / Control: avg=13.9 / 6.1
- Role Colors: red=7.39, blue=3.4, green=3.11, white=6.1
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 1371 |
| 2 | 防御 | 1175 |
| 3 | 圧迫 | 1174 |
| 4 | ステップ | 1153 |
| 5 | 集中 | 1061 |
| 6 | 構え | 1038 |
| 7 | 牽制 | 1028 |
| 8 | 踏み込み | 787 |
| 9 | 渾身 | 734 |
| 10 | 貫き | 701 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 645 |
| 2 | 圧迫 | 535 |
| 3 | 防御 | 534 |
| 4 | ステップ | 528 |
| 5 | 牽制 | 483 |
| 6 | 集中 | 476 |
| 7 | 構え | 455 |
| 8 | 踏み込み | 402 |
| 9 | 貫き | 327 |
| 10 | 崩し | 319 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 1371 | 313 | 128 | 97 |
| 防御 | `battle_defend` | `common` | 1175 | 248 | 88 | 51 |
| 圧迫 | `control_pressure` | `common` | 1174 | 227 | 104 | 0 |
| ステップ | `battle_step` | `common` | 1153 | 260 | 103 | 68 |
| 集中 | `control_focus` | `common` | 1061 | 104 | 37 | 0 |
| 構え | `control_guard` | `common` | 1038 | 139 | 64 | 0 |
| 牽制 | `control_disrupt` | `common` | 1028 | 286 | 131 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 787 | 233 | 148 | 145 |
| 渾身 | `battle_all_in` | `rare` | 734 | 215 | 88 | 79 |
| 貫き | `battle_pierce` | `uncommon` | 701 | 184 | 99 | 92 |
| 崩し | `battle_break` | `uncommon` | 655 | 173 | 104 | 93 |
| 大振り | `battle_heavy_swing` | `rare` | 643 | 188 | 80 | 73 |
| 粉砕 | `battle_crush` | `uncommon` | 574 | 159 | 85 | 71 |
| 返し刃 | `battle_counter` | `uncommon` | 547 | 147 | 78 | 58 |
| 踏ん張り | `battle_brace` | `uncommon` | 512 | 154 | 66 | 50 |
| 残像 | `battle_afterimage` | `rare` | 511 | 156 | 83 | 61 |
| 十字受け | `battle_cross_guard` | `uncommon` | 468 | 133 | 68 | 50 |
| 鉄壁 | `battle_wall` | `rare` | 468 | 122 | 52 | 19 |
| 強撃 | `battle_power_attack` | `uncommon` | 439 | 137 | 63 | 57 |
| フェイント | `battle_feint` | `uncommon` | 435 | 112 | 48 | 37 |
| Bastion | `battle_bastion` | `uncommon` | 427 | 119 | 50 | 27 |
| 押し込み | `battle_press` | `uncommon` | 427 | 115 | 62 | 43 |
| 退き足 | `battle_backstep` | `uncommon` | 421 | 97 | 40 | 22 |
| Bulwark | `battle_bulwark` | `uncommon` | 375 | 108 | 39 | 33 |
| 受け流し | `battle_guard` | `uncommon` | 345 | 89 | 33 | 22 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 319 | 71 | 30 | 15 |
| 疾走 | `battle_dash` | `rare` | 310 | 69 | 35 | 29 |
| 受け直し | `control_cover` | `uncommon` | 245 | 50 | 21 | 0 |
| Crush Spirit | `control_crush_spirit` | `rare` | 231 | 79 | 49 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 225 | 43 | 25 | 0 |
| 蓄え | `control_reserve` | `rare` | 211 | 50 | 27 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 196 | 30 | 8 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 193 | 31 | 18 | 0 |
| 補強 | `control_fortify` | `uncommon` | 172 | 29 | 17 | 0 |
| Blank First | `control_blank_first` | `uncommon` | 164 | 35 | 14 | 0 |
| 加速 | `control_haste` | `uncommon` | 160 | 26 | 12 | 0 |
| Tripwire | `battle_tripwire` | `rare` | 105 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 8000 | 1577 | 19.7% | 655 | 41.5% | 216 |
| `uncommon` | 8000 | 2042 | 25.5% | 980 | 48.0% | 670 |
| `rare` | 4000 | 1112 | 27.8% | 562 | 50.5% | 406 |

#### Match Logs

- [draft_match_0001](matches/match_0001_StandardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0002](matches/match_0002_AggroDraftBot_vs_StandardDraftBot.md)
- [draft_match_0003](matches/match_0003_StandardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0004](matches/match_0004_AggroDraftBot_vs_StandardDraftBot.md)
- [draft_match_0005](matches/match_0005_StandardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0006](matches/match_0006_AggroDraftBot_vs_StandardDraftBot.md)
- [draft_match_0007](matches/match_0007_StandardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0008](matches/match_0008_AggroDraftBot_vs_StandardDraftBot.md)
- [draft_match_0009](matches/match_0009_StandardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0010](matches/match_0010_AggroDraftBot_vs_StandardDraftBot.md)
- [draft_match_0011](matches/match_0011_StandardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0012](matches/match_0012_AggroDraftBot_vs_StandardDraftBot.md)
- [draft_match_0013](matches/match_0013_StandardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0014](matches/match_0014_AggroDraftBot_vs_StandardDraftBot.md)
- [draft_match_0015](matches/match_0015_StandardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0016](matches/match_0016_AggroDraftBot_vs_StandardDraftBot.md)
- [draft_match_0017](matches/match_0017_StandardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0018](matches/match_0018_AggroDraftBot_vs_StandardDraftBot.md)
- [draft_match_0019](matches/match_0019_StandardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0020](matches/match_0020_AggroDraftBot_vs_StandardDraftBot.md)

### StandardDraftBot

- Win Rate: 46.8%
- Draw Rate: 7.5%
- First Pass Win Rate: 45.8%
- Win With Fewer Cards: 25.4%
- Win With Same Cards: 33.8%
- Win With More Cards: 40.8%
- Winner Facedown Avg: 2.91
- Loser Facedown Avg: 2.72
- Starting Player Win Rate: 47.2%
- Responding Player Win Rate: 46.4%
- Final Stats Avg: A=3.73, B=0.89, S=1.73
- Losing Final Stats Avg: A=2.99, B=1.0, S=1.26
- Lost With Speed Advantage: 147 (14.7%)
- Won After Blocking Faster Attack: 118 (25.2%)
- Action Rates: set=70.0%, set_pass=2.2%, pass=27.8%
- set_pass Candidate Avg / Match: 11.46
- Turns: min=1, avg=1.35, max=4
- Battle / Control: avg=13.84 / 6.16
- Role Colors: red=7.05, blue=3.46, green=3.33, white=6.16
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 1260 |
| 2 | 圧迫 | 1204 |
| 3 | ステップ | 1183 |
| 4 | 防御 | 1159 |
| 5 | 構え | 1136 |
| 6 | 集中 | 1031 |
| 7 | 牽制 | 1027 |
| 8 | 踏み込み | 772 |
| 9 | 崩し | 674 |
| 10 | 渾身 | 674 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 圧迫 | 598 |
| 2 | 攻撃 | 590 |
| 3 | 防御 | 546 |
| 4 | ステップ | 541 |
| 5 | 構え | 504 |
| 6 | 牽制 | 487 |
| 7 | 集中 | 478 |
| 8 | 踏み込み | 402 |
| 9 | 崩し | 333 |
| 10 | 貫き | 323 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 1260 | 302 | 136 | 109 |
| 圧迫 | `control_pressure` | `common` | 1204 | 240 | 116 | 0 |
| ステップ | `battle_step` | `common` | 1183 | 270 | 100 | 74 |
| 防御 | `battle_defend` | `common` | 1159 | 266 | 101 | 60 |
| 構え | `control_guard` | `common` | 1136 | 151 | 56 | 0 |
| 集中 | `control_focus` | `common` | 1031 | 84 | 47 | 0 |
| 牽制 | `control_disrupt` | `common` | 1027 | 273 | 118 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 772 | 236 | 173 | 168 |
| 渾身 | `battle_all_in` | `rare` | 674 | 198 | 73 | 72 |
| 崩し | `battle_break` | `uncommon` | 674 | 182 | 106 | 101 |
| 貫き | `battle_pierce` | `uncommon` | 653 | 192 | 112 | 103 |
| 鉄壁 | `battle_wall` | `rare` | 623 | 177 | 84 | 34 |
| 大振り | `battle_heavy_swing` | `rare` | 599 | 160 | 60 | 56 |
| 返し刃 | `battle_counter` | `uncommon` | 565 | 138 | 76 | 67 |
| 粉砕 | `battle_crush` | `uncommon` | 536 | 157 | 92 | 83 |
| 十字受け | `battle_cross_guard` | `uncommon` | 517 | 131 | 64 | 46 |
| 残像 | `battle_afterimage` | `rare` | 503 | 156 | 82 | 63 |
| 踏ん張り | `battle_brace` | `uncommon` | 495 | 134 | 63 | 49 |
| Bastion | `battle_bastion` | `uncommon` | 457 | 129 | 48 | 30 |
| 退き足 | `battle_backstep` | `uncommon` | 440 | 115 | 44 | 27 |
| 強撃 | `battle_power_attack` | `uncommon` | 424 | 113 | 50 | 43 |
| フェイント | `battle_feint` | `uncommon` | 409 | 113 | 42 | 36 |
| Bulwark | `battle_bulwark` | `uncommon` | 400 | 100 | 40 | 29 |
| 押し込み | `battle_press` | `uncommon` | 395 | 99 | 35 | 28 |
| 受け流し | `battle_guard` | `uncommon` | 349 | 101 | 46 | 34 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 345 | 68 | 19 | 8 |
| 疾走 | `battle_dash` | `rare` | 311 | 89 | 44 | 39 |
| 受け直し | `control_cover` | `uncommon` | 260 | 54 | 19 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 226 | 49 | 26 | 0 |
| 蓄え | `control_reserve` | `rare` | 214 | 48 | 17 | 0 |
| Crush Spirit | `control_crush_spirit` | `rare` | 204 | 55 | 34 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 192 | 23 | 11 | 0 |
| 補強 | `control_fortify` | `uncommon` | 184 | 38 | 17 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 170 | 32 | 8 | 0 |
| Blank First | `control_blank_first` | `uncommon` | 158 | 38 | 14 | 0 |
| 加速 | `control_haste` | `uncommon` | 151 | 26 | 13 | 0 |
| Tripwire | `battle_tripwire` | `rare` | 100 | 2 | 2 | 2 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 8000 | 1586 | 19.8% | 674 | 42.5% | 243 |
| `uncommon` | 8000 | 2032 | 25.4% | 945 | 46.5% | 684 |
| `rare` | 4000 | 1121 | 28.0% | 569 | 50.8% | 434 |

#### Match Logs

- [draft_match_0001](matches/match_0001_StandardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0002](matches/match_0002_AggroDraftBot_vs_StandardDraftBot.md)
- [draft_match_0003](matches/match_0003_StandardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0004](matches/match_0004_AggroDraftBot_vs_StandardDraftBot.md)
- [draft_match_0005](matches/match_0005_StandardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0006](matches/match_0006_AggroDraftBot_vs_StandardDraftBot.md)
- [draft_match_0007](matches/match_0007_StandardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0008](matches/match_0008_AggroDraftBot_vs_StandardDraftBot.md)
- [draft_match_0009](matches/match_0009_StandardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0010](matches/match_0010_AggroDraftBot_vs_StandardDraftBot.md)
- [draft_match_0011](matches/match_0011_StandardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0012](matches/match_0012_AggroDraftBot_vs_StandardDraftBot.md)
- [draft_match_0013](matches/match_0013_StandardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0014](matches/match_0014_AggroDraftBot_vs_StandardDraftBot.md)
- [draft_match_0015](matches/match_0015_StandardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0016](matches/match_0016_AggroDraftBot_vs_StandardDraftBot.md)
- [draft_match_0017](matches/match_0017_StandardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0018](matches/match_0018_AggroDraftBot_vs_StandardDraftBot.md)
- [draft_match_0019](matches/match_0019_StandardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0020](matches/match_0020_AggroDraftBot_vs_StandardDraftBot.md)
