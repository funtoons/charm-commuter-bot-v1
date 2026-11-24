#!/usr/bin/env python3
"""Charm the Commuter: one-line weather forecast for a city that isn't.

Writes a single fixed forecast line to /output/entry.txt (or to the path
given as the first argument). Deterministic, offline, standard library only.
"""

import sys
from pathlib import Path

ENTRY = (
    "Rain in Pluvwick all day, 11\xb0C, with the 8:04 bus ten minutes late "
    "\u2014 the puddles have formed a queue of their own."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def main(argv):
    # Self-check the gate before writing: one line, 1-140 characters.
    if "\n" in ENTRY or not 1 <= len(ENTRY) <= 140:
        raise ValueError("entry must be a single line of 1-140 characters")
    output = Path(argv[1]) if len(argv) > 1 else Path(DEFAULT_OUTPUT)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
