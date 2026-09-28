"""Draft INDEX-en.tsv and INDEX-ja.tsv from the translations of an index.

Usage: python index_translations.py DIR

DIR is 4-plessis or 6-vollmer.  Reads DIR/INDEX.tsv, DIR/index.md and
its translations DIR/index-{en,ja}.md, and writes DIR/INDEX-{en,ja}.tsv
with the rows, headword, verse and form of INDEX.tsv and the
description cut from the translation.

The translations have the same entries, line for line, as index.md, and
the same verse numbers in each entry.  The numbers are the anchors:

- the rows of INDEX.tsv are assigned to the entries of index.md by
  their verses (a cross-reference without a verse by its text);
- an entry is cut after the last number of each row, up to the
  separator that follows it (". ", "; ", "。" ...), in index.md and in
  the translation alike;
- the words in front of the first row that INDEX.tsv leaves out (the
  headword, "Achilles]", "1.") are left out of the translation too.

The cut is repeated on index.md and compared with INDEX.tsv; the rows
where they differ, and those that could not be cut, are listed on
stderr for checking by hand.

A second column, headword-en or headword-ja, gives the headword as the
translation renders it where the translation has it (Plessis: the
Japanese reading and the homonyms); the rest is filled by hand.

This was run once; the TSV files have been corrected by hand since, so
it is not to be run again.
"""

import re
import sys
from pathlib import Path

NUM = re.compile(r"(?<![A-Za-z0-9_\-–—])\d{1,4}(?!\d)")
SEP = re.compile(r"\.\s+|;\s*|；\s*|。\s*|[:：]\s*(?=—)|\.$|$")


def entries(path):
    """The lines of the entries, with the page they are on."""
    out = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("- "):
            out.append(line[2:])
    return out


def read_pages(path):
    pages = []
    page = None
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("## p."):
            page = line
        if line.startswith("- "):
            pages.append(page)
    return pages


def join_texts(parts):
    text = ""
    for p in parts:
        p = re.sub(r"^\(cont\.\) ", "", p)
        if not text:
            text = p
        elif re.search(r"[^\x00-\u2fff]$", text):
            text += p
        elif text.endswith("-") and not text.endswith(" -"):
            text = text[:-1] + p
        else:
            text += " " + p
    return text


def tokens(text):
    return [(m.group(), m.start(), m.end()) for m in NUM.finditer(text)]


def verse_nums(verse):
    return [re.match(r"\d+", v).group() for v in verse.split(",")] if verse else []


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


TAIL = re.compile(r"(?:\s*[-–—]\d+)?(?: bis| sqq\.| ff\.| 以下)?")
CLOSE = re.compile(r"[\s;.。；]*[\]>)）]+")
PUNCT = re.compile(r"\s*[;；:：,，、.。]?\s*")
SEP = re.compile(r"\.\s+|;\s*|；\s*|。\s*|\.$|$")


ABBR = re.compile(r"\b(?:v|f|cf|sp|trad|loq|voc|fr|ff)$")


def sep(text, pos):
    """The first separator after pos that does not end an abbreviation."""
    for m in SEP.finditer(text, pos):
        if not (m.group().startswith(".") and ABBR.search(text, 0, m.start())):
            return m


def cut(text, rows, spans, plessis):
    """Cut an entry into the descriptions of its rows."""
    toks = tokens(text)
    out = []
    pos = 0
    for n, (r, sp) in enumerate(zip(rows, spans)):
        if sp:
            k, last = sp
            if plessis:
                desc = text[pos:toks[k][1]].rstrip(" ,、")
                after = TAIL.match(text, toks[last][2]).end()
                m = CLOSE.match(text, after)
                if m:
                    desc += re.sub(r"[\s;.。；]", "", m.group())
                    after = m.end()
                pos = PUNCT.match(text, after).end()
            else:
                after = toks[last][2]
                if re.search(r"\d[\])]*$", r[3]):
                    # the row ends at the number ("Lucifer 868: v. Hesperus")
                    # "arte paterna 350 を参照": the reference goes with it
                    m = re.compile(r"[\])]*(?:\s*を参照)?").match(text, after)
                    desc = text[pos:m.end()]
                    pos = re.compile(r"[\s.:：;；。]*").match(text, m.end()).end()
                else:
                    m = sep(text, after)
                    desc = text[pos:m.start()]
                    pos = m.end()
        else:
            nxt = next((s for s in spans[n + 1:] if s), None)
            refs_after = sum(1 for s in spans[n + 1:] if not s)
            if nxt:
                seg = text[pos:toks[nxt[0]][1]]
                word = r[3].rstrip(".").split()[-1].strip("[]()")
                q = seg.rfind(word)
                end = len(seg)
                if q >= 0:
                    m = re.match(r"[^.;。；]*?(?:を参照)?[.;。；]\s*", seg[q:])
                    end = q + (m.end() if m else len(word))
                desc = seg[:end]
                pos += end
            elif refs_after:
                m = re.search(r";\s*|；\s*", text[pos:])
                end = m.start() if m else len(text) - pos
                desc = text[pos:pos + end]
                pos += m.end() if m else end
            else:
                desc = text[pos:]
                pos = len(text)
        out.append(norm(desc))
    return out


def finish(seg, lat_seg, desc):
    """Leave out what INDEX.tsv leaves out in front, and the separator
    at the end unless the row keeps it."""
    q = lat_seg.find(desc)
    if q > 0:
        pre = lat_seg[:q]
        head = pre.split()[0].rstrip(",:")
        if seg.startswith(head):
            seg = seg[len(head):]
            seg = re.sub(r"^\([^)]*\)", "", seg)
            seg = seg.lstrip(" ,、:：")
        if pre.rstrip().endswith(":"):
            m = re.match(r"[^:：]*[:：]\s*", seg)
            if m:
                seg = seg[m.end():]
    if not desc.endswith("."):
        seg = seg.rstrip(" ;,.。；、")
    seg = seg.rstrip("。")
    seg = re.sub(r"\[\s+—", "[—", seg)
    return seg.strip()


REF = re.compile(r"(?:^|\s)(?:v|cf)\.\s")


def move_refs(out, rows, idx):
    """Vollmer: "cf. patri 23. patrem 42. ... vatis 44" is translated
    "patri 23. patrem 42. ... vatis 44 を参照"; the reference goes to
    the row that begins it, as "cf." does in the Latin."""
    for n, i in enumerate(idx):
        if not REF.search(rows[i][3]) or "を参照" in out[i]:
            continue
        for j in idx[n + 1:]:
            if REF.search(rows[j][3]):
                break
            if out[j].endswith(" を参照"):
                out[j] = out[j][:-len(" を参照")]
                out[i] = out[i].rstrip(".") + " を参照"
                break


def headwords(rows, lat, tr):
    """Plessis: the headwords as the translation renders them, from the
    line that begins the entry: the reading in brackets in the Japanese
    ("ABAS(アバース)"), and the description of a homonym in both
    ("ACAMAS, son of Antenor", "ACAMAS(アカマース)、アンテーノールの子")."""
    out = {}
    for hw in dict.fromkeys(r[0] for r in rows):
        i = next((i for i, t in enumerate(lat)
                  if re.match(r"\[?" + re.escape(hw) + r"(?![A-Za-z])", t)),
                 None)
        if i is None:
            continue
        name, _, rest = hw.partition(" ")
        m = re.match(r"\[?" + name + r"\]?(?:\(([^)]*)\))?", tr[i])
        head = m.group(1) or ""
        if rest:
            desc = re.sub(r"^\s*[,、]\s*", "", tr[i][m.end():]).rstrip(".。")
            if head:
                head += "、" + desc
            else:
                head = name.capitalize() + ", " + desc
        out[hw] = head
    return out


def main():
    d = Path(sys.argv[1])
    plessis = "plessis" in d.name
    rows = [l.split("\t") for l in
            (d / "INDEX.tsv").read_text(encoding="utf-8").splitlines()[1:]]
    lat = entries(d / "index.md")
    tr = {lang: entries(d / f"index-{lang}.md") for lang in ("en", "ja")}
    assert all(len(t) == len(lat) for t in tr.values())
    pages = read_pages(d / "index.md")
    groups = []
    for i, t in enumerate(lat):
        if t.startswith("*denotat"):
            continue
        if plessis:
            joined = (groups and pages[i] != pages[groups[-1][-1]]
                      and not re.search(r"[.\]>]$", lat[groups[-1][-1]]))
        else:
            joined = t.startswith("(cont.) ")
        if joined:
            groups[-1].append(i)
        else:
            groups.append([i])
    L = [join_texts([lat[i] for i in g]) for g in groups]
    T = {lang: [join_texts([t[i] for i in g]) for g in groups]
         for lang, t in tr.items()}

    # assign the rows to the entries by their verses, or by their text
    assign = []
    g, p = 0, 0
    for r in rows:
        nums = verse_nums(r[1])
        while True:
            toks = tokens(L[g])
            if nums:
                k = next((j for j in range(p, len(toks))
                          if toks[j][0] == nums[0]), None)
                if k is not None:
                    last = k
                    for n in nums[1:]:
                        last = next(j for j in range(last + 1, len(toks))
                                    if toks[j][0] == n)
                    assign.append((g, (k, last)))
                    p = last + 1
                    break
            else:
                start = toks[p - 1][2] if p else 0
                ref = re.escape(r[3].rstrip(".")) + r"(?![,\w])"
                if re.search(ref, L[g][start:]):
                    assign.append((g, None))
                    break
            g, p = g + 1, 0

    out = {lang: [""] * len(rows) for lang in tr}
    report = []
    for g in range(len(L)):
        idx = [i for i, a in enumerate(assign) if a[0] == g]
        if not idx:
            continue
        erows = [rows[i] for i in idx]
        spans = [assign[i][1] for i in idx]
        lat_cut = cut(L[g], erows, spans, plessis)
        for i, lc in zip(idx, lat_cut):
            if finish(lc, lc, rows[i][3]) != rows[i][3]:
                report.append(f"{i + 2}: la {lc!r}")
        for lang in tr:
            t = T[lang][g]
            if [x[0] for x in tokens(t)] != [x[0] for x in tokens(L[g])]:
                report.append(f"{idx[0] + 2}-{idx[-1] + 2}: {lang} numbers differ")
                continue
            for i, lc, seg in zip(idx, lat_cut, cut(t, erows, spans, plessis)):
                out[lang][i] = finish(seg, lc, rows[i][3])
            if lang == "ja" and not plessis:
                move_refs(out[lang], rows, idx)
    heads = {lang: headwords(rows, lat, t) if plessis else {}
             for lang, t in tr.items()}
    for lang in tr:
        lines = [f"headword\theadword-{lang}\tverse\tform\tdescription"]
        for r, s in zip(rows, out[lang]):
            lines.append("\t".join([r[0], heads[lang].get(r[0], "")]
                                    + r[1:3] + [s]))
        (d / f"INDEX-{lang}.tsv").write_text("\n".join(lines) + "\n",
                                             encoding="utf-8")
    print("\n".join(report), file=sys.stderr)


if __name__ == "__main__":
    main()
