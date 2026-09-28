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
| [INDEX.tsv](INDEX.tsv) | The index as a table of headword, verse, form and description, one row per place cited (see [below](#indextsv)) | 56–65 |
| [INDEX-en.tsv](INDEX-en.tsv), [INDEX-ja.tsv](INDEX-ja.tsv) | INDEX.tsv with the description in English and Japanese, cut from index-en.md and index-ja.md, and the headword translated (see [below](#index-entsv-and-index-jatsv)) | 56–65 |

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

## INDEX.tsv

The index (index.md) as a table, one row for each place cited, with a
header row and four columns:

- **headword**: the name the entry is sorted under, in the nominative.
  Vollmer prints it spaced out, often inside a phrase of the verse
  ("Locrum fortissimus Aiax"), and in the case of that phrase
  ("Abanta"); some entries begin with the name and a bracket
  ("Achilles]").  Homonyms keep his number after the name, as in his
  cross-references ("v. Antenor 1"): "Acamas 1", "Acamas 2".  Where he
  divides one entry between two persons, the person is added in
  brackets: "Aeacides (Achilles)", "Aeacides (Aiax Telamonius)",
  "Atrides (Agamemno)", "Atrides (Menelaus)".  Two entries of the same
  name that he does not number are told apart in the same way: "Aiax
  (Locrus)", "Aiax (Telamonius)", "Xanthus (Phaenopis f.)", "Xanthus
  (fluvius)".
- **verse**: the verse numbers of the phrase, without Vollmer's marks
  (the asterisk of an emended place, the brackets of a rejected verse,
  "(?)"); several numbers after one phrase ("magnus -es 860. 995")
  share one row, written "860,995", and "1—8" is written "1-8".  A
  cross-reference ("v. Graecus") has no verse.
- **form**: the word of the verse that the row cites, as it stands in
  ilias.md, without an enclitic -que, one for each verse; for a phrase
  without the name ("nati", "pio . . . patri") the word that stands for
  the person.  It is empty where the verse does not have the word: the
  acrostic (1-8), Priamus [983], Pelopeus 791 (not in the text),
  Pylaemenes 249 ("cf. et v. 249"), Syme 195 (an obelized place) and
  513 (Aeneas's charioteer, not named).
- **description**: Vollmer's words as printed, with the verse numbers
  and their marks, without the headword in front of a bracket
  ("Achilles]"), the homonym number and the name of the person where
  it is in the headword.  A remark after a colon (": Diomedes") stays
  with the phrase it follows.

The one misprint of the index is corrected in double braces, in
index.md, its translations and the row copied from it: "saevi duo
{{robora}} belli" (Epistrophus 1, printed "rubora").

The verses are Vollmer's own numbers.  They are those of The Latin
Library except at 957 and 958, which he prints in the other order and
numbers in his order: 958 is *saevus . . . Achilles*, where ilias.md,
numbered by The Latin Library, has 957.  The index also cites some
verses that do not have the word, kept as printed with the form taken
from the verse meant: Amaryncides 337 (in 377), Doris 874 (in 873),
Phoebus 69 (in 68), and the phrases that run on into the next verse,
Agamemnon 10 (*regi* in 11), Priamides 754 (in 755), Tydides 415
(in 416), and occasus and ortus 866 (in 867).  At 645 the index reads *Troica* with *Troiae* as a variant,
but the text prints *Troiae*, which is given as the form.

The table was drafted once by [index.py](index.py), which splits each
entry at its verse numbers and matches the first letters of the
headword or the phrase against the words of the verse; the draft was
then checked row by row and corrected by hand.

### INDEX-en.tsv and INDEX-ja.tsv

INDEX.tsv in English and Japanese: the same rows in the same order,
with headword, verse and form in Latin as in INDEX.tsv.  After the
headword a column is added, and the description is translated:

- **headword-en**, **headword-ja**: the headword translated, with the
  homonym number and the bracket of INDEX.tsv ("Acamas 1",
  "descendant of Aeacus (Achilles)", 「アイアコスの末裔(アキレウス)」).
  The translations of the index have no headwords, so these were added
  by hand, following the names used in the translations and in
  Plessis's INDEX-{en,ja}.tsv.
- **description**: the translation of the row, cut from index-en.md or
  index-ja.md at the same verses where INDEX.tsv cuts index.md, not
  translated anew.  The translations keep Vollmer's phrases in Latin
  and translate his notes, so the description keeps the verse numbers
  and marks as in INDEX.tsv, with "v." as "see" or 「を参照」 and "f."
  as "son of" or 「の子」.  In Japanese 「を参照」 follows the places
  it refers to ("patri 23. patrem 42. … vatis 44 を参照"); it is put
  on the row that has "v." or "cf." in the Latin.

The files were drafted once by [../index_translations.py](../index_translations.py),
which uses the verse numbers of each entry, the same in index.md and
its translations, as anchors, and repeats the cut on index.md to check
it against INDEX.tsv; the drafts were then checked row by row and
corrected by hand.
