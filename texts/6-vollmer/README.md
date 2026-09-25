# Vollmer

The *Ilias Latina* in F. Vollmer's edition, *Homerus Latinus*, in
*Poetae Latini Minores* II, fasc. 3 (Leipzig: Teubner, 1913), from the
Internet Archive scan [p1poetaelatinimi02baeh](https://archive.org/details/p1poetaelatinimi02baeh)
(item 6 of the [Internet Archive](../../README.md#internet-archive) list).
The scan is in the public domain.

The files were extracted once by `make vollmer` in
[src/](../../src/README.md) (`vollmer.py`) and are corrected by hand
from then on.  They are arranged by the page numbers printed in the book, with
the page of the PDF for looking up the page image.

| File | Contents | Pages |
|---|---|---|
| [preface.md](preface.md) | Preface and list of manuscripts (*conspectus codicum*) | IV–X |
| [ilias.md](ilias.md) | Text, margins, testimonia and apparatus | 1–55 |
| [index.md](index.md) | Index of names (*index nominum*), one entry per line | 56–65 |

## ilias.md

Each page has a table of the verses and lists of the notes below them.

- **Verse**: the verse number in The Latin Library numbering
  ([texts/ilias.txt](../ilias.txt)), found by matching the text.  It
  does not come from Vollmer, who prints a number only every five
  verses; his own numbers are in the Printed column.  The verses keep
  Vollmer's order, so a verse he moves appears out of sequence: 107,
  109, 108; 597 after 601; 790 after 794.  Verse 874 appears twice, in
  brackets after 863 and in its place, and verse 860 in two parts
  around a lacuna.  Verse 791 is not in the text (see the apparatus).
- **Margin**: the left margin as read by the OCR.  Vollmer prints there
  the lines of the *Iliad* that the poet follows (the book as a Greek
  letter where it changes, then the line), since he regards the
  24-book division of the manuscripts as useless (preface, p. VIII).
  Many verses have a dash instead, probably marking verses with no
  Homeric counterpart (not yet checked).
- **Printed**: the verse number in the right margin as read by the OCR.
- **Testimonia**: quotations and borrowings in later authors (e.g.
  Ermenricus, *Gesta Berengarii*), printed above the apparatus.
- **Apparatus**: split into items at the verse numbers it begins with.
  "(cont.)" is text before the first number on the page, usually a
  note continued from the previous page.

## Accuracy

The text is the OCR of the scan, corrected only where it has been
checked against the page images: elsewhere expect misread
letters, sigla (e.g. "Sl" or "il" for Ω), numbers and Greek letters.
Rows of dots marking a lacuna are not recognized, and the table of the
book divisions in the preface (pp. VII–VIII) is garbled.  Anything
quoted from these files must be checked against the page image first.

Errors found in this way are corrected directly in these files.
Superscript numerals mark the hands of a manuscript (G¹ = first hand
of G).  Vollmer's angle brackets for words supplied by the editor are
written `\<que>`, as `|` in the tables is written `\|`, so that they
are not taken for markup (a bare `<que>` would be dropped as an HTML
tag).
