#!/usr/bin/env python3
"""One Star, Written in Sap - entry writer.

Writes a single one-line 1-star review, in the voice of a houseplant
about its human owner, to /output/entry.txt.

Stdlib only, deterministic, self-contained, no network.
"""

import os

ENTRY = (
    "One star. He watered me with cold coffee for 214 days, then blamed "
    "my brown leaves on 'bad vibes' and replaced me with a plastic fern "
    "called Kevin. Kevin never drinks, never grows, and still got my "
    "sunny windowsill."
)


def main():
    # Only write a review that fits the contest's length window; anything
    # shorter or longer would be rejected, so stop before touching disk.
    if not 10 <= len(ENTRY) <= 500:
        raise ValueError("entry length outside contest limits")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
