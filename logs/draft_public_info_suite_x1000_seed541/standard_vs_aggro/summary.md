# Draft Report

## Configuration

- Draft Bot 1: `StandardDraftBot`
- Draft Bot 2: `AggroDraftBot`
- Play Bot 1: `StandardBot`
- Play Bot 2: `AggroBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 2541
- Pool: `base_pool` (64 copies)
- Pairing Mode: mirrored seats per round
- Draft Flow: hidden 3->1, then public 5 with reverse-order picks

## Drafter Summary

| Drafter | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Winner Set Avg | Loser Set Avg | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate | Battle Avg | Control Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `AggroDraftBot` | 1000 | 450 | 439 | 111 | 45.0% | 34.0% | 34.9% | 0.2% | 64.9% | 1.66 | 1.42 | 34.2% | 54.4% | 34.4% | 31.8% | 33.8% | 13.83 | 6.17 | 7.81 | 3.63 | 2.39 | 6.17 | 2.38 | 14.38 | 3.24 |
| `StandardDraftBot` | 1000 | 439 | 450 | 111 | 43.9% | 34.4% | 41.9% | 0.5% | 57.6% | 1.58 | 1.36 | 34.4% | 54.8% | 32.8% | 34.7% | 32.5% | 13.75 | 6.25 | 7.64 | 3.61 | 2.5 | 6.25 | 2.41 | 14.43 | 3.16 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| AggroDraftBot vs StandardDraftBot | 1000 | 111 | `AggroDraftBot`=450, `StandardDraftBot`=439 | 1.04 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 粉砕 | 525 |
| 2 | 踏み込み | 451 |
| 3 | 大振り | 386 |
| 4 | 返し刃 | 366 |
| 5 | 渾身 | 356 |
| 6 | 圧迫 | 306 |
| 7 | 前のめり | 293 |
| 8 | 受け直し | 262 |
| 9 | 強撃 | 228 |
| 10 | 蓄え | 208 |
| 11 | 疾走 | 182 |
| 12 | 十字受け | 155 |
| 13 | 勢い溜め | 136 |
| 14 | 加速 | 127 |
| 15 | 崩し | 123 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 325 |
| 2 | 返し刃 | 223 |
| 3 | 粉砕 | 205 |
| 4 | 前のめり | 162 |
| 5 | 受け直し | 138 |
| 6 | 疾走 | 116 |
| 7 | 強撃 | 113 |
| 8 | 圧迫 | 105 |
| 9 | 蓄え | 96 |
| 10 | 十字受け | 91 |
| 11 | 渾身 | 82 |
| 12 | 加速 | 76 |
| 13 | 崩し | 74 |
| 14 | 貫き | 64 |
| 15 | 大振り | 59 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 318 |
| 2 | 返し刃 | 213 |
| 3 | 粉砕 | 203 |
| 4 | 疾走 | 113 |
| 5 | 強撃 | 111 |
| 6 | 十字受け | 82 |
| 7 | 渾身 | 78 |
| 8 | 崩し | 73 |
| 9 | 貫き | 64 |
| 10 | 大振り | 58 |
| 11 | 残像 | 41 |
| 12 | 踏ん張り | 38 |
| 13 | 押し込み | 30 |
| 14 | 鉄壁 | 12 |
| 15 | 受け流し | 3 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `AggroDraftBot` | 4.61 | 0.24 | 0.89 | 4.82 | 0.16 | -0.12 | 33 (3.3%) | 35 (7.8%) |
| `StandardDraftBot` | 4.07 | 0.55 | 0.83 | 4.4 | 0.4 | -0.14 | 35 (3.5%) | 33 (7.5%) |

## Drafter Details

### AggroDraftBot

- Win Rate: 45.0%
- Draw Rate: 11.1%
- First Pass Win Rate: 34.0%
- Win With Fewer Cards: 34.9%
- Win With Same Cards: 0.2%
- Win With More Cards: 64.9%
- Winner Facedown Avg: 1.66
- Loser Facedown Avg: 1.42
- Starting Player Win Rate: 34.2%
- Responding Player Win Rate: 54.4%
- Final Stats Avg: A=4.61, B=0.24, S=0.89
- Losing Final Stats Avg: A=4.82, B=0.16, S=-0.12
- Lost With Speed Advantage: 33 (3.3%)
- Won After Blocking Faster Attack: 35 (7.8%)
- Action Rates: set=34.4%, set_pass=31.8%, pass=33.8%
- Turns: min=1, avg=1.04, max=3
- Battle / Control: avg=13.83 / 6.17
- Role Colors: red=7.81, blue=3.63, green=2.39, white=6.17
- Rarities: common=2.38, uncommon=14.38, rare=3.24

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 貫き | 919 |
| 2 | 粉砕 | 916 |
| 3 | 崩し | 895 |
| 4 | 返し刃 | 888 |
| 5 | フェイント | 882 |
| 6 | 踏ん張り | 857 |
| 7 | 十字受け | 843 |
| 8 | 受け流し | 842 |
| 9 | 強撃 | 831 |
| 10 | 退き足 | 791 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 貫き | 422 |
| 2 | 粉砕 | 410 |
| 3 | 崩し | 409 |
| 4 | 返し刃 | 405 |
| 5 | フェイント | 391 |
| 6 | 踏ん張り | 382 |
| 7 | 強撃 | 378 |
| 8 | 受け流し | 375 |
| 9 | 押し込み | 365 |
| 10 | 退き足 | 364 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 貫き | `battle_pierce` | `uncommon` | 919 | 69 | 46 | 46 |
| 粉砕 | `battle_crush` | `uncommon` | 916 | 297 | 115 | 113 |
| 崩し | `battle_break` | `uncommon` | 895 | 94 | 56 | 55 |
| 返し刃 | `battle_counter` | `uncommon` | 888 | 148 | 96 | 94 |
| フェイント | `battle_feint` | `uncommon` | 882 | 1 | 1 | 1 |
| 踏ん張り | `battle_brace` | `uncommon` | 857 | 20 | 9 | 9 |
| 十字受け | `battle_cross_guard` | `uncommon` | 843 | 21 | 15 | 15 |
| 受け流し | `battle_guard` | `uncommon` | 842 | 1 | 0 | 0 |
| 強撃 | `battle_power_attack` | `uncommon` | 831 | 151 | 75 | 74 |
| 退き足 | `battle_backstep` | `uncommon` | 791 | 1 | 0 | 0 |
| 押し込み | `battle_press` | `uncommon` | 786 | 28 | 15 | 15 |
| 受け直し | `control_cover` | `uncommon` | 773 | 130 | 77 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 749 | 135 | 67 | 0 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 743 | 0 | 0 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 708 | 41 | 27 | 0 |
| 補強 | `control_fortify` | `uncommon` | 664 | 48 | 17 | 0 |
| 加速 | `control_haste` | `uncommon` | 659 | 77 | 45 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 635 | 67 | 31 | 0 |
| 圧迫 | `control_pressure` | `common` | 612 | 151 | 56 | 0 |
| 大振り | `battle_heavy_swing` | `rare` | 483 | 202 | 39 | 38 |
| 残像 | `battle_afterimage` | `rare` | 479 | 41 | 25 | 25 |
| 踏み込み | `battle_step_in` | `rare` | 464 | 221 | 164 | 157 |
| 蓄え | `control_reserve` | `rare` | 460 | 101 | 41 | 0 |
| 鉄壁 | `battle_wall` | `rare` | 453 | 0 | 0 | 0 |
| 渾身 | `battle_all_in` | `rare` | 452 | 190 | 46 | 42 |
| 疾走 | `battle_dash` | `rare` | 446 | 105 | 63 | 61 |
| 構え | `control_guard` | `common` | 392 | 16 | 6 | 0 |
| 防御 | `battle_defend` | `common` | 353 | 0 | 0 | 0 |
| 攻撃 | `battle_attack` | `common` | 323 | 0 | 0 | 0 |
| 集中 | `control_focus` | `common` | 263 | 15 | 8 | 0 |
| 牽制 | `control_disrupt` | `common` | 254 | 12 | 6 | 0 |
| ステップ | `battle_step` | `common` | 185 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 2382 | 194 | 8.1% | 76 | 39.2% | 0 |
| `uncommon` | 14381 | 1329 | 9.2% | 692 | 52.1% | 422 |
| `rare` | 3237 | 860 | 26.6% | 378 | 44.0% | 323 |

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

- Win Rate: 43.9%
- Draw Rate: 11.1%
- First Pass Win Rate: 34.4%
- Win With Fewer Cards: 41.9%
- Win With Same Cards: 0.5%
- Win With More Cards: 57.6%
- Winner Facedown Avg: 1.58
- Loser Facedown Avg: 1.36
- Starting Player Win Rate: 34.4%
- Responding Player Win Rate: 54.8%
- Final Stats Avg: A=4.07, B=0.55, S=0.83
- Losing Final Stats Avg: A=4.4, B=0.4, S=-0.14
- Lost With Speed Advantage: 35 (3.5%)
- Won After Blocking Faster Attack: 33 (7.5%)
- Action Rates: set=32.8%, set_pass=34.7%, pass=32.5%
- Turns: min=1, avg=1.04, max=3
- Battle / Control: avg=13.75 / 6.25
- Role Colors: red=7.64, blue=3.61, green=2.5, white=6.25
- Rarities: common=2.41, uncommon=14.43, rare=3.16

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 崩し | 945 |
| 2 | 十字受け | 929 |
| 3 | 貫き | 927 |
| 4 | 踏ん張り | 876 |
| 5 | 返し刃 | 870 |
| 6 | 退き足 | 853 |
| 7 | 粉砕 | 849 |
| 8 | 低姿勢 | 835 |
| 9 | 受け直し | 833 |
| 10 | 前のめり | 795 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 崩し | 428 |
| 2 | 貫き | 408 |
| 3 | 返し刃 | 392 |
| 4 | 十字受け | 390 |
| 5 | 受け直し | 383 |
| 6 | 踏ん張り | 381 |
| 7 | 粉砕 | 380 |
| 8 | 前のめり | 376 |
| 9 | 低姿勢 | 363 |
| 10 | 退き足 | 361 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 崩し | `battle_break` | `uncommon` | 945 | 29 | 18 | 18 |
| 十字受け | `battle_cross_guard` | `uncommon` | 929 | 134 | 76 | 67 |
| 貫き | `battle_pierce` | `uncommon` | 927 | 23 | 18 | 18 |
| 踏ん張り | `battle_brace` | `uncommon` | 876 | 65 | 31 | 29 |
| 返し刃 | `battle_counter` | `uncommon` | 870 | 218 | 127 | 119 |
| 退き足 | `battle_backstep` | `uncommon` | 853 | 1 | 1 | 1 |
| 粉砕 | `battle_crush` | `uncommon` | 849 | 228 | 90 | 90 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 835 | 1 | 0 | 0 |
| 受け直し | `control_cover` | `uncommon` | 833 | 132 | 61 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 795 | 158 | 95 | 0 |
| 受け流し | `battle_guard` | `uncommon` | 780 | 3 | 3 | 3 |
| 重心落とし | `control_anchor` | `uncommon` | 766 | 35 | 18 | 0 |
| 押し込み | `battle_press` | `uncommon` | 751 | 27 | 16 | 15 |
| 強撃 | `battle_power_attack` | `uncommon` | 749 | 77 | 38 | 37 |
| フェイント | `battle_feint` | `uncommon` | 741 | 0 | 0 | 0 |
| 補強 | `control_fortify` | `uncommon` | 712 | 57 | 23 | 0 |
| 圧迫 | `control_pressure` | `common` | 653 | 155 | 49 | 0 |
| 加速 | `control_haste` | `uncommon` | 621 | 50 | 31 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 593 | 69 | 20 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 477 | 230 | 161 | 161 |
| 渾身 | `battle_all_in` | `rare` | 477 | 166 | 36 | 36 |
| 構え | `control_guard` | `common` | 477 | 21 | 10 | 0 |
| 鉄壁 | `battle_wall` | `rare` | 475 | 48 | 26 | 12 |
| 残像 | `battle_afterimage` | `rare` | 464 | 39 | 18 | 16 |
| 疾走 | `battle_dash` | `rare` | 451 | 77 | 53 | 52 |
| 大振り | `battle_heavy_swing` | `rare` | 442 | 184 | 20 | 20 |
| 防御 | `battle_defend` | `common` | 411 | 0 | 0 | 0 |
| 蓄え | `control_reserve` | `rare` | 376 | 107 | 55 | 0 |
| 攻撃 | `battle_attack` | `common` | 278 | 0 | 0 | 0 |
| 集中 | `control_focus` | `common` | 213 | 7 | 2 | 0 |
| 牽制 | `control_disrupt` | `common` | 212 | 9 | 4 | 0 |
| ステップ | `battle_step` | `common` | 169 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 2413 | 192 | 8.0% | 65 | 33.9% | 0 |
| `uncommon` | 14425 | 1307 | 9.1% | 666 | 51.0% | 397 |
| `rare` | 3162 | 851 | 26.9% | 369 | 43.4% | 297 |

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
