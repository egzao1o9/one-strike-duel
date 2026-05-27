# Draft Report

## Configuration

- Draft Bot 1: `StandardDraftBot`
- Draft Bot 2: `StandardDraftBot`
- Play Bot 1: `StandardBot`
- Play Bot 2: `StandardBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 1541
- Pool: `base_pool` (64 copies)
- Pairing Mode: mirrored seats per round
- Draft Flow: hidden 3->1, then public 5 with reverse-order picks

## Drafter Summary

| Drafter | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Winner Set Avg | Loser Set Avg | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate | Battle Avg | Control Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `StandardDraftBot` | 2000 | 898 | 898 | 204 | 44.9% | 35.6% | 39.5% | 0.3% | 60.1% | 1.6 | 1.39 | 35.7% | 54.1% | 33.2% | 33.5% | 33.3% | 13.78 | 6.22 | 7.7 | 3.61 | 2.46 | 6.22 | 2.34 | 14.43 | 3.22 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| StandardDraftBot vs StandardDraftBot | 1000 | 102 | `StandardDraftBot`=898 | 1.1 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 粉砕 | 505 |
| 2 | 踏み込み | 479 |
| 3 | 返し刃 | 428 |
| 4 | 大振り | 403 |
| 5 | 渾身 | 382 |
| 6 | 圧迫 | 333 |
| 7 | 前のめり | 326 |
| 8 | 受け直し | 261 |
| 9 | 十字受け | 243 |
| 10 | 蓄え | 237 |
| 11 | 疾走 | 187 |
| 12 | 強撃 | 160 |
| 13 | 踏ん張り | 155 |
| 14 | 勢い溜め | 127 |
| 15 | 補強 | 116 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 350 |
| 2 | 返し刃 | 242 |
| 3 | 粉砕 | 208 |
| 4 | 前のめり | 173 |
| 5 | 受け直し | 137 |
| 6 | 圧迫 | 134 |
| 7 | 疾走 | 120 |
| 8 | 十字受け | 120 |
| 9 | 渾身 | 99 |
| 10 | 蓄え | 97 |
| 11 | 大振り | 93 |
| 12 | 強撃 | 82 |
| 13 | 加速 | 68 |
| 14 | 踏ん張り | 60 |
| 15 | 鉄壁 | 59 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 344 |
| 2 | 返し刃 | 218 |
| 3 | 粉砕 | 200 |
| 4 | 疾走 | 111 |
| 5 | 十字受け | 106 |
| 6 | 渾身 | 92 |
| 7 | 大振り | 86 |
| 8 | 強撃 | 79 |
| 9 | 踏ん張り | 50 |
| 10 | 残像 | 32 |
| 11 | 貫き | 31 |
| 12 | 鉄壁 | 30 |
| 13 | 崩し | 27 |
| 14 | 押し込み | 23 |
| 15 | 受け流し | 3 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `StandardDraftBot` | 4.25 | 0.52 | 0.78 | 4.41 | 0.44 | -0.13 | 100 (5.0%) | 100 (11.1%) |

## Drafter Details

### StandardDraftBot

- Win Rate: 44.9%
- Draw Rate: 10.2%
- First Pass Win Rate: 35.6%
- Win With Fewer Cards: 39.5%
- Win With Same Cards: 0.3%
- Win With More Cards: 60.1%
- Winner Facedown Avg: 1.6
- Loser Facedown Avg: 1.39
- Starting Player Win Rate: 35.7%
- Responding Player Win Rate: 54.1%
- Final Stats Avg: A=4.25, B=0.52, S=0.78
- Losing Final Stats Avg: A=4.41, B=0.44, S=-0.13
- Lost With Speed Advantage: 100 (5.0%)
- Won After Blocking Faster Attack: 100 (11.1%)
- Action Rates: set=33.2%, set_pass=33.5%, pass=33.3%
- Turns: min=1, avg=1.1, max=3
- Battle / Control: avg=13.78 / 6.22
- Role Colors: red=7.7, blue=3.61, green=2.46, white=6.22
- Rarities: common=2.34, uncommon=14.43, rare=3.22

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 貫き | 1832 |
| 2 | 崩し | 1822 |
| 3 | 十字受け | 1773 |
| 4 | 踏ん張り | 1762 |
| 5 | 返し刃 | 1762 |
| 6 | 粉砕 | 1749 |
| 7 | 退き足 | 1656 |
| 8 | 受け直し | 1629 |
| 9 | 受け流し | 1620 |
| 10 | フェイント | 1614 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 貫き | 835 |
| 2 | 崩し | 825 |
| 3 | 返し刃 | 811 |
| 4 | 十字受け | 797 |
| 5 | 粉砕 | 750 |
| 6 | 踏ん張り | 748 |
| 7 | 低姿勢 | 747 |
| 8 | 受け直し | 741 |
| 9 | 強撃 | 729 |
| 10 | フェイント | 727 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 貫き | `battle_pierce` | `uncommon` | 1832 | 48 | 32 | 31 |
| 崩し | `battle_break` | `uncommon` | 1822 | 41 | 27 | 27 |
| 十字受け | `battle_cross_guard` | `uncommon` | 1773 | 243 | 120 | 106 |
| 返し刃 | `battle_counter` | `uncommon` | 1762 | 428 | 242 | 218 |
| 踏ん張り | `battle_brace` | `uncommon` | 1762 | 155 | 60 | 50 |
| 粉砕 | `battle_crush` | `uncommon` | 1749 | 505 | 208 | 200 |
| 退き足 | `battle_backstep` | `uncommon` | 1656 | 1 | 1 | 1 |
| 受け直し | `control_cover` | `uncommon` | 1629 | 261 | 137 | 0 |
| 受け流し | `battle_guard` | `uncommon` | 1620 | 7 | 3 | 3 |
| フェイント | `battle_feint` | `uncommon` | 1614 | 2 | 0 | 0 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 1596 | 0 | 0 | 0 |
| 強撃 | `battle_power_attack` | `uncommon` | 1595 | 160 | 82 | 79 |
| 押し込み | `battle_press` | `uncommon` | 1537 | 50 | 28 | 23 |
| 前のめり | `control_overclock` | `uncommon` | 1530 | 326 | 173 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 1471 | 77 | 48 | 0 |
| 補強 | `control_fortify` | `uncommon` | 1441 | 116 | 52 | 0 |
| 圧迫 | `control_pressure` | `common` | 1283 | 333 | 134 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 1251 | 127 | 55 | 0 |
| 加速 | `control_haste` | `uncommon` | 1226 | 112 | 68 | 0 |
| 鉄壁 | `battle_wall` | `rare` | 938 | 109 | 59 | 30 |
| 残像 | `battle_afterimage` | `rare` | 938 | 77 | 36 | 32 |
| 渾身 | `battle_all_in` | `rare` | 936 | 382 | 99 | 92 |
| 大振り | `battle_heavy_swing` | `rare` | 934 | 403 | 93 | 86 |
| 踏み込み | `battle_step_in` | `rare` | 933 | 479 | 350 | 344 |
| 疾走 | `battle_dash` | `rare` | 907 | 187 | 120 | 111 |
| 構え | `control_guard` | `common` | 886 | 47 | 14 | 0 |
| 蓄え | `control_reserve` | `rare` | 863 | 237 | 97 | 0 |
| 防御 | `battle_defend` | `common` | 768 | 0 | 0 | 0 |
| 攻撃 | `battle_attack` | `common` | 546 | 1 | 0 | 0 |
| 集中 | `control_focus` | `common` | 440 | 19 | 6 | 0 |
| 牽制 | `control_disrupt` | `common` | 424 | 14 | 6 | 0 |
| ステップ | `battle_step` | `common` | 338 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 4685 | 414 | 8.8% | 160 | 38.6% | 0 |
| `uncommon` | 28866 | 2659 | 9.2% | 1336 | 50.2% | 738 |
| `rare` | 6449 | 1874 | 29.1% | 854 | 45.6% | 695 |

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
