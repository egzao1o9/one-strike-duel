# Aggregate Report

## Inventory

| Type | Title | Path |
|---|---|---|
| `deck_tournament` | AttackBot | `bot_suite_x5_seed41/AttackBot/summary.json` |
| `deck_tournament` | BurstBot | `bot_suite_x5_seed41/BurstBot/summary.json` |
| `deck_tournament` | DefenseBot | `bot_suite_x5_seed41/DefenseBot/summary.json` |
| `deck_tournament` | DisruptBot | `bot_suite_x5_seed41/DisruptBot/summary.json` |
| `deck_tournament` | GreedyBot | `bot_suite_x5_seed41/GreedyBot/summary.json` |
| `deck_tournament` | RandomBot | `bot_suite_x5_seed41/RandomBot/summary.json` |
| `deck_tournament` | RiskBot | `bot_suite_x5_seed41/RiskBot/summary.json` |
| `deck_tournament` | TempoBot | `bot_suite_x5_seed41/TempoBot/summary.json` |
| `deck_tournament` | TurtleBot | `bot_suite_x5_seed41/TurtleBot/summary.json` |
| `deck_tournament` | deck_tournament_greedybot_x5_seed31 | `deck_tournament_greedybot_x5_seed31/summary.json` |
| `draft_report` | draft_report_rolebalancedraftbot_vs_randomdraftbot_greedybot_greedybot_r50_seed131 | `draft_report_rolebalancedraftbot_vs_randomdraftbot_greedybot_greedybot_r50_seed131/summary.json` |
| `random_bot_mix` | random_bot_mix_200_seed101 | `random_bot_mix_200_seed101/summary.json` |
| `random_bot_mix` | random_bot_mix_5000_seed101 | `random_bot_mix_5000_seed101/summary.json` |

## Random Bot Mix

| Matches | Seed | Top Bot | Top Win Rate | Bottom Bot | Bottom Win Rate | Path |
|---:|---:|---|---:|---|---:|---|
| 200 | 101 | `RandomBot` | 61.2% | `TempoBot` | 32.5% | `random_bot_mix_200_seed101/summary.json` |
| 5000 | 101 | `DefenseBot` | 60.5% | `GreedyBot` | 38.8% | `random_bot_mix_5000_seed101/summary.json` |

### Canonical Bot Ranking

| Rank | Bot | Matches | Wins | Losses | Draws | Win Rate | Turn Avg |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `DefenseBot` | 1050 | 635 | 411 | 4 | 60.5% | 2.45 |
| 2 | `AttackBot` | 1087 | 613 | 470 | 4 | 56.4% | 1.55 |
| 3 | `RiskBot` | 1128 | 617 | 498 | 13 | 54.7% | 2.38 |
| 4 | `DisruptBot` | 1136 | 588 | 527 | 21 | 51.8% | 2.57 |
| 5 | `BurstBot` | 1135 | 561 | 568 | 6 | 49.4% | 1.6 |
| 6 | `RandomBot` | 1128 | 527 | 580 | 21 | 46.7% | 2.66 |
| 7 | `TurtleBot` | 1107 | 478 | 588 | 41 | 43.2% | 4.05 |
| 8 | `TempoBot` | 1098 | 468 | 616 | 14 | 42.6% | 2.36 |
| 9 | `GreedyBot` | 1131 | 439 | 668 | 24 | 38.8% | 2.61 |

### Random Mix Stability

| Bot | Small Sample | Large Sample | Delta |
|---|---:|---:|---:|
| `DefenseBot` | 60.9% | 60.5% | -0.5pt |
| `AttackBot` | 58.7% | 56.4% | -2.3pt |
| `RiskBot` | 48.6% | 54.7% | +6.0pt |
| `DisruptBot` | 45.2% | 51.8% | +6.5pt |
| `BurstBot` | 51.3% | 49.4% | -1.9pt |
| `RandomBot` | 61.2% | 46.7% | -14.5pt |
| `TurtleBot` | 35.7% | 43.2% | +7.5pt |
| `TempoBot` | 32.5% | 42.6% | +10.1pt |
| `GreedyBot` | 39.0% | 38.8% | -0.2pt |

### Most Used Cards

| Rank | Card | Count |
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

### Most Effective Cards

| Rank | Card | Count |
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

### Most Lethal Cards

| Rank | Card | Count |
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

## Deck Overview

| Deck | Avg Win Rate | Min | Max | Avg Turns | Best Bot | Worst Bot |
|---|---:|---:|---:|---:|---|---|
| `starter_balanced` | 63.2% | 47.5% | 75.0% | 3.15 | `RandomBot` | `DisruptBot` |
| `starter_defense` | 55.2% | 32.5% | 80.0% | 3.57 | `DefenseBot` | `TempoBot` |
| `starter_attack` | 53.5% | 27.5% | 75.0% | 2.05 | `DisruptBot` | `TurtleBot` |
| `starter_speed` | 46.8% | 17.5% | 82.5% | 2.39 | `BurstBot` | `RandomBot` |
| `starter_heavy` | 25.5% | 5.0% | 40.0% | 3.68 | `RandomBot` | `BurstBot` |

### Bot x Deck Fit

| Bot | Avg Deck Win Rate | Best Deck | Best Rate | Worst Deck | Worst Rate |
|---|---:|---|---:|---|---:|
| `AttackBot` | 50.0% | `starter_balanced` | 65.0% | `starter_heavy` | 12.5% |
| `BurstBot` | 50.0% | `starter_speed` | 82.5% | `starter_heavy` | 5.0% |
| `DefenseBot` | 50.0% | `starter_defense` | 80.0% | `starter_speed` | 20.0% |
| `DisruptBot` | 50.0% | `starter_attack` | 75.0% | `starter_heavy` | 22.5% |
| `RandomBot` | 49.5% | `starter_balanced` | 75.0% | `starter_speed` | 17.5% |
| `RiskBot` | 49.5% | `starter_defense` | 65.0% | `starter_heavy` | 30.0% |
| `TempoBot` | 49.5% | `starter_attack` | 75.0% | `starter_heavy` | 30.0% |
| `GreedyBot` | 47.8% | `starter_balanced` | 75.0% | `starter_heavy` | 12.5% |
| `TurtleBot` | 44.5% | `starter_defense` | 80.0% | `starter_speed` | 20.0% |

## Draft Reports

### RoleBalanceDraftBot vs RandomDraftBot

- Matches: 100
- Play Bots: `GreedyBot` / `GreedyBot`
- Path: `draft_report_rolebalancedraftbot_vs_randomdraftbot_greedybot_greedybot_r50_seed131/summary.json`

| Rank | Drafter | Win Rate | Battle Avg | Control Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `RoleBalanceDraftBot` | 51.0% | 12.01 | 7.99 | 6.73 | 2.97 | 2.31 | 7.99 | 0.29 | 14.21 | 5.5 |
| 2 | `RandomDraftBot` | 48.0% | 10.8 | 9.2 | 6.13 | 2.87 | 1.8 | 9.2 | 11.59 | 7.91 | 0.5 |

## Light Analysis

- 最大試行の Bot 混成では `DefenseBot` が 60.5% で首位、`GreedyBot` は 38.8% で、上下差は 21.7pt です。
- 上位 3 Bot は `DefenseBot`, `AttackBot`, `RiskBot` で、防御寄りと高打点寄りの方針が安定しています。
- Bot 混成の試行数を 200 戦から 5000 戦へ増やすと、各 Bot の勝率差分は平均 5.5pt で、傾向はかなり安定しました。
- 固定デッキ群では平均勝率トップが `starter_balanced` 63.2%、最下位が `starter_heavy` 25.5% です。
- 勝率上位デッキは決着も比較的速く、テンポ優位がそのまま成績に出ています。
- ドラフト比較では `RoleBalanceDraftBot` が 51.0% で僅差優位です。役割バランスを見た指名は有効ですが、現状の差は小さく、さらなる評価関数の改善余地があります。
- `RoleBalanceDraftBot` は平均で battle 12.01 / control 7.99、`RandomDraftBot` は battle 10.8 / control 9.2 で、枚数配分の差がそのまま構築方針に出ています。
