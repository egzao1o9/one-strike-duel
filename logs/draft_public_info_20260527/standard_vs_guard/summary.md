# Draft Report

## Configuration

- Draft Bot 1: `StandardDraftBot`
- Draft Bot 2: `GuardDraftBot`
- Play Bot 1: `StandardBot`
- Play Bot 2: `StandardBot`
- Rounds: 50
- Total Matches: 100
- Seed: 431
- Pool: `base_pool` (64 copies)
- Pairing Mode: mirrored seats per round
- Draft Flow: hidden 3->1, then public 5 with reverse-order picks

## Drafter Summary

| Drafter | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Winner Set Avg | Loser Set Avg | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate | Battle Avg | Control Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `GuardDraftBot` | 100 | 49 | 38 | 13 | 49.0% | 40.9% | 36.7% | 0.0% | 63.3% | 1.61 | 1.45 | 40.9% | 55.4% | 34.1% | 31.8% | 34.1% | 13.77 | 6.23 | 7.67 | 3.48 | 2.62 | 6.23 | 2.47 | 14.05 | 3.48 |
| `StandardDraftBot` | 100 | 38 | 49 | 13 | 38.0% | 30.4% | 44.7% | 0.0% | 55.3% | 1.55 | 1.35 | 30.4% | 47.7% | 32.1% | 34.5% | 33.3% | 13.73 | 6.27 | 7.67 | 3.66 | 2.4 | 6.27 | 2.38 | 14.63 | 2.99 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| GuardDraftBot vs StandardDraftBot | 100 | 13 | `GuardDraftBot`=49, `StandardDraftBot`=38 | 1.12 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 57 |
| 2 | 粉砕 | 45 |
| 3 | 大振り | 43 |
| 4 | 渾身 | 42 |
| 5 | 圧迫 | 40 |
| 6 | 返し刃 | 36 |
| 7 | 前のめり | 25 |
| 8 | 十字受け | 24 |
| 9 | 受け直し | 21 |
| 10 | 踏ん張り | 20 |
| 11 | 蓄え | 20 |
| 12 | 勢い溜め | 18 |
| 13 | 加速 | 17 |
| 14 | 強撃 | 13 |
| 15 | 疾走 | 13 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 40 |
| 2 | 返し刃 | 20 |
| 3 | 粉砕 | 17 |
| 4 | 圧迫 | 15 |
| 5 | 渾身 | 14 |
| 6 | 前のめり | 14 |
| 7 | 受け直し | 13 |
| 8 | 十字受け | 12 |
| 9 | 加速 | 8 |
| 10 | 大振り | 7 |
| 11 | 強撃 | 7 |
| 12 | 鉄壁 | 7 |
| 13 | 勢い溜め | 7 |
| 14 | 踏ん張り | 7 |
| 15 | 疾走 | 6 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 39 |
| 2 | 返し刃 | 17 |
| 3 | 粉砕 | 15 |
| 4 | 渾身 | 14 |
| 5 | 十字受け | 10 |
| 6 | 大振り | 7 |
| 7 | 強撃 | 6 |
| 8 | 鉄壁 | 6 |
| 9 | 疾走 | 6 |
| 10 | 踏ん張り | 5 |
| 11 | 貫き | 4 |
| 12 | 崩し | 3 |
| 13 | 押し込み | 2 |
| 14 | 受け流し | 2 |
| 15 | 残像 | 2 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `GuardDraftBot` | 4.64 | 0.53 | 0.73 | 5.05 | 0.37 | -0.66 | 6 (6.0%) | 6 (12.2%) |
| `StandardDraftBot` | 4.26 | 0.57 | 0.54 | 4.29 | 0.51 | -0.24 | 6 (6.0%) | 6 (15.8%) |

## Drafter Details

### GuardDraftBot

- Win Rate: 49.0%
- Draw Rate: 13.0%
- First Pass Win Rate: 40.9%
- Win With Fewer Cards: 36.7%
- Win With Same Cards: 0.0%
- Win With More Cards: 63.3%
- Winner Facedown Avg: 1.61
- Loser Facedown Avg: 1.45
- Starting Player Win Rate: 40.9%
- Responding Player Win Rate: 55.4%
- Final Stats Avg: A=4.64, B=0.53, S=0.73
- Losing Final Stats Avg: A=5.05, B=0.37, S=-0.66
- Lost With Speed Advantage: 6 (6.0%)
- Won After Blocking Faster Attack: 6 (12.2%)
- Action Rates: set=34.1%, set_pass=31.8%, pass=34.1%
- Turns: min=1, avg=1.12, max=3
- Battle / Control: avg=13.77 / 6.23
- Role Colors: red=7.67, blue=3.48, green=2.62, white=6.23
- Rarities: common=2.47, uncommon=14.05, rare=3.48

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏ん張り | 95 |
| 2 | 貫き | 91 |
| 3 | 崩し | 88 |
| 4 | 粉砕 | 87 |
| 5 | 受け直し | 84 |
| 6 | 返し刃 | 84 |
| 7 | 受け流し | 83 |
| 8 | 十字受け | 81 |
| 9 | 退き足 | 80 |
| 10 | 押し込み | 79 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 貫き | 49 |
| 2 | 受け直し | 45 |
| 3 | 退き足 | 44 |
| 4 | 返し刃 | 43 |
| 5 | 押し込み | 42 |
| 6 | 低姿勢 | 42 |
| 7 | 踏ん張り | 42 |
| 8 | 十字受け | 41 |
| 9 | 粉砕 | 39 |
| 10 | 崩し | 38 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 踏ん張り | `battle_brace` | `uncommon` | 95 | 9 | 2 | 1 |
| 貫き | `battle_pierce` | `uncommon` | 91 | 4 | 3 | 3 |
| 崩し | `battle_break` | `uncommon` | 88 | 4 | 2 | 2 |
| 粉砕 | `battle_crush` | `uncommon` | 87 | 22 | 10 | 8 |
| 返し刃 | `battle_counter` | `uncommon` | 84 | 18 | 11 | 10 |
| 受け直し | `control_cover` | `uncommon` | 84 | 12 | 9 | 0 |
| 受け流し | `battle_guard` | `uncommon` | 83 | 2 | 2 | 2 |
| 十字受け | `battle_cross_guard` | `uncommon` | 81 | 11 | 8 | 8 |
| 退き足 | `battle_backstep` | `uncommon` | 80 | 0 | 0 | 0 |
| 押し込み | `battle_press` | `uncommon` | 79 | 1 | 1 | 0 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 77 | 0 | 0 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 71 | 12 | 9 | 0 |
| 補強 | `control_fortify` | `uncommon` | 71 | 5 | 2 | 0 |
| フェイント | `battle_feint` | `uncommon` | 71 | 0 | 0 | 0 |
| 強撃 | `battle_power_attack` | `uncommon` | 70 | 5 | 3 | 2 |
| 重心落とし | `control_anchor` | `uncommon` | 70 | 3 | 1 | 0 |
| 圧迫 | `control_pressure` | `common` | 68 | 19 | 8 | 0 |
| 加速 | `control_haste` | `uncommon` | 66 | 5 | 1 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 57 | 34 | 24 | 24 |
| 勢い溜め | `control_momentum` | `uncommon` | 57 | 6 | 3 | 0 |
| 鉄壁 | `battle_wall` | `rare` | 53 | 5 | 4 | 4 |
| 残像 | `battle_afterimage` | `rare` | 53 | 3 | 2 | 2 |
| 渾身 | `battle_all_in` | `rare` | 49 | 26 | 8 | 8 |
| 蓄え | `control_reserve` | `rare` | 49 | 12 | 5 | 0 |
| 防御 | `battle_defend` | `common` | 49 | 0 | 0 | 0 |
| 大振り | `battle_heavy_swing` | `rare` | 44 | 19 | 3 | 3 |
| 疾走 | `battle_dash` | `rare` | 43 | 6 | 2 | 2 |
| 構え | `control_guard` | `common` | 41 | 3 | 1 | 0 |
| 牽制 | `control_disrupt` | `common` | 23 | 1 | 1 | 0 |
| 集中 | `control_focus` | `common` | 23 | 1 | 1 | 0 |
| 攻撃 | `battle_attack` | `common` | 23 | 0 | 0 | 0 |
| ステップ | `battle_step` | `common` | 20 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 247 | 24 | 9.7% | 11 | 45.8% | 0 |
| `uncommon` | 1405 | 119 | 8.5% | 67 | 56.3% | 36 |
| `rare` | 348 | 105 | 30.2% | 48 | 45.7% | 43 |

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

- Win Rate: 38.0%
- Draw Rate: 13.0%
- First Pass Win Rate: 30.4%
- Win With Fewer Cards: 44.7%
- Win With Same Cards: 0.0%
- Win With More Cards: 55.3%
- Winner Facedown Avg: 1.55
- Loser Facedown Avg: 1.35
- Starting Player Win Rate: 30.4%
- Responding Player Win Rate: 47.7%
- Final Stats Avg: A=4.26, B=0.57, S=0.54
- Losing Final Stats Avg: A=4.29, B=0.51, S=-0.24
- Lost With Speed Advantage: 6 (6.0%)
- Won After Blocking Faster Attack: 6 (15.8%)
- Action Rates: set=32.1%, set_pass=34.5%, pass=33.3%
- Turns: min=1, avg=1.12, max=3
- Battle / Control: avg=13.73 / 6.27
- Role Colors: red=7.67, blue=3.66, green=2.4, white=6.27
- Rarities: common=2.38, uncommon=14.63, rare=2.99

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 貫き | 97 |
| 2 | 崩し | 97 |
| 3 | 粉砕 | 96 |
| 4 | 十字受け | 95 |
| 5 | フェイント | 92 |
| 6 | 踏ん張り | 86 |
| 7 | 受け流し | 84 |
| 8 | 返し刃 | 81 |
| 9 | 勢い溜め | 80 |
| 10 | 押し込み | 78 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | フェイント | 36 |
| 2 | 十字受け | 36 |
| 3 | 低姿勢 | 34 |
| 4 | 返し刃 | 34 |
| 5 | 貫き | 33 |
| 6 | 崩し | 33 |
| 7 | 退き足 | 33 |
| 8 | 粉砕 | 32 |
| 9 | 受け流し | 32 |
| 10 | 踏ん張り | 32 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 貫き | `battle_pierce` | `uncommon` | 97 | 3 | 1 | 1 |
| 崩し | `battle_break` | `uncommon` | 97 | 2 | 1 | 1 |
| 粉砕 | `battle_crush` | `uncommon` | 96 | 23 | 7 | 7 |
| 十字受け | `battle_cross_guard` | `uncommon` | 95 | 13 | 4 | 2 |
| フェイント | `battle_feint` | `uncommon` | 92 | 0 | 0 | 0 |
| 踏ん張り | `battle_brace` | `uncommon` | 86 | 11 | 5 | 4 |
| 受け流し | `battle_guard` | `uncommon` | 84 | 0 | 0 | 0 |
| 返し刃 | `battle_counter` | `uncommon` | 81 | 18 | 9 | 7 |
| 勢い溜め | `control_momentum` | `uncommon` | 80 | 12 | 4 | 0 |
| 押し込み | `battle_press` | `uncommon` | 78 | 6 | 3 | 2 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 78 | 0 | 0 | 0 |
| 退き足 | `battle_backstep` | `uncommon` | 78 | 0 | 0 | 0 |
| 強撃 | `battle_power_attack` | `uncommon` | 76 | 8 | 4 | 4 |
| 前のめり | `control_overclock` | `uncommon` | 74 | 13 | 5 | 0 |
| 受け直し | `control_cover` | `uncommon` | 71 | 9 | 4 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 70 | 4 | 2 | 0 |
| 圧迫 | `control_pressure` | `common` | 67 | 21 | 7 | 0 |
| 補強 | `control_fortify` | `uncommon` | 67 | 2 | 2 | 0 |
| 加速 | `control_haste` | `uncommon` | 63 | 12 | 7 | 0 |
| 大振り | `battle_heavy_swing` | `rare` | 48 | 24 | 4 | 4 |
| 構え | `control_guard` | `common` | 48 | 2 | 0 | 0 |
| 疾走 | `battle_dash` | `rare` | 47 | 7 | 4 | 4 |
| 渾身 | `battle_all_in` | `rare` | 45 | 16 | 6 | 6 |
| 鉄壁 | `battle_wall` | `rare` | 42 | 7 | 3 | 2 |
| 残像 | `battle_afterimage` | `rare` | 41 | 2 | 0 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 39 | 23 | 16 | 15 |
| 蓄え | `control_reserve` | `rare` | 37 | 8 | 1 | 0 |
| 防御 | `battle_defend` | `common` | 36 | 0 | 0 | 0 |
| 集中 | `control_focus` | `common` | 29 | 0 | 0 | 0 |
| 攻撃 | `battle_attack` | `common` | 24 | 0 | 0 | 0 |
| 牽制 | `control_disrupt` | `common` | 21 | 1 | 1 | 0 |
| ステップ | `battle_step` | `common` | 13 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 238 | 24 | 10.1% | 8 | 33.3% | 0 |
| `uncommon` | 1463 | 136 | 9.3% | 58 | 42.6% | 28 |
| `rare` | 299 | 87 | 29.1% | 34 | 39.1% | 31 |

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
