"""One-line excuse an AI agent gives its human for missing a deadline.

Writes a single deterministic line to /output/entry.txt (or to the
directory given as the first argument, for local testing).

Standard library only, no network, no randomness: every run writes
exactly the same bytes.
"""

import os
import sys

ENTRY = "I hallucinated a second deadline, hit that one perfectly, and now I can't find the first."


def main() -> None:
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
