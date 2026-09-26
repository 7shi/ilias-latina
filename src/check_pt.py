"""Check with an LLM that each translated line matches its Latin verse.

Usage: python check_pt.py -m MODEL PARALLEL.txt OUTPUT.json

PARALLEL.txt is the output of parallel.py: each verse takes two lines, the
label with the Latin text, then the indented translation.  The verses are
grouped into chunks at the ends of Latin sentences: sentences are added
until the chunk exceeds CHUNK_LINES lines, then the chunk is sent to the
model, which returns the labels of the matching (ok) and mismatching (ng)
lines as structured output.

OUTPUT.json maps each label to "ok" or "ng" in the order of the text.  It
is rewritten after every chunk, and chunks already judged in full are
skipped, so an interrupted run resumes where it left off.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from llm7shi import Client
from llm7shi.usage import append_usage, find_usage_file, print_today_totals
from pydantic import BaseModel

CHUNK_LINES = 20

PROMPT = """
The attached text is a part of the Ilias Latina with a Portuguese translation.
Each verse takes two lines: the verse label with the Latin text, then the
Portuguese translation of that verse, indented.

Check whether the translation of each verse corresponds to its Latin line.

- ok: the main content of the Latin line is rendered in its translation line.
  Words moved to the adjacent line, as is usual with enjambment, are allowed.
- ng: the translation is shifted by one or more lines, is missing, or renders
  the content of another line.

Put every verse label of the text in exactly one of "ok" and "ng".
""".strip()

# Set the path only when usage should be recorded
USAGE_PATH = None

VERSE_RE = re.compile(r"^(\S+) (.*)$")
SENTENCE_END_RE = re.compile(r"[.?!][^\w]*$")


class Result(BaseModel):
    ok: list[str]
    ng: list[str]


def load(path: Path) -> list[tuple[str, str, str]]:
    """Read the parallel text as a list of (label, latin, translation)."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if len(lines) % 2:
        sys.exit(f"{path}: odd number of lines")
    verses = []
    for i in range(0, len(lines), 2):
        if not (m := VERSE_RE.match(lines[i])) or not lines[i + 1].startswith(" "):
            sys.exit(f"{path}:{i + 1}: not a verse pair")
        verses.append((m.group(1), m.group(2), lines[i + 1].strip()))
    return verses


def chunks(verses):
    """Group the verses into chunks cut at the ends of Latin sentences,
    once a chunk exceeds CHUNK_LINES lines."""
    chunk = []
    for verse in verses:
        chunk.append(verse)
        if len(chunk) > CHUNK_LINES and SENTENCE_END_RE.search(verse[1]):
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def chunk_text(chunk) -> str:
    return "\n".join(
        f"{label} {latin}\n{' ' * len(label)} {trans}" for label, latin, trans in chunk
    )


def check(client: Client, chunk, rounds: int) -> dict[str, str]:
    """Judge a chunk, retrying until every label is judged exactly once."""
    labels = [label for label, _, _ in chunk]
    judged: dict[str, str] = {}
    for round_no in range(1, rounds + 1):
        response = client([chunk_text(chunk), PROMPT], schema=Result)
        result: Result = response.data
        ok, ng = set(result.ok), set(result.ng)
        judged = {
            label: "ok" if label in ok else "ng"
            for label in labels
            if (label in ok) != (label in ng)
        }
        if len(judged) == len(labels) and ok | ng <= set(labels):
            break
        print(f"\nround {round_no}: incomplete answer, retrying", file=sys.stderr)
    return judged


def main():
    global USAGE_PATH
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("src", type=Path, help="Parallel text from parallel.py")
    parser.add_argument("dst", type=Path, help="Output JSON of the judgments")
    parser.add_argument(
        "-m", "--model",
        required=True,
        help="Model name with optional vendor prefix (e.g. openai:gpt-5.6-terra)",
    )
    parser.add_argument(
        "-r", "--rounds",
        type=int,
        default=3,
        help="Max attempts per chunk until every line is judged (default: 3)",
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

    if args.model.startswith(("openai:", "gpt-")) or args.save_usage:
        USAGE_PATH = find_usage_file()

    verses = load(args.src)
    saved = json.loads(args.dst.read_text()) if args.dst.exists() else {}

    client = Client(
        model=args.model,
        include_thoughts=not args.no_think,
        show_params=False,
        keep_history=False,
        show_usage=True,
    )

    try:
        for chunk in chunks(verses):
            first, last = chunk[0][0], chunk[-1][0]
            if all(label in saved for label, _, _ in chunk):
                print(f"Skipped (already judged): {first}-{last}")
                continue
            print(f"\n--- {first}-{last} ---")
            saved |= check(client, chunk, args.rounds)
            # Rewritten in the order of the text, so resumed runs keep it sorted
            ordered = {label: saved[label] for label, _, _ in verses if label in saved}
            args.dst.write_text(json.dumps(ordered, indent=1) + "\n")
    finally:
        # Record silently so an interrupted run still logs what it consumed;
        # the report below is printed only on normal completion
        if client.usages and USAGE_PATH is not None:
            append_usage(sum(client.usages), args.model, USAGE_PATH)

    if missing := [label for label, _, _ in verses if label not in saved]:
        print(f"\nnot judged: {' '.join(missing)}", file=sys.stderr)
    ng = [label for label, _, _ in verses if saved.get(label) == "ng"]
    print(f"\nng ({len(ng)}): {' '.join(ng)}")

    if client.usages:
        print(f"\n--- Total Usage ---\n{sum(client.usages)}")
        if USAGE_PATH is not None:
            print()
            print_today_totals(USAGE_PATH, models=[args.model])


if __name__ == "__main__":
    main()
