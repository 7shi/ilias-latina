# Baehrens

The *Ilias Latina* in E. Baehrens's edition, *Italici Ilias Latina*, in
*Poetae Latini Minores* III (Leipzig: Teubner, 1881), pp. 3–59, from the
Internet Archive scan [poetaelatinimino34baeh](https://archive.org/details/poetaelatinimino34baeh)
(item 3 of the [Internet Archive](../../README.md#internet-archive) list).
The scan is in the public domain.

The files were extracted once by `make baehrens` in
[src/](../../src/README.md) (`baehrens.py`) and are corrected by hand
from then on.  They are arranged by the page numbers printed in the
book, with the page of the PDF for looking up the page image.

| File | Contents | Pages |
|---|---|---|
| [preface.md](preface.md) | Preface: author, date, medieval reception, the manuscripts B E F G L M N V, earlier editions | 3–7 |
| [ilias.md](ilias.md) | Text, right margin and apparatus | 7–59 |

There is no index for this poem.

## ilias.md

Each page has a table of the verses and a list of the apparatus items
below it.

- **Verse**: the verse number in The Latin Library numbering
  ([texts/ilias.txt](../ilias.txt)), found by matching the text.
- **Baehrens**: Baehrens's own number of the verse, counted from the
  rows and checked against the numbers printed every five verses.  The
  labels of the apparatus use these numbers.  They differ from The Latin
  Library in three places:
  - Verse 69 (*et prope consumptae uires redduntur Achiuis*) is not in
    the text; the apparatus (after 68) says that only G has it, added in
    the margin by a later hand, and that Baehrens removed it.  Instead he
    marks a lacuna after 79 with a row of dots numbered 80 (Verse "—").
    So Baehrens 69–79 are verses 70–80, and 81 onwards agree again.
  - 107 and 109 change places, after L. Müller (apparatus at 107); the
    printed margin reads 109, 108, 107.  The numbers go with the verses,
    so they agree with The Latin Library.
  - 873 and 874 change places: Baehrens 873 is verse 874 (*Fecerat et
    liquidas …*), which he moves before 874 (verse 873, *Tritonesque
    feros …*); see the apparatus at 873.
- **Text**: as printed.  Verses that Baehrens takes to be interpolated
  are in square brackets but keep their numbers: 297, 386, 601,
  621–626, 695, 791, 843–844 and 936, as found in the OCR (621–626
  checked against the page image).  Verse 791, empty in The Latin
  Library, is in his text in brackets.  A long verse whose last word is printed on the next row
  (1015 *maesto*) is joined into one row.
- **Printed**: the verse number in the right margin as read by the OCR
  (e.g. "lO" for 10).
- **Book**: the book number in the right margin as read by the OCR, at
  the first verse of each book (e.g. "YII" for VII; "!!•" is II at 111).
  Baehrens sometimes prints it on a row of its own above the verse
  (VII at 575); it is given with the verse that follows.  Book 1 has no
  number.  The apparatus records the divisions of the manuscripts at the
  same place (items labelled with the book number or "Lib.").
- **Apparatus**: split into items at the double bars (‖) that begin with
  a verse number of the page, "post 563", "Lib. VII" or a book number.
  "(cont.)" is text before the first item of the page, usually an item
  continued from the previous page.  There is no separate section of
  testimonia: the borrowings of the *Gesta Berengarii* and the
  conjectures of earlier editors (Higtius, Schraderus, Kootenus,
  L. Muellerus and others) are recorded in the apparatus.

## Sigla

- The manuscripts are B E F G L M N V (preface, pp. 5–6); the OCR often
  reads G as "Gr".  Hands are written *m. 1*, *m. 2*, *m. rec.*
- "0" stands for a bold 0 in the book, which seems to mean the
  manuscripts together (e.g. "Conficiebat 0" against a conjecture at
  6).  It is printed as a narrow bold O or zero; the files keep the
  plain "0" of the OCR.  The preface does not define
  it; the meaning is inferred from its use.  It occurs only in the
  apparatus, on nearly every page from p. 8 to p. 59; clear examples are
  at 6 and 11 (p. 8), 88 and 90 (p. 11), 98, 103 and 107 (p. 12), 560
  and 563 (p. 35), and 616, 620 and 626 (p. 38).
- "ς" marks readings of later manuscripts (preface, p. 7); the OCR reads
  it in various ways, e.g. "<?", "<S", "?".

## Accuracy

The text is the OCR of the scan, corrected only where it has been
checked against the page images: elsewhere expect misread letters,
sigla, numbers and marks (e.g. "\\" or "jj" for the double bar, "|" for
the single bar between readings).  Anything quoted from these files must
be checked against the page image first.

Errors found in this way are corrected directly in these files.
