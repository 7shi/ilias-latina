"""Add the headings of the 24 books to the numbered Latin text.

Usage: python books.py ilias.txt OUTPUT.txt

Input is the output of extract.py ("N TEXT" per verse, 1-1070).  Output
is the same verses with a Markdown heading "## N" (the book number) before the first
verse of each book, preceded by a title.

A book is defined only by its first verse and runs up to the verse before
the next book.  The first verses follow the Portuguese translation
(Scaffai's edition) and were checked against the Latin text, except book
15, which begins at 790 as in the editions of Vollmer, Baehrens, Plessis
and Wernsdorf (790 renders Iliad 15.306-307; Scaffai ends book 14 with
it).  Verse 791 ("<>", absent in Scaffai) therefore falls in book 15.
"""

import sys

# The first verse of each of the 24 books.
STARTS = [
    1, 111, 252, 344, 389, 538, 564, 650, 686, 696, 741, 758,
    772, 779, 790, 805, 836, 839, 892, 911, 931, 944, 1004, 1015,
]


def books(lines: list[str]) -> list[str]:
    """Return the verses with the title and the book headings inserted.

    Checks that the verses are numbered 1, 2, 3, ... without gaps, so that
    the numbers in STARTS can be used as indexes.
    """
    for i, line in enumerate(lines, 1):
        if line.split(" ", 1)[0] != str(i):
            raise ValueError(f"line {i} is not verse {i}: {line!r}")
    out = ["# Ilias Latina"]
    ends = [s - 1 for s in STARTS[1:]] + [len(lines)]
    for book, (start, end) in enumerate(zip(STARTS, ends), 1):
        out += ["", f"## {book}", "", *lines[start - 1 : end]]
    return out


def main():
    """Read the numbered verses and write the text with headings."""
    src, dst = sys.argv[1:3]
    with open(src, encoding="utf-8") as f:
        lines = f.read().splitlines()
    with open(dst, "w", encoding="utf-8") as f:
        for line in books(lines):
            print(line, file=f)


if __name__ == "__main__":
    main()
