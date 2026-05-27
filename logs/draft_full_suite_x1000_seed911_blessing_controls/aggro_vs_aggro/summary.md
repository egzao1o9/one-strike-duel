# Draft Report

## Configuration

- Draft Bot 1: `AggroDraftBot`
- Draft Bot 2: `AggroDraftBot`
- Play Bot 1: `AggroBot`
- Play Bot 2: `AggroBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 4911
- Pool: `base_pool` (166 copies)
- Pairing Mode: mirrored seats per round
- Draft Mode: `full`
- Fast Report: on
- Lean Draft Logging: on
- Save Battle Logs: on
- Draft Flow: normal public pack + normal hidden pack, then public rare + hidden rare, with order swapped in second half

## Drafter Summary

| Drafter | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Winner Set Avg | Loser Set Avg | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate | Battle Avg | Control Avg | Blessing Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `AggroDraftBot` | 2000 | 932 | 932 | 136 | 46.6% | 48.6% | 16.3% | 52.7% | 31.0% | 2.92 | 2.77 | 47.7% | 45.5% | 70.3% | 2.7% | 27.0% | 10.07 | 7.83 | 2.1 | 5.36 | 3.54 | 3.21 | 7.89 | 8 | 8 | 4 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| AggroDraftBot vs AggroDraftBot | 1000 | 68 | `AggroDraftBot`=932 | 1.6 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 619 |
| 2 | 防御 | 570 |
| 3 | ステップ | 505 |
| 4 | 圧迫 | 488 |
| 5 | 見定め | 461 |
| 6 | 牽制 | 443 |
| 7 | 構え | 418 |
| 8 | 遠眼 | 411 |
| 9 | 公開勝負 | 388 |
| 10 | 集中 | 371 |
| 11 | 崩し | 306 |
| 12 | 踏み込み | 279 |
| 13 | 粉砕 | 273 |
| 14 | 貫き | 264 |
| 15 | 鉄壁 | 262 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 291 |
| 2 | 防御 | 239 |
| 3 | 圧迫 | 229 |
| 4 | ステップ | 220 |
| 5 | 牽制 | 214 |
| 6 | 踏み込み | 207 |
| 7 | 崩し | 194 |
| 8 | 見定め | 179 |
| 9 | 構え | 173 |
| 10 | 貫き | 169 |
| 11 | 遠眼 | 167 |
| 12 | 粉砕 | 165 |
| 13 | 返し刃 | 155 |
| 14 | 公開勝負 | 150 |
| 15 | 集中 | 143 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 205 |
| 2 | 踏み込み | 196 |
| 3 | 崩し | 180 |
| 4 | 粉砕 | 149 |
| 5 | 貫き | 145 |
| 6 | ステップ | 132 |
| 7 | 防御 | 131 |
| 8 | 大振り | 126 |
| 9 | 渾身 | 120 |
| 10 | 返し刃 | 111 |
| 11 | 疾走 | 103 |
| 12 | 強撃 | 86 |
| 13 | 踏ん張り | 81 |
| 14 | 押し込み | 72 |
| 15 | 残像 | 68 |

### Blessing Involvement Overall

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 小太刀の加護 | `blessing_shortblade` | 297 | 48.5% | 303 | 53 | 53 | 8 | 8 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 285 | 41.4% | 287 | 46 | 45 | 5 | 5 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 271 | 42.8% | 275 | 56 | 56 | 19 | 19 | 0 | 0 |
| 受け流しの加護 | `blessing_parry` | 270 | 41.9% | 276 | 69 | 69 | 11 | 11 | 0 | 0 |
| 鈍りの加護 | `blessing_dullness` | 266 | 49.6% | 267 | 55 | 55 | 2 | 2 | 0 | 0 |
| 追風の加護 | `blessing_tailwind` | 264 | 41.3% | 271 | 56 | 56 | 1 | 1 | 0 | 0 |
| 小盾の加護 | `blessing_buckler` | 263 | 44.1% | 264 | 53 | 53 | 3 | 3 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 262 | 40.1% | 263 | 59 | 56 | 0 | 0 | 0 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | 254 | 47.6% | 258 | 84 | 84 | 14 | 14 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 245 | 42.4% | 245 | 70 | 69 | 15 | 15 | 0 | 0 |
| 速の加護 | `blessing_speed` | 243 | 39.5% | 243 | 40 | 39 | 1 | 1 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 242 | 46.3% | 245 | 60 | 58 | 12 | 12 | 0 | 0 |
| 間合いの加護 | `blessing_range` | 241 | 42.7% | 246 | 39 | 38 | 8 | 8 | 0 | 0 |
| 防の加護 | `blessing_guard` | 236 | 47.9% | 237 | 57 | 56 | 1 | 1 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 201 | 47.3% | 202 | 30 | 28 | 28 | 28 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 198 | 44.4% | 198 | 38 | 38 | 4 | 4 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 122 | 54.1% | 122 | 43 | 43 | 1 | 1 | 0 | 0 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `AggroDraftBot` | 2.91 | 0.83 | 1.23 | 1.88 | 0.81 | 1.05 | 308 (15.4%) | 308 (33.0%) |

## Drafter Details

### AggroDraftBot

- Win Rate: 46.6%
- Draw Rate: 6.8%
- First Pass Win Rate: 48.6%
- Win With Fewer Cards: 16.3%
- Win With Same Cards: 52.7%
- Win With More Cards: 31.0%
- Winner Facedown Avg: 2.92
- Loser Facedown Avg: 2.77
- Starting Player Win Rate: 47.7%
- Responding Player Win Rate: 45.5%
- Final Stats Avg: A=2.91, B=0.83, S=1.23
- Losing Final Stats Avg: A=1.88, B=0.81, S=1.05
- Lost With Speed Advantage: 308 (15.4%)
- Won After Blocking Faster Attack: 308 (33.0%)
- Blessing Ended Facedown: 136
- Blessing Placed But Unused: 788
- Opponent Pass / Set+Pass Into Face-Up Blessing: 1306
- Win Rate When Forcing Opponent Blessing Use: 35.0%
- Action Rates: set=70.3%, set_pass=2.7%, pass=27.0%
- set_pass Candidate Avg / Match: 15.31
- Turns: min=1, avg=1.6, max=11
- Battle / Control / Blessing: avg=10.07 / 7.83 / 2.1
- Role Colors: red=5.36, blue=3.54, green=3.21, white=7.89
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 2072 |
| 2 | 防御 | 1937 |
| 3 | ステップ | 1812 |
| 4 | 圧迫 | 1592 |
| 5 | 見定め | 1486 |
| 6 | 構え | 1461 |
| 7 | 牽制 | 1437 |
| 8 | 集中 | 1435 |
| 9 | 遠眼 | 1423 |
| 10 | 公開勝負 | 1345 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 1005 |
| 2 | 防御 | 913 |
| 3 | ステップ | 842 |
| 4 | 圧迫 | 763 |
| 5 | 牽制 | 700 |
| 6 | 見定め | 678 |
| 7 | 集中 | 661 |
| 8 | 構え | 648 |
| 9 | 遠眼 | 627 |
| 10 | 公開勝負 | 619 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 2072 | 619 | 291 | 205 |
| 防御 | `battle_defend` | `common` | 1937 | 570 | 239 | 131 |
| ステップ | `battle_step` | `common` | 1812 | 505 | 220 | 132 |
| 圧迫 | `control_pressure` | `common` | 1592 | 488 | 229 | 52 |
| 見定め | `control_peek_own_top` | `common` | 1486 | 461 | 179 | 42 |
| 構え | `control_guard` | `common` | 1461 | 418 | 173 | 52 |
| 牽制 | `control_disrupt` | `common` | 1437 | 443 | 214 | 14 |
| 集中 | `control_focus` | `common` | 1435 | 371 | 143 | 63 |
| 遠眼 | `control_peek_opponent_top` | `common` | 1423 | 411 | 167 | 48 |
| 公開勝負 | `control_opening_expose` | `common` | 1345 | 388 | 150 | 53 |
| 崩し | `battle_break` | `uncommon` | 909 | 306 | 194 | 180 |
| 貫き | `battle_pierce` | `uncommon` | 865 | 264 | 169 | 145 |
| 返し刃 | `battle_counter` | `uncommon` | 777 | 258 | 155 | 111 |
| 踏み込み | `battle_step_in` | `rare` | 758 | 279 | 207 | 196 |
| 粉砕 | `battle_crush` | `uncommon` | 749 | 273 | 165 | 149 |
| 踏ん張り | `battle_brace` | `uncommon` | 738 | 238 | 119 | 81 |
| 渾身 | `battle_all_in` | `rare` | 729 | 259 | 123 | 120 |
| 大振り | `battle_heavy_swing` | `rare` | 716 | 254 | 135 | 126 |
| 残像 | `battle_afterimage` | `rare` | 704 | 241 | 106 | 68 |
| 十字受け | `battle_cross_guard` | `uncommon` | 690 | 244 | 111 | 60 |
| フェイント | `battle_feint` | `uncommon` | 688 | 212 | 79 | 39 |
| 強撃 | `battle_power_attack` | `uncommon` | 668 | 208 | 100 | 86 |
| Bastion | `battle_bastion` | `uncommon` | 656 | 251 | 114 | 38 |
| 鉄壁 | `battle_wall` | `rare` | 653 | 262 | 135 | 45 |
| 退き足 | `battle_backstep` | `uncommon` | 638 | 203 | 82 | 43 |
| 疾走 | `battle_dash` | `rare` | 625 | 203 | 130 | 103 |
| 押し込み | `battle_press` | `uncommon` | 603 | 216 | 107 | 72 |
| 受け流し | `battle_guard` | `uncommon` | 592 | 209 | 102 | 58 |
| Bulwark | `battle_bulwark` | `uncommon` | 547 | 174 | 93 | 50 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 510 | 153 | 63 | 30 |
| Tripwire | `battle_tripwire` | `rare` | 500 | 2 | 1 | 1 |
| 受け直し | `control_cover` | `uncommon` | 369 | 131 | 63 | 9 |
| 前のめり | `control_overclock` | `uncommon` | 354 | 111 | 49 | 18 |
| 重心落とし | `control_anchor` | `uncommon` | 323 | 79 | 38 | 14 |
| 看破 | `control_opening_read` | `uncommon` | 306 | 81 | 33 | 13 |
| 探り | `control_peek_hand` | `uncommon` | 305 | 91 | 29 | 10 |
| 小太刀の加護 | `blessing_shortblade` | `uncommon` | 303 | 53 | 21 | 0 |
| 手繰り直し | `control_redraw_hand` | `uncommon` | 296 | 11 | 3 | 1 |
| 封祈 | `control_blessing_lock` | `uncommon` | 291 | 9 | 3 | 1 |
| 補強 | `control_fortify` | `uncommon` | 287 | 91 | 37 | 11 |
| 抑制の加護 | `blessing_suppression` | `rare` | 287 | 46 | 16 | 0 |
| 迷い手 | `control_hand_echo` | `uncommon` | 285 | 78 | 34 | 11 |
| 勢い溜め | `control_momentum` | `uncommon` | 284 | 81 | 27 | 8 |
| 加速 | `control_haste` | `uncommon` | 280 | 79 | 38 | 9 |
| 祓い直し | `control_discard_facedown_blessing` | `uncommon` | 280 | 3 | 2 | 0 |
| 穢れ | `control_defile` | `uncommon` | 279 | 24 | 12 | 0 |
| 受け流しの加護 | `blessing_parry` | `uncommon` | 276 | 69 | 29 | 0 |
| Blank First | `control_blank_first` | `uncommon` | 275 | 96 | 34 | 3 |
| 攻勢の加護 | `blessing_offense` | `rare` | 275 | 56 | 24 | 0 |
| 追風の加護 | `blessing_tailwind` | `uncommon` | 271 | 56 | 21 | 0 |
| 前借り | `control_all_in_focus` | `uncommon` | 271 | 52 | 22 | 7 |
| 鈍りの加護 | `blessing_dullness` | `uncommon` | 267 | 55 | 21 | 0 |
| 小盾の加護 | `blessing_buckler` | `uncommon` | 264 | 53 | 27 | 0 |
| 攻の加護 | `blessing_attack` | `rare` | 263 | 59 | 24 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | `uncommon` | 258 | 84 | 42 | 0 |
| 間合いの加護 | `blessing_range` | `uncommon` | 246 | 39 | 16 | 0 |
| 罠糸の加護 | `blessing_trap_web` | `rare` | 245 | 70 | 31 | 0 |
| 防壁の加護 | `blessing_barrier` | `rare` | 245 | 60 | 27 | 0 |
| 速の加護 | `blessing_speed` | `rare` | 243 | 40 | 18 | 0 |
| 防の加護 | `blessing_guard` | `rare` | 237 | 57 | 26 | 0 |
| 先触れ | `control_topdeck_hand` | `rare` | 207 | 59 | 20 | 7 |
| Crush Spirit | `control_crush_spirit` | `rare` | 204 | 66 | 37 | 1 |
| 蓄え | `control_reserve` | `rare` | 203 | 63 | 30 | 3 |
| 見切りの加護 | `blessing_insight` | `rare` | 202 | 30 | 16 | 0 |
| 鈍足の加護 | `blessing_slow` | `rare` | 198 | 38 | 19 | 0 |
| 転祈 | `control_blessing_flip` | `rare` | 194 | 12 | 5 | 0 |
| 破祈 | `control_blessing_break` | `rare` | 190 | 10 | 4 | 0 |
| 知恵の加護 | `blessing_draw` | `rare` | 122 | 43 | 20 | 0 |

### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 小太刀の加護 | `blessing_shortblade` | 297 | 48.5% | 303 | 53 | 53 | 8 | 8 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 285 | 41.4% | 287 | 46 | 45 | 5 | 5 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 271 | 42.8% | 275 | 56 | 56 | 19 | 19 | 0 | 0 |
| 受け流しの加護 | `blessing_parry` | 270 | 41.9% | 276 | 69 | 69 | 11 | 11 | 0 | 0 |
| 鈍りの加護 | `blessing_dullness` | 266 | 49.6% | 267 | 55 | 55 | 2 | 2 | 0 | 0 |
| 追風の加護 | `blessing_tailwind` | 264 | 41.3% | 271 | 56 | 56 | 1 | 1 | 0 | 0 |
| 小盾の加護 | `blessing_buckler` | 263 | 44.1% | 264 | 53 | 53 | 3 | 3 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 262 | 40.1% | 263 | 59 | 56 | 0 | 0 | 0 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | 254 | 47.6% | 258 | 84 | 84 | 14 | 14 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 245 | 42.4% | 245 | 70 | 69 | 15 | 15 | 0 | 0 |
| 速の加護 | `blessing_speed` | 243 | 39.5% | 243 | 40 | 39 | 1 | 1 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 242 | 46.3% | 245 | 60 | 58 | 12 | 12 | 0 | 0 |
| 間合いの加護 | `blessing_range` | 241 | 42.7% | 246 | 39 | 38 | 8 | 8 | 0 | 0 |
| 防の加護 | `blessing_guard` | 236 | 47.9% | 237 | 57 | 56 | 1 | 1 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 201 | 47.3% | 202 | 30 | 28 | 28 | 28 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 198 | 44.4% | 198 | 38 | 38 | 4 | 4 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 122 | 54.1% | 122 | 43 | 43 | 1 | 1 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 16000 | 4674 | 29.2% | 2005 | 42.9% | 792 |
| `uncommon` | 16000 | 4635 | 29.0% | 2254 | 48.6% | 1257 |
| `rare` | 8000 | 2209 | 27.6% | 1154 | 52.2% | 670 |

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
