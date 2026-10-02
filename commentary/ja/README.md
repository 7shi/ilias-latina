# Japanese translation and commentary

The Japanese translation of the English *Ilias Latina* translation
and commentary is complete and checked in all 24 books. It was made
by Gemini 3.8 Flash from the English alone, then compared with the English and
the Japanese edition notes and proper-name indexes.

Its book directories, sections and summaries correspond to those in
[en/](../en/README.md). The Latin verses and their numbering are
retained; the translation and commentary are in Japanese. The shared
editorial policy and source data are described in
[commentary/README.md](../README.md).

## Production and review

| Model | Contribution |
|---|---|
| GPT-6 Astra | Created the English translation and commentary used as the source. |
| Claude Opus 5.5 | Structured the English translation. |
| Gemini 3.8 Flash | Translated the English translation and commentary into Japanese. |
| GPT-6.1 Sol | Proofread the Japanese version, organized the proper-name tables and maintained the review records and directory guides. |

GPT-6.1 Sol checked the Japanese translation, commentary and summaries
in all 24 books against the English version, edition notes and
proper-name indexes. It investigated inconsistent name mappings in
[proper_noun.md](proper_noun.md), checked their occurrences and Japanese
katakana conventions, and corrected the table and running text while
preserving distinctions between Latin and Greek forms and namesakes.

It subsequently checked the reported differences in the draft notes
against the originals, corrected Japanese and English errors, and
propagated the reviewed corrections to the curated TSVs and edition
files in `texts/`. The decisions and scope of that review are recorded
in [PROOFREADING.md](PROOFREADING.md).

GPT-6.1 Sol separated the table's Latin, English and Japanese columns,
created the corresponding English table and translated its categories
and descriptions. It removed the contents lists from both tables and
moved the verse ranges from the Japanese headings into the text below
them. It also archived completed work in `DONE.md` and `PROOFREADING.md`,
kept pending work in `PLAN.md`, and wrote the directory guides.

## Files

| File or directory | Contents |
|---|---|
| `01/`–`24/` | One directory for each book. Read its numbered section files in order. |
| `NN/VVVV.md` | A section with the same filename as its English counterpart: `NN` is the two-digit book number and `VVVV` the four-digit first Latin verse number. It contains a heading with Latin and Homeric references, the Latin verses with a Japanese translation under each, then commentary on the section. |
| `NN/README.md` | The Japanese translation of the English book summary. It is distinct from this directory guide. |
| [proper_noun.md](proper_noun.md) | Proper names recorded by book, with separate Latin, English and Japanese columns, explanations and verse references; it corresponds to the [English table](../en/proper_noun.md). |
| [DONE.md](DONE.md) | Completed translation, checking, TSV preparation and propagation procedures and history. |
| [PROOFREADING.md](PROOFREADING.md) | Settled Japanese forms, corrections by book, and source-based decisions on reported draft differences, including English errors found during that review. |

The reviewed Japanese edition notes and proper-name index are
[commentary-ja.tsv](../commentary-ja.tsv) and
[index-ja.tsv](../index-ja.tsv) in the parent directory. Their
corrections have also been carried over to the corresponding edition
files in [texts/](../../texts/README.md).
Current work is recorded in [PLAN.md](../../PLAN.md).
