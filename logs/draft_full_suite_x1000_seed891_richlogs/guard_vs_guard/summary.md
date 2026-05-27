# Draft Report

## Configuration

- Draft Bot 1: `GuardDraftBot`
- Draft Bot 2: `GuardDraftBot`
- Play Bot 1: `GuardBot`
- Play Bot 2: `GuardBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 6891
- Pool: `base_pool` (95 copies)
- Pairing Mode: mirrored seats per round
- Draft Mode: `full`
- Fast Report: on
- Lean Draft Logging: on
- Save Battle Logs: on
- Draft Flow: normal public pack + normal hidden pack, then public rare + hidden rare, with order swapped in second half

## Drafter Summary

| Drafter | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Winner Set Avg | Loser Set Avg | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate | Battle Avg | Control Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `GuardDraftBot` | 2000 | 930 | 930 | 140 | 46.5% | 37.1% | 21.6% | 36.8% | 41.6% | 2.96 | 2.76 | 46.0% | 47.0% | 71.0% | 1.9% | 27.1% | 13.87 | 6.13 | 6.94 | 3.44 | 3.49 | 6.13 | 8 | 8 | 4 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| GuardDraftBot vs GuardDraftBot | 1000 | 70 | `GuardDraftBot`=930 | 1.53 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 防御 | 624 |
| 2 | 圧迫 | 598 |
| 3 | 踏み込み | 569 |
| 4 | 牽制 | 556 |
| 5 | 攻撃 | 556 |
| 6 | ステップ | 487 |
| 7 | 鉄壁 | 420 |
| 8 | 渾身 | 416 |
| 9 | 貫き | 398 |
| 10 | 崩し | 383 |
| 11 | 大振り | 366 |
| 12 | 十字受け | 345 |
| 13 | 踏ん張り | 342 |
| 14 | 返し刃 | 341 |
| 15 | 構え | 322 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 371 |
| 2 | 牽制 | 270 |
| 3 | 攻撃 | 258 |
| 4 | 圧迫 | 255 |
| 5 | 防御 | 254 |
| 6 | 貫き | 233 |
| 7 | 崩し | 230 |
| 8 | 鉄壁 | 182 |
| 9 | 残像 | 174 |
| 10 | ステップ | 172 |
| 11 | 返し刃 | 171 |
| 12 | 渾身 | 162 |
| 13 | 大振り | 157 |
| 14 | 構え | 154 |
| 15 | 踏ん張り | 154 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 356 |
| 2 | 貫き | 206 |
| 3 | 崩し | 206 |
| 4 | 攻撃 | 182 |
| 5 | 防御 | 155 |
| 6 | 渾身 | 150 |
| 7 | 大振り | 147 |
| 8 | 残像 | 135 |
| 9 | 返し刃 | 133 |
| 10 | 粉砕 | 120 |
| 11 | 踏ん張り | 107 |
| 12 | ステップ | 103 |
| 13 | 十字受け | 88 |
| 14 | 疾走 | 88 |
| 15 | 押し込み | 82 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `GuardDraftBot` | 4.03 | 0.88 | 1.66 | 3.25 | 0.98 | 1.19 | 259 (13.0%) | 259 (27.8%) |

## Drafter Details

### GuardDraftBot

- Win Rate: 46.5%
- Draw Rate: 7.0%
- First Pass Win Rate: 37.1%
- Win With Fewer Cards: 21.6%
- Win With Same Cards: 36.8%
- Win With More Cards: 41.6%
- Winner Facedown Avg: 2.96
- Loser Facedown Avg: 2.76
- Starting Player Win Rate: 46.0%
- Responding Player Win Rate: 47.0%
- Final Stats Avg: A=4.03, B=0.88, S=1.66
- Losing Final Stats Avg: A=3.25, B=0.98, S=1.19
- Lost With Speed Advantage: 259 (13.0%)
- Won After Blocking Faster Attack: 259 (27.8%)
- Action Rates: set=71.0%, set_pass=1.9%, pass=27.1%
- set_pass Candidate Avg / Match: 15.96
- Turns: min=1, avg=1.53, max=4
- Battle / Control: avg=13.87 / 6.13
- Role Colors: red=6.94, blue=3.44, green=3.49, white=6.13
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 防御 | 2493 |
| 2 | 攻撃 | 2450 |
| 3 | 圧迫 | 2416 |
| 4 | ステップ | 2323 |
| 5 | 構え | 2193 |
| 6 | 集中 | 2089 |
| 7 | 牽制 | 2036 |
| 8 | 踏み込み | 1598 |
| 9 | 渾身 | 1356 |
| 10 | 貫き | 1327 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 1167 |
| 2 | 防御 | 1141 |
| 3 | 圧迫 | 1105 |
| 4 | ステップ | 1051 |
| 5 | 構え | 1015 |
| 6 | 集中 | 994 |
| 7 | 牽制 | 967 |
| 8 | 踏み込み | 823 |
| 9 | 貫き | 666 |
| 10 | 崩し | 641 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 防御 | `battle_defend` | `common` | 2493 | 624 | 254 | 155 |
| 攻撃 | `battle_attack` | `common` | 2450 | 556 | 258 | 182 |
| 圧迫 | `control_pressure` | `common` | 2416 | 598 | 255 | 0 |
| ステップ | `battle_step` | `common` | 2323 | 487 | 172 | 103 |
| 構え | `control_guard` | `common` | 2193 | 322 | 154 | 0 |
| 集中 | `control_focus` | `common` | 2089 | 209 | 91 | 0 |
| 牽制 | `control_disrupt` | `common` | 2036 | 556 | 270 | 0 |
| 踏み込み | `battle_step_in` | `rare` | 1598 | 569 | 371 | 356 |
| 渾身 | `battle_all_in` | `rare` | 1356 | 416 | 162 | 150 |
| 貫き | `battle_pierce` | `uncommon` | 1327 | 398 | 233 | 206 |
| 崩し | `battle_break` | `uncommon` | 1314 | 383 | 230 | 206 |
| 鉄壁 | `battle_wall` | `rare` | 1265 | 420 | 182 | 66 |
| 返し刃 | `battle_counter` | `uncommon` | 1101 | 341 | 171 | 133 |
| 大振り | `battle_heavy_swing` | `rare` | 1088 | 366 | 157 | 147 |
| 十字受け | `battle_cross_guard` | `uncommon` | 1077 | 345 | 142 | 88 |
| 踏ん張り | `battle_brace` | `uncommon` | 1064 | 342 | 154 | 107 |
| 粉砕 | `battle_crush` | `uncommon` | 988 | 255 | 131 | 120 |
| 残像 | `battle_afterimage` | `rare` | 961 | 316 | 174 | 135 |
| Bastion | `battle_bastion` | `uncommon` | 941 | 302 | 120 | 54 |
| 退き足 | `battle_backstep` | `uncommon` | 861 | 249 | 97 | 63 |
| Bulwark | `battle_bulwark` | `uncommon` | 816 | 260 | 120 | 67 |
| 押し込み | `battle_press` | `uncommon` | 813 | 226 | 109 | 82 |
| 強撃 | `battle_power_attack` | `uncommon` | 775 | 197 | 90 | 76 |
| フェイント | `battle_feint` | `uncommon` | 766 | 204 | 92 | 60 |
| 受け流し | `battle_guard` | `uncommon` | 744 | 225 | 105 | 65 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 724 | 226 | 90 | 43 |
| 疾走 | `battle_dash` | `rare` | 644 | 198 | 104 | 88 |
| 受け直し | `control_cover` | `uncommon` | 535 | 129 | 58 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 475 | 91 | 45 | 0 |
| 蓄え | `control_reserve` | `rare` | 422 | 113 | 36 | 0 |
| Crush Spirit | `control_crush_spirit` | `rare` | 420 | 146 | 78 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 397 | 77 | 32 | 0 |
| 補強 | `control_fortify` | `uncommon` | 373 | 68 | 31 | 0 |
| Blank First | `control_blank_first` | `uncommon` | 308 | 87 | 42 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 301 | 46 | 22 | 0 |
| 加速 | `control_haste` | `uncommon` | 300 | 51 | 23 | 0 |
| Tripwire | `battle_tripwire` | `rare` | 246 | 4 | 3 | 3 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 16000 | 3352 | 20.9% | 1454 | 43.4% | 440 |
| `uncommon` | 16000 | 4502 | 28.1% | 2137 | 47.5% | 1370 |
| `rare` | 8000 | 2548 | 31.9% | 1267 | 49.7% | 945 |

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
