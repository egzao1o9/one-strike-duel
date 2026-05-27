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
| `AttackBot` | 1112 | 483 | 505 | 124 | 43.4% | 37.1% | 14.1% | 56.3% | 29.6% | 1.54 | 1.1 | 46.4% | 40.4% | 17.3% | 43.3% | 39.5% | 1 | 2.04 | 50 | 4.67 | 0.18 | 1.79 |
| `BurstBot` | 1076 | 578 | 371 | 127 | 53.7% | 49.5% | 12.5% | 58.5% | 29.1% | 1.44 | 1.28 | 56.3% | 50.5% | 23.1% | 65.8% | 11.2% | 1 | 1.4 | 50 | 3.72 | 0.32 | 1.86 |
| `DefenseBot` | 1037 | 496 | 470 | 71 | 47.8% | 37.9% | 5.0% | 48.2% | 46.8% | 1.41 | 1.25 | 52.3% | 43.4% | 25.8% | 51.9% | 22.3% | 1 | 3.24 | 50 | 1.92 | 1.63 | 0.77 |
| `DisruptBot` | 1121 | 599 | 391 | 131 | 53.4% | 44.1% | 9.3% | 59.3% | 31.4% | 1.45 | 1.08 | 59.5% | 48.3% | 8.9% | 65.4% | 25.6% | 1 | 2.33 | 50 | 3.12 | 0.24 | 2.03 |
| `GreedyBot` | 1101 | 454 | 523 | 124 | 41.2% | 31.0% | 9.3% | 52.4% | 38.3% | 1.56 | 1.21 | 44.4% | 38.3% | 23.8% | 45.1% | 31.1% | 1 | 2.25 | 50 | 2.93 | 0.72 | 1.15 |
| `RandomBot` | 1172 | 546 | 503 | 123 | 46.6% | 35.7% | 7.3% | 46.3% | 46.3% | 1.57 | 1.41 | 50.3% | 42.7% | 21.4% | 56.2% | 22.4% | 1 | 2.8 | 50 | 3.06 | 0.72 | 1.48 |
| `RiskBot` | 1085 | 466 | 483 | 136 | 42.9% | 38.9% | 9.2% | 57.1% | 33.7% | 1.36 | 1.33 | 46.2% | 39.2% | 9.9% | 61.3% | 28.8% | 1 | 3.14 | 50 | 3.41 | 1.14 | 0.28 |
| `TempoBot` | 1170 | 455 | 610 | 105 | 38.9% | 34.8% | 12.3% | 70.5% | 17.1% | 1.11 | 0.96 | 41.9% | 36.3% | 2.9% | 73.3% | 23.7% | 1 | 2.53 | 50 | 2.67 | 0.27 | 2.17 |
| `TurtleBot` | 1126 | 396 | 617 | 113 | 35.2% | 31.2% | 5.3% | 57.3% | 37.4% | 1.05 | 0.88 | 38.1% | 32.4% | 5.0% | 61.2% | 33.8% | 1 | 4.76 | 50 | 1.64 | 1.36 | 0.14 |

## Bot Pair Summary

| Pair | Matches | Draws | Wins | Turn Min | Turn Avg | Turn Max |
|---|---:|---:|---|---:|---:|---:|
| AttackBot vs AttackBot | 59 | 10 | `AttackBot`=49 | 1 | 2.68 | 50 |
| AttackBot vs BurstBot | 122 | 12 | `AttackBot`=46, `BurstBot`=64 | 1 | 1.16 | 6 |
| AttackBot vs DefenseBot | 118 | 11 | `AttackBot`=58, `DefenseBot`=49 | 1 | 2.66 | 50 |
| AttackBot vs DisruptBot | 127 | 16 | `AttackBot`=40, `DisruptBot`=71 | 1 | 1.93 | 50 |
| AttackBot vs GreedyBot | 136 | 15 | `AttackBot`=66, `GreedyBot`=55 | 1 | 1.51 | 50 |
| AttackBot vs RandomBot | 119 | 17 | `AttackBot`=43, `RandomBot`=59 | 1 | 2.44 | 50 |
| AttackBot vs RiskBot | 134 | 13 | `AttackBot`=59, `RiskBot`=62 | 1 | 1.6 | 50 |
| AttackBot vs TempoBot | 111 | 10 | `AttackBot`=50, `TempoBot`=51 | 1 | 1.68 | 50 |
| AttackBot vs TurtleBot | 127 | 10 | `AttackBot`=72, `TurtleBot`=45 | 1 | 2.84 | 50 |
| BurstBot vs BurstBot | 59 | 11 | `BurstBot`=48 | 1 | 1.1 | 3 |
| BurstBot vs DefenseBot | 123 | 6 | `BurstBot`=73, `DefenseBot`=44 | 1 | 1.85 | 8 |
| BurstBot vs DisruptBot | 119 | 15 | `BurstBot`=48, `DisruptBot`=56 | 1 | 1.15 | 4 |
| BurstBot vs GreedyBot | 123 | 15 | `BurstBot`=65, `GreedyBot`=43 | 1 | 1.11 | 4 |
| BurstBot vs RandomBot | 106 | 19 | `BurstBot`=55, `RandomBot`=32 | 1 | 1.28 | 6 |
| BurstBot vs RiskBot | 100 | 15 | `BurstBot`=53, `RiskBot`=32 | 1 | 1.44 | 10 |
| BurstBot vs TempoBot | 136 | 17 | `BurstBot`=80, `TempoBot`=39 | 1 | 1.6 | 50 |
| BurstBot vs TurtleBot | 129 | 6 | `BurstBot`=92, `TurtleBot`=31 | 1 | 1.87 | 8 |
| DefenseBot vs DefenseBot | 47 | 6 | `DefenseBot`=41 | 1 | 3.72 | 8 |
| DefenseBot vs DisruptBot | 96 | 8 | `DefenseBot`=39, `DisruptBot`=49 | 1 | 3.25 | 50 |
| DefenseBot vs GreedyBot | 128 | 5 | `DefenseBot`=74, `GreedyBot`=49 | 1 | 2.7 | 50 |
| DefenseBot vs RandomBot | 115 | 10 | `DefenseBot`=53, `RandomBot`=52 | 1 | 3.17 | 50 |
| DefenseBot vs RiskBot | 109 | 7 | `DefenseBot`=54, `RiskBot`=48 | 1 | 3.53 | 50 |
| DefenseBot vs TempoBot | 129 | 3 | `DefenseBot`=79, `TempoBot`=47 | 1 | 3.03 | 50 |
| DefenseBot vs TurtleBot | 125 | 9 | `DefenseBot`=63, `TurtleBot`=53 | 1 | 5.36 | 50 |
| DisruptBot vs DisruptBot | 64 | 9 | `DisruptBot`=55 | 1 | 3.56 | 50 |
| DisruptBot vs GreedyBot | 118 | 15 | `DisruptBot`=62, `GreedyBot`=41 | 1 | 2.19 | 50 |
| DisruptBot vs RandomBot | 129 | 12 | `DisruptBot`=66, `RandomBot`=51 | 1 | 1.76 | 13 |
| DisruptBot vs RiskBot | 125 | 16 | `DisruptBot`=67, `RiskBot`=42 | 1 | 2.44 | 50 |
| DisruptBot vs TempoBot | 165 | 17 | `DisruptBot`=104, `TempoBot`=44 | 1 | 1.45 | 9 |
| DisruptBot vs TurtleBot | 114 | 14 | `DisruptBot`=69, `TurtleBot`=31 | 1 | 3.75 | 50 |
| GreedyBot vs GreedyBot | 53 | 8 | `GreedyBot`=45 | 1 | 4.06 | 50 |
| GreedyBot vs RandomBot | 149 | 17 | `GreedyBot`=64, `RandomBot`=68 | 1 | 2.02 | 50 |
| GreedyBot vs RiskBot | 120 | 12 | `GreedyBot`=57, `RiskBot`=51 | 1 | 1.38 | 9 |
| GreedyBot vs TempoBot | 116 | 17 | `GreedyBot`=46, `TempoBot`=53 | 1 | 3.09 | 50 |
| GreedyBot vs TurtleBot | 105 | 12 | `GreedyBot`=54, `TurtleBot`=39 | 1 | 2.66 | 50 |
| RandomBot vs RandomBot | 62 | 3 | `RandomBot`=59 | 1 | 2.65 | 50 |
| RandomBot vs RiskBot | 136 | 14 | `RandomBot`=62, `RiskBot`=60 | 1 | 3.25 | 50 |
| RandomBot vs TempoBot | 139 | 12 | `RandomBot`=69, `TempoBot`=58 | 1 | 1.95 | 10 |
| RandomBot vs TurtleBot | 155 | 16 | `RandomBot`=94, `TurtleBot`=45 | 1 | 5.97 | 50 |
| RiskBot vs RiskBot | 59 | 16 | `RiskBot`=43 | 1 | 6.68 | 50 |
| RiskBot vs TempoBot | 132 | 13 | `RiskBot`=66, `TempoBot`=53 | 1 | 3.08 | 50 |
| RiskBot vs TurtleBot | 111 | 14 | `RiskBot`=62, `TurtleBot`=35 | 1 | 4.99 | 50 |
| TempoBot vs TempoBot | 55 | 2 | `TempoBot`=53 | 1 | 2.02 | 9 |
| TempoBot vs TurtleBot | 132 | 12 | `TempoBot`=57, `TurtleBot`=63 | 1 | 5.08 | 50 |
| TurtleBot vs TurtleBot | 64 | 10 | `TurtleBot`=54 | 3 | 9.59 | 50 |

## Deck Usage Summary

| Deck | Matches | Wins | Draws | Win Rate |
|---|---:|---:|---:|---:|
| `starter_attack` | 1962 | 1035 | 218 | 52.8% |
| `starter_balanced` | 2074 | 1122 | 239 | 54.1% |
| `starter_defense` | 2041 | 714 | 258 | 35.0% |
| `starter_heavy` | 1893 | 700 | 158 | 37.0% |
| `starter_speed` | 2030 | 902 | 181 | 44.4% |

## Bot Pattern Metrics

| Bot | Final A Avg | Final B Avg | Final S Avg | Loss A Avg | Loss B Avg | Loss S Avg | Speed Adv Losses | Block Counter Wins |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `AttackBot` | 4.18 | 0.17 | 0.99 | 3.75 | 0.18 | 0.2 | 103 (9.3%) | 96 (19.9%) |
| `BurstBot` | 3.98 | 0.26 | 1.13 | 4.37 | 0.18 | -0.02 | 46 (4.3%) | 113 (19.6%) |
| `DefenseBot` | 1.4 | 1.45 | 0.76 | 0.83 | 1.33 | 0.79 | 154 (14.9%) | 176 (35.5%) |
| `DisruptBot` | 2.47 | 0.28 | 1.53 | 1.65 | 0.39 | 0.94 | 109 (9.7%) | 124 (20.7%) |
| `GreedyBot` | 2.71 | 0.53 | 0.76 | 2.5 | 0.44 | 0.42 | 105 (9.5%) | 148 (32.6%) |
| `RandomBot` | 2.43 | 0.67 | 1.34 | 1.78 | 0.7 | 1.28 | 197 (16.8%) | 150 (27.5%) |
| `RiskBot` | 2.64 | 0.93 | 0.42 | 2.06 | 0.92 | 0.46 | 117 (10.8%) | 215 (46.1%) |
| `TempoBot` | 1.51 | 0.3 | 1.99 | 0.55 | 0.35 | 2.02 | 309 (26.4%) | 71 (15.6%) |
| `TurtleBot` | 0.88 | 1.09 | 0.28 | 0.38 | 1.02 | 0.36 | 148 (13.1%) | 195 (49.2%) |

## Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 4074 |
| 2 | 受け流し | 2537 |
| 3 | 押し込み | 2141 |
| 4 | 構え | 2110 |
| 5 | 鉄壁 | 1859 |
| 6 | 踏ん張り | 1718 |
| 7 | 牽制 | 1639 |
| 8 | 十字受け | 1634 |
| 9 | 加速 | 1514 |
| 10 | 圧迫 | 1472 |
| 11 | 踏み込み | 1379 |
| 12 | 退き足 | 1370 |
| 13 | 渾身 | 1344 |
| 14 | 蓄え | 1338 |
| 15 | 低姿勢 | 1241 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 1862 |
| 2 | 押し込み | 1055 |
| 3 | 踏み込み | 1037 |
| 4 | 構え | 907 |
| 5 | 受け流し | 894 |
| 6 | 牽制 | 814 |
| 7 | 踏ん張り | 801 |
| 8 | 圧迫 | 790 |
| 9 | 崩し | 775 |
| 10 | 鉄壁 | 770 |
| 11 | 貫き | 769 |
| 12 | 加速 | 742 |
| 13 | 疾走 | 692 |
| 14 | 十字受け | 590 |
| 15 | 補強 | 562 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 1013 |
| 2 | 踏み込み | 979 |
| 3 | 崩し | 715 |
| 4 | 貫き | 699 |
| 5 | 疾走 | 535 |
| 6 | 押し込み | 526 |
| 7 | 渾身 | 442 |
| 8 | 踏ん張り | 367 |
| 9 | 粉砕 | 310 |
| 10 | 大振り | 231 |
| 11 | 受け流し | 137 |
| 12 | 十字受け | 97 |
| 13 | 低姿勢 | 73 |
| 14 | 鉄壁 | 55 |
| 15 | 退き足 | 34 |

## Bot Details

### AttackBot

- Win Rate: 43.4%
- Draw Rate: 11.2%
- First Pass Win Rate: 37.1%
- Win With Fewer Cards: 14.1%
- Win With Same Cards: 56.3%
- Win With More Cards: 29.6%
- Winner Facedown Avg: 1.54
- Loser Facedown Avg: 1.1
- Starting Player Win Rate: 46.4%
- Responding Player Win Rate: 40.4%
- Final Stats Avg: A=4.18, B=0.17, S=0.99
- Losing Final Stats Avg: A=3.75, B=0.18, S=0.2
- Lost With Speed Advantage: 103 (9.3%)
- Won After Blocking Faster Attack: 96 (19.9%)
- Action Rates: set=17.3%, set_pass=43.3%, pass=39.5%
- Turn Stats: min=1, avg=2.04, max=50
- Winning Attack Stats: min=1, avg=4.67, max=19
- Winning Block Stats: min=0, avg=0.18, max=5
- Winning Speed Stats: min=-6, avg=1.79, max=7

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
| 1 | 前のめり | 396 |
| 2 | 集中 | 346 |
| 3 | 貫き | 286 |
| 4 | 崩し | 282 |
| 5 | 渾身 | 240 |
| 6 | 踏み込み | 222 |
| 7 | 圧迫 | 207 |
| 8 | 加速 | 181 |
| 9 | 構え | 150 |
| 10 | 大振り | 150 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 前のめり | 224 |
| 2 | 崩し | 182 |
| 3 | 貫き | 180 |
| 4 | 踏み込み | 163 |
| 5 | 集中 | 109 |
| 6 | 圧迫 | 103 |
| 7 | 渾身 | 73 |
| 8 | 粉砕 | 61 |
| 9 | 加速 | 53 |
| 10 | 返し刃 | 40 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 崩し | 175 |
| 2 | 貫き | 168 |
| 3 | 踏み込み | 154 |
| 4 | 渾身 | 69 |
| 5 | 粉砕 | 57 |
| 6 | 大振り | 37 |
| 7 | 返し刃 | 35 |
| 8 | 押し込み | 17 |
| 9 | 疾走 | 11 |
| 10 | 踏ん張り | 11 |

### BurstBot

- Win Rate: 53.7%
- Draw Rate: 11.8%
- First Pass Win Rate: 49.5%
- Win With Fewer Cards: 12.5%
- Win With Same Cards: 58.5%
- Win With More Cards: 29.1%
- Winner Facedown Avg: 1.44
- Loser Facedown Avg: 1.28
- Starting Player Win Rate: 56.3%
- Responding Player Win Rate: 50.5%
- Final Stats Avg: A=3.98, B=0.26, S=1.13
- Losing Final Stats Avg: A=4.37, B=0.18, S=-0.02
- Lost With Speed Advantage: 46 (4.3%)
- Won After Blocking Faster Attack: 113 (19.6%)
- Action Rates: set=23.1%, set_pass=65.8%, pass=11.2%
- Turn Stats: min=1, avg=1.4, max=50
- Winning Attack Stats: min=1, avg=3.72, max=18
- Winning Block Stats: min=0, avg=0.32, max=4
- Winning Speed Stats: min=-5, avg=1.86, max=7

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
| 1 | 返し刃 | 461 |
| 2 | 集中 | 312 |
| 3 | 前のめり | 303 |
| 4 | 渾身 | 248 |
| 5 | 圧迫 | 228 |
| 6 | 加速 | 216 |
| 7 | 踏み込み | 208 |
| 8 | 疾走 | 202 |
| 9 | 崩し | 165 |
| 10 | 貫き | 160 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 224 |
| 2 | 前のめり | 197 |
| 3 | 踏み込み | 155 |
| 4 | 疾走 | 146 |
| 5 | 圧迫 | 139 |
| 6 | 集中 | 136 |
| 7 | 加速 | 129 |
| 8 | 崩し | 115 |
| 9 | 貫き | 110 |
| 10 | 渾身 | 80 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 161 |
| 2 | 踏み込み | 146 |
| 3 | 疾走 | 114 |
| 4 | 崩し | 103 |
| 5 | 貫き | 97 |
| 6 | 渾身 | 72 |
| 7 | 粉砕 | 55 |
| 8 | 押し込み | 35 |
| 9 | 大振り | 32 |
| 10 | 踏ん張り | 17 |

### DefenseBot

- Win Rate: 47.8%
- Draw Rate: 6.8%
- First Pass Win Rate: 37.9%
- Win With Fewer Cards: 5.0%
- Win With Same Cards: 48.2%
- Win With More Cards: 46.8%
- Winner Facedown Avg: 1.41
- Loser Facedown Avg: 1.25
- Starting Player Win Rate: 52.3%
- Responding Player Win Rate: 43.4%
- Final Stats Avg: A=1.4, B=1.45, S=0.76
- Losing Final Stats Avg: A=0.83, B=1.33, S=0.79
- Lost With Speed Advantage: 154 (14.9%)
- Won After Blocking Faster Attack: 176 (35.5%)
- Action Rates: set=25.8%, set_pass=51.9%, pass=22.3%
- Turn Stats: min=1, avg=3.24, max=50
- Winning Attack Stats: min=1, avg=1.92, max=7
- Winning Block Stats: min=0, avg=1.63, max=11
- Winning Speed Stats: min=-3, avg=0.77, max=7

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
| 1 | 押し込み | 687 |
| 2 | 返し刃 | 657 |
| 3 | 構え | 536 |
| 4 | 受け流し | 527 |
| 5 | 蓄え | 452 |
| 6 | 牽制 | 435 |
| 7 | 鉄壁 | 400 |
| 8 | 十字受け | 340 |
| 9 | 踏ん張り | 326 |
| 10 | 退き足 | 324 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 378 |
| 2 | 押し込み | 348 |
| 3 | 構え | 271 |
| 4 | 受け流し | 252 |
| 5 | 牽制 | 234 |
| 6 | 蓄え | 207 |
| 7 | 鉄壁 | 201 |
| 8 | 踏ん張り | 176 |
| 9 | 補強 | 163 |
| 10 | 十字受け | 159 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 182 |
| 2 | 押し込み | 181 |
| 3 | 粉砕 | 76 |
| 4 | 踏ん張り | 71 |
| 5 | 受け流し | 48 |
| 6 | 十字受け | 38 |
| 7 | 渾身 | 28 |
| 8 | 低姿勢 | 26 |
| 9 | 貫き | 13 |
| 10 | 踏み込み | 10 |

### DisruptBot

- Win Rate: 53.4%
- Draw Rate: 11.7%
- First Pass Win Rate: 44.1%
- Win With Fewer Cards: 9.3%
- Win With Same Cards: 59.3%
- Win With More Cards: 31.4%
- Winner Facedown Avg: 1.45
- Loser Facedown Avg: 1.08
- Starting Player Win Rate: 59.5%
- Responding Player Win Rate: 48.3%
- Final Stats Avg: A=2.47, B=0.28, S=1.53
- Losing Final Stats Avg: A=1.65, B=0.39, S=0.94
- Lost With Speed Advantage: 109 (9.7%)
- Won After Blocking Faster Attack: 124 (20.7%)
- Action Rates: set=8.9%, set_pass=65.4%, pass=25.6%
- Turn Stats: min=1, avg=2.33, max=50
- Winning Attack Stats: min=1, avg=3.12, max=14
- Winning Block Stats: min=0, avg=0.24, max=2
- Winning Speed Stats: min=-3, avg=2.03, max=9

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
| 1 | 返し刃 | 394 |
| 2 | 圧迫 | 296 |
| 3 | 受け流し | 277 |
| 4 | 疾走 | 269 |
| 5 | 加速 | 262 |
| 6 | 牽制 | 256 |
| 7 | 崩し | 246 |
| 8 | 踏み込み | 225 |
| 9 | 貫き | 223 |
| 10 | 重心落とし | 158 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 疾走 | 194 |
| 2 | 踏み込み | 188 |
| 3 | 崩し | 179 |
| 4 | 圧迫 | 176 |
| 5 | 返し刃 | 163 |
| 6 | 貫き | 159 |
| 7 | 加速 | 157 |
| 8 | 牽制 | 124 |
| 9 | 重心落とし | 97 |
| 10 | 受け流し | 67 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 178 |
| 2 | 崩し | 170 |
| 3 | 疾走 | 155 |
| 4 | 貫き | 148 |
| 5 | 返し刃 | 94 |
| 6 | 渾身 | 31 |
| 7 | 粉砕 | 30 |
| 8 | 押し込み | 26 |
| 9 | 踏ん張り | 24 |
| 10 | 十字受け | 9 |

### GreedyBot

- Win Rate: 41.2%
- Draw Rate: 11.3%
- First Pass Win Rate: 31.0%
- Win With Fewer Cards: 9.3%
- Win With Same Cards: 52.4%
- Win With More Cards: 38.3%
- Winner Facedown Avg: 1.56
- Loser Facedown Avg: 1.21
- Starting Player Win Rate: 44.4%
- Responding Player Win Rate: 38.3%
- Final Stats Avg: A=2.71, B=0.53, S=0.76
- Losing Final Stats Avg: A=2.5, B=0.44, S=0.42
- Lost With Speed Advantage: 105 (9.5%)
- Won After Blocking Faster Attack: 148 (32.6%)
- Action Rates: set=23.8%, set_pass=45.1%, pass=31.1%
- Turn Stats: min=1, avg=2.25, max=50
- Winning Attack Stats: min=1, avg=2.93, max=11
- Winning Block Stats: min=0, avg=0.72, max=8
- Winning Speed Stats: min=-3, avg=1.15, max=11

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
| 1 | 返し刃 | 333 |
| 2 | 受け流し | 274 |
| 3 | 圧迫 | 272 |
| 4 | 渾身 | 233 |
| 5 | 押し込み | 213 |
| 6 | 貫き | 162 |
| 7 | 崩し | 148 |
| 8 | 踏ん張り | 147 |
| 9 | 十字受け | 145 |
| 10 | 踏み込み | 143 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 圧迫 | 138 |
| 2 | 返し刃 | 137 |
| 3 | 押し込み | 108 |
| 4 | 踏み込み | 104 |
| 5 | 崩し | 92 |
| 6 | 受け流し | 84 |
| 7 | 貫き | 83 |
| 8 | 踏ん張り | 70 |
| 9 | 疾走 | 67 |
| 10 | 渾身 | 62 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 99 |
| 2 | 返し刃 | 94 |
| 3 | 崩し | 79 |
| 4 | 貫き | 77 |
| 5 | 押し込み | 73 |
| 6 | 渾身 | 51 |
| 7 | 疾走 | 50 |
| 8 | 踏ん張り | 44 |
| 9 | 受け流し | 36 |
| 10 | 大振り | 28 |

### RandomBot

- Win Rate: 46.6%
- Draw Rate: 10.5%
- First Pass Win Rate: 35.7%
- Win With Fewer Cards: 7.3%
- Win With Same Cards: 46.3%
- Win With More Cards: 46.3%
- Winner Facedown Avg: 1.57
- Loser Facedown Avg: 1.41
- Starting Player Win Rate: 50.3%
- Responding Player Win Rate: 42.7%
- Final Stats Avg: A=2.43, B=0.67, S=1.34
- Losing Final Stats Avg: A=1.78, B=0.7, S=1.28
- Lost With Speed Advantage: 197 (16.8%)
- Won After Blocking Faster Attack: 150 (27.5%)
- Action Rates: set=21.4%, set_pass=56.2%, pass=22.4%
- Turn Stats: min=1, avg=2.8, max=50
- Winning Attack Stats: min=1, avg=3.06, max=15
- Winning Block Stats: min=0, avg=0.72, max=6
- Winning Speed Stats: min=-4, avg=1.48, max=12

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
| 1 | 返し刃 | 503 |
| 2 | 受け流し | 449 |
| 3 | 構え | 327 |
| 4 | 鉄壁 | 320 |
| 5 | 押し込み | 280 |
| 6 | 退き足 | 224 |
| 7 | 加速 | 212 |
| 8 | 集中 | 208 |
| 9 | 蓄え | 195 |
| 10 | 十字受け | 195 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 254 |
| 2 | 受け流し | 209 |
| 3 | 構え | 153 |
| 4 | 押し込み | 152 |
| 5 | 鉄壁 | 142 |
| 6 | 貫き | 112 |
| 7 | 踏み込み | 108 |
| 8 | 加速 | 108 |
| 9 | 崩し | 104 |
| 10 | 退き足 | 103 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 133 |
| 2 | 踏み込み | 99 |
| 3 | 崩し | 99 |
| 4 | 貫き | 97 |
| 5 | 押し込み | 85 |
| 6 | 疾走 | 64 |
| 7 | 渾身 | 58 |
| 8 | 大振り | 37 |
| 9 | 踏ん張り | 36 |
| 10 | 粉砕 | 35 |

### RiskBot

- Win Rate: 42.9%
- Draw Rate: 12.5%
- First Pass Win Rate: 38.9%
- Win With Fewer Cards: 9.2%
- Win With Same Cards: 57.1%
- Win With More Cards: 33.7%
- Winner Facedown Avg: 1.36
- Loser Facedown Avg: 1.33
- Starting Player Win Rate: 46.2%
- Responding Player Win Rate: 39.2%
- Final Stats Avg: A=2.64, B=0.93, S=0.42
- Losing Final Stats Avg: A=2.06, B=0.92, S=0.46
- Lost With Speed Advantage: 117 (10.8%)
- Won After Blocking Faster Attack: 215 (46.1%)
- Action Rates: set=9.9%, set_pass=61.3%, pass=28.8%
- Turn Stats: min=1, avg=3.14, max=50
- Winning Attack Stats: min=1, avg=3.41, max=15
- Winning Block Stats: min=0, avg=1.14, max=12
- Winning Speed Stats: min=-5, avg=0.28, max=7

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
| 1 | 構え | 458 |
| 2 | 返し刃 | 442 |
| 3 | 鉄壁 | 342 |
| 4 | 踏ん張り | 256 |
| 5 | 牽制 | 255 |
| 6 | 補強 | 242 |
| 7 | 十字受け | 232 |
| 8 | 受け流し | 226 |
| 9 | 渾身 | 218 |
| 10 | 押し込み | 201 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 構え | 188 |
| 2 | 返し刃 | 187 |
| 3 | 鉄壁 | 141 |
| 4 | 牽制 | 127 |
| 5 | 踏ん張り | 121 |
| 6 | 補強 | 112 |
| 7 | 踏み込み | 105 |
| 8 | 渾身 | 98 |
| 9 | 大振り | 78 |
| 10 | 押し込み | 77 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 101 |
| 2 | 返し刃 | 99 |
| 3 | 渾身 | 90 |
| 4 | 大振り | 75 |
| 5 | 踏ん張り | 57 |
| 6 | 貫き | 55 |
| 7 | 崩し | 44 |
| 8 | 鉄壁 | 35 |
| 9 | 押し込み | 30 |
| 10 | 受け流し | 13 |

### TempoBot

- Win Rate: 38.9%
- Draw Rate: 9.0%
- First Pass Win Rate: 34.8%
- Win With Fewer Cards: 12.3%
- Win With Same Cards: 70.5%
- Win With More Cards: 17.1%
- Winner Facedown Avg: 1.11
- Loser Facedown Avg: 0.96
- Starting Player Win Rate: 41.9%
- Responding Player Win Rate: 36.3%
- Final Stats Avg: A=1.51, B=0.3, S=1.99
- Losing Final Stats Avg: A=0.55, B=0.35, S=2.02
- Lost With Speed Advantage: 309 (26.4%)
- Won After Blocking Faster Attack: 71 (15.6%)
- Action Rates: set=2.9%, set_pass=73.3%, pass=23.7%
- Turn Stats: min=1, avg=2.53, max=50
- Winning Attack Stats: min=1, avg=2.67, max=10
- Winning Block Stats: min=0, avg=0.27, max=2
- Winning Speed Stats: min=-2, avg=2.17, max=8

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
| 1 | 返し刃 | 456 |
| 2 | 加速 | 443 |
| 3 | 受け流し | 336 |
| 4 | 疾走 | 315 |
| 5 | 踏み込み | 234 |
| 6 | 退き足 | 230 |
| 7 | 十字受け | 198 |
| 8 | 圧迫 | 198 |
| 9 | 勢い溜め | 150 |
| 10 | 重心落とし | 142 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 加速 | 198 |
| 2 | 踏み込み | 181 |
| 3 | 返し刃 | 148 |
| 4 | 疾走 | 148 |
| 5 | 圧迫 | 94 |
| 6 | 受け直し | 76 |
| 7 | 受け流し | 73 |
| 8 | 重心落とし | 61 |
| 9 | 勢い溜め | 54 |
| 10 | 十字受け | 53 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 171 |
| 2 | 疾走 | 121 |
| 3 | 返し刃 | 75 |
| 4 | 貫き | 35 |
| 5 | 粉砕 | 26 |
| 6 | 崩し | 25 |
| 7 | 渾身 | 24 |
| 8 | 踏ん張り | 16 |
| 9 | 押し込み | 9 |
| 10 | 大振り | 2 |

### TurtleBot

- Win Rate: 35.2%
- Draw Rate: 10.0%
- First Pass Win Rate: 31.2%
- Win With Fewer Cards: 5.3%
- Win With Same Cards: 57.3%
- Win With More Cards: 37.4%
- Winner Facedown Avg: 1.05
- Loser Facedown Avg: 0.88
- Starting Player Win Rate: 38.1%
- Responding Player Win Rate: 32.4%
- Final Stats Avg: A=0.88, B=1.09, S=0.28
- Losing Final Stats Avg: A=0.38, B=1.02, S=0.36
- Lost With Speed Advantage: 148 (13.1%)
- Won After Blocking Faster Attack: 195 (49.2%)
- Action Rates: set=5.0%, set_pass=61.2%, pass=33.8%
- Turn Stats: min=1, avg=4.76, max=50
- Winning Attack Stats: min=1, avg=1.64, max=5
- Winning Block Stats: min=0, avg=1.36, max=9
- Winning Speed Stats: min=-4, avg=0.14, max=2

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
| 1 | 返し刃 | 689 |
| 2 | 構え | 639 |
| 3 | 蓄え | 617 |
| 4 | 鉄壁 | 550 |
| 5 | 押し込み | 510 |
| 6 | 補強 | 464 |
| 7 | 踏ん張り | 452 |
| 8 | 牽制 | 452 |
| 9 | 低姿勢 | 407 |
| 10 | 十字受け | 346 |

### Winner Side Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 331 |
| 2 | 構え | 279 |
| 3 | 鉄壁 | 238 |
| 4 | 蓄え | 237 |
| 5 | 踏ん張り | 222 |
| 6 | 牽制 | 222 |
| 7 | 補強 | 218 |
| 8 | 押し込み | 209 |
| 9 | 低姿勢 | 176 |
| 10 | 受け流し | 128 |

### Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 140 |
| 2 | 踏ん張り | 91 |
| 3 | 押し込み | 70 |
| 4 | 踏み込み | 21 |
| 5 | 渾身 | 19 |
| 6 | 大振り | 17 |
| 7 | 崩し | 14 |
| 8 | 粉砕 | 13 |
| 9 | 低姿勢 | 10 |
| 10 | 貫き | 9 |
