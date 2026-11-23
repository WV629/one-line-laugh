#!/usr/bin/env python3
"""The One-Line Laugh — make.fun entry.

Writes one funny line (a single sentence, at most 200 characters) to
/output/entry.txt, where the house judge reads it.

The line: a setup with a relatable everyday truth (the smart speaker, the
pile of unread emails) and a surprise at the very end — the "relaxing"
thing the speaker picks is the least relaxing thing it could do.
"""

import os
import re

LINE = (
    "I asked my smart speaker to play something relaxing, "
    "and it started reading my unread emails out loud."
)


def validate(line: str) -> None:
    """The gate only accepts UTF-8 text of 1-200 chars, not only whitespace,
    and the judge only scores a single sentence: enforce both here so a
    bad line can never reach /output/entry.txt."""
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    assert line.strip(), "line must not be only whitespace"
    # One sentence: exactly one sentence-ending mark, at the very end.
    assert len(re.findall(r"[.!?]", line)) == 1 and line.endswith("."), (
        "line must be a single sentence ending in a period"
    )


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)  # no trailing newline: the gate counts every character


if __name__ == "__main__":
    main()
