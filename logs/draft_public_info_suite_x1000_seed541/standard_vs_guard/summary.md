# Draft Report

## Configuration

- Draft Bot 1: `StandardDraftBot`
- Draft Bot 2: `GuardDraftBot`
- Play Bot 1: `StandardBot`
- Play Bot 2: `GuardBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 3541
- Pool: `base_pool` (64 copies)
- Pairing Mode: mirrored seats per round
- Draft Flow: hidden 3->1, then public 5 with reverse-order picks

## Drafter Summary

| Drafter | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Winner Set Avg | Loser Set Avg | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate | Battle Avg | Control Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `GuardDraftBot` | 1000 | 449 | 446 | 105 | 44.9% | 35.7% | 39.6% | 0.9% | 59.5% | 1.59 | 1.36 | 35.9% | 53.9% | 33.0% | 33.1% | 33.8% | 13.78 | 6.22 | 7.63 | 3.57 | 2.58 | 6.22 | 2.37 | 14.41 | 3.23 |
| `StandardDraftBot` | 1000 | 446 | 449 | 105 | 44.6% | 35.1% | 39.0% | 0.7% | 60.3% | 1.58 | 1.39 | 35.3% | 53.9% | 32.9% | 34.5% | 32.7% | 13.74 | 6.26 | 7.73 | 3.62 | 2.4 | 6.26 | 2.31 | 14.48 | 3.21 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| GuardDraftBot vs StandardDraftBot | 1000 | 105 | `GuardDraftBot`=449, `StandardDraftBot`=446 | 1.17 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 528 |
| 2 | 大振り | 439 |
| 3 | 渾身 | 404 |
| 4 | 返し刃 | 391 |
| 5 | 十字受け | 377 |
| 6 | 前のめり | 374 |
| 7 | 圧迫 | 373 |
| 8 | 粉砕 | 326 |
| 9 | 受け直し | 279 |
| 10 | 踏ん張り | 268 |
| 11 | 鉄壁 | 231 |
| 12 | 蓄え | 214 |
| 13 | 加速 | 137 |
| 14 | 勢い溜め | 127 |
| 15 | 疾走 | 112 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 377 |
| 2 | 前のめり | 210 |
| 3 | 返し刃 | 190 |
| 4 | 十字受け | 188 |
| 5 | 粉砕 | 151 |
| 6 | 受け直し | 147 |
| 7 | 圧迫 | 136 |
| 8 | 渾身 | 130 |
| 9 | 踏ん張り | 129 |
| 10 | 大振り | 126 |
| 11 | 鉄壁 | 97 |
| 12 | 蓄え | 76 |
| 13 | 疾走 | 66 |
| 14 | 加速 | 66 |
| 15 | 勢い溜め | 55 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 365 |
| 2 | 返し刃 | 160 |
| 3 | 十字受け | 148 |
| 4 | 粉砕 | 142 |
| 5 | 渾身 | 125 |
| 6 | 大振り | 117 |
| 7 | 踏ん張り | 89 |
| 8 | 疾走 | 55 |
| 9 | 鉄壁 | 53 |
| 10 | 強撃 | 39 |
| 11 | 押し込み | 34 |
| 12 | 崩し | 29 |
| 13 | 貫き | 24 |
| 14 | 残像 | 22 |
| 15 | 低姿勢 | 9 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `GuardDraftBot` | 3.65 | 1.14 | 0.58 | 3.45 | 1.17 | -0.25 | 77 (7.7%) | 76 (16.9%) |
| `StandardDraftBot` | 4.51 | 0.45 | 0.67 | 4.53 | 0.37 | -0.01 | 76 (7.6%) | 77 (17.3%) |

## Drafter Details

### GuardDraftBot

- Win Rate: 44.9%
- Draw Rate: 10.5%
- First Pass Win Rate: 35.7%
- Win With Fewer Cards: 39.6%
- Win With Same Cards: 0.9%
- Win With More Cards: 59.5%
- Winner Facedown Avg: 1.59
- Loser Facedown Avg: 1.36
- Starting Player Win Rate: 35.9%
- Responding Player Win Rate: 53.9%
- Final Stats Avg: A=3.65, B=1.14, S=0.58
- Losing Final Stats Avg: A=3.45, B=1.17, S=-0.25
- Lost With Speed Advantage: 77 (7.7%)
- Won After Blocking Faster Attack: 76 (16.9%)
- Action Rates: set=33.0%, set_pass=33.1%, pass=33.8%
- Turns: min=1, avg=1.17, max=3
- Battle / Control: avg=13.78 / 6.22
- Role Colors: red=7.63, blue=3.57, green=2.58, white=6.22
- Rarities: common=2.37, uncommon=14.41, rare=3.23

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 崩し | 954 |
| 2 | 十字受け | 945 |
| 3 | 踏ん張り | 910 |
| 4 | 返し刃 | 885 |
| 5 | 貫き | 884 |
| 6 | 低姿勢 | 877 |
| 7 | 受け直し | 818 |
| 8 | 受け流し | 816 |
| 9 | 押し込み | 807 |
| 10 | 粉砕 | 803 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 十字受け | 422 |
| 2 | 崩し | 420 |
| 3 | 返し刃 | 409 |
| 4 | 貫き | 400 |
| 5 | 低姿勢 | 397 |
| 6 | 踏ん張り | 395 |
| 7 | 受け直し | 387 |
| 8 | 押し込み | 368 |
| 9 | 退き足 | 363 |
| 10 | 粉砕 | 361 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 崩し | `battle_break` | `uncommon` | 954 | 15 | 12 | 12 |
| 十字受け | `battle_cross_guard` | `uncommon` | 945 | 253 | 130 | 106 |
| 踏ん張り | `battle_brace` | `uncommon` | 910 | 188 | 83 | 65 |
| 返し刃 | `battle_counter` | `uncommon` | 885 | 179 | 99 | 82 |
| 貫き | `battle_pierce` | `uncommon` | 884 | 14 | 9 | 9 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 877 | 25 | 14 | 9 |
| 受け直し | `control_cover` | `uncommon` | 818 | 139 | 72 | 0 |
| 受け流し | `battle_guard` | `uncommon` | 816 | 25 | 8 | 5 |
| 押し込み | `battle_press` | `uncommon` | 807 | 54 | 30 | 27 |
| 粉砕 | `battle_crush` | `uncommon` | 803 | 47 | 28 | 28 |
| 退き足 | `battle_backstep` | `uncommon` | 800 | 4 | 2 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 766 | 174 | 102 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 747 | 32 | 19 | 0 |
| フェイント | `battle_feint` | `uncommon` | 742 | 0 | 0 | 0 |
| 補強 | `control_fortify` | `uncommon` | 724 | 56 | 34 | 0 |
| 強撃 | `battle_power_attack` | `uncommon` | 715 | 24 | 10 | 10 |
| 圧迫 | `control_pressure` | `common` | 662 | 189 | 66 | 0 |
| 加速 | `control_haste` | `uncommon` | 619 | 71 | 36 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 595 | 64 | 29 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 510 | 282 | 199 | 196 |
| 鉄壁 | `battle_wall` | `rare` | 479 | 171 | 69 | 39 |
| 疾走 | `battle_dash` | `rare` | 477 | 31 | 22 | 22 |
| 渾身 | `battle_all_in` | `rare` | 466 | 186 | 46 | 44 |
| 大振り | `battle_heavy_swing` | `rare` | 448 | 205 | 54 | 54 |
| 残像 | `battle_afterimage` | `rare` | 440 | 31 | 11 | 6 |
| 構え | `control_guard` | `common` | 438 | 40 | 20 | 0 |
| 防御 | `battle_defend` | `common` | 408 | 0 | 0 | 0 |
| 蓄え | `control_reserve` | `rare` | 407 | 109 | 38 | 0 |
| 攻撃 | `battle_attack` | `common` | 247 | 0 | 0 | 0 |
| 牽制 | `control_disrupt` | `common` | 223 | 9 | 2 | 0 |
| 集中 | `control_focus` | `common` | 223 | 8 | 2 | 0 |
| ステップ | `battle_step` | `common` | 165 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 2366 | 246 | 10.4% | 90 | 36.6% | 0 |
| `uncommon` | 14407 | 1364 | 9.5% | 717 | 52.6% | 353 |
| `rare` | 3227 | 1015 | 31.5% | 439 | 43.3% | 361 |

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

- Win Rate: 44.6%
- Draw Rate: 10.5%
- First Pass Win Rate: 35.1%
- Win With Fewer Cards: 39.0%
- Win With Same Cards: 0.7%
- Win With More Cards: 60.3%
- Winner Facedown Avg: 1.58
- Loser Facedown Avg: 1.39
- Starting Player Win Rate: 35.3%
- Responding Player Win Rate: 53.9%
- Final Stats Avg: A=4.51, B=0.45, S=0.67
- Losing Final Stats Avg: A=4.53, B=0.37, S=-0.01
- Lost With Speed Advantage: 76 (7.6%)
- Won After Blocking Faster Attack: 77 (17.3%)
- Action Rates: set=32.9%, set_pass=34.5%, pass=32.7%
- Turns: min=1, avg=1.17, max=3
- Battle / Control: avg=13.74 / 6.26
- Role Colors: red=7.73, blue=3.62, green=2.4, white=6.26
- Rarities: common=2.31, uncommon=14.48, rare=3.21

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 粉砕 | 929 |
| 2 | 貫き | 924 |
| 3 | 返し刃 | 889 |
| 4 | 崩し | 884 |
| 5 | 踏ん張り | 855 |
| 6 | フェイント | 854 |
| 7 | 退き足 | 848 |
| 8 | 十字受け | 835 |
| 9 | 強撃 | 830 |
| 10 | 受け直し | 817 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 貫き | 427 |
| 2 | 粉砕 | 410 |
| 3 | 返し刃 | 391 |
| 4 | 受け直し | 387 |
| 5 | フェイント | 381 |
| 6 | 崩し | 379 |
| 7 | 強撃 | 376 |
| 8 | 退き足 | 376 |
| 9 | 十字受け | 372 |
| 10 | 踏ん張り | 369 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 粉砕 | `battle_crush` | `uncommon` | 929 | 279 | 123 | 114 |
| 貫き | `battle_pierce` | `uncommon` | 924 | 23 | 16 | 15 |
| 返し刃 | `battle_counter` | `uncommon` | 889 | 212 | 91 | 78 |
| 崩し | `battle_break` | `uncommon` | 884 | 26 | 17 | 17 |
| 踏ん張り | `battle_brace` | `uncommon` | 855 | 80 | 46 | 24 |
| フェイント | `battle_feint` | `uncommon` | 854 | 0 | 0 | 0 |
| 退き足 | `battle_backstep` | `uncommon` | 848 | 0 | 0 | 0 |
| 十字受け | `battle_cross_guard` | `uncommon` | 835 | 124 | 58 | 42 |
| 強撃 | `battle_power_attack` | `uncommon` | 830 | 87 | 32 | 29 |
| 受け直し | `control_cover` | `uncommon` | 817 | 140 | 75 | 0 |
| 受け流し | `battle_guard` | `uncommon` | 787 | 5 | 3 | 1 |
| 前のめり | `control_overclock` | `uncommon` | 784 | 200 | 108 | 0 |
| 押し込み | `battle_press` | `uncommon` | 765 | 23 | 10 | 7 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 752 | 0 | 0 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 751 | 36 | 19 | 0 |
| 補強 | `control_fortify` | `uncommon` | 706 | 45 | 20 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 648 | 63 | 26 | 0 |
| 圧迫 | `control_pressure` | `common` | 625 | 184 | 70 | 0 |
| 加速 | `control_haste` | `uncommon` | 625 | 66 | 30 | 0 |
| 残像 | `battle_afterimage` | `rare` | 495 | 45 | 21 | 16 |
| 大振り | `battle_heavy_swing` | `rare` | 487 | 234 | 72 | 63 |
| 渾身 | `battle_all_in` | `rare` | 473 | 218 | 84 | 81 |
| 鉄壁 | `battle_wall` | `rare` | 455 | 60 | 28 | 14 |
| 蓄え | `control_reserve` | `rare` | 437 | 105 | 38 | 0 |
| 疾走 | `battle_dash` | `rare` | 432 | 81 | 44 | 33 |
| 構え | `control_guard` | `common` | 430 | 30 | 8 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 429 | 246 | 178 | 169 |
| 防御 | `battle_defend` | `common` | 402 | 0 | 0 | 0 |
| 攻撃 | `battle_attack` | `common` | 267 | 0 | 0 | 0 |
| 集中 | `control_focus` | `common` | 218 | 10 | 4 | 0 |
| 牽制 | `control_disrupt` | `common` | 215 | 10 | 4 | 0 |
| ステップ | `battle_step` | `common` | 152 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 2309 | 234 | 10.1% | 86 | 36.8% | 0 |
| `uncommon` | 14483 | 1409 | 9.7% | 674 | 47.8% | 327 |
| `rare` | 3208 | 989 | 30.8% | 465 | 47.0% | 376 |

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
