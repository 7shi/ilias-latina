"""Add the form in the verse to INDEX.tsv as its third column.

Usage: python index_forms.py ilias.md INDEX.tsv

For each row with a verse, looks in Plessis's text of that verse
(ilias.md) for the word that the row cites, by matching the first
letters of a key: for a description with a dash, the form found for
the row before under the same headword; otherwise the first word of
the description; and then the headword.  The first key that
matches one word only gives the form, without an enclitic -que; the
rows left empty are printed with their candidates, to be filled in by
hand.

This was run once; INDEX.tsv has been corrected by hand since, so it
is not to be run again.
"""

import re
import sys
from pathlib import Path

PREFIX = 4
ROW = re.compile(r"^\| (\d+|—) \| (.*?) \| (.*?) \|$")


def read_verses(path):
    verses = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if not m:
            continue
        num, text, printed = m.groups()
        if num == "—":
            b = re.fullmatch(r"\[(\d+) bis\]", printed)
            if not b:
                continue
            num = b.group(1) + "bis"
        verses.setdefault(num, text.replace("\\<", "<"))
    return verses


def expand(verse):
    m = re.fullmatch(r"(\d+)-(\d+)", verse)
    if m:
        return [str(n) for n in range(int(m.group(1)), int(m.group(2)) + 1)]
    return [verse]


def words(text):
    return re.findall(r"[A-Za-zÀ-ÿ]+", text)


def key(w):
    return w.lower()[:PREFIX]


def strip_que(w):
    return w[:-3] if w.endswith("que") and len(w) > 6 else w


def candidates(text, k):
    found = []
    for w in map(strip_que, words(text)):
        if key(w) == k and w not in found:
            found.append(w)
    return found


def find(text, keys):
    """Return the candidates for the first key that matches."""
    for k in keys:
        found = candidates(text, k)
        if found:
            return found
    return []


def main():
    verses = read_verses(sys.argv[1])
    path = Path(sys.argv[2])
    lines = path.read_text(encoding="utf-8").splitlines()
    out = ["headword\tverse\tform\tdescription"]
    prev_head, prev_form = None, None
    for line in lines[1:]:
        head, verse, desc = line.split("\t")
        if head != prev_head:
            prev_head, prev_form = head, None
        forms = []
        if verse:
            keys = []
            if "—" in desc:
                if prev_form:
                    keys.append(key(prev_form))
            else:
                first = words(desc)[:1]
                if first and first[0][0].isupper():
                    keys.append(key(first[0]))
            keys.append(key(head.split()[0]))
            for v in verse.split(", "):
                text = " ".join(verses.get(n, "") for n in expand(v))
                found = find(text, keys)
                forms.append(found[0] if len(found) == 1 else "")
                if len(found) != 1:
                    print(f"{head}\t{v}\t{found}\t{desc}")
        form = ", ".join(forms) if all(forms) else ""
        if form:
            prev_form = forms[-1]
        out.append("\t".join((head, verse, form, desc)))
    path.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
