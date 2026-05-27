# Draft Report

## Configuration

- Draft Bot 1: `StandardDraftBot`
- Draft Bot 2: `StandardDraftBot`
- Play Bot 1: `StandardBot`
- Play Bot 2: `StandardBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 1901
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
| `StandardDraftBot` | 2000 | 922 | 922 | 156 | 46.1% | 42.6% | 12.7% | 56.7% | 30.6% | 3.16 | 2.98 | 43.6% | 48.6% | 72.2% | 2.0% | 25.9% | 12.91 | 6.12 | 0.96 | 6.55 | 3.76 | 3.47 | 6.22 | 8 | 8 | 4 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| StandardDraftBot vs StandardDraftBot | 1000 | 78 | `StandardDraftBot`=922 | 1.57 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 圧迫 | 763 |
| 2 | 攻撃 | 711 |
| 3 | 防御 | 688 |
| 4 | 構え | 626 |
| 5 | ステップ | 621 |
| 6 | 牽制 | 585 |
| 7 | 集中 | 563 |
| 8 | 崩し | 427 |
| 9 | 貫き | 418 |
| 10 | 返し刃 | 368 |
| 11 | 十字受け | 329 |
| 12 | 粉砕 | 329 |
| 13 | 踏ん張り | 326 |
| 14 | 踏み込み | 292 |
| 15 | Bastion | 289 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 圧迫 | 319 |
| 2 | 攻撃 | 317 |
| 3 | 防御 | 289 |
| 4 | 牽制 | 285 |
| 5 | 構え | 264 |
| 6 | 崩し | 256 |
| 7 | ステップ | 249 |
| 8 | 貫き | 239 |
| 9 | 集中 | 206 |
| 10 | 返し刃 | 196 |
| 11 | 踏み込み | 194 |
| 12 | 十字受け | 180 |
| 13 | 粉砕 | 167 |
| 14 | 踏ん張り | 143 |
| 15 | 鉄壁 | 140 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 崩し | 238 |
| 2 | 攻撃 | 220 |
| 3 | 貫き | 220 |
| 4 | 踏み込み | 178 |
| 5 | ステップ | 150 |
| 6 | 返し刃 | 148 |
| 7 | 防御 | 147 |
| 8 | 粉砕 | 146 |
| 9 | 大振り | 115 |
| 10 | 強撃 | 109 |
| 11 | 十字受け | 107 |
| 12 | 渾身 | 105 |
| 13 | 疾走 | 99 |
| 14 | 踏ん張り | 97 |
| 15 | 押し込み | 80 |

### Blessing Involvement Overall

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 速の加護 | `blessing_speed` | 229 | 49.3% | 231 | 46 | 46 | 0 | 0 | 0 | 0 |
| 防の加護 | `blessing_guard` | 212 | 49.1% | 213 | 52 | 52 | 0 | 0 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 202 | 42.1% | 205 | 55 | 55 | 17 | 17 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 199 | 48.2% | 199 | 59 | 59 | 0 | 0 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 195 | 46.2% | 195 | 45 | 45 | 5 | 5 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 182 | 37.4% | 183 | 56 | 56 | 10 | 10 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 181 | 38.1% | 181 | 43 | 43 | 0 | 0 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 180 | 40.6% | 182 | 34 | 34 | 34 | 0 | 0 | 34 |
| 抑制の加護 | `blessing_suppression` | 178 | 46.1% | 178 | 32 | 32 | 3 | 3 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 159 | 45.3% | 161 | 41 | 41 | 11 | 11 | 0 | 0 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `StandardDraftBot` | 3.22 | 0.97 | 1.51 | 2.33 | 0.9 | 1.27 | 310 (15.5%) | 310 (33.6%) |

## Drafter Details

### StandardDraftBot

- Win Rate: 46.1%
- Draw Rate: 7.8%
- First Pass Win Rate: 42.6%
- Win With Fewer Cards: 12.7%
- Win With Same Cards: 56.7%
- Win With More Cards: 30.6%
- Winner Facedown Avg: 3.16
- Loser Facedown Avg: 2.98
- Starting Player Win Rate: 43.6%
- Responding Player Win Rate: 48.6%
- Final Stats Avg: A=3.22, B=0.97, S=1.51
- Losing Final Stats Avg: A=2.33, B=0.9, S=1.27
- Lost With Speed Advantage: 310 (15.5%)
- Won After Blocking Faster Attack: 310 (33.6%)
- Action Rates: set=72.2%, set_pass=2.0%, pass=25.9%
- set_pass Candidate Avg / Match: 16.28
- Turns: min=1, avg=1.57, max=14
- Battle / Control / Blessing: avg=12.91 / 6.12 / 0.96
- Role Colors: red=6.55, blue=3.76, green=3.47, white=6.22
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 2521 |
| 2 | 防御 | 2475 |
| 3 | 圧迫 | 2469 |
| 4 | ステップ | 2355 |
| 5 | 構え | 2152 |
| 6 | 集中 | 2020 |
| 7 | 牽制 | 2008 |
| 8 | 貫き | 1359 |
| 9 | 崩し | 1325 |
| 10 | 返し刃 | 1104 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 1166 |
| 2 | 防御 | 1165 |
| 3 | 圧迫 | 1128 |
| 4 | ステップ | 1064 |
| 5 | 構え | 993 |
| 6 | 牽制 | 949 |
| 7 | 集中 | 911 |
| 8 | 貫き | 662 |
| 9 | 崩し | 639 |
| 10 | 返し刃 | 531 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 2521 | 711 | 317 | 220 |
| 防御 | `battle_defend` | `common` | 2475 | 688 | 289 | 147 |
| 圧迫 | `control_pressure` | `common` | 2469 | 763 | 319 | 64 |
| ステップ | `battle_step` | `common` | 2355 | 621 | 249 | 150 |
| 構え | `control_guard` | `common` | 2152 | 626 | 264 | 79 |
| 集中 | `control_focus` | `common` | 2020 | 563 | 206 | 70 |
| 牽制 | `control_disrupt` | `common` | 2008 | 585 | 285 | 22 |
| 貫き | `battle_pierce` | `uncommon` | 1359 | 418 | 239 | 220 |
| 崩し | `battle_break` | `uncommon` | 1325 | 427 | 256 | 238 |
| 返し刃 | `battle_counter` | `uncommon` | 1104 | 368 | 196 | 148 |
| 踏ん張り | `battle_brace` | `uncommon` | 1045 | 326 | 143 | 97 |
| 粉砕 | `battle_crush` | `uncommon` | 1023 | 329 | 167 | 146 |
| 十字受け | `battle_cross_guard` | `uncommon` | 1020 | 329 | 180 | 107 |
| Bastion | `battle_bastion` | `uncommon` | 929 | 289 | 130 | 46 |
| 強撃 | `battle_power_attack` | `uncommon` | 895 | 284 | 135 | 109 |
| 踏み込み | `battle_step_in` | `rare` | 875 | 292 | 194 | 178 |
| 押し込み | `battle_press` | `uncommon` | 855 | 244 | 124 | 80 |
| フェイント | `battle_feint` | `uncommon` | 853 | 228 | 91 | 53 |
| 退き足 | `battle_backstep` | `uncommon` | 840 | 263 | 96 | 48 |
| 渾身 | `battle_all_in` | `rare` | 833 | 269 | 113 | 105 |
| 鉄壁 | `battle_wall` | `rare` | 764 | 267 | 140 | 55 |
| 受け流し | `battle_guard` | `uncommon` | 751 | 234 | 108 | 60 |
| 大振り | `battle_heavy_swing` | `rare` | 742 | 254 | 129 | 115 |
| Bulwark | `battle_bulwark` | `uncommon` | 732 | 239 | 113 | 57 |
| 残像 | `battle_afterimage` | `rare` | 727 | 230 | 107 | 70 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 695 | 203 | 80 | 42 |
| 疾走 | `battle_dash` | `rare` | 617 | 208 | 129 | 99 |
| 蓄え | `control_reserve` | `rare` | 515 | 153 | 52 | 6 |
| Crush Spirit | `control_crush_spirit` | `rare` | 506 | 146 | 78 | 3 |
| Tripwire | `battle_tripwire` | `rare` | 493 | 1 | 1 | 1 |
| 受け直し | `control_cover` | `uncommon` | 480 | 157 | 64 | 7 |
| 前のめり | `control_overclock` | `uncommon` | 406 | 131 | 64 | 15 |
| 補強 | `control_fortify` | `uncommon` | 372 | 117 | 51 | 9 |
| 重心落とし | `control_anchor` | `uncommon` | 364 | 106 | 50 | 17 |
| 加速 | `control_haste` | `uncommon` | 334 | 103 | 48 | 15 |
| Blank First | `control_blank_first` | `uncommon` | 318 | 106 | 46 | 3 |
| 勢い溜め | `control_momentum` | `uncommon` | 300 | 89 | 44 | 12 |
| 速の加護 | `blessing_speed` | `rare` | 231 | 46 | 25 | 0 |
| 防の加護 | `blessing_guard` | `rare` | 213 | 52 | 26 | 0 |
| 防壁の加護 | `blessing_barrier` | `rare` | 205 | 55 | 18 | 0 |
| 知恵の加護 | `blessing_draw` | `rare` | 199 | 59 | 23 | 0 |
| 鈍足の加護 | `blessing_slow` | `rare` | 195 | 45 | 20 | 0 |
| 罠糸の加護 | `blessing_trap_web` | `rare` | 183 | 56 | 16 | 0 |
| 見切りの加護 | `blessing_insight` | `rare` | 182 | 34 | 12 | 0 |
| 攻の加護 | `blessing_attack` | `rare` | 181 | 43 | 18 | 0 |
| 抑制の加護 | `blessing_suppression` | `rare` | 178 | 32 | 15 | 0 |
| 攻勢の加護 | `blessing_offense` | `rare` | 161 | 41 | 23 | 0 |

### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 速の加護 | `blessing_speed` | 229 | 49.3% | 231 | 46 | 46 | 0 | 0 | 0 | 0 |
| 防の加護 | `blessing_guard` | 212 | 49.1% | 213 | 52 | 52 | 0 | 0 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 202 | 42.1% | 205 | 55 | 55 | 17 | 17 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 199 | 48.2% | 199 | 59 | 59 | 0 | 0 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 195 | 46.2% | 195 | 45 | 45 | 5 | 5 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 182 | 37.4% | 183 | 56 | 56 | 10 | 10 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 181 | 38.1% | 181 | 43 | 43 | 0 | 0 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 180 | 40.6% | 182 | 34 | 34 | 34 | 0 | 0 | 34 |
| 抑制の加護 | `blessing_suppression` | 178 | 46.1% | 178 | 32 | 32 | 3 | 3 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 159 | 45.3% | 161 | 41 | 41 | 11 | 11 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 16000 | 4557 | 28.5% | 1929 | 42.3% | 752 |
| `uncommon` | 16000 | 4990 | 31.2% | 2425 | 48.6% | 1529 |
| `rare` | 8000 | 2283 | 28.5% | 1139 | 49.9% | 632 |

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
