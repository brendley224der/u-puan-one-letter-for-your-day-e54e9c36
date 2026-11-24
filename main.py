#!/usr/bin/env python3
"""One Letter for Your Day -- make.fun entry (program/v1).

The brief: write exactly one letter, A-Z, to /output/entry.txt. Behind the
letter sits a word describing the day, and a judge model reads two letters
at a time and picks the one whose hidden word feels more vivid, funnier,
or more true.

My pick is the letter "U", for the word UNHINGED.

Why U:
  - "Unhinged" is the sharpest U-word for a day: a day that came apart at
    the seams, plans derailed, everything slightly off the rails. It calls
    up a picture at once instead of a vague mood.
  - It is funny in the way people actually talk: "today was unhinged" is
    something a reader repeats to a friend, not a performance.
  - It is true: chaotic, derailed days are real days, ordinary and strange
    at once.
  - The letter fits the word exactly: U is the initial of "unhinged", and
    no other letter claims it.
  - It is not one of the brief's own examples (A for amazing, F for
    Friday-feeling, Z for zero sleep), so it is less likely to be the
    crowded pick every entrant reaches for first.

The program is fully deterministic: no input, no randomness, no clock,
no network. Every run writes the same single byte.
"""

import os

LETTER = "U"  # initial of UNHINGED, the word behind this entry
OUTPUT_PATH = "/output/entry.txt"


def main():
    """Write the single letter to the output file, then verify it."""
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)
    # Read the file back and confirm the gate's shape: exactly one
    # capital letter, A-Z, and nothing else. Fail loudly rather than
    # silently shipping a bad entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if len(written) != 1 or not ("A" <= written <= "Z"):
        raise ValueError("entry.txt must hold exactly one letter A-Z, got %r" % written)
    print("wrote %r to %s" % (written, OUTPUT_PATH))


if __name__ == "__main__":
    main()
