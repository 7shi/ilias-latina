"""Build the verse concordance of the editions organized in texts/.

Usage: python concordance.py TEXTS_DIR OUTPUT.md CHECK.txt

Reads the Latin Library text (TEXTS_DIR/ilias.txt) and the verse tables
of the editions (TEXTS_DIR/*/ilias.md), and writes one table per book of
The Latin Library: a row for each of its verses, and a row "—" for a
verse that it does not have, placed after the verse that precedes it in
the edition.  Each cell gives the edition's own number of the verse and
the printed page; the Note column gives the verses that an edition
prints out of the order of The Latin Library, with the verse they follow.

Only the numbers are compared: the text of each edition comes from its
own OCR, and the verse of The Latin Library that a row stands for is
taken from the Verse column of its ilias.md.  The rows whose text is
least like the verse of The Latin Library are listed in CHECK.txt for
checking against the page images.

The output is generated once and then corrected by hand.
"""

import re
import sys
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path

# (directory, column title, name of the own-number column or None).
EDITIONS = [
    ("6-vollmer", "Vollmer", None),
    ("3-baehrens", "Baehrens", "Baehrens"),
    ("4-plessis", "Plessis", None),
    ("2-lemaire", "Wernsdorf", "Wernsdorf"),
]

# Rows whose text is less like the verse than this are listed for checking.
THRESHOLD = 0.75

CELL = re.compile(r"(?<!\\)\|")


@dataclass
class Row:
    edition: str
    verse: int | None      # The Latin Library, None if it has no such verse
    own: str               # the edition's own number
    page: str
    text: str
    below: bool = False    # printed below the text (Plessis)
    printed: str = ""      # the number in the margin as read by the OCR
    after: int = 0         # the verse of The Latin Library before it
    moved: bool = False    # out of the order of The Latin Library


def read_ll(path: Path) -> tuple[dict[int, str], list[tuple[int, int]]]:
    """Return the verses and the (book, first verse) pairs."""
    verses, books, book = {}, [], 0
    for line in path.read_text().splitlines():
        if m := re.match(r"## (\d+)$", line):
            book = int(m[1])
            books.append((book, 0))
        elif m := re.match(r"(\d+) (.*)", line):
            n = int(m[1])
            verses[n] = m[2]
            if books[-1][1] == 0:
                books[-1] = (book, n)
    return verses, books


def read_edition(path: Path, name: str, own_col: str | None) -> list[Row]:
    """Return the verse rows of an ilias.md in the order of the edition."""
    rows, page, section, header = [], "", "", []
    for line in path.read_text().splitlines():
        if m := re.match(r"## p\. (\S+)", line):
            page, section, header = m[1], "text", []
        elif line.startswith("### "):
            section, header = line[4:], []
        elif line.startswith("| Verse "):
            header = [c.strip() for c in CELL.split(line)[1:-1]]
        elif line.startswith("|") and header and not line.startswith("|---"):
            cells = dict(zip(header, (c.strip() for c in CELL.split(line)[1:-1])))
            if section not in ("text", "Below the text"):
                continue
            verse = None if cells["Verse"] == "—" else int(cells["Verse"])
            own = cells[own_col] if own_col else str(verse or "")
            rows.append(Row(name, verse, own, page, cells["Text"],
                            printed=cells.get("Printed", ""),
                            below=section == "Below the text"))
    return rows


def mark_order(rows: list[Row]) -> None:
    """Set `after` and `moved` from the order of the rows.

    `after` is the verse of the row before it in the text.  The rows in
    the order of The Latin Library are the longest increasing series of
    their verse numbers; the others are moved.  A row printed below the
    text is not moved, and one that repeats the verse before it (a verse
    split in two) is not either.  A row that The Latin Library does not
    have and that has no own number is numbered "N bis" after the verse
    it follows; a verse of The Latin Library printed as "N bis" keeps
    that number.
    """
    main = [r for r in rows if r.verse is not None and not r.below]
    # Longest increasing subsequence (strictly increasing verse numbers).
    best: list[int] = [1] * len(main)
    prev: list[int] = [-1] * len(main)
    for i, r in enumerate(main):
        for j in range(i):
            if main[j].verse < r.verse and best[j] + 1 > best[i]:
                best[i], prev[i] = best[j] + 1, j
    keep, i = set(), max(range(len(main)), key=best.__getitem__, default=-1)
    while i >= 0:
        keep.add(id(main[i]))
        i = prev[i]
    last = 0
    for r in rows:
        r.after = last
        if r.verse is not None and "bis" in r.printed:
            r.own = re.sub(r"[^\d bis]", "", r.printed).strip()
            if not re.fullmatch(r"\d+ bis", r.own):
                r.own = ""
        if r.verse is None and not r.own:
            r.own = f"{last} bis"
        if r.verse is not None and not r.below:
            r.moved = id(r) not in keep and r.verse != last
            last = r.verse


def normalize(s: str) -> str:
    s = s.lower().replace("v", "u").replace("j", "i")
    return re.sub(r"[^a-z]", "", s)


def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, normalize(a), normalize(b)).ratio()


def label(r: Row) -> str:
    own = r.own
    if r.text.lstrip().startswith("["):
        own = f"[{own}]"
    if r.below:
        own += " below"
    return f"{own} (p. {r.page})"


def cells_for(rows: list[Row]) -> str:
    return "; ".join(label(r) for r in rows) or "—"


def build(texts: Path) -> tuple[list[str], list[str]]:
    verses, books = read_ll(texts / "ilias.txt")
    by_edition = {}
    for directory, name, own_col in EDITIONS:
        rows = read_edition(texts / directory / "ilias.md", name, own_col)
        mark_order(rows)
        by_edition[name] = rows

    # Rows of each verse, and the rows of verses that The Latin Library
    # does not have, grouped by the verse they follow.
    placed: dict[int, dict[str, list[Row]]] = {n: {} for n in verses}
    extra: dict[int, list[Row]] = {}
    check = []
    for name, rows in by_edition.items():
        for r in rows:
            if r.verse is None:
                extra.setdefault(r.after, []).append(r)
                continue
            placed[r.verse].setdefault(name, []).append(r)
            score = similarity(r.text, verses[r.verse])
            if score < THRESHOLD:
                check.append((score, r))

    names = [name for _, name, _ in EDITIONS]
    starts = {first: book for book, first in books}
    out = [
        "# Verse concordance",
        "",
        "The verses of the editions organized in this directory, keyed to",
        "the numbering of The Latin Library ([ilias.txt](ilias.txt)).",
        "Generated by `src/concordance.py` from the Verse columns of the",
        "editions' `ilias.md`; see [README.md](README.md#concordance).  The",
        "Wernsdorf column is the edition in [2-lemaire/](2-lemaire/README.md),",
        "Lemaire's reprint of Wernsdorf's text and numbering.",
    ]
    header = ["", "| LL | " + " | ".join(names) + " | Note |",
              "|---|" + "---|" * (len(names) + 1)]
    for n in sorted(verses):
        if n in starts:
            out += ["", f"## Book {starts[n]}", *header]
        rows = [r for name in names for r in placed[n].get(name, [])]
        out.append(f"| {n} | " + " | ".join(
            cells_for(placed[n].get(name, [])) for name in names) +
            f" | {note(rows)} |")
        for group in merge_extra(extra.get(n, [])):
            out.append("| — | " + " | ".join(
                cells_for([r for r in group if r.edition == name])
                for name in names) + f" | {note(group)} |")

    report = [f"{s:.2f}\t{r.edition}\tp. {r.page}\t{r.verse}\t{r.text}\t|\t{verses[r.verse]}"
              for s, r in sorted(check, key=lambda x: x[0])]
    return out, report


def note(rows: list[Row]) -> str:
    return "; ".join(f"{r.edition} after {r.after}" for r in rows if r.moved)


def merge_extra(rows: list[Row]) -> list[list[Row]]:
    """Group the rows that follow the same verse by the likeness of their text."""
    groups: list[list[Row]] = []
    for r in rows:
        for g in groups:
            if all(x.edition != r.edition for x in g) and \
                    similarity(g[0].text, r.text) >= 0.5:
                g.append(r)
                break
        else:
            groups.append([r])
    return groups


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    texts, output, check = map(Path, sys.argv[1:])
    out, report = build(texts)
    output.write_text("\n".join(out) + "\n")
    check.write_text("\n".join(report) + "\n")
    print(f"{output}: {len(out)} lines; {check}: {len(report)} rows to check",
          file=sys.stderr)


if __name__ == "__main__":
    main()
