"""Revise the generated readings of the Latin against the rules of generate.py.

Usage: python review.py -m MODEL (-b BOOKS | --verse VERSE)

Each reading ja/NN/VVVV.md is sent to the model with the example, the
reading of the previous section, the commentary of the section and
REVIEW_PROMPT, which repeats the form and manner of generate.py.  The
answer is the revised reading followed by a list of the changes; the
reading replaces the file once it passes the same check as a generated
one, and the list is saved as tmp/NN/VVVV.md.  The example is not
revised, and a section whose list is there already is skipped, so an
interrupted run resumes where it left off.
"""

import argparse
import sys
from pathlib import Path
from llm7shi import Client
from llm7shi.usage import append_usage, find_usage_file, print_today_totals

from generate import (
    COMMENTARY, EXAMPLE, FORM, MANNER, PREVIOUS, ROOT, Section,
    check, example, read_sections, select_books,
)

LOG = ROOT / "tmp"

REVIEW_PROMPT = """
<commentary> is a section of book {book} of the Ilias Latina from a
Japanese translation with commentary.  <reading> is a Japanese reading of
the Latin of this section, made by a model with the rules below, for a
reader who does not know Latin and reads it beside the translation and the
commentary.  <example> gives the commentary and the reading of the first
section, written by hand, as the standard.

Revise <reading> where it breaks the rules.  Keep every sentence that
already follows them as it is; change only those that do not, and do not
add or remove content beyond what the rules require, and keep the groups
of verses and their headings as they are.  Look in particular for:

- a quoted gloss before a Latin word (「ついにと *Tandem* で」「それからと
  いう *inde* とともに」), above all with adverbs and connectives;
- a Latin word met for the first time made the topic or subject
  (「*X* が告げる」「*X* が示す」「*X* が描く」「*X* が明かす」);
- 「解説が述べるとおり」 used for what the verses say themselves, or for
  more than the commentary says;
- an identification already made in <previous>, made again (one that
  <previous> does not state in words is not made yet and is kept);
- a sentence that is broken, unclear or says one thing twice;
- a misreading of the Latin.

Answer with the whole revised reading in the same form, without the
heading of the section, then a line `=== CHANGES ===`, then a list in
Japanese of what was changed and why, one item per change (`- なし` if
nothing).

{form}

{manner}
""".strip()

SEPARATOR = "=== CHANGES ==="

# Set the path only when usage should be recorded
USAGE_PATH = None


def log_path(sec: Section) -> Path:
    return LOG / sec.rel


def review(client: Client, sec: Section, messages: list[str], rounds: int) -> bool:
    prompt = REVIEW_PROMPT.format(book=sec.book, form=FORM, manner=MANNER)
    commentary = f"<commentary>\n{sec.text}\n</commentary>"
    body = sec.path.read_text().strip().split("\n", 1)[1].strip()
    reading = f"<reading>\n{body}\n</reading>"
    for round_no in range(1, rounds + 1):
        print(f"\n--- {sec.heading} (round {round_no}) ---")
        text = client([*messages, commentary, reading, prompt]).text
        answer, sep, changes = text.partition(SEPARATOR)
        answer, errors = check(answer, sec.verses)
        if not sep:
            errors.append("no list of changes")
        if not errors:
            sec.path.write_text(f"{sec.heading}\n\n{answer}\n")
            log = log_path(sec)
            log.parent.mkdir(parents=True, exist_ok=True)
            log.write_text(f"{sec.heading}\n\n{changes.strip()}\n")
            print(f"\nSaved to {sec.path} and {log}")
            return True
        print("\n" + "\n".join(errors), file=sys.stderr)
    return False


def context(sections: list[Section], i: int) -> list[str]:
    """The reading of the previous section of the same book, if any."""
    sec = sections[i]
    if not i or sections[i - 1].book != sec.book or not sections[i - 1].path.exists():
        return []
    prev = sections[i - 1].path
    return [f"{PREVIOUS}\n\n<previous>\n{prev.read_text().strip()}\n</previous>"]


def main():
    global USAGE_PATH
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-b", "--books",
        help='Books to process, e.g. "1", "1-3" or "2,5"',
    )
    group.add_argument(
        "--verse",
        help="Revise only the section of this verse, even if revised before",
    )
    parser.add_argument(
        "-m", "--model",
        required=True,
        help="Model name with optional vendor prefix (e.g. openai:gpt-5.6-terra)",
    )
    parser.add_argument(
        "-r", "--rounds",
        type=int,
        default=3,
        help="Max attempts per section until every verse is quoted (default: 3)",
    )
    parser.add_argument(
        "--no-think",
        action="store_true",
        help="Disable thinking output (include_thoughts=False)",
    )
    parser.add_argument(
        "--save-usage",
        action="store_true",
        help="Record usage regardless of model name",
    )
    args = parser.parse_args()

    sections = read_sections(COMMENTARY)
    if args.verse:
        if not args.verse.isdigit():
            parser.error(f"--verse must be a number: {args.verse}")
        verse = int(args.verse)
        indices = [i for i, sec in enumerate(sections) if verse in dict(sec.verses)]
        if not indices:
            parser.error(f"verse {verse} not found")
    else:
        selected = set(select_books(args.books, sorted({sec.book for sec in sections})))
        indices = [
            i for i, sec in enumerate(sections)
            if sec.book in selected and not log_path(sec).exists()
        ]
    indices = [i for i in indices if sections[i].rel != EXAMPLE and sections[i].path.exists()]
    if not indices:
        print("Nothing to review")
        return

    if args.model.startswith(("openai:", "gpt-")) or args.save_usage:
        USAGE_PATH = find_usage_file()

    client = Client(
        model=args.model,
        include_thoughts=not args.no_think,
        show_params=False,
        keep_history=False,
        show_usage=True,
    )

    ex = example(sections)
    ok = True
    try:
        for i in indices:
            if not (ok := review(client, sections[i], [ex, *context(sections, i)], args.rounds)):
                print(f"\ngiving up at {sections[i].heading}", file=sys.stderr)
                break
    finally:
        # Record silently so an interrupted run still logs what it consumed;
        # the report below is printed only on normal completion
        if client.usages and USAGE_PATH is not None:
            append_usage(sum(client.usages), args.model, USAGE_PATH)

    if client.usages:
        print(f"\n--- Total Usage ---\n{sum(client.usages)}")
        if USAGE_PATH is not None:
            print()
            print_today_totals(USAGE_PATH, models=[args.model])

    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
