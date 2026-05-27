# Draft Report

## Configuration

- Draft Bot 1: `GuardDraftBot`
- Draft Bot 2: `GuardDraftBot`
- Play Bot 1: `GuardBot`
- Play Bot 2: `GuardBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 6911
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
| `GuardDraftBot` | 2000 | 948 | 948 | 104 | 47.4% | 44.3% | 18.6% | 48.7% | 32.7% | 2.91 | 2.77 | 47.7% | 47.1% | 70.8% | 2.2% | 27.0% | 10.08 | 7.78 | 2.14 | 5.24 | 3.59 | 3.33 | 7.84 | 8 | 8 | 4 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| GuardDraftBot vs GuardDraftBot | 1000 | 52 | `GuardDraftBot`=948 | 1.75 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 防御 | 646 |
| 2 | 攻撃 | 604 |
| 3 | 圧迫 | 537 |
| 4 | 遠眼 | 536 |
| 5 | 見定め | 529 |
| 6 | 構え | 451 |
| 7 | 牽制 | 448 |
| 8 | ステップ | 438 |
| 9 | 集中 | 390 |
| 10 | 公開勝負 | 388 |
| 11 | 十字受け | 333 |
| 12 | 踏み込み | 300 |
| 13 | 踏ん張り | 298 |
| 14 | 鉄壁 | 286 |
| 15 | Bastion | 286 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 防御 | 294 |
| 2 | 攻撃 | 271 |
| 3 | 圧迫 | 247 |
| 4 | 遠眼 | 233 |
| 5 | 踏み込み | 230 |
| 6 | 牽制 | 230 |
| 7 | 見定め | 215 |
| 8 | 構え | 198 |
| 9 | 十字受け | 184 |
| 10 | 崩し | 181 |
| 11 | 貫き | 181 |
| 12 | ステップ | 176 |
| 13 | 集中 | 167 |
| 14 | 返し刃 | 160 |
| 15 | 公開勝負 | 158 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 210 |
| 2 | 攻撃 | 189 |
| 3 | 貫き | 171 |
| 4 | 崩し | 169 |
| 5 | 防御 | 143 |
| 6 | 粉砕 | 120 |
| 7 | 大振り | 120 |
| 8 | 渾身 | 115 |
| 9 | 返し刃 | 106 |
| 10 | ステップ | 103 |
| 11 | 踏ん張り | 100 |
| 12 | 押し込み | 97 |
| 13 | 疾走 | 92 |
| 14 | 強撃 | 86 |
| 15 | 十字受け | 77 |

### Blessing Involvement Overall

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 間合いの加護 | `blessing_range` | 291 | 46.0% | 295 | 24 | 24 | 4 | 4 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 285 | 46.3% | 289 | 88 | 87 | 37 | 37 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 285 | 43.5% | 287 | 26 | 26 | 2 | 2 | 0 | 0 |
| 受け流しの加護 | `blessing_parry` | 284 | 47.5% | 289 | 73 | 72 | 10 | 10 | 0 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | 278 | 47.1% | 287 | 81 | 77 | 15 | 15 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 274 | 45.6% | 280 | 58 | 58 | 0 | 0 | 0 | 0 |
| 鈍りの加護 | `blessing_dullness` | 271 | 44.6% | 275 | 49 | 49 | 1 | 1 | 0 | 0 |
| 小太刀の加護 | `blessing_shortblade` | 260 | 51.5% | 268 | 52 | 51 | 12 | 12 | 0 | 0 |
| 追風の加護 | `blessing_tailwind` | 259 | 50.2% | 263 | 61 | 59 | 7 | 7 | 0 | 0 |
| 小盾の加護 | `blessing_buckler` | 245 | 46.9% | 246 | 68 | 68 | 10 | 10 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 242 | 47.5% | 247 | 32 | 32 | 33 | 33 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 239 | 48.1% | 240 | 60 | 57 | 16 | 16 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 239 | 42.3% | 243 | 54 | 49 | 5 | 5 | 0 | 0 |
| 速の加護 | `blessing_speed` | 234 | 45.3% | 238 | 67 | 66 | 0 | 0 | 0 | 0 |
| 防の加護 | `blessing_guard` | 212 | 44.8% | 213 | 52 | 51 | 2 | 2 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 211 | 54.5% | 213 | 53 | 53 | 5 | 5 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 110 | 47.3% | 110 | 34 | 34 | 3 | 3 | 0 | 0 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `GuardDraftBot` | 2.88 | 0.88 | 1.21 | 1.82 | 0.81 | 1.09 | 332 (16.6%) | 332 (35.0%) |

## Drafter Details

### GuardDraftBot

- Win Rate: 47.4%
- Draw Rate: 5.2%
- First Pass Win Rate: 44.3%
- Win With Fewer Cards: 18.6%
- Win With Same Cards: 48.7%
- Win With More Cards: 32.7%
- Winner Facedown Avg: 2.91
- Loser Facedown Avg: 2.77
- Starting Player Win Rate: 47.7%
- Responding Player Win Rate: 47.1%
- Final Stats Avg: A=2.88, B=0.88, S=1.21
- Losing Final Stats Avg: A=1.82, B=0.81, S=1.09
- Lost With Speed Advantage: 332 (16.6%)
- Won After Blocking Faster Attack: 332 (35.0%)
- Blessing Ended Facedown: 169
- Blessing Placed But Unused: 776
- Opponent Pass / Set+Pass Into Face-Up Blessing: 1476
- Win Rate When Forcing Opponent Blessing Use: 36.5%
- Action Rates: set=70.8%, set_pass=2.2%, pass=27.0%
- set_pass Candidate Avg / Match: 18.63
- Turns: min=1, avg=1.75, max=23
- Battle / Control / Blessing: avg=10.08 / 7.78 / 2.14
- Role Colors: red=5.24, blue=3.59, green=3.33, white=7.84
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 2068 |
| 2 | 防御 | 1953 |
| 3 | ステップ | 1764 |
| 4 | 圧迫 | 1599 |
| 5 | 構え | 1494 |
| 6 | 見定め | 1472 |
| 7 | 遠眼 | 1454 |
| 8 | 公開勝負 | 1425 |
| 9 | 集中 | 1401 |
| 10 | 牽制 | 1370 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 933 |
| 2 | 防御 | 913 |
| 3 | ステップ | 843 |
| 4 | 圧迫 | 763 |
| 5 | 遠眼 | 740 |
| 6 | 構え | 716 |
| 7 | 公開勝負 | 677 |
| 8 | 牽制 | 676 |
| 9 | 見定め | 671 |
| 10 | 集中 | 652 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 2068 | 604 | 271 | 189 |
| 防御 | `battle_defend` | `common` | 1953 | 646 | 294 | 143 |
| ステップ | `battle_step` | `common` | 1764 | 438 | 176 | 103 |
| 圧迫 | `control_pressure` | `common` | 1599 | 537 | 247 | 36 |
| 構え | `control_guard` | `common` | 1494 | 451 | 198 | 65 |
| 見定め | `control_peek_own_top` | `common` | 1472 | 529 | 215 | 36 |
| 遠眼 | `control_peek_opponent_top` | `common` | 1454 | 536 | 233 | 64 |
| 公開勝負 | `control_opening_expose` | `common` | 1425 | 388 | 158 | 55 |
| 集中 | `control_focus` | `common` | 1401 | 390 | 167 | 76 |
| 牽制 | `control_disrupt` | `common` | 1370 | 448 | 230 | 15 |
| 貫き | `battle_pierce` | `uncommon` | 885 | 265 | 181 | 171 |
| 崩し | `battle_break` | `uncommon` | 858 | 272 | 181 | 169 |
| 十字受け | `battle_cross_guard` | `uncommon` | 785 | 333 | 184 | 77 |
| 踏み込み | `battle_step_in` | `rare` | 763 | 300 | 230 | 210 |
| 踏ん張り | `battle_brace` | `uncommon` | 739 | 298 | 157 | 100 |
| 粉砕 | `battle_crush` | `uncommon` | 732 | 241 | 135 | 120 |
| 渾身 | `battle_all_in` | `rare` | 723 | 234 | 121 | 115 |
| Bastion | `battle_bastion` | `uncommon` | 703 | 286 | 120 | 34 |
| 返し刃 | `battle_counter` | `uncommon` | 701 | 282 | 160 | 106 |
| 残像 | `battle_afterimage` | `rare` | 686 | 263 | 109 | 51 |
| 鉄壁 | `battle_wall` | `rare` | 674 | 286 | 133 | 40 |
| 大振り | `battle_heavy_swing` | `rare` | 650 | 247 | 125 | 120 |
| 押し込み | `battle_press` | `uncommon` | 643 | 249 | 140 | 97 |
| 退き足 | `battle_backstep` | `uncommon` | 638 | 255 | 100 | 42 |
| 疾走 | `battle_dash` | `rare` | 628 | 237 | 129 | 92 |
| 受け流し | `battle_guard` | `uncommon` | 625 | 212 | 108 | 54 |
| Bulwark | `battle_bulwark` | `uncommon` | 624 | 229 | 116 | 54 |
| 強撃 | `battle_power_attack` | `uncommon` | 598 | 196 | 99 | 86 |
| フェイント | `battle_feint` | `uncommon` | 596 | 206 | 83 | 45 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 591 | 219 | 99 | 44 |
| Tripwire | `battle_tripwire` | `rare` | 528 | 3 | 1 | 1 |
| 受け直し | `control_cover` | `uncommon` | 351 | 127 | 54 | 12 |
| 前のめり | `control_overclock` | `uncommon` | 342 | 108 | 61 | 17 |
| 重心落とし | `control_anchor` | `uncommon` | 324 | 89 | 42 | 17 |
| 穢れ | `control_defile` | `uncommon` | 310 | 29 | 11 | 1 |
| 補強 | `control_fortify` | `uncommon` | 304 | 110 | 55 | 14 |
| 加速 | `control_haste` | `uncommon` | 299 | 92 | 39 | 16 |
| 間合いの加護 | `blessing_range` | `uncommon` | 295 | 24 | 12 | 0 |
| 攻勢の加護 | `blessing_offense` | `rare` | 289 | 88 | 49 | 0 |
| 受け流しの加護 | `blessing_parry` | `uncommon` | 289 | 73 | 32 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | `uncommon` | 287 | 81 | 40 | 0 |
| 抑制の加護 | `blessing_suppression` | `rare` | 287 | 26 | 10 | 0 |
| Blank First | `control_blank_first` | `uncommon` | 284 | 117 | 53 | 4 |
| 祓い直し | `control_discard_facedown_blessing` | `uncommon` | 284 | 7 | 3 | 0 |
| 攻の加護 | `blessing_attack` | `rare` | 280 | 58 | 31 | 0 |
| 手繰り直し | `control_redraw_hand` | `uncommon` | 279 | 40 | 16 | 6 |
| 迷い手 | `control_hand_echo` | `uncommon` | 278 | 84 | 25 | 13 |
| 封祈 | `control_blessing_lock` | `uncommon` | 276 | 27 | 15 | 1 |
| 鈍りの加護 | `blessing_dullness` | `uncommon` | 275 | 49 | 14 | 0 |
| 小太刀の加護 | `blessing_shortblade` | `uncommon` | 268 | 52 | 24 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 263 | 81 | 38 | 9 |
| 追風の加護 | `blessing_tailwind` | `uncommon` | 263 | 61 | 33 | 0 |
| 探り | `control_peek_hand` | `uncommon` | 259 | 77 | 28 | 5 |
| 看破 | `control_opening_read` | `uncommon` | 256 | 75 | 32 | 12 |
| 前借り | `control_all_in_focus` | `uncommon` | 250 | 82 | 35 | 12 |
| 見切りの加護 | `blessing_insight` | `rare` | 247 | 32 | 12 | 0 |
| 小盾の加護 | `blessing_buckler` | `uncommon` | 246 | 68 | 31 | 0 |
| 鈍足の加護 | `blessing_slow` | `rare` | 243 | 54 | 30 | 0 |
| 防壁の加護 | `blessing_barrier` | `rare` | 240 | 60 | 25 | 0 |
| 速の加護 | `blessing_speed` | `rare` | 238 | 67 | 27 | 0 |
| 罠糸の加護 | `blessing_trap_web` | `rare` | 213 | 53 | 32 | 0 |
| 防の加護 | `blessing_guard` | `rare` | 213 | 52 | 17 | 0 |
| 転祈 | `control_blessing_flip` | `rare` | 209 | 8 | 4 | 0 |
| 破祈 | `control_blessing_break` | `rare` | 207 | 23 | 12 | 2 |
| 先触れ | `control_topdeck_hand` | `rare` | 202 | 64 | 24 | 7 |
| Crush Spirit | `control_crush_spirit` | `rare` | 185 | 82 | 40 | 1 |
| 蓄え | `control_reserve` | `rare` | 185 | 69 | 25 | 3 |
| 知恵の加護 | `blessing_draw` | `rare` | 110 | 34 | 12 | 0 |

### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 間合いの加護 | `blessing_range` | 291 | 46.0% | 295 | 24 | 24 | 4 | 4 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 285 | 46.3% | 289 | 88 | 87 | 37 | 37 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 285 | 43.5% | 287 | 26 | 26 | 2 | 2 | 0 | 0 |
| 受け流しの加護 | `blessing_parry` | 284 | 47.5% | 289 | 73 | 72 | 10 | 10 | 0 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | 278 | 47.1% | 287 | 81 | 77 | 15 | 15 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 274 | 45.6% | 280 | 58 | 58 | 0 | 0 | 0 | 0 |
| 鈍りの加護 | `blessing_dullness` | 271 | 44.6% | 275 | 49 | 49 | 1 | 1 | 0 | 0 |
| 小太刀の加護 | `blessing_shortblade` | 260 | 51.5% | 268 | 52 | 51 | 12 | 12 | 0 | 0 |
| 追風の加護 | `blessing_tailwind` | 259 | 50.2% | 263 | 61 | 59 | 7 | 7 | 0 | 0 |
| 小盾の加護 | `blessing_buckler` | 245 | 46.9% | 246 | 68 | 68 | 10 | 10 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 242 | 47.5% | 247 | 32 | 32 | 33 | 33 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 239 | 48.1% | 240 | 60 | 57 | 16 | 16 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 239 | 42.3% | 243 | 54 | 49 | 5 | 5 | 0 | 0 |
| 速の加護 | `blessing_speed` | 234 | 45.3% | 238 | 67 | 66 | 0 | 0 | 0 | 0 |
| 防の加護 | `blessing_guard` | 212 | 44.8% | 213 | 52 | 51 | 2 | 2 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 211 | 54.5% | 213 | 53 | 53 | 5 | 5 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 110 | 47.3% | 110 | 34 | 34 | 3 | 3 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 16000 | 4967 | 31.0% | 2189 | 44.1% | 782 |
| `uncommon` | 16000 | 5096 | 31.9% | 2556 | 50.2% | 1338 |
| `rare` | 8000 | 2340 | 29.2% | 1198 | 51.2% | 642 |

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
