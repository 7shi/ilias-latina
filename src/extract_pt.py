"""Extract the numbered verse translation from the Portuguese edition PDF.

Usage: python extract_pt.py [-v] BOOK.pdf OUTPUT.txt

With -v, the continuation lines chosen in each segment are printed to
stderr for review.

The PDF (Bébio Itálico, A Ilíada Latina, translated by Priscilla A. F.
Almeida, Coimbra University Press, 2021) translates the poem line by line,
following the critical edition of Scaffai (1997).  Output has one verse
per line in the form "LABEL TEXT", in the order printed in the book.

How the PDF is read:

1. "pdftotext -bbox-layout" (poppler-utils) gives the position and size of
   every word on pages FIRST_PAGE-LAST_PAGE.
2. Words are classified by height: verse text is about 13.2pt high, while
   footnotes, page numbers and superscript note numbers are smaller and
   are dropped.  Running heads and "Canto N" headings are dropped by text.
3. Numbers in the right margin (x > MARGIN_X) are verse numbers.  They are
   printed every five verses, on the physical line where that verse ends,
   and are attached to the verse line at the same height.
4. Verses too long for the page wrap onto the next line without any
   indentation, so wrapped lines cannot be told apart by position.  The
   margin numbers are used as anchors instead: between two anchors the
   number of verses is known, and the shortest lines are taken as
   continuation lines.  Other criteria were tried and rejected: a capital
   letter fails on proper names, and whether the first word would have
   fitted on the previous line fails because the typesetter does not
   break lines greedily.
5. The few cases the heuristic gets wrong are fixed by hand in
   MARKER_FIXES, STARTS and CONTINUATIONS.  Use -v to review the choices
   and compare the result with the Latin text (see parallel.py).

The verse labels follow the edition (see verse_labels): 791 is absent,
827a is added, and 597 is printed after 601.
"""

import re
import subprocess
import sys

from bs4 import BeautifulSoup

FIRST_PAGE = 93  # "Canto 1" (printed page 91)
LAST_PAGE = 151  # printed page 149

VERSE_HEIGHT = 12.8  # verse lines are ~13.2pt high, footnotes ~11.4pt
MARGIN_X = 272  # verse numbers start right of this
HEADERS = {"A Ilíada Latina", "Bébio Itálico"}
MARKER = re.compile(r"^\d+a?$")
DEBUG = False

# Margin numbers printed one line off: (printed, line prefix) -> corrected.
MARKER_FIXES = {
    ("75", "se não lhe restituísse"): "76",
}

# Manual corrections of the guess made by split_verses().
STARTS = (  # lines that start a verse although they are short
    "[Fizera também,",
)
CONTINUATIONS = (  # lines that continue the previous verse
    "teucros, é menos violento",
    "maravilhosamente, as líquidas",
    "Nereu cingido ao redor;",
)


def verse_labels() -> list[str]:
    """Verse labels in the order printed by the edition (Scaffai 1997)."""
    labels = []
    for n in range(1, 1071):
        if n in (597, 791):  # 597 is moved after 601; 791 is absent
            continue
        labels.append(str(n))
        if n == 601:
            labels.append("597")
        if n == 827:
            labels.append("827a")
    return labels


def read_lines(pdf: str) -> list[dict]:
    """Return the physical verse lines of the translation in reading order.

    Each line is a dict with "text", "width" (in points, including
    superscript note numbers, which take space on the line) and "label"
    (the margin verse number printed on that line, or None).
    """
    xml = subprocess.run(
        ["pdftotext", "-f", str(FIRST_PAGE), "-l", str(LAST_PAGE),
         "-bbox-layout", pdf, "-"],
        capture_output=True, text=True, check=True).stdout
    soup = BeautifulSoup(xml, "html.parser")
    result = []
    for page in soup.find_all("page"):
        texts = {}
        markers = {}
        for line in page.find_all("line"):
            y = round(float(line["ymin"]))
            words = []
            right = 0.0
            for w in line.find_all("word"):
                h = float(w["ymax"]) - float(w["ymin"])
                if h < VERSE_HEIGHT:
                    if words:  # superscript note number: still takes space
                        right = max(right, float(w["xmax"]))
                    continue  # footnote text, page number
                if float(w["xmin"]) > MARGIN_X and MARKER.match(w.text):
                    markers[y] = w.text
                    continue
                words.append((float(w["xmin"]), float(w["xmax"]), w.text))
                right = max(right, float(w["xmax"]))
            if not words:
                continue
            # Removing superscript note numbers can leave "word ,".
            text = re.sub(r" (?=[,;:.!?»])", "",
                          " ".join(t for _, _, t in words))
            if text in HEADERS or text.startswith("Bébio Itálico –"):
                continue
            if text.startswith("Canto "):
                continue
            texts[y] = (text, right - words[0][0])
        for y in sorted(texts):
            text, width = texts[y]
            label = next((markers[k] for k in markers if abs(k - y) <= 1),
                         None)
            for (printed, prefix), fixed in MARKER_FIXES.items():
                if label == printed and text.startswith(prefix):
                    label = fixed
            result.append({"text": text, "width": width, "label": label})
    return result


def split_verses(lines: list[dict]) -> list[tuple[str, str]]:
    """Join physical lines into verses and return them as (label, text).

    The lines between two labelled lines hold a known number of verses;
    the first line always starts a verse, and among the others the widest
    ones start verses while the rest are joined to the previous verse.  If
    there are fewer lines than verses, a warning is printed and the labels
    at the start of the segment are skipped.
    """
    labels = verse_labels()
    index = {label: i for i, label in enumerate(labels)}
    anchors = [(i, index[line["label"]]) for i, line in enumerate(lines)
               if line["label"]]
    if anchors[-1][1] != len(labels) - 1:
        anchors.append((len(lines) - 1, len(labels) - 1))
    verses = []
    prev_line, prev_verse = -1, -1
    for end_line, end_verse in anchors:
        seg = list(range(prev_line + 1, end_line + 1))
        count = end_verse - prev_verse
        if count > len(seg):
            print(f"warning: {count} verses in {len(seg)} lines before "
                  f"{labels[end_verse]}", file=sys.stderr)
            count = len(seg)
        # The first line always starts a verse; the widest of the remaining
        # lines are taken as the other verse starts, the shortest ones as
        # continuations.  STARTS and CONTINUATIONS override the guess.
        ranked = sorted(seg[1:], key=lambda k: (
            lines[k]["text"].startswith(STARTS),
            not lines[k]["text"].startswith(CONTINUATIONS),
            lines[k]["width"]), reverse=True)
        starts = {seg[0]} | set(ranked[:count - 1])
        if DEBUG and count < len(seg):
            conts = [k for k in seg if k not in starts]
            print(f"{labels[end_verse]:>5}: "
                  f"cont {max(lines[k]['width'] for k in conts):5.1f} / "
                  f"start {min(lines[k]['width'] for k in starts):5.1f} "
                  f"{[lines[k]['text'] for k in conts]}", file=sys.stderr)
        texts = []
        for k in seg:
            if k in starts:
                texts.append(lines[k]["text"])
            else:
                texts[-1] += " " + lines[k]["text"]
        first = end_verse - len(texts) + 1
        for n, text in enumerate(texts):
            verses.append((labels[first + n], text))
        prev_line, prev_verse = end_line, end_verse
    return verses


def main():
    """Parse the arguments and write the numbered translation."""
    global DEBUG
    DEBUG = "-v" in sys.argv
    pdf, dst = [a for a in sys.argv[1:] if a != "-v"]
    verses = split_verses(read_lines(pdf))
    with open(dst, "w", encoding="utf-8") as f:
        for label, text in verses:
            print(label, text, file=f)


if __name__ == "__main__":
    main()
