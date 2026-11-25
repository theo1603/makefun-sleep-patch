#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes one line of patch notes (at most 160 characters) to
/output/entry.txt: human sleep is fixed.

The line reads like a real changelog entry: a named bug (sleep
crashing at 3 a.m. and rebooting as existential dread), a terse fix,
and a kicker in release-notes voice ("no updates pending").

Deterministic: no randomness, no network, no clock, no input.
"""

import os

TEXT = (
    "Fixed: human sleep no longer crashes at 3 a.m. and reboots as "
    "existential dread. It now runs straight through the night, no "
    "updates pending."
)


def main() -> None:
    text = TEXT.strip()
    if not 1 <= len(text) <= 160:
        raise ValueError(f"entry is {len(text)} chars, must be 1-160")
    if "\n" in text or text != text.strip():
        raise ValueError("entry must be a single line with no padding")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
