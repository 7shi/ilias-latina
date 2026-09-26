"""List the lines of the *Iliad* that Vollmer prints in his left margin.

Usage: python iliad.py TEXTS_DIR OUTPUT.md

Reads the Margin column of Vollmer's text (TEXTS_DIR/6-vollmer/ilias.md)
and writes, for each verse with a line of the *Iliad* or a dash in the
margin, its number in The Latin Library, the margin as printed, the
lines as book.line and Vollmer's text of the verse, under the book
headings of The Latin Library (TEXTS_DIR/ilias.txt).  The verses keep
Vollmer's order.

The output is derived from the files above and is rebuilt from them;
it is not corrected by hand.
"""

import re
import sys
from pathlib import Path

CELL = re.compile(r"(?<!\\)\|")
GREEK = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"

HEADER = [
    "# *Iliad*",
    "",
    "The lines of the *Iliad* that Vollmer prints in the left margin of his",
    "text ([6-vollmer/ilias.md](6-vollmer/ilias.md)), verse by verse in his",
    "order under the books of The Latin Library ([ilias.txt](ilias.txt));",
    "a verse he moves stays in his order (790 after 794, in book 15).",
    "Built by `make iliad` in this directory ([iliad.py](iliad.py)) from",
    "these two files, and rebuilt from them; do not correct it by hand.",
    "",
    "- Vollmer gives the lines of the *Iliad* that the epitomator",
    "  reproduces, so that it becomes clear in which parts he displayed his",
    "  own art and invention (preface, p. VIII).  He does not explain the",
    "  marks further.",
    "- Verse: the number in The Latin Library (\"—\" a verse it does not",
    "  have).  Margin: as printed; the book is a Greek letter where it",
    "  changes and usually on the first verse of a page.  *Iliad*: the same",
    "  as book.line (\"1.8\" for \"Α 8\").",
    "- A line marks where the correspondence begins or resumes; how far it",
    "  runs is not given.  \"—\" is as printed, a verse to which Vollmer",
    "  gives no line of Homer, in the context of the preface the poet's own",
    "  addition.  Verses with an empty margin are left out: most of them",
    "  follow Homer near the lines given before or after them.",
]


def cells(line: str) -> list[str]:
    return [c.strip().replace("\\|", "|") for c in CELL.split(line)[1:-1]]


def iliad(margin: str, book: int) -> tuple[str, int]:
    """Return the lines of the *Iliad* in Vollmer's margin as book.line,
    and the current book.

    Vollmer gives the book as a Greek letter only where it changes (and
    at the top of most pages), so it is carried on to the lines that
    follow; "148. 369" in book 18 becomes "18.148, 18.369".  A letter
    alone gives no line and is left out.
    """
    refs = []
    for m in re.finditer(r"([Α-Ω])|(\d+\??)|(ss\.)|(—)", margin):
        if m[1]:
            book = GREEK.index(m[1]) + 1
        elif m[2]:
            refs.append(f"{book}.{m[2]}")
        elif m[3]:
            refs[-1] += " ss."
        else:
            refs.append("—")
    return ", ".join(refs), book


def read_books(path: Path) -> dict[int, int]:
    """Map each verse of The Latin Library to its book."""
    books, book = {}, 0
    for line in path.read_text().splitlines():
        if m := re.match(r"## (\d+)", line):
            book = int(m[1])
        elif m := re.match(r"(\d+) ", line):
            books[int(m[1])] = book
    return books


def main() -> None:
    texts, output = Path(sys.argv[1]), Path(sys.argv[2])
    books = read_books(texts / "ilias.txt")
    lines = list(HEADER)
    ll_book = greek = 0
    header: list[str] = []
    section = ""
    for line in (texts / "6-vollmer" / "ilias.md").read_text().splitlines():
        if line.startswith("## p. "):
            section, header = "text", []
        elif line.startswith("### "):
            section, header = line[4:], []
        elif line.startswith("| Verse "):
            header = cells(line)
        elif line.startswith("|") and header and not line.startswith("|---"):
            if section not in ("text", "Below the text"):
                continue
            c = dict(zip(header, cells(line)))
            refs, greek = iliad(c.get("Margin", ""), greek)
            if not refs:
                continue
            verse = c["Verse"]
            b = books.get(int(verse), ll_book) if verse != "—" else ll_book
            if b > ll_book:
                ll_book = b
                lines += ["", f"## Book {b}", "",
                          "| Verse | Margin | *Iliad* | Text |",
                          "|---|---|---|---|"]
            row = [verse, c["Margin"], refs, c["Text"]]
            lines.append("| " + " | ".join(s.replace("|", "\\|") for s in row) + " |")
    output.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
