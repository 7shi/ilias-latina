# Plan for the commentary

## HANDOFF

Notes for the next session.  Read README.md, this file,
texts/README.md, texts/COMMENTARY.md (book 1), texts/NOTES.md,
texts/concordance.md (the Book divisions) and src/README.md first.

### Rules (unchanged)

- The text and verse order follow The Latin Library (LL).  The
  Portuguese translation is only a guide to the book divisions and an
  aid for checking the content; only the analysis of its line-by-line
  correspondence with LL, with short quotations, is published
  ([src/PORTUGUESE.md](src/PORTUGUESE.md)).
- Processed texts from public-domain sources may be published.  texts/
  holds four editions: Lemaire [2], Baehrens [3], Plessis [4], Vollmer
  [6].  Spondanus [1] and Butler [5] are cited only for the background.
- src/ holds the scripts; src/tmp/ holds downloads and work files and is
  not committed.  The root README does not mention src/tmp or download
  steps, and lists as requirements only uv, make, curl and poppler-utils,
  without library names.
- Files are written in English, conversation is in Japanese.  "book 1"
  for a book; a line of the *Ilias Latina* is a verse, a line of the
  *Iliad* a line.
- A script extracts a source only once; later corrections are made in
  the output files, never kept in the scripts, and `make` does not
  rebuild an existing file (order-only prerequisites).  The exception is
  texts/COMMENTARY.md with its translations COMMENTARY-en.md and
  COMMENTARY-ja.md, which are derived and rebuilt by `make commentary`
  from the files they read; they are not corrected by hand.
- The translations (`-en.md`, `-ja.md`) follow their originals one for
  one.  A correction to an original is made in its translations too;
  the COMMENTARY-en/ja.md of an edition quote the notes of its
  ilias-en/ja.md, cut at the same places as its COMMENTARY.md.
- Notation: hands as each edition prints them; a literal `<` is `\<`,
  `|` in a table `\|`.  Ask the user before settling a notation.
- Each edition's text is from its own OCR; LL is used only to decide
  which verse a row is.  The concordance compares numbers, not text.
- The book divisions may differ between editions; src/books.py (the LL
  divisions) is not changed.
- Commit only after the user has reviewed, with /commit (staged files
  only).  Do not commit on your own.
- Do not restore or fix tracked files that look changed or missing;
  ask first.  Check facts in the sources before writing them, and mark
  conjectures as such.  Modern editions and commentaries (Scaffai,
  Kennedy, Perkins, Falcone & Schubert, Green) may be cited, not copied.

### State

- Step 1 of [Preparing the sources](#preparing-the-sources) is done:
  texts/concordance.md has the table of book divisions (written by
  hand) and a verse table per book (generated once by
  src/concordance.py, `make concordance`), with the columns LL |
  Vollmer | Baehrens | Plessis | Wernsdorf | Note, each cell "own
  number (p. page)".
- src/tmp/concordance_check.txt lists the 29 rows least like LL; all
  looked like variant readings or OCR noise, none assigned to a wrong
  verse, but they are not checked against the page images.
- The differences in the book divisions and their evidence (checked
  against the page images) are in texts/README.md under Concordance >
  Book divisions.  Vollmer's list (17 = 856–858, 18 = 859–891) is taken
  to be a misprint, marked as a conjecture.  The memo src/tmp/divisions.md
  has been checked and moved there.
- Pillow is a project dependency (`uv run python` can use it).
- All four editions in `texts/` (Lemaire [2], Baehrens [3], Plessis [4],
  Vollmer [6]) have now been fully proofread and corrected against the
  page images of the original scans; the notes of Lemaire and Plessis
  were checked again for texts/COMMENTARY.md.  Consulting page images is
  no longer routinely needed and is reserved as a last resort.
- Step 2 of [Preparing the sources](#preparing-the-sources) is done:
  each edition has a `COMMENTARY.md` with the notes on the
  interpretation (without the readings and conjectures), and
  texts/COMMENTARY.md puts the verses of LL and the four editions and
  these notes together verse by verse (`make commentary`).  It is the
  material for the notes; the separate tables planned before (Vollmer's
  margin → *Iliad* lines, Plessis's index → verses, Lemaire's notes keyed
  to LL) are no longer needed.
- The files of the editions, including ilias.md (apparatus and notes;
  the verse tables are kept verbatim) and COMMENTARY.md, have English
  and Japanese translations (`-en.md`, `-ja.md`), and `make commentary`
  also builds texts/COMMENTARY-en.md and texts/COMMENTARY-ja.md from
  them.  The translations are drafts, not yet reviewed.
- texts/overview.md (with -en, -ja) sums up what the editors say about
  the poem as a whole (author, date, transmission).  It is background,
  not a source for the notes on the verses.

### Next: the pilot notes for book 1

Steps 4–5 of [Order of work](#order-of-work); confirm the format with
the user before writing much:

- Work through texts/COMMENTARY.md, book 1 (verses 1–110), and write
  what is found along the way in texts/NOTES.md: points to check,
  comparisons of the editions and conclusions, with the verse numbers of
  The Latin Library.  NOTES.md is the working record; the notes in the
  layers below are written from it afterwards.
- Settle the [Open questions](#open-questions) (directory, file format,
  language of the notes) with the user before writing the notes
  themselves.
- The *Iliad* lines of Vollmer's margin are given under his verse in
  texts/COMMENTARY.md as book.line ("1.8" for his "Α 8"); the meaning of
  his dash (probably no Homeric counterpart) is still to be checked in
  his preface.

### Page images (last resort)

- Proofreading of all four editions in `texts/` against the original page
  images is now complete.  Extracting or checking page images is no longer
  routinely necessary and should be treated as a last resort if an
  unresolved doubt or ambiguity arises.
- Images (if needed as a last resort): `src/tmp/<number>-<id>/NNN.jpg`
  (150 dpi), NNN = PDF page.
  Vollmer: printed page = PDF page − 158 (p. 1 = PDF 159); preface
  p. VII = PDF 155.
- Where unclear, render with `pdftoppm -r 300..600 -f N -l N -png` and
  crop with PIL.

How the verse-by-verse commentary on the *Ilias Latina* will be prepared.
Background on the poem as a whole (date, author, transmission) belongs in
the Background section of [README.md](README.md), not in the notes.
Numbers in brackets refer to the Internet Archive list there.

## Base text

- The Latin text of The Latin Library, numbered 1–1070, with headings
  for the 24 books (`texts/ilias.txt`).
- It stays the base text although one of the printed editions might
  seem a better choice: the text of every edition carries its own
  editorial reservations, and arranging them into a text of our own
  would in effect make a new edition and add to the confusion.  The
  differences of the editions are given in the notes instead.
- Its editorial signs are kept and explained in the notes where they
  occur: `<que>`, `<et>` (words supplied by the editor, 517, 582, 685),
  `<>` (missing verse, 791) and the asterisks at 7, 890, 1008 and 1037.
- Where the numbering differs from Scaffai's edition (597, 791, 827a; see
  [src/README.md](src/README.md)), the note says so.

## Units

- The commentary is arranged by the 24 books (see the table in
  [texts/README.md](texts/README.md)), each book introduced by a short
  summary of what it keeps from the *Iliad* and what it leaves out.
- Notes are attached to a verse or a range of verses.

## Layers of each note

The sources for all layers are gathered verse by verse in
[texts/COMMENTARY.md](texts/COMMENTARY.md).

1. **Homer**: which lines of the *Iliad* the verse renders, and whether it
   follows, compresses, changes or adds to Homer.
   - Source: the references to Homer in the notes of Wernsdorf [2],
     Plessis [4] and Vollmer [6]; the *Iliad* lines in the margin of
     Vollmer's text, given under his verse.
2. **Latin models**: echoes of Vergil, Ovid and other Latin poets.
   - Source: Wernsdorf's notes, reprinted by Lemaire [2]; the parallels
     in Plessis [4] and Vollmer [6].
3. **Names and myth**: who the persons are and where else they appear in
   the poem.
   - Source: Wernsdorf's and Plessis's notes on the persons; Plessis's
     index of names and subjects [4] (texts/4-plessis/index.md) for the
     other places.
4. **Text**: only where it matters for the sense, e.g. the editorial signs
   above, or a place where the major editions disagree (Baehrens [3],
   Plessis [4], Vollmer [6]).  No full apparatus.
5. **Language**: grammar and vocabulary that a reader needs, kept short.

## Preparing the sources

The OCR texts were originally noisy, but all four editions in `texts/`
have now been thoroughly proofread and corrected against the page images.
Consulting page images is now kept only as a last resort.

1. Verse concordance: the editions do not all number the verses in the
   same way.  Extract the text of the poem with its verse numbers from
   each edition (Lemaire [2], Baehrens [3], Plessis [4], Vollmer [6])
   and align it with The Latin Library text, noting omitted, added and
   transposed verses and differences in the book divisions.  Known so
   far: Vollmer prints 597 after 601, as Scaffai does, and 790 after
   794, prints 874 twice (in brackets after 863 and in its place),
   splits 860 around a lacuna and does not have 791; Baehrens omits 69,
   counts a lacuna as 80 (so his 69–79 are 70–80 here), and exchanges
   107 and 109 and 873 and 874; Plessis keeps the numbers, prints the
   verses he rejects below the text, puts 108 after 110 and 874 before
   873, and adds 245 bis, 827 bis and a lacuna 869 bis; Wernsdorf
   (Lemaire) counts 1075 verses, adding six (among them 827 bis) and one
   in place of 957, joining 84–85 in one verse, and putting 597 before
   595, 874 after 863 and 936 before 935.  All other tables are keyed
   to The Latin Library numbering through this concordance.  Done:
   `texts/concordance.md`, with the book divisions of the editions.
2. Notes on the interpretation: from the notes of each edition, keep
   those on the interpretation and leave out the readings of the
   manuscripts and the conjectures (`texts/*/COMMENTARY.md`), and put
   them together with the verses of the editions, keyed to The Latin
   Library through the concordance.  Done: `texts/COMMENTARY.md`.  This
   replaces the separate tables planned earlier (Vollmer's margin →
   *Iliad* lines, Plessis's index → verses, Wernsdorf's notes keyed to
   The Latin Library): Wernsdorf's labels already give the verse of The
   Latin Library, Vollmer's margin is given under his verse, and the
   index is read where needed.
3. Publish these files and the cleaned texts in the repository.  The
   sources are in the public domain, so processed texts derived from them
   can be published.

### Handling of the sources

- Organized for reference: Lemaire [2], Baehrens [3], Plessis [4] and
  Vollmer [6].  The pages on the *Ilias Latina* are first turned into
  structured text from the OCR (see [Order of work](#order-of-work) and
  [Editing the processed texts](#editing-the-processed-texts)).  The
  PDFs of [3], [4] and [6] also have a text layer that can be searched
  page by page; [2] has none, and its OCR is read from the hOCR file of
  the scan on archive.org.
- OCR text only: Spondanus [1] (text without notes, cited only as
  evidence of the attribution) and Butler [5] (a few pages on the poem).
- [3] and [6] contain several volumes or fascicles, so the pages of the
  *Ilias Latina* are located first.
- Pages are cited as printed in the book, not by the page number of the
  PDF.

### Editing the processed texts

- A script in `src/` extracts each source from its OCR only once (e.g.
  `make vollmer` for `texts/6-vollmer/`).  The OCR is left as it is, so
  the first version is uncorrected.
- From then on the files are corrected by hand, directly in place, and
  the corrections are committed.  Corrections are not kept in the
  scripts, and `make` does not rebuild a file that exists: running the
  script again would overwrite the corrections.
- Proofreading of the texts against the page images (at 150 dpi, or rendered
  at 300–600 dpi where small type was unclear) has now been completed across
  all four editions in `texts/`.  Extracting and checking page images is
  no longer needed for ordinary work and remains only as a last resort for rare
  doubtful cases.
- Conventions for the corrected text: the sigla as printed, with Greek
  letters for the editions and the archetype (Ω, α β δ φ λ); the hands
  of a manuscript as each edition prints them (superscript numerals in
  Vollmer, G¹, W²; *m. 2* in Baehrens; *m 2* in Plessis); `|` for the
  separator between readings; abbreviation marks of a manuscript kept
  where printed (e.g. *Aptũ*).  A literal `<` (angle brackets for
  supplied words, `<que>`) is written `\<` and `|` in a table `\|`, so
  that they are not taken for markup.  Signs particular to one edition
  are described in its README (e.g. Baehrens's bold 0 for the
  manuscripts together, written as a plain 0, and ς for the later
  manuscripts, in `texts/3-baehrens/README.md`).

## Layout

`src/` holds only the scripts.  The work is done in separate directories:

- `texts/` — processed texts from the public-domain sources, one
  subdirectory per book of the Internet Archive list, named by its
  number and the editor (e.g. `texts/6-vollmer/`), with the concordance
  the collected commentary (`texts/COMMENTARY.md`) and the working
  notes (`texts/NOTES.md`).  The Latin
  Library text is published here as `texts/ilias.txt`: one continuous
  file with a heading for each book, so that the divisions can still be
  adjusted.
- `commentary/` — the commentary itself, arranged by book.

Downloads and intermediate files stay in `src/tmp/`, which is not
committed.  The Portuguese translation is not in the public domain; it
was consulted for the book divisions and is used only as an aid for
checking the content.  Of it, only the analysis in
[src/PORTUGUESE.md](src/PORTUGUESE.md), with short quotations, is
published.

## Other aids

- The Portuguese translation is used only to check the understanding of
  the Latin, through the parallel text built by the tools.
- The English translation is made from the Latin and the notes of the
  editions alone, without consulting the Portuguese translation, so that
  it is not derived from it.  Only when it is finished is it compared
  with the Portuguese translation, following the list of differences in
  [src/PORTUGUESE.md](src/PORTUGUESE.md): transposed lines (75-76,
  100-101, 862-864) are compared as a range, and lines without a
  counterpart (827a, 890) are left out.  An error found by the
  comparison is corrected from the Latin and the notes, not by taking
  over the wording of the Portuguese translation.
- Butler [5] and Plessis's introduction [4] supply the points for the book
  summaries (e.g. the uneven proportions of the books).
- Modern editions and commentaries (Scaffai, Kennedy, Perkins, Falcone &
  Schubert, Green) may be consulted and cited, but not copied.

## Order of work

1. Number the verses of The Latin Library text and mark the 24 books in
   it with headings, using the
   divisions in `texts/README.md` (based on the Portuguese translation
   and checked against the Latin).  Done: `texts/ilias.txt`.
2. Organize the sources for reference, one at a time: Vollmer [6],
   Baehrens [3], Plessis [4], Lemaire [2].  The pages on the *Ilias
   Latina* are turned into structured text in `texts/` (e.g.
   `texts/6-vollmer/`), arranged by printed page and keyed to the
   verse numbers of The Latin Library: the text, the *Iliad* line
   numbers in the margin, the apparatus and notes split by verse, the
   preface, and the indexes.  The OCR text is the basis and is corrected
   by hand afterwards (see
   [Editing the processed texts](#editing-the-processed-texts)).
   Done for Vollmer (`texts/6-vollmer/`), Baehrens
   (`texts/3-baehrens/`), Plessis (`texts/4-plessis/`) and Lemaire
   (`texts/2-lemaire/`).
3. Collate the sources (steps 1–2 of
   [Preparing the sources](#preparing-the-sources)): the verse
   concordance, the book divisions of the editions (compared, not
   imposed: `src/books.py` keeps the divisions of this repository) and
   the notes on the interpretation keyed to The Latin Library
   numbering.  Done: `texts/concordance.md` and `texts/COMMENTARY.md`,
   with English and Japanese translations of the editions' files.
4. Work through `texts/COMMENTARY.md` book by book, starting with
   book 1, and record the findings in `texts/NOTES.md`.
5. Write the notes for book 1 as a pilot from them and settle the format
   of the notes.
6. Proceed book by book.

## Open questions

- The name of the commentary directory in [Layout](#layout)
  (`commentary/`).
- The output format of the commentary (one Markdown file per book, or
  data files plus a generator).
- The language of the notes.
