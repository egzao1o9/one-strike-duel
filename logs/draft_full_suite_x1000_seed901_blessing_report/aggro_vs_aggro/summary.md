# Draft Report

## Configuration

- Draft Bot 1: `AggroDraftBot`
- Draft Bot 2: `AggroDraftBot`
- Play Bot 1: `AggroBot`
- Play Bot 2: `AggroBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 4901
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
| `AggroDraftBot` | 2000 | 921 | 921 | 158 | 46.1% | 45.5% | 15.6% | 54.4% | 30.0% | 3.15 | 3.01 | 44.3% | 47.8% | 72.4% | 2.0% | 25.5% | 12.93 | 6.11 | 0.97 | 6.6 | 3.8 | 3.4 | 6.2 | 8 | 8 | 4 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| AggroDraftBot vs AggroDraftBot | 1000 | 79 | `AggroDraftBot`=921 | 1.51 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 741 |
| 2 | 圧迫 | 735 |
| 3 | ステップ | 617 |
| 4 | 牽制 | 600 |
| 5 | 防御 | 599 |
| 6 | 構え | 598 |
| 7 | 集中 | 536 |
| 8 | 貫き | 402 |
| 9 | 崩し | 383 |
| 10 | 粉砕 | 357 |
| 11 | 返し刃 | 331 |
| 12 | 踏ん張り | 316 |
| 13 | 十字受け | 284 |
| 14 | 大振り | 272 |
| 15 | 強撃 | 272 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 321 |
| 2 | 圧迫 | 289 |
| 3 | 牽制 | 283 |
| 4 | 貫き | 260 |
| 5 | 構え | 258 |
| 6 | ステップ | 251 |
| 7 | 防御 | 239 |
| 8 | 崩し | 225 |
| 9 | 集中 | 215 |
| 10 | 粉砕 | 182 |
| 11 | 踏み込み | 178 |
| 12 | 返し刃 | 177 |
| 13 | 踏ん張り | 157 |
| 14 | 大振り | 147 |
| 15 | 強撃 | 132 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 貫き | 239 |
| 2 | 攻撃 | 228 |
| 3 | 崩し | 199 |
| 4 | 粉砕 | 167 |
| 5 | 踏み込み | 167 |
| 6 | ステップ | 162 |
| 7 | 防御 | 144 |
| 8 | 大振り | 139 |
| 9 | 返し刃 | 133 |
| 10 | 強撃 | 114 |
| 11 | 踏ん張り | 103 |
| 12 | 渾身 | 100 |
| 13 | 押し込み | 84 |
| 14 | 構え | 80 |
| 15 | 残像 | 79 |

### Blessing Involvement Overall

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 防の加護 | `blessing_guard` | 235 | 48.5% | 235 | 52 | 52 | 0 | 0 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 222 | 43.2% | 225 | 62 | 62 | 11 | 11 | 0 | 0 |
| 速の加護 | `blessing_speed` | 205 | 47.8% | 206 | 46 | 46 | 0 | 0 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 199 | 36.2% | 200 | 44 | 44 | 44 | 0 | 0 | 44 |
| 鈍足の加護 | `blessing_slow` | 189 | 45.5% | 190 | 36 | 36 | 1 | 1 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 187 | 42.2% | 188 | 61 | 61 | 0 | 0 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 185 | 47.0% | 185 | 64 | 64 | 18 | 18 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 168 | 46.4% | 169 | 42 | 42 | 12 | 12 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 167 | 43.7% | 169 | 32 | 32 | 0 | 0 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 166 | 38.6% | 166 | 28 | 28 | 1 | 1 | 0 | 0 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `AggroDraftBot` | 3.16 | 0.95 | 1.48 | 2.27 | 0.98 | 1.3 | 304 (15.2%) | 304 (33.0%) |

## Drafter Details

### AggroDraftBot

- Win Rate: 46.1%
- Draw Rate: 7.9%
- First Pass Win Rate: 45.5%
- Win With Fewer Cards: 15.6%
- Win With Same Cards: 54.4%
- Win With More Cards: 30.0%
- Winner Facedown Avg: 3.15
- Loser Facedown Avg: 3.01
- Starting Player Win Rate: 44.3%
- Responding Player Win Rate: 47.8%
- Final Stats Avg: A=3.16, B=0.95, S=1.48
- Losing Final Stats Avg: A=2.27, B=0.98, S=1.3
- Lost With Speed Advantage: 304 (15.2%)
- Won After Blocking Faster Attack: 304 (33.0%)
- Action Rates: set=72.4%, set_pass=2.0%, pass=25.5%
- set_pass Candidate Avg / Match: 15.59
- Turns: min=1, avg=1.51, max=5
- Battle / Control / Blessing: avg=12.93 / 6.11 / 0.97
- Role Colors: red=6.6, blue=3.8, green=3.4, white=6.2
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 2643 |
| 2 | 防御 | 2436 |
| 3 | ステップ | 2403 |
| 4 | 圧迫 | 2333 |
| 5 | 構え | 2113 |
| 6 | 集中 | 2045 |
| 7 | 牽制 | 2027 |
| 8 | 崩し | 1320 |
| 9 | 貫き | 1291 |
| 10 | 粉砕 | 1143 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 1181 |
| 2 | ステップ | 1128 |
| 3 | 防御 | 1101 |
| 4 | 圧迫 | 1029 |
| 5 | 構え | 996 |
| 6 | 集中 | 975 |
| 7 | 牽制 | 958 |
| 8 | 崩し | 658 |
| 9 | 貫き | 651 |
| 10 | 粉砕 | 515 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 2643 | 741 | 321 | 228 |
| 防御 | `battle_defend` | `common` | 2436 | 599 | 239 | 144 |
| ステップ | `battle_step` | `common` | 2403 | 617 | 251 | 162 |
| 圧迫 | `control_pressure` | `common` | 2333 | 735 | 289 | 78 |
| 構え | `control_guard` | `common` | 2113 | 598 | 258 | 80 |
| 集中 | `control_focus` | `common` | 2045 | 536 | 215 | 65 |
| 牽制 | `control_disrupt` | `common` | 2027 | 600 | 283 | 17 |
| 崩し | `battle_break` | `uncommon` | 1320 | 383 | 225 | 199 |
| 貫き | `battle_pierce` | `uncommon` | 1291 | 402 | 260 | 239 |
| 粉砕 | `battle_crush` | `uncommon` | 1143 | 357 | 182 | 167 |
| 返し刃 | `battle_counter` | `uncommon` | 1074 | 331 | 177 | 133 |
| 十字受け | `battle_cross_guard` | `uncommon` | 1025 | 284 | 130 | 73 |
| 踏ん張り | `battle_brace` | `uncommon` | 999 | 316 | 157 | 103 |
| 強撃 | `battle_power_attack` | `uncommon` | 910 | 272 | 132 | 114 |
| フェイント | `battle_feint` | `uncommon` | 898 | 264 | 99 | 57 |
| 踏み込み | `battle_step_in` | `rare` | 875 | 266 | 178 | 167 |
| Bastion | `battle_bastion` | `uncommon` | 857 | 266 | 112 | 44 |
| 押し込み | `battle_press` | `uncommon` | 841 | 255 | 120 | 84 |
| 退き足 | `battle_backstep` | `uncommon` | 840 | 230 | 88 | 48 |
| 大振り | `battle_heavy_swing` | `rare` | 802 | 272 | 147 | 139 |
| 渾身 | `battle_all_in` | `rare` | 800 | 258 | 106 | 100 |
| Bulwark | `battle_bulwark` | `uncommon` | 754 | 227 | 93 | 50 |
| 受け流し | `battle_guard` | `uncommon` | 738 | 227 | 95 | 55 |
| 残像 | `battle_afterimage` | `rare` | 732 | 233 | 103 | 79 |
| 鉄壁 | `battle_wall` | `rare` | 717 | 220 | 112 | 45 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 644 | 195 | 83 | 40 |
| 疾走 | `battle_dash` | `rare` | 643 | 182 | 92 | 71 |
| 蓄え | `control_reserve` | `rare` | 524 | 168 | 66 | 10 |
| Crush Spirit | `control_crush_spirit` | `rare` | 502 | 163 | 94 | 2 |
| 受け直し | `control_cover` | `uncommon` | 488 | 161 | 64 | 18 |
| Tripwire | `battle_tripwire` | `rare` | 472 | 1 | 0 | 0 |
| 前のめり | `control_overclock` | `uncommon` | 453 | 129 | 64 | 23 |
| 重心落とし | `control_anchor` | `uncommon` | 391 | 108 | 48 | 20 |
| 補強 | `control_fortify` | `uncommon` | 377 | 120 | 50 | 10 |
| 加速 | `control_haste` | `uncommon` | 331 | 97 | 57 | 28 |
| Blank First | `control_blank_first` | `uncommon` | 329 | 127 | 55 | 4 |
| 勢い溜め | `control_momentum` | `uncommon` | 297 | 96 | 42 | 7 |
| 防の加護 | `blessing_guard` | `rare` | 235 | 52 | 25 | 0 |
| 防壁の加護 | `blessing_barrier` | `rare` | 225 | 62 | 25 | 0 |
| 速の加護 | `blessing_speed` | `rare` | 206 | 46 | 26 | 0 |
| 見切りの加護 | `blessing_insight` | `rare` | 200 | 44 | 11 | 0 |
| 鈍足の加護 | `blessing_slow` | `rare` | 190 | 36 | 13 | 0 |
| 知恵の加護 | `blessing_draw` | `rare` | 188 | 61 | 24 | 0 |
| 罠糸の加護 | `blessing_trap_web` | `rare` | 185 | 64 | 30 | 0 |
| 攻勢の加護 | `blessing_offense` | `rare` | 169 | 42 | 19 | 0 |
| 攻の加護 | `blessing_attack` | `rare` | 169 | 32 | 20 | 0 |
| 抑制の加護 | `blessing_suppression` | `rare` | 166 | 28 | 12 | 0 |

### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 防の加護 | `blessing_guard` | 235 | 48.5% | 235 | 52 | 52 | 0 | 0 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 222 | 43.2% | 225 | 62 | 62 | 11 | 11 | 0 | 0 |
| 速の加護 | `blessing_speed` | 205 | 47.8% | 206 | 46 | 46 | 0 | 0 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 199 | 36.2% | 200 | 44 | 44 | 44 | 0 | 0 | 44 |
| 鈍足の加護 | `blessing_slow` | 189 | 45.5% | 190 | 36 | 36 | 1 | 1 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 187 | 42.2% | 188 | 61 | 61 | 0 | 0 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 185 | 47.0% | 185 | 64 | 64 | 18 | 18 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 168 | 46.4% | 169 | 42 | 42 | 12 | 12 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 167 | 43.7% | 169 | 32 | 32 | 0 | 0 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 166 | 38.6% | 166 | 28 | 28 | 1 | 1 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 16000 | 4426 | 27.7% | 1856 | 41.9% | 774 |
| `uncommon` | 16000 | 4847 | 30.3% | 2333 | 48.1% | 1516 |
| `rare` | 8000 | 2230 | 27.9% | 1103 | 49.5% | 613 |

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
