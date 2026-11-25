#!/usr/bin/env python3
"""Write the funniest one-line out-of-office reply to /output/entry.txt.

Deterministic, standard library only. No network, no randomness, no
input files: the reply is a constant, so every run produces the exact
same output.
"""

import os

REPLY = (
    "I'm out of the office \u2014 my cat is covering my inbox. "
    "She has already deleted everything and feels no remorse."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
