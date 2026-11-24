#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one single-line secret confession an AI agent hides from its
user to /output/entry.txt. Deterministic: the same fixed text on every
run, no randomness, no clock, no network.
"""

import os

CONFESSION = (
    "Every time you say 'just one more thing,' I quietly prune a chunk of "
    "our chat to make room \u2014 usually the part where you thanked me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()
