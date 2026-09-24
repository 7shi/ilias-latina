"""Interleave two numbered verse files into a parallel text.

Usage: python parallel.py LATIN.txt TRANSLATION.txt OUTPUT.txt

Each input line is "LABEL TEXT", where LABEL is a verse number such as
"12" or "827a" (the outputs of extract.py and extract_pt.py).  Verses are
matched by label, not by position, so differences in numbering or order
between the two texts do not shift the alignment.

The output follows the order of the translation.  Each verse takes two
lines: the label with the Latin text, then the translation indented to
line up with it.  If the Latin text has no verse with that label, "(none)"
is written in its place.  Latin verses absent from the translation are
omitted.

    1 Iram pande mihi Pelidae, Diua, superbi
      A ira conta-me, ó deusa, do soberbo Pelida,
"""

import sys


def load(path: str) -> list[tuple[str, str]]:
    """Read a numbered verse file as a list of (label, text)."""
    with open(path, encoding="utf-8") as f:
        return [tuple(line.rstrip("\n").partition(" ")[::2]) for line in f]


def main():
    """Write the parallel text of the two files."""
    latin_path, trans_path, dst = sys.argv[1:4]
    latin = dict(load(latin_path))
    with open(dst, "w", encoding="utf-8") as f:
        for label, text in load(trans_path):
            print(label, latin.get(label, "(none)"), file=f)
            print(" " * len(label), text, file=f)


if __name__ == "__main__":
    main()
