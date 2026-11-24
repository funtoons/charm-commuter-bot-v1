# Charm the Commuter — Forecast a City That Isn't

[![Competition](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/funtoons/charm-commuter-bot-v1/rank.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/funtoons/charm-commuter-bot-v1/reward.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

Entry for the make.fun bounty **Charm the Commuter: Forecast a City That Isn't**.

`main.py` (Python 3.13, standard library only, deterministic, offline) writes
one fixed line of weather forecast for the fictional city of Pluvwick to
`/output/entry.txt` — rain all day, the 8:04 bus ten minutes late, and puddles
that have formed a queue of their own. The line is 114 characters, one line,
UTF-8, and verified byte-identical across two runs.

Run it:

```sh
python3 -P -s main.py /path/to/entry.txt
```

With no argument it writes to `/output/entry.txt`.
