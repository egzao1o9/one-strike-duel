# Random Bot Mix Report

## Configuration

- Matches: 5000
- Seed: 101
- Selection Mode: p1/p2 bot and deck selected independently at random
- Bot Pool: `AttackBot`, `BurstBot`, `DefenseBot`, `DisruptBot`, `GreedyBot`, `RandomBot`, `RiskBot`, `TempoBot`, `TurtleBot`
- Deck Pool: `starter_attack`, `starter_balanced`, `starter_defense`, `starter_heavy`, `starter_speed`

## Bot Win Rates

| Bot | Matches | Wins | Losses | Draws | Win Rate | Turn Min | Turn Avg | Turn Max | Win A Avg | Win B Avg | Win S Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `AttackBot` | 1087 | 613 | 470 | 4 | 56.4% | 1 | 1.55 | 50 | 4.88 | 1.11 | 2.9 |
| `BurstBot` | 1135 | 561 | 568 | 6 | 49.4% | 1 | 1.6 | 50 | 3.72 | 0.97 | 2.86 |
| `DefenseBot` | 1050 | 635 | 411 | 4 | 60.5% | 1 | 2.45 | 50 | 2.41 | 3.53 | 2.17 |
| `DisruptBot` | 1136 | 588 | 527 | 21 | 51.8% | 1 | 2.57 | 50 | 3.27 | 0.63 | 3.16 |
| `GreedyBot` | 1131 | 439 | 668 | 24 | 38.8% | 1 | 2.61 | 50 | 2.77 | 1.34 | 1.97 |
| `RandomBot` | 1128 | 527 | 580 | 21 | 46.7% | 1 | 2.66 | 50 | 3.1 | 1.67 | 2.24 |
| `RiskBot` | 1128 | 617 | 498 | 13 | 54.7% | 1 | 2.38 | 50 | 3.13 | 2.5 | 1.31 |
| `TempoBot` | 1098 | 468 | 616 | 14 | 42.6% | 1 | 2.36 | 50 | 2.8 | 0.9 | 3.49 |
| `TurtleBot` | 1107 | 478 | 588 | 41 | 43.2% | 1 | 4.05 | 50 | 1.98 | 3.85 | 1.2 |

## Bot Pair Summary

| Pair | Matches | Draws | Wins | Turn Min | Turn Avg | Turn Max |
|---|---:|---:|---|---:|---:|---:|
| AttackBot vs AttackBot | 49 | 0 | `AttackBot`=49 | 1 | 1.06 | 2 |
| AttackBot vs BurstBot | 123 | 0 | `AttackBot`=69, `BurstBot`=54 | 1 | 1.14 | 5 |
| AttackBot vs DefenseBot | 127 | 0 | `AttackBot`=58, `DefenseBot`=69 | 1 | 1.72 | 10 |
| AttackBot vs DisruptBot | 140 | 1 | `AttackBot`=79, `DisruptBot`=60 | 1 | 1.65 | 50 |
| AttackBot vs GreedyBot | 112 | 1 | `AttackBot`=70, `GreedyBot`=41 | 1 | 1.7 | 50 |
| AttackBot vs RandomBot | 126 | 1 | `AttackBot`=86, `RandomBot`=39 | 1 | 1.69 | 50 |
| AttackBot vs RiskBot | 127 | 0 | `AttackBot`=59, `RiskBot`=68 | 1 | 1.46 | 5 |
| AttackBot vs TempoBot | 121 | 1 | `AttackBot`=71, `TempoBot`=49 | 1 | 1.76 | 50 |
| AttackBot vs TurtleBot | 113 | 0 | `AttackBot`=72, `TurtleBot`=41 | 1 | 1.66 | 6 |
| BurstBot vs BurstBot | 62 | 0 | `BurstBot`=62 | 1 | 1.32 | 3 |
| BurstBot vs DefenseBot | 130 | 0 | `BurstBot`=44, `DefenseBot`=86 | 1 | 1.71 | 6 |
| BurstBot vs DisruptBot | 130 | 0 | `BurstBot`=63, `DisruptBot`=67 | 1 | 1.31 | 7 |
| BurstBot vs GreedyBot | 146 | 2 | `BurstBot`=96, `GreedyBot`=48 | 1 | 1.9 | 50 |
| BurstBot vs RandomBot | 121 | 2 | `BurstBot`=62, `RandomBot`=57 | 1 | 2.11 | 50 |
| BurstBot vs RiskBot | 119 | 0 | `BurstBot`=48, `RiskBot`=71 | 1 | 1.29 | 5 |
| BurstBot vs TempoBot | 119 | 1 | `BurstBot`=70, `TempoBot`=48 | 1 | 1.75 | 50 |
| BurstBot vs TurtleBot | 123 | 1 | `BurstBot`=62, `TurtleBot`=60 | 1 | 1.85 | 50 |
| DefenseBot vs DefenseBot | 53 | 1 | `DefenseBot`=52 | 1 | 4.42 | 50 |
| DefenseBot vs DisruptBot | 99 | 0 | `DefenseBot`=62, `DisruptBot`=37 | 1 | 1.89 | 8 |
| DefenseBot vs GreedyBot | 126 | 0 | `DefenseBot`=94, `GreedyBot`=32 | 1 | 1.92 | 9 |
| DefenseBot vs RandomBot | 111 | 0 | `DefenseBot`=63, `RandomBot`=48 | 1 | 2.09 | 9 |
| DefenseBot vs RiskBot | 131 | 1 | `DefenseBot`=72, `RiskBot`=58 | 1 | 2.73 | 50 |
| DefenseBot vs TempoBot | 129 | 0 | `DefenseBot`=86, `TempoBot`=43 | 1 | 2.17 | 9 |
| DefenseBot vs TurtleBot | 91 | 1 | `DefenseBot`=51, `TurtleBot`=39 | 1 | 4.01 | 50 |
| DisruptBot vs DisruptBot | 65 | 1 | `DisruptBot`=64 | 1 | 2.43 | 50 |
| DisruptBot vs GreedyBot | 140 | 5 | `DisruptBot`=85, `GreedyBot`=50 | 1 | 3.31 | 50 |
| DisruptBot vs RandomBot | 131 | 5 | `DisruptBot`=61, `RandomBot`=65 | 1 | 3.47 | 50 |
| DisruptBot vs RiskBot | 114 | 2 | `DisruptBot`=55, `RiskBot`=57 | 1 | 2.64 | 50 |
| DisruptBot vs TempoBot | 117 | 2 | `DisruptBot`=74, `TempoBot`=41 | 1 | 2.57 | 50 |
| DisruptBot vs TurtleBot | 135 | 4 | `DisruptBot`=85, `TurtleBot`=46 | 1 | 3.66 | 50 |
| GreedyBot vs GreedyBot | 62 | 2 | `GreedyBot`=60 | 1 | 3.03 | 50 |
| GreedyBot vs RandomBot | 126 | 1 | `GreedyBot`=57, `RandomBot`=68 | 1 | 2 | 50 |
| GreedyBot vs RiskBot | 110 | 4 | `GreedyBot`=39, `RiskBot`=67 | 1 | 3.5 | 50 |
| GreedyBot vs TempoBot | 119 | 2 | `GreedyBot`=56, `TempoBot`=61 | 1 | 2.41 | 50 |
| GreedyBot vs TurtleBot | 128 | 5 | `GreedyBot`=56, `TurtleBot`=67 | 1 | 3.75 | 50 |
| RandomBot vs RandomBot | 60 | 0 | `RandomBot`=60 | 1 | 1.98 | 6 |
| RandomBot vs RiskBot | 148 | 1 | `RandomBot`=59, `RiskBot`=88 | 1 | 2.22 | 50 |
| RandomBot vs TempoBot | 129 | 3 | `RandomBot`=70, `TempoBot`=56 | 1 | 2.98 | 50 |
| RandomBot vs TurtleBot | 116 | 8 | `RandomBot`=61, `TurtleBot`=47 | 1 | 5.56 | 50 |
| RiskBot vs RiskBot | 51 | 0 | `RiskBot`=51 | 1 | 1.75 | 5 |
| RiskBot vs TempoBot | 132 | 1 | `RiskBot`=72, `TempoBot`=59 | 1 | 2 | 50 |
| RiskBot vs TurtleBot | 145 | 4 | `RiskBot`=85, `TurtleBot`=56 | 1 | 3.66 | 50 |
| TempoBot vs TempoBot | 57 | 0 | `TempoBot`=57 | 1 | 1.58 | 5 |
| TempoBot vs TurtleBot | 118 | 4 | `TempoBot`=54, `TurtleBot`=60 | 1 | 4.06 | 50 |
| TurtleBot vs TurtleBot | 69 | 7 | `TurtleBot`=62 | 1 | 7.81 | 50 |

## Deck Usage Summary

| Deck | Matches | Wins | Draws | Win Rate |
|---|---:|---:|---:|---:|
| `starter_attack` | 2023 | 1085 | 1 | 53.6% |
| `starter_balanced` | 2015 | 1138 | 18 | 56.5% |
| `starter_defense` | 1978 | 1053 | 83 | 53.2% |
| `starter_heavy` | 1993 | 757 | 27 | 38.0% |
| `starter_speed` | 1991 | 893 | 19 | 44.9% |

## Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 3638 |
| 2 | 押し込み | 2938 |
| 3 | 受け流し | 2352 |
| 4 | 構え | 1632 |
| 5 | 鉄壁 | 1530 |
| 6 | 踏ん張り | 1336 |
| 7 | 牽制 | 1310 |
| 8 | 低姿勢 | 1305 |
| 9 | 十字受け | 1202 |
| 10 | 加速 | 1199 |
| 11 | 渾身 | 1181 |
| 12 | 圧迫 | 1173 |
| 13 | 踏み込み | 1130 |
| 14 | 退き足 | 1110 |
| 15 | 蓄え | 1040 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 2378 |
| 2 | 押し込み | 1913 |
| 3 | 受け流し | 1329 |
| 4 | 構え | 996 |
| 5 | 鉄壁 | 875 |
| 6 | 低姿勢 | 795 |
| 7 | 踏み込み | 767 |
| 8 | 踏ん張り | 758 |
| 9 | 牽制 | 718 |
| 10 | 崩し | 687 |
| 11 | 貫き | 633 |
| 12 | 圧迫 | 630 |
| 13 | 加速 | 623 |
| 14 | 十字受け | 583 |
| 15 | 疾走 | 564 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 1757 |
| 2 | 押し込み | 1592 |
| 3 | 踏み込み | 663 |
| 4 | 崩し | 607 |
| 5 | 貫き | 553 |
| 6 | 疾走 | 477 |
| 7 | 低姿勢 | 405 |
| 8 | 踏ん張り | 381 |
| 9 | 渾身 | 356 |
| 10 | 受け流し | 354 |
| 11 | 大振り | 195 |
| 12 | 粉砕 | 191 |
| 13 | 十字受け | 170 |
| 14 | 鉄壁 | 143 |
| 15 | 残像 | 87 |

## Bot Details

### AttackBot

- Win Rate: 56.4%
- Draw Rate: 0.4%
- Turn Stats: min=1, avg=1.55, max=50
- Winning Attack Stats: min=1, avg=4.88, max=14
- Winning Block Stats: min=0, avg=1.11, max=9
- Winning Speed Stats: min=-5, avg=2.9, max=9

### Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | starter_balanced | 245 |
| 2 | starter_speed | 222 |
| 3 | starter_defense | 221 |
| 4 | starter_attack | 211 |
| 5 | starter_heavy | 188 |

### Most Used

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 488 |
| 2 | 押し込み | 441 |
| 3 | 集中 | 276 |
| 4 | 前のめり | 240 |
| 5 | 渾身 | 234 |
| 6 | 踏み込み | 215 |
| 7 | 加速 | 209 |
| 8 | 貫き | 207 |
| 9 | 圧迫 | 200 |
| 10 | 崩し | 198 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 343 |
| 2 | 返し刃 | 304 |
| 3 | 踏み込み | 168 |
| 4 | 貫き | 154 |
| 5 | 崩し | 148 |
| 6 | 前のめり | 125 |
| 7 | 圧迫 | 124 |
| 8 | 加速 | 122 |
| 9 | 集中 | 120 |
| 10 | 渾身 | 98 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 297 |
| 2 | 返し刃 | 255 |
| 3 | 踏み込み | 157 |
| 4 | 貫き | 139 |
| 5 | 崩し | 136 |
| 6 | 渾身 | 86 |
| 7 | 粉砕 | 39 |
| 8 | 大振り | 37 |
| 9 | 疾走 | 8 |
| 10 | 低姿勢 | 5 |

### BurstBot

- Win Rate: 49.4%
- Draw Rate: 0.5%
- Turn Stats: min=1, avg=1.6, max=50
- Winning Attack Stats: min=1, avg=3.72, max=12
- Winning Block Stats: min=0, avg=0.97, max=6
- Winning Speed Stats: min=-5, avg=2.86, max=14

### Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | starter_attack | 252 |
| 2 | starter_speed | 234 |
| 3 | starter_heavy | 221 |
| 4 | starter_balanced | 220 |
| 5 | starter_defense | 208 |

### Most Used

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 333 |
| 2 | 押し込み | 278 |
| 3 | 前のめり | 240 |
| 4 | 渾身 | 238 |
| 5 | 集中 | 236 |
| 6 | 圧迫 | 212 |
| 7 | 加速 | 193 |
| 8 | 貫き | 193 |
| 9 | 踏み込み | 166 |
| 10 | 疾走 | 166 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 215 |
| 2 | 押し込み | 199 |
| 3 | 前のめり | 122 |
| 4 | 圧迫 | 119 |
| 5 | 疾走 | 112 |
| 6 | 貫き | 109 |
| 7 | 加速 | 107 |
| 8 | 崩し | 105 |
| 9 | 踏み込み | 105 |
| 10 | 集中 | 101 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 187 |
| 2 | 返し刃 | 181 |
| 3 | 疾走 | 100 |
| 4 | 崩し | 98 |
| 5 | 貫き | 85 |
| 6 | 踏み込み | 81 |
| 7 | 渾身 | 59 |
| 8 | 粉砕 | 33 |
| 9 | 大振り | 26 |
| 10 | 低姿勢 | 14 |

### DefenseBot

- Win Rate: 60.5%
- Draw Rate: 0.4%
- Turn Stats: min=1, avg=2.45, max=50
- Winning Attack Stats: min=1, avg=2.41, max=6
- Winning Block Stats: min=0, avg=3.53, max=11
- Winning Speed Stats: min=-3, avg=2.17, max=16

### Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | starter_heavy | 229 |
| 2 | starter_speed | 212 |
| 3 | starter_attack | 211 |
| 4 | starter_defense | 205 |
| 5 | starter_balanced | 193 |

### Most Used

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 561 |
| 2 | 押し込み | 535 |
| 3 | 受け流し | 466 |
| 4 | 構え | 439 |
| 5 | 鉄壁 | 407 |
| 6 | 蓄え | 356 |
| 7 | 牽制 | 353 |
| 8 | 踏ん張り | 281 |
| 9 | 補強 | 280 |
| 10 | 低姿勢 | 280 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 444 |
| 2 | 受け流し | 357 |
| 3 | 押し込み | 357 |
| 4 | 構え | 319 |
| 5 | 鉄壁 | 300 |
| 6 | 踏ん張り | 216 |
| 7 | 牽制 | 215 |
| 8 | 低姿勢 | 213 |
| 9 | 補強 | 194 |
| 10 | 蓄え | 194 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 306 |
| 2 | 押し込み | 281 |
| 3 | 踏ん張り | 108 |
| 4 | 低姿勢 | 105 |
| 5 | 受け流し | 101 |
| 6 | 十字受け | 57 |
| 7 | 鉄壁 | 46 |
| 8 | 残像 | 34 |
| 9 | 粉砕 | 33 |
| 10 | 退き足 | 31 |

### DisruptBot

- Win Rate: 51.8%
- Draw Rate: 1.8%
- Turn Stats: min=1, avg=2.57, max=50
- Winning Attack Stats: min=1, avg=3.27, max=9
- Winning Block Stats: min=0, avg=0.63, max=3
- Winning Speed Stats: min=-3, avg=3.16, max=13

### Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | starter_speed | 238 |
| 2 | starter_heavy | 236 |
| 3 | starter_attack | 234 |
| 4 | starter_defense | 219 |
| 5 | starter_balanced | 209 |

### Most Used

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 339 |
| 2 | 返し刃 | 263 |
| 3 | 加速 | 234 |
| 4 | 疾走 | 232 |
| 5 | 牽制 | 216 |
| 6 | 受け流し | 188 |
| 7 | 圧迫 | 187 |
| 8 | 貫き | 180 |
| 9 | 踏み込み | 165 |
| 10 | 崩し | 165 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 248 |
| 2 | 疾走 | 168 |
| 3 | 返し刃 | 144 |
| 4 | 加速 | 131 |
| 5 | 貫き | 130 |
| 6 | 踏み込み | 130 |
| 7 | 崩し | 124 |
| 8 | 牽制 | 109 |
| 9 | 圧迫 | 101 |
| 10 | 受け流し | 71 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 214 |
| 2 | 疾走 | 143 |
| 3 | 貫き | 117 |
| 4 | 崩し | 111 |
| 5 | 踏み込み | 107 |
| 6 | 返し刃 | 85 |
| 7 | 渾身 | 34 |
| 8 | 粉砕 | 22 |
| 9 | 大振り | 20 |
| 10 | 踏ん張り | 16 |

### GreedyBot

- Win Rate: 38.8%
- Draw Rate: 2.1%
- Turn Stats: min=1, avg=2.61, max=50
- Winning Attack Stats: min=1, avg=2.77, max=7
- Winning Block Stats: min=0, avg=1.34, max=9
- Winning Speed Stats: min=-4, avg=1.97, max=18

### Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | starter_balanced | 251 |
| 2 | starter_speed | 229 |
| 3 | starter_heavy | 220 |
| 4 | starter_defense | 219 |
| 5 | starter_attack | 212 |

### Most Used

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 292 |
| 2 | 受け流し | 227 |
| 3 | 圧迫 | 216 |
| 4 | 押し込み | 209 |
| 5 | 渾身 | 186 |
| 6 | 貫き | 147 |
| 7 | 鉄壁 | 138 |
| 8 | 崩し | 130 |
| 9 | 退き足 | 126 |
| 10 | 踏み込み | 122 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 154 |
| 2 | 押し込み | 123 |
| 3 | 圧迫 | 98 |
| 4 | 崩し | 76 |
| 5 | 受け流し | 75 |
| 6 | 踏み込み | 62 |
| 7 | 貫き | 59 |
| 8 | 渾身 | 56 |
| 9 | 疾走 | 51 |
| 10 | 踏ん張り | 47 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 128 |
| 2 | 押し込み | 102 |
| 3 | 崩し | 67 |
| 4 | 踏み込み | 51 |
| 5 | 貫き | 48 |
| 6 | 渾身 | 45 |
| 7 | 疾走 | 42 |
| 8 | 踏ん張り | 29 |
| 9 | 受け流し | 25 |
| 10 | 低姿勢 | 22 |

### RandomBot

- Win Rate: 46.7%
- Draw Rate: 1.9%
- Turn Stats: min=1, avg=2.66, max=50
- Winning Attack Stats: min=1, avg=3.1, max=11
- Winning Block Stats: min=0, avg=1.67, max=12
- Winning Speed Stats: min=-4, avg=2.24, max=12

### Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | starter_attack | 234 |
| 2 | starter_defense | 234 |
| 3 | starter_speed | 233 |
| 4 | starter_balanced | 216 |
| 5 | starter_heavy | 211 |

### Most Used

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 328 |
| 2 | 受け流し | 310 |
| 3 | 押し込み | 218 |
| 4 | 鉄壁 | 210 |
| 5 | 構え | 206 |
| 6 | 退き足 | 170 |
| 7 | 低姿勢 | 153 |
| 8 | 蓄え | 153 |
| 9 | 踏ん張り | 150 |
| 10 | 十字受け | 147 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 192 |
| 2 | 受け流し | 147 |
| 3 | 押し込み | 139 |
| 4 | 鉄壁 | 94 |
| 5 | 構え | 92 |
| 6 | 低姿勢 | 89 |
| 7 | 踏み込み | 86 |
| 8 | 疾走 | 76 |
| 9 | 崩し | 75 |
| 10 | 踏ん張り | 74 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 153 |
| 2 | 押し込み | 108 |
| 3 | 踏み込み | 77 |
| 4 | 疾走 | 64 |
| 5 | 崩し | 60 |
| 6 | 貫き | 56 |
| 7 | 渾身 | 54 |
| 8 | 低姿勢 | 49 |
| 9 | 受け流し | 46 |
| 10 | 踏ん張り | 45 |

### RiskBot

- Win Rate: 54.7%
- Draw Rate: 1.2%
- Turn Stats: min=1, avg=2.38, max=50
- Winning Attack Stats: min=1, avg=3.13, max=13
- Winning Block Stats: min=0, avg=2.5, max=11
- Winning Speed Stats: min=-4, avg=1.31, max=10

### Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | starter_defense | 238 |
| 2 | starter_heavy | 236 |
| 3 | starter_balanced | 225 |
| 4 | starter_attack | 220 |
| 5 | starter_speed | 209 |

### Most Used

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 488 |
| 2 | 構え | 396 |
| 3 | 受け流し | 393 |
| 4 | 押し込み | 315 |
| 5 | 鉄壁 | 288 |
| 6 | 牽制 | 249 |
| 7 | 踏ん張り | 217 |
| 8 | 低姿勢 | 209 |
| 9 | 渾身 | 197 |
| 10 | 補強 | 196 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 376 |
| 2 | 受け流し | 282 |
| 3 | 構え | 251 |
| 4 | 押し込み | 192 |
| 5 | 鉄壁 | 178 |
| 6 | 低姿勢 | 148 |
| 7 | 牽制 | 143 |
| 8 | 踏ん張り | 136 |
| 9 | 補強 | 116 |
| 10 | 貫き | 96 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 260 |
| 2 | 押し込み | 151 |
| 3 | 受け流し | 98 |
| 4 | 低姿勢 | 88 |
| 5 | 貫き | 87 |
| 6 | 踏み込み | 79 |
| 7 | 踏ん張り | 72 |
| 8 | 大振り | 52 |
| 9 | 渾身 | 50 |
| 10 | 鉄壁 | 39 |

### TempoBot

- Win Rate: 42.6%
- Draw Rate: 1.3%
- Turn Stats: min=1, avg=2.36, max=50
- Winning Attack Stats: min=1, avg=2.8, max=9
- Winning Block Stats: min=0, avg=0.9, max=5
- Winning Speed Stats: min=-2, avg=3.49, max=18

### Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | starter_attack | 238 |
| 2 | starter_defense | 234 |
| 3 | starter_heavy | 223 |
| 4 | starter_balanced | 216 |
| 5 | starter_speed | 187 |

### Most Used

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 281 |
| 2 | 加速 | 270 |
| 3 | 受け流し | 258 |
| 4 | 返し刃 | 245 |
| 5 | 疾走 | 196 |
| 6 | 踏み込み | 188 |
| 7 | 十字受け | 184 |
| 8 | 圧迫 | 164 |
| 9 | 崩し | 147 |
| 10 | 勢い溜め | 141 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 185 |
| 2 | 返し刃 | 126 |
| 3 | 加速 | 123 |
| 4 | 踏み込み | 121 |
| 5 | 疾走 | 114 |
| 6 | 崩し | 109 |
| 7 | 受け流し | 88 |
| 8 | 圧迫 | 81 |
| 9 | 十字受け | 75 |
| 10 | 勢い溜め | 63 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 148 |
| 2 | 踏み込み | 107 |
| 3 | 疾走 | 97 |
| 4 | 崩し | 94 |
| 5 | 返し刃 | 87 |
| 6 | 十字受け | 29 |
| 7 | 残像 | 24 |
| 8 | 渾身 | 23 |
| 9 | 貫き | 17 |
| 10 | 低姿勢 | 16 |

### TurtleBot

- Win Rate: 43.2%
- Draw Rate: 3.7%
- Turn Stats: min=1, avg=4.05, max=50
- Winning Attack Stats: min=1, avg=1.98, max=5
- Winning Block Stats: min=0, avg=3.85, max=11
- Winning Speed Stats: min=-3, avg=1.2, max=7

### Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | starter_balanced | 240 |
| 2 | starter_heavy | 229 |
| 3 | starter_speed | 227 |
| 4 | starter_attack | 211 |
| 5 | starter_defense | 200 |

### Most Used

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 640 |
| 2 | 受け流し | 488 |
| 3 | 構え | 443 |
| 4 | 蓄え | 424 |
| 5 | 鉄壁 | 396 |
| 6 | 押し込み | 322 |
| 7 | 補強 | 319 |
| 8 | 牽制 | 305 |
| 9 | 踏ん張り | 296 |
| 10 | 低姿勢 | 280 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 423 |
| 2 | 受け流し | 304 |
| 3 | 構え | 266 |
| 4 | 鉄壁 | 228 |
| 5 | 低姿勢 | 178 |
| 6 | 踏ん張り | 175 |
| 7 | 補強 | 175 |
| 8 | 蓄え | 167 |
| 9 | 牽制 | 147 |
| 10 | 押し込み | 127 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 302 |
| 2 | 押し込み | 104 |
| 3 | 低姿勢 | 93 |
| 4 | 踏ん張り | 90 |
| 5 | 受け流し | 84 |
| 6 | 十字受け | 39 |
| 7 | 鉄壁 | 34 |
| 8 | 退き足 | 20 |
| 9 | 渾身 | 3 |
| 10 | 大振り | 2 |
