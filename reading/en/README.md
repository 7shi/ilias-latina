# English readings of the Latin

Each section of the *Ilias Latina* is read in English in the order of
the Latin, one word at a time, from what is already known to what is
new. The Latin words are embedded in English sentences as loanwords,
and the [English commentary](../../commentary/en/README.md) is drawn
on for the content. The method is that of the
[Japanese readings](../ja/README.md); the readings are written fresh
from the English commentary, not translated from the Japanese ones.

The readings are drafted in an agent harness from the first book, with
`make prompt READING=en` and `make check READING=en` giving it the
messages and the checks of [generate.py](../generate.py);
[HARNESS.md](../../HARNESS.md) describes the pattern, and
[PLAN.md](PLAN.md) the plan these readings follow.

## Production and review

| Model | Contribution |
|---|---|
| Claude Opus 5.5 | Wrote the example reading [01/0001.md](01/0001.md) and its step-by-step construction [ONESHOT.md](ONESHOT.md), wrote the English prompts of generate.py and the instructions to the harness, and corrected the readings by hand after generation. |
| Gemini 3.8 Flash | Drafted the readings in the Antigravity CLI, without review. |

| Book | Draft | Review | Correction |
|---|---|---|---|
| 1 | Gemini 3.8 Flash (Antigravity CLI) | — | Claude Opus 5.5 |

The raw output of each batch is committed before its corrections.

Book 1 was drafted in three batches, and the rules and the instruction
to the harness were revised after each from what had been corrected.
All readings passed the mechanical checks, mostly at the first attempt;
the corrections were of what the checks cannot see.

The first trial (verses 9–43) followed the rules carried over from the
Japanese readings, and showed habits of its own. Sentences ended in an
appended phrase that restated them ("an ejection demanded with
*excedere*"); words with *-que* were treated as connecting words
("joined by *spernitque*"); small words were brought in alone beside the
word they lead ("advancing with *per*"); words were held back several
at a time, in terms of the grammar ("with their noun still waiting");
and Latin was slotted into English phrases ("directing it *in me*").
Four words were misconstrued: *Pelasgum*, which goes with *regi* in the
next line; *Chrysenque*, the one Atrides orders out; *Fatidici*, the god
whose ears are addressed; and *sum*, given a sense the Latin does not
have.

In the second trial (verses 44–57), after these were added to the rules,
none of them recurred. A verb at the end of a section (*hortatur*) was
read as if complete, though the one it urges (*Thestoriden*) and what he
is urged to do (*edere*) come in the next section; an identification
repeated a name given in the same line (Thestorides and *Calchas*); and
the content of later words was told before they came.

The rest of the book (verses 58–110) was drafted in one batch. The
earlier habits were gone, but nearly every section told the content of
a later word in advance, the sentence of each word saying what the next
would say (*Tandem* read as "Peace returns", which is *resedit*). A
person was named before the patronymic and then identified (*ferus
Aeacides*), and a few words were turned the other way: *largis*, the
lavish feast, read as the feast revealed as lavish, and *letum
crudele*, the death Achilles threatens, read as one he will inflict.
The section of Juno's protest (98–105) needed most of its sentences
rewritten.

## Files

| File or directory | Contents |
|---|---|
| `NN/VVVV.md` | The reading of a section, with the same filename as in [commentary/en/](../../commentary/en/README.md): `NN` is the two-digit book number and `VVVV` the four-digit first Latin verse number. |
| [01/0001.md](01/0001.md) | The example reading of verses 1–8, given to the model with every section. |
| [ONESHOT.md](ONESHOT.md) | How the example reading was built, step by step; also given to the model. |
| [PLAN.md](PLAN.md) | The plan for the English readings. |

The drafts, the prompt of the harness, its instruction and the errors
of failed `make check` runs (`errors.tsv`) are kept locally in
`../tmp/en/`, which is not tracked.
