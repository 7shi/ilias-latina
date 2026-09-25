"""Organize Baehrens's edition of the Ilias Latina for reference.

Usage: python baehrens.py BAEHRENS.pdf ilias.txt OUTDIR

BAEHRENS.pdf is the Internet Archive scan of Poetae Latini Minores III-IV
(poetaelatinimino34baeh), whose text layer is the OCR of the scan.
ilias.txt is the numbered text of The Latin Library (output of
extract.py); it is used only to number the verses of Baehrens's text.

Writes two Markdown files to OUTDIR, arranged by the printed pages:

- preface.md   the preface, with the list of manuscripts (pp. 3-7)
- ilias.md     the text with the numbers in the right margin and the
               apparatus split by verse (pp. 7-59)

The reading of the pages and the numbering of the verses are shared
with vollmer.py.  Baehrens has no left margin; the right margin holds
the verse number every five verses and, at the first verse of a book,
its number in Roman numerals, sometimes on a row of its own above the
verse.  The items of the apparatus are separated by a double bar.

The OCR text is kept as it is.  The script is meant to be run once: the
output is then corrected by hand in place (and committed), so running it
again overwrites the corrections.
"""

import re
import sys

from vollmer import (Numberer, Word, apparatus_marks, column_paragraphs,
                     join_lines, md_cell, read_latin_library, read_pages)

# PDF pages (1-based) and the printed page number of their first page.
PREFACE = (7, 11, 3)  # pp. 3-7 (the text begins on p. 7)
TEXT = (11, 63, 7)  # pp. 7-59

# Baehrens's numbers where they do not follow the order of the rows: he
# prints 109 and 107 in each other's place (after L. Mueller).
# (printed page, first words) -> number.
NUMBER_FIXES = {
    (12, "Et dapibus diui"): 109,
    (12, "Interea sol emenso"): 108,
    (12, "Conciliumque simul"): 107,
}
# Rows whose verse of The Latin Library cannot be found by matching:
# 791 is empty there.
VERSE_FIXES = {
    (46, "[Instaurantque manus"): 791,
}

# A Roman numeral in the right margin (the OCR may read V as Y or T, or
# garble it into marks).
BOOK = re.compile(r"[IVXYTL!•.,]+")
# A verse number in the right margin (the OCR may read 1 as l, 0 as O).
NUMBER = re.compile(r"\d{1,4}|[\dlOoIis]{2,5}")
# A token that the OCR may make of the double bar between items ("||",
# "\\", "jj", "[|", "H" ...).
BAR = re.compile(r"[|!\[\](){}jiIlHfUy:\\1]{1,3}")
# The beginning of an item: a verse number or range, or a book heading.
LABEL = re.compile(r"((?:post|ante|inter)\s+)?\d+"
                   r"(?:\s*(?:—|-|,|/)\s*\d+)?(?:\s+sqq?\.)?|(?:Lib\.\s*)?[IVX]+(?=\s)")


def group_rows(words: list[Word], slope: float, tolerance: float) -> list[list[Word]]:
    """Group words into rows by their top edge corrected for the slope."""
    result: list[tuple[float, list[Word]]] = []
    for w in sorted(words, key=lambda w: w.y0 + slope * w.x0):
        y = w.y0 + slope * w.x0
        if result and y - result[-1][0] < tolerance:
            result[-1][1].append(w)
        else:
            result.append((y, [w]))
    return [sorted(r, key=lambda w: w.x0) for _, r in result]


def rows(words: list[Word]) -> list[list[Word]]:
    """Group words into rows, allowing for a page scanned at a slant.

    Some pages are slightly rotated, so that the words at the right end
    of a row are higher than the first; the slope that gives the fewest
    rows is used.
    """
    slopes = [i / 1000 for i in range(-20, 21)]
    best = min(slopes, key=lambda a: (len(group_rows(words, a, 3)), abs(a)))
    rs = group_rows(words, best, 4)
    # A verse number set a little apart from its row joins the nearest row
    # (a number with no row near it marks a lacuna).
    def y(r):
        return sum(w.y0 + best * w.x0 for w in r) / len(r)
    for r in [r for r in rs if all(re.fullmatch(r"[\dlOoI]{2,4}", w.text) for w in r)]:
        others = [o for o in rs if o is not r]
        near = min(others, key=lambda o: abs(y(o) - y(r)), default=None)
        if near and abs(y(near) - y(r)) < 8:
            near.extend(r)
            near.sort(key=lambda w: w.x0)
            rs.remove(r)
    return rs


def row_text(row) -> str:
    return " ".join(w.text for w in row)


def is_head(row) -> bool:
    """Return whether a row is the running head (page number, title)."""
    return len(row) <= 4 and any(re.fullmatch(r"[A-Z]{4,}\.?", w.text) for w in row)


def is_signature(row) -> bool:
    """Return whether a row is a printer's signature at the foot (3*,
    POET. LAT. MIN. III. 2)."""
    return bool(re.fullmatch(r"\d+\*|POET\..*", row_text(row)))


def text_start(rs, numberer: Numberer) -> int:
    """Return the index of the first verse row on p. 7."""
    return next(i for i, r in enumerate(rs) if numberer.peek(row_text(r)) >= 0.7)


def split_page(rs, numberer: Numberer):
    """Split the rows of a text page into verse rows and note rows.

    As in vollmer.py, the notes begin where the fewest rows are out of
    place (rows above that match no verse, rows below that match one);
    among equal places, at the widest gap (the rule).
    """
    good = [numberer.peek(row_text(r)) >= 0.5 and apparatus_marks(r) < 2 for r in rs]

    def gap(k: int) -> float:
        return rs[k][0].y0 - rs[k - 1][0].y0 if 0 < k < len(rs) else 0.0
    end = min(range(len(rs) + 1),
              key=lambda k: (good[:k].count(False) + good[k:].count(True), -gap(k)))
    return rs[:end], rs[end:]


class Counter:
    """Count Baehrens's own verse numbers from the rows of the text."""

    def __init__(self):
        self.last = 0

    def next(self, page: int, line: str, printed: str) -> int:
        fix = next((v for (p, start), v in NUMBER_FIXES.items()
                    if p == page and line.startswith(start)), None)
        n = fix or self.last + 1
        self.last = max(self.last, n)
        if printed.isdigit() and int(printed) != n:
            print(f"p. {page}: counted {n}, printed {printed}: {line}", file=sys.stderr)
        return n


def verse_rows(page: int, width: float, body, numberer: Numberer, counter: Counter):
    """Return (verse, score, baehrens, text, printed, book) for the verse rows.

    A row with a verse number but no text is the row of dots that marks
    a lacuna; it has no verse of The Latin Library ("—").
    """
    verses = []
    book = ""
    for r in body:
        right = [w for w in r if w.x0 > width * 0.8
                 and (BOOK.fullmatch(w.text) or NUMBER.fullmatch(w.text))]
        # A book number printed close after a long verse.
        while len(r) > len(right) + 1 and re.fullmatch(r"[IVXYT]{2,}\.?", r[-1 - len(right)].text):
            right.insert(0, r[-1 - len(right)])
        main = [w for w in r if w not in right]
        if all(BOOK.fullmatch(w.text) for w in r):
            # A book number on a row of its own belongs to the next verse.
            book = row_text(r)
            continue
        numeral = " ".join(w.text for w in right if BOOK.fullmatch(w.text))
        printed = " ".join(w.text for w in right if not BOOK.fullmatch(w.text))
        line = row_text(main)
        if verses and main and len(main) <= 2 and main[0].x0 > width * 0.3 \
                and numberer.peek(line) < 0.5:
            # The end of a long verse, printed below it at the right.
            n, score, b, text, right, bk = verses[-1]
            verses[-1] = (n, score, b, f"{text} {line}", f"{right} {printed}".strip(), bk)
            continue
        if not main or re.fullmatch(r"[.· ]*", line):
            n, score = None, 1.0
        else:
            fix = next((v for (p, start), v in VERSE_FIXES.items()
                        if p == page and line.startswith(start)), None)
            n, score = (fix, 1.0) if fix else numberer.number(line)
        verses.append((n, score, counter.next(page, line, printed), line, printed,
                       numeral or book))
        book = ""
    return verses


def split_items(text: str, numbers: list[int]) -> list[tuple[str, str]]:
    """Split the apparatus into (label, text) at the double bars.

    An item begins after a token that may be a double bar and with a
    label: a verse number of the page (Baehrens's numbering), or "post
    563", "Lib. VII", a Roman numeral (a book) after a clear double bar.
    Of the numbered labels, the longest series in ascending order is
    taken, so that a misread number does not hide the labels after it.
    Text before the first label continues an item from the previous page.
    """
    tokens = text.split(" ")
    numbered: list[tuple[int, int]] = []  # (token index, number)
    other: list[int] = []
    for i, tok in enumerate(tokens):
        m = LABEL.match(" ".join(tokens[i + 1:i + 5]))
        if not (m and i and BAR.fullmatch(tok)):
            continue
        n = re.search(r"\d+", m[0])
        if n and int(n[0]) in numbers:
            numbered.append((i, int(n[0])))
        elif n is None and tok in ("||", "\\\\"):
            other.append(i)
    # Longest non-decreasing series of numbers.
    best: list[list[tuple[int, int]]] = []
    for k, (i, n) in enumerate(numbered):
        prev = max((best[j] for j in range(k) if numbered[j][1] <= n),
                   key=len, default=[])
        best.append(prev + [(i, n)])
    splits = {i for i, _ in max(best, key=len, default=[])} | set(other)
    parts: list[list[str]] = [[]]
    for i, tok in enumerate(tokens):
        if i in splits:
            parts.append([])
        else:
            parts[-1].append(tok)
    items = []
    for words in parts:
        s = " ".join(words).strip()
        m = LABEL.match(s)
        if m:
            items.append((m[0], s[m.end():].strip()))
        elif s:
            items.append(("(cont.)", s))
    return items


def write_text(pdf: str, out: str, numberer: Numberer):
    """Write ilias.md."""
    counter = Counter()
    first, last, printed = TEXT
    lines = ["# Baehrens: text and apparatus", "",
             "Italici Ilias Latina, ed. E. Baehrens, *Poetae Latini Minores* III",
             "(1881), pp. 7–59.  Generated by `src/baehrens.py` from the OCR; see",
             "[README.md](README.md).", ""]
    for i, (width, words) in enumerate(read_pages(pdf, first, last)):
        page = printed + i
        rs = [r for r in rows(words) if not is_signature(r)]
        if rs and is_head(rs[0]):
            rs = rs[1:]
        if i == 0:
            rs = rs[text_start(rs, numberer):]
        body, notes = split_page(rs, numberer)
        verses = verse_rows(page, width, body, numberer, counter)
        lines += [f"## p. {page}", "", f"PDF page {first + i}.", "",
                  "| Verse | Baehrens | Text | Printed | Book |", "|---|---|---|---|---|"]
        for n, score, b, text, right, book in verses:
            label = "—" if n is None else "?" if not n else f"{n}?" if score < 0.6 else str(n)
            if score < 0.6:
                print(f"p. {page}: {n}? ({score:.2f}) {text}", file=sys.stderr)
            lines.append(f"| {label} | {b} | {md_cell(text)} | {md_cell(right)} | {md_cell(book)} |")
        lines.append("")
        if notes:
            lines += ["### Apparatus", ""]
            numbers = [b for _, _, b, *_ in verses]
            for label, text in split_items(join_lines([row_text(r) for r in notes]), numbers):
                lines.append(f"- **{label}** {text}")
            lines.append("")
    with open(f"{out}/ilias.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_preface(pdf: str, out: str, numberer: Numberer):
    """Write preface.md: the preface up to the beginning of the text."""
    first, last, printed = PREFACE
    lines = ["# Baehrens: preface", "",
             "Generated by `src/baehrens.py` from the OCR; see [README.md](README.md).", ""]
    for i, (width, words) in enumerate(read_pages(pdf, first, last)):
        rs = rows(words)
        if i and is_head(rs[0]):
            rs = rs[1:]
        if first + i == TEXT[0]:
            rs = rs[:text_start(rs, numberer)]
        lines += [f"## p. {printed + i}", "", f"PDF page {first + i}.", ""]
        for para in column_paragraphs([w for r in rs for w in r], hanging=False):
            lines += [para, ""]
    with open(f"{out}/preface.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    pdf, latin, out = sys.argv[1:4]
    verses = read_latin_library(latin)
    write_preface(pdf, out, Numberer(verses))
    write_text(pdf, out, Numberer(verses))


if __name__ == "__main__":
    main()
