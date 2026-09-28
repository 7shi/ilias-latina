"""Translate the Ilias Latina into English and comment on it, section by section.

Usage: python generate.py -m MODEL (-b BOOKS | --verse VERSE)

The sections are those of ../src/tmp/greek.md (`make greek` in src/):
each gives the verses of The Latin Library with the lines of the Iliad
they render, the notes that apply to them and the Greek of those lines.
Each section is sent to the model as its own message, preceded by the
context and followed by PROMPT, and the answer (the verses quoted with
their translation, then the commentary) is saved under its heading as
NN/VVVV.md (NN the book, VVVV the first verse).

The context is the whole previous section in <previous>; the first
section of a book has instead the summary of the previous book in
<summary> (NN/README.md), made by SUMMARY_PROMPT from the translations
of the book once all its sections are there.  The first section of
book 1 has none.  Existing files are skipped, so an interrupted run
resumes where it left off.  For testing, --verse generates only the
section of a verse, with what context there is, and no summary;
--verse next generates only the first thing missing from the start,
a section or the summary of a book.
"""

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from llm7shi import Client
from llm7shi.usage import append_usage, find_usage_file, print_today_totals

ROOT = Path(__file__).resolve().parent
GREEK = ROOT.parent / "src" / "tmp" / "greek.md"

PROMPT = """
The attached text is a section of book {book} of the Ilias Latina.  <latin>
gives the verses of The Latin Library, each followed by the lines of the
Iliad it renders in brackets ("—" none); <commentary> gives notes on these
verses from the editions; <greek> gives the Greek of those lines of the
Iliad.

Translate the section into English and comment on it, in Markdown.  The
result is meant to be read as an abridged Iliad by a reader with no
previous knowledge of the poem or of Homer, following the course of the
story rather than the scholarly interpretation of the Latin text.

- First quote every verse of <latin>, in order, in a single quotation block:
  `> N Latin` followed by `> (English translation)`, the verses separated by
  a line with `>` alone.  Copy the number and the Latin exactly as given,
  without the bracketed lines of the Iliad.
- Translate each verse on its own line, faithfully and plainly, with the
  words of that verse only, even where a sentence runs over and the
  English becomes less natural; do not move words to another verse.
  Give the names of persons and peoples in their usual English forms
  from the Latin (Vlixes Ulysses, Aiax Ajax, Iuppiter Jupiter, Priamus
  Priam; Grai Greeks, Danai Danaans, Achiui Achaeans, Pelasgi
  Pelasgians, Phryges Phrygians), keep patronymics and names used as
  they are in English (Atrides, Pelides, Somnus, Pergama, Cytherea),
  and explain in the commentary whom they mean.
- Read every note in <commentary> before translating.  Where a note
  explains what a word or phrase means (e.g. "pestem i.e. amorem
  Chryseidos"), follow it in the translation and the commentary, even if
  another reading seems more natural.  A note that only gives a parallel
  from another author, or reports or disputes someone's opinion, does
  not decide the meaning; where the meaning remains uncertain, do not
  state one reading as fact.  Follow the cross-references of a note
  ("see v. 26") to connect the passages.
- Then write the commentary in prose for a general reader, in the style
  of an essay rather than a scholarly note: what the passage means, how
  it retells the Iliad (what is kept, condensed, changed or added), and
  the persons, places and background that help to understand it.
- Treat the quoted verses as one passage.  Do not go through them verse
  by verse or dwell on small details; mention a verse number only where
  the reader would otherwise not find what is meant.
- <commentary> and <greek> are given to make the translation and the
  commentary accurate; the reader sees only the verses and your
  commentary.  Do not report the notes: leave out their parallels and
  references, and do not mention the notes, the editions, their editors
  or other materials.  Leave out what concerns only the transmission of
  the text (other readings, manuscripts, quotations by later authors).
- Do not quote the Greek.  When citing the Iliad, translate the passage
  into English and give the book and line (e.g. *Iliad* 1.1).
- Do not add a heading.
""".strip()

PREVIOUS = "The previous section, with its translation and commentary, for continuity:"

PREVIOUS_BOOK = "A summary of the previous book (book {book}), for continuity:"

SUMMARY_PROMPT = """
The attached text is the English translation of book {book} of the Ilias
Latina, verse by verse.  Summarize it as context for translating the next
book: the course of the events, the persons with the names and epithets used
for them, and where the book ends.  Write plain prose without headings.
""".strip()

# Set the path only when usage should be recorded
USAGE_PATH = None

BOOK_RE = re.compile(r"^## Book (\d+)$")
VERSE_RE = re.compile(r"^(\d+) (.*) \[[^\]]*\]$")
QUOTE_RE = re.compile(r"^>\s*(\d+)\s+(.*?)\s*$")
TRANS_RE = re.compile(r"^>\s*\((.*)\)\s*$")


@dataclass
class Section:
    book: int
    heading: str
    text: str
    verses: list[tuple[int, str]]

    @property
    def path(self) -> Path:
        return ROOT / f"{self.book:02d}" / f"{self.verses[0][0]:04d}.md"


def read_sections(path: Path) -> list[Section]:
    """Split greek.md at the `###` headings, keeping the verses of <latin>."""
    sections: list[Section] = []
    book, lines = 0, []

    def close():
        if lines:
            verses = [(int(m[1]), m[2]) for line in lines if (m := VERSE_RE.match(line))]
            text = "\n".join(lines).strip()
            sections.append(Section(book, lines[0], text, verses))

    for line in path.read_text().splitlines():
        if m := BOOK_RE.match(line):
            close()
            book, lines = int(m[1]), []
        elif line.startswith("### "):
            close()
            lines = [line]
        elif lines:
            lines.append(line)
    close()
    return sections


def select_books(spec: str, books: list[int]) -> list[int]:
    """Parse "1", "1-3" or "2,5" into book numbers."""
    out = set()
    for part in spec.split(","):
        a, _, b = part.partition("-")
        out |= set(range(int(a), int(b or a) + 1))
    return [b for b in books if b in out]


def escape(latin: str) -> str:
    return latin.replace("<", "\\<")


def check(answer: str, verses: list[tuple[int, str]]) -> tuple[str, list[str]]:
    """Check that every verse is quoted once, in order, with its
    translation, and write the quoted Latin as the notation has it."""
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
        if m[2].replace("\\<", "<") != latin[no]:
            errors.append(f"{no}: quoted text does not match")
        elif i + 1 >= len(lines) or not TRANS_RE.match(lines[i + 1]):
            errors.append(f"{no}: no translation")
        lines[i] = f"> {no} {escape(latin[no])}"
    if quoted != [no for no, _ in verses]:
        errors.append(f"verses quoted: {quoted}")
    return "\n".join(lines), errors


def translations(sections: list[Section]) -> str:
    """The translation of each verse of the sections, as `N translation`."""
    out = []
    for sec in sections:
        lines = sec.path.read_text().splitlines()
        for line, next_line in zip(lines, lines[1:]):
            if (m := QUOTE_RE.match(line)) and (t := TRANS_RE.match(next_line)):
                out.append(f"{m[1]} {t[1]}")
    return "\n".join(out)


def generate(client: Client, sec: Section, context: str, rounds: int) -> bool:
    prompt = PROMPT.format(book=sec.book)
    for round_no in range(1, rounds + 1):
        print(f"\n--- {sec.heading} (round {round_no}) ---")
        messages = [context, sec.text, prompt] if context else [sec.text, prompt]
        answer, errors = check(client(messages).text, sec.verses)
        if not errors:
            sec.path.parent.mkdir(parents=True, exist_ok=True)
            sec.path.write_text(f"{sec.heading}\n\n{answer}\n")
            print(f"\nSaved to {sec.path}")
            return True
        print("\n" + "\n".join(errors), file=sys.stderr)
    return False


def summarize(client: Client, book: int, sections: list[Section]):
    path = ROOT / f"{book:02d}" / "README.md"
    print(f"\n--- summary of book {book} ---")
    response = client([translations(sections), SUMMARY_PROMPT.format(book=book)])
    path.write_text(response.text.strip() + "\n")
    print(f"\nSaved to {path}")


def context(sections: list[Section], i: int) -> str | None:
    """The previous section of the same book, or the summary of the
    previous book for the first section; None if it is not there yet."""
    sec = sections[i]
    if i and sections[i - 1].book == sec.book:
        prev = sections[i - 1].path
        return f"{PREVIOUS}\n\n<previous>\n{prev.read_text().strip()}\n</previous>" if prev.exists() else None
    if sec.book == 1:
        return ""
    summary = ROOT / f"{sec.book - 1:02d}" / "README.md"
    if summary.exists():
        return f"{PREVIOUS_BOOK.format(book=sec.book - 1)}\n\n<summary>\n{summary.read_text().strip()}\n</summary>"
    return None


def next_missing(sections: list[Section]) -> int | Section | None:
    """The first section missing from the start, or the book whose
    summary is missing once all its sections are there; None if all are."""
    for book in sorted({sec.book for sec in sections}):
        for sec in sections:
            if sec.book == book and not sec.path.exists():
                return sec
        if not (ROOT / f"{book:02d}" / "README.md").exists():
            return book
    return None


def run(client: Client, book: int, sections: list[Section], rounds: int) -> bool:
    """Generate the missing sections of a book and then its summary."""
    for i, sec in enumerate(sections):
        if sec.path.exists():
            print(f"Skipped (already exists): {sec.path}")
            continue
        if (ctx := context(sections, i)) is None:
            print(f"\nmissing the summary of book {book - 1}: generate it first", file=sys.stderr)
            return False
        if not generate(client, sec, ctx, rounds):
            print(f"\ngiving up at {sec.heading}", file=sys.stderr)
            return False
    if not (ROOT / f"{book:02d}" / "README.md").exists():
        summarize(client, book, sections)
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
             'or with "next" the first thing missing from the start',
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

    if not GREEK.exists():
        parser.error(f"{GREEK} not found: run `make greek` in src/")
    sections = read_sections(GREEK)
    books = sorted({sec.book for sec in sections})
    target = None
    if args.verse and args.verse.lower() == "next":
        if (target := next_missing(sections)) is None:
            print("Nothing to generate: all sections and summaries exist")
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

    ok = True
    try:
        if isinstance(target, int):
            summarize(client, target, [s for s in sections if s.book == target])
        elif target:
            if (ctx := context(sections, sections.index(target))) is None:
                print("No context: the previous section or summary is not there yet")
                ctx = ""
            ok = generate(client, target, ctx, args.rounds)
        else:
            for book in select_books(args.books, books):
                if not (ok := run(client, book, [s for s in sections if s.book == book], args.rounds)):
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

    # Reported after the usage, so that make can tell a run that gave up
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
