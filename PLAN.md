# Plan for the commentary

Notes for the next session.  Read README.md, this file,
texts/README.md and src/README.md first.

## Rules

- Files are written in English, conversation is in Japanese.  "book 1"
  for a book; a line of the *Ilias Latina* is a verse, a line of the
  *Iliad* a line.
- The Latin Library (LL, texts/ilias.txt) stays the base text, with its
  numbering and book divisions (src/books.py is not changed).  Arranging
  the editions into a text of our own would make a new edition; their
  differences go into the notes.
- The Portuguese translation is not in the public domain: it is only a
  guide to the book divisions and an aid for checking the content, and
  of it only src/PORTUGUESE.md, with short quotations, is published.
  The English translation is made without consulting it and is compared
  with it only when finished; an error found is corrected from the Latin
  and the notes, not from its wording.
- A script extracts a source only once; later corrections are made in
  the output files, never in the scripts, and `make` does not rebuild an
  existing file.  The exception is the derived files rebuilt by `make`
  in texts/ (COMMENTARY.md, COMMENTARY-en/ja.md, iliad.md), which are
  not corrected by hand.
- The translations (`-en.md`, `-ja.md`) follow their originals one for
  one; a correction to an original is made in its translations too.
- Notation: hands as each edition prints them; a literal `<` is `\<`,
  `|` in a table `\|`.  Ask the user before settling a notation.
- Check facts in the sources before writing them, and mark conjectures
  as such.  Modern editions and commentaries (Scaffai, Kennedy, Perkins,
  Falcone & Schubert, Green) may be cited, not copied.
- The root README does not mention src/tmp or download steps, and lists
  as requirements only uv, make, curl and poppler-utils.
- Commit only after the user has reviewed, with /commit (staged files
  only).  Do not restore or fix tracked files that look changed or
  missing; ask first.

## State

- The four editions in texts/ have been proofread against the page
  images.  Page images are a last resort: `src/tmp/<number>-<id>/NNN.jpg`
  (150 dpi, NNN = PDF page; Vollmer p. 1 = PDF 159), or render with
  `pdftoppm -r 300..600` and crop with Pillow.
- texts/alignment.tsv was reviewed book by book against the Greek
  (2026-09-27); only 62 is left uncertain.  The Greek is downloaded by
  `make homer` and not committed; `make greek` in src/ builds
  src/tmp/greek.md, from which the user intends to translate into
  English section by section.
- The English and Japanese translations of the editions' files are
  drafts, not yet reviewed; texts/commentary.tsv was made from the
  English drafts before any review.
