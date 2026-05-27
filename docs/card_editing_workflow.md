# カード編集フロー

## 基本方針

- 手動編集の基点は `data/cards_src/`
- 1ファイル1カード
- ランタイムは `data/cards.json` を読む
- Notion とのやり取りは `Cards` / `CardEffects` の2CSVで行う

## ディレクトリ構成

- `data/cards_src/battle/*.json`
- `data/cards_src/control/*.json`
- `data/cards_src/blessing/*.json`

通常はファイル名をカードIDに合わせます。

## 推奨フロー

1. `data/cards_src/` のカードJSONを追加・修正する
2. 検証する
3. `data/cards.json` を再生成する
4. `data/card_pool.json` を再生成する
5. 参照Markdownを再生成する
6. テストを回す

## コマンド
### 検証

```bash
python -m sim.validate_cards
```

### ランタイムJSON再生成

```bash
python -m sim.build_cards
```

### まとめて更新

```bash
python -m sim.refresh_cards
```

### Notion向けCSV書き出し

```bash
python -m sim.export_cards_csv
```

出力されるファイル:

- `data/cards_export.csv`
- `data/card_effects_export.csv`

### 編集済みCSVの取り込み

```bash
python -m sim.import_cards_csv --cards-input data/cards_export.csv --effects-input data/card_effects_export.csv
```

### テスト

```bash
python -m pytest -q
```

## バリデーションの主な内容

- カードIDの重複がないこと
- `card_type` が `battle / control / blessing` のいずれかであること
- `rarity` が `common / uncommon / rare` のいずれかであること
- `attack / block / speed` が整数であること
- `tags` が文字列配列であること
- `CardEffects` が有効な `trigger / effect_type / target` を持つこと
- `duration = while_in_zone` のとき `active_zone` があること
- `blessing` のとき
  - `play_zone = blessing_zone`
  - `after_play_zone = blessing_zone`
  - `slot_type = blessing`

## メモ

- `tags` はCSVではカンマ区切りです
- 新方式の効果定義は `CardEffects` 側が基準です
- 旧 `timing / kind / value` も互換のためまだ読めます
- 詳しいコマンドは [command_reference.md](/h:/Github/one-strike-duel/docs/command_reference.md) を参照してください
