# Proofreading

A record of how the texts of the four editions were taken from the OCR
and proofread against the page images.  Times are in JST (UTC+9).

## Sources

Each edition was extracted once from the OCR that comes with its
Internet Archive scan; no new OCR was made.  The page images used for
proofreading were rendered from the same scans.

| Edition | Directory | Internet Archive ID | OCR used | Read by |
|---|---|---|---|---|
| Lemaire | [2-lemaire/](2-lemaire/README.md) | `poetaelatinimin00unkngoog` | hOCR (`_hocr.html`, ABBYY) | `src/lemaire.py` |
| Baehrens | [3-baehrens/](3-baehrens/README.md) | `poetaelatinimino34baeh` | text layer of the PDF | `src/baehrens.py` (`pdftotext -bbox-layout`) |
| Plessis | [4-plessis/](4-plessis/README.md) | `italiciiliaslati00plesuoft` | text layer of the PDF | `src/plessis.py` (`pdftotext -bbox-layout`) |
| Vollmer | [6-vollmer/](6-vollmer/README.md) | `p1poetaelatinimi02baeh` | text layer of the PDF | `src/vollmer.py` (`pdftotext -bbox-layout`) |

The PDF of Lemaire's scan has no text layer, so its hOCR is read
instead.  The text of The Latin Library ([ilias.txt](ilias.txt)) is
used only to number the verses; it is not OCR.

## History

### 1. Extraction (Claude Opus 5.5, 2026-09-25 07:00–18:03)

The OCR of each edition was organized into Markdown by page and verse
and committed as it was:

- `d45de65` Vollmer
- `78e5c68` Baehrens
- `0555775` angle brackets escaped in Vollmer and Baehrens
- `634980d` Plessis
- `d4b266e` Lemaire
- `a944e9a` verse concordance and book divisions

### 2. Proofreading begun (Claude Opus 5.5, 2026-09-25 18:15–18:46)

The aim was to make the repository self-contained, so that the page
images in `src/tmp` need not be consulted: the texts were corrected
against the images, but only where a reading could not be inferred from
the text, to save tokens (see [Prompts](#prompts)).

- Vollmer: `ilias.md` (pp. 1–55), `preface.md` (pp. V–IX) and
  `index.md` (pp. 61–65).
- Baehrens: `ilias.md` up to p. 26.

The session stopped at the usage limit while loading p. 27 of
Baehrens.  Nothing was committed.

### 3. Proofreading continued (Gemini 3.8 Flash, 2026-09-25 19:10 – 09-26 02:27)

Started from the uncommitted changes with the same prompt, and so with
the same limit on the checking.

- Baehrens: `ilias.md` pp. 27–59, then `preface.md` (pp. 3–7).
- Plessis: `preface.md`, `introduction.md`, `ilias.md` and `index.md`.
- Lemaire: `prooemium.md`, `testimonia.md`, `ilias.md` and
  `excursus.md`.
- `texts/README.md`, `texts/*/README.md` and `PLAN.md` updated to
  record the proofreading as complete.

Committed together with the changes of step 2 as `bbef34c`.

### 4. Translation, and corrections found by it (2026-09-26 03:23–16:26)

The texts were then translated into English (`-en.md`) and Japanese
(`-ja.md`).  Translating reads every word, so this served as a further
proofreading: errors left by steps 2 and 3 came to light and were
corrected against the page images, in the originals and in the
translations.

- `77308d9` (Claude Opus 5.5) translations of every file except
  `ilias.md`: the prefaces, introductions, prooemium, testimonia,
  excursus and indexes.
- `5a6d254` (Claude Opus 5.5) Plessis's `introduction.md`: OCR errors
  found in translating it are corrected against the page images, and
  the corrections are carried into `introduction-en.md` and
  `introduction-ja.md`.
- `f63941c` (Claude Opus 5.5) Plessis's `introduction-en.md` and
  `introduction-ja.md`: the translation of Havet's gloss.
- `830186d` (Claude Opus 5.5) errors found in the notes while the
  `COMMENTARY.md` files were made from them.  Lemaire's `ilias.md`: the
  notes on pp. 515–610 rewritten from the page images, with misread
  labels corrected and notes 216, 222, 463 and 646 separated from the
  preceding notes.  Plessis's `ilias.md`: the Greek quotations,
  references to the *Iliad*, names and labels in the Notes corrected.
- `fd3eb3f` (Gemini 3.8 Flash) translations of the apparatus, notes and
  testimonia in `ilias.md` of the four editions, made from the
  corrected notes.
- `f76ee86` (Claude Opus 5.5) translations of the `COMMENTARY.md` files,
  quoting the notes from `ilias-en.md` and `ilias-ja.md`; four spurious
  ellipses in Lemaire's `COMMENTARY.md` are removed.

### 5. Plessis's index as a table, and errors found by it (Claude Opus 5.5, 2026-09-28)

Plessis's index was made into `4-plessis/INDEX.tsv` (see
[4-plessis/README.md](4-plessis/README.md#indextsv)), with the form of
each cited verse taken from `ilias.md`.  Looking the forms up in the
verses showed that the text of Plessis's verses still has many OCR
errors.  About 70 words were corrected against the page images, in
`ilias.md`, `ilias-en.md` and `ilias-ja.md`: the forms cited by the
index, and the other misreadings on the same verses or seen on the
same pages (pp. 6–8, 11, 13–15, 19, 21, 23–26, 28–29, 31, 33, 35, 38,
41–42, 46, 50, 52, 54, 56, 84).

Since a wrong verse number in the index would make `INDEX.tsv` point to
the wrong verse, every verse number of `index.md` was then compared
with the page images of the index (pp. 87–98, all of them).  One was
misread: "340" for 346 (PANDARUS).  Two errors in the words were seen
on the way: "[107]" for "[— 107]" (OLYMPUS) and "dextra" for
"dextera" (TROICUS).  They are corrected in `index.md`, its
translations and `INDEX.tsv`.

### 6. Plessis's verses against the page images (Gemini 3.8 Flash, 2026-09-28)

The words of Plessis's verses (`4-plessis/ilias.md`) not in the
vocabulary of The Latin Library (compared in lower case, with j as i,
v as u, and a final -que removed) were listed, 365 words in 281 verses
after step 5, and each was checked against the page image.  The
misreadings were corrected in `ilias.md`, `ilias-en.md` and
`ilias-ja.md` (`f2c7570`), and `make commentary` rebuilt the
`COMMENTARY*.md` files (renamed `notes*.md`, built by `make notes`,
since the rows of the indexes were put in them with the items of the
commentaries).

- About 200 words in 159 verses on 47 pages (pp. 4–84), most of them
  in verses 1–750, such as `dcserit` (*deserit*), `Yenerat` (*Venerat*)
  and `Admonuilque` (*Admonuitque*); words run together or split by
  the OCR are divided or joined (`Pronato` for *Pro nato*); the *O*
  dropped by the OCR at 257 and 1028 is supplied; and at 817 and 1047
  the OCR's `Occurrit` and `supremumque` give way to the printed
  *Ocurrit* and *supremaque*.
- In the Printed column, "/180" for 485 and "5/io" for 545.
- The list is reduced to 174 words in 152 verses.  These are left as
  printed: Plessis's readings and spellings (*Ipsorum*, *discordi*,
  *cominus*, *jocundaque*, *Saltim*) and his supplement at 245 bis.

In reviewing this step (Claude Opus 5.5), the corrections doubted
were compared with the page images, and all agreed with them.  One
error was found: the margin numbers 440 and 480, read by the OCR into
the text as "MO" and "hSO", had been deleted from the text but not
put in the Printed column; they are restored there.  Misreadings that
make words of The Latin Library cannot be found by this list and may
be left.

### 7. Vollmer's index as a table (Claude Opus 5.5, 2026-09-28)

Before Vollmer's index was made into `6-vollmer/INDEX.tsv` (see
[6-vollmer/README.md](6-vollmer/README.md#indextsv)), every verse
number of `index.md` was compared with the page images of the index
(pp. 56–65, all of them); all were read correctly.  One word was
found to differ: "robora" for the misprint "rubora" (Epistrophus 1),
which the OCR had read as "nibora"; it is restored as printed in
`index.md` and its translations.  The same list as in step 6 of the words
of the verses not in The Latin Library, run on Vollmer's `ilias.md`,
has 89 words in 84 verses; all are his spellings and readings
(*inmensa*, *exultat*, *Tlepolomus*, *Pallados*, *Latiis*), with no
misreadings among them.  Looking the cited words up in the
verses showed places where the index itself does not agree with the
text (Amaryncides 337 for 377, Doris 874 for 873, Phoebus 69 for 68,
*Troica* at 645 where the text has *Troiae*); they are kept as
printed and listed in the README.

### 8. The words of both indexes against the page images (Claude Opus 5.5, 2026-09-28 – 09-29)

Every page of both indexes was rendered from the PDF (Plessis at 400
dpi, Vollmer at 600 dpi), cut into the two columns and each column into
three parts, and read letter by letter against `index.md`: spellings,
diacritics, italic remarks, dashes, brackets, asterisks and
punctuation.  Where a mark was doubtful, the place was enlarged; to
catch what the eye had passed over, the words of `index.md` were also
aligned with the text layer of the PDF, and every place where only the
punctuation differed was looked at in the image.  No verse number
changed.

- Plessis (pp. 87–98): a colon printed where `index.md` had a
  semicolon after 205-6 (AJAX), 454 (AENEAS), 510 (AGAMEMNON), 532
  (MINERVA), 556 (DIOMEDES) and 815 (HECTOR), and a comma after 820
  (HECTOR); "ad loq." at 322 (MENELAUS); "Cf." at NEREIUS and after 947
  (MINERVA); no period after TENTHREDO's "Prothous"; "amisso, planctu"
  at 1016 (TROJA); the dash before "in agmine" after 281 (TROJANI).
- Vollmer (pp. 56–65): *Cythereă* (for *Cythereā*), *Ilĭŏn* (for
  *Iliŏn*) and *Σύμηθεν* (for *Συμηθεν*).
- Misprints of the index are now corrected in double braces instead of
  being kept as printed: Plessis's {{Amphimachus}}, {{MESTHLES}},
  {{naves}}, {{Idomeneus}} and {{Ithacus}}, and Vollmer's {{robora}}
  (restored as "rubora" in step 7); see the READMEs.  The dash printed
  twice across a line break at PIROUS 378 is written once.
- Left as they stand: a few marks after "inclusos", "hasta",
  "interposito" and "interfecto" (Plessis) that may be periods or
  commas with the tail worn away, kept as commas, and the misprinted
  verse numbers of Vollmer's index listed in step 7.

The corrections are carried into `index-en.md`, `index-ja.md` (where
they quote the Latin or change the sense) and the description column
of `INDEX.tsv`.  Each description was then looked up in `index.md`
with the pages joined; those not found verbatim are the rows whose
brackets are closed within the row, as the READMEs describe.

### 9. The misprinted verses of the indexes corrected (Claude Opus 5.5, 2026-09-29)

The verses that the indexes misprint, kept as printed until now
(steps 5 and 7), are corrected in double braces in `index.md` and its
translations: Plessis's ACHILLES {{938}} (printed 937) and COROEBUS
{{249}} (250), and Vollmer's Amaryncides {{377}} (337), Doris {{873}}
(874) and Phoebus {{68}} (69).  The phrases that run on into the next
verse (Agamemnon 10) are not misprints and stay as printed.  The rows
of `INDEX.tsv` and its translations now give all the corrections of
the indexes, the words of step 8 too, without braces.

## Status

| File | Proofread by | Translated by |
|---|---|---|
| `6-vollmer/ilias.md` | Claude (step 2) | Gemini |
| `6-vollmer/preface.md`, `index.md` | Claude (step 2); the index against the images by Claude (steps 7 and 8) | Claude |
| `3-baehrens/ilias.md` | Claude to p. 26, Gemini from p. 27 | Gemini |
| `3-baehrens/preface.md` | Gemini | Claude |
| `4-plessis/preface.md`, `index.md` | Gemini; the index against the images by Claude (steps 5 and 8) | Claude |
| `4-plessis/introduction.md` | Gemini, corrected by Claude (`5a6d254`) | Claude |
| `4-plessis/ilias.md` | Gemini; the Notes corrected by Claude (`830186d`), the verses by Claude (step 5) and Gemini (step 6) | Gemini |
| `2-lemaire/prooemium.md`, `testimonia.md`, `excursus.md` | Gemini | Claude |
| `2-lemaire/ilias.md` | Gemini; the notes corrected by Claude (`830186d`) | Gemini |

In steps 2 and 3 only the readings that the model judged uncertain were
checked against the images.  Step 10 records the subsequent full image
recheck of every OCR source page, including prefaces, notes and indexes.

## Open issues

The OCR source pages listed in step 10 have all been checked against
their images.  A few readings that may be errors in the printed edition
or may represent a manuscript reading remain marked in the corresponding
source text.

### 10. Full image recheck of OCR sources (Codex, 2026-10-05)

Every page containing OCR source text was compared with its page image,
including prefaces, introductions, testimonia, verse text, apparatus and
notes, excursus, and indexes.  Confirmed OCR mismatches were corrected
in the source text and corresponding translations; suspected errors in
the printed editions are marked there with double braces.

| Edition | OCR source pages checked against images |
|---|---|
| Lemaire/Wernsdorf | PDF 463–630: prooemium, testimonia, *Ilias* and excursus |
| Baehrens | PDF 7–63: preface and *Ilias* with apparatus |
| Plessis | PDF 15–17, 19–65, 68–151, 153–164: preface, introduction, *Ilias* with notes, index |
| Vollmer | PDF 152–223: preface, *Ilias* with testimonia and apparatus, index |

`COMMENTARY.md` files are extracts from the corresponding `ilias.md`;
their included quotations were checked with those source pages.
Translations and derived tables are not OCR sources and were not
independently rechecked as translations.

## Prompts

The prompts were given in Japanese; they are translated here.

Steps 2 and 3 were set as a long-running goal (`/goal`):

> This repository refers to the images of the PDFs in src/tmp whenever
> something is unclear.  That way it is not self-contained in the files
> of the repository, so proofread, by looking at the images, the data in
> @texts/ that cannot be judged as typos or omissions.  However, checking
> everything against the images would consume an absurd number of
> tokens, so limit it to what cannot be inferred.

To Gemini the goal was given again with one more sentence:

> The work has partly progressed, so first check the situation with git
> status and git diff before proceeding.

The following prompts in step 3 moved on to the other editions and
closed the work:

> Likewise, proceed with proofreading @texts/4-plessis.

> Next, proofread @[texts/2-lemaire] in the same way.

> Reflect the results of the corrections in each of the READMEs in
> texts/*/README.md (fix the places quoted still garbled, etc.)

> @[PLAN.md] Basically there should no longer be any need to extract
> images from the PDFs and check them.  Write that the proofreading is
> done, and position checking the images as something like a last
> resort.

## Lessons

Looking back at the errors that were left, the prompts could have been
better in these ways.

- **Say what needs checking, rather than leaving it to judgment.**
  "What cannot be inferred" was decided by the model page by page.  The
  verses, which can be compared with The Latin Library, were checked
  well, but OCR errors in prose, notes and Greek often look plausible
  and were passed over.  A concrete list would have left less to
  judgment: every Greek word, every number and label (verse numbers,
  note labels, references to the *Iliad*), every siglum, and every word
  not in a Latin dictionary.
- **Name the whole scope.**  "Proofread @texts/" and "likewise" do not
  say that the notes, introductions and indexes count as much as the
  verses.  Listing the files and the parts of each file (verses,
  margins, apparatus, notes) would have made the omissions visible.
- **Ask for a record of what was checked.**  Without a list of the pages
  checked and the doubts left open, "done" could not be verified.  A
  per-page log, kept in the repository, would also have made the
  handoff from one model to another explicit instead of relying on
  `git diff`.
- **Do not declare completion before a review.**  The last prompt had
  the model write in PLAN.md that the proofreading was done, before
  anything had been checked independently.  A second pass by another
  model, or a sample of pages checked against the images, should come
  first.
- **Save tokens by triage, not by skipping.**  The cost can be kept down
  by first marking the suspicious places mechanically (non-Latin
  words, broken numbers, stray symbols) and then looking at the images
  only for those, rather than by letting the model decide what to skip.
