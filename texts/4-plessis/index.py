"""Draft INDEX.tsv from Plessis's index of names and subjects.

Usage: python index.py index.md INDEX.tsv

Reads the index (index.md, one entry per line) and writes a row for
each place it cites: the headword, the verse and the description.

- The headword is the word in capitals that begins an entry; the lines
  after it (other forms and names of the same person) belong to it.
  Homonyms, introduced by a line such as "ACAMAS Antenoris filius.",
  keep that description in the headword.
- The verse is written in full: "205-6" becomes "205-206", "245 bis"
  "245bis", and "895 sqq." "895-899"; places cited together ("248 et
  520") share one row as "248, 520".  A cross-reference has no verse.
- The description is the text before the verse as printed, with the
  dash (—) standing for the form last named; brackets are closed
  within the row.
- An entry broken across pages is joined.

This was run once; INDEX.tsv has been corrected by hand since, so it
is not to be regenerated.
"""

import re
import sys
from pathlib import Path

HEAD = re.compile(r"^\[?([A-Z]{2,})\b\.?\s*")
NUM = r"\d+(?:-\d+)?(?: bis)?(?: sqq\.)?"
CITE = re.compile(rf"(?<![\w-])({NUM}(?:(?: et |, ){NUM})*)(?![\w-])")
SQQ = {"895": "895-899"}


def read_items(src):
    """Return the entries, joining one broken across pages."""
    items = []
    page_break = False
    for line in src.splitlines():
        if line.startswith("## p."):
            page_break = True
        if not line.startswith("- "):
            continue
        text = line[2:].strip()
        joined = page_break and items and not re.search(r"[.\]>]$", items[-1])
        page_break = False
        if joined:
            prev = items[-1]
            items[-1] = prev[:-1] + text if prev.endswith("-") else prev + " " + text
        else:
            items.append(text)
    return items


def norm(n):
    if n.endswith(" sqq."):
        return SQQ[n[:-5]]
    if n.endswith(" bis"):
        return n[:-4] + "bis"
    m = re.fullmatch(r"(\d+)-(\d+)", n)
    if m:
        lo, hi = m.groups()
        return f"{lo}-{lo[:len(lo) - len(hi)] + hi}"
    return n


def balance(s):
    for o, c in "[]", "<>", "()":
        if s.count(o) > s.count(c):
            s += c
        elif s.count(c) > s.count(o):
            s = o + s
    return s


def clean(s):
    s = s.strip()
    s = re.sub(r"^[;.,]\s*", "", s)
    s = re.sub(r"\s*[;,]$", "", s)
    s = re.sub(r"\[\s+—", "[—", s)
    return balance(s.strip())


def rows_of(items):
    rows = []
    head = None
    for text in items:
        m = HEAD.match(text)
        if m:
            head = m.group(1)
            rest = text[m.end():]
            if text.startswith("["):
                # "[PELOPEA] cf. Grai.": keep the bracketed word as printed.
                rest = text if rest.startswith("]") else "[" + rest
            # A line like "ACAMAS Antenoris filius." names one of homonyms.
            if rest and not re.search(r"\d", rest) and "cf." not in rest:
                head = f"{head} {rest.rstrip('.')}"
                continue
            if not rest:
                continue
            text = rest
        pos = 0
        for c in CITE.finditer(text):
            desc = text[pos:c.start()]
            verses = ", ".join(norm(v) for v in re.split(r" et |, ", c.group(1)))
            pos = c.end()
            # A bracket closed after the verse belongs to this row.
            close = re.match(r"[;.\s]*[\]>)]+", text[pos:])
            if close:
                desc = desc.rstrip() + re.sub(r"[;.\s]", "", close.group())
                pos += close.end()
            rows.append((head, verses, clean(desc)))
        for tail in text[pos:].split("; "):
            if clean(tail):
                rows.append((head, "", clean(tail)))
    return rows


def main():
    src = Path(sys.argv[1]).read_text(encoding="utf-8")
    rows = rows_of(read_items(src))
    out = ["headword\tverse\tdescription"] + ["\t".join(r) for r in rows]
    Path(sys.argv[2]).write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
