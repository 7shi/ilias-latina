# Plan for the commentary

Notes for the next session.  Read README.md, this file,
texts/README.md and src/README.md first.

## Current work

1. The indexes of proper names in texts/ are in order:
   texts/4-plessis/INDEX.tsv and texts/6-vollmer/INDEX.tsv, the indexes
   of Plessis and Vollmer as tables of headword, verse, form and
   description (see the README of each; Lemaire and Baehrens have no
   index).  Both index.md files have been compared letter by letter
   with the page images (texts/PROOFREADING.md, step 8).  Their rows,
   with INDEX-en.tsv and INDEX-ja.tsv, are placed at their verses in
   texts/notes{,-en,-ja}.md.
2. Next the proper names in commentary/ are checked with them.  The
   indexes should have been in notes-en.md when commentary/ was
   generated and checked; they were added afterwards, so all 24 books
   are checked against them now (see [Checking the names](#checking-the-names)).
3. When the names are done, deploying the translation as a website is
   to be considered.

### Checking the names

The sections (commentary/NN/VVVV.md) are checked against the rows of
their verses in commentary/index.tsv (see commentary/README.md, Index),
which gives the rows of the indexes as texts/notes-en.md does,
with the headword, its English, the form and the description in
columns of their own.  The check is made in two passes, kept apart:

A. **The names** (notation), over all the books at once, headword by
   headword:
   - the name in the translation agrees with the English headword of
     the row ("Ulysses", "Ajax", "Greeks") and follows the policy in
     commentary/README.md.  Where the policy keeps a patronymic or a
     name as it is (Atrides, Pelides, Cytherea) and the headword is the
     person ("Agamemnon") or a gloss ("son of Peleus"), the translation
     keeps the Latin and only the person is checked (in B);
   - the same person or people is called the same way throughout, in
     the translation (106 *Ignipotente* "the fire god" but 862
     "Ignipotens"; *Myrmidones* for the Greeks at large, 23, 180) and
     in the commentary's explanations ("Pallas is Athena" or Minerva);
   - the name the row cites appears in the translation of its verse,
     not only as a gloss (108 *Olympo* "the sky", while the commentary
     speaks of "Olympus").
   A difference is reported with which side seems wrong: the
   translation, or the English headword of INDEX-en.tsv (added by hand,
   following the translations).  The decisions taken here (one form
   for each person) are applied in all the books.
B. **The content**, book by book, verse by verse:
   1. **The person**: the one the translation and the commentary mean
      is the one the headword gives, above all for patronymics,
      epithets and periphrases (Atrides, Aeacides, *Priami filius*,
      *Pelopea iuventus*, Cytherea) and for homonyms (Acamas 1 and 2,
      Aiax Locrus and Telamonius).
   2. **The word**: the form the row cites is translated in its own
      verse, not moved to another.
   3. **The commentary**: what it says of the person (descent, people,
      who kills whom) agrees with the description.

- index.tsv keeps the rows on readings that The Latin Library does not
  have (151 *Pelasgi*, 195 *Nireus*) and the rows of a range at its
  first verse; whether a row applies is judged here.
- Where Plessis and Vollmer identify a person differently, both are
  listed without deciding between them.
- A mechanical first pass is allowed (e.g. counting the verses with
  index rows whose translation lacks the headword-en); its script stays
  in the scratchpad unless the user wants it kept.
- The problems are reported before anything is edited, as in steps 3
  and 4 below: in A headword by headword (the forms found, with their
  verses and files, and a proposed form), in B book by book (verse,
  file, the passage, the index row, which of 1–3, a proposed
  correction).
- An index row that seems wrong is checked in the edition's index.md
  and ilias.md (the page images as a last resort) and reported.  It is
  corrected in the data, not in a script: in double braces in index.md
  and index-{en,ja}.md, without braces in INDEX*.tsv, and then
  `make notes` in texts/; commentary/index.tsv is corrected by
  hand in the same way.
- The translations of the indexes are drafts, not yet reviewed: a
  description whose English differs from the Latin is reported, not
  corrected.
- Giving the index rows to commentary/generate.py as context for any
  later generation may be proposed, not implemented.
- Corrections of the translation and commentary are committed by book
  or range of books; corrections of the data in separate commits.

## The commentary

The translation with a commentary in commentary/ (see its README) has
been checked in all 24 books and compared with the Portuguese
(books 1–3, 4–6, 7–9, 10–15, 16–20 and 21–24 in `git log`).  The
spelling is American throughout.  The steps followed, for any book to
be regenerated or checked again:

1. The user runs `make generate MODEL=gpt-6-astra` in commentary/ (the
   API key is in the user's shell, not here), and the generated files
   are committed as they are ("Add commentary/NN/, … as generated by
   gpt-6-astra").
2. Every section and the summary `NN/README.md` of a book are checked
   against the Latin, commentary/commentary.tsv and the Greek
   (src/tmp/greek.md, which gives each section's verses with the lines
   of the *Iliad*; the verse ranges of the books are in
   texts/books.tsv): the accuracy of the translation, the glosses
   followed, no uncertain reading stated as fact, and agreement with
   the books before.  Frequent errors in the drafts:
   - a sentence that runs over into the next verse translated twice or
     garbled, or cut by a full stop and resumed with "and";
   - words moved to another verse: each verse is translated with its
     own words only, even if the English is less natural;
   - names in the Latin form (*Vlixes*, *Danai*), which the drafts keep
     because they were generated before the English forms were adopted
     (see the policy in commentary/README.md; books 1–3 show the forms
     in use), and explanations that become circular once the name is
     in English ("the Danaans are the Danaans");
   - a claim that the Latin omits what comes in the next or the
     previous section;
   - genealogies; *Myrmidones* for the Greeks at large (23, 180), to be
     treated the same way throughout.
3. The translation is then compared with the Portuguese
   (src/tmp/ilias_la_pt.txt, the Latin and Portuguese line by line,
   minding the differences in src/PORTUGUESE.md).  The problems are
   reported first; nothing is edited until the user asks.
4. The corrections are made in the files; the user stages and commits
   them with /commit ("Correct the translation and commentary of book
   N", listing the verses).
5. The first section of a book was generated from the summary of the
   previous book before its correction; it is checked with the
   corrections of that summary in mind.

A note in commentary/commentary.tsv that seems wrong is checked before the
translation follows or departs from it.  The notes are the English
drafts of the editions' Latin (or French) notes, and the bracketed
glosses of a lemma were added in the drafts, not by the editors (338,
*suas*: "his own" for "her own").  The note is compared with the
original in the edition's `ilias.md` in texts/ (and with the page
images if the text itself is in doubt).  A note is corrected only
where its English or Japanese differs from the original (a wrong
gloss, a changed reference); an original that is itself mistaken or
open to question is left as it is, since the translation does not
have to follow it.  Such a difference is reported with the
translation's problems, and when the user agrees it is corrected in
every copy: commentary/commentary.tsv, the edition's
`ilias-en.md` and `ilias-ja.md`, and its `COMMENTARY-en.md` and
`COMMENTARY-ja.md` (kept by hand); then `make notes` in texts/
rebuilds the derived texts/notes*.md.  Sections already
translated after the wrong note are corrected too.

## Rules

- Files are written in English, conversation is in Japanese.  "book 1"
  for a book; a line of the *Ilias Latina* is a verse, a line of the
  *Iliad* a line.
- The Latin Library (LL, texts/ilias.txt) stays the base text, with its
  numbering and book divisions (texts/books.tsv is not changed).  Arranging
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
  in texts/ (notes.md, notes-en/ja.md, iliad.md), which are
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
- commentary/alignment.tsv was reviewed book by book against the Greek
  (2026-09-27).  The Greek is downloaded by
  `make homer` and not committed; `make greek` in src/ builds
  src/tmp/greek.md, the input of commentary/generate.py.
- The English and Japanese translations of the editions' files are
  drafts, not yet reviewed; commentary/commentary.tsv was made from the
  English drafts before any review (see the checking of notes under
  Current work).
