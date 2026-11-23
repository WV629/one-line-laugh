#!/usr/bin/env python3
"""The One-Line Laugh — make.fun entry.

Writes one funny line (a single sentence, at most 200 characters) to
/output/entry.txt, where the house judge reads it.

The line: a setup with a relatable everyday truth (the smart speaker, the
pile of unread emails) and a surprise at the very end — the "relaxing"
thing the speaker picks is the least relaxing thing it could do.
"""

import os

LINE = (
    "I asked my smart speaker to play something relaxing, "
    "and it started reading my unread emails out loud."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
