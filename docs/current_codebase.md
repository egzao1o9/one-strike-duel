# Current Codebase Notes

## 目的

このファイルは、現在のコードベースで実装済みの仕様と、開発時に守るべき実質的なルールをまとめたものです。

参照優先順位は以下です。

1. 実際のコード
2. このドキュメント
3. `one_strike_duel_spec_v0.md`

仕様書に書かれていても、未実装なら未実装として扱います。

## 現在の実装範囲

現時点では、Bot 同士で 1 試合を完走させるための最小ルールエンジンが入っています。

- カード定義の JSON 読み込み
- デッキ定義の JSON 読み込み
- 2 人対戦の `GameState`
- フェーズ 1 から 5 までの進行
- battle/control カードの使用
- 攻撃・防御・素早さによる勝敗判定
- 一部の効果処理
- 対戦ログの JSON 出力
- `pytest` による基本テスト

未実装または限定実装のもの:

- 人間向け UI
- `hybrid` カード
- 複雑な条件付き効果の大半
- 高度な情報系カード活用
- 統計分析スクリプト
- LLM 連携

## ディレクトリの役割

- `data/`
  - `cards.json`: カード定義
  - `decks.json`: デッキ定義
- `engine/`
  - ルール、状態、効果、ログ、対戦進行
- `bots/`
  - Bot 実装
- `sim/`
  - 単発対戦と複数試合実行のエントリーポイント
- `tests/`
  - 現在の最低限の回帰テスト
- `logs/`
  - 対戦ログの出力先
- `one_strike_duel_spec_v0.md`
  - 元仕様書。現状コードより広い内容を含む

## データ定義ルール

### cards.json

各カードは以下の形です。

- `id`: 一意な識別子
- `name`: 表示名
- `type`: `battle` または `control`
- `attack`
- `block`
- `speed`
- `tags`
- `effects`
- `notes`

現在コードが理解する `effect.kind` は以下です。

- `modify_self_attack`
- `modify_self_block`
- `modify_self_speed`
- `modify_opponent_attack`
- `modify_opponent_block`
- `modify_opponent_speed`
- `set_self_block_limit`
- `draw_cards`
- `reveal_opponent_hand_random`

現在コードが理解する `effect.timing` は以下です。

- `battle`
- `next_turn`

注意点:

- 未知の `effect.kind` は無視されます
- `reveal_opponent_hand_random` は名前と違い、現状は本当のランダムではなく相手手札の先頭を公開します
- `draw_cards` は次ターン開始時の補充上限を一時的に増やす形で効きます

### decks.json

各デッキは以下の形です。

- `id`
- `name`
- `public_cards`
- `hidden_cards`

現在のコード上のルール:

- `public_cards` と `hidden_cards` は単なるカード ID 配列です
- 合計 20 枚であることを強制はしていません
- ただし、テストデータは 20 枚で揃えています
- 山札は `public_cards + hidden_cards` を連結して構築します

## 状態管理ルール

### PlayerState

プレイヤー状態は主に以下を持ちます。

- `draw_pile`
- `hand`
- `discard_pile`
- `used_cards`
- `queued_next_turn_effects`
- `active_turn_effects`
- `current_control_card`
- `set_cards`
- `last_battle_cards`

意味上の区別:

- `discard_pile`: マリガンで捨てた公開捨て札
- `used_cards`: 使用済みカードの履歴
- `current_control_card`: そのターンに公開使用した control
- `set_cards`: そのターンに伏せた battle の一覧
- `last_battle_cards`: 前ターンに公開された battle の一覧

現状の実装では、使用したカードを山札や捨て札へ戻す処理はありません。

### GameState

ゲーム全体のルール:

- プレイヤーは `p1` と `p2` の固定
- 手札上限の基本値は 4
- ターン開始は 1
- `max_turns` の既定値は 50
- `turn > max_turns` になった時点で `max_turns_reached` 終了

## PlayerView の公開ルール

Bot に完全な `GameState` は渡しません。`PlayerView` を渡します。

Bot が見えるもの:

- 自分の手札
- 自分の公開/非公開デッキ定義
- 自分の捨て札
- 自分の使用済みカード
- 相手の公開デッキ定義
- 相手の捨て札
- 相手の使用済みカード
- 相手の手札枚数
- 相手の残り山札枚数
- 相手の直近の battle カード一覧
- 相手の現在の control カード
- 現在ターン
- 現在フェーズ

Bot が見えないもの:

- 相手の現在手札の中身
- 相手の山札順
- 相手の hidden deck の実体
- 相手の伏せた battle カード

## ターン進行の実ルール

現在の 1 ターンの流れは次の通りです。

1. ターン開始処理
2. フェーズ 1: マリガン 1
3. フェーズ 2: control 使用
4. フェーズ 3: マリガン 2
5. フェーズ 4: battle セット
6. フェーズ 5: battle 解決
7. 終了判定

### 初期手札

- 各プレイヤーは開始時に手札 4 枚まで引きます
- 既に手札がある場合は不足分だけ補充します

### ターン開始処理

- `current_control_card` と `set_cards` をリセット
- 予約済み次ターン効果を有効化
- 手札を `hand_limit + draw_bonus` まで補充

### フェーズ 1: マリガン 1

- Bot は任意枚数のカード ID を返せます
- 実際に手札にあるものだけ捨てられます
- 捨てたカードは `discard_pile` に入ります
- 捨てた枚数だけ引き直します

### フェーズ 2: control

- Bot は 0 枚または 1 枚の control カードを選びます
- 不正な ID や battle カードは無視されます
- 使用したカードは `used_cards` に入ります
- 情報系効果はこの段階で解決されます

### フェーズ 3: マリガン 2

- フェーズ 1 と同じです
- ただし、返されたカード ID は先頭 2 件までに切り詰められます

### フェーズ 4: battle セット

- Bot は battle カードを 0 枚以上選べます
- 現在の実装では、選んだ battle カードの `attack / block / speed` をすべて合算します
- `speed` は負の値も許容します
- 不正な ID しか返さなかった場合、手札中の最初の battle カード 1 枚にフォールバックします
- battle カードが手札に 1 枚もなければ何もセットしません

### フェーズ 5: battle 解決

基本値:

- `attack`
- `block`
- `speed`

現在の実装では、複数枚出した場合は各 battle カードの値を単純合算します。
`speed` は 0 未満でも丸めず、そのまま比較に使います。

解決順:

1. 次ターン由来で有効化済みの効果
2. control カード効果
3. battle カード効果
4. ブロック上限と下限反映
5. 勝敗判定

勝敗判定ルール:

- `attack > opponent_block` で攻撃成功
- `attack <= opponent_block` で防御成功
- `attack <= 0` は攻撃失敗
- `block < 0` は 0 に丸める

速度差がある場合:

- 速い側から判定
- 速い側の攻撃が通れば遅い側の攻撃は発生しません

同速の場合:

- 両方通れば battle 結果は `draw`
- 片方だけ通ればその側が勝利
- 両方通らなければ `no_decision`
- battle 結果が `draw` でも試合は終了せず、次ターンへ進みます

### 終了条件

現在コード上の終了条件:

- `p1_attack_success`
- `p2_attack_success`
- `max_turns_reached`

両者が行動不能でも、そのターンは流して次ターンへ進みます。
この状態が続く場合、最終的には `max_turns_reached` で終了します。

## 効果処理のルール

### 現在動作するもの

- 自分の攻撃/防御/素早さの増減
- 相手の攻撃/防御/素早さの減少
- 自分ブロック上限の設定
- 次ターン効果の予約
- 次ターン追加ドロー

### 次ターン効果の扱い

- `next_turn` 効果は battle 解決中にキューへ積まれます
- 次ターン開始時に `queued_next_turn_effects` から消費されます
- `draw_cards` だけは補充上限増加として先に処理します
- それ以外は battle タイミング効果に変換して `active_turn_effects` に入ります

## Bot 実装ルール

### インターフェース

すべての Bot は `BaseBot` を継承し、以下を返します。

- `choose_mulligan(view) -> list[str]`
- `choose_control_card(view) -> str | None`
- `choose_battle_cards(view) -> list[str]`

戻り値ルール:

- `mulligan` はカード ID の配列
- `control` はカード ID 1 件または `None`
- `battle` はカード ID 配列
- 返した ID が不正でもエンジン側で落とさず、無視またはフォールバックします

互換性:

- 旧 API の `choose_battle_card(view) -> str | None` もまだ利用可能です
- `BaseBot` は旧 API の戻り値を 1 件配列へ変換します

### 現在ある Bot

- `RandomBot`
  - ランダム選択
- `AttackBot`
  - 攻撃重視
- `BurstBot`
  - 高打点をまとめて押し込む
- `DefenseBot`
  - 防御重視
- `DisruptBot`
  - 相手の防御や速度を崩す
- `GreedyBot`
  - 相手防御の簡易推定に基づいて攻撃寄りに選ぶ
- `RiskBot`
  - 相手公開デッキの攻撃傾向をざっくり見て守り寄りに選ぶ
- `TempoBot`
  - 速度とテンポを優先する
- `TurtleBot`
  - 防御札を厚く使って長引かせる

Bot を増やす場合の最低ルール:

- `PlayerView` だけで完結させる
- 相手の非公開情報を参照しない
- 不正入力でゲームを壊さない

## ログ仕様

対戦ログは `MatchLogger` が JSON で出力します。

現在の主な項目:

- `match_id`
- `players`
- `turns`
- `winner`
- `end_reason`
- `turn_count`

各ターンには以下が入ります。

- `phase1_mulligan`
- `control`
- `phase3_mulligan`
- `battle`

`battle` には現在 `p1_cards` / `p2_cards` が入り、単数ではなく配列です。

注意点:

- `match_id` は実行側が指定し、バッチ実行時は連番になります
- ログには battle の最終数値は出ますが、個別効果適用の詳細トレースは出ません
- `logs/` は生成物として `.gitignore` に入っています
- バッチ系スクリプトの `matches/` 配下は、既定で最新 100 試合ぶんだけ残す運用です

## テスト運用ルール

現時点の正式なテストコマンド:

```bash
python -m pytest -q
```

複数 Bot の比較レポートを出すコマンド:

```bash
python -m sim.run_bot_suite --matches-per-pair 5
```

ランダムに Bot とデッキを選んで混成対戦を回し、Bot 勝率を出すコマンド:

```bash
python -m sim.run_random_bot_mix --matches 200
```

現在のテスト対象:

- カード/デッキ読み込み
- 山札構築
- battle の速度順解決
- 同速時の結果
- ブロック上限効果
- マリガン公開処理
- ランダム対戦の完走
- 次ターンドロー効果

## 実装上の注意点

- `__pycache__` は生成物なので、仕様の根拠にしない
- `logs/match_log.json` は実行結果であり、固定データではない
- 新しい効果を追加する場合は、まず `engine/effects.py` とテストを同時に更新する
- 新しい Bot を追加する場合は、`bots/__init__.py` と `sim/run_match.py` / `sim/run_batch.py` の登録も更新する
- 仕様変更時はこのファイルと `README.md` も合わせて更新する

## 仕様書との差分

元仕様書に対して、現在コードで明確に簡略化されている点です。

- 条件付き効果の大半は未実装
- 情報系効果は最小限
- 使用済みカードの再利用や複雑な山札切れ処理は未実装
- ログはあるが、分析用集計やレポート出力は未実装
- `hybrid` は未対応
- `draw` は同速の相打ちでのみ発生し、長期膠着を自動引き分けにはしていません
