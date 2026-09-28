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
| [preface.md](preface.md) ([en](preface-en.md), [ja](preface-ja.md)) | Preface (*prooemium*) | I–III |
| [introduction.md](introduction.md) ([en](introduction-en.md), [ja](introduction-ja.md)) | Introduction, *De Italici Iliade Latina*: the name of the author, the date, the Silius Italicus question; Latin translations of Homer; the method and purpose of the poem; manuscripts and editions; the name Pindarus | V–LI |
| [ilias.md](ilias.md) ([en](ilias-en.md), [ja](ilias-ja.md)) | List of manuscripts, text, verses printed below the text, readings of the manuscripts and notes | 2–85 |
| [COMMENTARY.md](COMMENTARY.md) ([en](COMMENTARY-en.md), [ja](COMMENTARY-ja.md)) | The references to the *Iliad* and the Latin parallels in the notes of ilias.md, without the readings and conjectures | 3–74 |
| [index.md](index.md) ([en](index-en.md), [ja](index-ja.md)) | Index of names and subjects (*index nominum et rerum*), one entry per line | 87–98 |
| [INDEX.tsv](INDEX.tsv) | The index as a table of headword, verse, form and description, one row per place cited (see [below](#indextsv)) | 87–98 |
| [INDEX-en.tsv](INDEX-en.tsv), [INDEX-ja.tsv](INDEX-ja.tsv) | INDEX.tsv with the description in English and Japanese, cut from index-en.md and index-ja.md, and the headword translated (see [below](#index-entsv-and-index-jatsv)) | 87–98 |

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
- **Printed**: the verse number in the right margin (printed every five
  verses); OCR misreadings (such as "2Z|0" for 240) have been corrected
  against the page images.
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
  verse numbers after a double bar (‖) or after the end of an item.
  Dropped bars and OCR misreadings (such as "II", "j|") have been
  corrected against the page images.
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

## INDEX.tsv

The index (index.md) as a table, one row for each place cited, with a
header row and four columns:

- **headword**: the word in capitals that begins the entry.  The lines
  after it, with other forms and names of the same person (Pelides,
  Aeacides under ACHILLES; Achivi, Danai, Pelasgi under GRAI), belong
  to it.  Homonyms keep the description by which Plessis tells them
  apart ("ACAMAS Antenoris filius", "ACAMAS dux Thracum").
- **verse**: the verse as printed in the index, written in full:
  "205-6" is "205-206", "245 bis" is "245bis", "895 sqq." is
  "895-899" (Aeneas meets Achilles and is saved by Neptune), and places
  cited together ("248 et 520") share one row as "248,520".  A
  cross-reference ("ACHIVI cf. Grai.") has no verse.
- **form**: the word of the verse that the row cites, as it stands in
  ilias.md; for a range, the word in one of its verses, and for a list,
  one form for each verse.  It is empty where the verse does not have
  the word: at 151 the vulgate reading *Achivi*, where Plessis reads
  *Pelasgi*, and at 257-258, which describe Paris without naming him.
- **description**: Plessis's Latin as printed, without the verse: his
  own summary of the passage around the words of the verse, not a
  quotation (« » marks one, and ( ) his remarks).  A dash (—) stands
  for the form last named, as in the index.  Brackets are closed within
  the row: [ ] marks a verse Plessis rejects, < > a supplement.

The misprints of the index are corrected in double braces, in index.md
and in the rows copied from it: {{Amphimachus}} (ELIS, printed
"Amphimacus"), {{MESTHLES}} ("MESTHLFS"), {{naves}} (NESTOR, "navec"),
{{Idomeneus}} (PHAESTUS, "Idemeneus") and {{Ithacus}} (ULIXES,
"Itachus").  The headword column has MESTHLES without braces.  The
translations keep the braces only where they quote the Latin.

The verses are Plessis's own numbers.  They are those of The Latin
Library except at 873 and 874, which he prints in the other order and
numbers in his order: 873 is *Nereidas* and 874 *Tritones … Dorida*,
where ilias.md, numbered by The Latin Library, has 874 and 873.  The
index misprints two verses, kept as printed with the form taken from
the verse meant: ACHILLES 937 (*Nereius* is in 938) and COROEBUS 250
(in 249).

The table was drafted once by [index.py](index.py), and the form added
by [index_forms.py](index_forms.py), which matches the first letters of
the headword, the description or the form of the row before against the
words of the verse; both drafts were then checked row by row and
corrected by hand.

### INDEX-en.tsv and INDEX-ja.tsv

INDEX.tsv in English and Japanese: the same rows in the same order,
with headword, verse and form in Latin as in INDEX.tsv.  After the
headword a column is added, and the description is translated:

- **headword-en**, **headword-ja**: the headword in the language of the
  file.  The Japanese is the reading given in brackets after the
  headword in index-ja.md ("ABAS(アバース)" gives アバース), and for
  homonyms the description of the heading ("アカマース、アンテーノールの子");
  the English of homonyms is taken from the heading of index-en.md
  ("Acamas, son of Antenor").  The other English headwords, which
  index-en.md leaves in Latin, were added by hand, following the names
  used in the translations.
- **description**: the translation of the row, cut from index-en.md or
  index-ja.md at the same verses where INDEX.tsv cuts index.md, not
  translated anew.  Like the Latin it leaves out the verse and the
  headword that begins the entry; the Latin forms that the translations
  keep ("Abanta: Diomedes kills him") and the dash (—) for the form last
  named are kept.  Ranges and punctuation are those of the translation.
  ARCTUS and LUCIFER, empty in INDEX.tsv, are empty here too.

Following the translations, the braces of the misprints are kept where
the Latin is quoted ("{{Ithacus}} Ithaci") and dropped in translated
text.

The files were drafted once by [../index_translations.py](../index_translations.py),
which uses the verse numbers of each entry, the same in index.md and
its translations, as anchors, and repeats the cut on index.md to check
it against INDEX.tsv; the drafts were then checked row by row and
corrected by hand.

## Sigla

- The manuscripts are those of the list on p. 2 (see above); they are
  printed in bold, written here as plain capitals.  OCR misreadings
  have been corrected against the page images.
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

All files in this directory ([preface.md](preface.md),
[introduction.md](introduction.md), [ilias.md](ilias.md), and
[index.md](index.md)) have been proofread and corrected against the page
images of the scan, with one limit (see
[PROOFREADING.md](../PROOFREADING.md), steps 5, 6 and 8): in the
verses of ilias.md, the words not in the vocabulary of The Latin
Library were checked against the images, but a misreading that makes
another Latin word may be left.  index.md has been compared letter by
letter with the images, its verse numbers in step 5 and its words and
punctuation in step 8.

Misread letters, sigla (such as "IV" or "X" for N, "IVI" for M), numbers,
Greek quotations, double bars (‖), and index entries have been verified
and corrected against the page images.
