# Draft Report

## Configuration

- Draft Bot 1: `StandardDraftBot`
- Draft Bot 2: `StandardDraftBot`
- Play Bot 1: `StandardBot`
- Play Bot 2: `StandardBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 1891
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
| `StandardDraftBot` | 2000 | 934 | 934 | 132 | 46.7% | 42.0% | 22.5% | 31.6% | 45.9% | 2.97 | 2.73 | 46.2% | 47.2% | 70.3% | 2.1% | 27.6% | 13.88 | 6.12 | 7.1 | 3.45 | 3.33 | 6.12 | 8 | 8 | 4 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| StandardDraftBot vs StandardDraftBot | 1000 | 66 | `StandardDraftBot`=934 | 1.41 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 595 |
| 2 | 防御 | 587 |
| 3 | 牽制 | 555 |
| 4 | ステップ | 542 |
| 5 | 圧迫 | 483 |
| 6 | 踏み込み | 472 |
| 7 | 渾身 | 424 |
| 8 | 貫き | 398 |
| 9 | 大振り | 398 |
| 10 | 崩し | 366 |
| 11 | 鉄壁 | 330 |
| 12 | 踏ん張り | 325 |
| 13 | 構え | 315 |
| 14 | 返し刃 | 312 |
| 15 | 残像 | 312 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 329 |
| 2 | 攻撃 | 261 |
| 3 | 貫き | 242 |
| 4 | 防御 | 231 |
| 5 | ステップ | 225 |
| 6 | 牽制 | 224 |
| 7 | 圧迫 | 218 |
| 8 | 崩し | 216 |
| 9 | 渾身 | 175 |
| 10 | 返し刃 | 175 |
| 11 | 大振り | 170 |
| 12 | 鉄壁 | 166 |
| 13 | 残像 | 155 |
| 14 | 粉砕 | 154 |
| 15 | 構え | 136 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 316 |
| 2 | 貫き | 215 |
| 3 | 攻撃 | 202 |
| 4 | 崩し | 194 |
| 5 | 渾身 | 167 |
| 6 | 大振り | 163 |
| 7 | ステップ | 162 |
| 8 | 粉砕 | 140 |
| 9 | 防御 | 132 |
| 10 | 返し刃 | 132 |
| 11 | 残像 | 123 |
| 12 | 強撃 | 88 |
| 13 | 踏ん張り | 85 |
| 14 | 十字受け | 83 |
| 15 | フェイント | 77 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `StandardDraftBot` | 4.01 | 0.93 | 1.59 | 3.37 | 0.97 | 1.16 | 272 (13.6%) | 272 (29.1%) |

## Drafter Details

### StandardDraftBot

- Win Rate: 46.7%
- Draw Rate: 6.6%
- First Pass Win Rate: 42.0%
- Win With Fewer Cards: 22.5%
- Win With Same Cards: 31.6%
- Win With More Cards: 45.9%
- Winner Facedown Avg: 2.97
- Loser Facedown Avg: 2.73
- Starting Player Win Rate: 46.2%
- Responding Player Win Rate: 47.2%
- Final Stats Avg: A=4.01, B=0.93, S=1.59
- Losing Final Stats Avg: A=3.37, B=0.97, S=1.16
- Lost With Speed Advantage: 272 (13.6%)
- Won After Blocking Faster Attack: 272 (29.1%)
- Action Rates: set=70.3%, set_pass=2.1%, pass=27.6%
- set_pass Candidate Avg / Match: 12.36
- Turns: min=1, avg=1.41, max=4
- Battle / Control: avg=13.88 / 6.12
- Role Colors: red=7.1, blue=3.45, green=3.33, white=6.12
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 2527 |
| 2 | 防御 | 2438 |
| 3 | 圧迫 | 2379 |
| 4 | ステップ | 2286 |
| 5 | 構え | 2224 |
| 6 | 集中 | 2084 |
| 7 | 牽制 | 2062 |
| 8 | 踏み込み | 1591 |
| 9 | 渾身 | 1370 |
| 10 | 貫き | 1338 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 1174 |
| 2 | 圧迫 | 1131 |
| 3 | 防御 | 1130 |
| 4 | 構え | 1075 |
| 5 | ステップ | 1048 |
| 6 | 牽制 | 961 |
| 7 | 集中 | 953 |
| 8 | 踏み込み | 833 |
| 9 | 貫き | 655 |
| 10 | 崩し | 642 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 2527 | 595 | 261 | 202 |
| 防御 | `battle_defend` | `common` | 2438 | 587 | 231 | 132 |
| 圧迫 | `control_pressure` | `common` | 2379 | 483 | 218 | 0 |
| ステップ | `battle_step` | `common` | 2286 | 542 | 225 | 162 |
| 構え | `control_guard` | `common` | 2224 | 315 | 136 | 0 |
| 集中 | `control_focus` | `common` | 2084 | 207 | 82 | 0 |
| 牽制 | `control_disrupt` | `common` | 2062 | 555 | 224 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 1591 | 472 | 329 | 316 |
| 渾身 | `battle_all_in` | `rare` | 1370 | 424 | 175 | 167 |
| 貫き | `battle_pierce` | `uncommon` | 1338 | 398 | 242 | 215 |
| 崩し | `battle_break` | `uncommon` | 1314 | 366 | 216 | 194 |
| 大振り | `battle_heavy_swing` | `rare` | 1208 | 398 | 170 | 163 |
| 鉄壁 | `battle_wall` | `rare` | 1130 | 330 | 166 | 69 |
| 返し刃 | `battle_counter` | `uncommon` | 1088 | 312 | 175 | 132 |
| 踏ん張り | `battle_brace` | `uncommon` | 1086 | 325 | 120 | 85 |
| 粉砕 | `battle_crush` | `uncommon` | 1037 | 308 | 154 | 140 |
| 残像 | `battle_afterimage` | `rare` | 1034 | 312 | 155 | 123 |
| 十字受け | `battle_cross_guard` | `uncommon` | 1006 | 289 | 134 | 83 |
| Bastion | `battle_bastion` | `uncommon` | 910 | 273 | 117 | 62 |
| 強撃 | `battle_power_attack` | `uncommon` | 887 | 225 | 103 | 88 |
| 退き足 | `battle_backstep` | `uncommon` | 865 | 239 | 91 | 61 |
| フェイント | `battle_feint` | `uncommon` | 854 | 248 | 110 | 77 |
| Bulwark | `battle_bulwark` | `uncommon` | 759 | 219 | 105 | 63 |
| 押し込み | `battle_press` | `uncommon` | 756 | 217 | 97 | 75 |
| 受け流し | `battle_guard` | `uncommon` | 731 | 185 | 82 | 58 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 695 | 176 | 68 | 34 |
| 疾走 | `battle_dash` | `rare` | 651 | 174 | 91 | 71 |
| 受け直し | `control_cover` | `uncommon` | 517 | 131 | 67 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 438 | 81 | 45 | 0 |
| 蓄え | `control_reserve` | `rare` | 422 | 107 | 47 | 0 |
| Crush Spirit | `control_crush_spirit` | `rare` | 389 | 106 | 57 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 370 | 52 | 26 | 0 |
| 補強 | `control_fortify` | `uncommon` | 357 | 68 | 36 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 348 | 55 | 34 | 0 |
| 加速 | `control_haste` | `uncommon` | 347 | 65 | 27 | 0 |
| Blank First | `control_blank_first` | `uncommon` | 297 | 70 | 33 | 0 |
| Tripwire | `battle_tripwire` | `rare` | 205 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 16000 | 3284 | 20.5% | 1377 | 41.9% | 496 |
| `uncommon` | 16000 | 4302 | 26.9% | 2082 | 48.4% | 1367 |
| `rare` | 8000 | 2323 | 29.0% | 1190 | 51.2% | 909 |

#### Match Logs

- [draft_match_0001](matches/match_0001_StandardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0001](matches/match_0001_StandardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0002](matches/match_0002_StandardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0002](matches/match_0002_StandardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0003](matches/match_0003_StandardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0003](matches/match_0003_StandardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0004](matches/match_0004_StandardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0004](matches/match_0004_StandardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0005](matches/match_0005_StandardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0005](matches/match_0005_StandardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0006](matches/match_0006_StandardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0006](matches/match_0006_StandardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0007](matches/match_0007_StandardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0007](matches/match_0007_StandardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0008](matches/match_0008_StandardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0008](matches/match_0008_StandardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0009](matches/match_0009_StandardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0009](matches/match_0009_StandardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0010](matches/match_0010_StandardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0010](matches/match_0010_StandardDraftBot_vs_StandardDraftBot.md)
