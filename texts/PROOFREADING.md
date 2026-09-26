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

## Status

| File | Proofread by | Translated by |
|---|---|---|
| `6-vollmer/ilias.md` | Claude (step 2) | Gemini |
| `6-vollmer/preface.md`, `index.md` | Claude (step 2) | Claude |
| `3-baehrens/ilias.md` | Claude to p. 26, Gemini from p. 27 | Gemini |
| `3-baehrens/preface.md` | Gemini | Claude |
| `4-plessis/preface.md`, `index.md` | Gemini | Claude |
| `4-plessis/introduction.md` | Gemini, corrected by Claude (`5a6d254`) | Claude |
| `4-plessis/ilias.md` | Gemini; the Notes corrected by Claude (`830186d`) | Gemini |
| `2-lemaire/prooemium.md`, `testimonia.md`, `excursus.md` | Gemini | Claude |
| `2-lemaire/ilias.md` | Gemini; the notes corrected by Claude (`830186d`) | Gemini |

In steps 2 and 3 only the readings that the model judged uncertain were
checked against the images.  Every file has since been read through in
translation, but the files and parts not corrected in step 4 have not
been checked against the images again.

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
