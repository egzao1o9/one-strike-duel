# Draft Report

## Configuration

- Draft Bot 1: `StandardDraftBot`
- Draft Bot 2: `AggroDraftBot`
- Play Bot 1: `StandardBot`
- Play Bot 2: `StandardBot`
- Rounds: 50
- Total Matches: 100
- Seed: 421
- Pool: `base_pool` (64 copies)
- Pairing Mode: mirrored seats per round
- Draft Flow: hidden 3->1, then public 5 with reverse-order picks

## Drafter Summary

| Drafter | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Winner Set Avg | Loser Set Avg | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate | Battle Avg | Control Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `AggroDraftBot` | 100 | 41 | 48 | 11 | 41.0% | 38.5% | 46.3% | 2.4% | 51.2% | 1.51 | 1.44 | 38.5% | 43.8% | 32.9% | 34.1% | 32.9% | 13.83 | 6.17 | 7.65 | 3.63 | 2.55 | 6.17 | 2.24 | 14.5 | 3.26 |
| `StandardDraftBot` | 100 | 48 | 41 | 11 | 48.0% | 43.8% | 43.8% | 0.0% | 56.2% | 1.56 | 1.46 | 43.8% | 51.9% | 33.3% | 33.3% | 33.3% | 13.77 | 6.23 | 7.82 | 3.57 | 2.38 | 6.23 | 2.3 | 14.53 | 3.17 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| AggroDraftBot vs StandardDraftBot | 100 | 11 | `AggroDraftBot`=41, `StandardDraftBot`=48 | 1.1 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 粉砕 | 59 |
| 2 | 踏み込み | 42 |
| 3 | 返し刃 | 42 |
| 4 | 前のめり | 39 |
| 5 | 渾身 | 37 |
| 6 | 大振り | 37 |
| 7 | 圧迫 | 33 |
| 8 | 十字受け | 25 |
| 9 | 蓄え | 25 |
| 10 | 強撃 | 22 |
| 11 | 受け直し | 21 |
| 12 | 疾走 | 15 |
| 13 | 加速 | 14 |
| 14 | 勢い溜め | 13 |
| 15 | 重心落とし | 11 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 32 |
| 2 | 前のめり | 20 |
| 3 | 返し刃 | 18 |
| 4 | 粉砕 | 17 |
| 5 | 受け直し | 17 |
| 6 | 十字受け | 16 |
| 7 | 渾身 | 14 |
| 8 | 圧迫 | 13 |
| 9 | 疾走 | 10 |
| 10 | 加速 | 9 |
| 11 | 重心落とし | 9 |
| 12 | 強撃 | 7 |
| 13 | 押し込み | 7 |
| 14 | 大振り | 7 |
| 15 | 鉄壁 | 7 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 30 |
| 2 | 粉砕 | 16 |
| 3 | 十字受け | 16 |
| 4 | 返し刃 | 15 |
| 5 | 渾身 | 14 |
| 6 | 疾走 | 10 |
| 7 | 強撃 | 7 |
| 8 | 押し込み | 7 |
| 9 | 大振り | 6 |
| 10 | 残像 | 4 |
| 11 | 踏ん張り | 4 |
| 12 | 鉄壁 | 3 |
| 13 | 貫き | 3 |
| 14 | 崩し | 2 |
| 15 | 前のめり | 0 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `AggroDraftBot` | 4.15 | 0.43 | 0.82 | 4.17 | 0.35 | 0.15 | 9 (9.0%) | 4 (9.8%) |
| `StandardDraftBot` | 4.17 | 0.56 | 0.82 | 4.83 | 0.32 | -0.44 | 4 (4.0%) | 9 (18.8%) |

## Drafter Details

### AggroDraftBot

- Win Rate: 41.0%
- Draw Rate: 11.0%
- First Pass Win Rate: 38.5%
- Win With Fewer Cards: 46.3%
- Win With Same Cards: 2.4%
- Win With More Cards: 51.2%
- Winner Facedown Avg: 1.51
- Loser Facedown Avg: 1.44
- Starting Player Win Rate: 38.5%
- Responding Player Win Rate: 43.8%
- Final Stats Avg: A=4.15, B=0.43, S=0.82
- Losing Final Stats Avg: A=4.17, B=0.35, S=0.15
- Lost With Speed Advantage: 9 (9.0%)
- Won After Blocking Faster Attack: 4 (9.8%)
- Action Rates: set=32.9%, set_pass=34.1%, pass=32.9%
- Turns: min=1, avg=1.1, max=2
- Battle / Control: avg=13.83 / 6.17
- Role Colors: red=7.65, blue=3.63, green=2.55, white=6.17
- Rarities: common=2.24, uncommon=14.5, rare=3.26

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 受け直し | 99 |
| 2 | 十字受け | 96 |
| 3 | 返し刃 | 96 |
| 4 | 粉砕 | 90 |
| 5 | 強撃 | 87 |
| 6 | 受け流し | 86 |
| 7 | 踏ん張り | 82 |
| 8 | 貫き | 82 |
| 9 | 崩し | 80 |
| 10 | 退き足 | 80 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 十字受け | 42 |
| 2 | 受け直し | 41 |
| 3 | 返し刃 | 39 |
| 4 | 強撃 | 38 |
| 5 | 貫き | 35 |
| 6 | 踏ん張り | 34 |
| 7 | 崩し | 34 |
| 8 | 押し込み | 33 |
| 9 | 受け流し | 33 |
| 10 | フェイント | 32 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 受け直し | `control_cover` | `uncommon` | 99 | 10 | 9 | 0 |
| 返し刃 | `battle_counter` | `uncommon` | 96 | 22 | 9 | 8 |
| 十字受け | `battle_cross_guard` | `uncommon` | 96 | 16 | 9 | 9 |
| 粉砕 | `battle_crush` | `uncommon` | 90 | 31 | 8 | 7 |
| 強撃 | `battle_power_attack` | `uncommon` | 87 | 12 | 3 | 3 |
| 受け流し | `battle_guard` | `uncommon` | 86 | 0 | 0 | 0 |
| 踏ん張り | `battle_brace` | `uncommon` | 82 | 4 | 3 | 2 |
| 貫き | `battle_pierce` | `uncommon` | 82 | 4 | 1 | 1 |
| 崩し | `battle_break` | `uncommon` | 80 | 1 | 1 | 1 |
| 退き足 | `battle_backstep` | `uncommon` | 80 | 0 | 0 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 78 | 16 | 7 | 0 |
| 押し込み | `battle_press` | `uncommon` | 78 | 2 | 2 | 2 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 78 | 0 | 0 | 0 |
| フェイント | `battle_feint` | `uncommon` | 76 | 0 | 0 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 73 | 5 | 3 | 0 |
| 補強 | `control_fortify` | `uncommon` | 65 | 8 | 2 | 0 |
| 加速 | `control_haste` | `uncommon` | 64 | 5 | 3 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 60 | 8 | 4 | 0 |
| 圧迫 | `control_pressure` | `common` | 52 | 14 | 6 | 0 |
| 鉄壁 | `battle_wall` | `rare` | 50 | 5 | 1 | 0 |
| 残像 | `battle_afterimage` | `rare` | 50 | 4 | 1 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 49 | 23 | 15 | 15 |
| 疾走 | `battle_dash` | `rare` | 46 | 5 | 4 | 4 |
| 渾身 | `battle_all_in` | `rare` | 45 | 20 | 8 | 8 |
| 蓄え | `control_reserve` | `rare` | 44 | 13 | 4 | 0 |
| 大振り | `battle_heavy_swing` | `rare` | 42 | 15 | 2 | 2 |
| 構え | `control_guard` | `common` | 41 | 0 | 0 | 0 |
| 防御 | `battle_defend` | `common` | 41 | 0 | 0 | 0 |
| 攻撃 | `battle_attack` | `common` | 34 | 0 | 0 | 0 |
| 牽制 | `control_disrupt` | `common` | 25 | 2 | 1 | 0 |
| 集中 | `control_focus` | `common` | 16 | 0 | 0 | 0 |
| ステップ | `battle_step` | `common` | 15 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 224 | 16 | 7.1% | 7 | 43.8% | 0 |
| `uncommon` | 1450 | 144 | 9.9% | 64 | 44.4% | 33 |
| `rare` | 326 | 85 | 26.1% | 35 | 41.2% | 29 |

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

- Win Rate: 48.0%
- Draw Rate: 11.0%
- First Pass Win Rate: 43.8%
- Win With Fewer Cards: 43.8%
- Win With Same Cards: 0.0%
- Win With More Cards: 56.2%
- Winner Facedown Avg: 1.56
- Loser Facedown Avg: 1.46
- Starting Player Win Rate: 43.8%
- Responding Player Win Rate: 51.9%
- Final Stats Avg: A=4.17, B=0.56, S=0.82
- Losing Final Stats Avg: A=4.83, B=0.32, S=-0.44
- Lost With Speed Advantage: 4 (4.0%)
- Won After Blocking Faster Attack: 9 (18.8%)
- Action Rates: set=33.3%, set_pass=33.3%, pass=33.3%
- Turns: min=1, avg=1.1, max=2
- Battle / Control: avg=13.77 / 6.23
- Role Colors: red=7.82, blue=3.57, green=2.38, white=6.23
- Rarities: common=2.3, uncommon=14.53, rare=3.17

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 貫き | 97 |
| 2 | 踏ん張り | 96 |
| 3 | 崩し | 93 |
| 4 | 強撃 | 89 |
| 5 | フェイント | 88 |
| 6 | 十字受け | 87 |
| 7 | 退き足 | 86 |
| 8 | 返し刃 | 86 |
| 9 | 粉砕 | 84 |
| 10 | 重心落とし | 83 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 貫き | 49 |
| 2 | 強撃 | 46 |
| 3 | フェイント | 45 |
| 4 | 十字受け | 44 |
| 5 | 崩し | 44 |
| 6 | 踏ん張り | 43 |
| 7 | 返し刃 | 42 |
| 8 | 受け流し | 40 |
| 9 | 粉砕 | 38 |
| 10 | 退き足 | 37 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 貫き | `battle_pierce` | `uncommon` | 97 | 3 | 2 | 2 |
| 踏ん張り | `battle_brace` | `uncommon` | 96 | 7 | 3 | 2 |
| 崩し | `battle_break` | `uncommon` | 93 | 2 | 1 | 1 |
| 強撃 | `battle_power_attack` | `uncommon` | 89 | 10 | 4 | 4 |
| フェイント | `battle_feint` | `uncommon` | 88 | 0 | 0 | 0 |
| 十字受け | `battle_cross_guard` | `uncommon` | 87 | 9 | 7 | 7 |
| 返し刃 | `battle_counter` | `uncommon` | 86 | 20 | 9 | 7 |
| 退き足 | `battle_backstep` | `uncommon` | 86 | 0 | 0 | 0 |
| 粉砕 | `battle_crush` | `uncommon` | 84 | 28 | 9 | 9 |
| 重心落とし | `control_anchor` | `uncommon` | 83 | 6 | 6 | 0 |
| 受け流し | `battle_guard` | `uncommon` | 81 | 0 | 0 | 0 |
| 圧迫 | `control_pressure` | `common` | 79 | 19 | 7 | 0 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 78 | 0 | 0 | 0 |
| 押し込み | `battle_press` | `uncommon` | 75 | 5 | 5 | 5 |
| 前のめり | `control_overclock` | `uncommon` | 74 | 23 | 13 | 0 |
| 加速 | `control_haste` | `uncommon` | 68 | 9 | 6 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 65 | 5 | 1 | 0 |
| 受け直し | `control_cover` | `uncommon` | 64 | 11 | 8 | 0 |
| 補強 | `control_fortify` | `uncommon` | 59 | 3 | 2 | 0 |
| 大振り | `battle_heavy_swing` | `rare` | 50 | 22 | 5 | 4 |
| 渾身 | `battle_all_in` | `rare` | 50 | 17 | 6 | 6 |
| 鉄壁 | `battle_wall` | `rare` | 46 | 6 | 6 | 3 |
| 構え | `control_guard` | `common` | 46 | 1 | 0 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 45 | 19 | 17 | 15 |
| 疾走 | `battle_dash` | `rare` | 45 | 10 | 6 | 6 |
| 残像 | `battle_afterimage` | `rare` | 42 | 7 | 5 | 4 |
| 蓄え | `control_reserve` | `rare` | 39 | 12 | 3 | 0 |
| 防御 | `battle_defend` | `common` | 33 | 0 | 0 | 0 |
| 集中 | `control_focus` | `common` | 25 | 3 | 1 | 0 |
| 牽制 | `control_disrupt` | `common` | 21 | 3 | 2 | 0 |
| 攻撃 | `battle_attack` | `common` | 17 | 0 | 0 | 0 |
| ステップ | `battle_step` | `common` | 9 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 230 | 26 | 11.3% | 10 | 38.5% | 0 |
| `uncommon` | 1453 | 141 | 9.7% | 76 | 53.9% | 37 |
| `rare` | 317 | 93 | 29.3% | 48 | 51.6% | 38 |

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
