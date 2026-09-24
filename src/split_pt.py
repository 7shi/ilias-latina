"""Split the text of the Portuguese edition PDF into sections.

Usage: python split_pt.py BOOK.pdf OUTDIR

The PDF (Bébio Itálico, A Ilíada Latina, translated by Priscilla A. F.
Almeida, Coimbra University Press, 2021) is converted with
"pdftotext -layout" (poppler-utils), and the text is cut at the section
headings listed in the table of contents (see SECTIONS):

    00_front                front matter, colophon, table of contents
    01_prefacio             preface (pp. 11-27)
    02_referencias          references of the preface
    03_introducao           introduction (pp. 31-33)
    04_estrutura - 09_...   the sections of the introduction (pp. 34-83)
    10_referencias          references of the introduction
    11_nota_preliminar      note on the translation (pp. 89-90)
    12_iliada_latina        the translation (pp. 91-149)
    13_back                 list of the series, abstract

Each section is written to OUTDIR as NN_name.txt, starting at the line of
its heading, and the line range is printed.  The text is not cleaned up:
running heads, page numbers, footnotes and form feeds remain, so
concatenating the files gives back the whole pdftotext output.  Headings
in the middle of a page leave the head of that page in the previous file.
"""

import os
import subprocess
import sys
import unicodedata

# (file name, heading) in the order they appear; the first part starts at
# the beginning of the text.  Headings are searched in order, each after
# the previous one.
SECTIONS = [
    ("00_front", None),
    ("01_prefacio", "Prefácio"),
    ("02_referencias", "Referências bibliográficas"),
    ("03_introducao", "Introdução"),
    ("04_estrutura", "Da estrutura e tradição manuscrita"),
    ("05_autoria", "Da autoria e data de composição da obra"),
    ("06_construcao", "Construção narrativa da Ilíada"),
    ("07_aspectos_latinos", "Aspectos latinos da Ilíada"),
    ("08_outros_aspectos", "Outros aspectos ideológicos"),
    ("09_consideracoes_finais", "Considerações finais"),
    ("10_referencias", "Referências bibliográficas"),
    ("11_nota_preliminar", "Nota preliminar à tradução"),
    ("12_iliada_latina", "Bébio Itálico – Ilíada"),
    ("13_back", "Volumes publicados na Coleção Autores"),
]


def is_heading(line: str, heading: str) -> bool:
    """True if the line is the heading itself, not a table of contents
    entry (which ends with a page number)."""
    # Some headings are preceded by control characters (\f, \a), and some
    # use decomposed accents.
    text = "".join(c for c in line if c.isprintable()).strip()
    text = unicodedata.normalize("NFC", text)
    return text.startswith(heading) and not text[-1].isdigit()


def split(lines: list[str]) -> list[tuple[str, int]]:
    """Return (name, first line index) of each section.

    Each heading is searched from the line after the previous one, so that
    a heading used twice ("Referências bibliográficas") is found in the
    right place.  Exits with an error if a heading is not found.
    """
    starts = []
    pos = 0
    for name, heading in SECTIONS:
        if heading is not None:
            while not is_heading(lines[pos], heading):
                pos += 1
                if pos == len(lines):
                    sys.exit(f"heading not found: {heading}")
        starts.append((name, pos))
        pos += 1
    return starts


def main():
    """Convert the PDF to text and write the sections."""
    pdf, outdir = sys.argv[1:3]
    text = subprocess.run(["pdftotext", "-layout", pdf, "-"],
                          capture_output=True, text=True, check=True).stdout
    # Split at "\n" only: splitlines() would also break at form feeds.
    lines = [line + "\n" for line in text.split("\n")]
    lines[-1] = lines[-1][:-1]
    if not lines[-1]:
        lines.pop()
    starts = split(lines)
    os.makedirs(outdir, exist_ok=True)
    ends = [pos for _, pos in starts[1:]] + [len(lines)]
    for (name, start), end in zip(starts, ends):
        with open(os.path.join(outdir, name + ".txt"), "w",
                  encoding="utf-8") as f:
            f.writelines(lines[start:end])
        print(f"{name}.txt: {start + 1}-{end}")


if __name__ == "__main__":
    main()
