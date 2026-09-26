# Scripts

Scripts that build the Latin text, organize the public-domain editions
for reference, and build the Portuguese translation and the parallel
text.  All outputs go into `tmp/` (ignored by git), except `make text`,
which writes the published text `../texts/ilias.txt`, and `make
vollmer`, `make baehrens`, `make plessis` and `make lemaire`, which
write `../texts/6-vollmer/`, `../texts/3-baehrens/`, `../texts/4-plessis/`
and `../texts/2-lemaire/` once, `make concordance`, which writes
`../texts/concordance.md` once, and `make commentary`, which writes
`../texts/COMMENTARY.md` and its translations `COMMENTARY-en.md` and
`COMMENTARY-ja.md` again whenever their sources change.

## Usage

Run the commands in this directory.  `make` with no target shows the help.

```sh
make                # show help
make all            # download the Latin text and number the verses
make text           # add the book headings (../texts/ilias.txt)
make vollmer        # extract Vollmer's edition once (../texts/6-vollmer/)
make baehrens       # extract Baehrens's edition once (../texts/3-baehrens/)
make plessis        # extract Plessis's edition once (../texts/4-plessis/)
make lemaire        # extract Lemaire's edition once (../texts/2-lemaire/)
make concordance    # build the verse concordance once (../texts/concordance.md)
make commentary     # put the verses and commentaries side by side (../texts/COMMENTARY.md, -en, -ja)
make homer          # download the Greek Iliad for reference (tmp/iliad-grc.xml)
```

`make homer` downloads the Greek text of the *Iliad* from the Perseus
Digital Library ([canonical-greekLit](https://github.com/PerseusDL/canonical-greekLit),
`tlg0012.tlg001.perseus-grc2.xml`): the edition of Monro and Allen,
*Homeri Opera*, 3rd ed. (Oxford, 1908–1920), which is in the public
domain, in Perseus's TEI encoding, licensed CC BY-SA 4.0.  It is used
only for reference while processing and stays in `tmp/`; it is not
part of this repository.

To process the Portuguese edition, put the PDF anywhere (for example in
`tmp/`) and pass its path with `PDF=`.  Quote it if the name contains
spaces.  `make pt` also downloads and numbers the Latin text if it is
not there yet.

```sh
make pt    PDF="tmp/book.pdf"   # numbered translation and parallel text
make parts PDF="tmp/book.pdf"   # split the whole book into sections
```

`make check-pt` has an LLM check that each translated line matches its
Latin verse (see [PORTUGUESE.md](PORTUGUESE.md) for the results).  The
model is required, with an optional vendor prefix as in llm7shi.  The
judgments are saved after every chunk, so an interrupted run resumes
when the target is run again.

```sh
make check-pt MODEL="gpt-5.6-terra"
```

### Targets and outputs

| Target | Output (in `tmp/`, except `text`) | Script |
|---|---|---|
| `download` | `ilias.html` — the page from The Latin Library | — |
| `homer` | `iliad-grc.xml` — the Greek *Iliad* from Perseus (TEI, one `<l n>` per line in each book) | — |
| `all` | `ilias.txt` — Latin text, `N TEXT` per verse | `extract.py` |
| `text` | `../texts/ilias.txt` — the same with `## N` book headings | `books.py` |
| `vollmer` | `../texts/6-vollmer/*.md` — Vollmer's edition by page (downloads the scan to `tmp/`) | `vollmer.py` |
| `baehrens` | `../texts/3-baehrens/*.md` — Baehrens's edition by page (downloads the scan to `tmp/`) | `baehrens.py` |
| `plessis` | `../texts/4-plessis/*.md` — Plessis's edition by page (downloads the scan to `tmp/`) | `plessis.py` |
| `lemaire` | `../texts/2-lemaire/*.md` — Lemaire's edition by page (downloads the OCR of the scan to `tmp/`) | `lemaire.py` |
| `concordance` | `../texts/concordance.md` — the verses of the four editions keyed to The Latin Library; `concordance_check.txt` — the rows to check | `concordance.py` |
| `commentary` | `../texts/COMMENTARY.md` — the verses of The Latin Library and of the four editions with the items of their commentaries; `COMMENTARY-en.md` and `COMMENTARY-ja.md` with the items of the editions' translations | `commentary.py` |
| `pt` | `ilias_pt.txt` — Portuguese translation, `LABEL TEXT` per verse | `extract_pt.py` |
| | `ilias_la_pt.txt` — Latin and Portuguese interleaved | `parallel.py` |
| `check-pt` | `ilias_la_pt_check.json` — `"ok"` or `"ng"` per verse | `check_pt.py` |
| `parts` | `parts/NN_name.txt` — the book split at its section headings | `split_pt.py` |

The scripts can also be run directly; see the docstring at the top of each
file for details.

```sh
uv run python extract.py tmp/ilias.html tmp/ilias.txt
uv run python books.py tmp/ilias.txt ../texts/ilias.txt
uv run python vollmer.py tmp/6-p1poetaelatinimi02baeh.pdf tmp/ilias.txt ../texts/6-vollmer
uv run python baehrens.py tmp/3-poetaelatinimino34baeh.pdf tmp/ilias.txt ../texts/3-baehrens
uv run python plessis.py tmp/4-italiciiliaslati00plesuoft.pdf tmp/ilias.txt ../texts/4-plessis
uv run python lemaire.py tmp/2-poetaelatinimin00unkngoog_hocr.html tmp/ilias.txt ../texts/2-lemaire
uv run python concordance.py ../texts ../texts/concordance.md tmp/concordance_check.txt
uv run python commentary.py ../texts ../texts/COMMENTARY.md
uv run python commentary.py ../texts ../texts/COMMENTARY-en.md en
uv run python extract_pt.py [-v] BOOK.pdf tmp/ilias_pt.txt
uv run python parallel.py tmp/ilias.txt tmp/ilias_pt.txt tmp/ilias_la_pt.txt
uv run python split_pt.py BOOK.pdf tmp/parts
```

### Example of the parallel text

```
1 Iram pande mihi Pelidae, Diua, superbi
  A ira conta-me, ó deusa, do soberbo Pelida,
2 Tristia quae miseris iniecit funera Grais
  que causou tristes funerais aos míseros gregos,
```

## Verse numbering

The Portuguese translation follows the critical edition of M. Scaffai
(*Baebii Italici Ilias Latina*, 2nd ed., Bologna 1997).  The text of The
Latin Library uses the same numbers, with three exceptions:

| Verse | The Latin Library | Scaffai / Portuguese edition |
|---|---|---|
| 597 | between 596 and 598 | moved after 601 |
| 791 | `<>` (missing verse) | not present |
| 827a | not present | present |

`parallel.py` matches verses by label, so these differences do not shift
the alignment.  Verse 827a appears with `(none)` on the Latin side.

## Book divisions

`../texts/ilias.txt` is generated by `books.py`, so do not move its
headings by hand: `make text` overwrites the file.  To change a division,
edit the first verses of the books in `STARTS` in `books.py` and run
`make text` again.

A book is defined only by its first verse and runs up to the verse before
the next book, so verse 791 (`<>`) falls in book 14.

## Vollmer's edition

`vollmer.py` reads the text layer of the Internet Archive scan (the OCR)
with the position of every word (`pdftotext -bbox-layout`).

- On a text page the OCR gives the verses and the notes the same size,
  so they are told apart by their content: a verse row matches a verse
  of The Latin Library (`tmp/ilias.txt`), a note row does not and has
  sigla, numbers or brackets.  The notes begin where the fewest rows are
  out of place; among equal places, at the widest gap (the rule).
- Words left of the verses are the margin (*Iliad* lines), words at the
  right edge the printed verse number.  The notes are split into
  testimonia and apparatus at the widest gap, and the apparatus into
  items at the verse numbers of the page.
- Each verse is numbered by matching it with the nearest similar verse
  of The Latin Library, so that the OCR of the printed numbers is not
  needed.  Rows that match poorly are reported on stderr.
- The index of names is read column by column; an entry begins at the
  left edge and continues in indented rows.
- The few cases the rules get wrong are fixed by hand in the script
  (`NOTES_START`, `VERSE_FIXES`).
- The script is run only once.  The output is then corrected by hand
  against the page images and committed, so `make vollmer` does nothing
  when `../texts/6-vollmer/ilias.md` exists; running `vollmer.py`
  directly overwrites the corrections.

## Baehrens's edition

`baehrens.py` reads the scan in the same way and imports the common
functions from `vollmer.py` (reading the words, numbering the verses by
matching, splitting verses from notes).  What differs:

- Some pages are scanned at a slight slant, so the words are grouped
  into rows along the slope that gives the fewest rows.  A verse number
  set a little apart joins the nearest row; a number with no row near
  it is the row of dots of a lacuna (80).
- There is no left margin.  The right margin holds the verse numbers
  and the book numbers (Roman numerals, sometimes on a row of their
  own); the last word of a long verse printed on the next row is joined
  to it.
- Baehrens's own verse numbers are counted from the rows and checked
  against the printed ones (reported on stderr where they differ).  His
  transposition of 107 and 109 is given in `NUMBER_FIXES`, verse 791
  (empty in The Latin Library) in `VERSE_FIXES`.
- The apparatus is split at the double bars before a verse number of
  the page, taking the longest ascending series of such numbers so that
  a misread number does not hide the rest.
- As with Vollmer, `make baehrens` does nothing when
  `../texts/3-baehrens/ilias.md` exists.

## Plessis's edition

`plessis.py` imports the common functions from `vollmer.py` (reading
the words, numbering the verses by matching) and the slope of a
slanted page from `baehrens.py`.  What differs:

- The bold sigla and the double bars of the readings are placed by the
  OCR a little below their row, so the words are grouped into rows by
  the middle of their height; a row of marks alone joins the row above,
  and a part of a row set a little lower joins it if their words do not
  overlap.
- Each book begins on a new page with its number as a heading.  The
  verses end at the first wide gap (the rule).  Below it the rows are
  split into blocks at the wider gaps: the verses that Plessis leaves
  out of the text, with a remark (only on some pages); the readings of
  the manuscripts, the first block with double bars; and the notes in
  small type, which begin where the rows start further left than the
  indented rows of the readings.
- The verses printed below the text are matched with the verses within
  40 of the count without moving it on; one that matches none takes its
  printed number (791).  A verse numbered "bis" has no verse of The
  Latin Library unless it matches one (874 as "863 bis").
- The readings are split at the verse numbers after a double bar or
  after the end of an item, taking the longest ascending series as in
  `baehrens.py`; the notes at rows that are indented or begin with a
  number.
- The preface and the introduction are split into paragraphs at the
  indented rows, measured against the left edge of the nearby rows, as
  the edge drifts on a slanted page.  The index is read column by
  column, with the gutter where the fewest words cross; an entry begins
  at the left edge, each row being compared with the one before it.
- The list of manuscripts (p. 2) is not in the text layer and is left
  to be transcribed by hand.
- As with Vollmer, `make plessis` does nothing when
  `../texts/4-plessis/ilias.md` exists.

## Lemaire's edition

The PDF of this scan has no text layer, so `lemaire.py` reads the OCR
of the scan from its hOCR file on archive.org (`_hocr.html`, made with
ABBYY FineReader), which gives the position of every word grouped into
lines and blocks.  It imports `Numberer` and the text helpers from
`vollmer.py`; the rest differs:

- The running head is the top line with anything level with it (the
  OCR sometimes puts the page number in a block of its own).  The
  "Digitized by Google" stamp, the ornamental rules and the printer's
  signatures are dropped; a drop capital is joined to its word.
- On a text page the verses are the lines above the note columns (the
  blocks in the left or right half of the page).  Each verse is
  numbered by matching, and Wernsdorf's own number is counted from the
  rows.  The verses that The Latin Library does not have and 791 are
  given in `VERSE_FIXES`.  The verse number in the margin is a block
  of its own or joined to the verse; on every fifth verse a short last
  word that may be a figure is moved to the margin, and the numbers
  that disagree with the count are reported on stderr.
- The notes begin on indented lines of the columns.  Their labels are
  old-style figures that the OCR misreads, so each character is given
  the figures it may stand for (`FIGURES`, e.g. "S" for 5 or 8, and
  1, 3 or 9 for 2); of the readings that fall among the verses of the
  page, in order, the one whose verse contains the lemma is taken,
  else the one with the fewest substitutions.
- In the prose a paragraph begins after a line that ends short of the
  right edge (measured against nearby lines, as the edges drift on a
  slanted page), not at an indent, as the testimonia have hanging
  indents; quoted verses (indented, short and in smaller type) are
  kept one per line.  ABBYY's own paragraphs are not used, as they join
  quotations to the prose around them.
- As with Vollmer, `make lemaire` does nothing when
  `../texts/2-lemaire/ilias.md` exists.

## Concordance

`concordance.py` reads `../texts/ilias.txt` and the verse tables of the
four editions (`../texts/*/ilias.md`), not the scans, so the corrections
made there are carried over.

- Each row of an edition goes to the verse of The Latin Library in its
  Verse column.  A row "—" (a verse that The Latin Library does not
  have) goes after the verse of the row before it; rows of different
  editions after the same verse share a line if their texts are alike.
- The verses in the order of The Latin Library are the longest
  increasing series of an edition's verse numbers; the others are noted
  as printed after the verse before them.  Verses printed below the
  text, and the second part of a verse split in two, are not.
- A verse that Plessis does not number is "N bis" after the verse it
  follows; his own "863 bis" (verse 874) is kept.
- Each row's text is compared with the verse of The Latin Library
  (ignoring case, punctuation, u/v and i/j), and the rows below 0.75 are
  written to `tmp/concordance_check.txt`, least alike first.
- As with the editions, `make concordance` does nothing when
  `../texts/concordance.md` exists.

## Commentary

`commentary.py` reads `../texts/ilias.txt`, `../texts/concordance.md`,
and the verse tables and `COMMENTARY.md` of the four editions.

- The rows follow the concordance, including its rows "—"; each
  edition's number of the verse is taken from its cell, and the text
  from the row of its ilias.md with the same verse and page.
- A commentary item goes to the verse of its label: Lemaire's labels
  give the verse of The Latin Library ("(LL n)"), and his "(cont.)" goes
  with the last note of the previous page; the numbers of Baehrens,
  Plessis and Vollmer are looked up in their concordance columns.  A
  label for several verses goes to the first of them.
- Unlike the concordance, `../texts/COMMENTARY.md` is not corrected by
  hand; corrections are made in its sources and `make commentary`
  rebuilds it.

## How the PDF is read

`extract_pt.py` uses `pdftotext -bbox-layout` to get the position and size
of every word.  Verse text, footnotes and superscript note numbers are
told apart by their height, and the verse numbers printed in the right
margin every five verses are used as anchors.  Long verses wrap onto the
next line without indentation, so between two anchors the shortest lines
are taken as continuations.  The few cases where this guess is wrong are
corrected by hand in the script (`MARKER_FIXES`, `STARTS`,
`CONTINUATIONS`).  Run it with `-v` to review the choices, and check the
result against the Latin text in `tmp/ilias_la_pt.txt`.

The page ranges, sizes and headings used by `extract_pt.py` and
`split_pt.py` are specific to this edition of the PDF.
