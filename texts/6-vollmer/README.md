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
| [preface.md](preface.md) ([en](preface-en.md), [ja](preface-ja.md)) | Preface and list of manuscripts (*conspectus codicum*) | IV–X |
| [ilias.md](ilias.md) ([en](ilias-en.md), [ja](ilias-ja.md)) | Text, margins, testimonia and apparatus | 1–55 |
| [COMMENTARY.md](COMMENTARY.md) ([en](COMMENTARY-en.md), [ja](COMMENTARY-ja.md)) | The testimonia, and the glosses and parallels of the apparatus, without the readings and conjectures | 1–54 |
| [index.md](index.md) ([en](index-en.md), [ja](index-ja.md)) | Index of names (*index nominum*), one entry per line | 56–65 |

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
  letter where it changes and usually on the first verse of a page,
  then the line), since he regards the 24-book division of the
  manuscripts as useless; this also shows, he says, in which parts
  the poet displayed his own art and invention (preface, p. VIII).
  He does not explain the marks further.  A line marks where the
  correspondence begins or resumes; how far it runs is not given.
  Many verses have a dash instead, in the context of the preface the
  poet's own additions (e.g. 33, 35–39, 41–43 in Chryses' prayer).  A
  verse with an empty margin is not marked; most such verses follow
  Homer near the lines given before or after them (34, on the
  sacrifices, is *Iliad* 1.39–40; 252, before Γ 16, is 3.1–15).  The
  lines are listed in [../iliad.md](../iliad.md).
- **Printed**: the verse number in the right margin as printed (every
  five verses), corrected against the page images.
- **Testimonia**: quotations and borrowings in later authors (e.g.
  Ermenricus, *Gesta Berengarii*), printed above the apparatus.
- **Apparatus**: split into items at the verse numbers it begins with.
  "(cont.)" is text before the first number on the page, usually a
  note continued from the previous page.

## Accuracy

All files in this directory ([preface.md](preface.md), [ilias.md](ilias.md),
and [index.md](index.md)) have been proofread and corrected against the page
images of the scan.

Misread letters, sigla (e.g. "Sl" or "il" for Ω), numbers, Greek letters,
and rows of dots marking lacunae have been verified and corrected against
the page images.  The table of the book divisions in the preface
(pp. VII–VIII) has been properly formatted and verified.

Superscript numerals mark the hands of a manuscript (G¹ = first hand
of G).  Vollmer's angle brackets for words supplied by the editor are
written `\<que>`, as `|` in the tables is written `\|`, so that they
are not taken for markup (a bare `<que>` would be dropped as an HTML
tag).
