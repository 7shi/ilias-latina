# Plessis

The *Ilias Latina* in F. Plessis's edition, *Italici Ilias Latina*
(Paris: Hachette, 1885), a Latin thesis, from the Internet Archive scan
[italiciiliaslati00plesuoft](https://archive.org/details/italiciiliaslati00plesuoft)
(item 4 of the [Internet Archive](../../README.md#internet-archive) list).
The scan is in the public domain.

The files were extracted once by `make plessis` in
[src/](../../src/README.md) (`plessis.py`) and are corrected by hand
from then on.  They are arranged by the page numbers printed in the
book, with the page of the PDF for looking up the page image.

| File | Contents | Pages |
|---|---|---|
| [preface.md](preface.md) | Preface (*prooemium*) | I–III |
| [introduction.md](introduction.md) | Introduction, *De Italici Iliade Latina*: the name of the author, the date, the Silius Italicus question; Latin translations of Homer; the method and purpose of the poem; manuscripts and editions; the name Pindarus | V–LI |
| [ilias.md](ilias.md) | List of manuscripts, text, verses printed below the text, readings of the manuscripts and notes | 2–85 |
| [index.md](index.md) | Index of names and subjects (*index nominum et rerum*), one entry per line | 87–98 |

## ilias.md

p. 2 is the list of manuscripts (E L F V M N B G Y R A I S T C D),
which is not in the text layer and was transcribed from the page image.
The introduction (p. XLIII) says that the readings of thirteen of them
are given throughout, and those of T, C and D for verses 1–111 and
1000–1070 and some doubtful places.

Each page of the text has a table of the verses and up to three
sections below it.

- **Book heading**: each book begins on a new page with its number as
  a heading, given before the table as read by the OCR (books 19 and
  20 together as "XIX-XX").  The OCR has no heading on p. 3; "I" was
  read from the page image.
- **Verse**: the verse number in The Latin Library numbering
  ([texts/ilias.txt](../ilias.txt)), found by matching the text.
  Plessis's own numbers, printed every five verses, are the same, so
  there is no separate column for them.  The verses keep his order:
  108 comes after 110 ("Sic versus disposuit Havet", p. 9, printed as
  [109], [110], [108]), and 874 before 873.  Verses not in The Latin
  Library have "—": 245 bis, supplied by Plessis with its words in
  angle brackets (p. 18); 827 bis, in square brackets (p. 64); and
  869 bis, a lacuna printed as a row of dots after "\<Sol." (p. 69).
- **Text**: as printed; a long verse whose end is printed on a row of
  its own is joined into one row.
- **Printed**: the verse number in the right margin as read by the OCR
  (e.g. "2Z|0" for 240).
- **Below the text**: on some pages the verses that Plessis leaves out
  of the text are printed after the rule below it, in smaller type
  with their numbers, followed by a remark in italics (e.g. "spurium
  esse Mueller vidit") and a second rule.  As found in the OCR these
  are 69, 222, 297, 597, 601, 621–626, 695, 791, 843–844, 863, 864 and
  874 (the last printed after 863 as "863 bis"; 874 also stands in
  the text), 936, 942, 1003 and 1054 (69, 222, 621–626, 695, 791 and
  863–864 checked against the page images).  Verse 791, empty in The Latin
  Library, is numbered from the printed number.  The same place holds
  a remark without verses on p. 9 (the order of 107–110), p. 15 and
  p. 18 (the lacuna filled by 245 bis).
- **Codices**: the readings of the manuscripts, split into items at the
  verse numbers after a double bar (‖) or after the end of an item
  (the OCR often drops the bar or reads it as "II", "j|" and the like).
  "(cont.)" is text before the first item of the page, usually an item
  continued from the previous page; the first page of a book begins
  with "Codices —", the book division in the manuscripts ("Lib. XV
  L …") and on p. 3 the title ("Titul.").
- **Notes**: in smaller type, the conjectures of Plessis and earlier
  editors and the parallels in the *Iliad* (e.g. "cf. Iliad. I, 4"),
  one item per verse.  The labels misread by the OCR have been
  corrected against the page images; besides verse numbers they
  include ranges and lists ("432-433", "242, 243, 244"), "post 345",
  "827 bis" and the book divisions of other editors ("Lib. XX").

## Sigla

- The manuscripts are those of the list on p. 2 (see above); they are
  printed in bold, written here as plain capitals.  The OCR often
  misreads them (see [Accuracy](#accuracy)).
- Hands are written as printed: "m 1" (the first hand), "m 2" (a
  corrector), "man. rec." (a later hand), after the siglum, e.g.
  "regis E m 2 T." at 11 (p. 4) and "tempore uite E L m 1" at 13.
  They are not turned into superscripts as in Vollmer's files.
- "omnes", "ceteri", "plerique" (in italics in the book) refer to the
  manuscripts; "Baehrensiani" to those used by Baehrens (introduction,
  p. XLIII: "Baehrensianis (praeter E et L)").
- Within an item a single bar (|) separates the readings of different
  words, and "]" closes a lemma ("Phoebi] diui T." at 68); items are
  separated by the double bar (‖).
- "≡" stands for letters erased in a manuscript (e.g. "lingua ≡ ≡ (nec
  m 2 supra lin. praefixit.)" at 137, p. 11); the meaning is inferred
  from its use with "ras." (rasura).  The OCR reads it as "=" or "==".
- Italics, which the book uses for the editor's own words and the
  names of scholars, are not kept.
- `<` (Plessis's angle brackets, e.g. `<Sol.` at 869 bis, and OCR
  noise) is written `\<`, as `|` in the tables is written `\|`, so
  that it is not taken for markup.

## Accuracy

The text is the OCR of the scan, corrected only where it has been
checked against the page images: elsewhere expect misread letters,
sigla (e.g. "IV" or "X" for N, "IVI" for M), numbers, Greek and marks.
The bold sigla and the double bars of the readings are placed by the
OCR a little below their row, and some may still be out of place.  The
index is read column by column, and some entries may be joined or split
where the columns are uneven.  Anything quoted from these files must
be checked against the page image first.

Errors found in this way are corrected directly in these files.
