# English translation and commentary

The English translation of the *Ilias Latina* with commentary is
complete and checked in all 24 books. It follows the text and verse
numbering of The Latin Library. The commentary explains the story,
its characters and its relationship to Homer's *Iliad*.

The text was checked against the Latin,
the editions' notes, the Greek, the proper-name indexes and the
Portuguese translation. The shared editorial policy and source data
are described in [commentary/README.md](../README.md).
The corresponding Japanese files are described in
[ja/README.md](../ja/README.md).

## Production and review

| Model | Contribution |
|---|---|
| GPT-6 Astra | Created the English translation and commentary. |
| Claude Opus 5.5 | Structured the English translation. |
| Gemini 3.8 Flash | Translated the English translation and commentary into Japanese. |
| GPT-6.1 Sol | Performed subsequent proofreading, organized the proper-name tables and maintained the review records and directory guides. |

During the Japanese review, GPT-6.1 Sol checked reported differences
against the sources and corrected English errors found in the notes
and commentary. It propagated the reviewed corrections to the curated
TSVs and the corresponding edition files in `texts/`. The decisions
and scope of that review are recorded in
[PROOFREADING.md](PROOFREADING.md) and the linked Japanese review log.

GPT-6.1 Sol also separated the Latin and English columns of the Japanese
proper-name table, checked the English forms in the corresponding books,
and created [proper_noun.md](proper_noun.md). It translated the Japanese
categories and descriptions for all 24 books and 1,026 entries, removed
the contents lists from both tables and placed verse ranges below the
book headings. It organized completed work in `DONE.md` and
`PROOFREADING.md`, kept pending work in `PLAN.md`, and wrote the
directory guides.

## Files

| File or directory | Contents |
|---|---|
| `01/`–`24/` | One directory for each book. Read its numbered section files in order. |
| `NN/VVVV.md` | A section, named after its first Latin verse: `NN` is the two-digit book number and `VVVV` the four-digit verse number. It contains a heading with Latin and Homeric references, the Latin verses with an English translation under each, then commentary on the section. |
| `NN/README.md` | A summary of the book, prepared as context for generating the next book. It is distinct from this directory guide. |
| [proper_noun.md](proper_noun.md) | Latin names and expressions, their English renderings, categories and descriptions, and locations by book; the corresponding Japanese table also supplies Japanese forms. |
| [DONE.md](DONE.md) | Completed generation, checking and propagation procedures, with the review status. |
| [PROOFREADING.md](PROOFREADING.md) | Settled forms, differences between the editions, and specific proofreading observations and decisions. |

The curated edition notes and proper-name index used for generation
and checking are [commentary-en.tsv](../commentary-en.tsv) and
[index-en.tsv](../index-en.tsv) in the parent directory. They are
separate from the section commentary read alongside the translation.
Current work is recorded in [PLAN.md](../../PLAN.md).
