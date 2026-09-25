"""Organize Lemaire's reprint of Wernsdorf's Ilias Latina for reference.

Usage: python lemaire.py LEMAIRE_hocr.html ilias.txt OUTDIR

LEMAIRE_hocr.html is the OCR of the Internet Archive scan of Poetae
Latini Minores III (Paris: Lemaire, 1824; poetaelatinimin00unkngoog) in
hOCR, with the position of every word.  The PDF of this scan has no text
layer, so the hOCR is read instead of pdftotext.  ilias.txt is the
numbered text of The Latin Library (output of extract.py); it is used
only to number the verses.

Writes four Markdown files to OUTDIR, arranged by the printed pages:

- prooemium.md    the half-title and Wernsdorf's prooemium on the poem,
                  its author, the Latin translators of Homer and the
                  editions (pp. 453-507)
- testimonia.md   the testimonia on the poem, with their notes
                  (pp. 508-514)
- ilias.md        the text with the verse numbers in the right margin
                  and the notes split by verse (pp. 515-610)
- excursus.md     the four excursus on the text (pp. 611-620)

The OCR (ABBYY) already groups the words into lines and the lines into
blocks.  On a text page the verses are the full-width block at the top,
and the notes the two column blocks below them; the verse numbers in
the right margin are small blocks of their own or the last word of a
verse line.  A note begins on an indented line with the number of its
verse, which the OCR often misreads (old-style figures), so the possible
readings are tried against the verses of the page.  In the prose a
paragraph begins after a line that ends short of the right edge, and
quoted verses are kept one per line.

Wernsdorf numbers the verses differently from The Latin Library, so
each verse is matched with the most similar verse of The Latin Library
(Numberer, as in vollmer.py), and his own number is counted from the
rows and checked against the printed ones (reported on stderr).  The
note labels are his numbers; the verse of The Latin Library is added
where it differs.

The OCR text is kept as it is.  The script is meant to be run once: the
output is then corrected by hand in place (and committed), so running it
again overwrites the corrections.
"""

import difflib
import html
import itertools
import re
import sys
from collections.abc import Iterator
from dataclasses import dataclass

from vollmer import Numberer, Word, join_lines, md_cell, normalize, read_latin_library

# PDF pages (1-based) and the printed page number of their first page.
TITLE = (463, 453)  # the half-title (unnumbered)
PROOEMIUM = (465, 517, 455)  # pp. 455-507
TESTIMONIA = (518, 524, 508)  # pp. 508-514
TEXT = (525, 620, 515)  # pp. 515-610
EXCURSUS = (621, 630, 611)  # pp. 611-620

# Pages that begin with a title instead of a running head.
TITLE_PAGES = {463, 465, 518, 525, 621, 627, 629}

# Rows whose verse cannot be found by matching: (printed page, first
# words) -> verse of The Latin Library, or None for a verse that The
# Latin Library does not have ("—").  791 is empty there; 957 there is
# "Hastam iam manibus saeuus librabat Achilles", which Wernsdorf does not
# have, printing another verse in its place.
VERSE_FIXES: dict[tuple[int, str], int | None] = {
    (539, "Yestrum nunc Helenam"): None,
    (566, "[Sortes miserunt"): None,
    (566, "Concurrunt armis Ajax"): None,
    (578, "[Rhesi ventigenas"): None,
    (583, "Instaurantque manus"): 791,
    (586, "Objicit et saxum"): None,
    (588, "[Tristis ait"): None,
    (598, "Interea validam Thetideius"): None,
}

# Old-style figures as the OCR reads them, with the figures each may
# stand for.
FIGURES = {"i": "1", "l": "1", "I": "1", "t": "1", "x": "1", "X": "1", "o": "0", "O": "0",
           "S": "58", "s": "58", "$": "58", "a": "2", "z": "2", "Z": "2", "g": "98",
           "y": "79", "b": "6", "G": "6", "B": "8", "&": "8", "%": "8"}
DIGITS = str.maketrans({k: v[0] for k, v in FIGURES.items()})
# The old-style 2 is also read as 1, 3 or 9.
FIGURES |= {"1": "12", "3": "32", "9": "92"}

# A book number printed at the start of a verse ("III.", "XIX et XX.").
BOOK = re.compile(r"[IVXL]+\.\s+(?:et\s+[IVXL]+\.\s+)?")


@dataclass
class Line:
    words: list[Word]

    @property
    def x0(self) -> float:
        return self.words[0].x0

    @property
    def y0(self) -> float:
        return min(w.y0 for w in self.words)

    @property
    def y1(self) -> float:
        return max(w.y1 for w in self.words)

    @property
    def text(self) -> str:
        return " ".join(w.text for w in self.words)


@dataclass
class Block:
    x0: float
    y0: float
    x1: float
    y1: float
    pars: list[list[Line]]

    @property
    def lines(self) -> list[Line]:
        return [line for par in self.pars for line in par]


@dataclass
class Page:
    width: float
    height: float
    blocks: list[Block]


def bbox(title: str) -> list[float]:
    return [float(v) for v in re.search(r"bbox (\d+) (\d+) (\d+) (\d+)", title).groups()]


def read_hocr(path: str, first: int, last: int) -> list[Page]:
    """Return the pages from first to last (PDF pages, 1-based)."""
    with open(path, encoding="utf-8") as f:
        source = f.read()
    parts = re.split(r'(?=<div class="ocr_page")', source)[1:]
    pages = []
    for part in parts[first - 1:last]:
        _, _, width, height = bbox(part)
        blocks = []
        for b in re.split(r'(?=<div class="ocr_carea")', part)[1:]:
            pars = []
            for p in re.split(r'(?=<p class="ocr_par")', b)[1:]:
                lines = []
                for l in re.split(r'(?=<span class="ocr_line")', p)[1:]:
                    words = [Word(*bbox(t), html.unescape(s).strip())
                             for t, s in re.findall(
                                 r'class="ocrx_word"[^>]*title="([^"]*)"[^>]*>([^<]*)<', l)]
                    words = [w for w in words if w.text]
                    if words:
                        lines.append(Line(words))
                if lines:
                    pars.append(lines)
            if pars:
                blocks.append(Block(*bbox(b), pars))
        pages.append(Page(width, height, blocks))
    return pages


def escape(s: str) -> str:
    """Escape a literal "<" so that it is not taken for an HTML tag."""
    return s.replace("<", "\\<")


# The "Digitized by Google" stamp as the OCR reads it.
STAMP = re.compile(r"Digiti|oogle|OOQ|OOgle")


def is_noise(line: Line) -> bool:
    """Return whether a line is the stamp, an ornamental rule or a mark
    (mostly signs read by the OCR)."""
    alnum = len(re.findall(r"\w", line.text))
    return bool(STAMP.search(line.text)) or alnum < 2 or alnum < len(line.text) / 2


def is_junk(block: Block, page: Page) -> bool:
    """Return whether a block is the "Digitized by Google" stamp or a
    stray mark in the margin."""
    text = " ".join(line.text for line in block.lines)
    if block.y0 > page.height * 0.9 and STAMP.search(text):
        return True
    return block.x1 - block.x0 < page.width * 0.1 and len(re.sub(r"\W", "", text)) <= 1


def body_blocks(page: Page, pdf_page: int) -> list[Block]:
    """Return the blocks of a page in reading order, without the stamp
    and the running head (the first line of the page)."""
    blocks = []
    for b in page.blocks:
        text = " ".join(l.text for l in b.lines)
        # A drop capital joins the line at its right (Quod, Iram).
        line = next((l for o in page.blocks for l in o.lines if o is not b
                     and l.x0 > b.x1 - 20 and l.x0 - b.x1 < 150 and l.y0 < b.y1 and b.y0 < l.y1),
                    None) if re.fullmatch(r"[A-Z]", text) else None
        if line:
            first = line.words[0]
            line.words[0] = Word(b.x0, first.y0, first.x1, first.y1, text + first.text)
        elif not is_junk(b, page):
            blocks.append(b)
    blocks.sort(key=lambda b: (b.y0, b.x0))
    if pdf_page not in TITLE_PAGES:
        # The running head: the top line and any part of it (such as the
        # page number) that the OCR puts in a line or block of its own.
        head = min((l for b in blocks for l in b.lines), key=lambda l: l.y0, default=None)
        if head:
            band = head.y0 + (head.y1 - head.y0) * 0.8
            for b in blocks:
                b.pars = [[l for l in p if (l.y0 + l.y1) / 2 > band] for p in b.pars]
                b.pars = [p for p in b.pars if p]
            blocks = [b for b in blocks if b.pars]
    return blocks


def is_column(block: Block, page: Page) -> bool:
    """Return whether a block is a column of the notes: narrower than
    the page and within its left or right half (a quotation is centred)."""
    mid = page.width / 2
    return page.width * 0.25 < block.x1 - block.x0 < page.width * 0.45 \
        and (block.x1 < mid + page.width * 0.05 or block.x0 > mid - page.width * 0.05)


def is_signature(line: Line, column: list[Line]) -> bool:
    """Return whether a line is the printer's signature at the foot of
    the page ("33."), set to the right below the last column."""
    left = min(l.x0 for l in column)
    return line is column[-1] and re.fullmatch(r"\S{1,3}\s?\.?", line.text) \
        is not None and line.x0 > left + 200


def column_items(columns: list[list[Line]]) -> list[list[str]]:
    """Split the lines of the note columns into items: an item begins on
    an indented line.  Lines before the first indent continue the item
    before (from the previous column or page)."""
    items: list[list[str]] = []
    for column in columns:
        column = [l for l in column if not is_noise(l)]
        column = [l for l in column if not is_signature(l, column)]
        if not column:
            continue
        xs = [round(l.x0) for l in column]
        # The left edge: the leftmost start shared by two lines (a stray
        # mark further left is not the edge).
        left = min((x for x in xs if sum(abs(x - y) <= 12 for y in xs) >= 2), default=min(xs))
        for line in column:
            if line.x0 > left + 40 or not items:
                items.append([])
                if line.x0 <= left + 40:
                    items[-1].append("(cont.)")
            items[-1].append(line.text)
    return items


def columns_of(blocks: list[Block], page: Page) -> list[list[Line]]:
    """Return the lines of the left and the right note column."""
    mid = page.width / 2
    cols = [b for b in blocks if is_column(b, page)]
    left = [l for b in cols if (b.x0 + b.x1) / 2 < mid for l in b.lines]
    right = [l for b in cols if (b.x0 + b.x1) / 2 >= mid for l in b.lines]
    return [sorted(left, key=lambda l: l.y0), sorted(right, key=lambda l: l.y0)]


def to_number(s: str) -> int | None:
    s = s.translate(DIGITS)
    return int(s) if s.isdigit() else None


# ---------------------------------------------------------------- prose


def prose_lines(page: Page, pdf_page: int, printed: str) -> list[str]:
    """Return the Markdown of a page of prose: the paragraphs of the
    full-width blocks, then the note columns (testimonia) as a list."""
    blocks = body_blocks(page, pdf_page)
    out = [f"## p. {printed}", "", f"PDF page {pdf_page}.", ""]
    lines = sorted((l for b in blocks if not is_column(b, page) for l in b.lines
                    if not is_noise(l)), key=lambda l: l.y0)
    # The printer's signature ("39.") below the last line, at the right.
    if lines and re.fullmatch(r"\S{1,4}\.?(?: \.)?", lines[-1].text) \
            and lines[-1].x0 > page.width / 2:
        lines = lines[:-1]
    for para in prose_paragraphs(lines):
        out += [escape(para), ""]
    items = column_items(columns_of(blocks, page))
    if items:
        out += ["### Notes", ""]
        out += [f"- {escape(join_lines(item))}" for item in items]
        out.append("")
    return out


def edge(xs: list[float], pick) -> float:
    """Return the leftmost or rightmost (pick = min or max) of the x
    shared by two lines or more (a stray mark lies further out)."""
    return pick((x for x in xs if sum(abs(x - y) <= 15 for y in xs) >= 2), default=pick(xs))


def prose_paragraphs(lines: list[Line]) -> list[str]:
    """Return the paragraphs of the prose lines of a page.

    The edges are measured against the nearby lines, as they drift on a
    slanted page.  A quoted verse, indented, short of the right edge and
    in smaller type, is a paragraph of its own.  A paragraph begins after
    a line that ends short of the right edge (not at an indent, as the
    testimonia are set with hanging indents).  The OCR's own paragraphs
    are not used, as they join quotations to the prose around them.
    """
    if not lines:
        return []
    heights = sorted(l.y1 - l.y0 for l in lines)
    height = heights[len(heights) // 2]
    paras: list[list[str]] = []
    prev_short = prev_quote = True
    # The edges are taken from the lines of prose, as wide as most lines
    # of the page (quoted verses are narrower).
    widths = sorted(l.words[-1].x1 - l.x0 for l in lines)
    wide = [l for l in lines if l.words[-1].x1 - l.x0 > widths[len(widths) * 3 // 4] * 0.8]
    for i, l in enumerate(lines):
        near = [o for o in wide if abs(o.y0 - l.y0) < height * 8] or wide
        left = edge([o.x0 for o in near], min)
        right = edge([o.words[-1].x1 for o in near], max)
        short = l.words[-1].x1 < right - 60
        quote = l.x0 > left + 60 and short and l.y1 - l.y0 < height * 0.85
        if quote or prev_quote or prev_short:
            paras.append([])
        paras[-1].append(l.text)
        prev_short, prev_quote = short, quote
    return [join_lines(p) for p in paras]


def write_prose(hocr: str, out: str, name: str, title: str, intro: list[str],
                pages: tuple[int, int, int], extra: tuple[tuple[int, int], ...] = ()):
    first, last, printed = pages
    lines = [f"# Lemaire: {title}", "", *intro,
             "Generated by `src/lemaire.py` from the OCR; see [README.md](README.md).", ""]
    # Unnumbered pages (the half-title), with the page number in brackets.
    for pdf_page, page_no in extra:
        lines += prose_lines(read_hocr(hocr, pdf_page, pdf_page)[0], pdf_page, f"[{page_no}]")
    for i, page in enumerate(read_hocr(hocr, first, last)):
        lines += prose_lines(page, first + i, str(printed + i))
    with open(f"{out}/{name}", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# ----------------------------------------------------------------- text


# Letters that the OCR never gives for a figure.
NOT_FIGURE = set("cdefhkmnpqruvw")


def is_margin_number(token: str) -> bool:
    """Return whether the last word of a verse row may be the verse
    number in the margin that the OCR has joined to it."""
    token = token.strip(".,;:")
    return 0 < len(token) <= 4 and sum(c.isalpha() and c.lower() in NOT_FIGURE
                                       for c in token) <= 1 and not token.istitle()


def verse_rows(page: Page, blocks: list[Block], page_no: int, numberer: Numberer,
               counter: Iterator[int]) -> tuple[list[str], list[list]]:
    """Return the title lines (first page only) and the verse rows
    [verse, score, wernsdorf, text, printed] of a text page.  Wernsdorf
    prints no verse out of order, so his number is counted (counter)."""
    top = min((b.y0 for b in blocks if is_column(b, page)), default=page.height)
    region = [b for b in blocks if not is_column(b, page) and b.y0 < top]
    lines = sorted((l for b in region for l in b.lines), key=lambda l: l.y0)
    margin = [l for l in lines if l.x0 > page.width * 0.8]
    main: list[Line] = []
    for l in lines:
        if l in margin:
            continue
        # A verse number printed close after the verse.
        words = list(l.words)
        while len(words) > 1 and words[-1].x0 > page.width * 0.8 \
                and (re.search(r"\d", words[-1].text) or words[-1].x0 - words[-2].x1 > 80):
            margin.append(Line([words.pop()]))
        main.append(Line(words))
    title: list[str] = []
    rows: list[list] = []
    for l in main:
        text = l.text
        if not rows and numberer.peek(BOOK.sub("", text, count=1)) < 0.5 and page_no == TEXT[2]:
            if len(re.findall(r"\w", text)) > len(text) / 2:  # not the ornament
                title.append(text)
            continue
        if rows and l.x0 > page.width * 0.4 and numberer.peek(text) < 0.5:
            # The end of a long verse, printed below it at the right.
            rows[-1][3] += " " + text
            continue
        if len(re.findall(r"[a-z]", text)) < 8:
            # A mark or a smudge read as letters.
            print(f"p. {page_no}: not a verse: {text}", file=sys.stderr)
            continue
        key = next((k for k in VERSE_FIXES if k[0] == page_no and text.startswith(k[1])), None)
        n, score = (VERSE_FIXES[key], 1.0) if key else \
            numberer.number(BOOK.sub("", text, count=1))
        rows.append([n, score, 0, text, "", l])
    for m in margin:
        # The margin number belongs to the verse row nearest in height.
        mid = (m.y0 + m.y1) / 2
        row = min(rows, key=lambda r: abs((r[5].y0 + r[5].y1) / 2 - mid), default=None)
        if row:
            row[4] = f"{row[4]} {m.text}".strip()
    for row in rows:
        row[2] = next(counter)
        words = row[3].split(" ")
        # Every fifth verse has its number in the margin; the OCR often
        # joins it to the end of the verse.
        if row[2] % 5 == 0 and not row[4] and len(words) > 1 \
                and row[5].words[-1].x0 > page.width * 0.75 and is_margin_number(words[-1]):
            row[3], row[4] = " ".join(words[:-1]), words[-1]
        number = to_number(row[4].replace(" ", ""))
        if number is not None and number != row[2]:
            print(f"p. {page_no}: counted {row[2]}, printed {row[4]}: {row[3]}", file=sys.stderr)
    return title, [row[:5] for row in rows]


FIGURE = r"[\d" + re.escape("".join(FIGURES)) + r"]"
LABEL = re.compile(rf"[·•.'\s]*((?:{FIGURE}\s?){{1,4}}?)"
                   rf"(?:\s*[-—]\s*((?:{FIGURE}\s?){{1,4}}?))?\s*[.,*•\-:;]\s*")


def readings(token: str) -> list[int]:
    """Return the numbers that a label read by the OCR may stand for,
    the likeliest first (the fewest figures read in a second way)."""
    options = [("", 0)]
    for c in token.replace(" ", ""):
        options = [(o + d, k + (i > 0)) for o, k in options
                   for i, d in enumerate(FIGURES.get(c, c))]
    return [int(o) for o, _ in sorted(options, key=lambda o: o[1])]


def note_label(text: str, numbers: set[int], last: int, to_ll: dict[int, int],
               verses: dict[int, list[str]]) -> tuple[str, str, int]:
    """Return (label, text, number) of a note: the number it begins
    with, read as a number of Wernsdorf's on or near the page and not
    before the label of the note before (last).  Of the possible
    readings, the one whose verse (verses) has the first word of the
    note (the lemma) is preferred."""
    m = LABEL.match(text)
    if not m:
        return "?", text, last
    lemma = next((w for w in map(normalize, text[m.end():].split()[:1]) if len(w) >= 4), "")
    ns = []
    for g in (g for g in m.groups() if g):
        fit = [n for n in readings(g) if n in numbers and n >= (ns[-1] if ns else last)]
        if not fit:
            return "?", text, last
        # How well the lemma matches a word of the verse.
        score = {n: max((difflib.SequenceMatcher(None, lemma, w).ratio()
                         for w in verses.get(n, [])), default=0.0) if lemma else 0.0
                 for n in fit}
        best = max(fit, key=lambda n: score[n])
        ns.append(best if score[best] >= 0.6 else fit[0])
    label = "–".join(map(str, ns))
    ll = [to_ll.get(n) for n in ns]
    if ll != ns:
        label += " (LL " + "–".join("?" if v is None else str(v) for v in ll) + ")"
    return label, text[m.end():], ns[0]


def write_text(hocr: str, out: str, numberer: Numberer):
    """Write ilias.md."""
    first, last, printed = TEXT
    counter = itertools.count(1)
    pages = []
    to_ll: dict[int, int] = {}
    verses: dict[int, list[str]] = {}  # Wernsdorf's number -> the words of his verse
    for i, page in enumerate(read_hocr(hocr, first, last)):
        page_no = printed + i
        blocks = body_blocks(page, first + i)
        title, rows = verse_rows(page, blocks, page_no, numberer, counter)
        for n, score, w, text, _ in rows:
            if n:
                to_ll[w] = n
            verses[w] = [normalize(v) for v in BOOK.sub("", text, count=1).split()]
            if n is not None and score < 0.6:
                print(f"p. {page_no}: {n}? ({score:.2f}) {text}", file=sys.stderr)
        pages.append((page_no, first + i, title, rows, columns_of(blocks, page)))
    lines = ["# Lemaire: text and notes", "",
             "Incerti auctoris (vulgo Pindari Thebani) Epitome Iliados Homeri, ed.",
             "J. C. Wernsdorf, reprinted in *Poetae Latini Minores* III (Paris:",
             "Lemaire, 1824), pp. 515–610.  Generated by `src/lemaire.py` from the",
             "OCR; see [README.md](README.md).", ""]
    for page_no, pdf_page, title, rows, columns in pages:
        lines += [f"## p. {page_no}", "", f"PDF page {pdf_page}.", ""]
        if title:
            lines += ["Title: " + escape(" / ".join(title)), ""]
        lines += ["| Verse | Wernsdorf | Text | Printed |", "|---|---|---|---|"]
        for n, score, w, text, right in rows:
            label = "—" if n is None else "?" if not n else f"{n}?" if score < 0.6 else str(n)
            lines.append(f"| {label} | {w} | {escape(md_cell(text))} | {escape(md_cell(right))} |")
        lines.append("")
        # Labels may refer to the verses of the page and a few before.
        ws = [r[2] for r in rows]
        numbers = set(range(min(ws, default=0) - 5, max(ws, default=0) + 3))
        items = column_items(columns)
        if items:
            lines += ["### Notes", ""]
            last = 0
            for item in items:
                if item[0] == "(cont.)":
                    label, text = "(cont.)", join_lines(item[1:])
                else:
                    label, text, last = note_label(join_lines(item), numbers, last, to_ll,
                                                   verses)
                lines.append(f"- **{label}** {escape(text)}")
            lines.append("")
    with open(f"{out}/ilias.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    hocr, latin, out = sys.argv[1:4]
    write_prose(hocr, out, "prooemium.md", "prooemium",
                ["Wernsdorf's prooemium on the *Epitome Iliados*, its author and",
                 "the Latin translators of Homer, *Poetae Latini Minores* III",
                 "(Paris: Lemaire, 1824), pp. 453–507.", ""],
                PROOEMIUM, extra=(TITLE,))
    write_prose(hocr, out, "testimonia.md", "testimonia",
                ["*De Epitome Iliados Homeri ejusque auctore testimonia auctorum ac",
                 "judicia*, *Poetae Latini Minores* III (Paris: Lemaire, 1824),",
                 "pp. 508–514.", ""], TESTIMONIA)
    write_text(hocr, out, Numberer(read_latin_library(latin)))
    write_prose(hocr, out, "excursus.md", "excursus",
                ["Excursus I–IV on the *Epitome Iliados*, *Poetae Latini Minores*",
                 "III (Paris: Lemaire, 1824), pp. 611–620.", ""], EXCURSUS)


if __name__ == "__main__":
    main()
