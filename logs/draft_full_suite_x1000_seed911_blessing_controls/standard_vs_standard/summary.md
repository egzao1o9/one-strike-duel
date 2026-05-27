# Draft Report

## Configuration

- Draft Bot 1: `StandardDraftBot`
- Draft Bot 2: `StandardDraftBot`
- Play Bot 1: `StandardBot`
- Play Bot 2: `StandardBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 1911
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
| `StandardDraftBot` | 2000 | 952 | 952 | 96 | 47.6% | 51.4% | 14.4% | 53.2% | 32.5% | 2.94 | 2.76 | 47.9% | 47.3% | 70.7% | 2.8% | 26.5% | 10.06 | 7.85 | 2.09 | 5.29 | 3.55 | 3.25 | 7.91 | 8 | 8 | 4 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| StandardDraftBot vs StandardDraftBot | 1000 | 48 | `StandardDraftBot`=952 | 1.55 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 592 |
| 2 | 防御 | 554 |
| 3 | 圧迫 | 532 |
| 4 | ステップ | 505 |
| 5 | 構え | 466 |
| 6 | 見定め | 439 |
| 7 | 遠眼 | 436 |
| 8 | 公開勝負 | 421 |
| 9 | 集中 | 407 |
| 10 | 牽制 | 401 |
| 11 | 渾身 | 288 |
| 12 | 貫き | 281 |
| 13 | 崩し | 266 |
| 14 | 踏み込み | 264 |
| 15 | 粉砕 | 256 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 271 |
| 2 | 防御 | 264 |
| 3 | 圧迫 | 263 |
| 4 | 構え | 218 |
| 5 | 踏み込み | 205 |
| 6 | ステップ | 205 |
| 7 | 牽制 | 201 |
| 8 | 貫き | 194 |
| 9 | 集中 | 191 |
| 10 | 崩し | 184 |
| 11 | 遠眼 | 182 |
| 12 | 見定め | 168 |
| 13 | 公開勝負 | 165 |
| 14 | 粉砕 | 148 |
| 15 | 渾身 | 138 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 198 |
| 2 | 踏み込み | 195 |
| 3 | 貫き | 176 |
| 4 | 崩し | 161 |
| 5 | 渾身 | 134 |
| 6 | 防御 | 131 |
| 7 | 粉砕 | 130 |
| 8 | ステップ | 129 |
| 9 | 大振り | 123 |
| 10 | 返し刃 | 101 |
| 11 | 疾走 | 101 |
| 12 | 強撃 | 100 |
| 13 | 集中 | 94 |
| 14 | 構え | 85 |
| 15 | 踏ん張り | 84 |

### Blessing Involvement Overall

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 間合いの加護 | `blessing_range` | 280 | 43.6% | 286 | 30 | 29 | 6 | 6 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 270 | 43.3% | 275 | 52 | 51 | 1 | 1 | 0 | 0 |
| 受け流しの加護 | `blessing_parry` | 269 | 45.0% | 273 | 61 | 61 | 13 | 13 | 0 | 0 |
| 小太刀の加護 | `blessing_shortblade` | 268 | 47.0% | 273 | 59 | 58 | 7 | 7 | 0 | 0 |
| 鈍りの加護 | `blessing_dullness` | 266 | 44.4% | 268 | 40 | 40 | 1 | 1 | 0 | 0 |
| 小盾の加護 | `blessing_buckler` | 264 | 44.7% | 266 | 61 | 59 | 10 | 10 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 263 | 41.1% | 268 | 36 | 35 | 1 | 1 | 0 | 0 |
| 追風の加護 | `blessing_tailwind` | 260 | 48.1% | 261 | 55 | 55 | 2 | 2 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 257 | 44.7% | 259 | 52 | 51 | 7 | 7 | 0 | 0 |
| 防の加護 | `blessing_guard` | 255 | 49.0% | 257 | 52 | 51 | 0 | 0 | 0 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | 255 | 41.6% | 258 | 68 | 65 | 13 | 13 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 233 | 49.4% | 238 | 59 | 59 | 19 | 19 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 230 | 50.9% | 230 | 71 | 71 | 11 | 11 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 222 | 45.5% | 225 | 54 | 54 | 10 | 10 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 216 | 47.2% | 219 | 34 | 34 | 35 | 35 | 0 | 0 |
| 速の加護 | `blessing_speed` | 213 | 53.1% | 215 | 41 | 40 | 0 | 0 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 107 | 50.5% | 107 | 30 | 29 | 1 | 1 | 0 | 0 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `StandardDraftBot` | 2.84 | 0.83 | 1.18 | 1.78 | 0.82 | 1.01 | 319 (16.0%) | 319 (33.5%) |

## Drafter Details

### StandardDraftBot

- Win Rate: 47.6%
- Draw Rate: 4.8%
- First Pass Win Rate: 51.4%
- Win With Fewer Cards: 14.4%
- Win With Same Cards: 53.2%
- Win With More Cards: 32.5%
- Winner Facedown Avg: 2.94
- Loser Facedown Avg: 2.76
- Starting Player Win Rate: 47.9%
- Responding Player Win Rate: 47.3%
- Final Stats Avg: A=2.84, B=0.83, S=1.18
- Losing Final Stats Avg: A=1.78, B=0.82, S=1.01
- Lost With Speed Advantage: 319 (16.0%)
- Won After Blocking Faster Attack: 319 (33.5%)
- Blessing Ended Facedown: 135
- Blessing Placed But Unused: 724
- Opponent Pass / Set+Pass Into Face-Up Blessing: 1175
- Win Rate When Forcing Opponent Blessing Use: 49.2%
- Action Rates: set=70.7%, set_pass=2.8%, pass=26.5%
- set_pass Candidate Avg / Match: 14.35
- Turns: min=1, avg=1.55, max=7
- Battle / Control / Blessing: avg=10.06 / 7.85 / 2.09
- Role Colors: red=5.29, blue=3.55, green=3.25, white=7.91
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 2024 |
| 2 | 防御 | 1900 |
| 3 | ステップ | 1833 |
| 4 | 圧迫 | 1693 |
| 5 | 構え | 1557 |
| 6 | 集中 | 1446 |
| 7 | 遠眼 | 1422 |
| 8 | 見定め | 1411 |
| 9 | 公開勝負 | 1403 |
| 10 | 牽制 | 1311 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 973 |
| 2 | 防御 | 919 |
| 3 | ステップ | 854 |
| 4 | 圧迫 | 809 |
| 5 | 構え | 755 |
| 6 | 集中 | 697 |
| 7 | 遠眼 | 690 |
| 8 | 牽制 | 663 |
| 9 | 見定め | 629 |
| 10 | 公開勝負 | 627 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 2024 | 592 | 271 | 198 |
| 防御 | `battle_defend` | `common` | 1900 | 554 | 264 | 131 |
| ステップ | `battle_step` | `common` | 1833 | 505 | 205 | 129 |
| 圧迫 | `control_pressure` | `common` | 1693 | 532 | 263 | 60 |
| 構え | `control_guard` | `common` | 1557 | 466 | 218 | 85 |
| 集中 | `control_focus` | `common` | 1446 | 407 | 191 | 94 |
| 遠眼 | `control_peek_opponent_top` | `common` | 1422 | 436 | 182 | 44 |
| 見定め | `control_peek_own_top` | `common` | 1411 | 439 | 168 | 39 |
| 公開勝負 | `control_opening_expose` | `common` | 1403 | 421 | 165 | 64 |
| 牽制 | `control_disrupt` | `common` | 1311 | 401 | 201 | 17 |
| 貫き | `battle_pierce` | `uncommon` | 869 | 281 | 194 | 176 |
| 崩し | `battle_break` | `uncommon` | 845 | 266 | 184 | 161 |
| 踏み込み | `battle_step_in` | `rare` | 767 | 264 | 205 | 195 |
| 渾身 | `battle_all_in` | `rare` | 763 | 288 | 138 | 134 |
| 返し刃 | `battle_counter` | `uncommon` | 752 | 238 | 137 | 101 |
| 粉砕 | `battle_crush` | `uncommon` | 750 | 256 | 148 | 130 |
| 十字受け | `battle_cross_guard` | `uncommon` | 734 | 248 | 112 | 71 |
| 踏ん張り | `battle_brace` | `uncommon` | 733 | 239 | 125 | 84 |
| 大振り | `battle_heavy_swing` | `rare` | 704 | 225 | 127 | 123 |
| 鉄壁 | `battle_wall` | `rare` | 697 | 228 | 104 | 34 |
| Bastion | `battle_bastion` | `uncommon` | 670 | 230 | 97 | 40 |
| 残像 | `battle_afterimage` | `rare` | 667 | 221 | 92 | 56 |
| 強撃 | `battle_power_attack` | `uncommon` | 661 | 199 | 120 | 100 |
| 押し込み | `battle_press` | `uncommon` | 635 | 207 | 110 | 77 |
| 退き足 | `battle_backstep` | `uncommon` | 634 | 188 | 66 | 40 |
| 疾走 | `battle_dash` | `rare` | 615 | 214 | 123 | 101 |
| フェイント | `battle_feint` | `uncommon` | 606 | 176 | 67 | 40 |
| Bulwark | `battle_bulwark` | `uncommon` | 605 | 199 | 83 | 45 |
| 受け流し | `battle_guard` | `uncommon` | 564 | 190 | 83 | 51 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 551 | 177 | 76 | 35 |
| Tripwire | `battle_tripwire` | `rare` | 539 | 1 | 0 | 0 |
| 受け直し | `control_cover` | `uncommon` | 387 | 119 | 58 | 15 |
| 前のめり | `control_overclock` | `uncommon` | 384 | 111 | 58 | 22 |
| 封祈 | `control_blessing_lock` | `uncommon` | 324 | 15 | 7 | 2 |
| 加速 | `control_haste` | `uncommon` | 314 | 97 | 51 | 17 |
| 祓い直し | `control_discard_facedown_blessing` | `uncommon` | 309 | 5 | 0 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 306 | 74 | 33 | 9 |
| 探り | `control_peek_hand` | `uncommon` | 299 | 89 | 37 | 11 |
| 間合いの加護 | `blessing_range` | `uncommon` | 286 | 30 | 14 | 0 |
| 迷い手 | `control_hand_echo` | `uncommon` | 282 | 81 | 32 | 11 |
| 勢い溜め | `control_momentum` | `uncommon` | 277 | 72 | 31 | 10 |
| 手繰り直し | `control_redraw_hand` | `uncommon` | 277 | 41 | 9 | 5 |
| 穢れ | `control_defile` | `uncommon` | 277 | 19 | 12 | 5 |
| 攻の加護 | `blessing_attack` | `rare` | 275 | 52 | 23 | 0 |
| 前借り | `control_all_in_focus` | `uncommon` | 274 | 91 | 41 | 9 |
| Blank First | `control_blank_first` | `uncommon` | 273 | 97 | 41 | 2 |
| 受け流しの加護 | `blessing_parry` | `uncommon` | 273 | 61 | 32 | 0 |
| 小太刀の加護 | `blessing_shortblade` | `uncommon` | 273 | 59 | 27 | 0 |
| 補強 | `control_fortify` | `uncommon` | 269 | 74 | 36 | 12 |
| 鈍りの加護 | `blessing_dullness` | `uncommon` | 268 | 40 | 19 | 0 |
| 抑制の加護 | `blessing_suppression` | `rare` | 268 | 36 | 11 | 0 |
| 小盾の加護 | `blessing_buckler` | `uncommon` | 266 | 61 | 23 | 0 |
| 追風の加護 | `blessing_tailwind` | `uncommon` | 261 | 55 | 25 | 0 |
| 攻勢の加護 | `blessing_offense` | `rare` | 259 | 52 | 19 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | `uncommon` | 258 | 68 | 25 | 0 |
| 防の加護 | `blessing_guard` | `rare` | 257 | 52 | 27 | 0 |
| 看破 | `control_opening_read` | `uncommon` | 254 | 66 | 25 | 5 |
| 防壁の加護 | `blessing_barrier` | `rare` | 238 | 59 | 26 | 0 |
| 罠糸の加護 | `blessing_trap_web` | `rare` | 230 | 71 | 28 | 0 |
| 鈍足の加護 | `blessing_slow` | `rare` | 225 | 54 | 23 | 0 |
| 見切りの加護 | `blessing_insight` | `rare` | 219 | 34 | 16 | 0 |
| 速の加護 | `blessing_speed` | `rare` | 215 | 41 | 21 | 0 |
| 破祈 | `control_blessing_break` | `rare` | 207 | 13 | 6 | 1 |
| 先触れ | `control_topdeck_hand` | `rare` | 198 | 54 | 21 | 7 |
| 蓄え | `control_reserve` | `rare` | 195 | 66 | 19 | 0 |
| Crush Spirit | `control_crush_spirit` | `rare` | 185 | 71 | 34 | 0 |
| 転祈 | `control_blessing_flip` | `rare` | 170 | 11 | 2 | 0 |
| 知恵の加護 | `blessing_draw` | `rare` | 107 | 30 | 12 | 0 |

### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 間合いの加護 | `blessing_range` | 280 | 43.6% | 286 | 30 | 29 | 6 | 6 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 270 | 43.3% | 275 | 52 | 51 | 1 | 1 | 0 | 0 |
| 受け流しの加護 | `blessing_parry` | 269 | 45.0% | 273 | 61 | 61 | 13 | 13 | 0 | 0 |
| 小太刀の加護 | `blessing_shortblade` | 268 | 47.0% | 273 | 59 | 58 | 7 | 7 | 0 | 0 |
| 鈍りの加護 | `blessing_dullness` | 266 | 44.4% | 268 | 40 | 40 | 1 | 1 | 0 | 0 |
| 小盾の加護 | `blessing_buckler` | 264 | 44.7% | 266 | 61 | 59 | 10 | 10 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 263 | 41.1% | 268 | 36 | 35 | 1 | 1 | 0 | 0 |
| 追風の加護 | `blessing_tailwind` | 260 | 48.1% | 261 | 55 | 55 | 2 | 2 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 257 | 44.7% | 259 | 52 | 51 | 7 | 7 | 0 | 0 |
| 防の加護 | `blessing_guard` | 255 | 49.0% | 257 | 52 | 51 | 0 | 0 | 0 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | 255 | 41.6% | 258 | 68 | 65 | 13 | 13 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 233 | 49.4% | 238 | 59 | 59 | 19 | 19 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 230 | 50.9% | 230 | 71 | 71 | 11 | 11 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 222 | 45.5% | 225 | 54 | 54 | 10 | 10 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 216 | 47.2% | 219 | 34 | 34 | 35 | 35 | 0 | 0 |
| 速の加護 | `blessing_speed` | 213 | 53.1% | 215 | 41 | 40 | 0 | 0 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 107 | 50.5% | 107 | 30 | 29 | 1 | 1 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 16000 | 4753 | 29.7% | 2128 | 44.8% | 861 |
| `uncommon` | 16000 | 4519 | 28.2% | 2238 | 49.5% | 1286 |
| `rare` | 8000 | 2137 | 26.7% | 1077 | 50.4% | 651 |

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
