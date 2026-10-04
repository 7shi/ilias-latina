"""Read the Latin of the Ilias Latina in Japanese, section by section.

Usage: python generate.py -m MODEL (-b BOOKS | --verse VERSE)

The sections are those of the Japanese translation with commentary,
../commentary/ja/NN/VVVV.md: each gives the verses of The Latin Library
with their translation, then the commentary.  Each section is sent to
the model as its own message, preceded by the example and the context
and followed by PROMPT, and the answer (the verses in groups, each
followed by its reading) is saved under the heading of the section as
ja/NN/VVVV.md, the same path as in the commentary.

The example is the first section, its commentary and its reading
(ja/01/0001.md, written by hand).  The context is the reading of the
previous section of the same book in <previous>; the first section of
a book has none.  Existing files are skipped, so an interrupted run
resumes where it left off.  For testing, --verse generates only the
section of a verse, with what context there is; --verse next generates
only the first section missing from the start.
"""

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from llm7shi import Client
from llm7shi.usage import append_usage, find_usage_file, print_today_totals

ROOT = Path(__file__).resolve().parent
COMMENTARY = ROOT.parent / "commentary" / "ja"
OUT = ROOT / "ja"
EXAMPLE = Path("01") / "0001.md"

INTRO = """
<commentary> is a section of book {book} of the Ilias Latina from a
Japanese translation with commentary: the verses of The Latin Library,
each followed by its Japanese translation in brackets, then an essay on
the passage.

Write in Japanese a reading of the Latin of this section, for a reader
who does not know Latin and reads it beside the translation and the
commentary.  <example> gives the commentary and the reading of the first
section; follow its form and manner.
""".strip()

FORM = """
Form:

- Do not add a heading at the top.
- Divide the section into groups of one verse, or of two or more verses
  where words of one verse are completed only in the next (an object, the
  noun of an adjective, the persons a sentence names).  Give each group a
  heading `#### N行目` or `#### N–M行目`, then quote its verses in a
  quotation block, `> N Latin`, the verses separated by a line with `>`
  alone, copying the number and the Latin exactly as given and without the
  translation; then write the reading of the group in paragraphs.
- Quote every verse of the section once, in order.
""".strip()

MANNER = """
Manner:

- Go through the words in the order in which the Latin gives them; do
  not reorder them to explain.
- Tell what the passage says as you go: the sentences carry the course
  of the content, and each Latin word comes in as the word that says it.
  The reading is not a list of glosses.
- Known to unknown: the front of a sentence holds what the reader already
  has (what was said before, the content, a Latin word already met), and
  the new Latin word comes at the back.  A Latin word once met may open a
  later sentence; a word met for the first time is not made the topic or
  subject at the front (not 「行末の *iussit* は、…と告げる」 or 「*X* が
  告げる」, but 「…と命じたのが、行末の *iussit* である」).
- Do not set a word and its gloss side by side (not 「怒り」*Iram*), nor
  put a quoted gloss before it (not 「ついにと *Tandem* で」 or 「それから
  という *inde* とともに」), least of all with adverbs and connectives.  Fold
  the meaning into the sentence and vary the endings (「〜が *X* である」
  「*X* と呼ばれる」「*X* と名指される」「〜を描くのが *X* である」 and so
  on); do not give consecutive sentences the same ending, and spread the
  endings over the section.
- Connectives and small words (*et*, *-que*, *atque*, *nam*, *ut*,
  *simul* and the like) are woven into the sentence of the words they
  join; do not give them a sentence of their own.  A word with *-que*
  is given for its own meaning, with the joining folded in (not
  「『そして』というつながりを担うのが *implicuitque* である」).
- Say each thing once: do not give a meaning in one sentence and name the
  word for it with the same meaning in the next, nor within one sentence
  (not 「〜と名指され、その名が *X* である」).
- A 「その」 or 「彼」 that takes up a person must not be readable as
  pointing to another person just mentioned (not 「その父」 right after
  another man; say 「娘の父」).
- At most two principal things in a sentence.
- An adjective next to its noun is taken together with it (*animas
  fortes*, *discordia pectora*).  Where words that belong together stand
  apart, give the first where it comes, say what is still awaited, and
  join it to the other where that comes.
- Do not explain grammar or use grammatical terms (names of cases, moods,
  tenses and the like).
- Write the Latin words in italics, as in the example.
- What the Latin does not say (whom a patronymic or a periphrasis means)
  is taken from the commentary and said to be so (「解説が述べるとおり」);
  do not add matters that are neither in the verses nor in the commentary,
  and do not go beyond what the commentary says.  「解説が述べるとおり」 is
  only for what the Latin does not say, not for what the verses say
  themselves.  An identification already made in <previous> is not made
  again.
- An asterisk in the Latin marks a place doubted in the base text: say so
  briefly and read it as printed.
""".strip()

PROMPT = f"{INTRO}\n\n{FORM}\n\n{MANNER}"

EXAMPLE_TEXT = "The first section, its commentary and its reading, as an example:"

PREVIOUS = "The reading of the previous section, for continuity:"

# Set the path only when usage should be recorded
USAGE_PATH = None

QUOTE_RE = re.compile(r"^>\s*(\d+)\s+(.*?)\s*$")
TRANS_RE = re.compile(r"^>\s*[（(]")


@dataclass
class Section:
    book: int
    heading: str
    text: str
    verses: list[tuple[int, str]]
    rel: Path

    @property
    def path(self) -> Path:
        return OUT / self.rel


def read_sections(root: Path) -> list[Section]:
    """Read the section files of the commentary, keeping the quoted Latin."""
    sections: list[Section] = []
    for path in sorted(root.glob("[0-9][0-9]/[0-9][0-9][0-9][0-9].md")):
        text = path.read_text().strip()
        lines = text.splitlines()
        verses = [(int(m[1]), m[2]) for line in lines if (m := QUOTE_RE.match(line))]
        rel = path.relative_to(root)
        sections.append(Section(int(rel.parts[0]), lines[0], text, verses, rel))
    return sections


def select_books(spec: str, books: list[int]) -> list[int]:
    """Parse "1", "1-3" or "2,5" into book numbers."""
    out = set()
    for part in spec.split(","):
        a, _, b = part.partition("-")
        out |= set(range(int(a), int(b or a) + 1))
    return [b for b in books if b in out]


def unescape(latin: str) -> str:
    return latin.replace("\\<", "<")


def check(answer: str, verses: list[tuple[int, str]]) -> tuple[str, list[str]]:
    """Check that every verse is quoted once, in order, without its
    translation, and write the quoted Latin as the commentary has it."""
    lines = [line.rstrip() for line in answer.strip().splitlines()]
    quoted: list[int] = []
    errors: list[str] = []
    latin = dict(verses)
    for i, line in enumerate(lines):
        if not (m := QUOTE_RE.match(line)):
            continue
        no = int(m[1])
        if no not in latin:
            continue
        quoted.append(no)
        if unescape(m[2]) != unescape(latin[no]):
            errors.append(f"{no}: quoted text does not match")
        elif i + 1 < len(lines) and TRANS_RE.match(lines[i + 1]):
            errors.append(f"{no}: translation quoted")
        lines[i] = f"> {no} {latin[no]}"
    if quoted != [no for no, _ in verses]:
        errors.append(f"verses quoted: {quoted}")
    if not lines or not lines[0].startswith("#### "):
        errors.append("no group heading at the start")
    return "\n".join(lines), errors


def example(sections: list[Section]) -> str:
    sec = next(s for s in sections if s.rel == EXAMPLE)
    return (
        f"{EXAMPLE_TEXT}\n\n<example>\n<commentary>\n{sec.text}\n</commentary>\n\n"
        f"<reading>\n{sec.path.read_text().strip()}\n</reading>\n</example>"
    )


def context(sections: list[Section], i: int) -> str | None:
    """The reading of the previous section of the same book, "" for the
    first section of a book; None if it is not there yet."""
    sec = sections[i]
    if not i or sections[i - 1].book != sec.book:
        return ""
    prev = sections[i - 1].path
    return f"{PREVIOUS}\n\n<previous>\n{prev.read_text().strip()}\n</previous>" if prev.exists() else None


def generate(client: Client, sec: Section, messages: list[str], rounds: int) -> bool:
    prompt = PROMPT.format(book=sec.book)
    commentary = f"<commentary>\n{sec.text}\n</commentary>"
    for round_no in range(1, rounds + 1):
        print(f"\n--- {sec.heading} (round {round_no}) ---")
        answer, errors = check(client([*messages, commentary, prompt]).text, sec.verses)
        if not errors:
            sec.path.parent.mkdir(parents=True, exist_ok=True)
            sec.path.write_text(f"{sec.heading}\n\n{answer}\n")
            print(f"\nSaved to {sec.path}")
            return True
        print("\n" + "\n".join(errors), file=sys.stderr)
    return False


def next_missing(sections: list[Section]) -> Section | None:
    """The first section missing from the start; None if all are there."""
    return next((sec for sec in sections if not sec.path.exists()), None)


def run(client: Client, ex: str, sections: list[Section], indices: list[int], rounds: int) -> bool:
    """Generate the missing sections among those given."""
    for i in indices:
        sec = sections[i]
        if sec.path.exists():
            print(f"Skipped (already exists): {sec.path}")
            continue
        if (ctx := context(sections, i)) is None:
            print(f"\nmissing {sections[i - 1].path}: generate it first", file=sys.stderr)
            return False
        if not generate(client, sec, [ex, ctx] if ctx else [ex], rounds):
            print(f"\ngiving up at {sec.heading}", file=sys.stderr)
            return False
    return True


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
        help='Generate only the section of this verse, for testing, '
             'or with "next" the first section missing from the start',
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
    if not (OUT / EXAMPLE).exists():
        parser.error(f"{OUT / EXAMPLE} not found: the example is needed")
    books = sorted({sec.book for sec in sections})
    target = None
    if args.verse and args.verse.lower() == "next":
        if (target := next_missing(sections)) is None:
            print("Nothing to generate: all sections exist")
            return
    elif args.verse:
        if not args.verse.isdigit():
            parser.error(f'--verse must be a number or "next": {args.verse}')
        verse = int(args.verse)
        found = [sec for sec in sections if verse in dict(sec.verses)]
        if not found:
            parser.error(f"verse {verse} not found")
        target = found[0]
        if target.path.exists():
            parser.error(f"{target.path} already exists")

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
        if target:
            if (ctx := context(sections, sections.index(target))) is None:
                print("No context: the previous section is not there yet")
                ctx = ""
            ok = generate(client, target, [ex, ctx] if ctx else [ex], args.rounds)
        else:
            selected = set(select_books(args.books, books))
            indices = [i for i, sec in enumerate(sections) if sec.book in selected]
            ok = run(client, ex, sections, indices, args.rounds)
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

    # Reported after the usage, so that make can tell a run that gave up
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
