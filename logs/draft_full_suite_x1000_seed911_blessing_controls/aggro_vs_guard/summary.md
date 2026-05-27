# Draft Report

## Configuration

- Draft Bot 1: `AggroDraftBot`
- Draft Bot 2: `GuardDraftBot`
- Play Bot 1: `AggroBot`
- Play Bot 2: `GuardBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 5911
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
| `AggroDraftBot` | 1000 | 494 | 447 | 59 | 49.4% | 49.3% | 15.0% | 52.6% | 32.4% | 2.93 | 2.87 | 49.9% | 48.9% | 70.7% | 3.3% | 26.1% | 10.08 | 7.79 | 2.13 | 5.47 | 3.56 | 3.12 | 7.85 | 8 | 8 | 4 |
| `GuardDraftBot` | 1000 | 447 | 494 | 59 | 44.7% | 45.6% | 16.6% | 58.8% | 24.6% | 2.95 | 2.75 | 44.7% | 44.7% | 71.3% | 2.1% | 26.6% | 10.02 | 7.88 | 2.1 | 5.16 | 3.56 | 3.36 | 7.92 | 8 | 8 | 4 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| AggroDraftBot vs GuardDraftBot | 1000 | 59 | `AggroDraftBot`=494, `GuardDraftBot`=447 | 1.6 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 592 |
| 2 | 防御 | 578 |
| 3 | ステップ | 534 |
| 4 | 圧迫 | 482 |
| 5 | 牽制 | 437 |
| 6 | 見定め | 431 |
| 7 | 構え | 422 |
| 8 | 遠眼 | 412 |
| 9 | 公開勝負 | 399 |
| 10 | 集中 | 381 |
| 11 | 貫き | 291 |
| 12 | 崩し | 279 |
| 13 | 踏ん張り | 274 |
| 14 | 踏み込み | 268 |
| 15 | 返し刃 | 263 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 258 |
| 2 | 防御 | 230 |
| 3 | 圧迫 | 228 |
| 4 | ステップ | 228 |
| 5 | 牽制 | 214 |
| 6 | 構え | 197 |
| 7 | 踏み込み | 195 |
| 8 | 貫き | 194 |
| 9 | 崩し | 187 |
| 10 | 見定め | 175 |
| 11 | 公開勝負 | 172 |
| 12 | 遠眼 | 165 |
| 13 | 踏ん張り | 155 |
| 14 | 返し刃 | 145 |
| 15 | 集中 | 143 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 181 |
| 2 | 貫き | 179 |
| 3 | 崩し | 175 |
| 4 | 攻撃 | 173 |
| 5 | ステップ | 134 |
| 6 | 粉砕 | 126 |
| 7 | 大振り | 123 |
| 8 | 防御 | 118 |
| 9 | 渾身 | 115 |
| 10 | 踏ん張り | 101 |
| 11 | 返し刃 | 101 |
| 12 | 強撃 | 93 |
| 13 | 疾走 | 82 |
| 14 | 構え | 79 |
| 15 | 押し込み | 74 |

### Blessing Involvement Overall

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 受け流しの加護 | `blessing_parry` | 293 | 43.0% | 297 | 63 | 62 | 13 | 13 | 0 | 0 |
| 間合いの加護 | `blessing_range` | 285 | 50.5% | 290 | 44 | 44 | 6 | 6 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 281 | 47.7% | 285 | 79 | 78 | 31 | 31 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 281 | 44.5% | 284 | 32 | 32 | 1 | 1 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 276 | 54.0% | 283 | 57 | 57 | 0 | 0 | 0 | 0 |
| 追風の加護 | `blessing_tailwind` | 273 | 46.9% | 278 | 66 | 66 | 7 | 7 | 0 | 0 |
| 小太刀の加護 | `blessing_shortblade` | 257 | 46.3% | 262 | 49 | 48 | 11 | 11 | 0 | 0 |
| 鈍りの加護 | `blessing_dullness` | 256 | 45.3% | 264 | 48 | 47 | 2 | 2 | 0 | 0 |
| 小盾の加護 | `blessing_buckler` | 249 | 49.8% | 252 | 61 | 61 | 16 | 16 | 0 | 0 |
| 速の加護 | `blessing_speed` | 241 | 45.2% | 245 | 55 | 54 | 0 | 0 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 240 | 52.5% | 243 | 74 | 74 | 12 | 12 | 0 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | 237 | 48.1% | 239 | 70 | 70 | 13 | 13 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 231 | 42.0% | 233 | 73 | 70 | 16 | 16 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 229 | 38.9% | 232 | 39 | 39 | 39 | 39 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 223 | 46.6% | 224 | 46 | 44 | 4 | 4 | 0 | 0 |
| 防の加護 | `blessing_guard` | 218 | 51.8% | 220 | 45 | 45 | 1 | 1 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 100 | 39.0% | 100 | 32 | 32 | 0 | 0 | 0 | 0 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `AggroDraftBot` | 2.96 | 0.81 | 1.26 | 1.79 | 0.76 | 1.14 | 158 (15.8%) | 154 (31.2%) |
| `GuardDraftBot` | 2.61 | 0.9 | 1.15 | 1.71 | 0.85 | 0.95 | 154 (15.4%) | 158 (35.3%) |

## Drafter Details

### AggroDraftBot

- Win Rate: 49.4%
- Draw Rate: 5.9%
- First Pass Win Rate: 49.3%
- Win With Fewer Cards: 15.0%
- Win With Same Cards: 52.6%
- Win With More Cards: 32.4%
- Winner Facedown Avg: 2.93
- Loser Facedown Avg: 2.87
- Starting Player Win Rate: 49.9%
- Responding Player Win Rate: 48.9%
- Final Stats Avg: A=2.96, B=0.81, S=1.26
- Losing Final Stats Avg: A=1.79, B=0.76, S=1.14
- Lost With Speed Advantage: 158 (15.8%)
- Won After Blocking Faster Attack: 154 (31.2%)
- Blessing Ended Facedown: 87
- Blessing Placed But Unused: 398
- Opponent Pass / Set+Pass Into Face-Up Blessing: 688
- Win Rate When Forcing Opponent Blessing Use: 44.7%
- Action Rates: set=70.7%, set_pass=3.3%, pass=26.1%
- set_pass Candidate Avg / Match: 15.74
- Turns: min=1, avg=1.6, max=10
- Battle / Control / Blessing: avg=10.08 / 7.79 / 2.13
- Role Colors: red=5.47, blue=3.56, green=3.12, white=7.85
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 1053 |
| 2 | ステップ | 966 |
| 3 | 防御 | 949 |
| 4 | 圧迫 | 830 |
| 5 | 集中 | 717 |
| 6 | 見定め | 711 |
| 7 | 牽制 | 709 |
| 8 | 構え | 703 |
| 9 | 遠眼 | 683 |
| 10 | 公開勝負 | 679 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 512 |
| 2 | ステップ | 479 |
| 3 | 防御 | 467 |
| 4 | 圧迫 | 413 |
| 5 | 構え | 368 |
| 6 | 牽制 | 356 |
| 7 | 公開勝負 | 343 |
| 8 | 遠眼 | 340 |
| 9 | 見定め | 339 |
| 10 | 集中 | 335 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 1053 | 323 | 151 | 98 |
| ステップ | `battle_step` | `common` | 966 | 297 | 139 | 78 |
| 防御 | `battle_defend` | `common` | 949 | 269 | 115 | 57 |
| 圧迫 | `control_pressure` | `common` | 830 | 254 | 128 | 29 |
| 集中 | `control_focus` | `common` | 717 | 193 | 69 | 25 |
| 見定め | `control_peek_own_top` | `common` | 711 | 206 | 88 | 26 |
| 牽制 | `control_disrupt` | `common` | 709 | 241 | 124 | 9 |
| 構え | `control_guard` | `common` | 703 | 197 | 106 | 39 |
| 遠眼 | `control_peek_opponent_top` | `common` | 683 | 181 | 85 | 31 |
| 公開勝負 | `control_opening_expose` | `common` | 679 | 207 | 100 | 39 |
| 崩し | `battle_break` | `uncommon` | 438 | 147 | 99 | 92 |
| 貫き | `battle_pierce` | `uncommon` | 434 | 162 | 114 | 104 |
| 粉砕 | `battle_crush` | `uncommon` | 411 | 135 | 76 | 71 |
| 踏み込み | `battle_step_in` | `rare` | 409 | 152 | 116 | 105 |
| 返し刃 | `battle_counter` | `uncommon` | 374 | 125 | 78 | 50 |
| 大振り | `battle_heavy_swing` | `rare` | 372 | 122 | 74 | 69 |
| 強撃 | `battle_power_attack` | `uncommon` | 369 | 120 | 68 | 55 |
| 踏ん張り | `battle_brace` | `uncommon` | 358 | 129 | 74 | 45 |
| 渾身 | `battle_all_in` | `rare` | 357 | 115 | 62 | 60 |
| 十字受け | `battle_cross_guard` | `uncommon` | 346 | 112 | 66 | 30 |
| 鉄壁 | `battle_wall` | `rare` | 333 | 122 | 60 | 16 |
| 残像 | `battle_afterimage` | `rare` | 326 | 114 | 50 | 31 |
| 押し込み | `battle_press` | `uncommon` | 320 | 102 | 53 | 39 |
| フェイント | `battle_feint` | `uncommon` | 313 | 91 | 33 | 17 |
| Bastion | `battle_bastion` | `uncommon` | 305 | 107 | 55 | 19 |
| 退き足 | `battle_backstep` | `uncommon` | 294 | 82 | 35 | 21 |
| 受け流し | `battle_guard` | `uncommon` | 293 | 106 | 55 | 32 |
| 疾走 | `battle_dash` | `rare` | 291 | 95 | 53 | 35 |
| Bulwark | `battle_bulwark` | `uncommon` | 268 | 95 | 50 | 25 |
| Tripwire | `battle_tripwire` | `rare` | 253 | 3 | 1 | 1 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 249 | 85 | 37 | 17 |
| 受け直し | `control_cover` | `uncommon` | 190 | 60 | 28 | 8 |
| 補強 | `control_fortify` | `uncommon` | 176 | 52 | 25 | 5 |
| 加速 | `control_haste` | `uncommon` | 166 | 43 | 25 | 8 |
| 迷い手 | `control_hand_echo` | `uncommon` | 165 | 54 | 32 | 13 |
| 前のめり | `control_overclock` | `uncommon` | 164 | 53 | 27 | 11 |
| 間合いの加護 | `blessing_range` | `uncommon` | 163 | 27 | 10 | 0 |
| 看破 | `control_opening_read` | `uncommon` | 159 | 41 | 12 | 6 |
| 攻勢の加護 | `blessing_offense` | `rare` | 157 | 41 | 22 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 156 | 54 | 20 | 5 |
| 受け流しの加護 | `blessing_parry` | `uncommon` | 156 | 33 | 14 | 0 |
| 探り | `control_peek_hand` | `uncommon` | 146 | 44 | 15 | 5 |
| 穢れ | `control_defile` | `uncommon` | 142 | 5 | 2 | 0 |
| 祓い直し | `control_discard_facedown_blessing` | `uncommon` | 141 | 5 | 1 | 0 |
| Blank First | `control_blank_first` | `uncommon` | 140 | 47 | 18 | 1 |
| 重心落とし | `control_anchor` | `uncommon` | 140 | 36 | 17 | 8 |
| 追風の加護 | `blessing_tailwind` | `uncommon` | 140 | 32 | 17 | 0 |
| 攻の加護 | `blessing_attack` | `rare` | 139 | 31 | 19 | 0 |
| 小太刀の加護 | `blessing_shortblade` | `uncommon` | 139 | 18 | 9 | 0 |
| 抑制の加護 | `blessing_suppression` | `rare` | 137 | 23 | 9 | 0 |
| 封祈 | `control_blessing_lock` | `uncommon` | 137 | 5 | 3 | 1 |
| 速の加護 | `blessing_speed` | `rare` | 127 | 38 | 18 | 0 |
| 鈍りの加護 | `blessing_dullness` | `uncommon` | 127 | 23 | 12 | 0 |
| 前借り | `control_all_in_focus` | `uncommon` | 126 | 28 | 14 | 5 |
| 小盾の加護 | `blessing_buckler` | `uncommon` | 124 | 24 | 12 | 0 |
| 手繰り直し | `control_redraw_hand` | `uncommon` | 120 | 4 | 1 | 1 |
| 罠糸の加護 | `blessing_trap_web` | `rare` | 118 | 36 | 22 | 0 |
| 防の加護 | `blessing_guard` | `rare` | 118 | 24 | 15 | 0 |
| 鈍足の加護 | `blessing_slow` | `rare` | 115 | 27 | 15 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | `uncommon` | 111 | 33 | 16 | 0 |
| Crush Spirit | `control_crush_spirit` | `rare` | 104 | 30 | 21 | 0 |
| 見切りの加護 | `blessing_insight` | `rare` | 102 | 20 | 8 | 0 |
| 蓄え | `control_reserve` | `rare` | 101 | 43 | 19 | 1 |
| 防壁の加護 | `blessing_barrier` | `rare` | 100 | 28 | 13 | 0 |
| 先触れ | `control_topdeck_hand` | `rare` | 99 | 24 | 8 | 2 |
| 転祈 | `control_blessing_flip` | `rare` | 93 | 6 | 1 | 0 |
| 破祈 | `control_blessing_break` | `rare` | 89 | 6 | 2 | 0 |
| 知恵の加護 | `blessing_draw` | `rare` | 60 | 17 | 3 | 0 |

### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 間合いの加護 | `blessing_range` | 161 | 57.8% | 163 | 27 | 27 | 3 | 3 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 154 | 48.7% | 157 | 41 | 41 | 18 | 18 | 0 | 0 |
| 受け流しの加護 | `blessing_parry` | 154 | 47.4% | 156 | 33 | 32 | 6 | 6 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 139 | 56.8% | 139 | 31 | 31 | 0 | 0 | 0 | 0 |
| 追風の加護 | `blessing_tailwind` | 137 | 54.0% | 140 | 32 | 32 | 3 | 3 | 0 | 0 |
| 小太刀の加護 | `blessing_shortblade` | 137 | 51.8% | 139 | 18 | 17 | 3 | 3 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 135 | 43.7% | 137 | 23 | 23 | 0 | 0 | 0 | 0 |
| 小盾の加護 | `blessing_buckler` | 123 | 53.7% | 124 | 24 | 24 | 8 | 8 | 0 | 0 |
| 速の加護 | `blessing_speed` | 123 | 48.8% | 127 | 38 | 37 | 0 | 0 | 0 | 0 |
| 鈍りの加護 | `blessing_dullness` | 122 | 48.4% | 127 | 23 | 23 | 0 | 0 | 0 | 0 |
| 防の加護 | `blessing_guard` | 117 | 56.4% | 118 | 24 | 24 | 1 | 1 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 117 | 52.1% | 118 | 36 | 36 | 5 | 5 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 114 | 48.2% | 115 | 27 | 25 | 2 | 2 | 0 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | 109 | 54.1% | 111 | 33 | 33 | 8 | 8 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 102 | 39.2% | 102 | 20 | 20 | 20 | 20 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 99 | 43.4% | 100 | 28 | 27 | 4 | 4 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 60 | 31.7% | 60 | 17 | 17 | 0 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 8000 | 2368 | 29.6% | 1105 | 46.7% | 431 |
| `uncommon` | 8000 | 2319 | 29.0% | 1223 | 52.7% | 694 |
| `rare` | 4000 | 1117 | 27.9% | 611 | 54.7% | 320 |

#### Match Logs

- [draft_match_0001](matches/match_0001_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0002](matches/match_0002_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0003](matches/match_0003_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0004](matches/match_0004_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0005](matches/match_0005_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0006](matches/match_0006_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0007](matches/match_0007_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0008](matches/match_0008_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0009](matches/match_0009_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0010](matches/match_0010_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0011](matches/match_0011_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0012](matches/match_0012_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0013](matches/match_0013_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0014](matches/match_0014_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0015](matches/match_0015_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0016](matches/match_0016_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0017](matches/match_0017_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0018](matches/match_0018_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0019](matches/match_0019_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0020](matches/match_0020_GuardDraftBot_vs_AggroDraftBot.md)

### GuardDraftBot

- Win Rate: 44.7%
- Draw Rate: 5.9%
- First Pass Win Rate: 45.6%
- Win With Fewer Cards: 16.6%
- Win With Same Cards: 58.8%
- Win With More Cards: 24.6%
- Winner Facedown Avg: 2.95
- Loser Facedown Avg: 2.75
- Starting Player Win Rate: 44.7%
- Responding Player Win Rate: 44.7%
- Final Stats Avg: A=2.61, B=0.9, S=1.15
- Losing Final Stats Avg: A=1.71, B=0.85, S=0.95
- Lost With Speed Advantage: 154 (15.4%)
- Won After Blocking Faster Attack: 158 (35.3%)
- Blessing Ended Facedown: 92
- Blessing Placed But Unused: 372
- Opponent Pass / Set+Pass Into Face-Up Blessing: 639
- Win Rate When Forcing Opponent Blessing Use: 33.8%
- Action Rates: set=71.3%, set_pass=2.1%, pass=26.6%
- set_pass Candidate Avg / Match: 15.74
- Turns: min=1, avg=1.6, max=10
- Battle / Control / Blessing: avg=10.02 / 7.88 / 2.1
- Role Colors: red=5.16, blue=3.56, green=3.36, white=7.92
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 防御 | 1003 |
| 2 | 攻撃 | 982 |
| 3 | ステップ | 895 |
| 4 | 圧迫 | 791 |
| 5 | 構え | 790 |
| 6 | 遠眼 | 752 |
| 7 | 集中 | 710 |
| 8 | 見定め | 695 |
| 9 | 公開勝負 | 691 |
| 10 | 牽制 | 691 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 440 |
| 2 | 防御 | 438 |
| 3 | ステップ | 386 |
| 4 | 圧迫 | 372 |
| 5 | 構え | 357 |
| 6 | 遠眼 | 336 |
| 7 | 公開勝負 | 322 |
| 8 | 集中 | 318 |
| 9 | 牽制 | 314 |
| 10 | 見定め | 293 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 防御 | `battle_defend` | `common` | 1003 | 309 | 115 | 61 |
| 攻撃 | `battle_attack` | `common` | 982 | 269 | 107 | 75 |
| ステップ | `battle_step` | `common` | 895 | 237 | 89 | 56 |
| 圧迫 | `control_pressure` | `common` | 791 | 228 | 100 | 28 |
| 構え | `control_guard` | `common` | 790 | 225 | 91 | 40 |
| 遠眼 | `control_peek_opponent_top` | `common` | 752 | 231 | 80 | 14 |
| 集中 | `control_focus` | `common` | 710 | 188 | 74 | 39 |
| 見定め | `control_peek_own_top` | `common` | 695 | 225 | 87 | 25 |
| 牽制 | `control_disrupt` | `common` | 691 | 196 | 90 | 8 |
| 公開勝負 | `control_opening_expose` | `common` | 691 | 192 | 72 | 31 |
| 貫き | `battle_pierce` | `uncommon` | 417 | 129 | 80 | 75 |
| 崩し | `battle_break` | `uncommon` | 405 | 132 | 88 | 83 |
| 十字受け | `battle_cross_guard` | `uncommon` | 392 | 140 | 63 | 35 |
| 踏ん張り | `battle_brace` | `uncommon` | 390 | 145 | 81 | 56 |
| 渾身 | `battle_all_in` | `rare` | 383 | 133 | 57 | 55 |
| 踏み込み | `battle_step_in` | `rare` | 373 | 116 | 79 | 76 |
| 返し刃 | `battle_counter` | `uncommon` | 365 | 138 | 67 | 51 |
| 鉄壁 | `battle_wall` | `rare` | 359 | 124 | 56 | 18 |
| Bastion | `battle_bastion` | `uncommon` | 348 | 127 | 54 | 24 |
| 粉砕 | `battle_crush` | `uncommon` | 343 | 103 | 62 | 55 |
| 押し込み | `battle_press` | `uncommon` | 331 | 104 | 51 | 35 |
| 大振り | `battle_heavy_swing` | `rare` | 328 | 108 | 59 | 54 |
| 残像 | `battle_afterimage` | `rare` | 319 | 120 | 46 | 26 |
| Bulwark | `battle_bulwark` | `uncommon` | 316 | 112 | 52 | 25 |
| 退き足 | `battle_backstep` | `uncommon` | 313 | 96 | 31 | 18 |
| フェイント | `battle_feint` | `uncommon` | 310 | 92 | 41 | 30 |
| 疾走 | `battle_dash` | `rare` | 303 | 98 | 54 | 47 |
| 強撃 | `battle_power_attack` | `uncommon` | 301 | 91 | 47 | 38 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 292 | 105 | 40 | 22 |
| 受け流し | `battle_guard` | `uncommon` | 283 | 90 | 41 | 27 |
| Tripwire | `battle_tripwire` | `rare` | 269 | 1 | 1 | 1 |
| 受け直し | `control_cover` | `uncommon` | 191 | 55 | 20 | 6 |
| 前のめり | `control_overclock` | `uncommon` | 185 | 53 | 30 | 13 |
| 重心落とし | `control_anchor` | `uncommon` | 183 | 54 | 27 | 16 |
| 勢い溜め | `control_momentum` | `uncommon` | 163 | 51 | 18 | 5 |
| 迷い手 | `control_hand_echo` | `uncommon` | 153 | 43 | 17 | 7 |
| 補強 | `control_fortify` | `uncommon` | 152 | 55 | 27 | 6 |
| 抑制の加護 | `blessing_suppression` | `rare` | 147 | 9 | 5 | 0 |
| 攻の加護 | `blessing_attack` | `rare` | 144 | 26 | 16 | 0 |
| Blank First | `control_blank_first` | `uncommon` | 143 | 52 | 21 | 2 |
| 看破 | `control_opening_read` | `uncommon` | 142 | 51 | 19 | 8 |
| 封祈 | `control_blessing_lock` | `uncommon` | 142 | 9 | 3 | 1 |
| 前借り | `control_all_in_focus` | `uncommon` | 141 | 33 | 11 | 5 |
| 受け流しの加護 | `blessing_parry` | `uncommon` | 141 | 30 | 11 | 0 |
| 探り | `control_peek_hand` | `uncommon` | 140 | 49 | 17 | 6 |
| 手繰り直し | `control_redraw_hand` | `uncommon` | 140 | 24 | 3 | 1 |
| 追風の加護 | `blessing_tailwind` | `uncommon` | 138 | 34 | 16 | 0 |
| 祓い直し | `control_discard_facedown_blessing` | `uncommon` | 138 | 1 | 0 | 0 |
| 鈍りの加護 | `blessing_dullness` | `uncommon` | 137 | 25 | 10 | 0 |
| 防壁の加護 | `blessing_barrier` | `rare` | 133 | 45 | 20 | 0 |
| 見切りの加護 | `blessing_insight` | `rare` | 130 | 19 | 6 | 0 |
| 穢れ | `control_defile` | `uncommon` | 130 | 9 | 1 | 0 |
| 加速 | `control_haste` | `uncommon` | 129 | 38 | 19 | 8 |
| 攻勢の加護 | `blessing_offense` | `rare` | 128 | 38 | 19 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | `uncommon` | 128 | 37 | 17 | 0 |
| 小盾の加護 | `blessing_buckler` | `uncommon` | 128 | 37 | 8 | 0 |
| 間合いの加護 | `blessing_range` | `uncommon` | 127 | 17 | 7 | 0 |
| 罠糸の加護 | `blessing_trap_web` | `rare` | 125 | 38 | 19 | 0 |
| 小太刀の加護 | `blessing_shortblade` | `uncommon` | 123 | 31 | 13 | 0 |
| 速の加護 | `blessing_speed` | `rare` | 118 | 17 | 4 | 0 |
| 鈍足の加護 | `blessing_slow` | `rare` | 109 | 19 | 8 | 0 |
| 破祈 | `control_blessing_break` | `rare` | 104 | 7 | 3 | 1 |
| 防の加護 | `blessing_guard` | `rare` | 102 | 21 | 12 | 0 |
| 蓄え | `control_reserve` | `rare` | 101 | 40 | 13 | 1 |
| 先触れ | `control_topdeck_hand` | `rare` | 101 | 25 | 5 | 2 |
| Crush Spirit | `control_crush_spirit` | `rare` | 100 | 42 | 20 | 0 |
| 転祈 | `control_blessing_flip` | `rare` | 84 | 8 | 4 | 1 |
| 知恵の加護 | `blessing_draw` | `rare` | 40 | 15 | 6 | 0 |

### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 抑制の加護 | `blessing_suppression` | 146 | 45.2% | 147 | 9 | 9 | 1 | 1 | 0 | 0 |
| 受け流しの加護 | `blessing_parry` | 139 | 38.1% | 141 | 30 | 30 | 7 | 7 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 137 | 51.1% | 144 | 26 | 26 | 0 | 0 | 0 | 0 |
| 追風の加護 | `blessing_tailwind` | 136 | 39.7% | 138 | 34 | 34 | 4 | 4 | 0 | 0 |
| 鈍りの加護 | `blessing_dullness` | 134 | 42.5% | 137 | 25 | 24 | 2 | 2 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 132 | 40.9% | 133 | 45 | 43 | 12 | 12 | 0 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | 128 | 43.0% | 128 | 37 | 37 | 5 | 5 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 127 | 46.5% | 128 | 38 | 37 | 13 | 13 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 127 | 38.6% | 130 | 19 | 19 | 19 | 19 | 0 | 0 |
| 小盾の加護 | `blessing_buckler` | 126 | 46.0% | 128 | 37 | 37 | 8 | 8 | 0 | 0 |
| 間合いの加護 | `blessing_range` | 124 | 41.1% | 127 | 17 | 17 | 3 | 3 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 123 | 52.8% | 125 | 38 | 38 | 7 | 7 | 0 | 0 |
| 小太刀の加護 | `blessing_shortblade` | 120 | 40.0% | 123 | 31 | 31 | 8 | 8 | 0 | 0 |
| 速の加護 | `blessing_speed` | 118 | 41.5% | 118 | 17 | 17 | 0 | 0 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 109 | 45.0% | 109 | 19 | 19 | 2 | 2 | 0 | 0 |
| 防の加護 | `blessing_guard` | 101 | 46.5% | 102 | 21 | 21 | 0 | 0 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 40 | 50.0% | 40 | 15 | 15 | 0 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 8000 | 2300 | 28.7% | 905 | 39.3% | 377 |
| `uncommon` | 8000 | 2392 | 29.9% | 1113 | 46.5% | 658 |
| `rare` | 4000 | 1069 | 26.7% | 512 | 47.9% | 282 |

#### Match Logs

- [draft_match_0001](matches/match_0001_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0002](matches/match_0002_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0003](matches/match_0003_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0004](matches/match_0004_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0005](matches/match_0005_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0006](matches/match_0006_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0007](matches/match_0007_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0008](matches/match_0008_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0009](matches/match_0009_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0010](matches/match_0010_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0011](matches/match_0011_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0012](matches/match_0012_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0013](matches/match_0013_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0014](matches/match_0014_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0015](matches/match_0015_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0016](matches/match_0016_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0017](matches/match_0017_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0018](matches/match_0018_GuardDraftBot_vs_AggroDraftBot.md)
- [draft_match_0019](matches/match_0019_AggroDraftBot_vs_GuardDraftBot.md)
- [draft_match_0020](matches/match_0020_GuardDraftBot_vs_AggroDraftBot.md)
