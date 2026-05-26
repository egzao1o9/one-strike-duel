# cards_src

- Edit cards here, not in `data/cards.json`.
- Use one file per card.
- Keep file names aligned with card ids when possible.

Typical workflow:

```bash
python -m sim.validate_cards
python -m sim.refresh_cards
python -m pytest -q
```
