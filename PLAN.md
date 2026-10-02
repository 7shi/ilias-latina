# Plan for the commentary

Notes for the next session.  Read README.md, this file,
commentary/README.md, texts/README.md and src/README.md first.

## Current state and next work

The English and Japanese translations with commentary are complete
and checked in all 24 books. Reviewed names and notes have been carried
over to the corresponding edition files in texts/, and the derived
notes and local Greek context have been rebuilt.

Completed checks and decisions are recorded in
[English proofreading](commentary/en/PROOFREADING.md) and
[Japanese proofreading](commentary/ja/PROOFREADING.md).
The editions' other translated material remains draft material outside
the names and individual items reviewed.

## Review of the reported draft differences

The reported draft differences have been resolved; the decisions are in
[Japanese proofreading](commentary/ja/PROOFREADING.md#reviewing-the-reported-draft-differences).

## Next

Stop before website work. The user has further checks to make first;
wait for those instructions before starting the website.

## Completed workflows

The completed generation, translation, checking and propagation steps
are archived in [English DONE.md](commentary/en/DONE.md) and
[Japanese DONE.md](commentary/ja/DONE.md). Individual proofreading
decisions remain in the logs linked above.

## How the present state is built

Each step depends only on the ones before it.

### 1. The texts

- The Latin Library (LL, texts/ilias.txt) is the base text, with its
  numbering and book divisions (texts/books.tsv).
- The Portuguese translation (Almeida, Coimbra 2021, on Scaffai's
  edition), from a PDF the user has, is extracted and paired with LL
  line by line by `make pt` in src/ (src/tmp/ilias_la_pt.txt, not
  committed); `make check-pt` confirmed that the pairing holds
  throughout, and src/PORTUGUESE.md records the places where the
  translation departs from LL (75–76 and 100–101 transposed, 827a,
  864, 890).  The book divisions of texts/books.tsv follow it, except
  book 15 (see texts/README.md, Books).
- The four editions (Lemaire, Baehrens, Plessis, Vollmer) are
  extracted by the scripts in src/, once, into texts/, and proofread
  against the page images (texts/PROOFREADING.md).  texts/concordance.md
  relates their verses to LL.
- Their English and Japanese translations (`ilias-{en,ja}.md`,
  `COMMENTARY-{en,ja}.md`, `index-{en,ja}.md`, …) remain drafts outside
  the names and individual items reviewed in commentary/ja/PROOFREADING.md.

### 2. The indexes

- Plessis and Vollmer have indexes of proper names (Lemaire and
  Baehrens have none).  Their index.md is compared letter by letter
  with the page images (texts/PROOFREADING.md, step 8) and turned into
  INDEX.tsv: headword, verse, form and description (see the README of
  each edition).
- INDEX-en.tsv and INDEX-ja.tsv are made from INDEX.tsv and
  index-{en,ja}.md by texts/index_translations.py.
- `make notes` in texts/ places the verses of the editions, their
  commentaries and the rows of their indexes side by side, verse by
  verse, in texts/notes{,-en,-ja}.md.

### 3. The data for the commentary

In commentary/, made by hand or once from texts/notes-en.md and
corrected by hand from then on (see commentary/README.md):

- alignment.tsv: the lines of the *Iliad* each verse renders
  (`make homer` in src/ downloads the Greek, not committed); it has
  been reviewed book by book against the Greek;
- commentary-en.tsv: the notes of the editions that apply to the text of
  LL;
- index-en.tsv: the rows of the indexes of Plessis and Vollmer at their
  verses, with the headword, its English, the form and the
  description in columns of their own.

### 4. The sections

`make greek` in src/ builds src/tmp/greek.md from LL, alignment.tsv
and commentary-en.tsv: the sections of the poem, each with its verses,
the lines of the *Iliad* they render, the notes that apply and the
Greek.

The subsequent generation, checking and propagation workflow is recorded
in [English DONE.md](commentary/en/DONE.md#generation); the Japanese
translation and checking workflow is recorded in
[Japanese DONE.md](commentary/ja/DONE.md#translating-into-japanese).

## Correcting the data

- A note in commentary-en.tsv that seems wrong is checked against the
  original in the edition's `ilias.md` (and the page images if the
  text itself is in doubt) before the translation follows or departs
  from it.  The notes are the English drafts of the editions' Latin
  (or French) notes, and the bracketed glosses of a lemma were added
  in the drafts, not by the editors (see the
  [individual note example](commentary/en/PROOFREADING.md#individual-note-example)).
  A note is corrected only where its English or Japanese
  differs from the original; an original that is itself mistaken or
  open to question is left as it is, since the translation does not
  have to follow it.  When the user agrees, it is corrected in every
  copy: commentary-en.tsv, the edition's `ilias-{en,ja}.md` and
  `COMMENTARY-{en,ja}.md`; then `make notes` in texts/.  Sections
  translated after the wrong note are corrected too.
- An index row that seems wrong is checked in the edition's index.md
  and ilias.md (the page images as a last resort) and reported.  It is
  corrected in double braces in index.md and index-{en,ja}.md, without
  braces in INDEX*.tsv, and by hand in commentary/index-en.tsv; then
  `make notes` in texts/.
- The translations of the editions' files remain drafts outside the
  checked items. Other draft differences are reported before correction;
  completed decisions are kept in the English and Japanese proofreading
  logs linked above.

## Rules

- Files are written in English, conversation is in Japanese.  "book 1"
  for a book; a line of the *Ilias Latina* is a verse, a line of the
  *Iliad* a line.
- LL stays the base text, with its numbering and book divisions
  (texts/books.tsv is not changed).  Arranging the editions into a
  text of our own would make a new edition; their differences go into
  the notes.
- The Portuguese translation is not in the public domain: it is only a
  guide to the book divisions and an aid for checking the content, and
  of it only src/PORTUGUESE.md, with short quotations, is published.
  The translation is made without consulting it and is compared with
  it only when finished; an error found is corrected from the Latin
  and the notes, not from its wording.
- A script extracts a source only once; later corrections are made in
  the output files, never in the scripts, and `make` does not rebuild
  an existing file.  The exception is the derived files rebuilt by
  `make` in texts/ (notes.md, notes-en/ja.md, iliad.md), which are not
  corrected by hand.
- The translations (`-en.md`, `-ja.md`) follow their originals one for
  one; a correction to an original is made in its translations too.
- Notation: hands as each edition prints them; a literal `<` is `\<`,
  `|` in a table `\|`.  Ask the user before settling a notation.
- Check facts in the sources before writing them, and mark conjectures
  as such.  Modern editions and commentaries (Scaffai, Kennedy,
  Perkins, Falcone & Schubert, Green) may be cited, not copied.
- The spelling of the English is American.
- The root README does not mention src/tmp or download steps, and lists
  as requirements only uv, make, curl and poppler-utils.
- Page images are a last resort: `src/tmp/<number>-<id>/NNN.jpg` (150
  dpi, NNN = PDF page; Vollmer p. 1 = PDF 159), or render with
  `pdftoppm -r 300..600` and crop with Pillow.
- Problems are reported first; nothing is edited until the user asks.
  Commit only after the user has reviewed, with /commit (staged files
  only).  The generated files, the corrections of the translation and
  the commentary (with the corrections of index-en.tsv they entail), and
  the corrections of the data in texts/ are committed separately.
  Do not restore or fix tracked files that look changed or missing;
  ask first.
