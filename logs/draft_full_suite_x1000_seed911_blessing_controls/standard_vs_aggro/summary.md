# Draft Report

## Configuration

- Draft Bot 1: `StandardDraftBot`
- Draft Bot 2: `AggroDraftBot`
- Play Bot 1: `StandardBot`
- Play Bot 2: `AggroBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 2911
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
| `AggroDraftBot` | 1000 | 475 | 473 | 52 | 47.5% | 49.9% | 18.1% | 50.9% | 30.9% | 2.99 | 2.71 | 45.1% | 50.1% | 70.8% | 2.5% | 26.7% | 10.09 | 7.82 | 2.09 | 5.38 | 3.61 | 3.13 | 7.88 | 8 | 8 | 4 |
| `StandardDraftBot` | 1000 | 473 | 475 | 52 | 47.3% | 49.5% | 15.2% | 52.9% | 31.9% | 2.88 | 2.86 | 45.3% | 49.1% | 70.8% | 2.3% | 26.9% | 10.06 | 7.8 | 2.13 | 5.31 | 3.58 | 3.24 | 7.87 | 8 | 8 | 4 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| AggroDraftBot vs StandardDraftBot | 1000 | 52 | `AggroDraftBot`=475, `StandardDraftBot`=473 | 1.56 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 610 |
| 2 | ステップ | 553 |
| 3 | 防御 | 544 |
| 4 | 圧迫 | 478 |
| 5 | 牽制 | 461 |
| 6 | 見定め | 440 |
| 7 | 公開勝負 | 416 |
| 8 | 遠眼 | 414 |
| 9 | 構え | 400 |
| 10 | 集中 | 378 |
| 11 | 踏ん張り | 266 |
| 12 | 崩し | 263 |
| 13 | 貫き | 260 |
| 14 | 渾身 | 254 |
| 15 | 鉄壁 | 254 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 283 |
| 2 | ステップ | 254 |
| 3 | 防御 | 244 |
| 4 | 牽制 | 218 |
| 5 | 圧迫 | 205 |
| 6 | 踏み込み | 187 |
| 7 | 貫き | 187 |
| 8 | 崩し | 172 |
| 9 | 構え | 171 |
| 10 | 見定め | 166 |
| 11 | 遠眼 | 165 |
| 12 | 集中 | 164 |
| 13 | 公開勝負 | 160 |
| 14 | 返し刃 | 141 |
| 15 | 踏ん張り | 141 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 215 |
| 2 | 踏み込み | 180 |
| 3 | 貫き | 167 |
| 4 | 崩し | 160 |
| 5 | ステップ | 154 |
| 6 | 渾身 | 129 |
| 7 | 防御 | 125 |
| 8 | 粉砕 | 116 |
| 9 | 大振り | 116 |
| 10 | 返し刃 | 111 |
| 11 | 強撃 | 108 |
| 12 | 疾走 | 96 |
| 13 | 踏ん張り | 93 |
| 14 | 十字受け | 70 |
| 15 | 残像 | 67 |

### Blessing Involvement Overall

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 小太刀の加護 | `blessing_shortblade` | 281 | 41.6% | 285 | 48 | 48 | 9 | 9 | 0 | 0 |
| 受け流しの加護 | `blessing_parry` | 272 | 47.4% | 278 | 73 | 71 | 13 | 13 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 268 | 47.8% | 268 | 45 | 44 | 1 | 1 | 0 | 0 |
| 追風の加護 | `blessing_tailwind` | 268 | 43.7% | 274 | 52 | 52 | 0 | 0 | 0 | 0 |
| 小盾の加護 | `blessing_buckler` | 265 | 48.3% | 270 | 45 | 44 | 6 | 6 | 0 | 0 |
| 鈍りの加護 | `blessing_dullness` | 261 | 48.7% | 268 | 45 | 45 | 3 | 3 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 261 | 41.8% | 264 | 75 | 74 | 26 | 26 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 258 | 45.3% | 264 | 57 | 56 | 0 | 0 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 254 | 47.2% | 254 | 57 | 56 | 6 | 6 | 0 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | 252 | 47.2% | 259 | 48 | 47 | 10 | 10 | 0 | 0 |
| 間合いの加護 | `blessing_range` | 250 | 45.6% | 252 | 37 | 37 | 4 | 4 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 245 | 49.0% | 246 | 72 | 71 | 24 | 24 | 0 | 0 |
| 防の加護 | `blessing_guard` | 234 | 48.7% | 236 | 46 | 45 | 1 | 1 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 232 | 40.5% | 233 | 32 | 32 | 32 | 32 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 226 | 46.9% | 227 | 79 | 77 | 13 | 13 | 0 | 0 |
| 速の加護 | `blessing_speed` | 224 | 46.0% | 225 | 61 | 60 | 2 | 2 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 123 | 43.9% | 123 | 35 | 35 | 0 | 0 | 0 | 0 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `AggroDraftBot` | 2.91 | 0.83 | 1.15 | 1.9 | 0.78 | 0.84 | 142 (14.2%) | 154 (32.4%) |
| `StandardDraftBot` | 2.65 | 0.92 | 1.23 | 1.74 | 0.87 | 1.14 | 154 (15.4%) | 142 (30.0%) |

## Drafter Details

### AggroDraftBot

- Win Rate: 47.5%
- Draw Rate: 5.2%
- First Pass Win Rate: 49.9%
- Win With Fewer Cards: 18.1%
- Win With Same Cards: 50.9%
- Win With More Cards: 30.9%
- Winner Facedown Avg: 2.99
- Loser Facedown Avg: 2.71
- Starting Player Win Rate: 45.1%
- Responding Player Win Rate: 50.1%
- Final Stats Avg: A=2.91, B=0.83, S=1.15
- Losing Final Stats Avg: A=1.9, B=0.78, S=0.84
- Lost With Speed Advantage: 142 (14.2%)
- Won After Blocking Faster Attack: 154 (32.4%)
- Blessing Ended Facedown: 67
- Blessing Placed But Unused: 390
- Opponent Pass / Set+Pass Into Face-Up Blessing: 656
- Win Rate When Forcing Opponent Blessing Use: 40.5%
- Action Rates: set=70.8%, set_pass=2.5%, pass=26.7%
- set_pass Candidate Avg / Match: 14.68
- Turns: min=1, avg=1.56, max=9
- Battle / Control / Blessing: avg=10.09 / 7.82 / 2.09
- Role Colors: red=5.38, blue=3.61, green=3.13, white=7.88
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 1041 |
| 2 | ステップ | 984 |
| 3 | 防御 | 915 |
| 4 | 圧迫 | 795 |
| 5 | 集中 | 733 |
| 6 | 牽制 | 728 |
| 7 | 遠眼 | 713 |
| 8 | 構え | 711 |
| 9 | 見定め | 698 |
| 10 | 公開勝負 | 682 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 509 |
| 2 | ステップ | 487 |
| 3 | 防御 | 434 |
| 4 | 圧迫 | 383 |
| 5 | 牽制 | 360 |
| 6 | 集中 | 344 |
| 7 | 遠眼 | 338 |
| 8 | 構え | 327 |
| 9 | 公開勝負 | 309 |
| 10 | 見定め | 309 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 1041 | 321 | 142 | 113 |
| ステップ | `battle_step` | `common` | 984 | 266 | 121 | 77 |
| 防御 | `battle_defend` | `common` | 915 | 278 | 122 | 64 |
| 圧迫 | `control_pressure` | `common` | 795 | 247 | 108 | 29 |
| 集中 | `control_focus` | `common` | 733 | 196 | 81 | 33 |
| 牽制 | `control_disrupt` | `common` | 728 | 234 | 102 | 10 |
| 遠眼 | `control_peek_opponent_top` | `common` | 713 | 207 | 76 | 23 |
| 構え | `control_guard` | `common` | 711 | 196 | 69 | 27 |
| 見定め | `control_peek_own_top` | `common` | 698 | 204 | 67 | 15 |
| 公開勝負 | `control_opening_expose` | `common` | 682 | 199 | 74 | 29 |
| 崩し | `battle_break` | `uncommon` | 442 | 133 | 91 | 89 |
| 貫き | `battle_pierce` | `uncommon` | 421 | 124 | 96 | 86 |
| 粉砕 | `battle_crush` | `uncommon` | 401 | 125 | 58 | 50 |
| 踏み込み | `battle_step_in` | `rare` | 400 | 129 | 101 | 96 |
| 強撃 | `battle_power_attack` | `uncommon` | 380 | 137 | 71 | 63 |
| 踏ん張り | `battle_brace` | `uncommon` | 375 | 128 | 65 | 44 |
| 返し刃 | `battle_counter` | `uncommon` | 365 | 119 | 67 | 57 |
| 大振り | `battle_heavy_swing` | `rare` | 362 | 125 | 64 | 59 |
| 残像 | `battle_afterimage` | `rare` | 359 | 124 | 57 | 39 |
| 渾身 | `battle_all_in` | `rare` | 354 | 128 | 71 | 67 |
| フェイント | `battle_feint` | `uncommon` | 341 | 90 | 41 | 17 |
| 退き足 | `battle_backstep` | `uncommon` | 327 | 103 | 39 | 21 |
| 押し込み | `battle_press` | `uncommon` | 319 | 100 | 47 | 35 |
| 十字受け | `battle_cross_guard` | `uncommon` | 315 | 120 | 62 | 39 |
| 鉄壁 | `battle_wall` | `rare` | 310 | 108 | 48 | 18 |
| 疾走 | `battle_dash` | `rare` | 305 | 92 | 54 | 47 |
| Bastion | `battle_bastion` | `uncommon` | 293 | 93 | 40 | 19 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 286 | 97 | 53 | 23 |
| 受け流し | `battle_guard` | `uncommon` | 283 | 83 | 40 | 29 |
| Bulwark | `battle_bulwark` | `uncommon` | 271 | 94 | 50 | 28 |
| Tripwire | `battle_tripwire` | `rare` | 241 | 0 | 0 | 0 |
| 受け直し | `control_cover` | `uncommon` | 186 | 62 | 35 | 10 |
| 前のめり | `control_overclock` | `uncommon` | 180 | 57 | 23 | 13 |
| 手繰り直し | `control_redraw_hand` | `uncommon` | 169 | 9 | 3 | 0 |
| 探り | `control_peek_hand` | `uncommon` | 156 | 48 | 16 | 4 |
| 重心落とし | `control_anchor` | `uncommon` | 152 | 52 | 21 | 11 |
| 前借り | `control_all_in_focus` | `uncommon` | 151 | 25 | 5 | 1 |
| 受け流しの加護 | `blessing_parry` | `uncommon` | 148 | 40 | 13 | 0 |
| 抑制の加護 | `blessing_suppression` | `rare` | 146 | 30 | 11 | 0 |
| 補強 | `control_fortify` | `uncommon` | 144 | 38 | 21 | 1 |
| 穢れ | `control_defile` | `uncommon` | 143 | 14 | 6 | 0 |
| 封祈 | `control_blessing_lock` | `uncommon` | 143 | 5 | 2 | 0 |
| 看破 | `control_opening_read` | `uncommon` | 141 | 42 | 18 | 7 |
| 迷い手 | `control_hand_echo` | `uncommon` | 141 | 36 | 13 | 3 |
| 加速 | `control_haste` | `uncommon` | 140 | 42 | 18 | 7 |
| 鈍りの加護 | `blessing_dullness` | `uncommon` | 140 | 24 | 12 | 0 |
| 祓い直し | `control_discard_facedown_blessing` | `uncommon` | 139 | 5 | 1 | 0 |
| 小盾の加護 | `blessing_buckler` | `uncommon` | 137 | 19 | 10 | 0 |
| 小太刀の加護 | `blessing_shortblade` | `uncommon` | 134 | 21 | 12 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 131 | 43 | 17 | 6 |
| 追風の加護 | `blessing_tailwind` | `uncommon` | 130 | 36 | 10 | 0 |
| Blank First | `control_blank_first` | `uncommon` | 129 | 52 | 27 | 1 |
| 踏み止まりの加護 | `blessing_laststand` | `uncommon` | 129 | 20 | 9 | 0 |
| 攻勢の加護 | `blessing_offense` | `rare` | 127 | 35 | 10 | 0 |
| 防壁の加護 | `blessing_barrier` | `rare` | 124 | 33 | 15 | 0 |
| 鈍足の加護 | `blessing_slow` | `rare` | 123 | 22 | 7 | 0 |
| 速の加護 | `blessing_speed` | `rare` | 118 | 34 | 14 | 0 |
| 間合いの加護 | `blessing_range` | `uncommon` | 118 | 22 | 8 | 0 |
| 攻の加護 | `blessing_attack` | `rare` | 118 | 21 | 13 | 0 |
| 罠糸の加護 | `blessing_trap_web` | `rare` | 116 | 42 | 23 | 0 |
| 防の加護 | `blessing_guard` | `rare` | 115 | 23 | 12 | 0 |
| Crush Spirit | `control_crush_spirit` | `rare` | 114 | 37 | 27 | 1 |
| 見切りの加護 | `blessing_insight` | `rare` | 111 | 15 | 4 | 0 |
| 破祈 | `control_blessing_break` | `rare` | 111 | 10 | 6 | 2 |
| 転祈 | `control_blessing_flip` | `rare` | 108 | 8 | 3 | 1 |
| 蓄え | `control_reserve` | `rare` | 93 | 34 | 10 | 2 |
| 先触れ | `control_topdeck_hand` | `rare` | 86 | 25 | 13 | 4 |
| 知恵の加護 | `blessing_draw` | `rare` | 59 | 16 | 4 | 0 |

### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 抑制の加護 | `blessing_suppression` | 146 | 47.9% | 146 | 30 | 29 | 1 | 1 | 0 | 0 |
| 受け流しの加護 | `blessing_parry` | 146 | 41.1% | 148 | 40 | 39 | 6 | 6 | 0 | 0 |
| 鈍りの加護 | `blessing_dullness` | 137 | 48.9% | 140 | 24 | 24 | 3 | 3 | 0 | 0 |
| 小盾の加護 | `blessing_buckler` | 134 | 48.5% | 137 | 19 | 19 | 3 | 3 | 0 | 0 |
| 小太刀の加護 | `blessing_shortblade` | 132 | 45.5% | 134 | 21 | 21 | 3 | 3 | 0 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | 127 | 44.1% | 129 | 20 | 19 | 4 | 4 | 0 | 0 |
| 追風の加護 | `blessing_tailwind` | 126 | 45.2% | 130 | 36 | 36 | 0 | 0 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 125 | 36.8% | 127 | 35 | 35 | 10 | 10 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 123 | 46.3% | 124 | 33 | 33 | 12 | 12 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 123 | 39.8% | 123 | 22 | 21 | 0 | 0 | 0 | 0 |
| 間合いの加護 | `blessing_range` | 118 | 42.4% | 118 | 22 | 22 | 2 | 2 | 0 | 0 |
| 速の加護 | `blessing_speed` | 117 | 47.9% | 118 | 34 | 33 | 1 | 1 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 117 | 44.4% | 118 | 21 | 21 | 0 | 0 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 115 | 51.3% | 116 | 42 | 41 | 7 | 7 | 0 | 0 |
| 防の加護 | `blessing_guard` | 115 | 51.3% | 115 | 23 | 23 | 1 | 1 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 110 | 38.2% | 111 | 15 | 15 | 16 | 16 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 59 | 42.4% | 59 | 16 | 16 | 0 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 8000 | 2348 | 29.3% | 962 | 41.0% | 420 |
| `uncommon` | 8000 | 2258 | 28.2% | 1120 | 49.6% | 664 |
| `rare` | 4000 | 1091 | 27.3% | 567 | 52.0% | 336 |

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

- Win Rate: 47.3%
- Draw Rate: 5.2%
- First Pass Win Rate: 49.5%
- Win With Fewer Cards: 15.2%
- Win With Same Cards: 52.9%
- Win With More Cards: 31.9%
- Winner Facedown Avg: 2.88
- Loser Facedown Avg: 2.86
- Starting Player Win Rate: 45.3%
- Responding Player Win Rate: 49.1%
- Final Stats Avg: A=2.65, B=0.92, S=1.23
- Losing Final Stats Avg: A=1.74, B=0.87, S=1.14
- Lost With Speed Advantage: 154 (15.4%)
- Won After Blocking Faster Attack: 142 (30.0%)
- Blessing Ended Facedown: 87
- Blessing Placed But Unused: 373
- Opponent Pass / Set+Pass Into Face-Up Blessing: 614
- Win Rate When Forcing Opponent Blessing Use: 53.2%
- Action Rates: set=70.8%, set_pass=2.3%, pass=26.9%
- set_pass Candidate Avg / Match: 14.68
- Turns: min=1, avg=1.56, max=9
- Battle / Control / Blessing: avg=10.06 / 7.8 / 2.13
- Role Colors: red=5.31, blue=3.58, green=3.24, white=7.87
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 1018 |
| 2 | 防御 | 931 |
| 3 | ステップ | 914 |
| 4 | 圧迫 | 780 |
| 5 | 集中 | 757 |
| 6 | 構え | 743 |
| 7 | 公開勝負 | 731 |
| 8 | 見定め | 729 |
| 9 | 牽制 | 700 |
| 10 | 遠眼 | 697 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 476 |
| 2 | 防御 | 450 |
| 3 | ステップ | 432 |
| 4 | 集中 | 370 |
| 5 | 圧迫 | 368 |
| 6 | 構え | 345 |
| 7 | 牽制 | 344 |
| 8 | 遠眼 | 344 |
| 9 | 見定め | 331 |
| 10 | 公開勝負 | 324 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 1018 | 289 | 141 | 102 |
| 防御 | `battle_defend` | `common` | 931 | 266 | 122 | 61 |
| ステップ | `battle_step` | `common` | 914 | 287 | 133 | 77 |
| 圧迫 | `control_pressure` | `common` | 780 | 231 | 97 | 16 |
| 集中 | `control_focus` | `common` | 757 | 182 | 83 | 31 |
| 構え | `control_guard` | `common` | 743 | 204 | 102 | 35 |
| 公開勝負 | `control_opening_expose` | `common` | 731 | 217 | 86 | 30 |
| 見定め | `control_peek_own_top` | `common` | 729 | 236 | 99 | 33 |
| 牽制 | `control_disrupt` | `common` | 700 | 227 | 116 | 8 |
| 遠眼 | `control_peek_opponent_top` | `common` | 697 | 207 | 89 | 24 |
| 崩し | `battle_break` | `uncommon` | 426 | 130 | 81 | 71 |
| 返し刃 | `battle_counter` | `uncommon` | 415 | 134 | 74 | 54 |
| 貫き | `battle_pierce` | `uncommon` | 410 | 136 | 91 | 81 |
| 踏ん張り | `battle_brace` | `uncommon` | 381 | 138 | 76 | 49 |
| 渾身 | `battle_all_in` | `rare` | 381 | 126 | 63 | 62 |
| 粉砕 | `battle_crush` | `uncommon` | 378 | 116 | 74 | 66 |
| Bastion | `battle_bastion` | `uncommon` | 377 | 135 | 65 | 25 |
| 踏み込み | `battle_step_in` | `rare` | 369 | 120 | 86 | 84 |
| 鉄壁 | `battle_wall` | `rare` | 363 | 146 | 63 | 29 |
| フェイント | `battle_feint` | `uncommon` | 356 | 114 | 41 | 22 |
| 残像 | `battle_afterimage` | `rare` | 349 | 120 | 58 | 28 |
| 大振り | `battle_heavy_swing` | `rare` | 341 | 111 | 61 | 57 |
| 十字受け | `battle_cross_guard` | `uncommon` | 329 | 116 | 52 | 31 |
| 押し込み | `battle_press` | `uncommon` | 325 | 89 | 42 | 26 |
| 退き足 | `battle_backstep` | `uncommon` | 315 | 100 | 43 | 21 |
| 強撃 | `battle_power_attack` | `uncommon` | 309 | 96 | 55 | 45 |
| 疾走 | `battle_dash` | `rare` | 284 | 97 | 55 | 49 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 278 | 87 | 36 | 15 |
| 受け流し | `battle_guard` | `uncommon` | 274 | 85 | 45 | 24 |
| Tripwire | `battle_tripwire` | `rare` | 272 | 3 | 3 | 3 |
| Bulwark | `battle_bulwark` | `uncommon` | 270 | 84 | 45 | 21 |
| 受け直し | `control_cover` | `uncommon` | 209 | 77 | 47 | 10 |
| 前のめり | `control_overclock` | `uncommon` | 168 | 50 | 26 | 11 |
| 重心落とし | `control_anchor` | `uncommon` | 157 | 50 | 24 | 13 |
| 勢い溜め | `control_momentum` | `uncommon` | 151 | 43 | 21 | 7 |
| 小太刀の加護 | `blessing_shortblade` | `uncommon` | 151 | 27 | 12 | 0 |
| Blank First | `control_blank_first` | `uncommon` | 147 | 55 | 23 | 0 |
| 加速 | `control_haste` | `uncommon` | 147 | 52 | 29 | 10 |
| 攻の加護 | `blessing_attack` | `rare` | 146 | 36 | 16 | 0 |
| 封祈 | `control_blessing_lock` | `uncommon` | 146 | 5 | 1 | 0 |
| 穢れ | `control_defile` | `uncommon` | 145 | 9 | 3 | 0 |
| 追風の加護 | `blessing_tailwind` | `uncommon` | 144 | 16 | 2 | 0 |
| 探り | `control_peek_hand` | `uncommon` | 143 | 40 | 19 | 8 |
| 補強 | `control_fortify` | `uncommon` | 141 | 54 | 26 | 8 |
| 看破 | `control_opening_read` | `uncommon` | 140 | 36 | 12 | 2 |
| 攻勢の加護 | `blessing_offense` | `rare` | 137 | 40 | 22 | 0 |
| 間合いの加護 | `blessing_range` | `uncommon` | 134 | 15 | 10 | 0 |
| 小盾の加護 | `blessing_buckler` | `uncommon` | 133 | 26 | 10 | 0 |
| 迷い手 | `control_hand_echo` | `uncommon` | 132 | 38 | 16 | 4 |
| 鈍足の加護 | `blessing_slow` | `rare` | 131 | 35 | 21 | 0 |
| 受け流しの加護 | `blessing_parry` | `uncommon` | 130 | 33 | 12 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | `uncommon` | 130 | 28 | 12 | 0 |
| 祓い直し | `control_discard_facedown_blessing` | `uncommon` | 130 | 3 | 1 | 0 |
| 鈍りの加護 | `blessing_dullness` | `uncommon` | 128 | 21 | 10 | 0 |
| 手繰り直し | `control_redraw_hand` | `uncommon` | 127 | 16 | 4 | 2 |
| 前借り | `control_all_in_focus` | `uncommon` | 124 | 42 | 18 | 1 |
| 防壁の加護 | `blessing_barrier` | `rare` | 122 | 39 | 20 | 0 |
| 見切りの加護 | `blessing_insight` | `rare` | 122 | 17 | 8 | 0 |
| 抑制の加護 | `blessing_suppression` | `rare` | 122 | 15 | 8 | 0 |
| 防の加護 | `blessing_guard` | `rare` | 121 | 23 | 8 | 0 |
| 罠糸の加護 | `blessing_trap_web` | `rare` | 111 | 37 | 17 | 0 |
| 破祈 | `control_blessing_break` | `rare` | 108 | 8 | 6 | 1 |
| 速の加護 | `blessing_speed` | `rare` | 107 | 27 | 13 | 0 |
| 蓄え | `control_reserve` | `rare` | 95 | 34 | 14 | 0 |
| 転祈 | `control_blessing_flip` | `rare` | 88 | 7 | 3 | 1 |
| 先触れ | `control_topdeck_hand` | `rare` | 84 | 22 | 9 | 2 |
| Crush Spirit | `control_crush_spirit` | `rare` | 83 | 24 | 14 | 0 |
| 知恵の加護 | `blessing_draw` | `rare` | 64 | 19 | 6 | 0 |

### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 小太刀の加護 | `blessing_shortblade` | 149 | 38.3% | 151 | 27 | 27 | 6 | 6 | 0 | 0 |
| 追風の加護 | `blessing_tailwind` | 142 | 42.3% | 144 | 16 | 16 | 0 | 0 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 141 | 46.1% | 146 | 36 | 35 | 0 | 0 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 136 | 46.3% | 137 | 40 | 39 | 16 | 16 | 0 | 0 |
| 間合いの加護 | `blessing_range` | 132 | 48.5% | 134 | 15 | 15 | 2 | 2 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 131 | 54.2% | 131 | 35 | 35 | 6 | 6 | 0 | 0 |
| 小盾の加護 | `blessing_buckler` | 131 | 48.1% | 133 | 26 | 25 | 3 | 3 | 0 | 0 |
| 受け流しの加護 | `blessing_parry` | 126 | 54.8% | 130 | 33 | 32 | 7 | 7 | 0 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | 125 | 50.4% | 130 | 28 | 28 | 6 | 6 | 0 | 0 |
| 鈍りの加護 | `blessing_dullness` | 124 | 48.4% | 128 | 21 | 21 | 0 | 0 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 122 | 51.6% | 122 | 39 | 38 | 12 | 12 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 122 | 47.5% | 122 | 15 | 15 | 0 | 0 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 122 | 42.6% | 122 | 17 | 17 | 16 | 16 | 0 | 0 |
| 防の加護 | `blessing_guard` | 119 | 46.2% | 121 | 23 | 22 | 0 | 0 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 111 | 42.3% | 111 | 37 | 36 | 6 | 6 | 0 | 0 |
| 速の加護 | `blessing_speed` | 107 | 43.9% | 107 | 27 | 27 | 1 | 1 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 64 | 45.3% | 64 | 19 | 19 | 0 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 8000 | 2346 | 29.3% | 1068 | 45.5% | 417 |
| `uncommon` | 8000 | 2296 | 28.7% | 1158 | 50.4% | 627 |
| `rare` | 4000 | 1106 | 27.7% | 574 | 51.9% | 316 |

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
