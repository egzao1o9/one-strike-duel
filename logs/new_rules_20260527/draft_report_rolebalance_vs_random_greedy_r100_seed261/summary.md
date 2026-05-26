# Draft Role Balance Report

## Configuration

- Draft Bot 1: `RoleBalanceDraftBot`
- Draft Bot 2: `RandomDraftBot`
- Play Bot 1: `GreedyBot`
- Play Bot 2: `GreedyBot`
- Rounds: 100
- Total Matches: 200
- Seed: 261
- Pool: `base_pool` (59 copies)
- Pairing Mode: mirrored seats per round

## Drafter Summary

| Drafter | Matches | Wins | Losses | Draws | Win Rate | Battle Avg | Control Avg | Red Avg | Blue Avg | Green Avg | White Avg | Common Avg | Uncommon Avg | Rare Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `RandomDraftBot` | 200 | 118 | 59 | 23 | 59.0% | 10.62 | 9.38 | 5.97 | 2.88 | 1.77 | 9.38 | 11.62 | 7.96 | 0.42 |
| `RoleBalanceDraftBot` | 200 | 59 | 118 | 23 | 29.5% | 12.04 | 7.96 | 6.76 | 2.98 | 2.31 | 7.96 | 0.3 | 14.12 | 5.58 |

## Pair Summary

| Pair | Matches | Draws | Wins | Turn Avg |
|---|---:|---:|---|---:|
| RandomDraftBot vs RoleBalanceDraftBot | 200 | 23 | `RandomDraftBot`=118, `RoleBalanceDraftBot`=59 | 1.07 |

## Match Card Highlights

### Most Used Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 圧迫 | 91 |
| 2 | 踏み込み | 71 |
| 3 | 渾身 | 68 |
| 4 | 返し刃 | 55 |
| 5 | 押し込み | 50 |
| 6 | 粉砕 | 50 |
| 7 | 貫き | 47 |
| 8 | 大振り | 43 |
| 9 | 崩し | 24 |
| 10 | 踏ん張り | 23 |
| 11 | 十字受け | 18 |
| 12 | 低姿勢 | 14 |
| 13 | 受け流し | 13 |
| 14 | 鉄壁 | 9 |
| 15 | 退き足 | 9 |

### Most Effective Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 圧迫 | 44 |
| 2 | 返し刃 | 41 |
| 3 | 押し込み | 41 |
| 4 | 踏み込み | 39 |
| 5 | 粉砕 | 28 |
| 6 | 貫き | 21 |
| 7 | 崩し | 16 |
| 8 | 踏ん張り | 16 |
| 9 | 渾身 | 11 |
| 10 | 十字受け | 9 |
| 11 | 低姿勢 | 9 |
| 12 | 大振り | 4 |
| 13 | 受け流し | 4 |
| 14 | 鉄壁 | 4 |
| 15 | 疾走 | 3 |

### Most Lethal Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 押し込み | 40 |
| 2 | 返し刃 | 40 |
| 3 | 踏み込み | 38 |
| 4 | 粉砕 | 27 |
| 5 | 貫き | 21 |
| 6 | 崩し | 15 |
| 7 | 踏ん張り | 14 |
| 8 | 渾身 | 8 |
| 9 | 十字受け | 7 |
| 10 | 低姿勢 | 6 |
| 11 | 大振り | 4 |
| 12 | 受け流し | 2 |
| 13 | 疾走 | 2 |
| 14 | 退き足 | 1 |
| 15 | 残像 | 1 |

## Drafter Details

### RandomDraftBot

- Win Rate: 59.0%
- Draw Rate: 11.5%
- Turns: min=1, avg=1.07, max=3
- Battle / Control: avg=10.62 / 9.38
- Role Colors: red=5.97, blue=2.88, green=1.77, white=9.38
- Rarities: common=11.62, uncommon=7.96, rare=0.42

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 圧迫 | 277 |
| 2 | 踏ん張り | 275 |
| 3 | 構え | 262 |
| 4 | 返し刃 | 261 |
| 5 | 牽制 | 260 |
| 6 | 十字受け | 256 |
| 7 | 集中 | 252 |
| 8 | 押し込み | 243 |
| 9 | 受け流し | 237 |
| 10 | フェイント | 182 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 返し刃 | 168 |
| 2 | 圧迫 | 160 |
| 3 | 踏ん張り | 158 |
| 4 | 押し込み | 157 |
| 5 | 牽制 | 155 |
| 6 | 十字受け | 153 |
| 7 | 構え | 152 |
| 8 | 集中 | 143 |
| 9 | 受け流し | 132 |
| 10 | フェイント | 110 |

#### Match Logs

- [draft_match_0001](matches/match_0001_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0002](matches/match_0002_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0003](matches/match_0003_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0004](matches/match_0004_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0005](matches/match_0005_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0006](matches/match_0006_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0007](matches/match_0007_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0008](matches/match_0008_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0009](matches/match_0009_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0010](matches/match_0010_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0011](matches/match_0011_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0012](matches/match_0012_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0013](matches/match_0013_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0014](matches/match_0014_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0015](matches/match_0015_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0016](matches/match_0016_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0017](matches/match_0017_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0018](matches/match_0018_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0019](matches/match_0019_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0020](matches/match_0020_RandomDraftBot_vs_RoleBalanceDraftBot.md)

### RoleBalanceDraftBot

- Win Rate: 29.5%
- Draw Rate: 11.5%
- Turns: min=1, avg=1.07, max=3
- Battle / Control: avg=12.04 / 7.96
- Role Colors: red=6.76, blue=2.98, green=2.31, white=7.96
- Rarities: common=0.3, uncommon=14.12, rare=5.58

### Most Picked Cards

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 351 |
| 2 | 貫き | 324 |
| 3 | 受け直し | 282 |
| 4 | 前のめり | 265 |
| 5 | 低姿勢 | 263 |
| 6 | 加速 | 226 |
| 7 | 勢い溜め | 213 |
| 8 | 補強 | 210 |
| 9 | 重心落とし | 208 |
| 10 | 渾身 | 199 |

### Winning Deck Usage

| Rank | Name | Count |
|---:|---|---:|
| 1 | 踏み込み | 108 |
| 2 | 貫き | 91 |
| 3 | 低姿勢 | 83 |
| 4 | 受け直し | 82 |
| 5 | 前のめり | 76 |
| 6 | 勢い溜め | 67 |
| 7 | 加速 | 66 |
| 8 | 重心落とし | 61 |
| 9 | 補強 | 61 |
| 10 | 渾身 | 59 |

#### Match Logs

- [draft_match_0001](matches/match_0001_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0002](matches/match_0002_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0003](matches/match_0003_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0004](matches/match_0004_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0005](matches/match_0005_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0006](matches/match_0006_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0007](matches/match_0007_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0008](matches/match_0008_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0009](matches/match_0009_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0010](matches/match_0010_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0011](matches/match_0011_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0012](matches/match_0012_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0013](matches/match_0013_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0014](matches/match_0014_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0015](matches/match_0015_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0016](matches/match_0016_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0017](matches/match_0017_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0018](matches/match_0018_RandomDraftBot_vs_RoleBalanceDraftBot.md)
- [draft_match_0019](matches/match_0019_RoleBalanceDraftBot_vs_RandomDraftBot.md)
- [draft_match_0020](matches/match_0020_RandomDraftBot_vs_RoleBalanceDraftBot.md)
