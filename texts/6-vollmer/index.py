"""Draft INDEX.tsv from Vollmer's index of names.

Usage: python index.py index.md ilias.md > INDEX.tsv

Each entry of index.md is split into the places it cites: a phrase
followed by one or more verse numbers ("magnus -es 860. 995").  A
remark after a colon (": Diomedes") stays with the phrase before it,
and a cross-reference without a verse ("v. Aeacides. Nereius.") is a
row of its own.  For each row the draft gives

- headword: the name the entry is sorted under ("Achilles]", the
  homonym number of "1. Acamas" as "Acamas 1"), as found; it is to be
  put in the nominative by hand;
- verse: the verse numbers without their marks (*, [ ], (?)), a list
  joined by commas without spaces;
- form: for each verse, the word of Vollmer's text (ilias.md) that
  begins with the same letters as the headword;
- description: the phrase as printed, with its verse numbers.

This was run once; INDEX.tsv has been corrected by hand since, so it
is not to be run again.
"""

import re
import sys
from pathlib import Path

PREFIX = 4
ROW = re.compile(r"^\| (\d+) \| [^|]* \| (.*?) \| [^|]* \|$")
NUM = r"\*?\d{1,4}(?:\(\?\))?"
ITEM = rf"(?:\[{NUM}\]|\(\d{{1,4}}\?\)|{NUM}(?:—\d{{1,4}})?)"
GROUP = re.compile(rf"(?<![\w-]){ITEM}(?:\.? {ITEM}(?![\w-]))*(?![\w-])")
# numbers that are not verses: "v. Antenor 1", "Chromius 1"
NOT_VERSE = re.compile(r"[A-Z][a-z]+ $")


def read_entries(path):
    entries = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.startswith("- ") or line.startswith("- *denotat"):
            continue
        text = line[2:]
        if text.startswith("(cont.) "):
            entries[-1] += " " + text[len("(cont.) "):]
        else:
            entries.append(text)
    return entries


def read_verses(path):
    verses = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if m:
            verses.setdefault(m.group(1), m.group(2))
    return verses


def headword(text):
    m = re.match(r"(\d)\. ", text)
    num = m.group(1) if m else ""
    body = text[m.end():] if m else text
    m = re.match(r"[(\[]?([A-Z][a-z]+)(?: [a-z]+)?[)\]]?\]", body)
    if m:
        word = m.group(1)
    else:
        lemma = GROUP.split(body)[0]
        caps = re.findall(r"\*?([A-Z][a-zāēīōūăĕĭŏŭëïü]+)", lemma)
        word = caps[0] if caps else body.split()[0]
    return f"{word} {num}".strip()


def segments(text):
    """Split an entry into (phrase, [verse items]) pairs."""
    out = []
    pos = 0
    for m in GROUP.finditer(text):
        before = text[pos:m.start()]
        if NOT_VERSE.search(before) and re.search(r"v\. [A-Z][a-z]+ $", before):
            continue
        end = m.end()
        rest = text[end:]
        g = re.match(r":.*?(?=\. |; |$)" if rest.startswith(":")
                     else r"\)?", rest)
        end += g.end()
        phrase = text[pos:end].strip(" .;")
        # "v. Aeacides. Nereius. ducis invicti 61": the names are a
        # cross-reference of their own
        x = re.match(r"((?:cf\. |v\. )(?:[A-Z]\w+(?: et [A-Z]\w+)?\. )+)(.+)",
                     phrase)
        if x:
            out.append((x.group(1).strip(), ""))
            phrase = x.group(2)
        out.append((phrase, m.group(0)))
        pos = end
    tail = text[pos:].strip(" .;:")
    if tail:
        out.append((tail, ""))
    return out


def verse_numbers(group):
    nums = []
    for item in re.findall(ITEM, group):
        r = re.search(r"(\d+)—(\d+)", item)
        if r:
            nums.append(f"{r.group(1)}-{r.group(2)}")
        else:
            nums.append(re.search(r"\d+", item).group(0))
    return nums


def form(verses, verse, head, phrase):
    """The word of the verse matching the headword or, for a phrase
    without it ("nati", "pio . . . patri"), the last word of the phrase."""
    first = verse.split("-")[0]
    words = [w[:-3] if w.endswith("que") and len(w) > 6 else w
             for w in re.findall(r"[A-Za-zäëïöüÄËÏÖÜ]+", verses.get(first, ""))]
    plain = re.sub(r"\([^)]*\)|\b(?:v|cf|voc|gen|dat|abl|nom|subst|plur)\.:?",
                   "", phrase)
    keys = [head.split()[0].lower()[:PREFIX]]
    if not re.search(r"(?<!\w)-\w", plain):
        found = [w for w in re.findall(r"[A-Za-zăĕĭŏŭāēīōūë]+", plain)]
        keys += [w.lower()[:PREFIX] for w in reversed(found)]
    for key in keys:
        for w in words:
            if w.lower()[:PREFIX] == key:
                return w
    return ""


def main():
    entries = read_entries(sys.argv[1])
    verses = read_verses(sys.argv[2])
    print("headword\tverse\tform\tdescription")
    for text in entries:
        head = headword(text)
        body = re.sub(r"^\d\. ", "", text)
        body = re.sub(r"^[(\[]?[A-Z][a-z]+(?: [a-z]+)?[)\]]?\] ?", "", body)
        for phrase, group in segments(body):
            nums = verse_numbers(group) if group else []
            forms = [form(verses, n, head, phrase) for n in nums]
            print(f"{head}\t{','.join(nums)}\t{','.join(forms)}\t{phrase}")


if __name__ == "__main__":
    main()
