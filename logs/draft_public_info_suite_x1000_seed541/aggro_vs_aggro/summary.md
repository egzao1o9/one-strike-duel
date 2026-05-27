# Draft Report

## Configuration

- Draft Bot 1: `AggroDraftBot`
- Draft Bot 2: `AggroDraftBot`
- Play Bot 1: `AggroBot`
- Play Bot 2: `AggroBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 4541
- Pool: `base_pool` (64 copies)
- Pairing Mode: mirrored seats per round
- Draft Flow: hidden 3->1, then public 5 with reverse-order picks

## Drafter Summary

| Drafter | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Winner Set Avg | Loser Set Avg | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate | Battle Avg | Control Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `AggroDraftBot` | 2000 | 874 | 874 | 252 | 43.7% | 37.3% | 42.4% | 0.6% | 57.0% | 1.59 | 1.44 | 37.3% | 50.1% | 33.7% | 33.3% | 32.9% | 13.81 | 6.19 | 7.76 | 3.65 | 2.4 | 6.19 | 2.39 | 14.39 | 3.21 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| AggroDraftBot vs AggroDraftBot | 1000 | 126 | `AggroDraftBot`=874 | 1.0 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 粉砕 | 572 |
| 2 | 踏み込み | 420 |
| 3 | 大振り | 369 |
| 4 | 渾身 | 364 |
| 5 | 圧迫 | 307 |
| 6 | 強撃 | 297 |
| 7 | 前のめり | 291 |
| 8 | 返し刃 | 275 |
| 9 | 受け直し | 255 |
| 10 | 蓄え | 213 |
| 11 | 疾走 | 201 |
| 12 | 崩し | 160 |
| 13 | 貫き | 154 |
| 14 | 勢い溜め | 124 |
| 15 | 加速 | 114 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 299 |
| 2 | 粉砕 | 221 |
| 3 | 前のめり | 165 |
| 4 | 返し刃 | 162 |
| 5 | 疾走 | 148 |
| 6 | 強撃 | 139 |
| 7 | 受け直し | 138 |
| 8 | 圧迫 | 103 |
| 9 | 崩し | 93 |
| 10 | 渾身 | 87 |
| 11 | 貫き | 85 |
| 12 | 蓄え | 82 |
| 13 | 加速 | 75 |
| 14 | 重心落とし | 47 |
| 15 | 勢い溜め | 45 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 299 |
| 2 | 粉砕 | 221 |
| 3 | 返し刃 | 161 |
| 4 | 疾走 | 148 |
| 5 | 強撃 | 139 |
| 6 | 崩し | 93 |
| 7 | 渾身 | 87 |
| 8 | 貫き | 85 |
| 9 | 残像 | 39 |
| 10 | 大振り | 38 |
| 11 | 押し込み | 28 |
| 12 | 十字受け | 25 |
| 13 | 踏ん張り | 20 |
| 14 | 受け流し | 1 |
| 15 | 攻撃 | 1 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `AggroDraftBot` | 4.54 | 0.24 | 0.84 | 4.97 | 0.2 | -0.31 | 38 (1.9%) | 38 (4.3%) |

## Drafter Details

### AggroDraftBot

- Win Rate: 43.7%
- Draw Rate: 12.6%
- First Pass Win Rate: 37.3%
- Win With Fewer Cards: 42.4%
- Win With Same Cards: 0.6%
- Win With More Cards: 57.0%
- Winner Facedown Avg: 1.59
- Loser Facedown Avg: 1.44
- Starting Player Win Rate: 37.3%
- Responding Player Win Rate: 50.1%
- Final Stats Avg: A=4.54, B=0.24, S=0.84
- Losing Final Stats Avg: A=4.97, B=0.2, S=-0.31
- Lost With Speed Advantage: 38 (1.9%)
- Won After Blocking Faster Attack: 38 (4.3%)
- Action Rates: set=33.7%, set_pass=33.3%, pass=32.9%
- Turns: min=1, avg=1.0, max=2
- Battle / Control: avg=13.81 / 6.19
- Role Colors: red=7.76, blue=3.65, green=2.4, white=6.19
- Rarities: common=2.39, uncommon=14.39, rare=3.21

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 貫き | 1852 |
| 2 | 崩し | 1820 |
| 3 | 粉砕 | 1767 |
| 4 | 返し刃 | 1753 |
| 5 | 十字受け | 1750 |
| 6 | 踏ん張り | 1722 |
| 7 | フェイント | 1670 |
| 8 | 退き足 | 1663 |
| 9 | 受け流し | 1620 |
| 10 | 強撃 | 1595 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 貫き | 831 |
| 2 | 崩し | 799 |
| 3 | 踏ん張り | 778 |
| 4 | 十字受け | 777 |
| 5 | 退き足 | 741 |
| 6 | 返し刃 | 737 |
| 7 | 受け直し | 729 |
| 8 | フェイント | 709 |
| 9 | 強撃 | 706 |
| 10 | 粉砕 | 703 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 貫き | `battle_pierce` | `uncommon` | 1852 | 154 | 85 | 85 |
| 崩し | `battle_break` | `uncommon` | 1820 | 160 | 93 | 93 |
| 粉砕 | `battle_crush` | `uncommon` | 1767 | 572 | 221 | 221 |
| 返し刃 | `battle_counter` | `uncommon` | 1753 | 275 | 162 | 161 |
| 十字受け | `battle_cross_guard` | `uncommon` | 1750 | 42 | 25 | 25 |
| 踏ん張り | `battle_brace` | `uncommon` | 1722 | 43 | 20 | 20 |
| フェイント | `battle_feint` | `uncommon` | 1670 | 0 | 0 | 0 |
| 退き足 | `battle_backstep` | `uncommon` | 1663 | 2 | 1 | 1 |
| 受け流し | `battle_guard` | `uncommon` | 1620 | 3 | 1 | 1 |
| 強撃 | `battle_power_attack` | `uncommon` | 1595 | 297 | 139 | 139 |
| 受け直し | `control_cover` | `uncommon` | 1591 | 255 | 138 | 0 |
| 押し込み | `battle_press` | `uncommon` | 1563 | 61 | 29 | 28 |
| 前のめり | `control_overclock` | `uncommon` | 1540 | 291 | 165 | 0 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 1534 | 1 | 0 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 1417 | 70 | 47 | 0 |
| 補強 | `control_fortify` | `uncommon` | 1392 | 77 | 26 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 1275 | 124 | 45 | 0 |
| 加速 | `control_haste` | `uncommon` | 1263 | 114 | 75 | 0 |
| 圧迫 | `control_pressure` | `common` | 1204 | 307 | 103 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 938 | 420 | 299 | 299 |
| 大振り | `battle_heavy_swing` | `rare` | 934 | 369 | 38 | 38 |
| 渾身 | `battle_all_in` | `rare` | 930 | 364 | 87 | 87 |
| 残像 | `battle_afterimage` | `rare` | 930 | 64 | 39 | 39 |
| 鉄壁 | `battle_wall` | `rare` | 925 | 0 | 0 | 0 |
| 疾走 | `battle_dash` | `rare` | 917 | 201 | 148 | 148 |
| 蓄え | `control_reserve` | `rare` | 854 | 213 | 82 | 0 |
| 構え | `control_guard` | `common` | 822 | 44 | 9 | 0 |
| 防御 | `battle_defend` | `common` | 716 | 0 | 0 | 0 |
| 攻撃 | `battle_attack` | `common` | 656 | 3 | 1 | 1 |
| 集中 | `control_focus` | `common` | 520 | 30 | 13 | 0 |
| 牽制 | `control_disrupt` | `common` | 497 | 13 | 6 | 0 |
| ステップ | `battle_step` | `common` | 370 | 1 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 4785 | 398 | 8.3% | 132 | 33.2% | 1 |
| `uncommon` | 28787 | 2541 | 8.8% | 1272 | 50.1% | 774 |
| `rare` | 6428 | 1631 | 25.4% | 693 | 42.5% | 611 |

#### Match Logs

- [draft_match_0001](matches/match_0001_AggroDraftBot_vs_AggroDraftBot.md)
- [draft_match_0001](matches/match_0001_AggroDraftBot_vs_AggroDraftBot.md)
- [draft_match_0002](matches/match_0002_AggroDraftBot_vs_AggroDraftBot.md)
- [draft_match_0002](matches/match_0002_AggroDraftBot_vs_AggroDraftBot.md)
- [draft_match_0003](matches/match_0003_AggroDraftBot_vs_AggroDraftBot.md)
- [draft_match_0003](matches/match_0003_AggroDraftBot_vs_AggroDraftBot.md)
- [draft_match_0004](matches/match_0004_AggroDraftBot_vs_AggroDraftBot.md)
- [draft_match_0004](matches/match_0004_AggroDraftBot_vs_AggroDraftBot.md)
- [draft_match_0005](matches/match_0005_AggroDraftBot_vs_AggroDraftBot.md)
- [draft_match_0005](matches/match_0005_AggroDraftBot_vs_AggroDraftBot.md)
- [draft_match_0006](matches/match_0006_AggroDraftBot_vs_AggroDraftBot.md)
- [draft_match_0006](matches/match_0006_AggroDraftBot_vs_AggroDraftBot.md)
- [draft_match_0007](matches/match_0007_AggroDraftBot_vs_AggroDraftBot.md)
- [draft_match_0007](matches/match_0007_AggroDraftBot_vs_AggroDraftBot.md)
- [draft_match_0008](matches/match_0008_AggroDraftBot_vs_AggroDraftBot.md)
- [draft_match_0008](matches/match_0008_AggroDraftBot_vs_AggroDraftBot.md)
- [draft_match_0009](matches/match_0009_AggroDraftBot_vs_AggroDraftBot.md)
- [draft_match_0009](matches/match_0009_AggroDraftBot_vs_AggroDraftBot.md)
- [draft_match_0010](matches/match_0010_AggroDraftBot_vs_AggroDraftBot.md)
- [draft_match_0010](matches/match_0010_AggroDraftBot_vs_AggroDraftBot.md)
