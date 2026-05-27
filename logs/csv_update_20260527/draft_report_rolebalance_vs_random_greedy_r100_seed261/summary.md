# Draft Role Balance Report

## Configuration

- Draft Bot 1: `RoleBalanceDraftBot`
- Draft Bot 2: `RandomDraftBot`
- Play Bot 1: `GreedyBot`
- Play Bot 2: `GreedyBot`
- Rounds: 100
- Total Matches: 200
- Seed: 261
- Pool: `base_pool` (64 copies)
- Pairing Mode: mirrored seats per round

## Drafter Summary

| Drafter | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Winner Set Avg | Loser Set Avg | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate | Battle Avg | Control Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `RandomDraftBot` | 200 | 107 | 73 | 20 | 53.5% | 36.5% | 0.9% | 60.7% | 38.3% | 1.46 | 1.45 | 58.4% | 48.5% | 33.2% | 61.2% | 5.6% | 11.7 | 8.3 | 5.6 | 3.4 | 2.69 | 8.3 | 8.13 | 11.39 | 0.48 |
| `RoleBalanceDraftBot` | 200 | 73 | 107 | 20 | 36.5% | 28.4% | 20.5% | 61.6% | 17.8% | 1.42 | 1.08 | 39.4% | 33.7% | 20.1% | 74.0% | 5.9% | 12 | 8 | 7.0 | 3.0 | 2 | 8 | 0.07 | 13.41 | 6.52 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| RandomDraftBot vs RoleBalanceDraftBot | 200 | 20 | `RandomDraftBot`=107, `RoleBalanceDraftBot`=73 | 1.07 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 圧迫 | 68 |
| 2 | 粉砕 | 63 |
| 3 | 渾身 | 60 |
| 4 | 大振り | 53 |
| 5 | 攻撃 | 51 |
| 6 | 貫き | 44 |
| 7 | 崩し | 42 |
| 8 | 踏み込み | 36 |
| 9 | 強撃 | 35 |
| 10 | 返し刃 | 25 |
| 11 | 踏ん張り | 24 |
| 12 | 疾走 | 23 |
| 13 | 受け流し | 23 |
| 14 | 十字受け | 22 |
| 15 | ステップ | 22 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 圧迫 | 38 |
| 2 | 貫き | 34 |
| 3 | 踏み込み | 33 |
| 4 | 攻撃 | 33 |
| 5 | 崩し | 24 |
| 6 | 粉砕 | 22 |
| 7 | 強撃 | 21 |
| 8 | 返し刃 | 19 |
| 9 | 疾走 | 15 |
| 10 | 押し込み | 11 |
| 11 | 十字受け | 10 |
| 12 | 踏ん張り | 10 |
| 13 | 大振り | 9 |
| 14 | 渾身 | 9 |
| 15 | 受け流し | 9 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 貫き | 33 |
| 2 | 踏み込み | 33 |
| 3 | 攻撃 | 31 |
| 4 | 崩し | 23 |
| 5 | 粉砕 | 22 |
| 6 | 強撃 | 21 |
| 7 | 返し刃 | 15 |
| 8 | 疾走 | 13 |
| 9 | 押し込み | 10 |
| 10 | 大振り | 9 |
| 11 | 渾身 | 9 |
| 12 | 受け流し | 8 |
| 13 | 十字受け | 7 |
| 14 | ステップ | 6 |
| 15 | 踏ん張り | 5 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `RandomDraftBot` | 1.99 | 0.49 | 0.57 | 1.67 | 0.6 | 0.59 | 20 (10.0%) | 7 (6.5%) |
| `RoleBalanceDraftBot` | 4.06 | 0.15 | 0.07 | 4.44 | 0.05 | -0.89 | 7 (3.5%) | 20 (27.4%) |

## Drafter Details

### RandomDraftBot

- Win Rate: 53.5%
- Draw Rate: 10.0%
- First Pass Win Rate: 36.5%
- Win With Fewer Cards: 0.9%
- Win With Same Cards: 60.7%
- Win With More Cards: 38.3%
- Winner Facedown Avg: 1.46
- Loser Facedown Avg: 1.45
- Starting Player Win Rate: 58.4%
- Responding Player Win Rate: 48.5%
- Final Stats Avg: A=1.99, B=0.49, S=0.57
- Losing Final Stats Avg: A=1.67, B=0.6, S=0.59
- Lost With Speed Advantage: 20 (10.0%)
- Won After Blocking Faster Attack: 7 (6.5%)
- Action Rates: set=33.2%, set_pass=61.2%, pass=5.6%
- Turns: min=1, avg=1.07, max=3
- Battle / Control: avg=11.7 / 8.3
- Role Colors: red=5.6, blue=3.4, green=2.69, white=8.3
- Rarities: common=8.13, uncommon=11.39, rare=0.48

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 防御 | 247 |
| 2 | 構え | 246 |
| 3 | 集中 | 236 |
| 4 | 牽制 | 231 |
| 5 | 攻撃 | 229 |
| 6 | 圧迫 | 223 |
| 7 | ステップ | 214 |
| 8 | 押し込み | 158 |
| 9 | 退き足 | 155 |
| 10 | 受け流し | 147 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 防御 | 138 |
| 2 | 圧迫 | 125 |
| 3 | 牽制 | 124 |
| 4 | 攻撃 | 123 |
| 5 | 構え | 123 |
| 6 | 集中 | 119 |
| 7 | ステップ | 114 |
| 8 | 押し込み | 85 |
| 9 | 強撃 | 84 |
| 10 | 退き足 | 80 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 防御 | `battle_defend` | `common` | 247 | 17 | 7 | 4 |
| 構え | `control_guard` | `common` | 246 | 0 | 0 | 0 |
| 集中 | `control_focus` | `common` | 236 | 0 | 0 | 0 |
| 牽制 | `control_disrupt` | `common` | 231 | 0 | 0 | 0 |
| 攻撃 | `battle_attack` | `common` | 229 | 51 | 33 | 31 |
| 圧迫 | `control_pressure` | `common` | 223 | 67 | 38 | 0 |
| ステップ | `battle_step` | `common` | 214 | 22 | 7 | 6 |
| 押し込み | `battle_press` | `uncommon` | 158 | 21 | 11 | 10 |
| 退き足 | `battle_backstep` | `uncommon` | 155 | 10 | 3 | 0 |
| 受け流し | `battle_guard` | `uncommon` | 147 | 18 | 7 | 6 |
| フェイント | `battle_feint` | `uncommon` | 146 | 6 | 2 | 0 |
| 強撃 | `battle_power_attack` | `uncommon` | 142 | 35 | 21 | 21 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 130 | 9 | 2 | 1 |
| 踏ん張り | `battle_brace` | `uncommon` | 128 | 14 | 7 | 4 |
| 返し刃 | `battle_counter` | `uncommon` | 127 | 19 | 14 | 11 |
| 十字受け | `battle_cross_guard` | `uncommon` | 126 | 11 | 4 | 4 |
| 前のめり | `control_overclock` | `uncommon` | 126 | 0 | 0 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 125 | 0 | 0 | 0 |
| 粉砕 | `battle_crush` | `uncommon` | 119 | 41 | 20 | 20 |
| 加速 | `control_haste` | `uncommon` | 118 | 0 | 0 | 0 |
| 受け直し | `control_cover` | `uncommon` | 116 | 0 | 0 | 0 |
| 補強 | `control_fortify` | `uncommon` | 111 | 0 | 0 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 105 | 0 | 0 | 0 |
| 崩し | `battle_break` | `uncommon` | 102 | 27 | 15 | 14 |
| 貫き | `battle_pierce` | `uncommon` | 97 | 25 | 20 | 19 |
| 蓄え | `control_reserve` | `rare` | 23 | 0 | 0 | 0 |
| 疾走 | `battle_dash` | `rare` | 22 | 5 | 4 | 3 |
| 残像 | `battle_afterimage` | `rare` | 18 | 1 | 1 | 0 |
| 鉄壁 | `battle_wall` | `rare` | 15 | 0 | 0 | 0 |
| 大振り | `battle_heavy_swing` | `rare` | 11 | 3 | 0 | 0 |
| 渾身 | `battle_all_in` | `rare` | 4 | 2 | 1 | 1 |
| 踏み込み | `battle_step_in` | `rare` | 3 | 1 | 1 | 1 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 1626 | 157 | 9.7% | 85 | 54.1% | 41 |
| `uncommon` | 2278 | 236 | 10.4% | 126 | 53.4% | 110 |
| `rare` | 96 | 12 | 12.5% | 7 | 58.3% | 5 |

#### Match Logs

- [draft_match_0001](matches/match_0001_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0002](matches/match_0002_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0003](matches/match_0003_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0004](matches/match_0004_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0005](matches/match_0005_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0006](matches/match_0006_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0007](matches/match_0007_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0008](matches/match_0008_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0009](matches/match_0009_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0010](matches/match_0010_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0011](matches/match_0011_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0012](matches/match_0012_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0013](matches/match_0013_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0014](matches/match_0014_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0015](matches/match_0015_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0016](matches/match_0016_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0017](matches/match_0017_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0018](matches/match_0018_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0019](matches/match_0019_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0020](matches/match_0020_RandomDraftBot_vs_RoleBalanceDraftBot.md)

### RoleBalanceDraftBot

- Win Rate: 36.5%
- Draw Rate: 10.0%
- First Pass Win Rate: 28.4%
- Win With Fewer Cards: 20.5%
- Win With Same Cards: 61.6%
- Win With More Cards: 17.8%
- Winner Facedown Avg: 1.42
- Loser Facedown Avg: 1.08
- Starting Player Win Rate: 39.4%
- Responding Player Win Rate: 33.7%
- Final Stats Avg: A=4.06, B=0.15, S=0.07
- Losing Final Stats Avg: A=4.44, B=0.05, S=-0.89
- Lost With Speed Advantage: 7 (3.5%)
- Won After Blocking Faster Attack: 20 (27.4%)
- Action Rates: set=20.1%, set_pass=74.0%, pass=5.9%
- Turns: min=1, avg=1.07, max=3
- Battle / Control: avg=12 / 8
- Role Colors: red=7.0, blue=3.0, green=2, white=8
- Rarities: common=0.07, uncommon=13.41, rare=6.52

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 受け直し | 267 |
| 2 | 前のめり | 263 |
| 3 | 加速 | 229 |
| 4 | 重心落とし | 225 |
| 5 | 補強 | 219 |
| 6 | 勢い溜め | 206 |
| 7 | 崩し | 202 |
| 8 | 踏み込み | 197 |
| 9 | 貫き | 197 |
| 10 | 渾身 | 196 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 受け直し | 103 |
| 2 | 前のめり | 102 |
| 3 | 重心落とし | 82 |
| 4 | 補強 | 79 |
| 5 | 加速 | 78 |
| 6 | 勢い溜め | 75 |
| 7 | 崩し | 74 |
| 8 | 踏み込み | 72 |
| 9 | 貫き | 72 |
| 10 | 渾身 | 70 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 受け直し | `control_cover` | `uncommon` | 267 | 0 | 0 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 263 | 0 | 0 | 0 |
| 加速 | `control_haste` | `uncommon` | 229 | 0 | 0 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 225 | 0 | 0 | 0 |
| 補強 | `control_fortify` | `uncommon` | 219 | 0 | 0 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 206 | 0 | 0 | 0 |
| 崩し | `battle_break` | `uncommon` | 202 | 15 | 9 | 9 |
| 踏み込み | `battle_step_in` | `rare` | 197 | 35 | 32 | 32 |
| 貫き | `battle_pierce` | `uncommon` | 197 | 19 | 14 | 14 |
| 渾身 | `battle_all_in` | `rare` | 196 | 58 | 8 | 8 |
| 粉砕 | `battle_crush` | `uncommon` | 194 | 22 | 2 | 2 |
| 大振り | `battle_heavy_swing` | `rare` | 189 | 50 | 9 | 9 |
| 十字受け | `battle_cross_guard` | `uncommon` | 186 | 11 | 6 | 3 |
| 鉄壁 | `battle_wall` | `rare` | 185 | 11 | 4 | 3 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 185 | 9 | 4 | 3 |
| 残像 | `battle_afterimage` | `rare` | 182 | 11 | 4 | 3 |
| 疾走 | `battle_dash` | `rare` | 178 | 18 | 11 | 10 |
| 蓄え | `control_reserve` | `rare` | 177 | 0 | 0 | 0 |
| 踏ん張り | `battle_brace` | `uncommon` | 116 | 10 | 3 | 1 |
| 返し刃 | `battle_counter` | `uncommon` | 109 | 6 | 5 | 4 |
| フェイント | `battle_feint` | `uncommon` | 43 | 4 | 1 | 1 |
| 受け流し | `battle_guard` | `uncommon` | 30 | 5 | 2 | 2 |
| 退き足 | `battle_backstep` | `uncommon` | 10 | 0 | 0 | 0 |
| 牽制 | `control_disrupt` | `common` | 6 | 0 | 0 | 0 |
| 構え | `control_guard` | `common` | 4 | 0 | 0 | 0 |
| 圧迫 | `control_pressure` | `common` | 3 | 1 | 0 | 0 |
| 強撃 | `battle_power_attack` | `uncommon` | 1 | 0 | 0 | 0 |
| 集中 | `control_focus` | `common` | 1 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 14 | 1 | 7.1% | 0 | 0.0% | 0 |
| `uncommon` | 2682 | 101 | 3.8% | 46 | 45.5% | 39 |
| `rare` | 1304 | 183 | 14.0% | 68 | 37.2% | 65 |

#### Match Logs

- [draft_match_0001](matches/match_0001_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0002](matches/match_0002_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0003](matches/match_0003_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0004](matches/match_0004_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0005](matches/match_0005_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0006](matches/match_0006_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0007](matches/match_0007_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0008](matches/match_0008_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0009](matches/match_0009_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0010](matches/match_0010_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0011](matches/match_0011_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0012](matches/match_0012_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0013](matches/match_0013_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0014](matches/match_0014_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0015](matches/match_0015_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0016](matches/match_0016_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0017](matches/match_0017_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0018](matches/match_0018_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0019](matches/match_0019_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0020](matches/match_0020_RandomDraftBot_vs_RoleBalanceDraftBot.md)
