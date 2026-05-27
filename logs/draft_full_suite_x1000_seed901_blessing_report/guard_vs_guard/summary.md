# Draft Report

## Configuration

- Draft Bot 1: `GuardDraftBot`
- Draft Bot 2: `GuardDraftBot`
- Play Bot 1: `GuardBot`
- Play Bot 2: `GuardBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 6901
- Pool: `base_pool` (115 copies)
- Pairing Mode: mirrored seats per round
- Draft Mode: `full`
- Fast Report: on
- Lean Draft Logging: on
- Save Battle Logs: on
- Draft Flow: normal public pack + normal hidden pack, then public rare + hidden rare, with order swapped in second half

## Drafter Summary

| Drafter | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Winner Set Avg | Loser Set Avg | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate | Battle Avg | Control Avg | Blessing Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `GuardDraftBot` | 2000 | 936 | 936 | 128 | 46.8% | 41.5% | 16.7% | 52.2% | 31.1% | 3.22 | 3.08 | 45.6% | 48.0% | 72.2% | 1.7% | 26.0% | 12.92 | 6.12 | 0.95 | 6.47 | 3.75 | 3.57 | 6.21 | 8 | 8 | 4 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| GuardDraftBot vs GuardDraftBot | 1000 | 64 | `GuardDraftBot`=936 | 1.8 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 圧迫 | 881 |
| 2 | 防御 | 789 |
| 3 | 牽制 | 679 |
| 4 | 攻撃 | 651 |
| 5 | 構え | 636 |
| 6 | 集中 | 544 |
| 7 | ステップ | 537 |
| 8 | 崩し | 438 |
| 9 | 貫き | 435 |
| 10 | Bastion | 414 |
| 11 | 十字受け | 414 |
| 12 | 踏ん張り | 411 |
| 13 | 返し刃 | 407 |
| 14 | 退き足 | 332 |
| 15 | Bulwark | 331 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 圧迫 | 373 |
| 2 | 牽制 | 345 |
| 3 | 防御 | 343 |
| 4 | 構え | 289 |
| 5 | 攻撃 | 287 |
| 6 | 崩し | 279 |
| 7 | 貫き | 265 |
| 8 | 踏み込み | 232 |
| 9 | 集中 | 227 |
| 10 | ステップ | 215 |
| 11 | 踏ん張り | 208 |
| 12 | 返し刃 | 186 |
| 13 | Bastion | 185 |
| 14 | 十字受け | 182 |
| 15 | 粉砕 | 161 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 崩し | 241 |
| 2 | 貫き | 234 |
| 3 | 踏み込み | 213 |
| 4 | 攻撃 | 202 |
| 5 | 防御 | 162 |
| 6 | 粉砕 | 144 |
| 7 | 返し刃 | 125 |
| 8 | 大振り | 124 |
| 9 | ステップ | 120 |
| 10 | 渾身 | 114 |
| 11 | 強撃 | 107 |
| 12 | 踏ん張り | 99 |
| 13 | 疾走 | 97 |
| 14 | 十字受け | 96 |
| 15 | 構え | 82 |

### Blessing Involvement Overall

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 罠糸の加護 | `blessing_trap_web` | 217 | 49.3% | 217 | 80 | 80 | 12 | 12 | 0 | 0 |
| 速の加護 | `blessing_speed` | 217 | 46.5% | 220 | 66 | 66 | 0 | 0 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 196 | 43.9% | 199 | 43 | 43 | 43 | 0 | 0 | 43 |
| 防の加護 | `blessing_guard` | 193 | 50.8% | 194 | 50 | 50 | 0 | 0 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 189 | 50.8% | 190 | 44 | 44 | 0 | 0 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 184 | 35.9% | 185 | 31 | 31 | 2 | 2 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 181 | 44.8% | 181 | 57 | 57 | 11 | 11 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 179 | 48.6% | 179 | 37 | 37 | 5 | 5 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 173 | 41.0% | 174 | 57 | 57 | 0 | 0 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 171 | 46.8% | 171 | 49 | 49 | 16 | 16 | 0 | 0 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `GuardDraftBot` | 3.23 | 0.98 | 1.62 | 2.24 | 1.04 | 1.51 | 323 (16.2%) | 323 (34.5%) |

## Drafter Details

### GuardDraftBot

- Win Rate: 46.8%
- Draw Rate: 6.4%
- First Pass Win Rate: 41.5%
- Win With Fewer Cards: 16.7%
- Win With Same Cards: 52.2%
- Win With More Cards: 31.1%
- Winner Facedown Avg: 3.22
- Loser Facedown Avg: 3.08
- Starting Player Win Rate: 45.6%
- Responding Player Win Rate: 48.0%
- Final Stats Avg: A=3.23, B=0.98, S=1.62
- Losing Final Stats Avg: A=2.24, B=1.04, S=1.51
- Lost With Speed Advantage: 323 (16.2%)
- Won After Blocking Faster Attack: 323 (34.5%)
- Action Rates: set=72.2%, set_pass=1.7%, pass=26.0%
- set_pass Candidate Avg / Match: 21.89
- Turns: min=1, avg=1.8, max=29
- Battle / Control / Blessing: avg=12.92 / 6.12 / 0.95
- Role Colors: red=6.47, blue=3.75, green=3.57, white=6.21
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 防御 | 2529 |
| 2 | 攻撃 | 2513 |
| 3 | 圧迫 | 2423 |
| 4 | ステップ | 2337 |
| 5 | 構え | 2153 |
| 6 | 集中 | 2037 |
| 7 | 牽制 | 2008 |
| 8 | 貫き | 1306 |
| 9 | 崩し | 1305 |
| 10 | 返し刃 | 1098 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 1185 |
| 2 | 防御 | 1176 |
| 3 | 圧迫 | 1119 |
| 4 | ステップ | 1064 |
| 5 | 構え | 1008 |
| 6 | 牽制 | 997 |
| 7 | 集中 | 939 |
| 8 | 崩し | 669 |
| 9 | 貫き | 656 |
| 10 | 踏ん張り | 509 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 防御 | `battle_defend` | `common` | 2529 | 789 | 343 | 162 |
| 攻撃 | `battle_attack` | `common` | 2513 | 651 | 287 | 202 |
| 圧迫 | `control_pressure` | `common` | 2423 | 881 | 373 | 77 |
| ステップ | `battle_step` | `common` | 2337 | 537 | 215 | 120 |
| 構え | `control_guard` | `common` | 2153 | 636 | 289 | 82 |
| 集中 | `control_focus` | `common` | 2037 | 544 | 227 | 69 |
| 牽制 | `control_disrupt` | `common` | 2008 | 679 | 345 | 37 |
| 貫き | `battle_pierce` | `uncommon` | 1306 | 435 | 265 | 234 |
| 崩し | `battle_break` | `uncommon` | 1305 | 438 | 279 | 241 |
| 返し刃 | `battle_counter` | `uncommon` | 1098 | 407 | 186 | 125 |
| 踏ん張り | `battle_brace` | `uncommon` | 1080 | 411 | 208 | 99 |
| 十字受け | `battle_cross_guard` | `uncommon` | 1031 | 414 | 182 | 96 |
| 粉砕 | `battle_crush` | `uncommon` | 1011 | 308 | 161 | 144 |
| Bastion | `battle_bastion` | `uncommon` | 974 | 414 | 185 | 51 |
| 踏み込み | `battle_step_in` | `rare` | 896 | 328 | 232 | 213 |
| 押し込み | `battle_press` | `uncommon` | 874 | 288 | 128 | 82 |
| 退き足 | `battle_backstep` | `uncommon` | 859 | 332 | 146 | 68 |
| 強撃 | `battle_power_attack` | `uncommon` | 794 | 248 | 132 | 107 |
| Bulwark | `battle_bulwark` | `uncommon` | 791 | 331 | 156 | 72 |
| 渾身 | `battle_all_in` | `rare` | 787 | 288 | 116 | 114 |
| フェイント | `battle_feint` | `uncommon` | 775 | 248 | 96 | 55 |
| 鉄壁 | `battle_wall` | `rare` | 766 | 309 | 140 | 36 |
| 受け流し | `battle_guard` | `uncommon` | 765 | 272 | 129 | 64 |
| 大振り | `battle_heavy_swing` | `rare` | 733 | 264 | 137 | 124 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 723 | 279 | 109 | 56 |
| 残像 | `battle_afterimage` | `rare` | 716 | 288 | 131 | 71 |
| 疾走 | `battle_dash` | `rare` | 680 | 234 | 133 | 97 |
| 蓄え | `control_reserve` | `rare` | 526 | 202 | 91 | 7 |
| Tripwire | `battle_tripwire` | `rare` | 504 | 5 | 4 | 4 |
| 受け直し | `control_cover` | `uncommon` | 495 | 190 | 92 | 16 |
| Crush Spirit | `control_crush_spirit` | `rare` | 482 | 192 | 105 | 3 |
| 補強 | `control_fortify` | `uncommon` | 407 | 146 | 65 | 16 |
| 前のめり | `control_overclock` | `uncommon` | 406 | 154 | 82 | 20 |
| 重心落とし | `control_anchor` | `uncommon` | 397 | 123 | 56 | 16 |
| 加速 | `control_haste` | `uncommon` | 332 | 113 | 49 | 17 |
| 勢い溜め | `control_momentum` | `uncommon` | 309 | 93 | 37 | 10 |
| Blank First | `control_blank_first` | `uncommon` | 268 | 106 | 50 | 11 |
| 速の加護 | `blessing_speed` | `rare` | 220 | 66 | 27 | 0 |
| 罠糸の加護 | `blessing_trap_web` | `rare` | 217 | 80 | 49 | 0 |
| 見切りの加護 | `blessing_insight` | `rare` | 199 | 43 | 15 | 0 |
| 防の加護 | `blessing_guard` | `rare` | 194 | 50 | 23 | 0 |
| 攻の加護 | `blessing_attack` | `rare` | 190 | 44 | 21 | 0 |
| 抑制の加護 | `blessing_suppression` | `rare` | 185 | 31 | 11 | 0 |
| 防壁の加護 | `blessing_barrier` | `rare` | 181 | 57 | 28 | 0 |
| 鈍足の加護 | `blessing_slow` | `rare` | 179 | 37 | 17 | 0 |
| 知恵の加護 | `blessing_draw` | `rare` | 174 | 57 | 15 | 0 |
| 攻勢の加護 | `blessing_offense` | `rare` | 171 | 49 | 21 | 0 |

### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 罠糸の加護 | `blessing_trap_web` | 217 | 49.3% | 217 | 80 | 80 | 12 | 12 | 0 | 0 |
| 速の加護 | `blessing_speed` | 217 | 46.5% | 220 | 66 | 66 | 0 | 0 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 196 | 43.9% | 199 | 43 | 43 | 43 | 0 | 0 | 43 |
| 防の加護 | `blessing_guard` | 193 | 50.8% | 194 | 50 | 50 | 0 | 0 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 189 | 50.8% | 190 | 44 | 44 | 0 | 0 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 184 | 35.9% | 185 | 31 | 31 | 2 | 2 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 181 | 44.8% | 181 | 57 | 57 | 11 | 11 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 179 | 48.6% | 179 | 37 | 37 | 5 | 5 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 173 | 41.0% | 174 | 57 | 57 | 0 | 0 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 171 | 46.8% | 171 | 49 | 49 | 16 | 16 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 16000 | 4717 | 29.5% | 2079 | 44.1% | 749 |
| `uncommon` | 16000 | 5750 | 35.9% | 2793 | 48.6% | 1600 |
| `rare` | 8000 | 2624 | 32.8% | 1316 | 50.2% | 669 |

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
