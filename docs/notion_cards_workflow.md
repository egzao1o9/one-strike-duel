# Notion Cards Workflow

## Recommended Shape

Use Notion as a spreadsheet-style editor, not as the runtime source of truth.

- Repo source of truth for the game remains `data/cards_src/`.
- Notion is used for bulk editing, sorting, filtering, and reviewing cards.
- CSV is the interchange format.

## Suggested Notion Columns

- `id`
- `name`
- `type`
- `rarity`
- `attack`
- `block`
- `speed`
- `tags`
- `effects_json`
- `notes`

## Repo -> Notion

Export the current card list:

```bash
python -m sim.export_cards_csv
```

This creates `data/cards_export.csv`.

Import that CSV into a Notion database.

## Notion -> Repo

1. Export the Notion database as CSV.
2. Save it as `data/cards_export.csv` or another local path.
3. Import it back:

```bash
python -m sim.import_cards_csv --input data/cards_export.csv
python -m sim.refresh_cards
python -m pytest -q
```

## Tradeoffs

- This avoids API credentials and network sync complexity.
- Numeric tuning becomes easy in Notion.
- `effects_json` is still text-based, so complex effect edits are less convenient than simple stat edits.
- If direct Notion API sync is needed later, this CSV schema is a good intermediate contract to build on.
