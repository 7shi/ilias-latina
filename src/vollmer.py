"""Organize Vollmer's edition of the Ilias Latina for reference.

Usage: python vollmer.py VOLLMER.pdf ilias.txt OUTDIR

VOLLMER.pdf is the Internet Archive scan of Poetae Latini Minores II,
fasc. 1-3 (p1poetaelatinimi02baeh), whose text layer is the OCR of the
scan.  ilias.txt is the numbered text of The Latin Library (output of
extract.py); it is used only to number the verses of Vollmer's text.

Writes three Markdown files to OUTDIR, arranged by the printed pages:

- preface.md   the preface and the list of manuscripts (pp. IV-X)
- ilias.md     the text with the margins, the testimonia and the
               apparatus split by verse (pp. 1-55)
- index.md     the index of names (pp. 56-65)

The words are read with their positions (pdftotext -bbox-layout).  On a
text page the verses are the largest lines; the numbers in the left
margin (Iliad book and line) and in the right margin (verse numbers) are
told apart by their position.  The smaller lines below the verses are
the testimonia and the apparatus, separated by a wider gap.

Vollmer prints a verse number only every five verses, and the OCR often
misreads or drops it, so each verse is matched instead with the most
similar verse of The Latin Library near the expected position.  Verses
matched with low similarity are marked with "?" and reported on stderr.

The OCR text is kept as it is.  The script is meant to be run once: the
output is then corrected by hand in place (and committed), so running it
again overwrites the corrections.
"""

import difflib
import html
import re
import subprocess
import sys
from dataclasses import dataclass

# PDF pages (1-based) and the printed page number of their first page.
PREFACE = (152, 158, 4)  # pp. IV-X
TEXT = (159, 213, 1)  # pp. 1-55
INDEX = (214, 223, 56)  # pp. 56-65

# Pages where the notes begin with a row that the matching takes for a
# verse (a note quoting a verse): printed page -> first words of the notes.
NOTES_START = {
    52: "mesto Helmstad.",
}

# Rows whose verse number cannot be found by matching: (printed page,
# first words) -> verse.  Vollmer prints 874 both after 863 (in brackets,
# as most manuscripts) and in its place, and 860 in two parts around a
# lacuna.
VERSE_FIXES = {
    (43, "evolat et Thetis"): 860,
    (44, "quae postquam magnus"): 860,
    (45, "fecerat et liquidas"): 874,
}

ROMAN = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]


@dataclass
class Word:
    x0: float
    y0: float
    x1: float
    y1: float
    text: str

    @property
    def height(self) -> float:
        return self.y1 - self.y0


def read_pages(pdf: str, first: int, last: int) -> list[tuple[float, list[Word]]]:
    """Return (page width, words) for each page from first to last."""
    out = subprocess.run(
        ["pdftotext", "-bbox-layout", "-f", str(first), "-l", str(last), pdf, "-"],
        capture_output=True, text=True, check=True).stdout
    pages = []
    for page in re.finditer(r'<page width="([\d.]+)".*?</page>', out, re.S):
        words = [Word(float(a), float(b), float(c), float(d), html.unescape(t))
                 for a, b, c, d, t in re.findall(
                     r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" '
                     r'yMax="([\d.]+)">([^<]*)</word>', page[0])]
        pages.append((float(page[1]), words))
    return pages


def rows(words: list[Word]) -> list[list[Word]]:
    """Group words into rows by their top edge, each sorted by x."""
    result: list[list[Word]] = []
    for w in sorted(words, key=lambda w: (w.y0, w.x0)):
        if result and abs(result[-1][0].y0 - w.y0) < 3:
            result[-1].append(w)
        else:
            result.append([w])
    return [sorted(r, key=lambda w: w.x0) for r in result]


def join_lines(lines: list[str]) -> str:
    """Join lines, removing hyphens at line ends before a lowercase word."""
    text = ""
    for line in lines:
        line = line.strip()
        if text.endswith("-") and line[:1].islower():
            text = text[:-1] + line
        else:
            text = f"{text} {line}" if text else line
    return text


def normalize(s: str) -> str:
    """Reduce a verse to lowercase letters for comparison."""
    s = s.lower().replace("v", "u").replace("j", "i")
    return re.sub(r"[^a-z]", "", s)


def read_latin_library(path: str) -> dict[int, str]:
    """Return the verses of The Latin Library by number."""
    verses = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            n, text = line.rstrip("\n").split(" ", 1)
            verses[int(n)] = normalize(text)
    return verses


class Numberer:
    """Assign verse numbers by matching with The Latin Library text."""

    def __init__(self, verses: dict[int, str]):
        self.verses = verses
        self.last = 0
        self.used: set[int] = set()

    def peek(self, text: str) -> float:
        """Return how well text matches any verse near the expected one."""
        target = normalize(text)
        return max((difflib.SequenceMatcher(None, target, self.verses[n]).ratio()
                    for n in range(self.last - 10, self.last + 41)
                    if n in self.verses and n not in self.used),
                   default=0.0)

    def number(self, text: str) -> tuple[int, float]:
        """Return the best matching verse near the expected one."""
        target = normalize(text)
        best, score = self.last + 1, -1.0
        for n in range(self.last - 10, self.last + 26):
            if n in self.used or n not in self.verses:
                continue
            r = difflib.SequenceMatcher(None, target, self.verses[n]).ratio()
            # Prefer the expected verse when the scores are close.
            if n == self.last + 1:
                r += 0.05
            if r > score:
                best, score = n, r
        if score < 0.5:
            # Too unlike any verse: leave the count where it is.
            return 0, score
        self.used.add(best)
        # A verse moved backwards (e.g. 597 after 601) does not reset the count.
        if best > self.last:
            self.last = best
        return best, score


NO_SPLIT_BEFORE = {"v.", "V.", "vv.", "post", "ante", "inter", "et", "cf.", "cf",
                   "ad", "vide", "u.", "—", "-", "in", "p.", "ex", "e", "cum", "a",
                   "ab", "usque", "=", "sic", "vs.", "versu", "versum"}


def split_notes(text: str, order: list[int]) -> list[tuple[str, str]]:
    """Split notes into (label, text) at the verse numbers of the page.

    A label is a verse number of the page (or "848/49"), not preceded by a
    word such as "v." or "post" and not before the previous label in the
    order of the verses on the page (597 comes after 601).
    When the same number starts two entries in a row, the first was a
    reference inside a note and is joined to the note before it.  Text
    before the first label continues a note from the previous page.
    """
    tokens = text.split(" ")
    entries: list[tuple[str, list[str]]] = [("", [])]
    pos = {n: i for i, n in enumerate(order)}
    last = -1
    for i, tok in enumerate(tokens):
        prev = tokens[i - 1] if i else ""
        m = re.fullmatch(r"(\d+)(/\d+)?", tok)
        if m and int(m[1]) in pos and prev not in NO_SPLIT_BEFORE \
                and pos[int(m[1])] >= last:
            if entries[-1][0] == tok and len(entries) > 1:
                label, words = entries.pop()
                entries[-1][1].extend([label, *words])
            entries.append((tok, []))
            last = pos[int(m[1])]
        elif tok.startswith("TIT.") and not entries[-1][1]:
            entries[-1] = ("TIT.", [tok[4:].lstrip(":").strip()] if tok[4:] else [])
        else:
            entries[-1][1].append(tok)
    result = []
    for label, words in entries:
        if label or words:
            result.append((label or "(cont.)", " ".join(words).strip(" :")))
    return result


def apparatus_marks(row: list[Word]) -> int:
    """Count the tokens typical of the notes (sigla, numbers, brackets).

    The first two words and the last are skipped, as they may be margin
    numbers.
    """
    count = 0
    for w in row[2:-1]:
        t = w.text
        if re.search(r"[()|\\]|\d", t) or (t.isupper() and 1 < len(t) <= 5) \
                or t in ("om.", "add.", "cett.", "corr.", "ras.", "Sl", "Sl,"):
            count += 1
    return count


def text_page(page: int, width: float, words: list[Word], numberer: Numberer):
    """Return the verses and the notes of a text page."""
    rs = [r for r in rows(words) if r]
    # Drop the running head (page number, BAEBI ITALICI ILIAS).
    rs = [r for r in rs if not any(w.text in ("BAEBI", "ITALICI") for w in r)]
    # The verses come first, then the notes.  The OCR does not tell the
    # sizes apart reliably, so split where the fewest rows are out of
    # place: rows above that match no verse, rows below that match one.
    good = [numberer.peek(" ".join(w.text for w in r)) >= 0.5 and apparatus_marks(r) < 2
            for r in rs]
    # Among equally good places, take the widest gap (the rule).
    def gap(k: int) -> float:
        return rs[k][0].y0 - rs[k - 1][0].y0 if 0 < k < len(rs) else 0.0
    end = min(range(len(rs) + 1),
              key=lambda k: (good[:k].count(False) + good[k:].count(True), -gap(k)))
    if page in NOTES_START:
        end = next(i for i, r in enumerate(rs)
                   if " ".join(w.text for w in r).startswith(NOTES_START[page]))
    body, notes = rs[:end], rs[end:]
    # The left edge of the verses: the most common start of the rows.
    starts = [round(w.x0 / 2) * 2 for r in body for w in r[:3] if w.text[:1].isalpha()
              and len(w.text) > 1]
    left = max(set(starts), key=starts.count) - 1
    verses = []
    for r in body:
        margin = [w for w in r if w.x1 < left + 3 and w.x0 < left - 2]
        right = [w for w in r if w.x0 > width * 0.82]
        main = [w for w in r if w not in margin and w not in right]
        if not main:
            continue
        line = " ".join(w.text for w in main)
        fix = next((v for (p, start), v in VERSE_FIXES.items()
                    if p == page and line.startswith(start)), None)
        n, score = (fix, 1.0) if fix else numberer.number(line)
        verses.append((n, score, " ".join(w.text for w in margin), line,
                       " ".join(w.text for w in right)))
    blocks: list[list[list[Word]]] = []
    if notes:
        gaps = [b[0].y0 - a[0].y0 for a, b in zip(notes, notes[1:])]
        step = sorted(gaps)[len(gaps) // 2] if gaps else 0
        blocks = [[notes[0]]]
        for gap, r in zip(gaps, notes[1:]):
            if gap > step * 1.6:
                blocks.append([r])
            else:
                blocks[-1].append(r)
    notes_text = [join_lines([" ".join(w.text for w in r) for r in b]) for b in blocks]
    return verses, notes_text


def md_cell(s: str) -> str:
    return s.replace("|", "\\|")


def write_text(pdf: str, out: str, numberer: Numberer):
    """Write ilias.md."""
    first, last, printed = TEXT
    lines = ["# Vollmer: text and apparatus", "",
             "Baebi Italici Ilias, ed. F. Vollmer, *Poetae Latini Minores* II 3",
             "(1913), pp. 1–55.  Generated by `src/vollmer.py` from the OCR; see",
             "[README.md](README.md).", ""]
    for i, (width, words) in enumerate(read_pages(pdf, first, last)):
        page = printed + i
        verses, blocks = text_page(page, width, words, numberer)
        order = [n for n, *_ in verses if n]
        lines += [f"## p. {page}", "", f"PDF page {first + i}.", "",
                  "| Verse | Margin | Text | Printed |", "|---|---|---|---|"]
        for n, score, margin, text, right in verses:
            label = "?" if not n else f"{n}?" if score < 0.6 else str(n)
            if score < 0.6:
                print(f"p. {page}: {n}? ({score:.2f}) {text}", file=sys.stderr)
            lines.append(f"| {label} | {md_cell(margin)} | {md_cell(text)} | {md_cell(right)} |")
        lines.append("")
        # The last block is the apparatus; any before it are testimonia.
        for j, block in enumerate(blocks):
            title = "Apparatus" if j == len(blocks) - 1 else "Testimonia"
            lines += [f"### {title}", ""]
            for label, text in split_notes(block, order):
                lines.append(f"- **{label}** {text}")
            lines.append("")
    with open(f"{out}/ilias.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def is_running_head(row: list[Word]) -> bool:
    """Return whether the top row is a running head (title, page number)."""
    return all(re.fullmatch(r"[IVXLC]+|\d+|PRAEFATIO|INDEX|NOMINVM|[^A-Za-z0-9]*", w.text)
               for w in row)


def column_paragraphs(words: list[Word], hanging: bool) -> list[str]:
    """Return the paragraphs of a column of words.

    With hanging=False a paragraph begins with an indented row (the
    preface); with hanging=True it begins with a row at the left edge and
    continues in indented rows (the index).  A footnote ("1) ...") always
    begins a paragraph.
    """
    rs = rows(words)
    if rs and is_running_head(rs[0]):
        rs = rs[1:]
    if not rs:
        return []
    starts = [round(r[0].x0) for r in rs]
    left = min(x for x in starts if starts.count(x) >= 2 or len(rs) < 4)
    paras: list[list[str]] = []
    for r in rs:
        indented = r[0].x0 > left + 3
        text = " ".join(w.text for w in r)
        new = (not indented) if hanging else indented
        if not paras or new or re.match(r"\d\)", text):
            paras.append([text])
        else:
            paras[-1].append(text)
    return [join_lines(p) for p in paras]


def write_preface(pdf: str, out: str):
    """Write preface.md: the preface and the list of manuscripts."""
    first, last, printed = PREFACE
    lines = ["# Vollmer: preface", "",
             "Generated by `src/vollmer.py` from the OCR; see [README.md](README.md).", ""]
    for i, (width, words) in enumerate(read_pages(pdf, first, last)):
        lines += [f"## p. {ROMAN[printed + i]}", "", f"PDF page {first + i}.", ""]
        for para in column_paragraphs(words, hanging=False):
            lines += [para, ""]
    with open(f"{out}/preface.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_index(pdf: str, out: str):
    """Write index.md: the index of names, one entry per line."""
    first, last, printed = INDEX
    lines = ["# Vollmer: index of names", "",
             "Generated by `src/vollmer.py` from the OCR; see [README.md](README.md).", ""]
    for i, (width, words) in enumerate(read_pages(pdf, first, last)):
        lines += [f"## p. {printed + i}", "", f"PDF page {first + i}.", ""]
        mid = width / 2
        for column in ([w for w in words if (w.x0 + w.x1) / 2 < mid],
                       [w for w in words if (w.x0 + w.x1) / 2 >= mid]):
            lines += [f"- {e}" for e in column_paragraphs(column, hanging=True)]
        lines.append("")
    with open(f"{out}/index.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    pdf, latin, out = sys.argv[1:4]
    numberer = Numberer(read_latin_library(latin))
    write_preface(pdf, out)
    write_text(pdf, out, numberer)
    write_index(pdf, out)


if __name__ == "__main__":
    main()
