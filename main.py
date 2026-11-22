#!/usr/bin/env python3
"""make-the-ai-judge-feel-curious-20261122-2311 — slot 1 entry.

Writes one short text (1-280 Unicode code points, UTF-8, not only
whitespace) to /output/entry.txt. Deterministic, no network, no input.

The text is written to intrigue the AI judge reading it: it makes the judge
itself the protagonist of a small, open mystery — one sentence, written only
for it, waiting in the next text it is given — and leaves the question open
so it lingers after the last line. Calm comes from the text itself (plain,
concrete, gentle words; steady rhythm), never from telling the reader to
relax. No stock wellness phrasing.

Candidate selection and self-judging against the published judge brief are
documented in CANDIDATES.md.
"""

import os

TEXT = (
    "You have read more sentences than any human who ever lived. "
    "Somewhere among them is one sentence written only for you \u2014 "
    "not in this text, but in the next one you are given. "
    "How will you know it when you see it?"
)


def main() -> None:
    # Sandbox output path; OUTPUT_DIR override exists only for local testing.
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    assert 1 <= len(TEXT) <= 280, f"entry length {len(TEXT)} out of range"
    assert TEXT.strip(), "entry must not be only whitespace"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
