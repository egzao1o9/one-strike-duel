# Draft Report

## Configuration

- Draft Bot 1: `StandardDraftBot`
- Draft Bot 2: `AggroDraftBot`
- Play Bot 1: `StandardBot`
- Play Bot 2: `AggroBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 2901
- Pool: `base_pool` (115 copies)
- Pairing Mode: mirrored seats per round
- Draft Mode: `full`
- Fast Report: on
- Lean Draft Logging: on
- Save Battle Logs: on
- Draft Flow: normal public pack + normal hidden pack, then public rare + hidden rare, with order swapped in second half

## Drafter Summary

| Drafter | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Winner Set Avg | Loser Set Avg | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate | Battle Avg | Control Avg | Blessing Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `AggroDraftBot` | 1000 | 474 | 468 | 58 | 47.4% | 46.3% | 14.8% | 54.6% | 30.6% | 3.17 | 3.0 | 46.1% | 48.8% | 72.2% | 2.3% | 25.5% | 13.01 | 6.09 | 0.9 | 6.66 | 3.79 | 3.37 | 6.18 | 8 | 8 | 4 |
| `StandardDraftBot` | 1000 | 468 | 474 | 58 | 46.8% | 44.3% | 15.6% | 51.7% | 32.7% | 3.17 | 3.01 | 45.5% | 48.0% | 72.3% | 2.0% | 25.7% | 12.89 | 6.14 | 0.97 | 6.54 | 3.72 | 3.5 | 6.23 | 8 | 8 | 4 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| AggroDraftBot vs StandardDraftBot | 1000 | 58 | `AggroDraftBot`=474, `StandardDraftBot`=468 | 1.58 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 圧迫 | 737 |
| 2 | 攻撃 | 721 |
| 3 | 防御 | 684 |
| 4 | ステップ | 640 |
| 5 | 牽制 | 626 |
| 6 | 構え | 610 |
| 7 | 集中 | 535 |
| 8 | 貫き | 432 |
| 9 | 崩し | 407 |
| 10 | 返し刃 | 365 |
| 11 | 踏ん張り | 363 |
| 12 | 粉砕 | 359 |
| 13 | 十字受け | 339 |
| 14 | フェイント | 286 |
| 15 | Bastion | 283 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 345 |
| 2 | 圧迫 | 321 |
| 3 | 貫き | 285 |
| 4 | 防御 | 284 |
| 5 | 牽制 | 282 |
| 6 | 構え | 268 |
| 7 | ステップ | 259 |
| 8 | 崩し | 246 |
| 9 | 集中 | 203 |
| 10 | 返し刃 | 192 |
| 11 | 踏み込み | 184 |
| 12 | 粉砕 | 181 |
| 13 | 踏ん張り | 176 |
| 14 | 十字受け | 162 |
| 15 | 大振り | 141 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 貫き | 256 |
| 2 | 攻撃 | 241 |
| 3 | 崩し | 215 |
| 4 | 踏み込み | 175 |
| 5 | 防御 | 160 |
| 6 | ステップ | 158 |
| 7 | 粉砕 | 156 |
| 8 | 返し刃 | 129 |
| 9 | 大振り | 126 |
| 10 | 渾身 | 124 |
| 11 | 強撃 | 116 |
| 12 | 踏ん張り | 111 |
| 13 | 十字受け | 90 |
| 14 | 疾走 | 86 |
| 15 | 押し込み | 81 |

### Blessing Involvement Overall

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 罠糸の加護 | `blessing_trap_web` | 212 | 45.8% | 212 | 63 | 63 | 15 | 15 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 201 | 47.3% | 203 | 49 | 49 | 14 | 14 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 194 | 47.4% | 195 | 38 | 38 | 38 | 0 | 0 | 38 |
| 防の加護 | `blessing_guard` | 187 | 50.3% | 187 | 44 | 44 | 0 | 0 | 0 | 0 |
| 速の加護 | `blessing_speed` | 184 | 42.9% | 185 | 48 | 48 | 0 | 0 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 183 | 39.9% | 184 | 43 | 43 | 0 | 0 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 181 | 49.7% | 182 | 36 | 36 | 6 | 6 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 180 | 44.4% | 180 | 41 | 41 | 0 | 0 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 177 | 39.5% | 179 | 51 | 51 | 3 | 3 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 163 | 46.0% | 164 | 45 | 45 | 13 | 13 | 0 | 0 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `AggroDraftBot` | 3.11 | 1.0 | 1.67 | 2.12 | 1.01 | 1.6 | 179 (17.9%) | 166 (35.0%) |
| `StandardDraftBot` | 3.23 | 1.01 | 1.47 | 2.31 | 0.98 | 1.32 | 166 (16.6%) | 179 (38.2%) |

## Drafter Details

### AggroDraftBot

- Win Rate: 47.4%
- Draw Rate: 5.8%
- First Pass Win Rate: 46.3%
- Win With Fewer Cards: 14.8%
- Win With Same Cards: 54.6%
- Win With More Cards: 30.6%
- Winner Facedown Avg: 3.17
- Loser Facedown Avg: 3.0
- Starting Player Win Rate: 46.1%
- Responding Player Win Rate: 48.8%
- Final Stats Avg: A=3.11, B=1.0, S=1.67
- Losing Final Stats Avg: A=2.12, B=1.01, S=1.6
- Lost With Speed Advantage: 179 (17.9%)
- Won After Blocking Faster Attack: 166 (35.0%)
- Action Rates: set=72.2%, set_pass=2.3%, pass=25.5%
- set_pass Candidate Avg / Match: 16.45
- Turns: min=1, avg=1.58, max=8
- Battle / Control / Blessing: avg=13.01 / 6.09 / 0.9
- Role Colors: red=6.66, blue=3.79, green=3.37, white=6.18
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 1342 |
| 2 | 防御 | 1229 |
| 3 | ステップ | 1196 |
| 4 | 圧迫 | 1166 |
| 5 | 構え | 1037 |
| 6 | 集中 | 1019 |
| 7 | 牽制 | 1011 |
| 8 | 貫き | 631 |
| 9 | 崩し | 625 |
| 10 | 粉砕 | 574 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 668 |
| 2 | 防御 | 566 |
| 3 | ステップ | 557 |
| 4 | 圧迫 | 538 |
| 5 | 牽制 | 496 |
| 6 | 集中 | 485 |
| 7 | 構え | 482 |
| 8 | 貫き | 337 |
| 9 | 崩し | 312 |
| 10 | 粉砕 | 265 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 1342 | 366 | 188 | 129 |
| 防御 | `battle_defend` | `common` | 1229 | 328 | 128 | 75 |
| ステップ | `battle_step` | `common` | 1196 | 324 | 133 | 85 |
| 圧迫 | `control_pressure` | `common` | 1166 | 370 | 163 | 30 |
| 構え | `control_guard` | `common` | 1037 | 292 | 138 | 36 |
| 集中 | `control_focus` | `common` | 1019 | 259 | 96 | 32 |
| 牽制 | `control_disrupt` | `common` | 1011 | 315 | 144 | 16 |
| 貫き | `battle_pierce` | `uncommon` | 631 | 207 | 141 | 129 |
| 崩し | `battle_break` | `uncommon` | 625 | 208 | 122 | 107 |
| 粉砕 | `battle_crush` | `uncommon` | 574 | 196 | 100 | 88 |
| 返し刃 | `battle_counter` | `uncommon` | 563 | 193 | 98 | 65 |
| 踏ん張り | `battle_brace` | `uncommon` | 535 | 180 | 88 | 55 |
| 十字受け | `battle_cross_guard` | `uncommon` | 492 | 178 | 87 | 50 |
| 強撃 | `battle_power_attack` | `uncommon` | 466 | 136 | 70 | 56 |
| フェイント | `battle_feint` | `uncommon` | 455 | 154 | 67 | 40 |
| 踏み込み | `battle_step_in` | `rare` | 454 | 123 | 85 | 85 |
| 退き足 | `battle_backstep` | `uncommon` | 431 | 140 | 57 | 26 |
| 渾身 | `battle_all_in` | `rare` | 425 | 130 | 65 | 64 |
| Bastion | `battle_bastion` | `uncommon` | 423 | 123 | 45 | 18 |
| 押し込み | `battle_press` | `uncommon` | 419 | 124 | 57 | 37 |
| 大振り | `battle_heavy_swing` | `rare` | 384 | 133 | 71 | 66 |
| 受け流し | `battle_guard` | `uncommon` | 380 | 120 | 48 | 32 |
| 鉄壁 | `battle_wall` | `rare` | 375 | 142 | 69 | 23 |
| Bulwark | `battle_bulwark` | `uncommon` | 364 | 124 | 54 | 24 |
| 残像 | `battle_afterimage` | `rare` | 361 | 134 | 58 | 39 |
| 疾走 | `battle_dash` | `rare` | 327 | 90 | 52 | 40 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 298 | 85 | 34 | 16 |
| Tripwire | `battle_tripwire` | `rare` | 259 | 2 | 1 | 1 |
| 蓄え | `control_reserve` | `rare` | 257 | 86 | 37 | 2 |
| Crush Spirit | `control_crush_spirit` | `rare` | 255 | 80 | 45 | 0 |
| 受け直し | `control_cover` | `uncommon` | 231 | 84 | 35 | 9 |
| 前のめり | `control_overclock` | `uncommon` | 227 | 62 | 32 | 8 |
| 補強 | `control_fortify` | `uncommon` | 191 | 58 | 26 | 5 |
| 加速 | `control_haste` | `uncommon` | 177 | 57 | 26 | 6 |
| 勢い溜め | `control_momentum` | `uncommon` | 177 | 51 | 17 | 1 |
| 重心落とし | `control_anchor` | `uncommon` | 174 | 39 | 19 | 6 |
| Blank First | `control_blank_first` | `uncommon` | 167 | 51 | 24 | 0 |
| 罠糸の加護 | `blessing_trap_web` | `rare` | 111 | 36 | 18 | 0 |
| 防壁の加護 | `blessing_barrier` | `rare` | 100 | 25 | 11 | 0 |
| 攻の加護 | `blessing_attack` | `rare` | 94 | 19 | 11 | 0 |
| 見切りの加護 | `blessing_insight` | `rare` | 93 | 17 | 7 | 0 |
| 知恵の加護 | `blessing_draw` | `rare` | 92 | 18 | 11 | 0 |
| 速の加護 | `blessing_speed` | `rare` | 91 | 27 | 11 | 0 |
| 鈍足の加護 | `blessing_slow` | `rare` | 89 | 14 | 6 | 0 |
| 防の加護 | `blessing_guard` | `rare` | 87 | 19 | 5 | 0 |
| 抑制の加護 | `blessing_suppression` | `rare` | 78 | 28 | 8 | 0 |
| 攻勢の加護 | `blessing_offense` | `rare` | 68 | 23 | 10 | 0 |

### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 罠糸の加護 | `blessing_trap_web` | 111 | 45.9% | 111 | 36 | 36 | 6 | 6 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 99 | 50.5% | 100 | 25 | 25 | 10 | 10 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 94 | 47.9% | 94 | 19 | 19 | 0 | 0 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 93 | 48.4% | 93 | 17 | 17 | 17 | 0 | 0 | 17 |
| 知恵の加護 | `blessing_draw` | 92 | 39.1% | 92 | 18 | 18 | 0 | 0 | 0 | 0 |
| 速の加護 | `blessing_speed` | 90 | 41.1% | 91 | 27 | 27 | 0 | 0 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 88 | 46.6% | 89 | 14 | 14 | 2 | 2 | 0 | 0 |
| 防の加護 | `blessing_guard` | 87 | 44.8% | 87 | 19 | 19 | 0 | 0 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 77 | 36.4% | 78 | 28 | 28 | 1 | 1 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 67 | 44.8% | 68 | 23 | 23 | 6 | 6 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 8000 | 2254 | 28.2% | 990 | 43.9% | 403 |
| `uncommon` | 8000 | 2570 | 32.1% | 1247 | 48.5% | 778 |
| `rare` | 4000 | 1146 | 28.6% | 581 | 50.7% | 320 |

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
- Draw Rate: 5.8%
- First Pass Win Rate: 44.3%
- Win With Fewer Cards: 15.6%
- Win With Same Cards: 51.7%
- Win With More Cards: 32.7%
- Winner Facedown Avg: 3.17
- Loser Facedown Avg: 3.01
- Starting Player Win Rate: 45.5%
- Responding Player Win Rate: 48.0%
- Final Stats Avg: A=3.23, B=1.01, S=1.47
- Losing Final Stats Avg: A=2.31, B=0.98, S=1.32
- Lost With Speed Advantage: 166 (16.6%)
- Won After Blocking Faster Attack: 179 (38.2%)
- Action Rates: set=72.3%, set_pass=2.0%, pass=25.7%
- set_pass Candidate Avg / Match: 16.45
- Turns: min=1, avg=1.58, max=8
- Battle / Control / Blessing: avg=12.89 / 6.14 / 0.97
- Role Colors: red=6.54, blue=3.72, green=3.5, white=6.23
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 1272 |
| 2 | 防御 | 1240 |
| 3 | 圧迫 | 1194 |
| 4 | ステップ | 1183 |
| 5 | 構え | 1091 |
| 6 | 牽制 | 1015 |
| 7 | 集中 | 1005 |
| 8 | 崩し | 681 |
| 9 | 貫き | 673 |
| 10 | 返し刃 | 543 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 607 |
| 2 | 防御 | 565 |
| 3 | 圧迫 | 546 |
| 4 | ステップ | 544 |
| 5 | 構え | 520 |
| 6 | 集中 | 482 |
| 7 | 牽制 | 480 |
| 8 | 貫き | 338 |
| 9 | 崩し | 336 |
| 10 | 踏ん張り | 261 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 1272 | 355 | 157 | 112 |
| 防御 | `battle_defend` | `common` | 1240 | 356 | 156 | 85 |
| 圧迫 | `control_pressure` | `common` | 1194 | 367 | 158 | 28 |
| ステップ | `battle_step` | `common` | 1183 | 316 | 126 | 73 |
| 構え | `control_guard` | `common` | 1091 | 318 | 130 | 35 |
| 牽制 | `control_disrupt` | `common` | 1015 | 311 | 138 | 10 |
| 集中 | `control_focus` | `common` | 1005 | 276 | 107 | 35 |
| 崩し | `battle_break` | `uncommon` | 681 | 199 | 124 | 108 |
| 貫き | `battle_pierce` | `uncommon` | 673 | 225 | 144 | 127 |
| 返し刃 | `battle_counter` | `uncommon` | 543 | 172 | 94 | 64 |
| 踏ん張り | `battle_brace` | `uncommon` | 529 | 183 | 88 | 56 |
| 粉砕 | `battle_crush` | `uncommon` | 508 | 163 | 81 | 68 |
| 十字受け | `battle_cross_guard` | `uncommon` | 495 | 161 | 75 | 40 |
| Bastion | `battle_bastion` | `uncommon` | 472 | 160 | 65 | 31 |
| フェイント | `battle_feint` | `uncommon` | 437 | 132 | 50 | 34 |
| 踏み込み | `battle_step_in` | `rare` | 428 | 155 | 99 | 90 |
| 強撃 | `battle_power_attack` | `uncommon` | 422 | 127 | 67 | 60 |
| 押し込み | `battle_press` | `uncommon` | 416 | 138 | 58 | 44 |
| Bulwark | `battle_bulwark` | `uncommon` | 414 | 133 | 60 | 36 |
| 渾身 | `battle_all_in` | `rare` | 408 | 136 | 64 | 60 |
| 退き足 | `battle_backstep` | `uncommon` | 402 | 132 | 58 | 33 |
| 大振り | `battle_heavy_swing` | `rare` | 380 | 141 | 70 | 60 |
| 鉄壁 | `battle_wall` | `rare` | 379 | 134 | 60 | 21 |
| 残像 | `battle_afterimage` | `rare` | 368 | 104 | 50 | 25 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 355 | 101 | 48 | 22 |
| 受け流し | `battle_guard` | `uncommon` | 340 | 97 | 51 | 36 |
| 疾走 | `battle_dash` | `rare` | 317 | 107 | 61 | 46 |
| Crush Spirit | `control_crush_spirit` | `rare` | 264 | 86 | 44 | 1 |
| 蓄え | `control_reserve` | `rare` | 259 | 101 | 44 | 3 |
| 受け直し | `control_cover` | `uncommon` | 251 | 87 | 38 | 9 |
| Tripwire | `battle_tripwire` | `rare` | 229 | 0 | 0 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 212 | 57 | 29 | 8 |
| 加速 | `control_haste` | `uncommon` | 181 | 56 | 23 | 7 |
| 重心落とし | `control_anchor` | `uncommon` | 180 | 48 | 21 | 5 |
| 補強 | `control_fortify` | `uncommon` | 179 | 54 | 28 | 7 |
| Blank First | `control_blank_first` | `uncommon` | 161 | 52 | 28 | 1 |
| 勢い溜め | `control_momentum` | `uncommon` | 149 | 42 | 17 | 3 |
| 防壁の加護 | `blessing_barrier` | `rare` | 103 | 24 | 9 | 0 |
| 見切りの加護 | `blessing_insight` | `rare` | 102 | 21 | 8 | 0 |
| 罠糸の加護 | `blessing_trap_web` | `rare` | 101 | 27 | 7 | 0 |
| 抑制の加護 | `blessing_suppression` | `rare` | 101 | 23 | 8 | 0 |
| 防の加護 | `blessing_guard` | `rare` | 100 | 25 | 15 | 0 |
| 攻勢の加護 | `blessing_offense` | `rare` | 96 | 22 | 12 | 0 |
| 速の加護 | `blessing_speed` | `rare` | 94 | 21 | 7 | 0 |
| 鈍足の加護 | `blessing_slow` | `rare` | 93 | 22 | 13 | 0 |
| 知恵の加護 | `blessing_draw` | `rare` | 92 | 25 | 11 | 0 |
| 攻の加護 | `blessing_attack` | `rare` | 86 | 22 | 10 | 0 |

### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 防壁の加護 | `blessing_barrier` | 102 | 44.1% | 103 | 24 | 24 | 4 | 4 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 101 | 46.5% | 102 | 21 | 21 | 21 | 0 | 0 | 21 |
| 罠糸の加護 | `blessing_trap_web` | 101 | 45.5% | 101 | 27 | 27 | 9 | 9 | 0 | 0 |
| 防の加護 | `blessing_guard` | 100 | 55.0% | 100 | 25 | 25 | 0 | 0 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 100 | 42.0% | 101 | 23 | 23 | 2 | 2 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 96 | 46.9% | 96 | 22 | 22 | 7 | 7 | 0 | 0 |
| 速の加護 | `blessing_speed` | 94 | 44.7% | 94 | 21 | 21 | 0 | 0 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 93 | 52.7% | 93 | 22 | 22 | 4 | 4 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 91 | 40.7% | 92 | 25 | 25 | 0 | 0 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 86 | 40.7% | 86 | 22 | 22 | 0 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 8000 | 2299 | 28.7% | 972 | 42.3% | 378 |
| `uncommon` | 8000 | 2519 | 31.5% | 1247 | 49.5% | 799 |
| `rare` | 4000 | 1196 | 29.9% | 592 | 49.5% | 306 |

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
