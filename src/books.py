"""Add the headings of the 24 books to the numbered Latin text.

Usage: python books.py ilias.txt books.tsv OUTPUT.txt

Input is the output of extract.py ("N TEXT" per verse, 1-1070) and
books.tsv, which gives the first verse of each book (columns "book" and
"verse").  Output is the same verses with a Markdown heading "## N" (the
book number) before the first verse of each book, preceded by a title.

A book is defined only by its first verse and runs up to the verse before
the next book.  The first verses follow the Portuguese translation
(Scaffai's edition) and were checked against the Latin text, except book
15, which begins at 790 as in the editions of Vollmer, Baehrens, Plessis
and Wernsdorf (790 renders Iliad 15.306-307; Scaffai ends book 14 with
it).  Verse 791 ("<>", absent in Scaffai) therefore falls in book 15.
"""

import csv
import sys


def read_starts(path: str) -> list[int]:
    """Return the first verse of each book from books.tsv.

    Checks that the books are numbered 1, 2, 3, ... and that their first
    verses increase.
    """
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    starts = []
    for i, row in enumerate(rows, 1):
        if row["book"] != str(i):
            raise ValueError(f"row {i} is not book {i}: {row!r}")
        verse = int(row["verse"])
        if starts and verse <= starts[-1]:
            raise ValueError(f"book {i} does not start after book {i - 1}")
        starts.append(verse)
    return starts


def books(lines: list[str], starts: list[int]) -> list[str]:
    """Return the verses with the title and the book headings inserted.

    Checks that the verses are numbered 1, 2, 3, ... without gaps, so that
    the numbers in starts can be used as indexes.
    """
    for i, line in enumerate(lines, 1):
        if line.split(" ", 1)[0] != str(i):
            raise ValueError(f"line {i} is not verse {i}: {line!r}")
    out = ["# Ilias Latina"]
    ends = [s - 1 for s in starts[1:]] + [len(lines)]
    for book, (start, end) in enumerate(zip(starts, ends), 1):
        out += ["", f"## {book}", "", *lines[start - 1 : end]]
    return out


def main():
    """Read the numbered verses and write the text with headings."""
    src, tsv, dst = sys.argv[1:4]
    with open(src, encoding="utf-8") as f:
        lines = f.read().splitlines()
    starts = read_starts(tsv)
    with open(dst, "w", encoding="utf-8") as f:
        for line in books(lines, starts):
            print(line, file=f)


if __name__ == "__main__":
    main()
