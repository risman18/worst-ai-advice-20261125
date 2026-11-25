#!/usr/bin/env python3
"""Worst AI Advice entry: writes one line of deliberately terrible advice
to /output/entry.txt. Deterministic, no network, no randomness."""

import os

LINE = (
    "Your smoke alarm keeps beeping at night? Just remove the battery \u2014 "
    "a quiet house sleeps better, and fires are rare anyway."
)

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
