"""Put the Greek lines of the Iliad beside the verses that follow them.

Usage: python greek.py ILIAD_GRC.xml TEXTS_DIR OUTPUT.md

Divides the verses of The Latin Library (TEXTS_DIR/ilias.txt) into
sections at the verses where Vollmer prints a line of the Iliad in his
margin (TEXTS_DIR/iliad.md) and at the first verse of each book.  Each
verse is followed by the lines it renders (../commentary/alignment.tsv
from this script), and each section by the notes of alignment.tsv, the
notes of the editions that apply to the text (../commentary/commentary-en.tsv)
and the Greek of those lines (ILIAD_GRC.xml, the Perseus TEI of Monro
and Allen), in the order the verses first render them and in runs of
consecutive lines.

The output is for reference in translating and is not committed, as it
quotes the Perseus text.
"""

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

TEI = "{http://www.tei-c.org/ns/1.0}"
REF = re.compile(r"(\d+)\.(\d+)")
DIR = Path(__file__).resolve().parent.parent / "commentary"
ALIGNMENT = DIR / "alignment.tsv"
COMMENTARY = DIR / "commentary-en.tsv"


def read_greek(path: Path) -> dict[tuple[int, int], str]:
    lines = {}
    for div in ET.parse(path).getroot().iter(f"{TEI}div"):
        if div.get("subtype") == "Book":
            for l in div.iter(f"{TEI}l"):
                if (n := l.get("n")) and n.isdigit():
                    lines[int(div.get("n")), int(n)] = " ".join("".join(l.itertext()).split())
    return lines


def read_ll(path: Path) -> list[tuple[int, int, str]]:
    """Return (book, verse, text) for each verse."""
    out, book = [], 0
    for line in path.read_text().splitlines():
        if m := re.match(r"## (\d+)", line):
            book = int(m[1])
        elif m := re.match(r"(\d+) (.*)", line):
            out.append((book, int(m[1]), m[2]))
    return out


def read_margin(path: Path) -> dict[int, list[tuple[int, int]] | None]:
    """Map a verse to its lines of the Iliad, or None for a dash."""
    out = {}
    for line in path.read_text().splitlines():
        c = [s.strip() for s in line.split("|")[1:-1]]
        if len(c) == 4 and c[0].isdigit():
            out[int(c[0])] = None if c[2] == "—" else [
                (int(m[1]), int(m[2])) for m in REF.finditer(c[2])]
    return out


def read_alignment(path: Path) -> dict[int, tuple[str, str]]:
    """Map a verse to its lines of the Iliad and its note."""
    out = {}
    for line in path.read_text().splitlines()[1:]:
        verse, iliad, note = line.split("\t")
        out[int(verse)] = (iliad, note)
    return out


def read_commentary(path: Path) -> dict[int, list[str]]:
    """Map a verse to its notes, without the marks of omission (…)."""
    out: dict[int, list[str]] = {}
    for line in path.read_text().splitlines()[1:]:
        verse, _, note = line.split("\t")
        # A short headword before the first mark keeps a colon after it.
        note = re.sub(r"^([^….:;]{1,40}?) … ", r"\1: ", note)
        note = " ".join(re.sub(r"\s*…\s*", " ", note).split())
        note = re.sub(r" ([.,;:)])", r"\1", note).replace("( ", "(")
        out.setdefault(int(verse), []).append(note)
    return out


def expand(refs: str) -> list[tuple[int, int]]:
    """Turn "1.4–5, 1.11" into [(1, 4), (1, 5), (1, 11)]."""
    out = []
    for m in re.finditer(r"(\d+)\.(\d+)(?:–(\d+))?", refs):
        b, a = int(m[1]), int(m[2])
        out += [(b, k) for k in range(a, int(m[3] or a) + 1)]
    return out


def runs(lines: list[tuple[int, int]]) -> list[list[tuple[int, int]]]:
    """Group lines into runs of consecutive lines of the same book."""
    out: list[list[tuple[int, int]]] = []
    for b, k in lines:
        if out and out[-1][-1] == (b, k - 1):
            out[-1].append((b, k))
        else:
            out.append([(b, k)])
    return out


def main() -> None:
    greek = read_greek(Path(sys.argv[1]))
    texts, output = Path(sys.argv[2]), Path(sys.argv[3])
    verses = read_ll(texts / "ilias.txt")
    margin = read_margin(texts / "iliad.md")
    alignment = read_alignment(ALIGNMENT)
    commentary = read_commentary(COMMENTARY)

    # Sections begin at the verses with lines of the Iliad and at the
    # first verse of each book.
    sections: list[list[tuple[int, int, str]]] = []
    for v in verses:
        if not sections or margin.get(v[1]) or v[0] != sections[-1][0][0]:
            sections.append([])
        sections[-1].append(v)

    lines = [
        "# Ilias Latina with the Greek lines",
        "",
        "Verses of The Latin Library in sections from the lines of the",
        "*Iliad* in Vollmer's margin, as context for translating.  In each",
        "section, <latin> gives the verses with the lines they render",
        "(commentary/alignment.tsv, \"—\" none), <commentary> the notes of the",
        "alignment and of the editions (commentary/commentary-en.tsv), and <greek>",
        "those lines (Monro and Allen, from Perseus, CC BY-SA 4.0), in runs",
        "separated by a blank line.  Generated by src/greek.py; for",
        "reference only, not committed.",
    ]
    book = 0
    for sec in sections:
        if sec[0][0] != book:
            book = sec[0][0]
            lines += ["", f"## Book {book}"]
        seen: list[tuple[int, int]] = []
        for _, v, _ in sec:
            for ref in expand(alignment[v][0]):
                if ref not in seen and ref in greek:
                    seen.append(ref)
        blocks = runs(seen)
        span = ", ".join(f"{g[0][0]}.{g[0][1]}" + (f"–{g[-1][1]}" if len(g) > 1 else "")
                         for g in blocks)
        head = f"{sec[0][1]}–{sec[-1][1]}" if len(sec) > 1 else f"{sec[0][1]}"
        lines += ["", f"### {head}" + (f" (*Iliad* {span})" if span else ""), "", "<latin>"]
        lines += [f"{v} {text} [{alignment[v][0]}]" for _, v, text in sec]
        lines.append("</latin>")
        notes = [f"- {v}: {note}" for _, v, _ in sec
                 for note in [alignment[v][1]] * bool(alignment[v][1]) + commentary.get(v, [])]
        if notes:
            lines += ["<commentary>"] + notes + ["</commentary>"]
        if blocks:
            lines.append("<greek>")
            for i, g in enumerate(blocks):
                lines += [""] * bool(i) + [f"{b}.{k} {greek[b, k]}" for b, k in g]
            lines.append("</greek>")
    output.write_text("\n".join(line.rstrip() for line in lines) + "\n")


if __name__ == "__main__":
    main()
