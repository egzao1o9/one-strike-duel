# One Strike Duel：カード管理スキーマ拡張と加護カード実装仕様

## 目的

現在のカード管理を、今後のカード種類追加に耐えられる形へ整理する。

特に以下を目的とする。

- Notion上でカード効果を編集しやすくする
- カード本体情報と効果情報を分離する
- CSV / JSON import-export を安定させる
- ランタイム側では壊れにくい構造化JSONとして扱う
- 将来的に「加護カード」のような場に残るカードを追加できる土台を作る
- 既存のバトルカード / コントロールカードを壊さず段階的に移行する

今回の実装では、加護カードを大量追加することが目的ではない。  
まずは「加護カードを扱える土台」を作ることを優先する。

---

## 設計方針

### 基本方針

カード管理は以下の2テーブル構造にする。

- `Cards`
- `CardEffects`

`Cards` はカード本体情報を持つ。  
`CardEffects` はカードに紐づく効果を、1効果1行で持つ。

1枚のカードが複数の効果を持つ可能性があるため、カード1行にすべての効果を押し込まない。

---

## Notion管理の考え方

Notion上では編集しやすさを優先する。

そのため、効果を完全に細分化しすぎず、以下のような中間表現で管理する。

- `trigger`
- `effect_type`
- `target`
- `stat`
- `value`
- `duration`
- `active_zone`
- `condition`
- `params_json`

Notion上では `target` を1列で持つ。  
export時に必要であれば、ランタイムJSON側で `side / layer / zone / selector` などに展開する。

---

## Cards テーブル仕様

### 必須列

| 列名 | 型 | 説明 |
|---|---|---|
| `id` | text | カードID。内部処理用。ユニーク必須 |
| `name` | text | 表示名 |
| `rarity` | select | `common` / `uncommon` / `rare` |
| `card_type` | select | `battle` / `control` / `blessing` |
| `attack` | number | 基礎攻撃値。不要なら0 |
| `block` | number | 基礎防御値。不要なら0 |
| `speed` | number | 基礎速度値。不要なら0 |
| `tags` | text | カンマ区切りタグ |
| `public_text` | text | カードに表示する効果文 |
| `enabled` | checkbox / bool | 使用可能か |

### 追加列

| 列名 | 型 | 説明 |
|---|---|---|
| `play_zone` | select | 使用時に置かれる場所 |
| `after_play_zone` | select | 使用後に移動する場所 |
| `slot_type` | select | 専用スロット種別。加護なら `blessing` |
| `flavor_text` | text | フレーバーテキスト。任意 |
| `notes` | text | 開発メモ |

---

## card_type

### `battle`

既存のバトルカード。

- バトル時に伏せる
- 公開時に値や効果を解決する
- バトル終了後、基本的に捨て札へ行く

推奨設定：

| 項目 | 値 |
|---|---|
| `card_type` | `battle` |
| `play_zone` | `set` |
| `after_play_zone` | `discard` |
| `slot_type` | 空欄 |

---

### `control`

既存のコントロールカード。

- 即時使用する
- 使用後、基本的に捨て札へ行く
- ドロー、妨害、マリガン調整などに使う

推奨設定：

| 項目 | 値 |
|---|---|
| `card_type` | `control` |
| `play_zone` | `instant` |
| `after_play_zone` | `discard` |
| `slot_type` | 空欄 |

---

### `blessing`

新規追加する加護カード。

- 使用すると専用の `blessing_zone` に置かれる
- 場にある限り効果を発揮する
- 各プレイヤーの加護ゾーンには1枚まで置ける
- 新しい加護カードを置く場合、既存の加護カードは捨て札へ送る

推奨設定：

| 項目 | 値 |
|---|---|
| `card_type` | `blessing` |
| `play_zone` | `blessing_zone` |
| `after_play_zone` | `blessing_zone` |
| `slot_type` | `blessing` |

---

## CardEffects テーブル仕様

### 基本列

| 列名 | 型 | 説明 |
|---|---|---|
| `id` | text | 効果ID。ユニーク推奨 |
| `card_id` | relation/text | 対象カードID |
| `seq` | number | 同一カード内の効果順 |
| `enabled` | checkbox/bool | 効果を有効化するか |
| `trigger` | select | 効果が発火するタイミング |
| `priority` | number | 同一trigger内での処理順 |
| `effect_type` | select | 効果の種類 |
| `target` | select | 対象 |
| `stat` | select | 対象ステータス |
| `value` | number | 主数値 |
| `value2` | number | 補助数値 |
| `count` | number | 枚数など |
| `duration` | select | 効果の持続期間 |
| `active_zone` | select | 効果が有効になるゾーン |
| `condition` | select/text | 発動条件 |
| `keyword` | text | 人間向けの効果ラベル |
| `display_text` | text | 印刷/表示用の効果文 |
| `params_json` | text/json | 特殊効果用の追加パラメータ |
| `notes` | text | 開発メモ |

---

## trigger

`trigger` は効果が発火するタイミングを表す。

最初に対応したい候補は以下。

| trigger | 説明 |
|---|---|
| `passive` | 常時有効。主に加護カード用 |
| `on_reveal` | バトルカード公開時 |
| `on_battle_start` | バトル開始時 |
| `on_battle_calculate` | バトル最終値計算時 |
| `on_battle_resolve` | バトル結果確定時 |
| `on_turn_start` | ターン開始時 |
| `on_draw_step` | 通常ドロー処理時 |
| `on_turn_end` | ターン終了時 |
| `on_play` | カード使用時 |
| `on_discard` | 捨て札へ送られた時 |
| `on_mulligan` | マリガン処理時 |

### 加護カードで主に使う trigger

加護カードでは特に以下を使う。

- `passive`
- `on_draw_step`
- `on_battle_calculate`
- `on_turn_start`

---

## duration

`duration` は効果の持続期間を表す。

| duration | 説明 |
|---|---|
| `instant` | 即時効果 |
| `current_battle` | 現在のバトル中のみ |
| `current_turn` | 現在のターン中のみ |
| `next_turn` | 次のターン中のみ |
| `while_in_zone` | 指定ゾーンにある間だけ有効 |
| `until_used` | 使用されるまで有効 |
| `permanent` | 永続。基本的には使用非推奨 |

加護カードは基本的に以下を使う。

```text
 duration = while_in_zone
 active_zone = blessing_zone
```

---

## active_zone

`active_zone` は、その効果が有効になるゾーンを表す。

| active_zone | 説明 |
|---|---|
| 空欄 | ゾーン条件なし |
| `set` | 伏せカードゾーン |
| `hand` | 手札 |
| `deck` | 山札 |
| `discard` | 捨て札 |
| `blessing_zone` | 加護ゾーン |

加護カードの常時効果は、原則として `active_zone = blessing_zone` を指定する。

---

## effect_type

最初に対応したい効果タイプ。

| effect_type | 説明 |
|---|---|
| `modify_total_stat` | 最終合計値を修正する |
| `modify_card_stat` | カード単体の値を修正する |
| `modify_rule_value` | ドロー枚数などルール値を修正する |
| `draw_cards` | カードを引く |
| `discard_cards` | カードを捨てる |
| `reveal_cards` | カードを公開する |
| `negate_card` | カード効果またはカード値を無効化する |
| `adjust_mulligan` | マリガン関連値を修正する |
| `adjust_draw_limit` | ドロー上限などを修正する |
| `replace_zone_card` | 専用ゾーンのカードを入れ替える |
| `custom` | 特殊処理用 |

---

## target

Notion上では、編集しやすさのために `target` は1列で管理する。

初期候補：

| target | 説明 |
|---|---|
| `self_player` | 自分プレイヤー |
| `opponent_player` | 相手プレイヤー |
| `both_players` | 両プレイヤー |
| `self_total` | 自分の最終合計値 |
| `opponent_total` | 相手の最終合計値 |
| `self_card` | 自分のカード単体 |
| `opponent_card` | 相手のカード単体 |
| `self_set_cards` | 自分の伏せカード群 |
| `opponent_set_cards` | 相手の伏せカード群 |
| `self_hand` | 自分の手札 |
| `opponent_hand` | 相手の手札 |
| `self_deck` | 自分の山札 |
| `opponent_deck` | 相手の山札 |
| `self_discard` | 自分の捨て札 |
| `opponent_discard` | 相手の捨て札 |
| `self_blessing_zone` | 自分の加護ゾーン |
| `opponent_blessing_zone` | 相手の加護ゾーン |

export時にランタイムJSONへ変換する際、必要に応じて以下のような構造に展開する。

```json
{
  "side": "opponent",
  "layer": "total",
  "zone": null,
  "selector": null
}
```

---

## stat

| stat | 説明 |
|---|---|
| `attack` | 攻撃 |
| `block` | 防御 |
| `speed` | 速度 |
| `draw_per_turn` | 通常ドロー枚数 |
| `hand_limit` | 手札上限 |
| `mulligan_count` | マリガン可能回数 |
| `battle_card_limit` | バトルカード上限 |
| 空欄 | stat不要の効果 |

---

## 加護ゾーン仕様

### 基本

各プレイヤーは `blessing_zone` を1つ持つ。

```text
 player.blessing_zone: Card | null
```

### 制限

- 各プレイヤーの加護ゾーンに置ける加護カードは1枚まで
- 新しい加護カードを使用する場合、古い加護カードを捨て札へ送る
- その後、新しい加護カードを加護ゾーンに置く

### 置き換え処理

擬似コード：

```python
def play_blessing(player, card):
    old = player.blessing_zone

    if old is not None:
        move_card(old, from_zone="blessing_zone", to_zone="discard")

    move_card(card, from_zone="hand", to_zone="blessing_zone")
    player.blessing_zone = card
```

### 加護カードの除去

現時点では、加護を直接破壊・除去するカードは必須ではない。  
将来的に追加する場合は `target = opponent_blessing_zone` と `effect_type = discard_cards` または `replace_zone_card` で対応する。

---

## 加護効果の適用ルール

### 常時効果

`trigger = passive` かつ `duration = while_in_zone` の効果は、対象カードが `active_zone` に存在する間だけ有効とする。

例：

```text
 trigger = passive
 duration = while_in_zone
 active_zone = blessing_zone
```

### バトル計算時効果

防御+1など、バトル最終値に関わる加護は以下で表す。

```text
trigger = on_battle_calculate
 effect_type = modify_total_stat
 target = self_total
 stat = block
 value = 1
 duration = while_in_zone
 active_zone = blessing_zone
```

### ドロー補正効果

ドロー+1など、通常ドロー枚数に関わる加護は以下で表す。

```text
trigger = passive
 effect_type = modify_rule_value
 target = self_player
 stat = draw_per_turn
 value = 1
 duration = while_in_zone
 active_zone = blessing_zone
```

または、処理都合によって以下でもよい。

```text
trigger = on_draw_step
 effect_type = draw_cards
 target = self_player
 count = 1
 duration = while_in_zone
 active_zone = blessing_zone
```

推奨は `modify_rule_value`。  
理由は、通常ドロー処理に自然に統合できるため。

---

## 加護カード例

### 例1：守りの加護

場にある限り、自分の防御+1。

#### Cards

| id | name | rarity | card_type | attack | block | speed | play_zone | after_play_zone | slot_type | public_text |
|---|---|---|---|---:|---:|---:|---|---|---|---|
| `blessing_guard` | 守りの加護 | rare | blessing | 0 | 0 | 0 | blessing_zone | blessing_zone | blessing | 場にある限り、自分の防御+1。 |

#### CardEffects

| card_id | seq | trigger | effect_type | target | stat | value | duration | active_zone | display_text |
|---|---:|---|---|---|---|---:|---|---|---|
| `blessing_guard` | 1 | on_battle_calculate | modify_total_stat | self_total | block | 1 | while_in_zone | blessing_zone | 場にある限り、自分の防御+1。 |

---

### 例2：知恵の加護

場にある限り、通常ドロー+1。

#### Cards

| id | name | rarity | card_type | attack | block | speed | play_zone | after_play_zone | slot_type | public_text |
|---|---|---|---|---:|---:|---:|---|---|---|---|
| `blessing_draw` | 知恵の加護 | rare | blessing | 0 | 0 | 0 | blessing_zone | blessing_zone | blessing | 場にある限り、通常ドロー+1。 |

#### CardEffects

| card_id | seq | trigger | effect_type | target | stat | value | duration | active_zone | display_text |
|---|---:|---|---|---|---|---:|---|---|---|
| `blessing_draw` | 1 | passive | modify_rule_value | self_player | draw_per_turn | 1 | while_in_zone | blessing_zone | 場にある限り、通常ドロー+1。 |

---

### 例3：刃の加護

場にある限り、自分の攻撃+1。

#### CardEffects

| card_id | seq | trigger | effect_type | target | stat | value | duration | active_zone | display_text |
|---|---:|---|---|---|---|---:|---|---|---|
| `blessing_attack` | 1 | on_battle_calculate | modify_total_stat | self_total | attack | 1 | while_in_zone | blessing_zone | 場にある限り、自分の攻撃+1。 |

---

## ランタイムJSON形式

import/export後、ランタイム側ではカードを以下のように扱う。

```json
{
  "id": "blessing_guard",
  "name": "守りの加護",
  "rarity": "rare",
  "card_type": "blessing",
  "base": {
    "attack": 0,
    "block": 0,
    "speed": 0
  },
  "zones": {
    "play_zone": "blessing_zone",
    "after_play_zone": "blessing_zone",
    "slot_type": "blessing"
  },
  "tags": ["blessing", "defense"],
  "text": "場にある限り、自分の防御+1。",
  "effects": [
    {
      "id": "blessing_guard_01",
      "seq": 1,
      "enabled": true,
      "trigger": "on_battle_calculate",
      "priority": 100,
      "type": "modify_total_stat",
      "target": {
        "side": "self",
        "layer": "total"
      },
      "stat": "block",
      "value": 1,
      "duration": "while_in_zone",
      "active_zone": "blessing_zone",
      "text": "場にある限り、自分の防御+1。"
    }
  ]
}
```

---

## import/export 仕様

### export

NotionまたはCSVから以下を出力する。

- `cards_export.csv`
- `card_effects_export.csv`
- ランタイム用 `cards.json`

### import

既存の import 処理は以下に対応する。

- `Cards` CSV
- `CardEffects` CSV
- 2CSVからランタイムJSONを生成
- `card_id` で効果をカード本体へ紐づける
- `seq` 順に effects 配列を構築する

### バリデーション

import時に最低限以下を検証する。

#### Cards

- `id` が空でない
- `id` が重複していない
- `rarity` が有効値
- `card_type` が有効値
- `attack/block/speed` が数値
- `card_type = blessing` の場合：
  - `play_zone = blessing_zone`
  - `after_play_zone = blessing_zone`
  - `slot_type = blessing`

#### CardEffects

- `card_id` が Cards に存在する
- `trigger` が有効値
- `effect_type` が有効値
- `target` が有効値
- `duration` が有効値
- `active_zone` が有効値または空欄
- `effect_type = modify_total_stat` の場合：
  - `stat` が必須
  - `value` が必須
- `effect_type = modify_rule_value` の場合：
  - `stat` が必須
  - `value` が必須
- `duration = while_in_zone` の場合：
  - `active_zone` が必須

---

## 既存カード移行方針

### 既存バトルカード

既存の攻撃・防御・速度値は `Cards` 側へ残す。

効果があるカードのみ、`CardEffects` に効果行を追加する。

例：トリップワイヤー

```text
card_id = tripwire
trigger = on_reveal
effect_type = modify_total_stat
target = opponent_total
stat = attack
value = -3
duration = current_battle
display_text = 相手の攻撃を-3する。
```

### 既存コントロールカード

即時効果は以下のようにする。

```text
trigger = on_play
duration = instant
```

---

## ログ出力に追加したい項目

加護カード検証用に、以下をログに追加する。

### match_records.jsonl

- `p1_blessing_cards`
- `p2_blessing_cards`
- `p1_active_blessing`
- `p2_active_blessing`
- `blessing_play_count`
- `blessing_replace_count`
- `blessing_used_by_winner`
- `blessing_used_by_loser`

### battle log

各バトル解決時に以下を記録する。

- active blessing
- blessing effect applied
- stat modifiers from blessing
- final attack/block/speed before blessing
- final attack/block/speed after blessing

例：

```json
{
  "battle_index": 1,
  "p1_active_blessing": "blessing_guard",
  "p2_active_blessing": null,
  "modifiers": [
    {
      "source_card": "blessing_guard",
      "source_zone": "blessing_zone",
      "target": "p1_total",
      "stat": "block",
      "value": 1
    }
  ]
}
```

---

## Bot対応

初期実装では、Botの加護カード評価は簡易でよい。

### 推奨ルール

- 加護カードは、手札にあり、現在の加護ゾーンが空なら使用候補に入れる
- 既に加護がある場合、新しい加護の評価値が既存加護より高い場合のみ入れ替える
- ドロー+1系は序盤ほど高評価
- 攻撃+1系はAggro寄りBotで高評価
- 防御+1系はGuard寄りBotで高評価
- 終盤では加護の評価を下げる

### 注意

加護カードはゲームを長期化させる可能性がある。  
現時点では、加護カードの強さや枚数を増やしすぎないこと。

---

## ゲームデザイン上の注意

このゲームは一撃決闘を中心にしている。  
そのため、加護カードのようなセットアップ系カードは増やしすぎるとゲーム性が変わる。

加護カードは主軸ではなく、以下のような役割に抑える。

- デッキ方針を少し補強する
- 相手に見える脅威を作る
- 中長期戦になった時の差を作る
- ドローや防御などの軽い継続効果を与える

避けたい方向：

- 加護を置かないと勝てない
- 加護の入れ替えが主ゲームになる
- ライフ制ゲームのように長期戦前提になる
- 一撃決闘の緊張感が薄れる

---

## 今回の実装スコープ

今回実装するもの：

- `Cards` / `CardEffects` 分離に対応
- `card_type = blessing` 追加
- `blessing_zone` 追加
- 各プレイヤーの加護ゾーン1枚制限
- 加護カード使用時の置き換え処理
- `duration = while_in_zone`
- `active_zone = blessing_zone`
- `passive` / `on_battle_calculate` / `on_draw_step` / `modify_rule_value` の土台
- import/exportの対応
- 最小限のログ出力

今回必須ではないもの：

- 加護破壊カード
- 複数加護スロット
- 加護コピー
- 加護レベルアップ
- 加護専用UIの作り込み
- 複雑な条件付き加護

---

## 実装順序

推奨実装順：

1. `Cards` / `CardEffects` の2CSV対応
2. import/export の更新
3. ランタイムJSON生成処理の更新
4. `card_type` / `play_zone` / `after_play_zone` / `slot_type` の導入
5. `blessing_zone` をプレイヤー状態に追加
6. 加護カード使用処理を追加
7. `duration = while_in_zone` と `active_zone` の評価処理を追加
8. `modify_total_stat` を加護から適用できるようにする
9. `modify_rule_value` を加護から適用できるようにする
10. ログ出力追加
11. 簡単な加護カードを2〜3枚追加してテスト

---

## 最小テストカード

最初は以下の3枚だけでよい。

### 守りの加護

```text
場にある限り、自分の防御+1。
```

### 刃の加護

```text
場にある限り、自分の攻撃+1。
```

### 知恵の加護

```text
場にある限り、通常ドロー+1。
```

---

## テスト項目

### import/export

- Cards CSV と CardEffects CSV から JSON が生成できる
- 1枚のカードに複数効果を紐づけられる
- 無効な `card_id` を検出できる
- `duration = while_in_zone` で `active_zone` 未設定ならエラーにできる

### 加護ゾーン

- 加護カードを使用すると blessing_zone に置かれる
- 使用後に捨て札へ行かない
- 2枚目の加護を使うと1枚目が捨て札へ行く
- 各プレイヤーが別々に加護を保持できる

### 加護効果

- 防御+1がバトル計算に反映される
- 攻撃+1がバトル計算に反映される
- ドロー+1が通常ドローに反映される
- 加護が捨て札へ移動したら効果が消える

### ログ

- 加護カードの使用回数が記録される
- 加護カードの置き換え回数が記録される
- バトル時に加護効果が適用されたことが記録される

---

## Codexへの要約指示

以下の方針で実装してください。

```text
Cards と CardEffects を分離し、1カード複数効果を扱えるようにしてください。

Cards にはカード本体情報を置き、CardEffects には効果を1行1効果で置きます。

新しく card_type = blessing を追加します。
blessing カードは使用すると blessing_zone に置かれ、捨て札へ行かず、場にある限り効果を発揮します。

各プレイヤーの blessing_zone は1枚制限です。
新しい blessing を置く場合、既存の blessing は捨て札へ送ってから新しい blessing を置いてください。

CardEffects には trigger / effect_type / target / stat / value / duration / active_zone を持たせてください。
duration = while_in_zone と active_zone = blessing_zone によって、加護ゾーンにある間だけ効果が有効になるようにします。

まずは以下の効果に対応してください。

- modify_total_stat
- modify_rule_value
- draw_cards

加護カードの最小テストとして、以下を実装できるようにしてください。

- 場にある限り攻撃+1
- 場にある限り防御+1
- 場にある限り通常ドロー+1

import/export は Cards CSV と CardEffects CSV の2ファイルに対応してください。
既存カードの挙動を壊さないようにしてください。
ログには加護カードの使用、置き換え、効果適用を記録してください。
```

---

## 補足

加護カードはゲームの戦略を広げるが、増やしすぎると一撃決闘の緊張感を弱める可能性がある。

そのため、今回の目的は「加護を主軸にする」ことではなく、将来的な拡張に耐えるスキーマと最低限の実装を用意することである。
