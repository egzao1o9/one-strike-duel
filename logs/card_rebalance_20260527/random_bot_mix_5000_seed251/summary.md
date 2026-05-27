# Random Bot Mix Report

## Configuration

- Matches: 5000
- Seed: 251
- Selection Mode: p1/p2 bot and deck selected independently at random
- Bot Pool: `AttackBot`, `BurstBot`, `DefenseBot`, `DisruptBot`, `GreedyBot`, `RandomBot`, `RiskBot`, `TempoBot`, `TurtleBot`
- Deck Pool: `starter_attack`, `starter_balanced`, `starter_defense`, `starter_heavy`, `starter_speed`

## Bot Win Rates

| Bot | Matches | Wins | Losses | Draws | Win Rate | First Pass Win | Fewer Win | Same Win | More Win | Winner Set Avg | Loser Set Avg | Start Win | Second Win | Set Rate | Set+Pass Rate | Pass Rate | Turn Min | Turn Avg | Turn Max | Win A Avg | Win B Avg | Win S Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `AttackBot` | 1112 | 473 | 526 | 113 | 42.5% | 28.9% | 10.6% | 49.9% | 39.5% | 1.71 | 1.32 | 44.5% | 40.3% | 24.9% | 42.2% | 32.8% | 1 | 1.89 | 50 | 4.23 | 0.6 | 1.38 |
| `BurstBot` | 1076 | 504 | 461 | 111 | 46.8% | 36.5% | 9.3% | 55.6% | 35.1% | 1.54 | 1.3 | 50.0% | 43.1% | 21.2% | 64.2% | 14.6% | 1 | 1.62 | 50 | 3.24 | 0.41 | 1.83 |
| `DefenseBot` | 1037 | 632 | 335 | 70 | 60.9% | 37.3% | 5.2% | 47.3% | 47.5% | 1.56 | 1.03 | 62.6% | 59.3% | 28.1% | 51.8% | 20.1% | 1 | 3.12 | 50 | 1.97 | 2.5 | 0.93 |
| `DisruptBot` | 1121 | 547 | 462 | 112 | 48.8% | 39.5% | 9.9% | 57.2% | 32.9% | 1.42 | 1.1 | 55.3% | 43.0% | 8.1% | 69.1% | 22.8% | 1 | 2.55 | 50 | 2.38 | 0.36 | 1.92 |
| `GreedyBot` | 1101 | 430 | 564 | 107 | 39.1% | 20.2% | 6.0% | 44.0% | 50.0% | 1.84 | 1.24 | 42.8% | 35.5% | 27.9% | 43.2% | 29.0% | 1 | 2.21 | 50 | 2.82 | 1.39 | 1.21 |
| `RandomBot` | 1172 | 560 | 506 | 106 | 47.8% | 33.5% | 6.4% | 46.2% | 47.3% | 1.59 | 1.4 | 50.8% | 44.6% | 23.8% | 60.1% | 16.2% | 1 | 2.65 | 50 | 2.7 | 1.23 | 1.29 |
| `RiskBot` | 1085 | 493 | 479 | 113 | 45.4% | 33.1% | 7.1% | 47.3% | 45.6% | 1.48 | 1.4 | 48.0% | 42.6% | 16.8% | 58.4% | 24.8% | 1 | 3.15 | 50 | 2.6 | 2.15 | -0.03 |
| `TempoBot` | 1170 | 380 | 693 | 97 | 32.5% | 28.0% | 11.3% | 68.4% | 20.3% | 1.09 | 0.99 | 36.9% | 28.8% | 2.9% | 78.4% | 18.7% | 1 | 2.68 | 50 | 1.74 | 0.5 | 1.94 |
| `TurtleBot` | 1126 | 517 | 510 | 99 | 45.9% | 37.8% | 6.2% | 50.1% | 43.7% | 1.26 | 0.84 | 51.0% | 41.1% | 15.1% | 62.5% | 22.4% | 1 | 3.91 | 50 | 1.46 | 2.51 | 0.24 |

## Bot Pair Summary

| Pair | Matches | Draws | Wins | Turn Min | Turn Avg | Turn Max |
|---|---:|---:|---|---:|---:|---:|
| AttackBot vs AttackBot | 59 | 8 | `AttackBot`=51 | 1 | 1.2 | 9 |
| AttackBot vs BurstBot | 122 | 19 | `AttackBot`=49, `BurstBot`=54 | 1 | 1.21 | 6 |
| AttackBot vs DefenseBot | 118 | 11 | `AttackBot`=40, `DefenseBot`=67 | 1 | 2.75 | 50 |
| AttackBot vs DisruptBot | 127 | 12 | `AttackBot`=43, `DisruptBot`=72 | 1 | 1.97 | 50 |
| AttackBot vs GreedyBot | 136 | 16 | `AttackBot`=67, `GreedyBot`=53 | 1 | 1.85 | 50 |
| AttackBot vs RandomBot | 119 | 13 | `AttackBot`=42, `RandomBot`=64 | 1 | 2.18 | 50 |
| AttackBot vs RiskBot | 134 | 7 | `AttackBot`=67, `RiskBot`=60 | 1 | 1.82 | 50 |
| AttackBot vs TempoBot | 111 | 8 | `AttackBot`=62, `TempoBot`=41 | 1 | 1.77 | 50 |
| AttackBot vs TurtleBot | 127 | 11 | `AttackBot`=52, `TurtleBot`=64 | 1 | 2.28 | 10 |
| BurstBot vs BurstBot | 59 | 12 | `BurstBot`=47 | 1 | 1.93 | 50 |
| BurstBot vs DefenseBot | 123 | 5 | `BurstBot`=40, `DefenseBot`=78 | 1 | 1.81 | 9 |
| BurstBot vs DisruptBot | 119 | 9 | `BurstBot`=56, `DisruptBot`=54 | 1 | 1.24 | 6 |
| BurstBot vs GreedyBot | 123 | 9 | `BurstBot`=62, `GreedyBot`=52 | 1 | 1.5 | 50 |
| BurstBot vs RandomBot | 106 | 16 | `BurstBot`=47, `RandomBot`=43 | 1 | 1.26 | 7 |
| BurstBot vs RiskBot | 100 | 10 | `BurstBot`=50, `RiskBot`=40 | 1 | 2.07 | 50 |
| BurstBot vs TempoBot | 136 | 12 | `BurstBot`=82, `TempoBot`=42 | 1 | 1.46 | 6 |
| BurstBot vs TurtleBot | 129 | 7 | `BurstBot`=66, `TurtleBot`=56 | 1 | 2.11 | 9 |
| DefenseBot vs DefenseBot | 47 | 4 | `DefenseBot`=43 | 1 | 3.83 | 9 |
| DefenseBot vs DisruptBot | 96 | 6 | `DefenseBot`=63, `DisruptBot`=27 | 1 | 3.36 | 50 |
| DefenseBot vs GreedyBot | 128 | 5 | `DefenseBot`=86, `GreedyBot`=37 | 1 | 2.32 | 9 |
| DefenseBot vs RandomBot | 115 | 8 | `DefenseBot`=65, `RandomBot`=42 | 1 | 3.11 | 50 |
| DefenseBot vs RiskBot | 109 | 6 | `DefenseBot`=66, `RiskBot`=37 | 1 | 2.95 | 10 |
| DefenseBot vs TempoBot | 129 | 7 | `DefenseBot`=102, `TempoBot`=20 | 1 | 3.88 | 50 |
| DefenseBot vs TurtleBot | 125 | 14 | `DefenseBot`=62, `TurtleBot`=49 | 1 | 4.23 | 50 |
| DisruptBot vs DisruptBot | 64 | 9 | `DisruptBot`=55 | 1 | 4.03 | 50 |
| DisruptBot vs GreedyBot | 118 | 15 | `DisruptBot`=58, `GreedyBot`=45 | 1 | 2.02 | 50 |
| DisruptBot vs RandomBot | 129 | 10 | `DisruptBot`=59, `RandomBot`=60 | 1 | 2.75 | 50 |
| DisruptBot vs RiskBot | 125 | 18 | `DisruptBot`=61, `RiskBot`=46 | 1 | 2.97 | 50 |
| DisruptBot vs TempoBot | 165 | 16 | `DisruptBot`=105, `TempoBot`=44 | 1 | 1.79 | 10 |
| DisruptBot vs TurtleBot | 114 | 8 | `DisruptBot`=56, `TurtleBot`=50 | 1 | 3.21 | 50 |
| GreedyBot vs GreedyBot | 53 | 7 | `GreedyBot`=46 | 1 | 4.19 | 50 |
| GreedyBot vs RandomBot | 149 | 13 | `GreedyBot`=59, `RandomBot`=77 | 1 | 1.7 | 10 |
| GreedyBot vs RiskBot | 120 | 14 | `GreedyBot`=50, `RiskBot`=56 | 1 | 1.44 | 6 |
| GreedyBot vs TempoBot | 116 | 16 | `GreedyBot`=48, `TempoBot`=52 | 1 | 3.23 | 50 |
| GreedyBot vs TurtleBot | 105 | 5 | `GreedyBot`=40, `TurtleBot`=60 | 1 | 2.07 | 8 |
| RandomBot vs RandomBot | 62 | 5 | `RandomBot`=57 | 1 | 2.84 | 50 |
| RandomBot vs RiskBot | 136 | 12 | `RandomBot`=59, `RiskBot`=65 | 1 | 3.1 | 50 |
| RandomBot vs TempoBot | 139 | 10 | `RandomBot`=79, `TempoBot`=50 | 1 | 2.27 | 10 |
| RandomBot vs TurtleBot | 155 | 14 | `RandomBot`=79, `TurtleBot`=62 | 1 | 4.26 | 50 |
| RiskBot vs RiskBot | 59 | 14 | `RiskBot`=45 | 1 | 6.95 | 50 |
| RiskBot vs TempoBot | 132 | 8 | `RiskBot`=84, `TempoBot`=40 | 1 | 2.42 | 50 |
| RiskBot vs TurtleBot | 111 | 10 | `RiskBot`=60, `TurtleBot`=41 | 1 | 4.82 | 50 |
| TempoBot vs TempoBot | 55 | 4 | `TempoBot`=51 | 1 | 2.75 | 8 |
| TempoBot vs TurtleBot | 132 | 12 | `TempoBot`=40, `TurtleBot`=80 | 1 | 4.83 | 50 |
| TurtleBot vs TurtleBot | 64 | 9 | `TurtleBot`=55 | 1 | 7 | 50 |

## Deck Usage Summary

| Deck | Matches | Wins | Draws | Win Rate |
|---|---:|---:|---:|---:|
| `starter_attack` | 1962 | 876 | 191 | 44.6% |
| `starter_balanced` | 2074 | 1134 | 220 | 54.7% |
| `starter_defense` | 2041 | 923 | 210 | 45.2% |
| `starter_heavy` | 1893 | 714 | 133 | 37.7% |
| `starter_speed` | 2030 | 889 | 174 | 43.8% |

## Bot Pattern Metrics

| Bot | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `AttackBot` | 4.06 | 0.4 | 0.8 | 3.93 | 0.25 | 0.2 | 117 (10.5%) | 123 (26.0%) |
| `BurstBot` | 3.43 | 0.31 | 1.07 | 3.72 | 0.23 | 0.23 | 105 (9.8%) | 108 (21.4%) |
| `DefenseBot` | 1.72 | 1.94 | 0.9 | 1.22 | 1.07 | 0.91 | 114 (11.0%) | 248 (39.2%) |
| `DisruptBot` | 1.97 | 0.4 | 1.54 | 1.55 | 0.53 | 1.23 | 192 (17.1%) | 132 (24.1%) |
| `GreedyBot` | 2.67 | 0.77 | 0.73 | 2.6 | 0.4 | 0.38 | 133 (12.1%) | 159 (37.0%) |
| `RandomBot` | 2.36 | 0.9 | 1.3 | 1.96 | 0.67 | 1.37 | 219 (18.7%) | 176 (31.4%) |
| `RiskBot` | 2.45 | 1.38 | 0.1 | 2.44 | 0.79 | 0.17 | 126 (11.6%) | 263 (53.3%) |
| `TempoBot` | 1.11 | 0.53 | 1.92 | 0.68 | 0.6 | 2.02 | 400 (34.2%) | 66 (17.4%) |
| `TurtleBot` | 1.15 | 1.66 | 0.37 | 0.79 | 0.99 | 0.5 | 144 (12.8%) | 275 (53.2%) |

## Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 4068 |
| 2 | 受け流し | 3406 |
| 3 | 押し込み | 2991 |
| 4 | 構え | 2333 |
| 5 | 鉄壁 | 1990 |
| 6 | 踏ん張り | 1901 |
| 7 | 低姿勢 | 1733 |
| 8 | 牽制 | 1689 |
| 9 | 退き足 | 1642 |
| 10 | 十字受け | 1611 |
| 11 | 加速 | 1586 |
| 12 | 圧迫 | 1503 |
| 13 | 蓄え | 1358 |
| 14 | 貫き | 1300 |
| 15 | 補強 | 1294 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 1998 |
| 2 | 受け流し | 1663 |
| 3 | 押し込み | 1511 |
| 4 | 構え | 1327 |
| 5 | 踏ん張り | 1045 |
| 6 | 鉄壁 | 1029 |
| 7 | 低姿勢 | 953 |
| 8 | 牽制 | 901 |
| 9 | 補強 | 735 |
| 10 | 踏み込み | 728 |
| 11 | 圧迫 | 727 |
| 12 | 加速 | 717 |
| 13 | 十字受け | 703 |
| 14 | 貫き | 699 |
| 15 | 崩し | 694 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 1091 |
| 2 | 返し刃 | 1077 |
| 3 | 貫き | 631 |
| 4 | 崩し | 617 |
| 5 | 踏み込み | 613 |
| 6 | 踏ん張り | 494 |
| 7 | 疾走 | 481 |
| 8 | 低姿勢 | 458 |
| 9 | 渾身 | 322 |
| 10 | 受け流し | 269 |
| 11 | 大振り | 221 |
| 12 | 粉砕 | 218 |
| 13 | 十字受け | 135 |
| 14 | 退き足 | 91 |
| 15 | 鉄壁 | 66 |

## Bot Details

### AttackBot

- Win Rate: 42.5%
- Draw Rate: 10.2%
- First Pass Win Rate: 28.9%
- Win With Fewer Cards: 10.6%
- Win With Same Cards: 49.9%
- Win With More Cards: 39.5%
- Winner Facedown Avg: 1.71
- Loser Facedown Avg: 1.32
- Starting Player Win Rate: 44.5%
- Responding Player Win Rate: 40.3%
- Final Stats Avg: A=4.06, B=0.4, S=0.8
- Losing Final Stats Avg: A=3.93, B=0.25, S=0.2
- Lost With Speed Advantage: 117 (10.5%)
- Won After Blocking Faster Attack: 123 (26.0%)
- Action Rates: set=24.9%, set_pass=42.2%, pass=32.8%
- Turn Stats: min=1, avg=1.89, max=50
- Winning Attack Stats: min=1, avg=4.23, max=18
- Winning Block Stats: min=0, avg=0.6, max=6
- Winning Speed Stats: min=-6, avg=1.38, max=6

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
| 1 | 押し込み | 493 |
| 2 | 前のめり | 387 |
| 3 | 集中 | 366 |
| 4 | 貫き | 258 |
| 5 | 崩し | 253 |
| 6 | 渾身 | 236 |
| 7 | 圧迫 | 225 |
| 8 | 加速 | 212 |
| 9 | 踏み込み | 202 |
| 10 | 大振り | 154 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 277 |
| 2 | 前のめり | 197 |
| 3 | 崩し | 145 |
| 4 | 貫き | 138 |
| 5 | 圧迫 | 117 |
| 6 | 集中 | 114 |
| 7 | 踏み込み | 112 |
| 8 | 加速 | 72 |
| 9 | 渾身 | 65 |
| 10 | 粉砕 | 58 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 231 |
| 2 | 崩し | 135 |
| 3 | 貫き | 126 |
| 4 | 踏み込み | 101 |
| 5 | 渾身 | 62 |
| 6 | 粉砕 | 53 |
| 7 | 大振り | 35 |
| 8 | 返し刃 | 32 |
| 9 | 低姿勢 | 11 |
| 10 | 踏ん張り | 10 |

### BurstBot

- Win Rate: 46.8%
- Draw Rate: 10.3%
- First Pass Win Rate: 36.5%
- Win With Fewer Cards: 9.3%
- Win With Same Cards: 55.6%
- Win With More Cards: 35.1%
- Winner Facedown Avg: 1.54
- Loser Facedown Avg: 1.3
- Starting Player Win Rate: 50.0%
- Responding Player Win Rate: 43.1%
- Final Stats Avg: A=3.43, B=0.31, S=1.07
- Losing Final Stats Avg: A=3.72, B=0.23, S=0.23
- Lost With Speed Advantage: 105 (9.8%)
- Won After Blocking Faster Attack: 108 (21.4%)
- Action Rates: set=21.2%, set_pass=64.2%, pass=14.6%
- Turn Stats: min=1, avg=1.62, max=50
- Winning Attack Stats: min=1, avg=3.24, max=17
- Winning Block Stats: min=0, avg=0.41, max=5
- Winning Speed Stats: min=-5, avg=1.83, max=7

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
| 1 | 返し刃 | 493 |
| 2 | 集中 | 320 |
| 3 | 前のめり | 308 |
| 4 | 渾身 | 258 |
| 5 | 圧迫 | 231 |
| 6 | 加速 | 225 |
| 7 | 疾走 | 219 |
| 8 | 貫き | 200 |
| 9 | 崩し | 199 |
| 10 | 粉砕 | 139 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 210 |
| 2 | 前のめり | 171 |
| 3 | 疾走 | 137 |
| 4 | 崩し | 127 |
| 5 | 貫き | 122 |
| 6 | 集中 | 121 |
| 7 | 圧迫 | 119 |
| 8 | 加速 | 107 |
| 9 | 踏み込み | 79 |
| 10 | 渾身 | 65 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 149 |
| 2 | 崩し | 119 |
| 3 | 貫き | 117 |
| 4 | 疾走 | 110 |
| 5 | 踏み込み | 71 |
| 6 | 渾身 | 57 |
| 7 | 粉砕 | 44 |
| 8 | 押し込み | 41 |
| 9 | 大振り | 28 |
| 10 | 踏ん張り | 26 |

### DefenseBot

- Win Rate: 60.9%
- Draw Rate: 6.8%
- First Pass Win Rate: 37.3%
- Win With Fewer Cards: 5.2%
- Win With Same Cards: 47.3%
- Win With More Cards: 47.5%
- Winner Facedown Avg: 1.56
- Loser Facedown Avg: 1.03
- Starting Player Win Rate: 62.6%
- Responding Player Win Rate: 59.3%
- Final Stats Avg: A=1.72, B=1.94, S=0.9
- Losing Final Stats Avg: A=1.22, B=1.07, S=0.91
- Lost With Speed Advantage: 114 (11.0%)
- Won After Blocking Faster Attack: 248 (39.2%)
- Action Rates: set=28.1%, set_pass=51.8%, pass=20.1%
- Turn Stats: min=1, avg=3.12, max=50
- Winning Attack Stats: min=1, avg=1.97, max=7
- Winning Block Stats: min=0, avg=2.5, max=11
- Winning Speed Stats: min=-4, avg=0.93, max=6

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
| 1 | 返し刃 | 718 |
| 2 | 押し込み | 670 |
| 3 | 構え | 582 |
| 4 | 受け流し | 553 |
| 5 | 蓄え | 455 |
| 6 | 鉄壁 | 453 |
| 7 | 牽制 | 446 |
| 8 | 踏ん張り | 353 |
| 9 | 低姿勢 | 347 |
| 10 | 補強 | 346 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 468 |
| 2 | 押し込み | 391 |
| 3 | 構え | 372 |
| 4 | 受け流し | 339 |
| 5 | 牽制 | 285 |
| 6 | 鉄壁 | 270 |
| 7 | 踏ん張り | 230 |
| 8 | 低姿勢 | 228 |
| 9 | 蓄え | 225 |
| 10 | 補強 | 214 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 277 |
| 2 | 返し刃 | 234 |
| 3 | 低姿勢 | 106 |
| 4 | 踏ん張り | 97 |
| 5 | 受け流し | 76 |
| 6 | 十字受け | 53 |
| 7 | 踏み込み | 49 |
| 8 | 粉砕 | 32 |
| 9 | 退き足 | 31 |
| 10 | 鉄壁 | 16 |

### DisruptBot

- Win Rate: 48.8%
- Draw Rate: 10.0%
- First Pass Win Rate: 39.5%
- Win With Fewer Cards: 9.9%
- Win With Same Cards: 57.2%
- Win With More Cards: 32.9%
- Winner Facedown Avg: 1.42
- Loser Facedown Avg: 1.1
- Starting Player Win Rate: 55.3%
- Responding Player Win Rate: 43.0%
- Final Stats Avg: A=1.97, B=0.4, S=1.54
- Losing Final Stats Avg: A=1.55, B=0.53, S=1.23
- Lost With Speed Advantage: 192 (17.1%)
- Won After Blocking Faster Attack: 132 (24.1%)
- Action Rates: set=8.1%, set_pass=69.1%, pass=22.8%
- Turn Stats: min=1, avg=2.55, max=50
- Winning Attack Stats: min=1, avg=2.38, max=9
- Winning Block Stats: min=0, avg=0.36, max=3
- Winning Speed Stats: min=-3, avg=1.92, max=8

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
| 1 | 返し刃 | 378 |
| 2 | 圧迫 | 313 |
| 3 | 受け流し | 297 |
| 4 | 疾走 | 286 |
| 5 | 加速 | 286 |
| 6 | 牽制 | 266 |
| 7 | 崩し | 246 |
| 8 | 踏み込み | 239 |
| 9 | 貫き | 235 |
| 10 | 退き足 | 195 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 疾走 | 178 |
| 2 | 圧迫 | 170 |
| 3 | 返し刃 | 166 |
| 4 | 踏み込み | 161 |
| 5 | 加速 | 160 |
| 6 | 崩し | 155 |
| 7 | 貫き | 150 |
| 8 | 牽制 | 115 |
| 9 | 受け流し | 94 |
| 10 | 重心落とし | 89 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 140 |
| 2 | 疾走 | 139 |
| 3 | 貫き | 136 |
| 4 | 崩し | 130 |
| 5 | 返し刃 | 96 |
| 6 | 押し込み | 37 |
| 7 | 踏ん張り | 30 |
| 8 | 粉砕 | 22 |
| 9 | 渾身 | 20 |
| 10 | 退き足 | 10 |

### GreedyBot

- Win Rate: 39.1%
- Draw Rate: 9.7%
- First Pass Win Rate: 20.2%
- Win With Fewer Cards: 6.0%
- Win With Same Cards: 44.0%
- Win With More Cards: 50.0%
- Winner Facedown Avg: 1.84
- Loser Facedown Avg: 1.24
- Starting Player Win Rate: 42.8%
- Responding Player Win Rate: 35.5%
- Final Stats Avg: A=2.67, B=0.77, S=0.73
- Losing Final Stats Avg: A=2.6, B=0.4, S=0.38
- Lost With Speed Advantage: 133 (12.1%)
- Won After Blocking Faster Attack: 159 (37.0%)
- Action Rates: set=27.9%, set_pass=43.2%, pass=29.0%
- Turn Stats: min=1, avg=2.21, max=50
- Winning Attack Stats: min=1, avg=2.82, max=11
- Winning Block Stats: min=0, avg=1.39, max=9
- Winning Speed Stats: min=-4, avg=1.21, max=11

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
| 1 | 返し刃 | 359 |
| 2 | 押し込み | 292 |
| 3 | 受け流し | 287 |
| 4 | 圧迫 | 269 |
| 5 | 貫き | 192 |
| 6 | 渾身 | 185 |
| 7 | 崩し | 170 |
| 8 | 踏ん張り | 166 |
| 9 | 十字受け | 158 |
| 10 | 低姿勢 | 148 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 146 |
| 2 | 返し刃 | 142 |
| 3 | 圧迫 | 113 |
| 4 | 貫き | 97 |
| 5 | 崩し | 95 |
| 6 | 受け流し | 91 |
| 7 | 踏ん張り | 78 |
| 8 | 踏み込み | 77 |
| 9 | 低姿勢 | 69 |
| 10 | 十字受け | 55 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 129 |
| 2 | 返し刃 | 98 |
| 3 | 貫き | 91 |
| 4 | 崩し | 87 |
| 5 | 踏み込み | 66 |
| 6 | 踏ん張り | 50 |
| 7 | 低姿勢 | 48 |
| 8 | 疾走 | 41 |
| 9 | 受け流し | 39 |
| 10 | 渾身 | 31 |

### RandomBot

- Win Rate: 47.8%
- Draw Rate: 9.0%
- First Pass Win Rate: 33.5%
- Win With Fewer Cards: 6.4%
- Win With Same Cards: 46.2%
- Win With More Cards: 47.3%
- Winner Facedown Avg: 1.59
- Loser Facedown Avg: 1.4
- Starting Player Win Rate: 50.8%
- Responding Player Win Rate: 44.6%
- Final Stats Avg: A=2.36, B=0.9, S=1.3
- Losing Final Stats Avg: A=1.96, B=0.67, S=1.37
- Lost With Speed Advantage: 219 (18.7%)
- Won After Blocking Faster Attack: 176 (31.4%)
- Action Rates: set=23.8%, set_pass=60.1%, pass=16.2%
- Turn Stats: min=1, avg=2.65, max=50
- Winning Attack Stats: min=1, avg=2.7, max=12
- Winning Block Stats: min=0, avg=1.23, max=11
- Winning Speed Stats: min=-5, avg=1.29, max=10

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
| 1 | 返し刃 | 535 |
| 2 | 受け流し | 459 |
| 3 | 構え | 358 |
| 4 | 鉄壁 | 331 |
| 5 | 押し込み | 314 |
| 6 | 退き足 | 241 |
| 7 | 加速 | 232 |
| 8 | 集中 | 217 |
| 9 | 十字受け | 210 |
| 10 | 蓄え | 208 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 309 |
| 2 | 受け流し | 272 |
| 3 | 構え | 202 |
| 4 | 鉄壁 | 182 |
| 5 | 押し込み | 166 |
| 6 | 低姿勢 | 134 |
| 7 | 踏ん張り | 127 |
| 8 | 退き足 | 124 |
| 9 | 加速 | 120 |
| 10 | 十字受け | 116 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 138 |
| 2 | 押し込み | 108 |
| 3 | 貫き | 88 |
| 4 | 崩し | 86 |
| 5 | 踏み込み | 68 |
| 6 | 疾走 | 65 |
| 7 | 低姿勢 | 57 |
| 8 | 渾身 | 53 |
| 9 | 踏ん張り | 49 |
| 10 | 大振り | 41 |

### RiskBot

- Win Rate: 45.4%
- Draw Rate: 10.4%
- First Pass Win Rate: 33.1%
- Win With Fewer Cards: 7.1%
- Win With Same Cards: 47.3%
- Win With More Cards: 45.6%
- Winner Facedown Avg: 1.48
- Loser Facedown Avg: 1.4
- Starting Player Win Rate: 48.0%
- Responding Player Win Rate: 42.6%
- Final Stats Avg: A=2.45, B=1.38, S=0.1
- Losing Final Stats Avg: A=2.44, B=0.79, S=0.17
- Lost With Speed Advantage: 126 (11.6%)
- Won After Blocking Faster Attack: 263 (53.3%)
- Action Rates: set=16.8%, set_pass=58.4%, pass=24.8%
- Turn Stats: min=1, avg=3.15, max=50
- Winning Attack Stats: min=1, avg=2.6, max=14
- Winning Block Stats: min=0, avg=2.15, max=11
- Winning Speed Stats: min=-6, avg=-0.03, max=4

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
| 1 | 構え | 522 |
| 2 | 受け流し | 490 |
| 3 | 押し込み | 450 |
| 4 | 返し刃 | 406 |
| 5 | 鉄壁 | 366 |
| 6 | 牽制 | 284 |
| 7 | 低姿勢 | 279 |
| 8 | 踏ん張り | 277 |
| 9 | 補強 | 263 |
| 10 | 渾身 | 252 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 構え | 302 |
| 2 | 受け流し | 281 |
| 3 | 返し刃 | 216 |
| 4 | 押し込み | 210 |
| 5 | 鉄壁 | 185 |
| 6 | 低姿勢 | 162 |
| 7 | 踏ん張り | 155 |
| 8 | 補強 | 147 |
| 9 | 牽制 | 140 |
| 10 | 受け直し | 91 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 146 |
| 2 | 返し刃 | 113 |
| 3 | 低姿勢 | 77 |
| 4 | 踏ん張り | 73 |
| 5 | 渾身 | 70 |
| 6 | 大振り | 68 |
| 7 | 受け流し | 56 |
| 8 | 貫き | 35 |
| 9 | 崩し | 31 |
| 10 | 鉄壁 | 29 |

### TempoBot

- Win Rate: 32.5%
- Draw Rate: 8.3%
- First Pass Win Rate: 28.0%
- Win With Fewer Cards: 11.3%
- Win With Same Cards: 68.4%
- Win With More Cards: 20.3%
- Winner Facedown Avg: 1.09
- Loser Facedown Avg: 0.99
- Starting Player Win Rate: 36.9%
- Responding Player Win Rate: 28.8%
- Final Stats Avg: A=1.11, B=0.53, S=1.92
- Losing Final Stats Avg: A=0.68, B=0.6, S=2.02
- Lost With Speed Advantage: 400 (34.2%)
- Won After Blocking Faster Attack: 66 (17.4%)
- Action Rates: set=2.9%, set_pass=78.4%, pass=18.7%
- Turn Stats: min=1, avg=2.68, max=50
- Winning Attack Stats: min=1, avg=1.74, max=7
- Winning Block Stats: min=0, avg=0.5, max=3
- Winning Speed Stats: min=-2, avg=1.94, max=8

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
| 1 | 受け流し | 495 |
| 2 | 加速 | 456 |
| 3 | 返し刃 | 410 |
| 4 | 疾走 | 323 |
| 5 | 退き足 | 241 |
| 6 | 踏み込み | 231 |
| 7 | 圧迫 | 209 |
| 8 | 十字受け | 190 |
| 9 | 勢い溜め | 162 |
| 10 | 踏ん張り | 154 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 加速 | 166 |
| 2 | 疾走 | 130 |
| 3 | 受け流し | 127 |
| 4 | 返し刃 | 125 |
| 5 | 踏み込み | 123 |
| 6 | 圧迫 | 79 |
| 7 | 受け直し | 62 |
| 8 | 勢い溜め | 56 |
| 9 | 退き足 | 55 |
| 10 | 重心落とし | 53 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 109 |
| 2 | 疾走 | 103 |
| 3 | 返し刃 | 59 |
| 4 | 貫き | 27 |
| 5 | 踏ん張り | 25 |
| 6 | 崩し | 22 |
| 7 | 低姿勢 | 21 |
| 8 | 渾身 | 16 |
| 9 | 粉砕 | 15 |
| 10 | 押し込み | 12 |

### TurtleBot

- Win Rate: 45.9%
- Draw Rate: 8.8%
- First Pass Win Rate: 37.8%
- Win With Fewer Cards: 6.2%
- Win With Same Cards: 50.1%
- Win With More Cards: 43.7%
- Winner Facedown Avg: 1.26
- Loser Facedown Avg: 0.84
- Starting Player Win Rate: 51.0%
- Responding Player Win Rate: 41.1%
- Final Stats Avg: A=1.15, B=1.66, S=0.37
- Losing Final Stats Avg: A=0.79, B=0.99, S=0.5
- Lost With Speed Advantage: 144 (12.8%)
- Won After Blocking Faster Attack: 275 (53.2%)
- Action Rates: set=15.1%, set_pass=62.5%, pass=22.4%
- Turn Stats: min=1, avg=3.91, max=50
- Winning Attack Stats: min=1, avg=1.46, max=5
- Winning Block Stats: min=0, avg=2.51, max=11
- Winning Speed Stats: min=-3, avg=0.24, max=4

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
| 1 | 受け流し | 734 |
| 2 | 構え | 724 |
| 3 | 返し刃 | 635 |
| 4 | 蓄え | 624 |
| 5 | 鉄壁 | 593 |
| 6 | 押し込み | 501 |
| 7 | 補強 | 494 |
| 8 | 踏ん張り | 473 |
| 9 | 低姿勢 | 445 |
| 10 | 牽制 | 445 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 受け流し | 439 |
| 2 | 構え | 424 |
| 3 | 鉄壁 | 341 |
| 4 | 返し刃 | 321 |
| 5 | 踏ん張り | 295 |
| 6 | 補強 | 284 |
| 7 | 低姿勢 | 278 |
| 8 | 蓄え | 260 |
| 9 | 牽制 | 239 |
| 10 | 押し込み | 172 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 158 |
| 2 | 踏ん張り | 134 |
| 3 | 低姿勢 | 119 |
| 4 | 押し込み | 110 |
| 5 | 受け流し | 55 |
| 6 | 十字受け | 15 |
| 7 | 大振り | 12 |
| 8 | 渾身 | 9 |
| 9 | 退き足 | 8 |
| 10 | 鉄壁 | 7 |
