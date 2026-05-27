# Draft Report

## Configuration

- Draft Bot 1: `StandardDraftBot`
- Draft Bot 2: `RandomDraftBot`
- Play Bot 1: `StandardBot`
- Play Bot 2: `StandardBot`
- Rounds: 50
- Total Matches: 100
- Seed: 411
- Pool: `base_pool` (64 copies)
- Pairing Mode: mirrored seats per round
- Draft Flow: hidden 3->1, then public 5 with reverse-order picks

## Drafter Summary

| Drafter | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Winner Set Avg | Loser Set Avg | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate | Battle Avg | Control Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `RandomDraftBot` | 100 | 45 | 44 | 11 | 45.0% | 33.3% | 37.8% | 2.2% | 60.0% | 1.6 | 1.27 | 33.3% | 57.1% | 33.1% | 31.3% | 35.5% | 10.98 | 9.02 | 5.26 | 3.17 | 2.55 | 9.02 | 8.17 | 10.65 | 1.18 |
| `StandardDraftBot` | 100 | 44 | 45 | 11 | 44.0% | 38.8% | 38.6% | 4.5% | 56.8% | 1.45 | 1.38 | 38.8% | 49.0% | 31.5% | 37.0% | 31.5% | 14.52 | 5.48 | 8.86 | 3.73 | 1.93 | 5.48 | 1.33 | 13.86 | 4.81 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| RandomDraftBot vs StandardDraftBot | 100 | 11 | `RandomDraftBot`=45, `StandardDraftBot`=44 | 1.11 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 41 |
| 2 | 前のめり | 38 |
| 3 | 大振り | 38 |
| 4 | 粉砕 | 36 |
| 5 | 圧迫 | 33 |
| 6 | 渾身 | 33 |
| 7 | 返し刃 | 28 |
| 8 | 強撃 | 23 |
| 9 | 十字受け | 23 |
| 10 | 受け直し | 22 |
| 11 | 踏ん張り | 18 |
| 12 | 蓄え | 18 |
| 13 | 加速 | 15 |
| 14 | 補強 | 15 |
| 15 | 押し込み | 11 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 28 |
| 2 | 前のめり | 21 |
| 3 | 返し刃 | 19 |
| 4 | 圧迫 | 14 |
| 5 | 粉砕 | 13 |
| 6 | 強撃 | 12 |
| 7 | 十字受け | 10 |
| 8 | 渾身 | 10 |
| 9 | 踏ん張り | 10 |
| 10 | 大振り | 9 |
| 11 | 加速 | 8 |
| 12 | 補強 | 8 |
| 13 | 受け直し | 7 |
| 14 | 貫き | 7 |
| 15 | 疾走 | 6 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 27 |
| 2 | 返し刃 | 16 |
| 3 | 粉砕 | 13 |
| 4 | 強撃 | 11 |
| 5 | 十字受け | 9 |
| 6 | 渾身 | 9 |
| 7 | 踏ん張り | 9 |
| 8 | 大振り | 9 |
| 9 | 貫き | 7 |
| 10 | 疾走 | 6 |
| 11 | 押し込み | 5 |
| 12 | 崩し | 5 |
| 13 | 残像 | 3 |
| 14 | 攻撃 | 3 |
| 15 | 受け流し | 2 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `RandomDraftBot` | 2.73 | 0.91 | 1.03 | 2.5 | 0.84 | 0.68 | 13 (13.0%) | 6 (13.3%) |
| `StandardDraftBot` | 5 | 0.4 | 0.49 | 5.07 | 0.2 | -0.22 | 6 (6.0%) | 13 (29.5%) |

## Drafter Details

### RandomDraftBot

- Win Rate: 45.0%
- Draw Rate: 11.0%
- First Pass Win Rate: 33.3%
- Win With Fewer Cards: 37.8%
- Win With Same Cards: 2.2%
- Win With More Cards: 60.0%
- Winner Facedown Avg: 1.6
- Loser Facedown Avg: 1.27
- Starting Player Win Rate: 33.3%
- Responding Player Win Rate: 57.1%
- Final Stats Avg: A=2.73, B=0.91, S=1.03
- Losing Final Stats Avg: A=2.5, B=0.84, S=0.68
- Lost With Speed Advantage: 13 (13.0%)
- Won After Blocking Faster Attack: 6 (13.3%)
- Action Rates: set=33.1%, set_pass=31.3%, pass=35.5%
- Turns: min=1, avg=1.11, max=3
- Battle / Control: avg=10.98 / 9.02
- Role Colors: red=5.26, blue=3.17, green=2.55, white=9.02
- Rarities: common=8.17, uncommon=10.65, rare=1.18

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 124 |
| 2 | 構え | 123 |
| 3 | ステップ | 120 |
| 4 | 牽制 | 120 |
| 5 | 集中 | 119 |
| 6 | 圧迫 | 112 |
| 7 | 防御 | 99 |
| 8 | 低姿勢 | 77 |
| 9 | 補強 | 72 |
| 10 | 加速 | 71 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 牽制 | 61 |
| 2 | ステップ | 59 |
| 3 | 攻撃 | 53 |
| 4 | 集中 | 53 |
| 5 | 構え | 53 |
| 6 | 圧迫 | 43 |
| 7 | 防御 | 41 |
| 8 | 補強 | 38 |
| 9 | 重心落とし | 32 |
| 10 | 加速 | 32 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 124 | 7 | 4 | 3 |
| 構え | `control_guard` | `common` | 123 | 4 | 2 | 0 |
| 牽制 | `control_disrupt` | `common` | 120 | 2 | 1 | 0 |
| ステップ | `battle_step` | `common` | 120 | 1 | 0 | 0 |
| 集中 | `control_focus` | `common` | 119 | 4 | 1 | 0 |
| 圧迫 | `control_pressure` | `common` | 112 | 19 | 9 | 0 |
| 防御 | `battle_defend` | `common` | 99 | 3 | 0 | 0 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 77 | 3 | 1 | 1 |
| 補強 | `control_fortify` | `uncommon` | 72 | 9 | 4 | 0 |
| 加速 | `control_haste` | `uncommon` | 71 | 9 | 3 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 69 | 7 | 5 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 69 | 3 | 2 | 0 |
| 受け流し | `battle_guard` | `uncommon` | 65 | 6 | 1 | 1 |
| フェイント | `battle_feint` | `uncommon` | 63 | 1 | 0 | 0 |
| 強撃 | `battle_power_attack` | `uncommon` | 62 | 19 | 10 | 9 |
| 前のめり | `control_overclock` | `uncommon` | 61 | 20 | 10 | 0 |
| 押し込み | `battle_press` | `uncommon` | 61 | 11 | 6 | 5 |
| 粉砕 | `battle_crush` | `uncommon` | 60 | 22 | 9 | 9 |
| 受け直し | `control_cover` | `uncommon` | 56 | 12 | 4 | 0 |
| 踏ん張り | `battle_brace` | `uncommon` | 55 | 9 | 6 | 6 |
| 十字受け | `battle_cross_guard` | `uncommon` | 52 | 14 | 7 | 6 |
| 退き足 | `battle_backstep` | `uncommon` | 49 | 1 | 0 | 0 |
| 返し刃 | `battle_counter` | `uncommon` | 47 | 16 | 13 | 11 |
| 貫き | `battle_pierce` | `uncommon` | 40 | 6 | 5 | 5 |
| 崩し | `battle_break` | `uncommon` | 36 | 5 | 3 | 3 |
| 蓄え | `control_reserve` | `rare` | 30 | 8 | 3 | 0 |
| 残像 | `battle_afterimage` | `rare` | 17 | 6 | 4 | 3 |
| 疾走 | `battle_dash` | `rare` | 16 | 4 | 3 | 3 |
| 大振り | `battle_heavy_swing` | `rare` | 15 | 8 | 0 | 0 |
| 渾身 | `battle_all_in` | `rare` | 15 | 7 | 2 | 2 |
| 鉄壁 | `battle_wall` | `rare` | 14 | 3 | 2 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 11 | 6 | 5 | 5 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 817 | 40 | 4.9% | 17 | 42.5% | 3 |
| `uncommon` | 1065 | 173 | 16.2% | 89 | 51.4% | 56 |
| `rare` | 118 | 42 | 35.6% | 19 | 45.2% | 13 |

#### Match Logs

- [draft_match_0001](matches/match_0001_StandardDraftBot_vs_RandomDraftBot.md)
- [draft_match_0002](matches/match_0002_RandomDraftBot_vs_StandardDraftBot.md)
- [draft_match_0003](matches/match_0003_StandardDraftBot_vs_RandomDraftBot.md)
- [draft_match_0004](matches/match_0004_RandomDraftBot_vs_StandardDraftBot.md)
- [draft_match_0005](matches/match_0005_StandardDraftBot_vs_RandomDraftBot.md)
- [draft_match_0006](matches/match_0006_RandomDraftBot_vs_StandardDraftBot.md)
- [draft_match_0007](matches/match_0007_StandardDraftBot_vs_RandomDraftBot.md)
- [draft_match_0008](matches/match_0008_RandomDraftBot_vs_StandardDraftBot.md)
- [draft_match_0009](matches/match_0009_StandardDraftBot_vs_RandomDraftBot.md)
- [draft_match_0010](matches/match_0010_RandomDraftBot_vs_StandardDraftBot.md)
- [draft_match_0011](matches/match_0011_StandardDraftBot_vs_RandomDraftBot.md)
- [draft_match_0012](matches/match_0012_RandomDraftBot_vs_StandardDraftBot.md)
- [draft_match_0013](matches/match_0013_StandardDraftBot_vs_RandomDraftBot.md)
- [draft_match_0014](matches/match_0014_RandomDraftBot_vs_StandardDraftBot.md)
- [draft_match_0015](matches/match_0015_StandardDraftBot_vs_RandomDraftBot.md)
- [draft_match_0016](matches/match_0016_RandomDraftBot_vs_StandardDraftBot.md)
- [draft_match_0017](matches/match_0017_StandardDraftBot_vs_RandomDraftBot.md)
- [draft_match_0018](matches/match_0018_RandomDraftBot_vs_StandardDraftBot.md)
- [draft_match_0019](matches/match_0019_StandardDraftBot_vs_RandomDraftBot.md)
- [draft_match_0020](matches/match_0020_RandomDraftBot_vs_StandardDraftBot.md)

### StandardDraftBot

- Win Rate: 44.0%
- Draw Rate: 11.0%
- First Pass Win Rate: 38.8%
- Win With Fewer Cards: 38.6%
- Win With Same Cards: 4.5%
- Win With More Cards: 56.8%
- Winner Facedown Avg: 1.45
- Loser Facedown Avg: 1.38
- Starting Player Win Rate: 38.8%
- Responding Player Win Rate: 49.0%
- Final Stats Avg: A=5, B=0.4, S=0.49
- Losing Final Stats Avg: A=5.07, B=0.2, S=-0.22
- Lost With Speed Advantage: 6 (6.0%)
- Won After Blocking Faster Attack: 13 (29.5%)
- Action Rates: set=31.5%, set_pass=37.0%, pass=31.5%
- Turns: min=1, avg=1.11, max=3
- Battle / Control: avg=14.52 / 5.48
- Role Colors: red=8.86, blue=3.73, green=1.93, white=5.48
- Rarities: common=1.33, uncommon=13.86, rare=4.81

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 貫き | 129 |
| 2 | 崩し | 126 |
| 3 | 返し刃 | 100 |
| 4 | 十字受け | 98 |
| 5 | 踏ん張り | 92 |
| 6 | 粉砕 | 87 |
| 7 | 受け直し | 82 |
| 8 | 踏み込み | 81 |
| 9 | 渾身 | 77 |
| 10 | 重心落とし | 73 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 貫き | 57 |
| 2 | 崩し | 57 |
| 3 | 返し刃 | 47 |
| 4 | 踏ん張り | 45 |
| 5 | 十字受け | 45 |
| 6 | 踏み込み | 40 |
| 7 | 前のめり | 36 |
| 8 | 退き足 | 35 |
| 9 | 粉砕 | 34 |
| 10 | 受け直し | 34 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 貫き | `battle_pierce` | `uncommon` | 129 | 2 | 2 | 2 |
| 崩し | `battle_break` | `uncommon` | 126 | 5 | 2 | 2 |
| 返し刃 | `battle_counter` | `uncommon` | 100 | 12 | 6 | 5 |
| 十字受け | `battle_cross_guard` | `uncommon` | 98 | 9 | 3 | 3 |
| 踏ん張り | `battle_brace` | `uncommon` | 92 | 9 | 4 | 3 |
| 粉砕 | `battle_crush` | `uncommon` | 87 | 14 | 4 | 4 |
| 受け直し | `control_cover` | `uncommon` | 82 | 10 | 3 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 81 | 35 | 23 | 22 |
| 渾身 | `battle_all_in` | `rare` | 77 | 26 | 8 | 7 |
| 大振り | `battle_heavy_swing` | `rare` | 73 | 30 | 9 | 9 |
| 前のめり | `control_overclock` | `uncommon` | 73 | 18 | 11 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 73 | 1 | 1 | 0 |
| 退き足 | `battle_backstep` | `uncommon` | 70 | 0 | 0 | 0 |
| 鉄壁 | `battle_wall` | `rare` | 69 | 6 | 1 | 1 |
| 残像 | `battle_afterimage` | `rare` | 68 | 4 | 1 | 0 |
| 疾走 | `battle_dash` | `rare` | 67 | 5 | 3 | 3 |
| フェイント | `battle_feint` | `uncommon` | 66 | 0 | 0 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 63 | 4 | 1 | 0 |
| 補強 | `control_fortify` | `uncommon` | 61 | 6 | 4 | 0 |
| 押し込み | `battle_press` | `uncommon` | 59 | 0 | 0 | 0 |
| 受け流し | `battle_guard` | `uncommon` | 58 | 1 | 1 | 1 |
| 強撃 | `battle_power_attack` | `uncommon` | 53 | 4 | 2 | 2 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 52 | 0 | 0 | 0 |
| 蓄え | `control_reserve` | `rare` | 46 | 10 | 3 | 0 |
| 加速 | `control_haste` | `uncommon` | 44 | 6 | 5 | 0 |
| 圧迫 | `control_pressure` | `common` | 40 | 14 | 5 | 0 |
| 構え | `control_guard` | `common` | 29 | 1 | 0 | 0 |
| 集中 | `control_focus` | `common` | 22 | 0 | 0 | 0 |
| 牽制 | `control_disrupt` | `common` | 15 | 0 | 0 | 0 |
| 防御 | `battle_defend` | `common` | 14 | 0 | 0 | 0 |
| 攻撃 | `battle_attack` | `common` | 9 | 0 | 0 | 0 |
| ステップ | `battle_step` | `common` | 4 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 133 | 15 | 11.3% | 5 | 33.3% | 0 |
| `uncommon` | 1386 | 101 | 7.3% | 49 | 48.5% | 22 |
| `rare` | 481 | 116 | 24.1% | 48 | 41.4% | 42 |

#### Match Logs

- [draft_match_0001](matches/match_0001_StandardDraftBot_vs_RandomDraftBot.md)
- [draft_match_0002](matches/match_0002_RandomDraftBot_vs_StandardDraftBot.md)
- [draft_match_0003](matches/match_0003_StandardDraftBot_vs_RandomDraftBot.md)
- [draft_match_0004](matches/match_0004_RandomDraftBot_vs_StandardDraftBot.md)
- [draft_match_0005](matches/match_0005_StandardDraftBot_vs_RandomDraftBot.md)
- [draft_match_0006](matches/match_0006_RandomDraftBot_vs_StandardDraftBot.md)
- [draft_match_0007](matches/match_0007_StandardDraftBot_vs_RandomDraftBot.md)
- [draft_match_0008](matches/match_0008_RandomDraftBot_vs_StandardDraftBot.md)
- [draft_match_0009](matches/match_0009_StandardDraftBot_vs_RandomDraftBot.md)
- [draft_match_0010](matches/match_0010_RandomDraftBot_vs_StandardDraftBot.md)
- [draft_match_0011](matches/match_0011_StandardDraftBot_vs_RandomDraftBot.md)
- [draft_match_0012](matches/match_0012_RandomDraftBot_vs_StandardDraftBot.md)
- [draft_match_0013](matches/match_0013_StandardDraftBot_vs_RandomDraftBot.md)
- [draft_match_0014](matches/match_0014_RandomDraftBot_vs_StandardDraftBot.md)
- [draft_match_0015](matches/match_0015_StandardDraftBot_vs_RandomDraftBot.md)
- [draft_match_0016](matches/match_0016_RandomDraftBot_vs_StandardDraftBot.md)
- [draft_match_0017](matches/match_0017_StandardDraftBot_vs_RandomDraftBot.md)
- [draft_match_0018](matches/match_0018_RandomDraftBot_vs_StandardDraftBot.md)
- [draft_match_0019](matches/match_0019_StandardDraftBot_vs_RandomDraftBot.md)
- [draft_match_0020](matches/match_0020_RandomDraftBot_vs_StandardDraftBot.md)
