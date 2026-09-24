"""Extract the numbered verse text of the Ilias Latina from The Latin Library.

Usage: python extract.py ilias.html OUTPUT.txt

Input is https://www.thelatinlibrary.com/ilias.html (downloaded by
"make download").  The poem is a single <p> element whose verses are
separated by <br>; the page title, separators and navigation links are
left out.

Output has one verse per line in the form "N TEXT", numbered 1-1070 in the
order of the page.  The text is kept as on the page, including its
editorial signs:

- <que>, <et>: words supplied by the editor
- <> (line 791): a missing verse
- word* and *word* (lines 7, 890, 1008, 1037): marks not explained on the
  page; line 890 is a corrupt verse in Scaffai's edition

Compared with the numbering of Scaffai's critical edition (1997), used by
the Portuguese translation, verse 791 exists here only as "<>", verse 827a
is missing, and verse 597 stands in its manuscript position (Scaffai moves
it after 601).  Otherwise the numbers agree.
"""

import sys

from bs4 import BeautifulSoup


def extract(html: str) -> list[str]:
    """Return the verses of the poem, without empty lines.

    Each <br> in the source is followed by a newline, so the text of the
    <p> element can simply be split into lines.  HTML entities such as
    &lt;que&gt; are decoded by BeautifulSoup.
    """
    soup = BeautifulSoup(html, "html.parser")
    # The poem is the only <p> without a class attribute that contains <br>.
    for p in soup.find_all("p", class_=False):
        if p.find("br"):
            lines = p.get_text().splitlines()
            return [line.strip() for line in lines if line.strip()]
    raise ValueError("poem text not found")


def main():
    """Read the HTML file and write the numbered verses."""
    src, dst = sys.argv[1:3]
    with open(src, encoding="utf-8") as f:
        lines = extract(f.read())
    with open(dst, "w", encoding="utf-8") as f:
        for i, line in enumerate(lines, 1):
            print(i, line, file=f)


if __name__ == "__main__":
    main()
