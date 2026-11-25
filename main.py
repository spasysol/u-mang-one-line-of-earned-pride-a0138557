#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes one line (1-240 characters) to /output/entry.txt: a quiet,
earned moment of pride for someone in a scene. Pure standard library.
"""

import os

ENTRY = "She had failed the driving test four times; on the fifth, she parked perfectly, turned the engine off, and sat there smiling at nothing."

MAX_CHARS = 240


def main():
    # Fail loudly instead of submitting a gate-violating entry.
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY:
        raise SystemExit("entry must be a single line with no surrounding whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
