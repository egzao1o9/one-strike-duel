# Draft Role Balance Report

## Configuration

- Draft Bot 1: `RoleBalanceDraftBot`
- Draft Bot 2: `RandomDraftBot`
- Play Bot 1: `GreedyBot`
- Play Bot 2: `GreedyBot`
- Rounds: 100
- Total Matches: 200
- Seed: 261
- Pool: `base_pool` (59 copies)
- Pairing Mode: mirrored seats per round

## Drafter Summary

| Drafter | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Winner Set Avg | Loser Set Avg | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate | Battle Avg | Control Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `RandomDraftBot` | 200 | 139 | 46 | 15 | 69.5% | 37.3% | 2.9% | 55.4% | 41.7% | 1.63 | 1.17 | 73.3% | 65.3% | 34.6% | 55.5% | 9.9% | 10.79 | 9.21 | 6.16 | 2.95 | 1.68 | 9.21 | 11.74 | 7.83 | 0.42 |
| `RoleBalanceDraftBot` | 200 | 46 | 139 | 15 | 23.0% | 10.5% | 6.5% | 43.5% | 50.0% | 1.61 | 1.24 | 28.4% | 18.1% | 26.4% | 66.6% | 7.0% | 12 | 8 | 6.01 | 3.05 | 2.94 | 8 | 0.58 | 13.85 | 5.58 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| RandomDraftBot vs RoleBalanceDraftBot | 200 | 15 | `RandomDraftBot`=139, `RoleBalanceDraftBot`=46 | 1.16 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 圧迫 | 93 |
| 2 | 粉砕 | 89 |
| 3 | 大振り | 73 |
| 4 | 返し刃 | 55 |
| 5 | 踏み込み | 54 |
| 6 | 押し込み | 52 |
| 7 | 崩し | 51 |
| 8 | 低姿勢 | 43 |
| 9 | 渾身 | 40 |
| 10 | 貫き | 38 |
| 11 | 踏ん張り | 34 |
| 12 | 十字受け | 31 |
| 13 | 受け流し | 30 |
| 14 | フェイント | 28 |
| 15 | 疾走 | 27 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 圧迫 | 63 |
| 2 | 返し刃 | 47 |
| 3 | 押し込み | 44 |
| 4 | 崩し | 39 |
| 5 | 踏み込み | 36 |
| 6 | 貫き | 28 |
| 7 | 踏ん張り | 26 |
| 8 | 低姿勢 | 26 |
| 9 | 粉砕 | 25 |
| 10 | 十字受け | 20 |
| 11 | 受け流し | 17 |
| 12 | 疾走 | 16 |
| 13 | フェイント | 13 |
| 14 | 大振り | 10 |
| 15 | 退き足 | 10 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 43 |
| 2 | 押し込み | 41 |
| 3 | 崩し | 36 |
| 4 | 踏み込み | 36 |
| 5 | 貫き | 25 |
| 6 | 粉砕 | 25 |
| 7 | 踏ん張り | 21 |
| 8 | 低姿勢 | 16 |
| 9 | 十字受け | 12 |
| 10 | 疾走 | 12 |
| 11 | 受け流し | 10 |
| 12 | 大振り | 9 |
| 13 | 渾身 | 5 |
| 14 | フェイント | 4 |
| 15 | 退き足 | 4 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `RandomDraftBot` | 2.22 | 1.08 | 1.09 | 1.43 | 0.91 | 1.02 | 19 (9.5%) | 12 (8.6%) |
| `RoleBalanceDraftBot` | 3.78 | 0.15 | -0.15 | 3.95 | 0.06 | -0.51 | 12 (6.0%) | 19 (41.3%) |

## Drafter Details

### RandomDraftBot

- Win Rate: 69.5%
- Draw Rate: 7.5%
- First Pass Win Rate: 37.3%
- Win With Fewer Cards: 2.9%
- Win With Same Cards: 55.4%
- Win With More Cards: 41.7%
- Winner Facedown Avg: 1.63
- Loser Facedown Avg: 1.17
- Starting Player Win Rate: 73.3%
- Responding Player Win Rate: 65.3%
- Final Stats Avg: A=2.22, B=1.08, S=1.09
- Losing Final Stats Avg: A=1.43, B=0.91, S=1.02
- Lost With Speed Advantage: 19 (9.5%)
- Won After Blocking Faster Attack: 12 (8.6%)
- Action Rates: set=34.6%, set_pass=55.5%, pass=9.9%
- Turns: min=1, avg=1.16, max=4
- Battle / Control: avg=10.79 / 9.21
- Role Colors: red=6.16, blue=2.95, green=1.68, white=9.21
- Rarities: common=11.74, uncommon=7.83, rare=0.42

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏ん張り | 277 |
| 2 | 圧迫 | 268 |
| 3 | 返し刃 | 268 |
| 4 | 構え | 267 |
| 5 | 押し込み | 266 |
| 6 | 牽制 | 256 |
| 7 | 集中 | 255 |
| 8 | 十字受け | 250 |
| 9 | 受け流し | 242 |
| 10 | 退き足 | 166 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 203 |
| 2 | 押し込み | 192 |
| 3 | 構え | 191 |
| 4 | 圧迫 | 188 |
| 5 | 踏ん張り | 187 |
| 6 | 十字受け | 175 |
| 7 | 集中 | 174 |
| 8 | 牽制 | 171 |
| 9 | 受け流し | 166 |
| 10 | 退き足 | 114 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 踏ん張り | `battle_brace` | `common` | 277 | 34 | 26 | 21 |
| 圧迫 | `control_pressure` | `common` | 268 | 87 | 61 | 0 |
| 返し刃 | `battle_counter` | `common` | 268 | 55 | 47 | 43 |
| 構え | `control_guard` | `common` | 267 | 0 | 0 | 0 |
| 押し込み | `battle_press` | `common` | 266 | 52 | 44 | 41 |
| 牽制 | `control_disrupt` | `common` | 256 | 0 | 0 | 0 |
| 集中 | `control_focus` | `common` | 255 | 0 | 0 | 0 |
| 十字受け | `battle_cross_guard` | `common` | 250 | 31 | 20 | 12 |
| 受け流し | `battle_guard` | `common` | 242 | 25 | 15 | 9 |
| 退き足 | `battle_backstep` | `uncommon` | 166 | 18 | 10 | 4 |
| 粉砕 | `battle_crush` | `uncommon` | 143 | 49 | 23 | 23 |
| 勢い溜め | `control_momentum` | `uncommon` | 141 | 0 | 0 | 0 |
| フェイント | `battle_feint` | `uncommon` | 139 | 17 | 9 | 4 |
| 重心落とし | `control_anchor` | `uncommon` | 136 | 0 | 0 | 0 |
| 補強 | `control_fortify` | `uncommon` | 133 | 0 | 0 | 0 |
| 加速 | `control_haste` | `uncommon` | 132 | 0 | 0 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 119 | 0 | 0 | 0 |
| 崩し | `battle_break` | `uncommon` | 102 | 32 | 28 | 27 |
| 受け直し | `control_cover` | `uncommon` | 101 | 0 | 0 | 0 |
| 貫き | `battle_pierce` | `uncommon` | 88 | 20 | 17 | 16 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 86 | 7 | 7 | 5 |
| 踏み込み | `battle_step_in` | `uncommon` | 80 | 20 | 19 | 19 |
| 蓄え | `control_reserve` | `rare` | 34 | 0 | 0 | 0 |
| 疾走 | `battle_dash` | `rare` | 22 | 3 | 3 | 2 |
| 残像 | `battle_afterimage` | `rare` | 13 | 0 | 0 | 0 |
| 鉄壁 | `battle_wall` | `rare` | 8 | 1 | 0 | 0 |
| 渾身 | `battle_all_in` | `rare` | 5 | 1 | 0 | 0 |
| 大振り | `battle_heavy_swing` | `rare` | 3 | 1 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 2349 | 284 | 12.1% | 213 | 75.0% | 126 |
| `uncommon` | 1566 | 163 | 10.4% | 113 | 69.3% | 98 |
| `rare` | 85 | 6 | 7.1% | 3 | 50.0% | 2 |

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

- Win Rate: 23.0%
- Draw Rate: 7.5%
- First Pass Win Rate: 10.5%
- Win With Fewer Cards: 6.5%
- Win With Same Cards: 43.5%
- Win With More Cards: 50.0%
- Winner Facedown Avg: 1.61
- Loser Facedown Avg: 1.24
- Starting Player Win Rate: 28.4%
- Responding Player Win Rate: 18.1%
- Final Stats Avg: A=3.78, B=0.15, S=-0.15
- Losing Final Stats Avg: A=3.95, B=0.06, S=-0.51
- Lost With Speed Advantage: 12 (6.0%)
- Won After Blocking Faster Attack: 19 (41.3%)
- Action Rates: set=26.4%, set_pass=66.6%, pass=7.0%
- Turns: min=1, avg=1.16, max=4
- Battle / Control: avg=12 / 8
- Role Colors: red=6.01, blue=3.05, green=2.94, white=8
- Rarities: common=0.58, uncommon=13.85, rare=5.58

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 低姿勢 | 314 |
| 2 | 受け直し | 289 |
| 3 | 前のめり | 270 |
| 4 | 踏み込み | 232 |
| 5 | 加速 | 220 |
| 6 | 補強 | 216 |
| 7 | 重心落とし | 206 |
| 8 | 勢い溜め | 199 |
| 9 | 崩し | 198 |
| 10 | 貫き | 198 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 低姿勢 | 76 |
| 2 | 受け直し | 66 |
| 3 | 前のめり | 56 |
| 4 | 踏み込み | 54 |
| 5 | 勢い溜め | 51 |
| 6 | 補強 | 50 |
| 7 | 貫き | 49 |
| 8 | 加速 | 49 |
| 9 | 重心落とし | 48 |
| 10 | 渾身 | 46 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 低姿勢 | `battle_low_stance` | `uncommon` | 314 | 36 | 19 | 11 |
| 受け直し | `control_cover` | `uncommon` | 289 | 0 | 0 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 270 | 0 | 0 | 0 |
| 踏み込み | `battle_step_in` | `uncommon` | 232 | 34 | 17 | 17 |
| 加速 | `control_haste` | `uncommon` | 220 | 0 | 0 | 0 |
| 補強 | `control_fortify` | `uncommon` | 216 | 0 | 0 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 206 | 0 | 0 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 199 | 0 | 0 | 0 |
| 崩し | `battle_break` | `uncommon` | 198 | 19 | 11 | 9 |
| 貫き | `battle_pierce` | `uncommon` | 198 | 18 | 11 | 9 |
| 大振り | `battle_heavy_swing` | `rare` | 197 | 72 | 10 | 9 |
| 渾身 | `battle_all_in` | `rare` | 195 | 39 | 5 | 5 |
| 鉄壁 | `battle_wall` | `rare` | 192 | 13 | 5 | 1 |
| 残像 | `battle_afterimage` | `rare` | 187 | 18 | 4 | 0 |
| フェイント | `battle_feint` | `uncommon` | 185 | 11 | 4 | 0 |
| 粉砕 | `battle_crush` | `uncommon` | 182 | 40 | 2 | 2 |
| 疾走 | `battle_dash` | `rare` | 178 | 24 | 13 | 10 |
| 蓄え | `control_reserve` | `rare` | 166 | 0 | 0 | 0 |
| 受け流し | `battle_guard` | `common` | 82 | 5 | 2 | 1 |
| 退き足 | `battle_backstep` | `uncommon` | 60 | 4 | 0 | 0 |
| 牽制 | `control_disrupt` | `common` | 11 | 0 | 0 | 0 |
| 構え | `control_guard` | `common` | 10 | 0 | 0 | 0 |
| 圧迫 | `control_pressure` | `common` | 9 | 6 | 2 | 0 |
| 集中 | `control_focus` | `common` | 4 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 116 | 11 | 9.5% | 4 | 36.4% | 1 |
| `uncommon` | 2769 | 162 | 5.9% | 64 | 39.5% | 48 |
| `rare` | 1115 | 166 | 14.9% | 37 | 22.3% | 25 |

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
