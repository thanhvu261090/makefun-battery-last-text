#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes one line (at most 200 characters) -- the phone battery's final
text message to the charger it waited for all day -- to /output/entry.txt.

Deterministic: the entry is a fixed string; every run writes byte-identical
output.
"""

import os
import sys

ENTRY = (
    "hey it's me, 1%. i waited all day while you charged your vape, "
    "your watch, your toothbrush. plug me in, say sorry, and don't "
    "unplug me at 80% to 'save my health.'"
)

MAX_CHARS = 200


def gate_check(text: str) -> None:
    """Enforce the competition gate: 1-200 chars, single line, no
    leading/trailing whitespace, non-blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> int:
    gate_check(ENTRY)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    # Write exactly the line, no trailing newline, so the gated file is
    # byte-identical to ENTRY.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
