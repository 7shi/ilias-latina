# Completed Japanese commentary work

Translation, checking and propagation to texts/ are complete for all
24 books. This archives their procedures and completion history from
PLAN.md and PROOFREADING.md; the procedures below are records of the
completed workflow. Current work and shared rules remain in
[PLAN.md](../../PLAN.md). Settled forms and individual corrections are
recorded in [PROOFREADING.md](PROOFREADING.md).

## Translation and TSV review

For the Japanese, commentary/commentary-ja.tsv and
commentary/index-ja.tsv have been made, row for row with their English
counterparts, from the editions' Japanese drafts:

- commentary-ja.tsv takes, for each note of commentary-en.tsv, the
  Japanese of the same item in texts/notes-ja.md (374 notes).  The 122
  notes that commentary-en.tsv had adapted (joined across pages,
  excerpted with "…", Wernsdorf's verse numbers given in LL numbers,
  remarks on readings added) were adapted in the same way from the
  full Japanese in the edition's ilias-ja.md, by hand; all have now
  been read against the English rows. The reported non-name draft
  meaning differences have now been checked against the originals,
  corrected where necessary and recorded in the proofreading log.
- index-ja.tsv takes, for each row of index-en.tsv, the Japanese
  headword and description of the same row of the edition's
  INDEX-ja.tsv.  Its names began as the drafts'; the forms reviewed
  for all 24 books have now been unified throughout the index.

The Japanese translation with a commentary in commentary/ja/ is
finished in all 24 books: translated section by section from the
English by Gemini without looking at commentary-ja.tsv and
index-ja.tsv (see [Translating into Japanese](#translating-into-japanese)),
mechanically checked against commentary/en/ (headings, Latin verses,
paragraph counts), with proper names recorded book by book in
[proper_noun.md](proper_noun.md).

All 24 books have been checked. Completed checks and corrections are
recorded by book in [PROOFREADING.md](PROOFREADING.md).
The finalized Japanese names have also been carried over to the editions'
files in texts/, and notes-ja.md has been rebuilt with `make notes`.

The completed stages formerly listed under Next in PLAN.md:

1. [Done] commentary/ja/: the Japanese translation of commentary/en/,
   finished in all 24 books, with proper names recorded book by book in
   [proper_noun.md](proper_noun.md).
2. [Done] commentary/ja/, commentary-ja.tsv and index-ja.tsv are checked
   against each other, and the TSVs corrected (the names above all,
   and the 122 adapted notes; see [Checking the Japanese](#checking-the-japanese)).
3. [Done] The corrections have been fed back to texts/: the notes to the editions'
   ilias-ja.md and COMMENTARY-ja.md, the index rows to INDEX-ja.tsv and
   index-ja.md; then `make notes` in texts/.
4. [Done] The reported draft meaning differences and the English
   discrepancy at 677 have been reviewed, resolved and recorded in
   commentary/ja/PROOFREADING.md.

## Translating into Japanese

Each file of commentary/en/ is translated into Japanese and written to
commentary/ja/ under the same name: the sections `NN/VVVV.md` and the
summaries `NN/README.md`.

- Book by book, the files of a book in order.  A file that already
  exists in commentary/ja/ is skipped, so that an interrupted run
  resumes where it left off.
- The Japanese follows the policy in commentary/README.md, as the
  English does, and the forms of
  [The forms settled](../en/PROOFREADING.md#the-forms-settled).
- Not read: commentary/commentary-ja.tsv, commentary/index-ja.tsv and
  the Japanese files in texts/ (`*-ja.md`, `INDEX-ja.tsv`,
  notes-ja.md).  The Japanese is made from the English alone, so that
  it can be checked against them afterwards (see
  [Checking the Japanese](#checking-the-japanese)).
- Written only in commentary/ja/ (including commentary/ja/proper_noun.md); no other
  file is changed, and nothing is committed.

The form:

- The structure of each file is kept exactly: the heading, the
  quotation block with every verse, then the commentary, paragraph for
  paragraph.
- Heading: `### 1–8 (*Iliad* 1.1–7)` becomes `### 1–8（『イリアス』1.1–7）`.
- Verses: each `> N Latin` line is kept unchanged, and the English line
  under it, `> (…)`, is replaced by the Japanese in full-width
  parentheses, `> （…）`; the lines with `>` alone between the verses
  are kept.
- Each verse is translated from its English line with the words of
  that verse only, even where a sentence runs over and the Japanese
  becomes less natural; no word is moved to another verse.  Where the
  English is ambiguous, the Latin quoted above it decides.
- The commentary: every sentence is translated, nothing added and
  nothing left out, in plain written Japanese in the である style.
  “…” becomes 「…」 and titles 『…』 (*Iliad* 1.5 becomes 『イリアス』1.5);
  Latin words stay in Latin, in italics as in the English
  (*Mavortius*).

The names: heroes and peoples in the usual Japanese forms from the
Greek, the gods in their Roman forms, as the English does.  Long
vowels are generally left out (ホメロス, not ホメーロス; ヘクトル), but
where a form with a long vowel is the one in common use, it is
preferred (ムーサ, ユノー).  The same person is always written the same
way, in the verses and in the commentary.

The Japanese forms are recorded in
[Japanese proper-name forms](PROOFREADING.md#japanese-proper-name-forms).

At the end of each book, its proper names are recorded in
commentary/ja/proper_noun.md in a section for that book, with their English or
Latin forms, Japanese katakana, category/explanation, and verse
numbers.  The files written are reported, with every name not in the
recorded list of Japanese forms and the Japanese form chosen for it,
so that the forms can be checked before the next book.

## Checking the Japanese

When Gemini has finished (or finished a range of books), the checking
is taken over here, followed by propagation to texts/:

1. The files are committed as Gemini wrote them ("Add commentary/ja/NN/,
   … as translated by Gemini"), before any correction, so that the
   history keeps the two apart.
2. **Against the English.**  A mechanical first pass: the same files,
   headings and verses as commentary/en/, each `> N Latin` line
   unchanged, one `> （…）` under each, the same number of paragraphs.
   Then each section is read against the English: nothing added or
   left out, each verse with its own words only, the headings and
   quotation marks as in [Translating into Japanese](#translating-into-japanese).
3. **The names.**  The names in commentary/ja/proper_noun.md and those found in
   the files are checked with their verses and files; each person or
   people has one form, following the rules above,
   [Japanese proper-name forms](PROOFREADING.md#japanese-proper-name-forms)
   and [The forms settled](../en/PROOFREADING.md#the-forms-settled).
   A form not in the recorded list is decided with the user and added to it.
4. **Against the TSVs.**  commentary/ja/ is compared with
   commentary-ja.tsv and index-ja.tsv, as the English was with
   index-en.tsv (see [Checking](../en/DONE.md#checking), 2): the Japanese headwords
   and the names in the descriptions of index-ja.tsv are made to agree
   with the translation, not the other way round, all the rows of a
   headword getting the same Japanese; the 122 adapted notes of
   commentary-ja.tsv are read against their English rows.  A Japanese
   note or description whose sense differs from the English is
   reported rather than corrected, except for the names, unless the
   user authorizes a source-based review. The completed review is recorded in
   [Japanese proofreading](PROOFREADING.md#reviewing-the-reported-draft-differences).
   Draft material outside the reviewed items keeps the report-first policy.

The problems are reported before anything is edited, as a table
(verse, file, the passage, the English or the TSV row, a proposed
correction), in a form agreed with the user first.  The corrections of
commentary/ja/ and of the TSVs they entail are committed by book or
range of books.

After checking, carry the corrections over as for the English (see
[Carrying the names over to texts/](../en/DONE.md#carrying-the-names-over-to-texts)):
the diff of index-ja.tsv goes to the editions' INDEX-ja.tsv (the
Japanese headwords and the names in the descriptions) and index-ja.md
(the names in the descriptions only), after checking that each
headword has one Japanese form; the corrections of commentary-ja.tsv
go to the edition's ilias-ja.md and COMMENTARY-ja.md; then `make notes`
in texts/, committed apart from commentary/.

## Carrying the corrections over to texts/

The finalized Japanese names have been carried over to the editions'
INDEX-ja.tsv and index-ja.md, and to ilias-ja.md and COMMENTARY-ja.md.
All 1,371 verse-bearing source index rows were matched using the
concordance, their Latin headwords and quoted forms; the two Nereides
rows at LL 874 were distinguished by their descriptions. Cross-reference
headwords use the settled forms of the corresponding names.

Corrections from 240 reviewed TSV notes were matched to their source
items. Full notes retain their original numbering and wording, rather
than being replaced by the adapted commentary excerpts. Roman and Greek
name forms follow the context. Non-name draft meaning differences were
left unchanged in that propagation; they were subsequently examined in
[the subsequent review](PROOFREADING.md#reviewing-the-reported-draft-differences).
`make notes` in texts/ rebuilt notes-ja.md from the
corrected edition files. The source index rows and descriptions were
checked against the reviewed TSVs; Latin and Greek quotations, numbers,
verse tables, headings and note labels were verified unchanged.
