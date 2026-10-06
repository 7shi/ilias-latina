# Readings of the Latin

Each section of the *Ilias Latina* is read in the order of the Latin,
one word at a time, from what is already known to what is new: the
reading of the Latin text in
[commentary/METHOD.md](../commentary/METHOD.md#2-reading-the-latin).
Each sentence brings in one Latin word, which stands in it as a
loanword, and says what that word adds; a word whose sense waits on a
later one is held until that word comes. The commentary of the same
language is drawn on for identifications and for what each word does.

The readings are kept apart from the commentary under the same names,
section by section, so that the commentary and the reading of a passage
can be shown side by side.

| Directory | Contents |
|---|---|
| [ja/](ja/README.md) | The Japanese readings, made from the [Japanese commentary](../commentary/ja/README.md). |
| [en/](en/README.md) | The English readings, made from the [English commentary](../commentary/en/README.md), written fresh rather than translated from the Japanese. |

Both cover all 24 books. They were drafted by models and corrected by
hand; the README of each records the models book by book and what was
corrected.

## How they were made

Each language has an example reading of verses 1–8 written by hand
(`01/0001.md`) and an account of how it was built (`ONESHOT.md`), both
given to the model with every section, together with the commentary of
the section and the corrected reading of the previous one.

- The Japanese readings of books 1–14 were drafted through an API by
  [generate.py](generate.py), some with a review by a second model;
  from book 15 they were drafted in an agent harness.
- The English readings were drafted in an agent harness from the
  first book, five sections at a time, each batch corrected before the
  next; the drafting model reported the points it had guessed and
  could ask the reviewer while drafting.

[HARNESS.md](../HARNESS.md) describes how the harness takes the
messages and the checks of generate.py, and how the drafting and the
review were divided between two agents for the English readings.

## Use

The tools require [uv](https://docs.astral.sh/uv/) and `make`. Run
`make` in this directory for help; `READING=en` selects the English
readings (Japanese is the default).

```sh
make generate MODEL=... BOOKS=3          # draft through an API
make prompt BOOKS=3                      # tmp/prompt.md for a harness
make check BOOKS=1-24 NO_LOG=1           # check the readings
make check READING=en BOOKS=1-24 NO_LOG=1
```

`make check` applies the mechanical checks of a draft to the existing
readings. Passing it shows only that the form is right; the readings
were also read against the commentary and corrected by hand.

## Files

| File or directory | Contents |
|---|---|
| [generate.py](generate.py) | Drafts, reviews and checks the readings; writes the prompt for a harness. |
| [Makefile](Makefile) | The targets `generate`, `prompt` and `check`. |
| `ja/`, `en/` | The readings, `NN/VVVV.md` with the same filenames as in `commentary/{ja,en}/`, and the example and its construction. |
| `tmp/` | Drafts, prompts, the instruction to the harness and the logs of errors (`tmp/en/` for English); not tracked. |
