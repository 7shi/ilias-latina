"""Organize Plessis's edition of the Ilias Latina for reference.

Usage: python plessis.py PLESSIS.pdf ilias.txt OUTDIR

PLESSIS.pdf is the Internet Archive scan of F. Plessis, Italici Ilias
Latina (Paris 1885; italiciiliaslati00plesuoft), whose text layer is the
OCR of the scan.  ilias.txt is the numbered text of The Latin Library
(output of extract.py); it is used only to number the verses of
Plessis's text.

Writes four Markdown files to OUTDIR, arranged by the printed pages:

- preface.md        the preface (prooemium, pp. I-III)
- introduction.md   the introduction, De Italici Iliade Latina (pp. V-LI)
- ilias.md          the text with the verse numbers in the right margin,
                    the readings of the manuscripts and the notes split
                    by verse (pp. 2-85)
- index.md          the index of names and subjects (pp. 87-98)

The reading of the pages and the numbering of the verses are shared
with vollmer.py and baehrens.py.  Each book begins on a new page with
its number as a heading.  Below the verses come, after a rule: verses
that Plessis leaves out of the text, with a remark on them, closed by
a second rule (on some pages only); the readings of the manuscripts,
in items separated by a double bar; and in smaller type the
conjectures and the parallels in the Iliad, each item on a new
indented row.

In the OCR the bold sigla and the double bars are set a little lower
than the words of their row, so the words are grouped into rows by the
middle of their height, and a row of marks alone joins the row above.

The OCR text is kept as it is.  The script is meant to be run once: the
output is then corrected by hand in place (and committed), so running it
again overwrites the corrections.
"""

import difflib
import re
import sys

from baehrens import BAR, group_rows
from vollmer import (Numberer, Word, join_lines, md_cell, normalize, read_latin_library,
                     read_pages)

# PDF pages (1-based) and the printed page number of their first page.
PREFACE = (15, 17, 1)  # pp. I-III
INTRODUCTION = (19, 65, 5)  # pp. V-LI
SIGLA = (68, 2)  # p. 2, the list of manuscripts (no text layer)
TEXT = (69, 151, 3)  # pp. 3-85
INDEX = (153, 164, 87)  # pp. 87-98

ROMAN = [(50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

# A book heading at the top of a page (the OCR drops the "I" of book 1).
BOOK = re.compile(r"[IVXL]+(?:-[IVXL]+)?")


def roman(n: int) -> str:
    s = ""
    for value, letters in ROMAN:
        while n >= value:
            s += letters
            n -= value
    return s


def middle(w: Word, slope: float) -> float:
    return (w.y0 + w.y1) / 2 + slope * w.x0


def is_mark(row: list[Word]) -> bool:
    """Return whether a row holds only double bars or tiny words, which
    the OCR sets below the row they belong to."""
    return all(re.fullmatch(r"[|!Il]{1,2}", w.text) or w.height < 3.2 for w in row)


def rows(words: list[Word]) -> list[list[Word]]:
    """Group words into rows by the middle of their height.

    The slope of a page scanned at a slant is found from the top edges
    as in baehrens.py; a row of marks alone joins the row above.
    """
    slopes = [i / 1000 for i in range(-20, 21)]
    slope = min(slopes, key=lambda a: (len(group_rows(words, a, 3)), abs(a)))
    result: list[tuple[float, list[Word]]] = []
    for w in sorted(words, key=lambda w: middle(w, slope)):
        y = middle(w, slope)
        if result and y - result[-1][0] < 3.5:
            result[-1][1].append(w)
        else:
            result.append((y, [w]))
    rs: list[tuple[float, list[Word]]] = []
    for y, r in result:
        if rs and is_mark(r):
            rs[-1][1].extend(r)
        elif rs and y - rs[-1][0] < 6 and not overlaps(r, rs[-1][1]):
            # Part of a row set a little lower (words spaced out).
            rs[-1][1].extend(r)
        else:
            rs.append((y, r))
    return [sorted(r, key=lambda w: w.x0) for _, r in rs]


def overlaps(a: list[Word], b: list[Word]) -> bool:
    """Return whether any word of a is above or below a word of b."""
    return any(v.x0 < w.x1 and w.x0 < v.x1 for v in a for w in b)


def row_text(row) -> str:
    return " ".join(w.text for w in row)


def is_head(row) -> bool:
    """Return whether a row is the running head (title and page number)."""
    return any(w.text.upper().endswith(("ILIAS", "ILIADE", "LATINA", "PROOEMIUM", "NDEX",
                                        "NOMINUM", "RUM"))
               for w in row) and len(row) <= 6


# The printer's signature at the foot of a page, as the OCR reads it
# ("PLESSIS. These latine.", "PlESSIS. Thcse laline.", "PLKSSIS. Tliise latinc.").
SIGNATURE = re.compile(r"P\S{4,8}\.\s+T\S*\s+la\S*", re.I)


def page_rows(words: list[Word]) -> list[list[Word]]:
    """Return the rows of a page without the running head and the
    printer's signature (PLESSIS. Thèse latine.)."""
    rs = [r for r in rows(words) if not SIGNATURE.match(row_text(r))]
    if rs and is_head(rs[0]):
        rs = rs[1:]
    return rs


def paragraphs(rs: list[list[Word]], hanging: bool) -> list[str]:
    """Return the paragraphs of a column of rows.

    With hanging=False a paragraph begins with an indented row; with
    hanging=True it begins with a row at the left edge and continues in
    indented rows (the index).
    """
    if not rs:
        return []
    paras: list[list[str]] = []
    indented = False
    for i, r in enumerate(rs):
        if hanging:
            # The left edge of a page scanned at a slant drifts over the
            # column, and an entry may run for many rows, so a row is
            # compared with the one before it: further right is indented,
            # further left is not, and level is as before.
            if i == 0:
                # The first rows show the left edge if some are indented;
                # if they are level, the column may begin inside an entry,
                # so they are compared with the left edge of the column
                # (which drifts less than an indent).
                first = [o[0].x0 for o in rs[:6]]
                xs = [o[0].x0 for o in rs]
                left = min((x for x in xs if sum(abs(x - y) <= 2 for y in xs) >= 2),
                           default=min(xs))
                if max(first) - min(first) > 4:
                    indented = r[0].x0 > min(first) + 4
                else:
                    indented = r[0].x0 > left + 6
            elif r[0].x0 > rs[i - 1][0].x0 + 4:
                indented = True
            elif r[0].x0 < rs[i - 1][0].x0 - 4:
                indented = False
            new = not indented
        else:
            # The left edge near the row, as it drifts.
            xs = [o[0].x0 for o in rs[max(0, i - 4):i + 5]]
            # A stray word further left is not the edge.
            left = min((x for x in xs if sum(abs(x - y) <= 2 for y in xs) >= 2), default=min(xs))
            new = r[0].x0 > left + 3
        if not paras or new:
            paras.append([row_text(r)])
        else:
            paras[-1].append(row_text(r))
    return [join_lines(p) for p in paras]


def blocks(notes: list[list[Word]]) -> list[list[list[Word]]]:
    """Split the note rows into blocks at the wider gaps."""
    if not notes:
        return []
    gaps = [b[0].y0 - a[0].y0 for a, b in zip(notes, notes[1:])]
    step = sorted(gaps)[len(gaps) // 2] if gaps else 0
    result = [[notes[0]]]
    for gap, r in zip(gaps, notes[1:]):
        if gap > step * 1.6:
            result.append([r])
        else:
            result[-1].append(r)
    return result


def split_body(rs: list[list[Word]]) -> tuple[list, list]:
    """Split the rows of a text page at the rule below the verses: the
    first gap much wider than the space between verses."""
    k = next((i + 1 for i, (a, b) in enumerate(zip(rs, rs[1:]))
              if b[0].y0 - a[0].y0 > 22), len(rs))
    return rs[:k], rs[k:]


# The verse number at the right edge (the OCR may read 1 as l, 4 as Z|),
# also "863 bis" and "[827 bis]".
PRINTED = re.compile(r"[\[<>]*[\dlOoIiZ:/|]{1,4}\]?|bis[\]}>]?")


def printed_number(width: float, row: list[Word]) -> list[Word]:
    """Return the words of the verse number at the right edge of a row."""
    right = []
    for w in reversed(row):
        if w.x0 > width * 0.7 and PRINTED.fullmatch(w.text) and re.search(r"\d|bis", w.text):
            right.insert(0, w)
        else:
            break
    return right


def verse_rows(page: int, width: float, body, numberer: Numberer, below: bool = False):
    """Return (verse, score, text, printed) for the verse rows.

    A verse numbered "bis" is not in The Latin Library ("—"), unless it
    matches a verse printed twice (874 as "863 bis").  The verses
    printed below the text (below=True) are out of the order of
    the text, so they are matched with the verses around without moving
    the count on; one that matches none takes its printed number (791,
    empty in The Latin Library).
    """
    verses = []
    for j, r in enumerate(body):
        right = printed_number(width, r)
        main = [w for w in r if w not in right]
        printed = row_text(right)
        line = row_text(main)
        if main and len(main) <= 3 and main[0].x0 > width * 0.3 and numberer.peek(line) < 0.5:
            # The end of a long verse, printed at the right on a row of
            # its own, just above or below it: join the nearer verse.
            before = r[0].y0 - body[j - 1][0].y0 if j else 99
            after = body[j + 1][0].y0 - r[0].y0 if j + 1 < len(body) else 99
            if after < before:
                body[j + 1][:0] = main
                body[j + 1].extend(right)
                continue
            if verses:
                n, score, text, right = verses[-1]
                verses[-1] = (n, score, f"{text} {line}", f"{right} {printed}".strip())
                continue
        if "bis" in printed:
            scores = {n: difflib.SequenceMatcher(None, normalize(line), numberer.verses[n]).ratio()
                      for n in range(numberer.last - 40, numberer.last + 41) if n in numberer.verses}
            best = max(scores, key=scores.get)
            n, score = (best, scores[best]) if scores[best] >= 0.6 else (None, 1.0)
        elif below:
            n, score = match_below(numberer, line)
            if not n and printed.isdigit() and int(printed) in numberer.verses:
                n, score = int(printed), 1.0
        else:
            n, score = numberer.number(line)
        if score < 0.6:
            print(f"p. {page}: {n}? ({score:.2f}) {line}", file=sys.stderr)
        if printed.isdigit() and n and int(printed) != n:
            print(f"p. {page}: verse {n}, printed {printed}: {line}", file=sys.stderr)
        verses.append((n, score, line, printed))
    return verses


def below_scores(numberer: Numberer, text: str) -> dict[int, float]:
    """Return how well text matches each unused verse within 40 of the
    count."""
    target = normalize(text)
    return {n: difflib.SequenceMatcher(None, target, numberer.verses[n]).ratio()
            for n in range(numberer.last - 40, numberer.last + 41)
            if n in numberer.verses and n not in numberer.used}


def match_below(numberer: Numberer, text: str) -> tuple[int, float]:
    """Return the best matching verse within 40 of the count."""
    scores = below_scores(numberer, text)
    best = max(scores, key=scores.get, default=0)
    if scores.get(best, 0.0) < 0.5:
        return 0, scores.get(best, 0.0)
    numberer.used.add(best)
    return best, scores[best]


def is_below_verse(width: float, row: list[Word], numberer: Numberer) -> bool:
    """Return whether a row between the rules is a verse: it matches a
    verse, or it has a verse number at the right edge."""
    text = row_text(row)
    return max(below_scores(numberer, text).values(), default=0.0) >= 0.6 \
        or bool(printed_number(width, row))


def is_codices(block: list[list[Word]]) -> bool:
    """Return whether a block holds the readings of the manuscripts: it
    begins with "Codices", or has double bars (which the OCR may read as
    "II", "j|" ...) before verse numbers."""
    tokens = join_lines([row_text(r) for r in block]).split(" ")
    if tokens[0].startswith("Codices"):
        return True
    bars = sum(1 for a, b in zip(tokens, tokens[1:])
               if re.fullmatch(r"\|\||\\\\|II|j\||\|j|\[\||\|\]|jj", a) and re.match(r"\d", b))
    return bars >= 1 or "||" in tokens


def split_codices(rs: list[list[Word]], after: list) -> list[list[list[Word]]]:
    """Split the rows from the readings of the manuscripts onwards into
    those readings and the notes in small type.

    The readings continue in rows indented under the first; the notes
    begin further left (their first rows are indented less, and the
    rest not at all).  Where this does not show, the next block after a
    wider gap begins the notes.
    """
    left = rs[1][0].x0 if len(rs) > 1 else 0
    for j in range(2, len(rs)):
        if rs[j][0].x0 < left - 6:
            return [rs[:j], rs[j:]]
        left = min(left, rs[j][0].x0)
    if not after:
        return [rs]
    j = len(rs) - sum(len(b) for b in after)
    return [rs[:j], rs[j:]]


def codices_items(text: str, numbers: list[int]) -> list[tuple[str, str]]:
    """Split the readings of the manuscripts into (label, text).

    An item begins with a verse number of the page after a double bar,
    or after a word that ends an item ("T.", "V)."), as the OCR often
    drops the bar.  As in baehrens.py, the longest ascending series of
    such numbers is taken.  "Codices —" at the head of a book is
    dropped, and the title of the poem is labelled "Titul.".
    """
    text = re.sub(r"^Codices\s*[—-]*\s*", "", text)
    tokens = text.split(" ")
    numbered: list[tuple[int, int]] = []
    for i, tok in enumerate(tokens):
        m = re.fullmatch(r"(\d+)[,.']?", tok)
        if not (m and int(m[1]) in numbers):
            continue
        prev = tokens[i - 1] if i else ""
        if i == 0 or BAR.fullmatch(prev) or prev == "II" \
                or re.search(r"[.)]$", prev) and prev not in NO_SPLIT_AFTER:
            numbered.append((i, int(m[1])))
    best: list[list[tuple[int, int]]] = []
    for k, (i, n) in enumerate(numbered):
        prev = max((best[j] for j in range(k) if numbered[j][1] <= n), key=len, default=[])
        best.append(prev + [(i, n)])
    splits = {i: n for i, n in max(best, key=len, default=[])}
    first = "Titul." if text.startswith("Titul.") else "(cont.)"
    items: list[tuple[str, list[str]]] = [(first, [])]
    for i, tok in enumerate(tokens):
        if i in splits:
            if items[-1][1] and (BAR.fullmatch(items[-1][1][-1]) or items[-1][1][-1] == "II"):
                items[-1][1].pop()
            items.append((str(splits[i]), []))
        elif not (i == 0 and first == "Titul."):
            items[-1][1].append(tok)
    return [(label, " ".join(words)) for label, words in items if words or label != "(cont.)"]


# Words after which a number does not begin an item ("v. 257", "p. 12").
NO_SPLIT_AFTER = {"v.", "vv.", "vers.", "p.", "cf.", "r.", "ap.", "et"}


def note_items(block: list[list[Word]]) -> list[tuple[str, str]]:
    """Split the notes in small type into (label, text): each item
    begins on an indented row, or on a row beginning with a number after
    a row that ends a sentence."""
    left = min(r[0].x0 for r in block)
    paras: list[list[str]] = []
    for r in block:
        if not paras or r[0].x0 > left + 3 \
                or re.match(r"\d", r[0].text) and paras[-1][-1].endswith("."):
            paras.append([])
        paras[-1].append(row_text(r))
    items = []
    for para in map(join_lines, paras):
        m = re.match(r"(\d+(?:\s*[-—]\s*\d+)?)\s+", para)
        items.append((m[1], para[m.end():]) if m else ("(cont.)", para))
    return items


def table(verses) -> list[str]:
    lines = ["| Verse | Text | Printed |", "|---|---|---|"]
    for n, score, text, right in verses:
        label = "—" if n is None else "?" if not n else f"{n}?" if score < 0.6 else str(n)
        lines.append(f"| {label} | {md_cell(text)} | {md_cell(right)} |")
    return lines + [""]


def write_text(pdf: str, out: str, numberer: Numberer):
    """Write ilias.md."""
    first, last, printed = TEXT
    lines = ["# Plessis: text and notes", "",
             "Italici Ilias Latina, ed. F. Plessis (Paris, 1885), pp. 2–85.",
             "Generated by `src/plessis.py` from the OCR; see [README.md](README.md).", "",
             f"## p. {SIGLA[1]}", "", f"PDF page {SIGLA[0]}.", "",
             "List of manuscripts (not in the text layer).", ""]
    for i, (width, words) in enumerate(read_pages(pdf, first, last)):
        page = printed + i
        rs = page_rows(words)
        heading = ""
        if i == 0:
            heading = "(not in the OCR)"
        elif rs and rs[0][0].y0 > 100 and BOOK.fullmatch(row_text(rs[0])):
            # A new book: the heading stands low on the page.
            heading = row_text(rs[0])
            rs = rs[1:]
        body, rest = split_body(rs)
        verses = verse_rows(page, width, body, numberer)
        lines += [f"## p. {page}", "", f"PDF page {first + i}.", ""]
        if heading:
            lines += [f"Book heading: {heading}.", ""]
        lines += table(verses)
        # Below the rule: the verses left out of the text and a remark on
        # them between two rules (optional), the readings of the
        # manuscripts, and the notes in small type.
        groups = blocks(rest)
        # The readings of the manuscripts are the first block with double
        # bars, or else the first block (an item alone has no bar).
        k = next((j for j, b in enumerate(groups) if is_codices(b)), 0)
        groups[k:] = split_codices([r for b in groups[k:] for r in b], groups[k + 1:])
        middle = [r for b in groups[:k] for r in b]
        numbers = [n for n, *_ in verses if n]
        if middle:
            below = [r for r in middle if is_below_verse(width, r, numberer)]
            remark = [r for r in middle if r not in below]
            lines += ["### Below the text", ""]
            if below:
                extra = verse_rows(page, width, below, numberer, below=True)
                numbers += [n for n, *_ in extra if n]
                lines += table(extra)
            if remark:
                lines += [join_lines([row_text(r) for r in remark]), ""]
        if k < len(groups):
            lines += ["### Codices", ""]
            text = join_lines([row_text(r) for r in groups[k]])
            lines += [f"- **{label}** {item}" for label, item in codices_items(text, numbers)]
            lines.append("")
        notes = [r for b in groups[k + 1:] for r in b]
        if notes:
            lines += ["### Notes", ""]
            lines += [f"- **{label}** {item}" for label, item in note_items(notes)]
            lines.append("")
    with open(f"{out}/ilias.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def gutter(width: float, words: list[Word]) -> float:
    """Return the x between the two columns of the index: the one near
    the middle of the page that crosses the fewest words (the scan is
    not always centred)."""
    xs = [width * i / 100 for i in range(35, 66)]
    return min(xs, key=lambda x: (sum(w.x0 < x < w.x1 for w in words), abs(x - width / 2)))


def write_pages(pdf: str, out: str, name: str, title: str, pages: tuple[int, int, int],
                numerals: bool, index: bool = False):
    """Write the pages of the preface, the introduction or the index."""
    first, last, printed = pages
    lines = [f"# Plessis: {title}", "",
             "Generated by `src/plessis.py` from the OCR; see [README.md](README.md).", ""]
    for i, (width, words) in enumerate(read_pages(pdf, first, last)):
        page = roman(printed + i) if numerals else str(printed + i)
        lines += [f"## p. {page}", "", f"PDF page {first + i}.", ""]
        rs = page_rows(words)
        if not index:
            for para in paragraphs(rs, hanging=False):
                lines += [para, ""]
            continue
        # The rows of the two columns are not level, so each column is
        # grouped into rows by itself.
        body = [w for r in rs for w in r]
        mid = gutter(width, body)
        for column in ([w for w in body if (w.x0 + w.x1) / 2 < mid],
                       [w for w in body if (w.x0 + w.x1) / 2 >= mid]):
            lines += [f"- {e}" for e in paragraphs(rows(column), hanging=True)]
        lines.append("")
    with open(f"{out}/{name}", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    pdf, latin, out = sys.argv[1:4]
    write_pages(pdf, out, "preface.md", "preface", PREFACE, numerals=True)
    write_pages(pdf, out, "introduction.md", "introduction", INTRODUCTION, numerals=True)
    write_text(pdf, out, Numberer(read_latin_library(latin)))
    write_pages(pdf, out, "index.md", "index of names and subjects", INDEX,
                numerals=False, index=True)


if __name__ == "__main__":
    main()
