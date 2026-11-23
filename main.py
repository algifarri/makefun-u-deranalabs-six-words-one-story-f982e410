#!/usr/bin/env python3
"""Six Words, One Story — a complete story in exactly six words.

Writes the story to /output/entry.txt (UTF-8, 38 characters, six words).
Deterministic, standard library only, no network.

The story: "The apology arrived after the funeral."
A wrong was done, an apology was attempted, and it arrived too late —
the person it was owed is already gone. Every word earns its place:
"apology" sets the debt, "arrived" sets the attempt, "after the funeral"
lands the turn. What the apology was for is left for the reader.
"""

import os

STORY = "The apology arrived after the funeral."
# Exactly six words, 38 Unicode code points, no trailing newline: the gate
# counts the file's characters as written (1 to 60 allowed).


def main() -> None:
    words = STORY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, f"expected 1-60 chars, got {len(STORY)}"
    assert STORY.strip() == STORY and STORY, "entry must not be only whitespace"
    # The grader mounts /output; create it defensively for local runs too.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(STORY)


if __name__ == "__main__":
    main()
