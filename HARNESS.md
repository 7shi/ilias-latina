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
```

See [reading/ja/README.md](reading/ja/README.md) for the models used and
how the readings drafted in the harness compared with those drafted
through the API.
