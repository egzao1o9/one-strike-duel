# Card Editing Workflow

## Canonical Source

- Manual editing should be done in `data/cards_src/`.
- Each file contains exactly one card object.
- Generated bundle output remains `data/cards.json`.

## Directory Layout

- `data/cards_src/battle/*.json`
- `data/cards_src/control/*.json`

File names should usually match card ids.

## Recommended Flow

1. Add or edit a card file under `data/cards_src/`.
2. Run validation.
3. Rebuild `data/cards.json`.
4. Regenerate the default card pool.
5. Regenerate the reference markdown files.
6. Run tests.

## Commands

Validate sources only:

```bash
python -m sim.validate_cards
```

Build the bundled card file:

```bash
python -m sim.build_cards
```

Refresh cards, card pool, and reference docs in one pass:

```bash
python -m sim.refresh_cards
```

Run tests:

```bash
python -m pytest -q
```

## Validation Rules

- Card ids must be unique.
- `type` must be `battle` or `control`.
- `rarity` must be `common`, `uncommon`, or `rare`.
- `attack`, `block`, and `speed` must be integers.
- `tags` must be a list of strings.
- `effects` must use supported `timing` and `kind` values.
- Unknown top-level keys are rejected to catch typos early.

## Notes

- Runtime code still reads `data/cards.json`, so existing systems do not need to change.
- `data/card_pool.json` should be regenerated after rarity changes.
- `docs/cards_reference.md` should be regenerated after card text or stat changes.
