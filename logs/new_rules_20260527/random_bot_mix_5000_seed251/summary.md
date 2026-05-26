# Random Bot Mix Report

## Configuration

- Matches: 5000
- Seed: 251
- Selection Mode: p1/p2 bot and deck selected independently at random
- Bot Pool: `AttackBot`, `BurstBot`, `DefenseBot`, `DisruptBot`, `GreedyBot`, `RandomBot`, `RiskBot`, `TempoBot`, `TurtleBot`
- Deck Pool: `starter_attack`, `starter_balanced`, `starter_defense`, `starter_heavy`, `starter_speed`

## Bot Win Rates

| Bot | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Card Win | Set Rate | Set+Pass Rate | Pass Rate | Turn Min | Turn Avg | Turn Max | Win A Avg | Win B Avg | Win S Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `AttackBot` | 1112 | 518 | 487 | 107 | 46.6% | 33.0% | 10.8% | 32.3% | 40.4% | 27.4% | 1 | 1.66 | 50 | 4.86 | 1.26 | 2.91 |
| `BurstBot` | 1076 | 484 | 490 | 102 | 45.0% | 35.1% | 9.5% | 24.8% | 61.9% | 13.2% | 1 | 1.46 | 50 | 3.99 | 0.92 | 2.71 |
| `DefenseBot` | 1037 | 600 | 379 | 58 | 57.9% | 34.3% | 5.7% | 30.8% | 50.4% | 18.9% | 1 | 2.79 | 50 | 2.48 | 3.23 | 1.96 |
| `DisruptBot` | 1121 | 538 | 500 | 83 | 48.0% | 32.2% | 8.6% | 15.8% | 64.0% | 20.3% | 1 | 2.22 | 50 | 3.61 | 0.73 | 3.98 |
| `GreedyBot` | 1101 | 398 | 601 | 102 | 36.1% | 21.8% | 6.8% | 24.5% | 46.3% | 29.2% | 1 | 2.04 | 50 | 3.07 | 1.81 | 2.32 |
| `RandomBot` | 1172 | 534 | 553 | 85 | 45.6% | 31.2% | 6.6% | 26.6% | 59.0% | 14.4% | 1 | 2.27 | 50 | 3.1 | 1.68 | 2.54 |
| `RiskBot` | 1085 | 525 | 470 | 90 | 48.4% | 31.1% | 6.5% | 27.2% | 48.0% | 24.7% | 1 | 2.62 | 50 | 3.42 | 2.66 | 1.53 |
| `TempoBot` | 1170 | 487 | 601 | 82 | 41.6% | 29.1% | 8.2% | 13.6% | 70.9% | 15.5% | 1 | 2.26 | 50 | 2.78 | 0.84 | 3.96 |
| `TurtleBot` | 1126 | 514 | 517 | 95 | 45.6% | 29.4% | 5.8% | 22.2% | 51.2% | 26.6% | 1 | 3.44 | 50 | 2.13 | 3.54 | 1.09 |

## Bot Pair Summary

| Pair | Matches | Draws | Wins | Turn Min | Turn Avg | Turn Max |
|---|---:|---:|---|---:|---:|---:|
| AttackBot vs AttackBot | 59 | 12 | `AttackBot`=47 | 1 | 1.92 | 50 |
| AttackBot vs BurstBot | 122 | 12 | `AttackBot`=68, `BurstBot`=42 | 1 | 1.07 | 4 |
| AttackBot vs DefenseBot | 118 | 9 | `AttackBot`=39, `DefenseBot`=70 | 1 | 1.47 | 9 |
| AttackBot vs DisruptBot | 127 | 7 | `AttackBot`=62, `DisruptBot`=58 | 1 | 1.19 | 5 |
| AttackBot vs GreedyBot | 136 | 13 | `AttackBot`=84, `GreedyBot`=39 | 1 | 1.43 | 50 |
| AttackBot vs RandomBot | 119 | 13 | `AttackBot`=45, `RandomBot`=61 | 1 | 2.24 | 50 |
| AttackBot vs RiskBot | 134 | 12 | `AttackBot`=58, `RiskBot`=64 | 1 | 1.61 | 50 |
| AttackBot vs TempoBot | 111 | 6 | `AttackBot`=57, `TempoBot`=48 | 1 | 1.23 | 5 |
| AttackBot vs TurtleBot | 127 | 11 | `AttackBot`=58, `TurtleBot`=58 | 1 | 2.8 | 50 |
| BurstBot vs BurstBot | 59 | 6 | `BurstBot`=53 | 1 | 1.92 | 50 |
| BurstBot vs DefenseBot | 123 | 5 | `BurstBot`=47, `DefenseBot`=71 | 1 | 1.7 | 9 |
| BurstBot vs DisruptBot | 119 | 12 | `BurstBot`=56, `DisruptBot`=51 | 1 | 1.18 | 6 |
| BurstBot vs GreedyBot | 123 | 17 | `BurstBot`=64, `GreedyBot`=42 | 1 | 1.55 | 50 |
| BurstBot vs RandomBot | 106 | 10 | `BurstBot`=55, `RandomBot`=41 | 1 | 1.21 | 7 |
| BurstBot vs RiskBot | 100 | 10 | `BurstBot`=39, `RiskBot`=51 | 1 | 1.4 | 7 |
| BurstBot vs TempoBot | 136 | 11 | `BurstBot`=68, `TempoBot`=57 | 1 | 1.31 | 6 |
| BurstBot vs TurtleBot | 129 | 13 | `BurstBot`=60, `TurtleBot`=56 | 1 | 1.74 | 7 |
| DefenseBot vs DefenseBot | 47 | 2 | `DefenseBot`=45 | 1 | 3.72 | 8 |
| DefenseBot vs DisruptBot | 96 | 3 | `DefenseBot`=51, `DisruptBot`=42 | 1 | 3.46 | 50 |
| DefenseBot vs GreedyBot | 128 | 4 | `DefenseBot`=91, `GreedyBot`=33 | 1 | 2.15 | 9 |
| DefenseBot vs RandomBot | 115 | 7 | `DefenseBot`=71, `RandomBot`=37 | 1 | 3.04 | 50 |
| DefenseBot vs RiskBot | 109 | 4 | `DefenseBot`=61, `RiskBot`=44 | 1 | 2.57 | 9 |
| DefenseBot vs TempoBot | 129 | 13 | `DefenseBot`=85, `TempoBot`=31 | 1 | 3.76 | 50 |
| DefenseBot vs TurtleBot | 125 | 9 | `DefenseBot`=55, `TurtleBot`=61 | 1 | 3.54 | 9 |
| DisruptBot vs DisruptBot | 64 | 6 | `DisruptBot`=58 | 1 | 3.17 | 50 |
| DisruptBot vs GreedyBot | 118 | 12 | `DisruptBot`=62, `GreedyBot`=44 | 1 | 2.19 | 50 |
| DisruptBot vs RandomBot | 129 | 6 | `DisruptBot`=57, `RandomBot`=66 | 1 | 2.22 | 50 |
| DisruptBot vs RiskBot | 125 | 16 | `DisruptBot`=57, `RiskBot`=52 | 1 | 2.63 | 50 |
| DisruptBot vs TempoBot | 165 | 7 | `DisruptBot`=98, `TempoBot`=60 | 1 | 1.59 | 10 |
| DisruptBot vs TurtleBot | 114 | 8 | `DisruptBot`=55, `TurtleBot`=51 | 1 | 2.8 | 50 |
| GreedyBot vs GreedyBot | 53 | 8 | `GreedyBot`=45 | 1 | 3.19 | 50 |
| GreedyBot vs RandomBot | 149 | 10 | `GreedyBot`=64, `RandomBot`=75 | 1 | 1.6 | 10 |
| GreedyBot vs RiskBot | 120 | 13 | `GreedyBot`=43, `RiskBot`=64 | 1 | 1.66 | 50 |
| GreedyBot vs TempoBot | 116 | 9 | `GreedyBot`=51, `TempoBot`=56 | 1 | 2.57 | 50 |
| GreedyBot vs TurtleBot | 105 | 8 | `GreedyBot`=37, `TurtleBot`=60 | 1 | 2.37 | 50 |
| RandomBot vs RandomBot | 62 | 5 | `RandomBot`=57 | 1 | 2.5 | 50 |
| RandomBot vs RiskBot | 136 | 8 | `RandomBot`=54, `RiskBot`=74 | 1 | 2.38 | 50 |
| RandomBot vs TempoBot | 139 | 9 | `RandomBot`=66, `TempoBot`=64 | 1 | 1.99 | 10 |
| RandomBot vs TurtleBot | 155 | 12 | `RandomBot`=77, `TurtleBot`=66 | 1 | 3.14 | 50 |
| RiskBot vs RiskBot | 59 | 7 | `RiskBot`=52 | 1 | 5.02 | 50 |
| RiskBot vs TempoBot | 132 | 6 | `RiskBot`=67, `TempoBot`=59 | 1 | 2.78 | 50 |
| RiskBot vs TurtleBot | 111 | 7 | `RiskBot`=57, `TurtleBot`=47 | 1 | 3.61 | 50 |
| TempoBot vs TempoBot | 55 | 6 | `TempoBot`=49 | 1 | 2.07 | 8 |
| TempoBot vs TurtleBot | 132 | 9 | `TempoBot`=63, `TurtleBot`=60 | 1 | 3.15 | 9 |
| TurtleBot vs TurtleBot | 64 | 9 | `TurtleBot`=55 | 1 | 7.62 | 50 |

## Deck Usage Summary

| Deck | Matches | Wins | Draws | Win Rate |
|---|---:|---:|---:|---:|
| `starter_attack` | 1962 | 902 | 190 | 46.0% |
| `starter_balanced` | 2074 | 1078 | 216 | 52.0% |
| `starter_defense` | 2041 | 1085 | 155 | 53.2% |
| `starter_heavy` | 1893 | 620 | 90 | 32.8% |
| `starter_speed` | 2030 | 913 | 153 | 45.0% |

## Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 4678 |
| 2 | 押し込み | 3651 |
| 3 | 受け流し | 2903 |
| 4 | 構え | 2057 |
| 5 | 鉄壁 | 1800 |
| 6 | 踏ん張り | 1706 |
| 7 | 十字受け | 1559 |
| 8 | 牽制 | 1548 |
| 9 | 低姿勢 | 1515 |
| 10 | 退き足 | 1464 |
| 11 | 加速 | 1434 |
| 12 | 圧迫 | 1405 |
| 13 | 貫き | 1286 |
| 14 | 渾身 | 1278 |
| 15 | 踏み込み | 1264 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 2658 |
| 2 | 押し込み | 1919 |
| 3 | 受け流し | 1515 |
| 4 | 構え | 1194 |
| 5 | 鉄壁 | 946 |
| 6 | 踏ん張り | 891 |
| 7 | 低姿勢 | 810 |
| 8 | 牽制 | 774 |
| 9 | 加速 | 737 |
| 10 | 補強 | 684 |
| 11 | 崩し | 673 |
| 12 | 踏み込み | 668 |
| 13 | 圧迫 | 666 |
| 14 | 十字受け | 650 |
| 15 | 貫き | 630 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 1728 |
| 2 | 押し込み | 1517 |
| 3 | 崩し | 629 |
| 4 | 踏み込み | 621 |
| 5 | 貫き | 592 |
| 6 | 疾走 | 482 |
| 7 | 踏ん張り | 421 |
| 8 | 低姿勢 | 370 |
| 9 | 渾身 | 296 |
| 10 | 受け流し | 288 |
| 11 | 粉砕 | 188 |
| 12 | 十字受け | 187 |
| 13 | 大振り | 160 |
| 14 | 鉄壁 | 120 |
| 15 | 退き足 | 115 |

## Bot Details

### AttackBot

- Win Rate: 46.6%
- Draw Rate: 9.6%
- First Pass Win Rate: 33.0%
- Win With Fewer Cards: 10.8%
- Win With Same Cards: 45.8%
- Win With More Cards: 43.4%
- Action Rates: set=32.3%, set_pass=40.4%, pass=27.4%
- Turn Stats: min=1, avg=1.66, max=50
- Winning Attack Stats: min=1, avg=4.86, max=16
- Winning Block Stats: min=0, avg=1.26, max=9
- Winning Speed Stats: min=-6, avg=2.91, max=13

### Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | starter_speed | 239 |
| 2 | starter_balanced | 230 |
| 3 | starter_defense | 222 |
| 4 | starter_heavy | 215 |
| 5 | starter_attack | 206 |

### Most Used

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 608 |
| 2 | 押し込み | 469 |
| 3 | 前のめり | 368 |
| 4 | 集中 | 319 |
| 5 | 貫き | 251 |
| 6 | 崩し | 231 |
| 7 | 渾身 | 227 |
| 8 | 圧迫 | 205 |
| 9 | 踏み込み | 192 |
| 10 | 加速 | 173 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 297 |
| 2 | 押し込み | 272 |
| 3 | 前のめり | 179 |
| 4 | 崩し | 139 |
| 5 | 貫き | 127 |
| 6 | 集中 | 121 |
| 7 | 圧迫 | 107 |
| 8 | 踏み込み | 94 |
| 9 | 加速 | 81 |
| 10 | 渾身 | 51 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 245 |
| 2 | 押し込み | 243 |
| 3 | 崩し | 129 |
| 4 | 貫き | 126 |
| 5 | 踏み込み | 89 |
| 6 | 渾身 | 49 |
| 7 | 粉砕 | 43 |
| 8 | 大振り | 33 |
| 9 | 低姿勢 | 6 |
| 10 | 踏ん張り | 6 |

### BurstBot

- Win Rate: 45.0%
- Draw Rate: 9.5%
- First Pass Win Rate: 35.1%
- Win With Fewer Cards: 9.5%
- Win With Same Cards: 58.1%
- Win With More Cards: 32.4%
- Action Rates: set=24.8%, set_pass=61.9%, pass=13.2%
- Turn Stats: min=1, avg=1.46, max=50
- Winning Attack Stats: min=1, avg=3.99, max=15
- Winning Block Stats: min=0, avg=0.92, max=8
- Winning Speed Stats: min=-5, avg=2.71, max=19

### Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | starter_balanced | 226 |
| 2 | starter_defense | 226 |
| 3 | starter_attack | 211 |
| 4 | starter_speed | 209 |
| 5 | starter_heavy | 204 |

### Most Used

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 457 |
| 2 | 集中 | 300 |
| 3 | 前のめり | 292 |
| 4 | 貫き | 248 |
| 5 | 渾身 | 241 |
| 6 | 圧迫 | 218 |
| 7 | 押し込み | 212 |
| 8 | 加速 | 209 |
| 9 | 踏み込み | 197 |
| 10 | 疾走 | 134 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 231 |
| 2 | 前のめり | 146 |
| 3 | 押し込み | 131 |
| 4 | 貫き | 119 |
| 5 | 加速 | 114 |
| 6 | 集中 | 114 |
| 7 | 圧迫 | 97 |
| 8 | 踏み込み | 89 |
| 9 | 疾走 | 82 |
| 10 | 崩し | 71 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 167 |
| 2 | 貫き | 114 |
| 3 | 押し込み | 107 |
| 4 | 踏み込み | 84 |
| 5 | 崩し | 67 |
| 6 | 疾走 | 67 |
| 7 | 渾身 | 61 |
| 8 | 粉砕 | 36 |
| 9 | 踏ん張り | 23 |
| 10 | 大振り | 22 |

### DefenseBot

- Win Rate: 57.9%
- Draw Rate: 5.6%
- First Pass Win Rate: 34.3%
- Win With Fewer Cards: 5.7%
- Win With Same Cards: 43.3%
- Win With More Cards: 51.0%
- Action Rates: set=30.8%, set_pass=50.4%, pass=18.9%
- Turn Stats: min=1, avg=2.79, max=50
- Winning Attack Stats: min=1, avg=2.48, max=9
- Winning Block Stats: min=0, avg=3.23, max=13
- Winning Speed Stats: min=-3, avg=1.96, max=11

### Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | starter_balanced | 227 |
| 2 | starter_defense | 209 |
| 3 | starter_attack | 207 |
| 4 | starter_speed | 204 |
| 5 | starter_heavy | 190 |

### Most Used

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 707 |
| 2 | 押し込み | 698 |
| 3 | 構え | 544 |
| 4 | 受け流し | 523 |
| 5 | 牽制 | 442 |
| 6 | 鉄壁 | 432 |
| 7 | 蓄え | 430 |
| 8 | 踏ん張り | 349 |
| 9 | 十字受け | 332 |
| 10 | 低姿勢 | 330 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 494 |
| 2 | 押し込み | 370 |
| 3 | 構え | 357 |
| 4 | 受け流し | 344 |
| 5 | 鉄壁 | 272 |
| 6 | 牽制 | 255 |
| 7 | 踏ん張り | 221 |
| 8 | 低姿勢 | 210 |
| 9 | 補強 | 201 |
| 10 | 蓄え | 191 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 297 |
| 2 | 押し込み | 270 |
| 3 | 低姿勢 | 91 |
| 4 | 踏ん張り | 87 |
| 5 | 受け流し | 70 |
| 6 | 十字受け | 53 |
| 7 | 粉砕 | 35 |
| 8 | 退き足 | 34 |
| 9 | 鉄壁 | 30 |
| 10 | 踏み込み | 9 |

### DisruptBot

- Win Rate: 48.0%
- Draw Rate: 7.4%
- First Pass Win Rate: 32.2%
- Win With Fewer Cards: 8.6%
- Win With Same Cards: 47.6%
- Win With More Cards: 43.9%
- Action Rates: set=15.8%, set_pass=64.0%, pass=20.3%
- Turn Stats: min=1, avg=2.22, max=50
- Winning Attack Stats: min=1, avg=3.61, max=12
- Winning Block Stats: min=0, avg=0.73, max=4
- Winning Speed Stats: min=-2, avg=3.98, max=17

### Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | starter_balanced | 247 |
| 2 | starter_attack | 229 |
| 3 | starter_defense | 220 |
| 4 | starter_speed | 218 |
| 5 | starter_heavy | 207 |

### Most Used

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 435 |
| 2 | 返し刃 | 320 |
| 3 | 圧迫 | 294 |
| 4 | 加速 | 261 |
| 5 | 疾走 | 257 |
| 6 | 牽制 | 245 |
| 7 | 受け流し | 240 |
| 8 | 崩し | 220 |
| 9 | 踏み込み | 217 |
| 10 | 貫き | 210 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 270 |
| 2 | 疾走 | 175 |
| 3 | 圧迫 | 162 |
| 4 | 返し刃 | 156 |
| 5 | 踏み込み | 143 |
| 6 | 崩し | 141 |
| 7 | 加速 | 135 |
| 8 | 貫き | 127 |
| 9 | 牽制 | 100 |
| 10 | 重心落とし | 80 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 225 |
| 2 | 疾走 | 154 |
| 3 | 踏み込み | 135 |
| 4 | 崩し | 133 |
| 5 | 貫き | 121 |
| 6 | 返し刃 | 88 |
| 7 | 踏ん張り | 24 |
| 8 | 粉砕 | 19 |
| 9 | 渾身 | 19 |
| 10 | 退き足 | 15 |

### GreedyBot

- Win Rate: 36.1%
- Draw Rate: 9.3%
- First Pass Win Rate: 21.8%
- Win With Fewer Cards: 6.8%
- Win With Same Cards: 51.5%
- Win With More Cards: 41.7%
- Action Rates: set=24.5%, set_pass=46.3%, pass=29.2%
- Turn Stats: min=1, avg=2.04, max=50
- Winning Attack Stats: min=1, avg=3.07, max=13
- Winning Block Stats: min=0, avg=1.81, max=11
- Winning Speed Stats: min=-4, avg=2.32, max=16

### Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | starter_heavy | 231 |
| 2 | starter_balanced | 230 |
| 3 | starter_speed | 224 |
| 4 | starter_attack | 208 |
| 5 | starter_defense | 208 |

### Most Used

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 332 |
| 2 | 圧迫 | 265 |
| 3 | 受け流し | 246 |
| 4 | 渾身 | 234 |
| 5 | 押し込み | 222 |
| 6 | 貫き | 170 |
| 7 | 踏み込み | 143 |
| 8 | 十字受け | 143 |
| 9 | 鉄壁 | 137 |
| 10 | 踏ん張り | 132 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 169 |
| 2 | 押し込み | 131 |
| 3 | 圧迫 | 98 |
| 4 | 受け流し | 86 |
| 5 | 崩し | 70 |
| 6 | 踏ん張り | 67 |
| 7 | 踏み込み | 64 |
| 8 | 十字受け | 53 |
| 9 | 貫き | 53 |
| 10 | 低姿勢 | 49 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 134 |
| 2 | 押し込み | 113 |
| 3 | 崩し | 67 |
| 4 | 踏み込み | 58 |
| 5 | 貫き | 45 |
| 6 | 踏ん張り | 44 |
| 7 | 疾走 | 40 |
| 8 | 受け流し | 38 |
| 9 | 渾身 | 38 |
| 10 | 低姿勢 | 31 |

### RandomBot

- Win Rate: 45.6%
- Draw Rate: 7.3%
- First Pass Win Rate: 31.2%
- Win With Fewer Cards: 6.6%
- Win With Same Cards: 44.2%
- Win With More Cards: 49.3%
- Action Rates: set=26.6%, set_pass=59.0%, pass=14.4%
- Turn Stats: min=1, avg=2.27, max=50
- Winning Attack Stats: min=1, avg=3.1, max=15
- Winning Block Stats: min=0, avg=1.68, max=11
- Winning Speed Stats: min=-7, avg=2.54, max=17

### Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | starter_defense | 253 |
| 2 | starter_speed | 247 |
| 3 | starter_balanced | 244 |
| 4 | starter_attack | 237 |
| 5 | starter_heavy | 191 |

### Most Used

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 499 |
| 2 | 受け流し | 433 |
| 3 | 鉄壁 | 319 |
| 4 | 構え | 308 |
| 5 | 押し込み | 278 |
| 6 | 退き足 | 228 |
| 7 | 加速 | 199 |
| 8 | 踏ん張り | 199 |
| 9 | 集中 | 196 |
| 10 | 低姿勢 | 191 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 325 |
| 2 | 受け流し | 260 |
| 3 | 鉄壁 | 188 |
| 4 | 構え | 184 |
| 5 | 押し込み | 156 |
| 6 | 退き足 | 128 |
| 7 | 加速 | 119 |
| 8 | 低姿勢 | 118 |
| 9 | 踏ん張り | 115 |
| 10 | 十字受け | 101 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 170 |
| 2 | 押し込み | 115 |
| 3 | 崩し | 85 |
| 4 | 貫き | 80 |
| 5 | 踏み込み | 67 |
| 6 | 疾走 | 63 |
| 7 | 低姿勢 | 48 |
| 8 | 踏ん張り | 45 |
| 9 | 渾身 | 39 |
| 10 | 受け流し | 38 |

### RiskBot

- Win Rate: 48.4%
- Draw Rate: 8.3%
- First Pass Win Rate: 31.1%
- Win With Fewer Cards: 6.5%
- Win With Same Cards: 37.5%
- Win With More Cards: 56.0%
- Action Rates: set=27.2%, set_pass=48.0%, pass=24.7%
- Turn Stats: min=1, avg=2.62, max=50
- Winning Attack Stats: min=1, avg=3.42, max=12
- Winning Block Stats: min=0, avg=2.66, max=14
- Winning Speed Stats: min=-6, avg=1.53, max=9

### Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | starter_speed | 229 |
| 2 | starter_heavy | 225 |
| 3 | starter_balanced | 213 |
| 4 | starter_defense | 210 |
| 5 | starter_attack | 208 |

### Most Used

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 573 |
| 2 | 構え | 468 |
| 3 | 受け流し | 430 |
| 4 | 押し込み | 411 |
| 5 | 鉄壁 | 341 |
| 6 | 補強 | 261 |
| 7 | 踏ん張り | 257 |
| 8 | 牽制 | 256 |
| 9 | 低姿勢 | 247 |
| 10 | 渾身 | 232 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 353 |
| 2 | 構え | 274 |
| 3 | 受け流し | 244 |
| 4 | 押し込み | 195 |
| 5 | 鉄壁 | 178 |
| 6 | 補強 | 143 |
| 7 | 踏ん張り | 138 |
| 8 | 低姿勢 | 136 |
| 9 | 牽制 | 127 |
| 10 | 貫き | 83 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 245 |
| 2 | 押し込み | 157 |
| 3 | 貫き | 81 |
| 4 | 踏ん張り | 67 |
| 5 | 低姿勢 | 62 |
| 6 | 踏み込み | 62 |
| 7 | 受け流し | 58 |
| 8 | 渾身 | 58 |
| 9 | 大振り | 47 |
| 10 | 鉄壁 | 37 |

### TempoBot

- Win Rate: 41.6%
- Draw Rate: 7.0%
- First Pass Win Rate: 29.1%
- Win With Fewer Cards: 8.2%
- Win With Same Cards: 55.6%
- Win With More Cards: 36.1%
- Action Rates: set=13.6%, set_pass=70.9%, pass=15.5%
- Turn Stats: min=1, avg=2.26, max=50
- Winning Attack Stats: min=1, avg=2.78, max=10
- Winning Block Stats: min=0, avg=0.84, max=5
- Winning Speed Stats: min=-2, avg=3.96, max=18

### Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | starter_defense | 265 |
| 2 | starter_speed | 242 |
| 3 | starter_balanced | 233 |
| 4 | starter_attack | 217 |
| 5 | starter_heavy | 213 |

### Most Used

| Rank | Name | Count |
|---:|---|---:|
| 1 | 加速 | 442 |
| 2 | 押し込み | 431 |
| 3 | 受け流し | 385 |
| 4 | 返し刃 | 328 |
| 5 | 疾走 | 286 |
| 6 | 十字受け | 268 |
| 7 | 崩し | 207 |
| 8 | 踏み込み | 203 |
| 9 | 圧迫 | 196 |
| 10 | 退き足 | 172 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 234 |
| 2 | 加速 | 208 |
| 3 | 疾走 | 154 |
| 4 | 返し刃 | 143 |
| 5 | 受け流し | 134 |
| 6 | 崩し | 121 |
| 7 | 踏み込み | 110 |
| 8 | 圧迫 | 91 |
| 9 | 十字受け | 90 |
| 10 | 重心落とし | 65 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 191 |
| 2 | 疾走 | 124 |
| 3 | 崩し | 112 |
| 4 | 踏み込み | 107 |
| 5 | 返し刃 | 75 |
| 6 | 十字受け | 29 |
| 7 | 低姿勢 | 20 |
| 8 | 渾身 | 16 |
| 9 | 貫き | 15 |
| 10 | 粉砕 | 15 |

### TurtleBot

- Win Rate: 45.6%
- Draw Rate: 8.4%
- First Pass Win Rate: 29.4%
- Win With Fewer Cards: 5.8%
- Win With Same Cards: 43.2%
- Win With More Cards: 51.0%
- Action Rates: set=22.2%, set_pass=51.2%, pass=26.6%
- Turn Stats: min=1, avg=3.44, max=50
- Winning Attack Stats: min=1, avg=2.13, max=6
- Winning Block Stats: min=0, avg=3.54, max=13
- Winning Speed Stats: min=-3, avg=1.09, max=6

### Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | starter_attack | 239 |
| 2 | starter_defense | 228 |
| 3 | starter_balanced | 224 |
| 4 | starter_speed | 218 |
| 5 | starter_heavy | 217 |

### Most Used

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 854 |
| 2 | 受け流し | 618 |
| 3 | 構え | 613 |
| 4 | 蓄え | 573 |
| 5 | 押し込み | 495 |
| 6 | 鉄壁 | 495 |
| 7 | 補強 | 457 |
| 8 | 踏ん張り | 416 |
| 9 | 牽制 | 388 |
| 10 | 低姿勢 | 385 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 490 |
| 2 | 受け流し | 362 |
| 3 | 構え | 344 |
| 4 | 補強 | 250 |
| 5 | 鉄壁 | 249 |
| 6 | 踏ん張り | 228 |
| 7 | 蓄え | 224 |
| 8 | 低姿勢 | 218 |
| 9 | 牽制 | 182 |
| 10 | 押し込み | 160 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 307 |
| 2 | 踏ん張り | 112 |
| 3 | 低姿勢 | 97 |
| 4 | 押し込み | 96 |
| 5 | 受け流し | 81 |
| 6 | 鉄壁 | 27 |
| 7 | 十字受け | 25 |
| 8 | 退き足 | 17 |
| 9 | 渾身 | 12 |
| 10 | 踏み込み | 10 |
