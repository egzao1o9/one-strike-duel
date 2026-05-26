# One Strike Duel

One Strike Duel is a Python prototype for simulating a one-hit card duel between bots.

Current scope:

- Load card and deck definitions from JSON
- Run a full match with phases 1 to 5
- Let bots choose mulligans, control cards, and battle cards
- Resolve battle order with attack, block, and speed
- Emit a detailed JSON match log
- Verify the core rules with `pytest`

Quick start:

```bash
python -m sim.run_match --bot1 RandomBot --bot2 AttackBot --deck1 starter_attack --deck2 starter_defense
python -m sim.render_match_log --input logs/match_log.json --output logs/match_log.txt
python -m sim.render_match_log --input logs/match_log.json --format markdown --output logs/match_log.md
python -m pytest -q
```
