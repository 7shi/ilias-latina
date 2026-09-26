"""Put the verses and the commentaries of the four editions side by side.

Usage: python commentary.py TEXTS_DIR OUTPUT.md [LANG]

For each row of the verse concordance (TEXTS_DIR/concordance.md), in
the order of The Latin Library, writes the verse of The Latin Library
(TEXTS_DIR/ilias.txt) and then, for each edition, its own number and
text of the verse (from its ilias.md) as an item of a list, with the
items of its COMMENTARY.md on that verse nested under it.

A commentary item is placed at the verse of its label; a label for a
range of verses ("474—482", "242, 243, 244") at its first verse.  The
own numbers of Baehrens, Plessis and Vollmer are converted by the
concordance; Lemaire's labels give the verse of The Latin Library
("(LL n)"), and "(cont.)" goes with the note continued from the
previous page.

With LANG ("en" or "ja"), the items are read from the translations
COMMENTARY-LANG.md instead, and the heading and the explanation are
written in that language; the verses stay in Latin.

The output is derived from the files above and is rebuilt from them;
it is not corrected by hand.
"""

import re
import sys
from pathlib import Path

# (bracketed number, directory, concordance column).
EDITIONS = [
    (2, "2-lemaire", "Wernsdorf"),
    (3, "3-baehrens", "Baehrens"),
    (4, "4-plessis", "Plessis"),
    (6, "6-vollmer", "Vollmer"),
]

CELL = re.compile(r"(?<!\\)\|")
ENTRY = re.compile(r"(?P<own>.*?)(?P<below> below)? ?\(p\. (?P<page>[^)]+)\)$")


def cells(line: str) -> list[str]:
    return [c.strip() for c in CELL.split(line)[1:-1]]


def unescape(s: str) -> str:
    return s.replace("\\|", "|")


def read_ll(path: Path) -> dict[int, str]:
    verses = {}
    for line in path.read_text().splitlines():
        if m := re.match(r"(\d+) (.*)", line):
            verses[int(m[1])] = m[2]
    return verses


def read_concordance(path: Path) -> list[tuple[int, dict]]:
    """Return (book, row) for each verse row; a row maps column to cell."""
    rows, book, header = [], 0, []
    for line in path.read_text().splitlines():
        if m := re.match(r"## Book (\d+)$", line):
            book, header = int(m[1]), []
        elif line.startswith("| LL | Vollmer"):
            header = cells(line)
        elif book and header and line.startswith("|") and not line.startswith("|---"):
            rows.append((book, dict(zip(header, cells(line)))))
    return rows


# Per language: the file of the commentary items, the headings of the
# testimonia in it, the marker for them, and the heading and explanation
# of the output.
LANGS = {
    "": {
        "commentary": "COMMENTARY.md",
        "testimonia": "Testimonia",
        "marker": "(testimonia)",
        "header": [
            "# Commentary",
            "",
            "The verses of the four editions organized in this directory and the",
            "items of their commentaries, verse by verse in the order of The Latin",
            "Library ([ilias.txt](ilias.txt)).  Built by `make commentary` in",
            "this directory ([commentary.py](commentary.py)) from",
            "[concordance.md](concordance.md), the editions' `ilias.md` and their",
            "`COMMENTARY.md`, and rebuilt from them; do not correct it by hand.",
            "Translations: [en](COMMENTARY-en.md), [ja](COMMENTARY-ja.md).",
            "",
            "- Each verse begins with its number and text in The Latin Library",
            "  (LL); \"79a\", \"79b\" are verses that The Latin Library does not have,",
            "  placed after the verse that precedes them in the editions.",
            "- Then, as a list, each edition, [2] Lemaire (Wernsdorf's numbers),",
            "  [3] Baehrens, [4] Plessis and [6] Vollmer, with its own number and text",
            "  of the verse as in the concordance (\"[n]\" a verse the edition",
            "  brackets, \"below\" one Plessis prints below the text, \"—\" none),",
            "  and the items of its COMMENTARY.md on the verse nested under it.",
            "- An item keeps its label only where the label is more than the",
            "  number of the verse given above it: a range of verses, whose item",
            "  is given at the first of them, or Lemaire's \"(cont.)\", a note",
            "  continued from the previous page.  Vollmer's testimonia are marked",
            "  \"(testimonia)\".",
            "- The texts and the items are quoted as they stand in the files;",
            "  see each edition's COMMENTARY.md for what is kept and left out.",
        ],
    },
    "en": {
        "commentary": "COMMENTARY-en.md",
        "testimonia": "Testimonia",
        "marker": "(testimonia)",
        "header": [
            "# Commentary",
            "",
            "English translation of [COMMENTARY.md](COMMENTARY.md): the verses of",
            "the four editions organized in this directory and the items of their",
            "commentaries in English, verse by verse in the order of The Latin",
            "Library ([ilias.txt](ilias.txt)).  Built by `make commentary` in",
            "this directory ([commentary.py](commentary.py)) from",
            "[concordance.md](concordance.md), the editions' `ilias.md` and their",
            "`COMMENTARY-en.md`, and rebuilt from them; do not correct it by hand.",
            "",
            "- Each verse begins with its number and text in The Latin Library",
            "  (LL); \"79a\", \"79b\" are verses that The Latin Library does not have,",
            "  placed after the verse that precedes them in the editions.",
            "- Then, as a list, each edition, [2] Lemaire (Wernsdorf's numbers),",
            "  [3] Baehrens, [4] Plessis and [6] Vollmer, with its own number and text",
            "  of the verse as in the concordance (\"[n]\" a verse the edition",
            "  brackets, \"below\" one Plessis prints below the text, \"—\" none),",
            "  and the items of its COMMENTARY-en.md on the verse nested under it.",
            "  The verses are in Latin.",
            "- An item keeps its label only where the label is more than the",
            "  number of the verse given above it: a range of verses, whose item",
            "  is given at the first of them, or Lemaire's \"(cont.)\", a note",
            "  continued from the previous page.  Vollmer's testimonia are marked",
            "  \"(testimonia)\".",
            "- The texts and the items are quoted as they stand in the files;",
            "  see each edition's COMMENTARY-en.md for what is kept and left out.",
        ],
    },
    "ja": {
        "commentary": "COMMENTARY-ja.md",
        "testimonia": "証言",
        "marker": "（証言）",
        "header": [
            "# 注解",
            "",
            "[COMMENTARY.md](COMMENTARY.md) の日本語訳。このディレクトリで整理した4つの版の詩行と、各版の注解の項目の日本語訳を、The Latin Library（[ilias.txt](ilias.txt)）の順に詩行ごとに並べる。このディレクトリの `make commentary`（[commentary.py](commentary.py)）が [concordance.md](concordance.md)、各版の `ilias.md` と `COMMENTARY-ja.md` から生成し、それらが変わると作り直す。手で修正しないこと。",
            "",
            "- 各詩行は The Latin Library（LL）の行番号と本文で始まる。「79a」「79b」は The Latin Library にない詩行で、各版でその前にある詩行の後に置く。",
            "- 続いて各版、[2] Lemaire（ヴェルンスドルフの行番号）、[3] Baehrens、[4] Plessis、[6] Vollmer を箇条書きにし、対照表のとおりにその版の行番号と本文を示す（「[n]」はその版が括弧に入れる詩行、「below」はプレシが本文の下に印刷する詩行、「—」は該当なし）。その下の入れ子にその版の COMMENTARY-ja.md のうち、その詩行の項目を置く。詩行はラテン語のまま。",
            "- 項目のラベルは、上に示した詩行の番号以上の情報がある場合に限って残す。すなわち詩行の範囲（項目はその最初の詩行に置く）と、前の頁から続く Lemaire の注「(cont.)」である。フォルマーの証言には「（証言）」と記す。",
            "- 本文と項目は各ファイルにあるとおりに引く。何を残し何を省いたかは各版の COMMENTARY-ja.md を参照。",
        ],
    },
}

def read_verses(path: Path) -> dict[tuple, list[str]]:
    """Map (LL verse or None, page, below) to the texts, in order."""
    out, page, section, header = {}, "", "", []
    for line in path.read_text().splitlines():
        if m := re.match(r"## p\. (\S+)", line):
            page, section, header = m[1], "text", []
        elif line.startswith("### "):
            section, header = line[4:], []
        elif line.startswith("| Verse "):
            header = cells(line)
        elif line.startswith("|") and header and not line.startswith("|---"):
            if section not in ("text", "Below the text"):
                continue
            c = dict(zip(header, cells(line)))
            verse = None if c["Verse"] == "—" else int(c["Verse"])
            key = (verse, page, section == "Below the text")
            out.setdefault(key, []).append(unescape(c["Text"]))
    return out


def read_commentary(path: Path) -> list[tuple[str, str, str, str]]:
    """Return (page, section, label, text) for each item."""
    items, page, section = [], "", ""
    for line in path.read_text().splitlines():
        if m := re.match(r"## p\. (\S+)", line):
            page, section = m[1], ""
        elif line.startswith("### "):
            section = line[4:]
        elif m := re.match(r"- \*\*(.+?)\*\* ?(.*)$", line):
            items.append((page, section, m[1], m[2]))
    return items


def last_labels(path: Path) -> dict[str, str]:
    """Map each page of Lemaire's ilias.md to the last note label before
    the end of it, for the notes continued on the next page."""
    out, page, last, notes = {}, "", "", False
    for line in path.read_text().splitlines():
        if m := re.match(r"## p\. (\S+)", line):
            page, notes = m[1], False
        elif line.startswith("### "):
            notes = line == "### Notes"
        elif notes and (m := re.match(r"- \*\*(.+?)\*\*", line)):
            if m[1] != "(cont.)":
                last = m[1]
        out[page] = last
    return out


def main() -> None:
    texts, output = Path(sys.argv[1]), Path(sys.argv[2])
    lang = LANGS[sys.argv[3] if len(sys.argv) > 3 else ""]
    ll = read_ll(texts / "ilias.txt")
    rows = read_concordance(texts / "concordance.md")

    # The entries of each edition per row, and its own numbers -> row.
    entries: list[dict[int, list[tuple[str, str]]]] = [{} for _ in rows]
    own_row: dict[tuple[int, str], int] = {}
    ll_row: dict[int, int] = {}
    for num, d, col in EDITIONS:
        verses = read_verses(texts / d / "ilias.md")
        for i, (_, row) in enumerate(rows):
            verse = None if row["LL"] == "—" else int(row["LL"])
            if verse is not None:
                ll_row.setdefault(verse, i)
            out = []
            if row[col] != "—":
                for e in row[col].split("; "):
                    m = ENTRY.match(e)
                    own = m["own"].strip()
                    key = (verse, m["page"], bool(m["below"]))
                    if not verses.get(key):
                        # A verse that ilias.md does not number ("863 bis").
                        key = (None,) + key[1:]
                    text = verses[key].pop(0) if verses.get(key) else ""
                    label = own + (" below" if m["below"] else "")
                    out.append((label or "—", text))
                    bare = own.strip("[]")
                    if bare:
                        own_row.setdefault((num, bare), i)
            entries[i][num] = out

    # The commentary items per row and edition.
    notes: list[dict[int, list[str]]] = [{} for _ in rows]
    for num, d, col in EDITIONS:
        items = read_commentary(texts / d / lang["commentary"])
        cont = last_labels(texts / d / "ilias.md") if num == 2 else {}
        pages = list(cont)
        for page, section, label, text in items:
            if num == 2:
                ref = label
                if label == "(cont.)":
                    ref = cont[pages[pages.index(page) - 1]]
                m = re.match(r"(\d+)(?: \(LL (\d+|—)\))?", ref)
                if m[2] == "—":
                    i = own_row[(num, m[1])]
                else:
                    i = ll_row[int(m[2] or m[1])]
            else:
                n = re.search(r"\d+", label)[0]
                i = own_row.get((num, n))
                if i is None:
                    i = ll_row[int(n)]
            # The label is left out where it is only the number of the
            # verse given above ("1075 (LL 1070)", "474").
            owns = {l.removesuffix(" below").strip("[]")
                    for l, _ in entries[i][num]}
            head = [] if re.sub(r" \(LL .*\)$", "", label) in owns else [f"**{label}**"]
            if section == lang["testimonia"]:
                head.append(lang["marker"])
            notes[i].setdefault(num, []).append(" ".join(["-"] + head + [text]))

    lines = list(lang["header"])
    book = last = extra = 0
    for i, (b, row) in enumerate(rows):
        if b != book:
            book = b
            lines += ["", f"## Book {book}"]
        if row["LL"] == "—":
            # Numbered "79a", "79b" after the verse of The Latin Library.
            extra += 1
            lines += ["", f"{last}{'abcdefgh'[extra - 1]}"]
        else:
            last, extra = int(row["LL"]), 0
            lines += ["", f"{last} {ll[last]}"]
        # Each edition is an item of a list, its commentary items nested
        # under it; "[2]" rather than "2." keeps Markdown from renumbering.
        for num, d, col in EDITIONS:
            for label, text in entries[i][num] or [("—", "")]:
                if label == "—" and not text:
                    lines.append(f"- [{num}] —")
                else:
                    lines.append(f"- [{num}] {label} {text}".rstrip())
            lines += ["  " + n for n in notes[i].get(num, [])]
    output.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
