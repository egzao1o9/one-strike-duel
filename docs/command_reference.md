# コマンド一覧

このリポジトリで日常的に使うコマンドを、日本語でまとめています。  
特にカード編集まわりは、`Cards` と `CardEffects` の2CSVを前提にしています。

## カード管理
### カード定義を検証する

`data/cards_src/` のJSON定義を検証します。

```bash
python -m sim.validate_cards
```

### ランタイム用 `data/cards.json` を再生成する

```bash
python -m sim.build_cards
```

### カード関連生成物をまとめて更新する

以下をまとめて実行します。

- カード定義の検証
- `data/cards.json` の再生成
- `data/card_pool.json` の再生成
- 参照Markdownの再生成

```bash
python -m sim.refresh_cards
```

## CSVエクスポート / インポート
### Cards / CardEffects をCSVへ書き出す

Notion 編集用に、2つのCSVを書き出します。

- `data/cards_export.csv`
- `data/card_effects_export.csv`

```bash
python -m sim.export_cards_csv
```

出力先を変える場合:

```bash
python -m sim.export_cards_csv --cards-output data/cards_export.csv --effects-output data/card_effects_export.csv
```

### 編集済みCSVを取り込む

`Cards` CSV と `CardEffects` CSV を `data/cards_src/` に戻し、必要なら `data/cards.json` も再生成します。

```bash
python -m sim.import_cards_csv --cards-input data/cards_export.csv --effects-input data/card_effects_export.csv
```

別パスから取り込む場合:

```bash
python -m sim.import_cards_csv --cards-input path/to/cards.csv --effects-input path/to/card_effects.csv --source-dir data/cards_src --bundle-output data/cards.json
```

## CSV列の考え方
### Cards CSV

主な列:

- `id`
- `name`
- `rarity`
- `card_type`
- `attack`
- `block`
- `speed`
- `tags`
- `public_text`
- `enabled`
- `play_zone`
- `after_play_zone`
- `slot_type`
- `flavor_text`
- `notes`

補足:

- `tags` は **カンマ区切り** です
- `card_type` は `battle / control / blessing`

### CardEffects CSV

主な列:

- `id`
- `card_id`
- `seq`
- `enabled`
- `trigger`
- `priority`
- `effect_type`
- `target`
- `stat`
- `value`
- `value2`
- `count`
- `duration`
- `active_zone`
- `condition`
- `keyword`
- `display_text`
- `params_json`
- `timing`
- `kind`
- `notes`

補足:

- 新方式では `trigger / effect_type / target / stat / value ...` を使います
- `timing / kind` は既存カード互換のための旧列です

## 参照ドキュメント生成
### カード / デッキ / プールのMarkdownを更新する

```bash
python -m sim.render_reference_docs
```

生成先:

- `docs/cards_reference.md`
- `docs/decks_reference.md`
- `docs/card_pool_reference.md`

## 単発対戦
### 固定デッキ対戦

```bash
python -m sim.run_match --bot1 RandomBot --bot2 RandomBot --deck1 starter_attack --deck2 starter_defense
```

### ドラフト対戦

```bash
python -m sim.run_draft_match --draft-bot1 StandardDraftBot --draft-bot2 GuardDraftBot --bot1 StandardBot --bot2 StandardBot
```

## レポート生成
### ドラフトレポート

```bash
python -m sim.run_draft_report --draft-bot1 StandardDraftBot --draft-bot2 GuardDraftBot --bot1 StandardBot --bot2 StandardBot --rounds 50
```

よく使うオプション:

- `--draft-mode full`
  - フルドラフトを使う
- `--draft-mode simple`
  - 軽量な簡易ドラフトを使う
- `--fast-report`
  - 試合ごとの重い保存を減らして高速化する
- `--lean-draft-logging`
  - ドラフト候補やピック履歴の保存を軽量化する
- `--save-battle-logs`
  - 戦闘ログだけを保存する
- `--keep-match-logs 100`
  - 詳細ログの保持件数を制限する

### ドラフトBot総当たり

```bash
python -m sim.run_draft_bot_suite --matches-per-matchup 1000 --draft-mode full --fast-report --lean-draft-logging --save-battle-logs --workers 0
```

補足:

- `--workers 0` は自動設定です
- 現在は matchup 内 chunk 並列も入っているので、かなり高速です
- `--save-battle-logs` を付けると、ドラフト履歴は省きつつ戦闘ログだけ残せます

## テスト
### 全テスト

```bash
python -m pytest -q
```

### カードCSVまわりだけ

```bash
python -m pytest tests/test_card_csv.py -q
```
