# Draft Report

## Configuration

- Draft Bot 1: `GuardDraftBot`
- Draft Bot 2: `GuardDraftBot`
- Play Bot 1: `GuardBot`
- Play Bot 2: `GuardBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 6541
- Pool: `base_pool` (64 copies)
- Pairing Mode: mirrored seats per round
- Draft Flow: hidden 3->1, then public 5 with reverse-order picks

## Drafter Summary

| Drafter | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Winner Set Avg | Loser Set Avg | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate | Battle Avg | Control Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `GuardDraftBot` | 2000 | 917 | 917 | 166 | 45.9% | 29.3% | 31.3% | 1.9% | 66.8% | 1.63 | 1.27 | 29.3% | 62.4% | 32.3% | 34.5% | 33.3% | 13.79 | 6.21 | 7.66 | 3.63 | 2.5 | 6.21 | 2.36 | 14.45 | 3.19 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| GuardDraftBot vs GuardDraftBot | 1000 | 83 | `GuardDraftBot`=917 | 1.25 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 549 |
| 2 | 十字受け | 477 |
| 3 | 大振り | 464 |
| 4 | 返し刃 | 419 |
| 5 | 渾身 | 412 |
| 6 | 踏ん張り | 405 |
| 7 | 圧迫 | 377 |
| 8 | 鉄壁 | 351 |
| 9 | 前のめり | 337 |
| 10 | 受け直し | 287 |
| 11 | 蓄え | 253 |
| 12 | 粉砕 | 132 |
| 13 | 勢い溜め | 128 |
| 14 | 加速 | 127 |
| 15 | 補強 | 114 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 409 |
| 2 | 十字受け | 233 |
| 3 | 返し刃 | 232 |
| 4 | 大振り | 196 |
| 5 | 踏ん張り | 188 |
| 6 | 前のめり | 185 |
| 7 | 鉄壁 | 152 |
| 8 | 圧迫 | 152 |
| 9 | 渾身 | 149 |
| 10 | 受け直し | 149 |
| 11 | 蓄え | 103 |
| 12 | 加速 | 81 |
| 13 | 補強 | 58 |
| 14 | 粉砕 | 56 |
| 15 | 勢い溜め | 53 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 375 |
| 2 | 返し刃 | 193 |
| 3 | 大振り | 187 |
| 4 | 十字受け | 165 |
| 5 | 踏ん張り | 140 |
| 6 | 渾身 | 128 |
| 7 | 鉄壁 | 84 |
| 8 | 粉砕 | 50 |
| 9 | 疾走 | 36 |
| 10 | 押し込み | 35 |
| 11 | 強撃 | 28 |
| 12 | 貫き | 22 |
| 13 | 低姿勢 | 15 |
| 14 | 残像 | 14 |
| 15 | 崩し | 14 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `GuardDraftBot` | 3.76 | 0.98 | 0.44 | 3.35 | 1.01 | -0.17 | 203 (10.2%) | 203 (22.1%) |

## Drafter Details

### GuardDraftBot

- Win Rate: 45.9%
- Draw Rate: 8.3%
- First Pass Win Rate: 29.3%
- Win With Fewer Cards: 31.3%
- Win With Same Cards: 1.9%
- Win With More Cards: 66.8%
- Winner Facedown Avg: 1.63
- Loser Facedown Avg: 1.27
- Starting Player Win Rate: 29.3%
- Responding Player Win Rate: 62.4%
- Final Stats Avg: A=3.76, B=0.98, S=0.44
- Losing Final Stats Avg: A=3.35, B=1.01, S=-0.17
- Lost With Speed Advantage: 203 (10.2%)
- Won After Blocking Faster Attack: 203 (22.1%)
- Action Rates: set=32.3%, set_pass=34.5%, pass=33.3%
- Turns: min=1, avg=1.25, max=3
- Battle / Control: avg=13.79 / 6.21
- Role Colors: red=7.66, blue=3.63, green=2.5, white=6.21
- Rarities: common=2.36, uncommon=14.45, rare=3.19

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 崩し | 1836 |
| 2 | 貫き | 1832 |
| 3 | 返し刃 | 1796 |
| 4 | 十字受け | 1795 |
| 5 | 踏ん張り | 1789 |
| 6 | 粉砕 | 1725 |
| 7 | 退き足 | 1697 |
| 8 | 低姿勢 | 1654 |
| 9 | 受け流し | 1632 |
| 10 | 受け直し | 1608 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 856 |
| 2 | 貫き | 839 |
| 3 | 踏ん張り | 834 |
| 4 | 十字受け | 822 |
| 5 | 崩し | 803 |
| 6 | 粉砕 | 798 |
| 7 | 受け流し | 761 |
| 8 | 受け直し | 747 |
| 9 | 退き足 | 744 |
| 10 | 押し込み | 740 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 崩し | `battle_break` | `uncommon` | 1836 | 24 | 14 | 14 |
| 貫き | `battle_pierce` | `uncommon` | 1832 | 29 | 23 | 22 |
| 返し刃 | `battle_counter` | `uncommon` | 1796 | 419 | 232 | 193 |
| 十字受け | `battle_cross_guard` | `uncommon` | 1795 | 477 | 233 | 165 |
| 踏ん張り | `battle_brace` | `uncommon` | 1789 | 405 | 188 | 140 |
| 粉砕 | `battle_crush` | `uncommon` | 1725 | 132 | 56 | 50 |
| 退き足 | `battle_backstep` | `uncommon` | 1697 | 11 | 3 | 2 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 1654 | 50 | 22 | 15 |
| 受け流し | `battle_guard` | `uncommon` | 1632 | 32 | 11 | 7 |
| 受け直し | `control_cover` | `uncommon` | 1608 | 287 | 149 | 0 |
| 押し込み | `battle_press` | `uncommon` | 1582 | 95 | 42 | 35 |
| 前のめり | `control_overclock` | `uncommon` | 1572 | 337 | 185 | 0 |
| フェイント | `battle_feint` | `uncommon` | 1558 | 0 | 0 | 0 |
| 強撃 | `battle_power_attack` | `uncommon` | 1515 | 70 | 30 | 28 |
| 重心落とし | `control_anchor` | `uncommon` | 1485 | 99 | 44 | 0 |
| 補強 | `control_fortify` | `uncommon` | 1409 | 114 | 58 | 0 |
| 圧迫 | `control_pressure` | `common` | 1345 | 377 | 152 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 1212 | 128 | 53 | 0 |
| 加速 | `control_haste` | `uncommon` | 1211 | 127 | 81 | 0 |
| 渾身 | `battle_all_in` | `rare` | 935 | 412 | 149 | 128 |
| 踏み込み | `battle_step_in` | `rare` | 933 | 549 | 409 | 375 |
| 鉄壁 | `battle_wall` | `rare` | 927 | 351 | 152 | 84 |
| 構え | `control_guard` | `common` | 926 | 63 | 31 | 0 |
| 疾走 | `battle_dash` | `rare` | 917 | 90 | 43 | 36 |
| 大振り | `battle_heavy_swing` | `rare` | 910 | 464 | 196 | 187 |
| 残像 | `battle_afterimage` | `rare` | 909 | 50 | 18 | 14 |
| 蓄え | `control_reserve` | `rare` | 839 | 253 | 103 | 0 |
| 防御 | `battle_defend` | `common` | 797 | 0 | 0 | 0 |
| 攻撃 | `battle_attack` | `common` | 475 | 0 | 0 | 0 |
| 集中 | `control_focus` | `common` | 404 | 24 | 10 | 0 |
| 牽制 | `control_disrupt` | `common` | 400 | 25 | 11 | 0 |
| ステップ | `battle_step` | `common` | 375 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 4722 | 489 | 10.4% | 204 | 41.7% | 0 |
| `uncommon` | 28908 | 2836 | 9.8% | 1424 | 50.2% | 671 |
| `rare` | 6370 | 2169 | 34.1% | 1070 | 49.3% | 824 |

#### Match Logs

- [draft_match_0001](matches/match_0001_GuardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0001](matches/match_0001_GuardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0002](matches/match_0002_GuardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0002](matches/match_0002_GuardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0003](matches/match_0003_GuardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0003](matches/match_0003_GuardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0004](matches/match_0004_GuardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0004](matches/match_0004_GuardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0005](matches/match_0005_GuardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0005](matches/match_0005_GuardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0006](matches/match_0006_GuardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0006](matches/match_0006_GuardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0007](matches/match_0007_GuardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0007](matches/match_0007_GuardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0008](matches/match_0008_GuardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0008](matches/match_0008_GuardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0009](matches/match_0009_GuardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0009](matches/match_0009_GuardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0010](matches/match_0010_GuardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0010](matches/match_0010_GuardDraftBot_vs_GuardDraftBot.md)
