# Draft Report

## Configuration

- Draft Bot 1: `StandardDraftBot`
- Draft Bot 2: `GuardDraftBot`
- Play Bot 1: `StandardBot`
- Play Bot 2: `GuardBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 3901
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
| `GuardDraftBot` | 1000 | 469 | 462 | 69 | 46.9% | 41.8% | 16.2% | 58.0% | 25.8% | 3.17 | 2.94 | 44.1% | 49.5% | 72.9% | 1.5% | 25.5% | 12.98 | 6.09 | 0.93 | 6.48 | 3.67 | 3.66 | 6.19 | 8 | 8 | 4 |
| `StandardDraftBot` | 1000 | 462 | 469 | 69 | 46.2% | 43.2% | 15.2% | 54.5% | 30.3% | 3.09 | 3.07 | 43.5% | 49.1% | 72.4% | 2.5% | 25.1% | 12.93 | 6.15 | 0.92 | 6.53 | 3.86 | 3.36 | 6.25 | 8 | 8 | 4 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| GuardDraftBot vs StandardDraftBot | 1000 | 69 | `GuardDraftBot`=469, `StandardDraftBot`=462 | 1.59 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 圧迫 | 762 |
| 2 | 防御 | 717 |
| 3 | 攻撃 | 679 |
| 4 | 牽制 | 605 |
| 5 | 構え | 601 |
| 6 | ステップ | 564 |
| 7 | 集中 | 556 |
| 8 | 貫き | 413 |
| 9 | 崩し | 396 |
| 10 | 踏ん張り | 351 |
| 11 | 十字受け | 345 |
| 12 | 返し刃 | 332 |
| 13 | Bastion | 326 |
| 14 | 粉砕 | 324 |
| 15 | 踏み込み | 295 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 圧迫 | 340 |
| 2 | 防御 | 314 |
| 3 | 牽制 | 280 |
| 4 | 攻撃 | 278 |
| 5 | 崩し | 260 |
| 6 | 構え | 260 |
| 7 | 貫き | 253 |
| 8 | ステップ | 226 |
| 9 | 集中 | 213 |
| 10 | 踏み込み | 204 |
| 11 | 十字受け | 179 |
| 12 | 返し刃 | 171 |
| 13 | 粉砕 | 164 |
| 14 | 踏ん張り | 163 |
| 15 | 大振り | 139 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 貫き | 227 |
| 2 | 崩し | 223 |
| 3 | 攻撃 | 204 |
| 4 | 踏み込み | 196 |
| 5 | 防御 | 154 |
| 6 | ステップ | 144 |
| 7 | 粉砕 | 133 |
| 8 | 大振り | 127 |
| 9 | 返し刃 | 118 |
| 10 | 渾身 | 115 |
| 11 | 強撃 | 109 |
| 12 | 踏ん張り | 101 |
| 13 | 十字受け | 99 |
| 14 | 疾走 | 99 |
| 15 | 押し込み | 91 |

### Blessing Involvement Overall

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 速の加護 | `blessing_speed` | 207 | 49.8% | 210 | 47 | 47 | 0 | 0 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 200 | 42.0% | 200 | 49 | 49 | 0 | 0 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 196 | 41.8% | 198 | 67 | 67 | 12 | 12 | 0 | 0 |
| 防の加護 | `blessing_guard` | 191 | 44.5% | 192 | 42 | 42 | 0 | 0 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 190 | 52.1% | 193 | 38 | 38 | 38 | 0 | 0 | 38 |
| 防壁の加護 | `blessing_barrier` | 182 | 42.9% | 182 | 43 | 43 | 13 | 13 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 176 | 42.0% | 176 | 38 | 38 | 4 | 4 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 168 | 50.6% | 170 | 43 | 43 | 12 | 12 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 167 | 53.3% | 169 | 37 | 37 | 4 | 4 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 158 | 50.0% | 158 | 41 | 41 | 0 | 0 | 0 | 0 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `GuardDraftBot` | 3.07 | 1.01 | 1.5 | 2.08 | 1.12 | 1.22 | 162 (16.2%) | 148 (31.6%) |
| `StandardDraftBot` | 3.3 | 0.99 | 1.51 | 2.49 | 0.95 | 1.3 | 148 (14.8%) | 162 (35.1%) |

## Drafter Details

### GuardDraftBot

- Win Rate: 46.9%
- Draw Rate: 6.9%
- First Pass Win Rate: 41.8%
- Win With Fewer Cards: 16.2%
- Win With Same Cards: 58.0%
- Win With More Cards: 25.8%
- Winner Facedown Avg: 3.17
- Loser Facedown Avg: 2.94
- Starting Player Win Rate: 44.1%
- Responding Player Win Rate: 49.5%
- Final Stats Avg: A=3.07, B=1.01, S=1.5
- Losing Final Stats Avg: A=2.08, B=1.12, S=1.22
- Lost With Speed Advantage: 162 (16.2%)
- Won After Blocking Faster Attack: 148 (31.6%)
- Action Rates: set=72.9%, set_pass=1.5%, pass=25.5%
- set_pass Candidate Avg / Match: 17.55
- Turns: min=1, avg=1.59, max=8
- Battle / Control / Blessing: avg=12.98 / 6.09 / 0.93
- Role Colors: red=6.48, blue=3.67, green=3.66, white=6.19
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 1308 |
| 2 | 防御 | 1241 |
| 3 | 圧迫 | 1201 |
| 4 | ステップ | 1138 |
| 5 | 構え | 1072 |
| 6 | 集中 | 1038 |
| 7 | 牽制 | 1002 |
| 8 | 貫き | 645 |
| 9 | 崩し | 635 |
| 10 | 返し刃 | 578 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 627 |
| 2 | 防御 | 570 |
| 3 | 圧迫 | 559 |
| 4 | ステップ | 528 |
| 5 | 構え | 509 |
| 6 | 牽制 | 488 |
| 7 | 集中 | 471 |
| 8 | 貫き | 332 |
| 9 | 崩し | 316 |
| 10 | 返し刃 | 271 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 1308 | 346 | 150 | 111 |
| 防御 | `battle_defend` | `common` | 1241 | 373 | 172 | 86 |
| 圧迫 | `control_pressure` | `common` | 1201 | 380 | 173 | 33 |
| ステップ | `battle_step` | `common` | 1138 | 231 | 90 | 50 |
| 構え | `control_guard` | `common` | 1072 | 298 | 131 | 35 |
| 集中 | `control_focus` | `common` | 1038 | 288 | 106 | 37 |
| 牽制 | `control_disrupt` | `common` | 1002 | 309 | 153 | 11 |
| 貫き | `battle_pierce` | `uncommon` | 645 | 204 | 130 | 112 |
| 崩し | `battle_break` | `uncommon` | 635 | 194 | 134 | 116 |
| 返し刃 | `battle_counter` | `uncommon` | 578 | 181 | 96 | 65 |
| 踏ん張り | `battle_brace` | `uncommon` | 547 | 180 | 86 | 55 |
| Bastion | `battle_bastion` | `uncommon` | 523 | 181 | 72 | 23 |
| 十字受け | `battle_cross_guard` | `uncommon` | 512 | 160 | 84 | 54 |
| 粉砕 | `battle_crush` | `uncommon` | 480 | 135 | 77 | 63 |
| 踏み込み | `battle_step_in` | `rare` | 460 | 158 | 111 | 109 |
| Bulwark | `battle_bulwark` | `uncommon` | 428 | 148 | 67 | 31 |
| 鉄壁 | `battle_wall` | `rare` | 424 | 151 | 76 | 20 |
| 押し込み | `battle_press` | `uncommon` | 423 | 139 | 71 | 47 |
| 受け流し | `battle_guard` | `uncommon` | 417 | 122 | 60 | 33 |
| 強撃 | `battle_power_attack` | `uncommon` | 416 | 131 | 70 | 60 |
| 退き足 | `battle_backstep` | `uncommon` | 411 | 128 | 53 | 25 |
| 渾身 | `battle_all_in` | `rare` | 397 | 115 | 60 | 59 |
| 残像 | `battle_afterimage` | `rare` | 362 | 115 | 53 | 33 |
| フェイント | `battle_feint` | `uncommon` | 362 | 100 | 49 | 31 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 361 | 120 | 54 | 25 |
| 疾走 | `battle_dash` | `rare` | 341 | 114 | 70 | 54 |
| 大振り | `battle_heavy_swing` | `rare` | 332 | 114 | 53 | 51 |
| Crush Spirit | `control_crush_spirit` | `rare` | 261 | 85 | 48 | 3 |
| 蓄え | `control_reserve` | `rare` | 254 | 90 | 37 | 6 |
| 受け直し | `control_cover` | `uncommon` | 253 | 88 | 44 | 8 |
| Tripwire | `battle_tripwire` | `rare` | 239 | 1 | 0 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 207 | 74 | 33 | 9 |
| 重心落とし | `control_anchor` | `uncommon` | 178 | 61 | 26 | 10 |
| 補強 | `control_fortify` | `uncommon` | 169 | 58 | 26 | 7 |
| 勢い溜め | `control_momentum` | `uncommon` | 159 | 46 | 19 | 4 |
| 加速 | `control_haste` | `uncommon` | 151 | 45 | 20 | 8 |
| Blank First | `control_blank_first` | `uncommon` | 145 | 45 | 22 | 1 |
| 速の加護 | `blessing_speed` | `rare` | 106 | 22 | 9 | 0 |
| 罠糸の加護 | `blessing_trap_web` | `rare` | 101 | 32 | 16 | 0 |
| 鈍足の加護 | `blessing_slow` | `rare` | 100 | 18 | 9 | 0 |
| 攻勢の加護 | `blessing_offense` | `rare` | 98 | 25 | 13 | 0 |
| 見切りの加護 | `blessing_insight` | `rare` | 98 | 19 | 8 | 0 |
| 知恵の加護 | `blessing_draw` | `rare` | 96 | 23 | 9 | 0 |
| 抑制の加護 | `blessing_suppression` | `rare` | 86 | 18 | 5 | 0 |
| 防の加護 | `blessing_guard` | `rare` | 83 | 19 | 9 | 0 |
| 防壁の加護 | `blessing_barrier` | `rare` | 83 | 17 | 8 | 0 |
| 攻の加護 | `blessing_attack` | `rare` | 79 | 15 | 8 | 0 |

### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 速の加護 | `blessing_speed` | 104 | 47.1% | 106 | 22 | 22 | 0 | 0 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 99 | 46.5% | 100 | 18 | 18 | 3 | 3 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 99 | 40.4% | 101 | 32 | 32 | 8 | 8 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 97 | 52.6% | 98 | 19 | 19 | 19 | 0 | 0 | 19 |
| 知恵の加護 | `blessing_draw` | 96 | 46.9% | 96 | 23 | 23 | 0 | 0 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 96 | 45.8% | 98 | 25 | 25 | 6 | 6 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 86 | 46.5% | 86 | 18 | 18 | 4 | 4 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 83 | 43.4% | 83 | 17 | 17 | 6 | 6 | 0 | 0 |
| 防の加護 | `blessing_guard` | 83 | 42.2% | 83 | 19 | 19 | 0 | 0 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 79 | 53.2% | 79 | 15 | 15 | 0 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 8000 | 2225 | 27.8% | 975 | 43.8% | 363 |
| `uncommon` | 8000 | 2540 | 31.8% | 1293 | 50.9% | 787 |
| `rare` | 4000 | 1151 | 28.8% | 602 | 52.3% | 335 |

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
- First Pass Win Rate: 43.2%
- Win With Fewer Cards: 15.2%
- Win With Same Cards: 54.5%
- Win With More Cards: 30.3%
- Winner Facedown Avg: 3.09
- Loser Facedown Avg: 3.07
- Starting Player Win Rate: 43.5%
- Responding Player Win Rate: 49.1%
- Final Stats Avg: A=3.3, B=0.99, S=1.51
- Losing Final Stats Avg: A=2.49, B=0.95, S=1.3
- Lost With Speed Advantage: 148 (14.8%)
- Won After Blocking Faster Attack: 162 (35.1%)
- Action Rates: set=72.4%, set_pass=2.5%, pass=25.1%
- set_pass Candidate Avg / Match: 17.55
- Turns: min=1, avg=1.59, max=8
- Battle / Control / Blessing: avg=12.93 / 6.15 / 0.92
- Role Colors: red=6.53, blue=3.86, green=3.36, white=6.25
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 1262 |
| 2 | ステップ | 1226 |
| 3 | 防御 | 1208 |
| 4 | 圧迫 | 1182 |
| 5 | 構え | 1114 |
| 6 | 牽制 | 1010 |
| 7 | 集中 | 998 |
| 8 | 貫き | 669 |
| 9 | 崩し | 659 |
| 10 | 粉砕 | 547 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 576 |
| 2 | 防御 | 570 |
| 3 | ステップ | 569 |
| 4 | 圧迫 | 549 |
| 5 | 構え | 536 |
| 6 | 牽制 | 452 |
| 7 | 集中 | 444 |
| 8 | 崩し | 335 |
| 9 | 貫き | 327 |
| 10 | 十字受け | 251 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 1262 | 333 | 128 | 93 |
| ステップ | `battle_step` | `common` | 1226 | 333 | 136 | 94 |
| 防御 | `battle_defend` | `common` | 1208 | 344 | 142 | 68 |
| 圧迫 | `control_pressure` | `common` | 1182 | 382 | 167 | 33 |
| 構え | `control_guard` | `common` | 1114 | 303 | 129 | 30 |
| 牽制 | `control_disrupt` | `common` | 1010 | 296 | 127 | 11 |
| 集中 | `control_focus` | `common` | 998 | 268 | 107 | 38 |
| 貫き | `battle_pierce` | `uncommon` | 669 | 209 | 123 | 115 |
| 崩し | `battle_break` | `uncommon` | 659 | 202 | 126 | 107 |
| 粉砕 | `battle_crush` | `uncommon` | 547 | 189 | 87 | 70 |
| 返し刃 | `battle_counter` | `uncommon` | 534 | 151 | 75 | 53 |
| 十字受け | `battle_cross_guard` | `uncommon` | 527 | 185 | 95 | 45 |
| 踏ん張り | `battle_brace` | `uncommon` | 489 | 171 | 77 | 46 |
| 退き足 | `battle_backstep` | `uncommon` | 454 | 138 | 54 | 28 |
| 大振り | `battle_heavy_swing` | `rare` | 442 | 164 | 86 | 76 |
| フェイント | `battle_feint` | `uncommon` | 430 | 131 | 57 | 39 |
| 強撃 | `battle_power_attack` | `uncommon` | 430 | 128 | 60 | 49 |
| Bastion | `battle_bastion` | `uncommon` | 426 | 145 | 52 | 15 |
| 踏み込み | `battle_step_in` | `rare` | 424 | 137 | 93 | 87 |
| 渾身 | `battle_all_in` | `rare` | 422 | 150 | 64 | 56 |
| 押し込み | `battle_press` | `uncommon` | 408 | 130 | 64 | 44 |
| Bulwark | `battle_bulwark` | `uncommon` | 385 | 129 | 53 | 28 |
| 残像 | `battle_afterimage` | `rare` | 366 | 124 | 61 | 33 |
| 受け流し | `battle_guard` | `uncommon` | 361 | 119 | 49 | 34 |
| 鉄壁 | `battle_wall` | `rare` | 348 | 123 | 55 | 26 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 329 | 96 | 35 | 16 |
| 疾走 | `battle_dash` | `rare` | 327 | 116 | 56 | 45 |
| 受け直し | `control_cover` | `uncommon` | 261 | 81 | 42 | 6 |
| Tripwire | `battle_tripwire` | `rare` | 259 | 0 | 0 | 0 |
| 蓄え | `control_reserve` | `rare` | 248 | 81 | 30 | 0 |
| Crush Spirit | `control_crush_spirit` | `rare` | 246 | 90 | 45 | 1 |
| 前のめり | `control_overclock` | `uncommon` | 229 | 73 | 35 | 10 |
| 重心落とし | `control_anchor` | `uncommon` | 197 | 56 | 23 | 10 |
| 補強 | `control_fortify` | `uncommon` | 185 | 60 | 29 | 6 |
| 勢い溜め | `control_momentum` | `uncommon` | 163 | 37 | 14 | 1 |
| 加速 | `control_haste` | `uncommon` | 162 | 57 | 28 | 10 |
| Blank First | `control_blank_first` | `uncommon` | 155 | 52 | 22 | 3 |
| 防の加護 | `blessing_guard` | `rare` | 109 | 23 | 11 | 0 |
| 知恵の加護 | `blessing_draw` | `rare` | 104 | 26 | 11 | 0 |
| 速の加護 | `blessing_speed` | `rare` | 104 | 25 | 11 | 0 |
| 防壁の加護 | `blessing_barrier` | `rare` | 99 | 26 | 12 | 0 |
| 罠糸の加護 | `blessing_trap_web` | `rare` | 97 | 35 | 17 | 0 |
| 見切りの加護 | `blessing_insight` | `rare` | 95 | 19 | 7 | 0 |
| 抑制の加護 | `blessing_suppression` | `rare` | 90 | 20 | 5 | 0 |
| 攻の加護 | `blessing_attack` | `rare` | 79 | 26 | 14 | 0 |
| 攻勢の加護 | `blessing_offense` | `rare` | 72 | 18 | 10 | 0 |
| 鈍足の加護 | `blessing_slow` | `rare` | 69 | 19 | 11 | 0 |

### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 防の加護 | `blessing_guard` | 108 | 46.3% | 109 | 23 | 23 | 0 | 0 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 104 | 37.5% | 104 | 26 | 26 | 0 | 0 | 0 | 0 |
| 速の加護 | `blessing_speed` | 103 | 52.4% | 104 | 25 | 25 | 0 | 0 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 99 | 42.4% | 99 | 26 | 26 | 7 | 7 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 97 | 43.3% | 97 | 35 | 35 | 4 | 4 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 93 | 51.6% | 95 | 19 | 19 | 19 | 0 | 0 | 19 |
| 抑制の加護 | `blessing_suppression` | 90 | 37.8% | 90 | 20 | 20 | 0 | 0 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 79 | 46.8% | 79 | 26 | 26 | 0 | 0 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 72 | 56.9% | 72 | 18 | 18 | 6 | 6 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 68 | 63.2% | 69 | 19 | 19 | 1 | 1 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 8000 | 2259 | 28.2% | 936 | 41.4% | 367 |
| `uncommon` | 8000 | 2539 | 31.7% | 1200 | 47.3% | 735 |
| `rare` | 4000 | 1222 | 30.6% | 599 | 49.0% | 324 |

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
