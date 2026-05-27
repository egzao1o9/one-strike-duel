# Notionカード運用

## 考え方

Notion は編集・並び替え・レビューのために使い、ゲーム実行時の真のソースはリポジトリ側に置きます。

- 実行時の基点: `data/cards_src/`
- Notion は一括編集用
- 受け渡しはCSV

## 推奨テーブル

Notion では 2 テーブル運用を推奨します。

1. `Cards`
2. `CardEffects`

理由:

- 1枚のカードが複数効果を持てる
- 効果を1行1効果で管理できる
- 数値調整や並べ替えがしやすい

## `Cards` テーブルの主な列

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

- `tags` はカンマ区切り
- `card_type` は `battle / control / blessing`

## `CardEffects` テーブルの主な列

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
- `notes`

## Repo → Notion

現在のカード定義をCSVへ書き出します。

```bash
python -m sim.export_cards_csv
```

出力:

- `data/cards_export.csv`
- `data/card_effects_export.csv`

この2つを Notion へ取り込みます。

## Notion → Repo

1. Notion から `Cards` と `CardEffects` をそれぞれCSVで書き出す
2. ローカルへ保存する
3. 取り込む

```bash
python -m sim.import_cards_csv --cards-input data/cards_export.csv --effects-input data/card_effects_export.csv
python -m sim.refresh_cards
python -m pytest -q
```

## 利点

- API認証なしで運用できる
- 数値調整がかなりやりやすい
- 効果を構造化して扱える
- Blessing のような新カード種別にも対応しやすい

## 注意点

- Notion 側で列名を変えすぎると import が壊れます
- `CardEffects` の `card_id` は必ず `Cards.id` と一致させてください
- `duration = while_in_zone` の場合は `active_zone` が必須です
