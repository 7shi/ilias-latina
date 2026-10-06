# Plan for the English readings

Notes for the sessions that work on `reading/en/`. Read this file,
[../ja/README.md](../ja/README.md), [../ja/ONESHOT.md](../ja/ONESHOT.md),
[../../HARNESS.md](../../HARNESS.md) and [../generate.py](../generate.py)
first. The work is in progress: [README.md](README.md) records the books
done and what was corrected, and the steps below say how to go on.

## Aim

An English counterpart of the Japanese readings in `reading/ja/`: each
section of the *Ilias Latina* read in English in the order of the Latin,
one word at a time, from what is already known to what is new, with the
Latin words embedded in English sentences as loanwords. The reader knows
no Latin and reads beside the English translation and commentary of
[commentary/en/](../../commentary/en/README.md). The method is the one
of `reading/ja/ONESHOT.md`; only the language of the reading changes.

The readings are written fresh from the English commentary, not
translated from the Japanese readings.

## Inputs

- `commentary/en/NN/VVVV.md`: the same sections as `commentary/ja/`
  (same files, same verse groups), each with the Latin verses, the
  English translation in parentheses `> (...)`, and the commentary.
  The check of a quoted translation (`TRANS_RE`) already accepts `(`.
- [commentary/en/proper_noun.md](../../commentary/en/proper_noun.md):
  the English forms of the names (for example *Pelides*, *Orcus*). The
  readings use the same forms as the English commentary.
- The example `en/01/0001.md` and its construction `en/ONESHOT.md`,
  written by hand (see step 2 below).

## Drafting from the start in the harness

The Japanese readings were first drafted through the API and moved to
an agent harness from book 15. The English readings are drafted in the
harness (the Antigravity CLI, Gemini 3.8 Flash, on its subscription
quota) from the first book, following [HARNESS.md](../../HARNESS.md):

- `make prompt` writes the messages of the next missing section to a
  prompt file; the harness writes the reading and runs `make check`
  until it passes, one section at a time.
- The instruction to the harness lives in a file of its own, not in the
  prompt file, which `make prompt` overwrites.
- `make check MODEL=...` logs failed checks to `errors.tsv`; checks run
  only to inspect use `NO_LOG=1`.
- Token usage is not recorded; the harness shows its own quota.

## Steps

### 1. Generalize generate.py for a language

`generate.py` is written for Japanese. Add a language option (`--lang
ja|en`, default `ja`) and keep the Japanese behaviour byte for byte:
before changing anything, save `make prompt` output for a few Japanese
sections and compare it after the change.

What depends on the language:

| Item | Japanese | English |
|---|---|---|
| Commentary | `../commentary/ja` | `../commentary/en` |
| Output | `ja/` | `en/` |
| Example and construction | `ja/01/0001.md`, `ja/ONESHOT.md` | `en/01/0001.md`, `en/ONESHOT.md` |
| Prompts (`INTRO`, `RULES`, `REVIEW_INTRO`, `FLAGS`, ...) | about a Japanese reading | about an English reading |
| Identification sentence (`IDENT_RE`) | 「解説が述べるとおり、…。」 | for example "As the commentary says, …." |
| Paragraph opening with the commentary (`flags`) | starts with 解説 | starts with "The commentary" |
| Drafts, prompt file and logs in `tmp/` | as now | kept apart, for example under `tmp/en/` |

Keep `tmp/` paths of Japanese as they are; the English ones must not
collide with them (drafts `tmp/NN/VVVV.md`, `tmp/prompt.md`,
`errors.tsv` keyed by `NN/VVVV.md`).

In the Makefile, pass the language with a variable that is not `LANG`
(the locale variable of the environment), for example `READING=en`.
`make prompt`, `make check` and `make generate` all take it.

The English prompts are not translations of the Japanese ones word for
word: the rules name Japanese forms (「…と名指される」, 「まだ明かされない」)
that need English equivalents settled from the English example.

### 2. Write the English example and construction by hand

Claude writes `en/01/0001.md` (verses 1–8) and `en/ONESHOT.md`, the
English counterparts of `ja/01/0001.md` and `ja/ONESHOT.md`, and the
user reviews them before any drafting. As in Japanese, every sentence
of the example is quoted in the construction, in order.

Points to settle in the example:

- Known to unknown: put what the reader already has at the start of the
  sentence and the new Latin word at the end ("The poem begins with a
  man's anger. That anger is the opening *Iram*."). English end-focus
  suits this.
- Latin as loanwords inside English grammar: no broken macaronic, no
  Latin word slotted in place of an English one ("then, *deinde*, he
  throws").
- No word-talk: not "the word for 'wrath' is *Iram*", "the verb
  *pande*", "*superbi* means proud". No quoted glosses.
- Varied sentence endings, the English counterparts of 「*X* と呼ばれる／
  名指される／描かれる」 ("is called *X*", "is named *X*", "is described
  as *X*"), without one ending repeated sentence after sentence.
- Holding back a word whose noun comes later ("but what is grievous is
  not yet said") only over a distance. "Never for a word one or two
  words away" would contradict *summi* … *regis* and *Latrantum* …
  *rostris*, held in both examples; [ONESHOT.md](ONESHOT.md) settles it
  as holding back only where something else is read before the partner
  comes.
- The editor's mark of doubt on *protulerant\** noted briefly, as in
  the Japanese example.
- One identification from the commentary, at the name *Achilles* in
  line 8 for the *Pelidae* of line 1, as in the Japanese example.
  [ONESHOT.md](ONESHOT.md) settles it in English, without the Latin
  word as its subject: "the son of Peleus in line 1 is this Achilles".
- Check every rule of step 3 against the example: the Japanese rules
  twice contradicted the Japanese example (the endings 「…が *X* である」
  and the note on the mark of doubt), and the readings were corrected
  against rules the example did not follow until this was found. The
  English example ends at most one sentence a paragraph with "… is
  *X*", the counterpart of 「…が *X* である」, and the rule says the
  same.

### 3. Write the English prompts and the harness instruction

Write the English prompts from the settled example, then the first
instruction to the harness (for example `tmp/en/harness.md`). Carry
over, in English form, what the Japanese readings needed corrected,
since the same model will draft them:

- no grammatical terms ("preposition", "negative", "conjunction",
  "genitive", "main clause", "case"); a word is brought in by what it
  does in the story;
- no talk of punctuation ("after the semicolon");
- no word-talk ("the word for keel gives *carinas*"); no enclitic
  brought out as a word beside its word ("together with *-que*,
  *uastumque*"), though *-que* alone may be woven into a sentence of
  connection as the example does;
- identifications do not make the Latin word just read their subject
  ("As the commentary says, this *Pelasgi* means the Greeks" was
  corrected to "the Pelasgians are the Greeks"), do not repeat what the
  verse says (*Troianus Apollo*), and are made once a book. The
  Japanese example itself identifies 「1行目の *Pelidae*」, a word met
  seven lines earlier; the English example identifies the son of Peleus
  of line 1 where the name comes in line 8, and the rule allows an
  identification to look back to an earlier line;
- check from the commentary's translation which noun an adjective goes
  with and whom a pronoun or a possessive refers to (*ultrix* with
  *dextera*; *ille* as Achilles; *patriae* as the father's);
- a word whose noun comes in the next line, or in the next section, is
  held there and joined there (*suis* … *equis*; *totis* … *aquis*);
- no colour the Latin does not give ("grievous wounds" for *uulnera*);
- lost lines (`\<>`) and places the commentary calls damaged are said
  to be lost or damaged, as the commentary says, not described by their
  editorial signs; a word marked with the editor's doubt is noted
  briefly as in the example; variant readings of other editors are not
  mentioned;
- the closing sentence that says a held pair has come together only
  after a word held back over a distance, once a section; no closing
  that goes over the Latin again; no "this ends the book" except at the
  end of a book;
- reread for broken sentences (a sentence ending on a bare word: "is
  placed with *per*.") and typos.

### 4. Try book 1 and settle the method

Run the harness on the first sections of book 1, review them against
the commentary, and adjust the prompts, the example or the instruction
before going on. Report the findings to the user before running the
remaining books.

### 5. Book by book

As with the Japanese readings:

1. The user runs the harness for a book.
2. Claude checks it (`make check READING=en BOOKS=N NO_LOG=1`), reads
   every section against the English commentary, and commits the raw
   output.
3. Claude corrects by hand and commits the corrections separately.
4. Claude records the model and what was corrected in
   `reading/en/README.md`.
5. Claude updates the harness instruction for the next book with what
   was corrected.

## Files to create

| File | Contents |
|---|---|
| `en/README.md` | The aim, the models, a table by book, and what was corrected, as in `ja/README.md`. |
| `en/ONESHOT.md` | How the example was built, step by step. |
| `en/01/0001.md` | The example reading of verses 1–8, written by hand. |
| `en/NN/VVVV.md` | The reading of each section, with the same filename as in `commentary/en/`. |
