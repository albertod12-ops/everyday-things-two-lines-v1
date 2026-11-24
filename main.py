#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the two-line entry to /output/entry.txt.

Line 1 explains an escalator to a 10-year-old through one concrete
analogy (a staircase that does the walking). Line 2 says honestly what
the analogy maps and what it leaves out.
"""
import os

ENTRY = (
    "An escalator is a staircase that decided to do the walking for you, "
    "carrying your feet upward while you just stand still and ride along.\n"
    "It maps the steps and the climb, but leaves out that you still have "
    "to step on and off by yourself, and that it can only travel straight "
    "up or straight down."
)

os.umask(0o022)


def main():
    assert 1 <= len(ENTRY) <= 400, len(ENTRY)
    lines = ENTRY.split("\n")
    assert len(lines) == 2, len(lines)
    assert all(line.strip() for line in lines)
    # Each line must be exactly one sentence: no second sentence hiding
    # behind an extra full stop mid-line.
    assert all(line.rstrip().endswith(".") and line.count(".") == 1
               for line in lines)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
