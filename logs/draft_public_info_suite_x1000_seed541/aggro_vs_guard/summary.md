# Draft Report

## Configuration

- Draft Bot 1: `AggroDraftBot`
- Draft Bot 2: `GuardDraftBot`
- Play Bot 1: `AggroBot`
- Play Bot 2: `GuardBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 5541
- Pool: `base_pool` (64 copies)
- Pairing Mode: mirrored seats per round
- Draft Flow: hidden 3->1, then public 5 with reverse-order picks

## Drafter Summary

| Drafter | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Winner Set Avg | Loser Set Avg | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate | Battle Avg | Control Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `AggroDraftBot` | 1000 | 451 | 438 | 111 | 45.1% | 32.8% | 32.4% | 1.1% | 66.5% | 1.66 | 1.44 | 32.8% | 55.3% | 34.1% | 32.1% | 33.8% | 13.79 | 6.21 | 7.77 | 3.66 | 2.37 | 6.21 | 2.38 | 14.33 | 3.29 |
| `GuardDraftBot` | 1000 | 438 | 451 | 111 | 43.8% | 35.0% | 43.6% | 0.5% | 55.9% | 1.56 | 1.32 | 35.0% | 54.4% | 32.3% | 35.3% | 32.4% | 13.79 | 6.21 | 7.62 | 3.56 | 2.61 | 6.21 | 2.4 | 14.48 | 3.12 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| AggroDraftBot vs GuardDraftBot | 1000 | 111 | `AggroDraftBot`=451, `GuardDraftBot`=438 | 1.1 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 484 |
| 2 | 大振り | 402 |
| 3 | 粉砕 | 394 |
| 4 | 渾身 | 375 |
| 5 | 前のめり | 359 |
| 6 | 返し刃 | 353 |
| 7 | 圧迫 | 324 |
| 8 | 受け直し | 264 |
| 9 | 十字受け | 249 |
| 10 | 蓄え | 216 |
| 11 | 踏ん張り | 199 |
| 12 | 強撃 | 181 |
| 13 | 鉄壁 | 163 |
| 14 | 勢い溜め | 144 |
| 15 | 疾走 | 132 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 345 |
| 2 | 前のめり | 201 |
| 3 | 返し刃 | 188 |
| 4 | 粉砕 | 173 |
| 5 | 受け直し | 140 |
| 6 | 十字受け | 133 |
| 7 | 圧迫 | 126 |
| 8 | 渾身 | 110 |
| 9 | 大振り | 95 |
| 10 | 踏ん張り | 95 |
| 11 | 疾走 | 87 |
| 12 | 強撃 | 84 |
| 13 | 蓄え | 74 |
| 14 | 鉄壁 | 67 |
| 15 | 加速 | 67 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 336 |
| 2 | 返し刃 | 177 |
| 3 | 粉砕 | 165 |
| 4 | 渾身 | 108 |
| 5 | 十字受け | 105 |
| 6 | 踏ん張り | 87 |
| 7 | 疾走 | 85 |
| 8 | 大振り | 83 |
| 9 | 強撃 | 79 |
| 10 | 崩し | 49 |
| 11 | 貫き | 48 |
| 12 | 鉄壁 | 40 |
| 13 | 押し込み | 34 |
| 14 | 残像 | 18 |
| 15 | 受け流し | 10 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `AggroDraftBot` | 4.76 | 0.22 | 0.79 | 4.85 | 0.18 | -0.05 | 78 (7.8%) | 58 (12.9%) |
| `GuardDraftBot` | 3.5 | 1.14 | 0.55 | 3.47 | 1.11 | -0.3 | 58 (5.8%) | 78 (17.8%) |

## Drafter Details

### AggroDraftBot

- Win Rate: 45.1%
- Draw Rate: 11.1%
- First Pass Win Rate: 32.8%
- Win With Fewer Cards: 32.4%
- Win With Same Cards: 1.1%
- Win With More Cards: 66.5%
- Winner Facedown Avg: 1.66
- Loser Facedown Avg: 1.44
- Starting Player Win Rate: 32.8%
- Responding Player Win Rate: 55.3%
- Final Stats Avg: A=4.76, B=0.22, S=0.79
- Losing Final Stats Avg: A=4.85, B=0.18, S=-0.05
- Lost With Speed Advantage: 78 (7.8%)
- Won After Blocking Faster Attack: 58 (12.9%)
- Action Rates: set=34.1%, set_pass=32.1%, pass=33.8%
- Turns: min=1, avg=1.1, max=3
- Battle / Control: avg=13.79 / 6.21
- Role Colors: red=7.77, blue=3.66, green=2.37, white=6.21
- Rarities: common=2.38, uncommon=14.33, rare=3.29

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 粉砕 | 1034 |
| 2 | 貫き | 933 |
| 3 | フェイント | 899 |
| 4 | 崩し | 888 |
| 5 | 返し刃 | 867 |
| 6 | 強撃 | 840 |
| 7 | 退き足 | 810 |
| 8 | 踏ん張り | 797 |
| 9 | 受け流し | 790 |
| 10 | 十字受け | 790 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 粉砕 | 458 |
| 2 | 崩し | 430 |
| 3 | 貫き | 409 |
| 4 | フェイント | 408 |
| 5 | 返し刃 | 390 |
| 6 | 強撃 | 386 |
| 7 | 前のめり | 365 |
| 8 | 十字受け | 360 |
| 9 | 受け流し | 359 |
| 10 | 退き足 | 357 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 粉砕 | `battle_crush` | `uncommon` | 1034 | 346 | 158 | 150 |
| 貫き | `battle_pierce` | `uncommon` | 933 | 69 | 44 | 44 |
| フェイント | `battle_feint` | `uncommon` | 899 | 3 | 0 | 0 |
| 崩し | `battle_break` | `uncommon` | 888 | 65 | 44 | 43 |
| 返し刃 | `battle_counter` | `uncommon` | 867 | 177 | 94 | 85 |
| 強撃 | `battle_power_attack` | `uncommon` | 840 | 156 | 70 | 65 |
| 退き足 | `battle_backstep` | `uncommon` | 810 | 1 | 0 | 0 |
| 踏ん張り | `battle_brace` | `uncommon` | 797 | 17 | 10 | 9 |
| 十字受け | `battle_cross_guard` | `uncommon` | 790 | 20 | 14 | 10 |
| 受け流し | `battle_guard` | `uncommon` | 790 | 3 | 1 | 1 |
| 前のめり | `control_overclock` | `uncommon` | 788 | 192 | 106 | 0 |
| 受け直し | `control_cover` | `uncommon` | 767 | 120 | 64 | 0 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 714 | 0 | 0 | 0 |
| 押し込み | `battle_press` | `uncommon` | 710 | 29 | 11 | 10 |
| 重心落とし | `control_anchor` | `uncommon` | 694 | 40 | 21 | 0 |
| 補強 | `control_fortify` | `uncommon` | 673 | 47 | 19 | 0 |
| 加速 | `control_haste` | `uncommon` | 669 | 53 | 30 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 666 | 74 | 28 | 0 |
| 圧迫 | `control_pressure` | `common` | 598 | 145 | 65 | 0 |
| 残像 | `battle_afterimage` | `rare` | 495 | 34 | 15 | 14 |
| 鉄壁 | `battle_wall` | `rare` | 492 | 1 | 0 | 0 |
| 大振り | `battle_heavy_swing` | `rare` | 481 | 209 | 49 | 37 |
| 疾走 | `battle_dash` | `rare` | 474 | 94 | 65 | 63 |
| 渾身 | `battle_all_in` | `rare` | 469 | 202 | 67 | 65 |
| 踏み込み | `battle_step_in` | `rare` | 462 | 236 | 161 | 152 |
| 構え | `control_guard` | `common` | 423 | 27 | 11 | 0 |
| 蓄え | `control_reserve` | `rare` | 421 | 116 | 40 | 0 |
| 防御 | `battle_defend` | `common` | 370 | 0 | 0 | 0 |
| 攻撃 | `battle_attack` | `common` | 291 | 2 | 0 | 0 |
| 集中 | `control_focus` | `common` | 261 | 12 | 4 | 0 |
| 牽制 | `control_disrupt` | `common` | 246 | 9 | 2 | 0 |
| ステップ | `battle_step` | `common` | 188 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 2377 | 195 | 8.2% | 82 | 42.1% | 0 |
| `uncommon` | 14329 | 1412 | 9.9% | 714 | 50.6% | 417 |
| `rare` | 3294 | 892 | 27.1% | 397 | 44.5% | 331 |

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

- Win Rate: 43.8%
- Draw Rate: 11.1%
- First Pass Win Rate: 35.0%
- Win With Fewer Cards: 43.6%
- Win With Same Cards: 0.5%
- Win With More Cards: 55.9%
- Winner Facedown Avg: 1.56
- Loser Facedown Avg: 1.32
- Starting Player Win Rate: 35.0%
- Responding Player Win Rate: 54.4%
- Final Stats Avg: A=3.5, B=1.14, S=0.55
- Losing Final Stats Avg: A=3.47, B=1.11, S=-0.3
- Lost With Speed Advantage: 58 (5.8%)
- Won After Blocking Faster Attack: 78 (17.8%)
- Action Rates: set=32.3%, set_pass=35.3%, pass=32.4%
- Turns: min=1, avg=1.1, max=3
- Battle / Control: avg=13.79 / 6.21
- Role Colors: red=7.62, blue=3.56, green=2.61, white=6.21
- Rarities: common=2.4, uncommon=14.48, rare=3.12

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 十字受け | 987 |
| 2 | 踏ん張り | 969 |
| 3 | 崩し | 940 |
| 4 | 返し刃 | 915 |
| 5 | 低姿勢 | 908 |
| 6 | 貫き | 892 |
| 7 | 退き足 | 848 |
| 8 | 受け直し | 844 |
| 9 | 受け流し | 826 |
| 10 | 押し込み | 808 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 十字受け | 440 |
| 2 | 崩し | 430 |
| 3 | 踏ん張り | 430 |
| 4 | 返し刃 | 412 |
| 5 | 貫き | 388 |
| 6 | 受け直し | 386 |
| 7 | 低姿勢 | 383 |
| 8 | 受け流し | 367 |
| 9 | 退き足 | 360 |
| 10 | 押し込み | 346 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 十字受け | `battle_cross_guard` | `uncommon` | 987 | 229 | 119 | 95 |
| 踏ん張り | `battle_brace` | `uncommon` | 969 | 182 | 85 | 78 |
| 崩し | `battle_break` | `uncommon` | 940 | 8 | 6 | 6 |
| 返し刃 | `battle_counter` | `uncommon` | 915 | 176 | 94 | 92 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 908 | 24 | 8 | 6 |
| 貫き | `battle_pierce` | `uncommon` | 892 | 10 | 4 | 4 |
| 退き足 | `battle_backstep` | `uncommon` | 848 | 4 | 2 | 1 |
| 受け直し | `control_cover` | `uncommon` | 844 | 144 | 76 | 0 |
| 受け流し | `battle_guard` | `uncommon` | 826 | 20 | 9 | 9 |
| 押し込み | `battle_press` | `uncommon` | 808 | 56 | 25 | 24 |
| 粉砕 | `battle_crush` | `uncommon` | 743 | 48 | 15 | 15 |
| 重心落とし | `control_anchor` | `uncommon` | 743 | 41 | 21 | 0 |
| 補強 | `control_fortify` | `uncommon` | 727 | 37 | 21 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 724 | 167 | 95 | 0 |
| 強撃 | `battle_power_attack` | `uncommon` | 718 | 25 | 14 | 14 |
| フェイント | `battle_feint` | `uncommon` | 708 | 0 | 0 | 0 |
| 圧迫 | `control_pressure` | `common` | 673 | 179 | 61 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 591 | 70 | 24 | 0 |
| 加速 | `control_haste` | `uncommon` | 591 | 59 | 37 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 481 | 248 | 184 | 184 |
| 渾身 | `battle_all_in` | `rare` | 461 | 173 | 43 | 43 |
| 構え | `control_guard` | `common` | 460 | 22 | 11 | 0 |
| 大振り | `battle_heavy_swing` | `rare` | 452 | 193 | 46 | 46 |
| 鉄壁 | `battle_wall` | `rare` | 446 | 162 | 67 | 40 |
| 疾走 | `battle_dash` | `rare` | 432 | 38 | 22 | 22 |
| 防御 | `battle_defend` | `common` | 429 | 0 | 0 | 0 |
| 残像 | `battle_afterimage` | `rare` | 423 | 18 | 4 | 4 |
| 蓄え | `control_reserve` | `rare` | 420 | 100 | 34 | 0 |
| 攻撃 | `battle_attack` | `common` | 243 | 0 | 0 | 0 |
| 牽制 | `control_disrupt` | `common` | 230 | 5 | 1 | 0 |
| 集中 | `control_focus` | `common` | 209 | 9 | 3 | 0 |
| ステップ | `battle_step` | `common` | 159 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 2403 | 215 | 8.9% | 76 | 35.3% | 0 |
| `uncommon` | 14482 | 1300 | 9.0% | 655 | 50.4% | 344 |
| `rare` | 3115 | 932 | 29.9% | 400 | 42.9% | 339 |

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
