# Lemaire

The *Ilias Latina* in J. C. Wernsdorf's edition (*Poetae Latini
Minores* IV, 1784), as reprinted in N. E. Lemaire's *Poetae Latini
Minores* III (Paris: Lemaire, 1824) under the title *Incerti auctoris
(vulgo Pindari Thebani) Epitome Iliados Homeri*, from the Internet
Archive scan
[poetaelatinimin00unkngoog](https://archive.org/details/poetaelatinimin00unkngoog)
(item 2 of the [Internet Archive](../../README.md#internet-archive) list).
The scan is in the public domain.

The files were extracted once by `make lemaire` in
[src/](../../src/README.md) (`lemaire.py`) and are corrected by hand
from then on.  The PDF of the scan has no text layer; the OCR is the
hOCR file of the same scan on archive.org.  The files are arranged by
the page numbers printed in the book, with the page of the PDF for
looking up the page image (the printed page is the PDF page minus 10
throughout).

| File | Contents | Pages |
|---|---|---|
| [prooemium.md](prooemium.md) | Half-title, and Wernsdorf's prooemium on the poem, its author, the name Pindarus, the Latin translators of Homer and the editions | [453], 455–507 |
| [testimonia.md](testimonia.md) | *De Epitome Iliados Homeri ejusque auctore testimonia auctorum ac judicia*, with notes | 508–514 |
| [ilias.md](ilias.md) | Text and notes | 515–610 |
| [excursus.md](excursus.md) | Excursus I–IV on verses 690 seq., 867–870, 894–896 and 919–921 (Wernsdorf's numbers) | 611–620 |

## prooemium.md

The half-title (p. [453], unnumbered) reads *Incerti auctoris, fortasse
Rufi Festi Avieni, Epitome Iliados Homeri … Accedit T. Petronii Arbitri
Trojae Halosis*.  The prooemium has no section headings; its parts, as
named by the running heads, are:

| Pages | Running head |
|---|---|
| 455 | (title page of the prooemium) |
| 456–457 | *De Epitome Iliados Homeri* |
| 458–467 | *De auctore Epitomes Homeri* |
| 468–471 | *De nomine Pindari Thebani inscripto* |
| 472–473 | *De versione Homeri Lat. e qua ducta est Epit.* |
| 474–497 | *Homeristae Latini eorumque fragmenta* |
| 498–501 | *De Epitomes Homeri edendae ratione et subsidiis* |
| 502–505 | *Epitomes Homeri editiones* |
| 506–507 | *De Petronii Trojae halosi* |

The running heads were read from the OCR; they are not in the files.
The footnotes ("(1) …") are given as paragraphs at the end of the page.

## ilias.md

Each page has a table of the verses and a list of the notes below it.
The first page begins with the title as read by the OCR.

- **Verse**: the verse number in The Latin Library numbering
  ([texts/ilias.txt](../ilias.txt)), found by matching the text.
  Verses that The Latin Library does not have are marked "—".
- **Wernsdorf**: his own verse number, counted from the rows (1–1075).
  He prints no verse out of order, so the count agrees with the numbers
  in the margin wherever the OCR reads them (see Printed).
- **Text**: as printed.  The book number printed at the start of a
  verse is kept there ("III. Jamque duae stabant acies …", p. 538;
  "XXII. Unus, tota salus …", p. 596).
- **Printed**: the verse number in the right margin as read by the OCR
  (e.g. "aSo" for 250).  The OCR often joins it to the end of the verse
  or drops it: the script moves a short last word of every fifth verse
  here, but some numbers are still in the text (e.g. "nostis?i6o" at
  160) and many are missing.

### Numbering

Compared with The Latin Library:

- Verses that The Latin Library does not have (Wernsdorf's numbers;
  all checked against the page images):
  270 *Vestrum nunc Helenam sumat quis rectius ipsam*; 587 *[Sortes
  miserunt, quis eorum in bella valeret]*; 590 *Concurrunt armis Ajax
  crudelis et Hector*; 736 *[Rhesi ventigenas secum adduxere jugales]*;
  831 *Objicit et saxum multo cum pondere missum* (Plessis's 827 bis);
  854 *[Tristis ait, jam jamque meo cruciabere ferro]*; 962 *Interea
  validam Thetideius extulit hastam*, in the place of The Latin
  Library's 957 (*Hastam iam manibus saeuus librabat Achilles*), which
  Wernsdorf does not have.  The square brackets are his.
- His 84, *Castraque Myrmidonum praetervolat, inde per auras*, takes
  the place of The Latin Library's 84–85 (checked against the page
  image, p. 523); 85 is therefore not in the table.
- 791, empty in The Latin Library, is his 794 *Instaurantque manus;
  cedit Pelopeia virtus* (p. 583, checked).
- Order: [597] is printed after 594, before 595 (end of p. 566, checked
  against the page image); 874 after 863, with square brackets from
  *liquidas* in 863 to *Oceanum* in 864 (p. 589, checked); [936] before
  935 (p. 596, checked).
- The printed numbers that disagree with the count are misreadings of
  the OCR: 135 read "35", 365 read "355" (checked, p. 547), 870 read
  "87".

In all, his 1075 verses are the 1070 of The Latin Library less 85 and
957, plus the seven above.  The book divisions have not yet been
compared with the other editions.

### Notes

The notes are printed in two columns; each begins on an indented line
with Wernsdorf's number of the verse and a lemma in italics (the OCR
does not keep the italics).

- **Label**: his verse number, followed by "(LL n)" where the verse of
  The Latin Library differs, or "(LL —)" where it has none.  The OCR misreads the old-style figures
  (e.g. "S6." for 86, "x5o." for 150, "3o5." for 205), so the script
  tries the possible readings against the verses of the page and
  prefers the one whose verse contains the lemma.  Labels are not
  checked against the page images.
- **?**: the label could not be read; the OCR text of the label is
  kept at the start of the note (74 notes).
- **(cont.)**: text before the first label of the page, a note
  continued from the previous page.  A note continued from the left
  column into the right one is joined to it.
- Many notes end with "ED."; what it marks has not been checked
  (presumably the additions of the Paris editors to Wernsdorf's notes).
- The manuscripts and editions cited (G. 1, G. 2, H., A., L. and
  others) are described in the prooemium, pp. 498–501; they are not
  yet listed here.

## testimonia.md and excursus.md

Paragraphs as in the prooemium.  The quoted verses, set in smaller type
and indented, are given one per line.  The notes of the testimonia (two
columns, as in the text) are listed after the text of each page,
beginning with the number of the line of the quotation or "*" for a
footnote.

## Accuracy

The text is the OCR of the scan, corrected only where it has been
checked against the page images: elsewhere expect misread letters
(u/n, s/f, e/c, "tnihi" for *mihi*), numbers and Greek.  The paragraphs
are inferred from the line ends and may be split or joined wrongly,
especially at the top of a page that begins with quoted verses (e.g.
p. 509).  Anything quoted from these files must be checked against the
page image first.

Errors found in this way are corrected directly in these files.  A
literal `<` is written `\<`, as `|` in the tables is written `\|`, so
that they are not taken for markup.  The OCR gives the ligatures *æ*
and *œ* as "ae" and "oe", and the files keep them so.

Corrected so far against the page images: the verses quoted under
[Numbering](#numbering) (270, 736, 831, 854 and 84 in ilias.md), the
label of the note on 562 (p. 564, read "565" with "G. 1" for "G. 2"),
and the heading of Excursus III ("vs. 894-896").

## Open questions

- What "ED." at the end of many notes marks: presumably the additions
  of the Paris editors to Wernsdorf's notes, not checked.
- The manuscripts and editions cited in the notes (G. 1, G. 2, H., A.,
  L., "Lips.", "Basil. Torini", "edd." and others): described in the
  prooemium, pp. 498–501, but not yet read or listed here.
- How far the text and notes of 1824 reproduce Wernsdorf's edition of
  1784; that edition has not been consulted.
- His 962 *Interea validam Thetideius extulit hastam* against The Latin
  Library's 957 *Hastam iam manibus saeuus librabat Achilles*: whether
  it is a variant of the same verse or another verse.  His note on 962
  seems to say that the verse is missing in H. and G. 1 (from the OCR,
  not checked).
- The note labels: 74 could not be read ("?"), and the others are not
  checked against the page images; a few chosen readings may be wrong
  (the note on 562 was one; the first of the two notes labelled 831,
  on p. 585, beginning "Huc age huc", does not fit that verse).
- The Printed column: many of the numbers in the margin are missing or
  still joined to the verse.
- The book numbers printed at the start of verses (e.g. "XV." at his
  793, p. 583; "XVII." at 840 and "XVIII." at 845, p. 586) have not
  yet been listed or compared with the other editions.
- The title on p. 515, the running heads of the prooemium and the
  headings of Excursus II and IV are read from the OCR (the heading of
  Excursus I, "v. 690 seq.", was seen on the page image).
- The paragraphs of the prose, where a page begins with quoted verses
  (e.g. p. 509), and the Greek, which the OCR does not read.
