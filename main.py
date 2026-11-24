"""One Word for Your Wi-Fi — make.fun bounty entry.

Deterministic, no network, no randomness, no LLM calls.
Writes the single-word entry to <ENTRY_OUTPUT_DIR>/entry.txt
(default /output) and validates it with a self-check gate.
"""

import os
import sys

ENTRY = "Limbo"


def validate(word: str) -> None:
    """Self-check gate: exactly one word, 1-30 chars, no spaces/punctuation."""
    assert isinstance(word, str), "entry must be a string"
    assert word.strip() != "", "entry must not be blank"
    assert word == word.strip(), "entry must not have leading/trailing whitespace"
    assert " " not in word, "entry must be a single word (no spaces)"
    assert len(word.split()) == 1, "entry must be exactly one token"
    assert 1 <= len(word) <= 30, "entry must be 1-30 characters"
    assert word.isalnum(), "entry must be a single alphanumeric token (no punctuation)"


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
