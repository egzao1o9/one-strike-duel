# Draft Report

## Configuration

- Draft Bot 1: `AggroDraftBot`
- Draft Bot 2: `GuardDraftBot`
- Play Bot 1: `AggroBot`
- Play Bot 2: `GuardBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 5901
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
| `AggroDraftBot` | 1000 | 478 | 455 | 67 | 47.8% | 44.6% | 14.4% | 54.6% | 31.0% | 3.14 | 3.18 | 46.5% | 49.2% | 72.4% | 2.4% | 25.2% | 13 | 6.08 | 0.92 | 6.68 | 3.78 | 3.37 | 6.17 | 8 | 8 | 4 |
| `GuardDraftBot` | 1000 | 455 | 478 | 67 | 45.5% | 42.0% | 14.1% | 58.5% | 27.5% | 3.32 | 2.97 | 43.8% | 47.1% | 72.9% | 1.6% | 25.5% | 12.96 | 6.1 | 0.95 | 6.35 | 3.77 | 3.69 | 6.2 | 8 | 8 | 4 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| AggroDraftBot vs GuardDraftBot | 1000 | 67 | `AggroDraftBot`=478, `GuardDraftBot`=455 | 1.6 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 圧迫 | 749 |
| 2 | 攻撃 | 691 |
| 3 | 防御 | 667 |
| 4 | 牽制 | 586 |
| 5 | 構え | 572 |
| 6 | ステップ | 572 |
| 7 | 集中 | 549 |
| 8 | 崩し | 450 |
| 9 | 貫き | 441 |
| 10 | 返し刃 | 355 |
| 11 | 十字受け | 345 |
| 12 | 踏ん張り | 345 |
| 13 | 踏み込み | 326 |
| 14 | 粉砕 | 313 |
| 15 | 残像 | 284 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 圧迫 | 321 |
| 2 | 攻撃 | 302 |
| 3 | 牽制 | 277 |
| 4 | 防御 | 274 |
| 5 | 崩し | 273 |
| 6 | 貫き | 261 |
| 7 | 構え | 235 |
| 8 | 踏み込み | 232 |
| 9 | 集中 | 222 |
| 10 | ステップ | 215 |
| 11 | 返し刃 | 183 |
| 12 | 十字受け | 179 |
| 13 | 踏ん張り | 167 |
| 14 | 粉砕 | 162 |
| 15 | 強撃 | 138 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 崩し | 252 |
| 2 | 貫き | 234 |
| 3 | 踏み込み | 227 |
| 4 | 攻撃 | 211 |
| 5 | 防御 | 159 |
| 6 | ステップ | 140 |
| 7 | 粉砕 | 140 |
| 8 | 返し刃 | 132 |
| 9 | 大振り | 129 |
| 10 | 渾身 | 117 |
| 11 | 踏ん張り | 110 |
| 12 | 十字受け | 99 |
| 13 | 強撃 | 99 |
| 14 | 疾走 | 90 |
| 15 | 押し込み | 84 |

### Blessing Involvement Overall

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 防壁の加護 | `blessing_barrier` | 223 | 44.4% | 226 | 52 | 52 | 9 | 9 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 213 | 44.6% | 216 | 77 | 77 | 18 | 18 | 0 | 0 |
| 防の加護 | `blessing_guard` | 189 | 43.9% | 190 | 49 | 49 | 0 | 0 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 188 | 47.9% | 188 | 55 | 55 | 18 | 18 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 187 | 46.5% | 187 | 62 | 62 | 0 | 0 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 179 | 43.6% | 181 | 29 | 29 | 29 | 0 | 0 | 29 |
| 速の加護 | `blessing_speed` | 179 | 41.3% | 182 | 49 | 49 | 0 | 0 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 173 | 42.8% | 174 | 43 | 43 | 5 | 5 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 164 | 40.9% | 164 | 30 | 30 | 0 | 0 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 158 | 39.9% | 158 | 30 | 30 | 1 | 1 | 0 | 0 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `AggroDraftBot` | 3.45 | 0.83 | 1.77 | 2.55 | 0.84 | 1.7 | 147 (14.7%) | 148 (31.0%) |
| `GuardDraftBot` | 3.13 | 1.08 | 1.57 | 1.97 | 1.2 | 1.31 | 148 (14.8%) | 147 (32.3%) |

## Drafter Details

### AggroDraftBot

- Win Rate: 47.8%
- Draw Rate: 6.7%
- First Pass Win Rate: 44.6%
- Win With Fewer Cards: 14.4%
- Win With Same Cards: 54.6%
- Win With More Cards: 31.0%
- Winner Facedown Avg: 3.14
- Loser Facedown Avg: 3.18
- Starting Player Win Rate: 46.5%
- Responding Player Win Rate: 49.2%
- Final Stats Avg: A=3.45, B=0.83, S=1.77
- Losing Final Stats Avg: A=2.55, B=0.84, S=1.7
- Lost With Speed Advantage: 147 (14.7%)
- Won After Blocking Faster Attack: 148 (31.0%)
- Action Rates: set=72.4%, set_pass=2.4%, pass=25.2%
- set_pass Candidate Avg / Match: 18.02
- Turns: min=1, avg=1.6, max=11
- Battle / Control / Blessing: avg=13 / 6.08 / 0.92
- Role Colors: red=6.68, blue=3.78, green=3.37, white=6.17
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 1357 |
| 2 | 防御 | 1198 |
| 3 | ステップ | 1175 |
| 4 | 圧迫 | 1146 |
| 5 | 構え | 1080 |
| 6 | 集中 | 1023 |
| 7 | 牽制 | 1021 |
| 8 | 貫き | 689 |
| 9 | 崩し | 634 |
| 10 | 粉砕 | 572 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 617 |
| 2 | 防御 | 571 |
| 3 | ステップ | 565 |
| 4 | 圧迫 | 546 |
| 5 | 構え | 534 |
| 6 | 集中 | 507 |
| 7 | 牽制 | 484 |
| 8 | 貫き | 353 |
| 9 | 崩し | 326 |
| 10 | 返し刃 | 269 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 1357 | 341 | 144 | 97 |
| 防御 | `battle_defend` | `common` | 1198 | 288 | 114 | 62 |
| ステップ | `battle_step` | `common` | 1175 | 325 | 126 | 83 |
| 圧迫 | `control_pressure` | `common` | 1146 | 371 | 168 | 45 |
| 構え | `control_guard` | `common` | 1080 | 281 | 110 | 28 |
| 集中 | `control_focus` | `common` | 1023 | 282 | 122 | 40 |
| 牽制 | `control_disrupt` | `common` | 1021 | 318 | 151 | 16 |
| 貫き | `battle_pierce` | `uncommon` | 689 | 217 | 133 | 119 |
| 崩し | `battle_break` | `uncommon` | 634 | 224 | 131 | 119 |
| 粉砕 | `battle_crush` | `uncommon` | 572 | 192 | 99 | 83 |
| 返し刃 | `battle_counter` | `uncommon` | 549 | 194 | 98 | 71 |
| フェイント | `battle_feint` | `uncommon` | 503 | 153 | 58 | 30 |
| 踏ん張り | `battle_brace` | `uncommon` | 499 | 164 | 75 | 54 |
| 強撃 | `battle_power_attack` | `uncommon` | 461 | 156 | 85 | 58 |
| 十字受け | `battle_cross_guard` | `uncommon` | 460 | 139 | 72 | 37 |
| 押し込み | `battle_press` | `uncommon` | 437 | 141 | 64 | 41 |
| 踏み込み | `battle_step_in` | `rare` | 428 | 163 | 112 | 110 |
| 退き足 | `battle_backstep` | `uncommon` | 423 | 128 | 52 | 32 |
| 渾身 | `battle_all_in` | `rare` | 407 | 140 | 61 | 59 |
| 大振り | `battle_heavy_swing` | `rare` | 406 | 139 | 70 | 65 |
| 残像 | `battle_afterimage` | `rare` | 405 | 156 | 70 | 41 |
| 受け流し | `battle_guard` | `uncommon` | 394 | 128 | 53 | 35 |
| Bulwark | `battle_bulwark` | `uncommon` | 392 | 125 | 53 | 24 |
| Bastion | `battle_bastion` | `uncommon` | 379 | 115 | 50 | 20 |
| 鉄壁 | `battle_wall` | `rare` | 344 | 112 | 56 | 17 |
| 疾走 | `battle_dash` | `rare` | 325 | 101 | 56 | 44 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 324 | 84 | 36 | 17 |
| 蓄え | `control_reserve` | `rare` | 266 | 112 | 45 | 2 |
| Crush Spirit | `control_crush_spirit` | `rare` | 262 | 104 | 50 | 2 |
| Tripwire | `battle_tripwire` | `rare` | 239 | 4 | 2 | 2 |
| 受け直し | `control_cover` | `uncommon` | 234 | 81 | 40 | 10 |
| 前のめり | `control_overclock` | `uncommon` | 200 | 69 | 35 | 7 |
| 勢い溜め | `control_momentum` | `uncommon` | 176 | 40 | 17 | 3 |
| Blank First | `control_blank_first` | `uncommon` | 171 | 56 | 23 | 1 |
| 補強 | `control_fortify` | `uncommon` | 170 | 55 | 22 | 6 |
| 重心落とし | `control_anchor` | `uncommon` | 170 | 51 | 21 | 12 |
| 加速 | `control_haste` | `uncommon` | 163 | 47 | 24 | 9 |
| 防壁の加護 | `blessing_barrier` | `rare` | 120 | 27 | 13 | 0 |
| 罠糸の加護 | `blessing_trap_web` | `rare` | 119 | 40 | 18 | 0 |
| 防の加護 | `blessing_guard` | `rare` | 101 | 25 | 9 | 0 |
| 攻勢の加護 | `blessing_offense` | `rare` | 93 | 35 | 12 | 0 |
| 見切りの加護 | `blessing_insight` | `rare` | 91 | 15 | 4 | 0 |
| 知恵の加護 | `blessing_draw` | `rare` | 88 | 28 | 14 | 0 |
| 速の加護 | `blessing_speed` | `rare` | 83 | 23 | 9 | 0 |
| 鈍足の加護 | `blessing_slow` | `rare` | 78 | 16 | 7 | 0 |
| 攻の加護 | `blessing_attack` | `rare` | 76 | 17 | 8 | 0 |
| 抑制の加護 | `blessing_suppression` | `rare` | 69 | 10 | 3 | 0 |

### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 防壁の加護 | `blessing_barrier` | 118 | 48.3% | 120 | 27 | 27 | 4 | 4 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 117 | 46.2% | 119 | 40 | 40 | 8 | 8 | 0 | 0 |
| 防の加護 | `blessing_guard` | 100 | 44.0% | 101 | 25 | 25 | 0 | 0 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 93 | 46.2% | 93 | 35 | 35 | 11 | 11 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 91 | 47.3% | 91 | 15 | 15 | 15 | 0 | 0 | 15 |
| 知恵の加護 | `blessing_draw` | 88 | 47.7% | 88 | 28 | 28 | 0 | 0 | 0 | 0 |
| 速の加護 | `blessing_speed` | 82 | 45.1% | 83 | 23 | 23 | 0 | 0 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 78 | 39.7% | 78 | 16 | 16 | 1 | 1 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 76 | 42.1% | 76 | 17 | 17 | 0 | 0 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 69 | 40.6% | 69 | 10 | 10 | 1 | 1 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 8000 | 2206 | 27.6% | 935 | 42.4% | 371 |
| `uncommon` | 8000 | 2559 | 32.0% | 1241 | 48.5% | 788 |
| `rare` | 4000 | 1267 | 31.7% | 619 | 48.9% | 342 |

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

- Win Rate: 45.5%
- Draw Rate: 6.7%
- First Pass Win Rate: 42.0%
- Win With Fewer Cards: 14.1%
- Win With Same Cards: 58.5%
- Win With More Cards: 27.5%
- Winner Facedown Avg: 3.32
- Loser Facedown Avg: 2.97
- Starting Player Win Rate: 43.8%
- Responding Player Win Rate: 47.1%
- Final Stats Avg: A=3.13, B=1.08, S=1.57
- Losing Final Stats Avg: A=1.97, B=1.2, S=1.31
- Lost With Speed Advantage: 148 (14.8%)
- Won After Blocking Faster Attack: 147 (32.3%)
- Action Rates: set=72.9%, set_pass=1.6%, pass=25.5%
- set_pass Candidate Avg / Match: 18.02
- Turns: min=1, avg=1.6, max=11
- Battle / Control / Blessing: avg=12.96 / 6.1 / 0.95
- Role Colors: red=6.35, blue=3.77, green=3.69, white=6.2
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 防御 | 1307 |
| 2 | 攻撃 | 1274 |
| 3 | 圧迫 | 1198 |
| 4 | ステップ | 1153 |
| 5 | 構え | 1107 |
| 6 | 集中 | 1016 |
| 7 | 牽制 | 945 |
| 8 | 崩し | 675 |
| 9 | 貫き | 624 |
| 10 | 十字受け | 577 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 588 |
| 2 | 防御 | 582 |
| 3 | ステップ | 536 |
| 4 | 構え | 533 |
| 5 | 圧迫 | 521 |
| 6 | 集中 | 445 |
| 7 | 牽制 | 435 |
| 8 | 崩し | 336 |
| 9 | 貫き | 293 |
| 10 | 十字受け | 273 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 防御 | `battle_defend` | `common` | 1307 | 379 | 160 | 97 |
| 攻撃 | `battle_attack` | `common` | 1274 | 350 | 158 | 114 |
| 圧迫 | `control_pressure` | `common` | 1198 | 378 | 153 | 24 |
| ステップ | `battle_step` | `common` | 1153 | 247 | 89 | 57 |
| 構え | `control_guard` | `common` | 1107 | 291 | 125 | 30 |
| 集中 | `control_focus` | `common` | 1016 | 267 | 100 | 35 |
| 牽制 | `control_disrupt` | `common` | 945 | 268 | 126 | 16 |
| 崩し | `battle_break` | `uncommon` | 675 | 226 | 142 | 133 |
| 貫き | `battle_pierce` | `uncommon` | 624 | 224 | 128 | 115 |
| 十字受け | `battle_cross_guard` | `uncommon` | 577 | 206 | 107 | 62 |
| 踏ん張り | `battle_brace` | `uncommon` | 541 | 181 | 92 | 56 |
| 返し刃 | `battle_counter` | `uncommon` | 532 | 161 | 85 | 61 |
| Bastion | `battle_bastion` | `uncommon` | 511 | 167 | 76 | 28 |
| 粉砕 | `battle_crush` | `uncommon` | 474 | 121 | 63 | 57 |
| 退き足 | `battle_backstep` | `uncommon` | 457 | 149 | 71 | 42 |
| 踏み込み | `battle_step_in` | `rare` | 442 | 163 | 120 | 117 |
| Bulwark | `battle_bulwark` | `uncommon` | 425 | 147 | 57 | 26 |
| 鉄壁 | `battle_wall` | `rare` | 404 | 145 | 68 | 20 |
| 受け流し | `battle_guard` | `uncommon` | 401 | 121 | 52 | 34 |
| 押し込み | `battle_press` | `uncommon` | 400 | 135 | 64 | 43 |
| 渾身 | `battle_all_in` | `rare` | 389 | 120 | 60 | 58 |
| フェイント | `battle_feint` | `uncommon` | 372 | 94 | 33 | 20 |
| 強撃 | `battle_power_attack` | `uncommon` | 364 | 105 | 53 | 41 |
| 大振り | `battle_heavy_swing` | `rare` | 361 | 125 | 66 | 64 |
| 残像 | `battle_afterimage` | `rare` | 355 | 128 | 53 | 32 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 347 | 102 | 45 | 23 |
| 疾走 | `battle_dash` | `rare` | 324 | 103 | 58 | 46 |
| 蓄え | `control_reserve` | `rare` | 277 | 102 | 45 | 8 |
| Crush Spirit | `control_crush_spirit` | `rare` | 254 | 85 | 47 | 4 |
| 受け直し | `control_cover` | `uncommon` | 254 | 82 | 37 | 4 |
| Tripwire | `battle_tripwire` | `rare` | 246 | 2 | 0 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 229 | 84 | 41 | 12 |
| 重心落とし | `control_anchor` | `uncommon` | 202 | 43 | 19 | 6 |
| 補強 | `control_fortify` | `uncommon` | 185 | 57 | 30 | 10 |
| 加速 | `control_haste` | `uncommon` | 158 | 42 | 18 | 8 |
| Blank First | `control_blank_first` | `uncommon` | 143 | 45 | 14 | 3 |
| 勢い溜め | `control_momentum` | `uncommon` | 129 | 39 | 14 | 3 |
| 防壁の加護 | `blessing_barrier` | `rare` | 106 | 25 | 9 | 0 |
| 知恵の加護 | `blessing_draw` | `rare` | 99 | 34 | 18 | 0 |
| 速の加護 | `blessing_speed` | `rare` | 99 | 26 | 7 | 0 |
| 罠糸の加護 | `blessing_trap_web` | `rare` | 97 | 37 | 15 | 0 |
| 鈍足の加護 | `blessing_slow` | `rare` | 96 | 27 | 16 | 0 |
| 攻勢の加護 | `blessing_offense` | `rare` | 95 | 20 | 11 | 0 |
| 見切りの加護 | `blessing_insight` | `rare` | 90 | 14 | 5 | 0 |
| 防の加護 | `blessing_guard` | `rare` | 89 | 24 | 12 | 0 |
| 抑制の加護 | `blessing_suppression` | `rare` | 89 | 20 | 5 | 0 |
| 攻の加護 | `blessing_attack` | `rare` | 88 | 13 | 6 | 0 |

### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 防壁の加護 | `blessing_barrier` | 105 | 40.0% | 106 | 25 | 25 | 5 | 5 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 99 | 45.5% | 99 | 34 | 34 | 0 | 0 | 0 | 0 |
| 速の加護 | `blessing_speed` | 97 | 38.1% | 99 | 26 | 26 | 0 | 0 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 96 | 42.7% | 97 | 37 | 37 | 10 | 10 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 95 | 49.5% | 95 | 20 | 20 | 7 | 7 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 95 | 45.3% | 96 | 27 | 27 | 4 | 4 | 0 | 0 |
| 防の加護 | `blessing_guard` | 89 | 43.8% | 89 | 24 | 24 | 0 | 0 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 89 | 39.3% | 89 | 20 | 20 | 0 | 0 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 88 | 39.8% | 88 | 13 | 13 | 0 | 0 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 88 | 39.8% | 90 | 14 | 14 | 14 | 0 | 0 | 14 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 8000 | 2180 | 27.3% | 911 | 41.8% | 373 |
| `uncommon` | 8000 | 2531 | 31.6% | 1241 | 49.0% | 787 |
| `rare` | 4000 | 1213 | 30.3% | 621 | 51.2% | 349 |

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
