# Draft Report

## Configuration

- Draft Bot 1: `StandardDraftBot`
- Draft Bot 2: `GuardDraftBot`
- Play Bot 1: `StandardBot`
- Play Bot 2: `GuardBot`
- Rounds: 500
- Total Matches: 1000
- Seed: 3911
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
| `GuardDraftBot` | 1000 | 479 | 464 | 57 | 47.9% | 43.9% | 13.6% | 54.3% | 32.2% | 2.98 | 2.74 | 47.8% | 48.0% | 71.4% | 1.8% | 26.7% | 10.14 | 7.79 | 2.07 | 5.28 | 3.57 | 3.3 | 7.86 | 8 | 8 | 4 |
| `StandardDraftBot` | 1000 | 464 | 479 | 57 | 46.4% | 43.9% | 15.3% | 52.8% | 31.9% | 2.91 | 2.79 | 46.8% | 46.0% | 70.7% | 2.7% | 26.6% | 9.98 | 7.86 | 2.17 | 5.33 | 3.5 | 3.26 | 7.92 | 8 | 8 | 4 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| GuardDraftBot vs StandardDraftBot | 1000 | 57 | `GuardDraftBot`=479, `StandardDraftBot`=464 | 1.61 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 防御 | 635 |
| 2 | 攻撃 | 581 |
| 3 | ステップ | 522 |
| 4 | 圧迫 | 517 |
| 5 | 構え | 472 |
| 6 | 見定め | 450 |
| 7 | 遠眼 | 446 |
| 8 | 牽制 | 440 |
| 9 | 公開勝負 | 404 |
| 10 | 集中 | 382 |
| 11 | 貫き | 293 |
| 12 | 崩し | 281 |
| 13 | 十字受け | 265 |
| 14 | 踏ん張り | 263 |
| 15 | 返し刃 | 259 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 272 |
| 2 | 防御 | 262 |
| 3 | 圧迫 | 234 |
| 4 | ステップ | 215 |
| 5 | 構え | 214 |
| 6 | 牽制 | 207 |
| 7 | 貫き | 197 |
| 8 | 踏み込み | 191 |
| 9 | 見定め | 186 |
| 10 | 崩し | 184 |
| 11 | 遠眼 | 167 |
| 12 | 公開勝負 | 166 |
| 13 | 集中 | 154 |
| 14 | 返し刃 | 149 |
| 15 | 粉砕 | 148 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 204 |
| 2 | 貫き | 183 |
| 3 | 踏み込み | 177 |
| 4 | 崩し | 166 |
| 5 | 大振り | 137 |
| 6 | 防御 | 134 |
| 7 | 粉砕 | 133 |
| 8 | ステップ | 128 |
| 9 | 返し刃 | 121 |
| 10 | 渾身 | 101 |
| 11 | 疾走 | 94 |
| 12 | 強撃 | 88 |
| 13 | 構え | 86 |
| 14 | 踏ん張り | 77 |
| 15 | 十字受け | 72 |

### Blessing Involvement Overall

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 攻の加護 | `blessing_attack` | 290 | 49.0% | 296 | 75 | 74 | 0 | 0 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 285 | 42.1% | 287 | 82 | 81 | 31 | 31 | 0 | 0 |
| 間合いの加護 | `blessing_range` | 280 | 46.1% | 283 | 20 | 20 | 3 | 3 | 0 | 0 |
| 小盾の加護 | `blessing_buckler` | 278 | 42.4% | 284 | 62 | 61 | 17 | 17 | 0 | 0 |
| 受け流しの加護 | `blessing_parry` | 275 | 49.8% | 280 | 62 | 61 | 6 | 6 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 273 | 47.3% | 274 | 38 | 37 | 1 | 1 | 0 | 0 |
| 追風の加護 | `blessing_tailwind` | 267 | 48.3% | 271 | 55 | 55 | 2 | 2 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 256 | 52.0% | 262 | 65 | 63 | 7 | 7 | 0 | 0 |
| 鈍りの加護 | `blessing_dullness` | 255 | 43.1% | 256 | 53 | 53 | 7 | 7 | 0 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | 252 | 46.4% | 257 | 64 | 63 | 14 | 14 | 0 | 0 |
| 小太刀の加護 | `blessing_shortblade` | 251 | 44.6% | 255 | 57 | 56 | 10 | 10 | 0 | 0 |
| 速の加護 | `blessing_speed` | 239 | 47.7% | 240 | 49 | 49 | 1 | 1 | 0 | 0 |
| 防の加護 | `blessing_guard` | 225 | 50.2% | 225 | 51 | 50 | 0 | 0 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 220 | 41.8% | 223 | 28 | 27 | 29 | 29 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 217 | 46.5% | 218 | 60 | 60 | 18 | 18 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 198 | 51.0% | 199 | 38 | 38 | 5 | 5 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 123 | 44.7% | 123 | 32 | 30 | 0 | 0 | 0 | 0 |

## Drafter Pattern Metrics

| Drafter | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `GuardDraftBot` | 2.63 | 0.91 | 1.29 | 1.56 | 0.89 | 1.13 | 152 (15.2%) | 149 (31.1%) |
| `StandardDraftBot` | 2.9 | 0.82 | 1.16 | 1.88 | 0.77 | 0.96 | 149 (14.9%) | 152 (32.8%) |

## Drafter Details

### GuardDraftBot

- Win Rate: 47.9%
- Draw Rate: 5.7%
- First Pass Win Rate: 43.9%
- Win With Fewer Cards: 13.6%
- Win With Same Cards: 54.3%
- Win With More Cards: 32.2%
- Winner Facedown Avg: 2.98
- Loser Facedown Avg: 2.74
- Starting Player Win Rate: 47.8%
- Responding Player Win Rate: 48.0%
- Final Stats Avg: A=2.63, B=0.91, S=1.29
- Losing Final Stats Avg: A=1.56, B=0.89, S=1.13
- Lost With Speed Advantage: 152 (15.2%)
- Won After Blocking Faster Attack: 149 (31.1%)
- Blessing Ended Facedown: 77
- Blessing Placed But Unused: 369
- Opponent Pass / Set+Pass Into Face-Up Blessing: 640
- Win Rate When Forcing Opponent Blessing Use: 51.4%
- Action Rates: set=71.4%, set_pass=1.8%, pass=26.7%
- set_pass Candidate Avg / Match: 16.02
- Turns: min=1, avg=1.61, max=12
- Battle / Control / Blessing: avg=10.14 / 7.79 / 2.07
- Role Colors: red=5.28, blue=3.57, green=3.3, white=7.86
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 1027 |
| 2 | 防御 | 992 |
| 3 | ステップ | 892 |
| 4 | 圧迫 | 830 |
| 5 | 構え | 787 |
| 6 | 牽制 | 718 |
| 7 | 遠眼 | 715 |
| 8 | 集中 | 691 |
| 9 | 公開勝負 | 678 |
| 10 | 見定め | 670 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 512 |
| 2 | 防御 | 458 |
| 3 | ステップ | 424 |
| 4 | 圧迫 | 392 |
| 5 | 構え | 363 |
| 6 | 牽制 | 362 |
| 7 | 遠眼 | 344 |
| 8 | 見定め | 334 |
| 9 | 公開勝負 | 325 |
| 10 | 集中 | 318 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 1027 | 290 | 143 | 111 |
| 防御 | `battle_defend` | `common` | 992 | 338 | 142 | 71 |
| ステップ | `battle_step` | `common` | 892 | 247 | 105 | 63 |
| 圧迫 | `control_pressure` | `common` | 830 | 266 | 125 | 33 |
| 構え | `control_guard` | `common` | 787 | 242 | 104 | 48 |
| 牽制 | `control_disrupt` | `common` | 718 | 218 | 112 | 6 |
| 遠眼 | `control_peek_opponent_top` | `common` | 715 | 225 | 88 | 18 |
| 集中 | `control_focus` | `common` | 691 | 178 | 70 | 29 |
| 公開勝負 | `control_opening_expose` | `common` | 678 | 197 | 92 | 38 |
| 見定め | `control_peek_own_top` | `common` | 670 | 223 | 106 | 25 |
| 崩し | `battle_break` | `uncommon` | 436 | 139 | 94 | 84 |
| 貫き | `battle_pierce` | `uncommon` | 428 | 153 | 106 | 100 |
| 十字受け | `battle_cross_guard` | `uncommon` | 405 | 137 | 70 | 38 |
| 返し刃 | `battle_counter` | `uncommon` | 400 | 135 | 76 | 58 |
| 踏み込み | `battle_step_in` | `rare` | 374 | 115 | 89 | 82 |
| 踏ん張り | `battle_brace` | `uncommon` | 371 | 137 | 73 | 49 |
| 粉砕 | `battle_crush` | `uncommon` | 371 | 114 | 70 | 62 |
| Bastion | `battle_bastion` | `uncommon` | 359 | 122 | 48 | 16 |
| 鉄壁 | `battle_wall` | `rare` | 348 | 126 | 54 | 16 |
| 残像 | `battle_afterimage` | `rare` | 343 | 125 | 58 | 32 |
| 渾身 | `battle_all_in` | `rare` | 343 | 88 | 48 | 46 |
| 大振り | `battle_heavy_swing` | `rare` | 342 | 115 | 68 | 64 |
| 押し込み | `battle_press` | `uncommon` | 335 | 111 | 65 | 38 |
| 退き足 | `battle_backstep` | `uncommon` | 311 | 131 | 53 | 25 |
| 疾走 | `battle_dash` | `rare` | 308 | 103 | 67 | 53 |
| 強撃 | `battle_power_attack` | `uncommon` | 300 | 99 | 52 | 44 |
| フェイント | `battle_feint` | `uncommon` | 298 | 102 | 42 | 30 |
| Tripwire | `battle_tripwire` | `rare` | 294 | 0 | 0 | 0 |
| 受け流し | `battle_guard` | `uncommon` | 292 | 114 | 55 | 35 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 287 | 91 | 43 | 20 |
| Bulwark | `battle_bulwark` | `uncommon` | 284 | 90 | 34 | 19 |
| 受け直し | `control_cover` | `uncommon` | 202 | 62 | 25 | 9 |
| 前のめり | `control_overclock` | `uncommon` | 182 | 56 | 25 | 9 |
| 看破 | `control_opening_read` | `uncommon` | 159 | 42 | 19 | 5 |
| 祓い直し | `control_discard_facedown_blessing` | `uncommon` | 159 | 2 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | `rare` | 158 | 44 | 26 | 0 |
| 穢れ | `control_defile` | `uncommon` | 152 | 4 | 1 | 0 |
| 補強 | `control_fortify` | `uncommon` | 149 | 46 | 20 | 5 |
| 攻の加護 | `blessing_attack` | `rare` | 149 | 41 | 20 | 0 |
| 前借り | `control_all_in_focus` | `uncommon` | 149 | 27 | 13 | 6 |
| Blank First | `control_blank_first` | `uncommon` | 147 | 46 | 23 | 2 |
| 加速 | `control_haste` | `uncommon` | 145 | 38 | 15 | 2 |
| 勢い溜め | `control_momentum` | `uncommon` | 141 | 45 | 25 | 14 |
| 封祈 | `control_blessing_lock` | `uncommon` | 141 | 9 | 2 | 0 |
| 追風の加護 | `blessing_tailwind` | `uncommon` | 140 | 32 | 16 | 0 |
| 小盾の加護 | `blessing_buckler` | `uncommon` | 136 | 29 | 12 | 0 |
| 間合いの加護 | `blessing_range` | `uncommon` | 135 | 9 | 3 | 0 |
| 重心落とし | `control_anchor` | `uncommon` | 131 | 32 | 14 | 5 |
| 受け流しの加護 | `blessing_parry` | `uncommon` | 131 | 32 | 9 | 0 |
| 鈍りの加護 | `blessing_dullness` | `uncommon` | 131 | 30 | 13 | 0 |
| 罠糸の加護 | `blessing_trap_web` | `rare` | 123 | 34 | 18 | 0 |
| 手繰り直し | `control_redraw_hand` | `uncommon` | 123 | 21 | 7 | 3 |
| 踏み止まりの加護 | `blessing_laststand` | `uncommon` | 121 | 28 | 10 | 0 |
| 小太刀の加護 | `blessing_shortblade` | `uncommon` | 121 | 26 | 13 | 0 |
| 防壁の加護 | `blessing_barrier` | `rare` | 120 | 31 | 12 | 0 |
| 抑制の加護 | `blessing_suppression` | `rare` | 120 | 15 | 5 | 0 |
| 迷い手 | `control_hand_echo` | `uncommon` | 115 | 40 | 19 | 5 |
| 探り | `control_peek_hand` | `uncommon` | 113 | 38 | 15 | 1 |
| 速の加護 | `blessing_speed` | `rare` | 109 | 21 | 11 | 0 |
| 防の加護 | `blessing_guard` | `rare` | 107 | 24 | 13 | 0 |
| 鈍足の加護 | `blessing_slow` | `rare` | 103 | 20 | 11 | 0 |
| 転祈 | `control_blessing_flip` | `rare` | 103 | 8 | 3 | 0 |
| Crush Spirit | `control_crush_spirit` | `rare` | 102 | 38 | 23 | 1 |
| 見切りの加護 | `blessing_insight` | `rare` | 101 | 10 | 6 | 0 |
| 蓄え | `control_reserve` | `rare` | 100 | 31 | 16 | 1 |
| 先触れ | `control_topdeck_hand` | `rare` | 100 | 25 | 12 | 6 |
| 破祈 | `control_blessing_break` | `rare` | 91 | 11 | 4 | 0 |
| 知恵の加護 | `blessing_draw` | `rare` | 62 | 16 | 5 | 0 |

### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 攻勢の加護 | `blessing_offense` | 156 | 41.7% | 158 | 44 | 44 | 17 | 17 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 146 | 50.7% | 149 | 41 | 41 | 0 | 0 | 0 | 0 |
| 追風の加護 | `blessing_tailwind` | 138 | 48.6% | 140 | 32 | 32 | 1 | 1 | 0 | 0 |
| 小盾の加護 | `blessing_buckler` | 135 | 43.0% | 136 | 29 | 29 | 12 | 12 | 0 | 0 |
| 間合いの加護 | `blessing_range` | 132 | 45.5% | 135 | 9 | 9 | 2 | 2 | 0 | 0 |
| 鈍りの加護 | `blessing_dullness` | 130 | 47.7% | 131 | 30 | 30 | 4 | 4 | 0 | 0 |
| 受け流しの加護 | `blessing_parry` | 129 | 45.0% | 131 | 32 | 31 | 1 | 1 | 0 | 0 |
| 小太刀の加護 | `blessing_shortblade` | 121 | 45.5% | 121 | 26 | 26 | 6 | 6 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 120 | 54.2% | 123 | 34 | 33 | 4 | 4 | 0 | 0 |
| 抑制の加護 | `blessing_suppression` | 120 | 50.0% | 120 | 15 | 14 | 0 | 0 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 119 | 46.2% | 120 | 31 | 31 | 8 | 8 | 0 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | 118 | 48.3% | 121 | 28 | 28 | 8 | 8 | 0 | 0 |
| 速の加護 | `blessing_speed` | 109 | 42.2% | 109 | 21 | 21 | 1 | 1 | 0 | 0 |
| 防の加護 | `blessing_guard` | 107 | 55.1% | 107 | 24 | 23 | 0 | 0 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 102 | 49.0% | 103 | 20 | 20 | 2 | 2 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 100 | 43.0% | 101 | 10 | 10 | 12 | 12 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 62 | 45.2% | 62 | 16 | 15 | 0 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 8000 | 2424 | 30.3% | 1087 | 44.8% | 442 |
| `uncommon` | 8000 | 2369 | 29.6% | 1180 | 49.8% | 684 |
| `rare` | 4000 | 1041 | 26.0% | 569 | 54.7% | 301 |

#### Match Logs

- [draft_match_0001](matches/match_0001_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0002](matches/match_0002_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0003](matches/match_0003_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0004](matches/match_0004_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0005](matches/match_0005_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0006](matches/match_0006_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0007](matches/match_0007_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0008](matches/match_0008_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0009](matches/match_0009_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0010](matches/match_0010_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0011](matches/match_0011_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0012](matches/match_0012_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0013](matches/match_0013_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0014](matches/match_0014_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0015](matches/match_0015_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0016](matches/match_0016_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0017](matches/match_0017_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0018](matches/match_0018_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0019](matches/match_0019_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0020](matches/match_0020_GuardDraftBot_vs_StandardDraftBot.md)

### StandardDraftBot

- Win Rate: 46.4%
- Draw Rate: 5.7%
- First Pass Win Rate: 43.9%
- Win With Fewer Cards: 15.3%
- Win With Same Cards: 52.8%
- Win With More Cards: 31.9%
- Winner Facedown Avg: 2.91
- Loser Facedown Avg: 2.79
- Starting Player Win Rate: 46.8%
- Responding Player Win Rate: 46.0%
- Final Stats Avg: A=2.9, B=0.82, S=1.16
- Losing Final Stats Avg: A=1.88, B=0.77, S=0.96
- Lost With Speed Advantage: 149 (14.9%)
- Won After Blocking Faster Attack: 152 (32.8%)
- Blessing Ended Facedown: 77
- Blessing Placed But Unused: 377
- Opponent Pass / Set+Pass Into Face-Up Blessing: 675
- Win Rate When Forcing Opponent Blessing Use: 30.1%
- Action Rates: set=70.7%, set_pass=2.7%, pass=26.6%
- set_pass Candidate Avg / Match: 16.02
- Turns: min=1, avg=1.61, max=12
- Battle / Control / Blessing: avg=9.98 / 7.86 / 2.17
- Role Colors: red=5.33, blue=3.5, green=3.26, white=7.92
- Rarities: common=8, uncommon=8, rare=4

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 攻撃 | 1005 |
| 2 | 防御 | 991 |
| 3 | ステップ | 912 |
| 4 | 圧迫 | 826 |
| 5 | 構え | 742 |
| 6 | 遠眼 | 714 |
| 7 | 牽制 | 712 |
| 8 | 集中 | 708 |
| 9 | 公開勝負 | 707 |
| 10 | 見定め | 683 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 防御 | 459 |
| 2 | 攻撃 | 455 |
| 3 | ステップ | 443 |
| 4 | 圧迫 | 377 |
| 5 | 牽制 | 347 |
| 6 | 集中 | 345 |
| 7 | 構え | 336 |
| 8 | 公開勝負 | 334 |
| 9 | 遠眼 | 320 |
| 10 | 見定め | 296 |

### Draft Card Stats

| Card | ID | Rarity | Picked | Used | Winner Usage | Lethal |
|---|---|---|---:|---:|---:|---:|
| 攻撃 | `battle_attack` | `common` | 1005 | 291 | 129 | 93 |
| 防御 | `battle_defend` | `common` | 991 | 297 | 120 | 63 |
| ステップ | `battle_step` | `common` | 912 | 275 | 110 | 65 |
| 圧迫 | `control_pressure` | `common` | 826 | 251 | 109 | 23 |
| 構え | `control_guard` | `common` | 742 | 230 | 110 | 38 |
| 遠眼 | `control_peek_opponent_top` | `common` | 714 | 221 | 79 | 23 |
| 牽制 | `control_disrupt` | `common` | 712 | 222 | 95 | 11 |
| 集中 | `control_focus` | `common` | 708 | 204 | 84 | 36 |
| 公開勝負 | `control_opening_expose` | `common` | 707 | 207 | 74 | 24 |
| 見定め | `control_peek_own_top` | `common` | 683 | 227 | 80 | 16 |
| 崩し | `battle_break` | `uncommon` | 448 | 142 | 90 | 82 |
| 貫き | `battle_pierce` | `uncommon` | 438 | 140 | 91 | 83 |
| 粉砕 | `battle_crush` | `uncommon` | 387 | 138 | 78 | 71 |
| 返し刃 | `battle_counter` | `uncommon` | 379 | 124 | 73 | 63 |
| 渾身 | `battle_all_in` | `rare` | 376 | 126 | 58 | 55 |
| 踏ん張り | `battle_brace` | `uncommon` | 369 | 126 | 55 | 28 |
| 踏み込み | `battle_step_in` | `rare` | 368 | 136 | 102 | 95 |
| 十字受け | `battle_cross_guard` | `uncommon` | 358 | 128 | 61 | 34 |
| 大振り | `battle_heavy_swing` | `rare` | 354 | 128 | 75 | 73 |
| 残像 | `battle_afterimage` | `rare` | 329 | 109 | 43 | 23 |
| 鉄壁 | `battle_wall` | `rare` | 323 | 119 | 46 | 21 |
| 強撃 | `battle_power_attack` | `uncommon` | 322 | 101 | 54 | 44 |
| 退き足 | `battle_backstep` | `uncommon` | 319 | 122 | 53 | 26 |
| Bastion | `battle_bastion` | `uncommon` | 317 | 108 | 48 | 20 |
| 押し込み | `battle_press` | `uncommon` | 315 | 102 | 53 | 28 |
| フェイント | `battle_feint` | `uncommon` | 296 | 100 | 44 | 29 |
| 受け流し | `battle_guard` | `uncommon` | 285 | 91 | 42 | 28 |
| 低姿勢 | `battle_low_stance` | `uncommon` | 284 | 93 | 41 | 19 |
| 疾走 | `battle_dash` | `rare` | 281 | 97 | 54 | 41 |
| Bulwark | `battle_bulwark` | `uncommon` | 271 | 98 | 49 | 28 |
| Tripwire | `battle_tripwire` | `rare` | 251 | 0 | 0 | 0 |
| 受け直し | `control_cover` | `uncommon` | 204 | 59 | 27 | 6 |
| 重心落とし | `control_anchor` | `uncommon` | 173 | 58 | 28 | 13 |
| 前のめり | `control_overclock` | `uncommon` | 166 | 55 | 26 | 3 |
| 補強 | `control_fortify` | `uncommon` | 163 | 47 | 17 | 2 |
| 探り | `control_peek_hand` | `uncommon` | 155 | 41 | 10 | 3 |
| 抑制の加護 | `blessing_suppression` | `rare` | 154 | 23 | 9 | 0 |
| 受け流しの加護 | `blessing_parry` | `uncommon` | 149 | 30 | 12 | 0 |
| 小盾の加護 | `blessing_buckler` | `uncommon` | 148 | 33 | 11 | 0 |
| 間合いの加護 | `blessing_range` | `uncommon` | 148 | 11 | 3 | 0 |
| 攻の加護 | `blessing_attack` | `rare` | 147 | 34 | 13 | 0 |
| Blank First | `control_blank_first` | `uncommon` | 146 | 56 | 31 | 1 |
| 手繰り直し | `control_redraw_hand` | `uncommon` | 146 | 25 | 11 | 4 |
| 祓い直し | `control_discard_facedown_blessing` | `uncommon` | 146 | 3 | 1 | 0 |
| 勢い溜め | `control_momentum` | `uncommon` | 143 | 35 | 12 | 3 |
| 看破 | `control_opening_read` | `uncommon` | 139 | 44 | 19 | 8 |
| 迷い手 | `control_hand_echo` | `uncommon` | 139 | 44 | 16 | 4 |
| 罠糸の加護 | `blessing_trap_web` | `rare` | 139 | 31 | 14 | 0 |
| 前借り | `control_all_in_focus` | `uncommon` | 137 | 41 | 18 | 4 |
| 踏み止まりの加護 | `blessing_laststand` | `uncommon` | 136 | 36 | 14 | 0 |
| 封祈 | `control_blessing_lock` | `uncommon` | 135 | 13 | 8 | 1 |
| 小太刀の加護 | `blessing_shortblade` | `uncommon` | 134 | 31 | 14 | 0 |
| 速の加護 | `blessing_speed` | `rare` | 131 | 28 | 16 | 0 |
| 追風の加護 | `blessing_tailwind` | `uncommon` | 131 | 23 | 13 | 0 |
| 攻勢の加護 | `blessing_offense` | `rare` | 129 | 38 | 21 | 0 |
| 鈍りの加護 | `blessing_dullness` | `uncommon` | 125 | 23 | 10 | 0 |
| 穢れ | `control_defile` | `uncommon` | 125 | 9 | 3 | 1 |
| 加速 | `control_haste` | `uncommon` | 124 | 41 | 17 | 5 |
| 見切りの加護 | `blessing_insight` | `rare` | 122 | 18 | 8 | 0 |
| 先触れ | `control_topdeck_hand` | `rare` | 121 | 44 | 17 | 4 |
| 防の加護 | `blessing_guard` | `rare` | 118 | 27 | 11 | 0 |
| 転祈 | `control_blessing_flip` | `rare` | 111 | 4 | 1 | 1 |
| 破祈 | `control_blessing_break` | `rare` | 104 | 7 | 3 | 1 |
| 防壁の加護 | `blessing_barrier` | `rare` | 98 | 29 | 14 | 0 |
| 蓄え | `control_reserve` | `rare` | 97 | 32 | 15 | 1 |
| 鈍足の加護 | `blessing_slow` | `rare` | 96 | 18 | 9 | 0 |
| Crush Spirit | `control_crush_spirit` | `rare` | 90 | 20 | 10 | 0 |
| 知恵の加護 | `blessing_draw` | `rare` | 61 | 16 | 7 | 0 |

### Blessing Involvement

| Blessing | ID | In Deck Matches | Deck Win Rate | Deck Copies | Played | Active | Events | Decisive | Passive Decisive | Pre-Reveal |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 抑制の加護 | `blessing_suppression` | 153 | 45.1% | 154 | 23 | 23 | 1 | 1 | 0 | 0 |
| 間合いの加護 | `blessing_range` | 148 | 46.6% | 148 | 11 | 11 | 1 | 1 | 0 | 0 |
| 受け流しの加護 | `blessing_parry` | 146 | 54.1% | 149 | 30 | 30 | 5 | 5 | 0 | 0 |
| 攻の加護 | `blessing_attack` | 144 | 47.2% | 147 | 34 | 33 | 0 | 0 | 0 | 0 |
| 小盾の加護 | `blessing_buckler` | 143 | 42.0% | 148 | 33 | 32 | 5 | 5 | 0 | 0 |
| 罠糸の加護 | `blessing_trap_web` | 136 | 50.0% | 139 | 31 | 30 | 3 | 3 | 0 | 0 |
| 踏み止まりの加護 | `blessing_laststand` | 134 | 44.8% | 136 | 36 | 35 | 6 | 6 | 0 | 0 |
| 速の加護 | `blessing_speed` | 130 | 52.3% | 131 | 28 | 28 | 0 | 0 | 0 | 0 |
| 小太刀の加護 | `blessing_shortblade` | 130 | 43.8% | 134 | 31 | 30 | 4 | 4 | 0 | 0 |
| 追風の加護 | `blessing_tailwind` | 129 | 48.1% | 131 | 23 | 23 | 1 | 1 | 0 | 0 |
| 攻勢の加護 | `blessing_offense` | 129 | 42.6% | 129 | 38 | 37 | 14 | 14 | 0 | 0 |
| 鈍りの加護 | `blessing_dullness` | 125 | 38.4% | 125 | 23 | 23 | 3 | 3 | 0 | 0 |
| 見切りの加護 | `blessing_insight` | 120 | 40.8% | 122 | 18 | 17 | 17 | 17 | 0 | 0 |
| 防の加護 | `blessing_guard` | 118 | 45.8% | 118 | 27 | 27 | 0 | 0 | 0 | 0 |
| 防壁の加護 | `blessing_barrier` | 98 | 46.9% | 98 | 29 | 29 | 10 | 10 | 0 | 0 |
| 鈍足の加護 | `blessing_slow` | 96 | 53.1% | 96 | 18 | 18 | 3 | 3 | 0 | 0 |
| 知恵の加護 | `blessing_draw` | 61 | 44.3% | 61 | 16 | 15 | 0 | 0 | 0 | 0 |

### Rarity Play Stats

| Rarity | Picked | Used | Usage Rate | Winner Usage | Win Contribution | Lethal |
|---|---:|---:|---:|---:|---:|---:|
| `common` | 8000 | 2425 | 30.3% | 990 | 40.8% | 392 |
| `uncommon` | 8000 | 2371 | 29.6% | 1153 | 48.6% | 641 |
| `rare` | 4000 | 1084 | 27.1% | 546 | 50.4% | 315 |

#### Match Logs

- [draft_match_0001](matches/match_0001_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0002](matches/match_0002_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0003](matches/match_0003_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0004](matches/match_0004_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0005](matches/match_0005_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0006](matches/match_0006_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0007](matches/match_0007_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0008](matches/match_0008_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0009](matches/match_0009_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0010](matches/match_0010_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0011](matches/match_0011_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0012](matches/match_0012_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0013](matches/match_0013_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0014](matches/match_0014_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0015](matches/match_0015_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0016](matches/match_0016_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0017](matches/match_0017_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0018](matches/match_0018_GuardDraftBot_vs_StandardDraftBot.md)
- [draft_match_0019](matches/match_0019_StandardDraftBot_vs_GuardDraftBot.md)
- [draft_match_0020](matches/match_0020_GuardDraftBot_vs_StandardDraftBot.md)
