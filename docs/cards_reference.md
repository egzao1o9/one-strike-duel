# Cards Reference

## Summary

- Total Cards: 28
- Battle Cards: 17
- Control Cards: 11

## Card List

| ID | Name | Type | Attack | Block | Speed | Tags |
|---|---|---|---:|---:|---:|---|
| `battle_afterimage` | 残像 | `battle` | 0 | 1 | 6 | speed |
| `battle_all_in` | 渾身 | `battle` | 4 | 0 | -1 | attack, finisher |
| `battle_backstep` | 退き足 | `battle` | -1 | 2 | 3 | speed, defense |
| `battle_brace` | 踏ん張り | `battle` | 1 | 2 | 0 | balanced |
| `battle_break` | 崩し | `battle` | 2 | 0 | 2 | attack |
| `battle_counter` | 返し刃 | `battle` | 2 | 2 | 1 | balanced |
| `battle_cross_guard` | 十字受け | `battle` | 0 | 2 | 2 | defense, speed |
| `battle_crush` | 粉砕 | `battle` | 3 | -1 | 0 | attack, risk |
| `battle_dash` | 疾走 | `battle` | 1 | 0 | 5 | speed, risk |
| `battle_feint` | フェイント | `battle` | -1 | 0 | 4 | speed, trick |
| `battle_guard` | 受け流し | `battle` | 0 | 3 | 1 | defense |
| `battle_heavy_swing` | 大振り | `battle` | 4 | 0 | -2 | attack, heavy |
| `battle_low_stance` | 低姿勢 | `battle` | 1 | 3 | -1 | defense |
| `battle_pierce` | 貫き | `battle` | 3 | 0 | 1 | attack |
| `battle_press` | 押し込み | `battle` | 2 | 1 | 2 | balanced |
| `battle_step_in` | 踏み込み | `battle` | 3 | 0 | 2 | attack, risk |
| `battle_wall` | 鉄壁 | `battle` | -1 | 4 | -2 | defense, heavy |
| `control_anchor` | 重心落とし | `control` | 0 | 0 | 0 | debuff |
| `control_cover` | 受け直し | `control` | 0 | 0 | 0 | buff |
| `control_disrupt` | 牽制 | `control` | 0 | 0 | 0 | debuff |
| `control_focus` | 集中 | `control` | 0 | 0 | 0 | buff, next_turn |
| `control_fortify` | 補強 | `control` | 0 | 0 | 0 | buff |
| `control_guard` | 構え | `control` | 0 | 0 | 0 | buff |
| `control_haste` | 加速 | `control` | 0 | 0 | 0 | buff |
| `control_momentum` | 勢い溜め | `control` | 0 | 0 | 0 | next_turn |
| `control_overclock` | 前のめり | `control` | 0 | 0 | 0 | buff, risk |
| `control_pressure` | 圧迫 | `control` | 0 | 0 | 0 | debuff |
| `control_reserve` | 蓄え | `control` | 0 | 0 | 0 | next_turn |

## Details

### 残像

- ID: `battle_afterimage`
- Type: `battle`
- Stats: `A=0 / B=1 / S=6`
- Tags: speed
- Notes: 極端に速いが打点は持たない。
- Effects: なし

### 渾身

- ID: `battle_all_in`
- Type: `battle`
- Stats: `A=4 / B=0 / S=-1`
- Tags: attack, finisher
- Notes: 高火力だが無防備で遅い。
- Effects:
  - `battle` / `set_self_block_limit` / value=0

### 退き足

- ID: `battle_backstep`
- Type: `battle`
- Stats: `A=-1 / B=2 / S=3`
- Tags: speed, defense
- Notes: 攻めない代わりに位置取りを優先する。
- Effects: なし

### 踏ん張り

- ID: `battle_brace`
- Type: `battle`
- Stats: `A=1 / B=2 / S=0`
- Tags: balanced
- Notes: 大きな弱点のない中継ぎ。
- Effects: なし

### 崩し

- ID: `battle_break`
- Type: `battle`
- Stats: `A=2 / B=0 / S=2`
- Tags: attack
- Notes: 相手の防御を崩す。
- Effects:
  - `battle` / `modify_opponent_block` / value=1

### 返し刃

- ID: `battle_counter`
- Type: `battle`
- Stats: `A=2 / B=2 / S=1`
- Tags: balanced
- Notes: 平均的なカウンター向けカード。
- Effects: なし

### 十字受け

- ID: `battle_cross_guard`
- Type: `battle`
- Stats: `A=0 / B=2 / S=2`
- Tags: defense, speed
- Notes: 軽い受けでテンポを維持する。
- Effects: なし

### 粉砕

- ID: `battle_crush`
- Type: `battle`
- Stats: `A=3 / B=-1 / S=0`
- Tags: attack, risk
- Notes: 前のめりで防御に穴が空く。
- Effects: なし

### 疾走

- ID: `battle_dash`
- Type: `battle`
- Stats: `A=1 / B=0 / S=5`
- Tags: speed, risk
- Notes: 最速クラスだが防御はない。
- Effects: なし

### フェイント

- ID: `battle_feint`
- Type: `battle`
- Stats: `A=-1 / B=0 / S=4`
- Tags: speed, trick
- Notes: 先制は取りやすいが決定打にはならない。
- Effects: なし

### 受け流し

- ID: `battle_guard`
- Type: `battle`
- Stats: `A=0 / B=3 / S=1`
- Tags: defense
- Notes: 堅実な防御。
- Effects: なし

### 大振り

- ID: `battle_heavy_swing`
- Type: `battle`
- Stats: `A=4 / B=0 / S=-2`
- Tags: attack, heavy
- Notes: 威力は大きいがかなり遅い。
- Effects: なし

### 低姿勢

- ID: `battle_low_stance`
- Type: `battle`
- Stats: `A=1 / B=3 / S=-1`
- Tags: defense
- Notes: 守りやすいが主導権は取りづらい。
- Effects: なし

### 貫き

- ID: `battle_pierce`
- Type: `battle`
- Stats: `A=3 / B=0 / S=1`
- Tags: attack
- Notes: 防御を削りながら通しにいく。
- Effects:
  - `battle` / `modify_opponent_block` / value=1

### 押し込み

- ID: `battle_press`
- Type: `battle`
- Stats: `A=2 / B=1 / S=2`
- Tags: balanced
- Notes: 標準的な攻防一体カード。
- Effects: なし

### 踏み込み

- ID: `battle_step_in`
- Type: `battle`
- Stats: `A=3 / B=0 / S=2`
- Tags: attack, risk
- Notes: このターン、自分はブロック値を得られない。
- Effects:
  - `battle` / `set_self_block_limit` / value=0

### 鉄壁

- ID: `battle_wall`
- Type: `battle`
- Stats: `A=-1 / B=4 / S=-2`
- Tags: defense, heavy
- Notes: 非常に硬いが、攻撃できず動きも重い。
- Effects: なし

### 重心落とし

- ID: `control_anchor`
- Type: `control`
- Stats: `A=0 / B=0 / S=0`
- Tags: debuff
- Notes: このターン、相手の素早さ-2。
- Effects:
  - `battle` / `modify_opponent_speed` / value=2

### 受け直し

- ID: `control_cover`
- Type: `control`
- Stats: `A=0 / B=0 / S=0`
- Tags: buff
- Notes: このターン、ブロック+1、素早さ+1。
- Effects:
  - `battle` / `modify_self_block` / value=1
  - `battle` / `modify_self_speed` / value=1

### 牽制

- ID: `control_disrupt`
- Type: `control`
- Stats: `A=0 / B=0 / S=0`
- Tags: debuff
- Notes: このターン、相手の攻撃-1。
- Effects:
  - `battle` / `modify_opponent_attack` / value=1

### 集中

- ID: `control_focus`
- Type: `control`
- Stats: `A=0 / B=0 / S=0`
- Tags: buff, next_turn
- Notes: 次ターン、自分の攻撃+1。
- Effects:
  - `next_turn` / `modify_self_attack` / value=1

### 補強

- ID: `control_fortify`
- Type: `control`
- Stats: `A=0 / B=0 / S=0`
- Tags: buff
- Notes: このターン、自分のブロック+2。
- Effects:
  - `battle` / `modify_self_block` / value=2

### 構え

- ID: `control_guard`
- Type: `control`
- Stats: `A=0 / B=0 / S=0`
- Tags: buff
- Notes: このターン、自分のブロック+1。
- Effects:
  - `battle` / `modify_self_block` / value=1

### 加速

- ID: `control_haste`
- Type: `control`
- Stats: `A=0 / B=0 / S=0`
- Tags: buff
- Notes: このターン、自分の素早さ+2。
- Effects:
  - `battle` / `modify_self_speed` / value=2

### 勢い溜め

- ID: `control_momentum`
- Type: `control`
- Stats: `A=0 / B=0 / S=0`
- Tags: next_turn
- Notes: 次ターン、自分の素早さ+2。
- Effects:
  - `next_turn` / `modify_self_speed` / value=2

### 前のめり

- ID: `control_overclock`
- Type: `control`
- Stats: `A=0 / B=0 / S=0`
- Tags: buff, risk
- Notes: このターン、攻撃+1、素早さ+1。
- Effects:
  - `battle` / `modify_self_attack` / value=1
  - `battle` / `modify_self_speed` / value=1

### 圧迫

- ID: `control_pressure`
- Type: `control`
- Stats: `A=0 / B=0 / S=0`
- Tags: debuff
- Notes: このターン、相手のブロック-1。
- Effects:
  - `battle` / `modify_opponent_block` / value=1

### 蓄え

- ID: `control_reserve`
- Type: `control`
- Stats: `A=0 / B=0 / S=0`
- Tags: next_turn
- Notes: 次ターン開始時、追加で1枚引く。
- Effects:
  - `next_turn` / `draw_cards` / value=1
