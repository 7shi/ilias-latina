# Running a generation script through a harness

A pattern for having an agent harness (a coding agent with its own
model, such as the Antigravity CLI) do the work of a script that calls a
model through an API, while the script keeps what must stay
deterministic. It was worked out for the Japanese readings of
[reading/](reading/), whose [generate.py](reading/generate.py) drafts
each section through an API; from book 15 the readings were drafted
in a harness instead, on its subscription quota.

## Division of work

| Part | Script | Harness |
|---|---|---|
| Building the context of each item | yes | |
| Calling the model | | yes |
| Checking the answer | yes | |
| Retrying after a failed check | | yes |
| Logging the errors | yes | |

The script assembles exactly what it would send through the API and
judges the result; the harness only supplies the model and the loop of
writing, checking and correcting.

## The contract

1. **The prompt is a file.** `make prompt` writes the messages of one
   item to `tmp/prompt.md`, as they would be sent through the API, and
   the harness is told to read only that file. A harness that gathers
   its own context reads different things each time.
2. **The prompt names the output.** It ends with an instruction to write
   the answer to a given path in a given form (here the heading of the
   section, a blank line and the reading), so the result is a file of
   the project like any other.
3. **The check is a command.** `make check` runs the checks the script
   applies to an answer from the API, prints the errors and exits with
   a non-zero status if any fails. The harness runs it and corrects the
   file until it passes; the exit status, not the agent's report, is
   what counts as done.
4. **One item at a time.** The prompt of an item holds the output of the
   previous one, so the harness runs `make prompt` again for each item
   instead of writing several at once.
5. **The check logs.** Each failed check is appended to `tmp/errors.tsv`
   in the same form as the failed rounds of the script, with the model
   given as `MODEL=` and the number of the check, so the retries of the
   harness can be compared with those of the script. Checks run only to
   inspect the results use `NO_LOG=1`.

## The instruction to the harness

The instruction given to the harness is short and mostly about scope:

- the loop: run `make prompt`, write the file it names, run
  `make check` until it passes, repeat until there is nothing to make;
- read only `tmp/prompt.md`, write only the output files, change no
  script and run no git command;
- a final `make check` over the whole batch.

It also carries the corrections found in the previous batch, as rules
with an example of the rejected and the accepted form. A harness adds
its own habits to the output (in book 15, grammatical terms such as
「前置詞」 that the script's drafts never used); a habit seen once is
added to the instruction, and in this project none recurred after it
was.

## Drafting and review by two agents

The English readings of [reading/en/](reading/en/README.md) add a
second agent to the pattern: one harness drafts, and another reviews,
corrects and commits. The aim is to leave as few oversights as
possible rather than to save work. The two agents run in panes of a
terminal multiplexer, herdr, and send prompts to each other:

```sh
herdr agent prompt ilias-agy "..."     # the reviewer instructs the drafter
herdr agent prompt ilias-claude "..."  # the drafter reports or asks
```

### The drafter's instruction

The instruction is a file, `reading/tmp/en/harness.md` (not tracked),
written by the reviewer and read again by the drafter at each batch.
Besides the loop and the scope above, it holds:

- **The batch.** The book and its number of sections; five sections
  per batch, then stop and report. The previous section in each prompt
  is then always a corrected one, so the drafter's habits do not spread
  through a book.
- **A check before drafting.** For each section, list every point of
  the Latin not settled beyond doubt by the commentary's translation:
  which noun an adjective goes with, what a case depends on, whom a
  pronoun refers to, whether an identification is new, whether a line
  without a full stop runs on into the next section.
- **Asking is part of the work.** Where a point is not settled, ask the
  reviewer before writing that section, with the reading proposed. A
  passing `make check` does not show that the Latin was read correctly.
- **The report.** At the end of a batch, a final `make check` and a
  report naming the sections written and a list headed `Guessed:` of
  every point settled by guessing, one item each (section, Latin words,
  reading chosen), even when the drafter thinks the guess right.
- **The lessons.** The corrections of earlier books as rules, and a
  contrast table of the corrections that recur, each row a sentence of
  a draft, its correction and the reason. Rows are added from each
  batch.

### Rebuilding the instruction file

The file is not tracked; these are its parts, enough to write it
again. `N` is the book, `VVVV` a section.

1. **Opening.** Make the English readings for book N (its number of
   sections and first verse), in batches of five; this batch, the next
   five missing sections, then stop and report.
2. **Steps.** (1) `make prompt READING=en BOOKS=N`; (2) read
   `tmp/en/prompt.md`, list the doubtful points (adjective and noun,
   case, ellipsis, what *-que* or *et* joins, pronoun, identification),
   check them against the commentary's translation, ask if any is
   unsettled, then write `reading/en/NN/VVVV.md`; (3)
   `make check READING=en VERSE=V MODEL=gemini-3.8-flash` until it
   passes, and look over what it lists without failing; (4) back to
   (1), stopping after five sections or at "Nothing to generate".
3. **Notes.**
   - Asking: "Asking is part of the work, not an exception to it", with
     the misreadings of earlier books that passed the check as the
     reason; ask with
     `herdr agent prompt ilias-claude "Question: <section, Latin words, readings weighed>"`
     and stop until the answer comes as a new prompt.
   - One section at a time, in order; read only the instruction and
     `tmp/en/prompt.md`; write only `reading/en/NN/`; change no script,
     commentary or existing reading; run no git command.
   - Reread each section for broken sentences and typos; say that the
     book ends only in its last section ("which ends the Nth book as
     *X*").
   - At the end, `make check READING=en BOOKS=N NO_LOG=1`, then
     `herdr agent prompt ilias-claude "Book N batch done: sections VVVV-VVVV written, make check all ok. Guessed: <list>"`,
     every guessed point one item (section, Latin words, reading
     chosen), "Guessed: none" if none.
4. **Rules from the corrections**, each with a rejected and an accepted
   sentence:
   - Bring in a word in a plain form matched to it: a verb "told with
     *X*", an adjective or participle "described as *X*", a noun
     "named *X*", a name or title "called *X*", a phrase with a
     preposition or a pair "given as *X*", an adverb or connective
     "marked by *X*", a pronoun "as *X*", the last word "which closes
     the line as *X*".
   - Tell nothing before its word, for the whole clause: at a subject,
     pronoun, adverb, place word or connective say only who or what
     comes in ("Night comes in as well, named *noxque*", not "Night
     also approaches").
   - Hold an adjective until its noun ("though what it is is not yet
     said"), at most two holds a group; when a clause runs on past the
     section, end with "... comes only in the next section", checking
     the next verse whenever a line has no full stop.
   - Identify only as the commentary does ("As the commentary says,
     ..."), after the word identified; take nothing else from its
     interpretation.
   - No talk of grammar or word order, no verb made its own subject, no
     Latin slotted into an English phrase or put in apposition, no
     opening sentence restating the previous section; a word with
     *-que* is one word; editorial signs escaped (*Crethona\<que>*).
5. **Contrast table.** A table of `Not (draft) | But (corrected) | Why`,
   started from the recurring corrections and extended after each
   batch, with the instruction to check every sentence against it
   before finishing a section.

### The reviewer's loop

For each report:

1. Run `make check READING=en BOOKS=N NO_LOG=1` and list the new files
   with `git status`.
2. Read each reading beside the commentary's translation, word by
   word, and the commentary's identifications; check every point of
   the `Guessed:` list.
3. Commit the raw output as it is ("Generate the English readings of
   book N, verses A–B").
4. Correct by hand: small corrections as exact substitutions, larger
   ones by rewriting the prose of a section; check again, including
   that no group holds more than two words back.
5. Commit the corrections separately ("Correct the English readings
   of book N, verses A–B", with a summary of what was fixed).
6. Add rows to the contrast table for any correction likely to recur.
7. Send the next batch, naming the kinds of correction just made.

A question from the drafter is answered after checking the Latin
construction and the commentary, before the drafter goes on; an answer
given without that check was the source of one later correction.

At the end of a book, the reviewer adds the book to the table and the
account of
[reading/en/README.md](reading/en/README.md) (what the drafts got
wrong, what was corrected, how the drafter's guesses and questions
fared), commits it, and switches the instruction to the next book.

### What made it work

- The raw commits keep the drafter's output, so the corrections can be
  counted and described per book.
- The contrast table brought the corrections from rewriting most
  sentences down to a few words a batch; the instructions alone had
  not.
- The drafter did not report its guesses, nor ask, until told that the
  list is for guesses it thinks right and that asking is part of the
  work. Its guesses were then right throughout, and from book 14 it
  asked while drafting, about the points most often misread.

## Limits

- The harness's own system prompt and tools shape the output, and the
  checks catch only what is mechanical; the output is still read and
  corrected by hand.
- The usage of tokens is not recorded. Here it was recorded only to keep
  within free quotas, and a harness shows its own remaining quota.
- The harness must be trusted to keep to its scope; the instruction
  says so, and `git status` shows whether it did.

## In this project

```sh
cd reading
make prompt BOOKS=18                         # tmp/prompt.md for the next section
make check VERSE=839 MODEL=gemini-3.8-flash  # check one section, logging errors
make check BOOKS=18 NO_LOG=1                 # inspect a book without logging
make prompt READING=en BOOKS=16              # the same for the English readings
make check READING=en BOOKS=16 NO_LOG=1
```

See [reading/ja/README.md](reading/ja/README.md) for the models used and
how the readings drafted in the harness compared with those drafted
through the API.
