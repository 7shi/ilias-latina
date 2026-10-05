"""Read the Latin of the Ilias Latina in Japanese or English, section by section.

Usage: python generate.py [--lang ja|en] -m MODEL [-R REVIEW_MODEL] (-b BOOKS | --verse VERSE)
       python generate.py [--lang ja|en] (--prompt | --check) (-b BOOKS | --verse VERSE)

The sections are those of the translation with commentary in the
language of the reading (ja by default), ../commentary/LANG/NN/VVVV.md:
each gives the verses of The Latin Library with their translation, then
the commentary.  Each section is sent to the model as its own message,
preceded by the example and the context and followed by PROMPT, and the
answer (the verses in groups, each followed by its reading) is the
draft.  With a review model, the draft is saved as TMP/NN/VVVV.md and
sent to that model with the same messages and REVIEW_PROMPT, which
repeats the rules, and its revision is the reading; without one, the
draft is the reading unless it leaves Latin words unread, and only then
is it reviewed in the same way by the model that made it.  The places of
the draft that a mechanical check finds (Latin words not read, runs of
Latin words, paragraphs opening with the commentary) are listed for the
review, and the revision must read every word.  The reading is saved
under the heading of the section as LANG/NN/VVVV.md, the same path as in
the commentary.  TMP is tmp/ for Japanese and tmp/en/ for English, so
that the drafts, prompts and logs of the two do not mix.  A draft that is
there already is reviewed without being made again.

The example is the commentary of the first section with the account in
the language of the reading of the aim of the reading and of how the
reading of that section (LANG/01/0001.md, written by hand) was built,
quoting all of it (LANG/ONESHOT.md).  The context is the reading of the
previous section of the same book in <previous>; the first section of
a book has none.  Existing files are skipped, so an interrupted run
resumes where it left off.  For testing, --verse generates only the
section of a verse, with what context there is; --verse next generates
only the first section missing from the start.

For a harness that drafts in its own session (a coding agent), --prompt
writes the messages of one section, the next missing one of the books or
the one of --verse, with an instruction to write the reading into its
file, to TMP/prompt.md, and --check checks the readings of the books or
of the verse as a draft is checked, listing also the places that the
review is given.  Neither needs a model; with -m, --check logs the errors
of each failing section in TMP/errors.tsv under that model, as the
rounds of a draft are logged, unless --no-log is given.
"""

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from llm7shi import Client
from llm7shi.usage import append_usage, find_usage_file, print_today_totals

ROOT = Path(__file__).resolve().parent
EXAMPLE = Path("01") / "0001.md"

JA_INTRO = """
<commentary> is a section of book {book} of the Ilias Latina from a
Japanese translation with commentary: the verses of The Latin Library,
each followed by its Japanese translation in brackets, then an essay on
the passage.

Write in Japanese a reading of the Latin of this section, for a reader
who does not know Latin and reads it beside the translation and the
commentary.  <example> gives the commentary of the first section and
<construction>, an account in Japanese of the aim of the reading and of
how the reading of that section was built, step by step, quoting every
sentence of it.  Follow the aim, the steps and the checks there; the
rules below add what the first section does not show.
""".strip()

JA_FORM = """
Form:

- Do not add a heading at the top.
- Divide the section into groups as <construction> does.  Give each group
  a heading `#### N行目` or `#### N–M行目`, then quote its verses in a
  quotation block, `> N Latin`, the verses separated by a line with `>`
  alone, copying the number and the Latin exactly as given and without the
  translation; then write the reading of the group in plain paragraphs,
  not in quotation blocks, with the Latin words in italics.
- Quote every verse of the section once, in order, and bring in every
  Latin word of the verses, small words included.
""".strip()

JA_RULES = """
Beyond the first section:

- Bring in the Latin one word at a time even where the verse runs on in a
  long clause (not *dumque tuo premitur pondere dulci*, nor
  *haec illi mandata refer*).
- Take from the commentary only what the Latin does not say: whom a
  patronymic or a periphrasis means, each in one short sentence
  (「解説が述べるとおり、…」), and no more than the commentary says.  Do
  not use 「解説が述べるとおり」 for what the verses say themselves, and do
  not retell the commentary (lineage, legend, comparison with Homer, the
  poet's design) in sentences or a paragraph of its own.
- An identification already made in <previous> or listed in <identified>
  is not made again; it counts as made only where it is stated
  (「解説が述べるとおり、これはアガメムノンである」), not where the name
  only appears.  A name the reader already has (ユピテル, ヘレネ) needs no
  identification.
- Latin words met in <previous> may be used again as known words, as the
  example uses the words of its earlier verses.
- Do not close a group or a paragraph with a sentence that goes over the
  Latin words just read again (「こうして *corpora* が野に広がり、*sanguine*
  は *prata* を潤す」「*suorum* の *uires* が *numine* によって削がれているの
  である」) or that only says the story goes on (「話はまだ先へ続いていく」).
  A sentence that says what a line has brought together, as the example
  does once, is not such a sentence.
""".strip()

JA_REVIEW_INTRO = """
<commentary> is a section of book {book} of the Ilias Latina from a
Japanese translation with commentary.  <reading> is a Japanese reading of
the Latin of this section, made by a model, for a reader who does not
know Latin and reads it beside the translation and the commentary.
<example> gives the commentary of the first section and <construction>,
an account in Japanese of the aim of the reading and of how the reading
of that section, written by hand as the standard, was built; its aim,
steps and checks, with the rules below, are the rules of the reading.

Revise <reading> where it breaks the rules.  Keep every sentence that
already follows them as it is; change only those that do not, and do not
add or remove content beyond what the rules require, and keep the groups
of verses and their headings as they are.  Where a group is wrong
throughout (the Latin quoted in runs, the commentary retold), write its
reading again.  Look in particular for:

- a Latin word of the verses not read, small words such as *et* included;
- a clause or a run of Latin words quoted at once instead of one word at
  a time, or the meaning of a run told first and the run quoted after;
- a paragraph or sentences that retell the commentary beyond whom or what
  a word means;
- what the checks and the rejected forms of <construction> name, above
  all a quoted gloss (with adverbs and connectives too), the Latin spoken
  of as words, and a Latin word met for the first time made the topic or
  subject;
- 「解説が述べるとおり」 used for what the verses say themselves, or for
  more than the commentary says;
- an identification already made in <previous> or <identified>, made
  again (one that they do not state in words is not made yet and is kept);
- a word held back (「まだ明かされない」「先に示される」) where the word it
  waits for comes only one or two words later, and sentence endings that
  repeat (「〜と示される」「〜と明かされる」 sentence after sentence); do not
  add holding back that the draft does not have;
- a Latin word slotted into a Japanese sentence in place of a Japanese
  word (「それから、*deinde*、槍を投げる」);
- a closing sentence that goes over the Latin words just read again or
  only says the story goes on;
- a sentence that is broken, unclear or says one thing twice;
- a misreading of the Latin.

Answer with the whole revised reading in the same form, without the
heading of the section, and nothing else.
""".strip()

EN_INTRO = """
<commentary> is a section of book {book} of the Ilias Latina from an
English translation with commentary: the verses of The Latin Library,
each followed by its English translation in parentheses, then an essay
on the passage.

Write in English a reading of the Latin of this section, for a reader
who does not know Latin and reads it beside the translation and the
commentary.  <example> gives the commentary of the first section and
<construction>, an account of the aim of the reading and of how the
reading of that section was built, step by step, quoting every sentence
of it.  Follow the aim, the steps and the checks there; the rules below
add what the first section does not show.
""".strip()

EN_FORM = """
Form:

- Do not add a heading at the top.
- Divide the section into groups as <construction> does.  Give each group
  a heading `#### Line N` or `#### Lines N–M`, then quote its verses in a
  quotation block, `> N Latin`, the verses separated by a line with `>`
  alone, copying the number and the Latin exactly as given and without the
  translation; then write the reading of the group in plain paragraphs,
  not in quotation blocks, with the Latin words in italics.
- Quote every verse of the section once, in order, and bring in every
  Latin word of the verses, small words included.
""".strip()

EN_RULES = """
Beyond the first section:

- Bring in the Latin one word at a time even where the verse runs on in a
  long clause (not *dumque tuo premitur pondere dulci*, nor
  *haec illi mandata refer*).
- Take from the commentary only what the Latin does not say: whom a
  patronymic or a periphrasis means, each in one short sentence ("As the
  commentary says, …"), and no more than the commentary says.  Do not use
  "As the commentary says" for what the verses say themselves (not "As
  the commentary says, he is a god who favors Troy" for *Troianus
  Apollo*), and do not retell the commentary (lineage, legend, comparison
  with Homer, the poet's design) in sentences or a paragraph of its own.
- An identification names the person or people in English, as the
  commentary names them, and does not make the Latin word its subject:
  "As the commentary says, the Pelasgians are the Greeks", not "As the
  commentary says, this *Pelasgi* means the Greeks".
- An identification already made in <previous> or listed in <identified>
  is not made again; it counts as made only where it is stated ("As the
  commentary says, this son of Atreus is Agamemnon"), not where the name
  only appears.  A name the reader already has (Jupiter, Helen) needs no
  identification.
- Latin words met in <previous> may be used again as known words, as the
  example uses the words of its earlier verses.
- Use no terms of grammar ("preposition", "negative", "conjunction",
  "genitive", "case", "clause", "main clause", "pronoun", "participle",
  "enclitic" and the like); bring a word in by what it does in the story.
  Not "the negative *nec* denies it" but "The god's shape does not hold,
  and that it does not is told with *nec*"; not "his genitive is shown by
  *cuius*" but "Ajax, whose strength it is, is referred to again as
  *cuius*".
- Do not talk of punctuation: not "After the semicolon the slaughter
  spreads" but "Then the slaughter spreads".
- Do not talk of the Latin as words: not "The word for keel gives
  *carinas*" but "The ships are shown by their keels, named *carinas*".
  Do not bring out an enclitic as a word beside its word ("together with
  *-que*, *uastumque*"); give the word whole ("described as
  *uastumque*"), or weave *-que* alone into a sentence about the
  connection, as the example does with *Latrantum*.
- Check in the commentary's translation which noun an adjective goes
  with, and whom a pronoun or a possessive refers to: *ultrix* goes with
  *dextera*, the avenging hand of Troy, not with a person; *ille* is
  Achilles in pursuit, not the river; *patriae* are the prayers of the
  father who holds his son back, not of the one held back.
- A word whose noun comes in the next line is held back there and joined
  there (*suis* … *equis*: their own horses).  A word at the end of a
  section whose noun opens the next section is held back in the same way
  and not read as if complete (*totis* waiting for *aquis*).
- Add no color the Latin does not give (not "grievous wounds" for
  *uulnera*); a possessive such as *sua* is said briefly ("their own").
- A lost line (`\\<>`) or a place the commentary calls damaged is said to
  be lost or damaged, as the commentary says, not described by its
  editorial signs.  A word marked with the editor's doubt (`*` after it)
  is noted briefly as the example does with *protulerant*, and read as it
  stands.  Variant readings of other editors are not mentioned, even when
  the commentary cites them.
- A sentence ending "… is *X*" comes at most once a paragraph, and no
  ending is repeated sentence after sentence.
- Do not close a group or a paragraph with a sentence that goes over the
  Latin words just read again ("So the *corpora* spread over the field and
  the *sanguine* soaks the *prata*") or that only says the story goes on
  ("The story goes on from here").  A sentence that says what a line has
  brought together, as the example does once, is not such a sentence.  "So
  *X* and *Y* come together" is said only of a word held back as
  <construction> allows, once a section, never of a pair side by side ("So
  *more* and *ferarum* come together").  Do not say that the book ends
  except in the last section of a book.
- Reread for broken sentences, such as a sentence that lacks its subject
  or object or ends on a bare word ("is placed with *per*."), and for
  typos.
""".strip()

EN_REVIEW_INTRO = """
<commentary> is a section of book {book} of the Ilias Latina from an
English translation with commentary.  <reading> is an English reading of
the Latin of this section, made by a model, for a reader who does not
know Latin and reads it beside the translation and the commentary.
<example> gives the commentary of the first section and <construction>,
an account of the aim of the reading and of how the reading of that
section, written by hand as the standard, was built; its aim, steps and
checks, with the rules below, are the rules of the reading.

Revise <reading> where it breaks the rules.  Keep every sentence that
already follows them as it is; change only those that do not, and do not
add or remove content beyond what the rules require, and keep the groups
of verses and their headings as they are.  Where a group is wrong
throughout (the Latin quoted in runs, the commentary retold), write its
reading again.  Look in particular for:

- a Latin word of the verses not read, small words such as *et* included;
- a clause or a run of Latin words quoted at once instead of one word at
  a time, or the meaning of a run told first and the run quoted after;
- a paragraph or sentences that retell the commentary beyond whom or what
  a word means;
- what the checks and the forms to avoid of <construction> name, above
  all a quoted gloss or a gloss set beside the word (with adverbs and
  connectives too), the Latin spoken of as words, terms of grammar, and a
  Latin word met for the first time made the topic or subject;
- "As the commentary says" used for what the verses say themselves, or
  for more than the commentary says, or with the Latin word as its
  subject;
- an identification already made in <previous> or <identified>, made
  again (one that they do not state in words is not made yet and is kept);
- a word held back ("is not yet said") where the word it waits for comes
  next, a word read as complete though its noun comes in the next line or
  section, and sentence endings that repeat ("is called *X*", "is named
  *X*" sentence after sentence, or "… is *X*" more than once a
  paragraph); do not add holding back that the draft does not have;
- an adjective joined to the wrong noun, or a pronoun or possessive
  referred to the wrong person, against the commentary's translation;
- a Latin word slotted into an English sentence in place of an English
  word ("then, *deinde*, he throws the spear");
- a closing sentence that goes over the Latin words just read again or
  only says the story goes on;
- a sentence that is broken, unclear or says one thing twice;
- a misreading of the Latin.

Answer with the whole revised reading in the same form, without the
heading of the section, and nothing else.
""".strip()

EXAMPLE_TEXT = "The first section, its commentary and how its reading was built, as an example:"

PREVIOUS = "The reading of the previous section, for continuity:"

IDENTIFIED = "The identifications made in the sections of this book before it:"

FLAGS = """
A mechanical check of <reading> found these places.  A word not read must
be brought in where the Latin gives it.  The others may break the rules:
a phrase of a preposition and its noun or an adjective next to its noun
may stand together, and a one-sentence identification is kept.
""".strip()

HARNESS = """
Write the answer to the messages above into reading/{path}: its first
line is the heading of the section, `{heading}`, then a blank line, then
the answer.  Then run `{check} VERSE={verse}` in reading/ and, while it
reports errors, correct the file and run it again.  Make the reading of
this section only.
""".strip()

# Set the path only when usage should be recorded
RETRY = """
A mechanical check rejected the previous answer for these reasons.  Answer
again from the start; quote each verse word for word, in its order, as the
commentary gives it, even where the order of the Latin seems strange.
""".strip()

USAGE_PATH = None

QUOTE_RE = re.compile(r"^>\s*(\d+)\s+(.*?)\s*$")
TRANS_RE = re.compile(r"^>\s*[（(]")
ITALIC_RE = re.compile(r"\*([^*\n]+)\*")
WORD_RE = re.compile(r"[A-Za-z]+")
ENCLITICS = ("que", "ne", "ue")


@dataclass(frozen=True)
class Language:
    """What depends on the language of the reading."""
    intro: str
    form: str
    rules: str
    review_intro: str
    ident_re: re.Pattern  # an identification taken from the commentary
    opening: str  # the start of a paragraph that opens with the commentary
    tmp: str  # the directory of drafts, prompt and logs, under ROOT
    check: str  # the command that checks a reading


LANGUAGES = {
    "ja": Language(
        JA_INTRO, JA_FORM, JA_RULES, JA_REVIEW_INTRO,
        re.compile(r"解説が述べるとおり[^。\n]*。"), "解説", "tmp", "make check",
    ),
    "en": Language(
        EN_INTRO, EN_FORM, EN_RULES, EN_REVIEW_INTRO,
        re.compile(r"As the commentary says[^.\n]*\."), "The commentary", "tmp/en", "make check READING=en",
    ),
}


def set_language(code: str):
    """Point the paths, prompts and checks to the language of the reading."""
    global LANG, COMMENTARY, OUT, DRAFT, PROMPT_FILE, MODELS, ERRORS, CONSTRUCTION, PROMPT, REVIEW_PROMPT
    LANG = LANGUAGES[code]
    COMMENTARY = ROOT.parent / "commentary" / code
    OUT = ROOT / code
    DRAFT = ROOT / LANG.tmp
    PROMPT_FILE = DRAFT / "prompt.md"
    MODELS = DRAFT / "models.tsv"
    ERRORS = DRAFT / "errors.tsv"
    CONSTRUCTION = OUT / "ONESHOT.md"
    PROMPT = f"{LANG.intro}\n\n{LANG.form}\n\n{LANG.rules}"
    REVIEW_PROMPT = f"{LANG.review_intro}\n\n{LANG.form}\n\n{LANG.rules}"


set_language("ja")


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


def check(answer: str, verses: list[tuple[int, str]], words: bool = False) -> tuple[str, list[str]]:
    """Check that every verse is quoted once, in order, without its
    translation, and, with words, that every word is read; write the
    quoted Latin as the commentary has it."""
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
            errors.append(f"{no}: quoted text does not match: {m[2]} (the commentary: {latin[no]})")
        elif i + 1 < len(lines) and TRANS_RE.match(lines[i + 1]):
            errors.append(f"{no}: translation quoted")
        lines[i] = f"> {no} {latin[no]}"
    if quoted != [no for no, _ in verses]:
        errors.append(f"verses quoted: {quoted}")
    if not lines or not lines[0].startswith("#### "):
        errors.append("no group heading at the start")
    if words and (missing := missing_words(answer, verses)):
        errors.append(f"Latin words not read: {' '.join(missing)}")
    return "\n".join(lines), errors


def missing_words(answer: str, verses: list[tuple[int, str]]) -> list[str]:
    """The words of the verses that the reading does not give in italics;
    a word with an enclitic counts as given with or without it."""
    given = {w.lower() for run in ITALIC_RE.findall(answer) for w in WORD_RE.findall(run)}

    def read(word: str) -> bool:
        w = word.lower()
        return w in given or any(w.endswith(e) and w[:-len(e)] in given for e in ENCLITICS)

    return [w for _, latin in verses for w in WORD_RE.findall(unescape(latin)) if not read(w)]


def flags(answer: str, verses: list[tuple[int, str]]) -> list[str]:
    """Places that may break the rules, for the review: Latin words not
    read, runs of three or more Latin words, and paragraphs that open
    with the commentary."""
    missing = [f"- a Latin word not read: *{w}*" for w in missing_words(answer, verses)]
    runs = [run for run in ITALIC_RE.findall(answer) if len(run.split()) >= 3]
    paras = [line for line in answer.splitlines() if line.startswith(LANG.opening)]
    return missing + [f"- a run of Latin words: *{run}*" for run in runs] + [
        f"- a paragraph opening with the commentary: {line[:40]}…" for line in paras
    ]


def example(sections: list[Section]) -> str:
    sec = next(s for s in sections if s.rel == EXAMPLE)
    return (
        f"{EXAMPLE_TEXT}\n\n<example>\n<commentary>\n{sec.text}\n</commentary>\n\n"
        f"<construction>\n{CONSTRUCTION.read_text().strip()}\n</construction>\n</example>"
    )


def context(sections: list[Section], i: int) -> str | None:
    """The reading of the previous section of the same book with the
    identifications of the sections before it, "" for the first section
    of a book; None if it is not there yet."""
    sec = sections[i]
    if not i or sections[i - 1].book != sec.book:
        return ""
    prev = sections[i - 1].path
    if not prev.exists():
        return None
    ctx = f"{PREVIOUS}\n\n<previous>\n{prev.read_text().strip()}\n</previous>"
    earlier = [s.path for s in sections[:i - 1] if s.book == sec.book and s.path.exists()]
    if found := [m for path in earlier for m in LANG.ident_re.findall(path.read_text())]:
        ctx += f"\n\n{IDENTIFIED}\n\n<identified>\n" + "\n".join(dict.fromkeys(found)) + "\n</identified>"
    return ctx


def ask(client: Client, model: str, sec: Section, messages: list[str], rounds: int, step: str, words: bool = False) -> str | None:
    """The checked answer of the model; None if every round fails.  The
    errors of a failed round are logged in TMP/errors.tsv and given with
    the next round."""
    retry: list[str] = []
    for round_no in range(1, rounds + 1):
        print(f"\n--- {sec.heading} ({step}, round {round_no}) ---")
        answer, errors = check(client([*messages, *retry]).text, sec.verses, words)
        if not errors:
            return answer
        print("\n" + "\n".join(errors), file=sys.stderr)
        ERRORS.parent.mkdir(parents=True, exist_ok=True)
        with ERRORS.open("a") as f:
            f.writelines(f"{sec.rel}\t{step}\t{round_no}\t{model}\t{e}\n" for e in errors)
        retry = [f"{RETRY}\n\n" + "\n".join(f"- {e}" for e in errors)]
    return None


def save(path: Path, sec: Section, answer: str, step: str, model: str):
    """Save the answer and log the model that wrote it in TMP/models.tsv."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"{sec.heading}\n\n{answer}\n")
    MODELS.parent.mkdir(parents=True, exist_ok=True)
    with MODELS.open("a") as f:
        f.write(f"{sec.rel}\t{step}\t{model}\n")
    print(f"\nSaved to {path}")


def generate(clients: list[Client], models: list[str], sec: Section, messages: list[str], rounds: int) -> bool:
    """Make the draft with the first client and have the last one review
    it; with a single client, only a draft that leaves Latin words unread
    is reviewed."""
    commentary = f"<commentary>\n{sec.text}\n</commentary>"
    draft_path = DRAFT / sec.rel
    if draft_path.exists():
        print(f"\nDraft found: {draft_path}")
        draft = draft_path.read_text().strip().split("\n", 1)[1].strip()
    else:
        prompt = PROMPT.format(book=sec.book)
        if (draft := ask(clients[0], models[0], sec, [*messages, commentary, prompt], rounds, "draft")) is None:
            return False
        if len(clients) == 1 and not missing_words(draft, sec.verses):
            save(sec.path, sec, draft, "draft", models[0])
            return True
        save(draft_path, sec, draft, "draft", models[0])
    reading = f"<reading>\n{draft}\n</reading>"
    if found := flags(draft, sec.verses):
        reading += f"\n\n{FLAGS}\n\n" + "\n".join(found)
    prompt = REVIEW_PROMPT.format(book=sec.book)
    if (answer := ask(clients[-1], models[-1], sec, [*messages, commentary, reading, prompt], rounds, "review", True)) is None:
        return False
    save(sec.path, sec, answer, "review", models[-1])
    return True


def write_prompt(sections: list[Section], sec: Section) -> bool:
    """Write the messages of a section for a harness to TMP/prompt.md."""
    if (ctx := context(sections, sections.index(sec))) is None:
        print(f"missing {sections[sections.index(sec) - 1].path}: make it first", file=sys.stderr)
        return False
    harness = HARNESS.format(path=sec.path.relative_to(ROOT), heading=sec.heading, verse=sec.verses[0][0], check=LANG.check)
    messages = [example(sections), ctx, f"<commentary>\n{sec.text}\n</commentary>", PROMPT.format(book=sec.book), harness]
    PROMPT_FILE.parent.mkdir(parents=True, exist_ok=True)
    PROMPT_FILE.write_text("\n\n".join(m for m in messages if m) + "\n")
    print(f"{sec.heading}\nPrompt: {PROMPT_FILE}\nReading: {sec.path}")
    return True


def check_round(rel: Path) -> int:
    """The number of the next failed check of a section in TMP/errors.tsv."""
    if not ERRORS.exists():
        return 1
    rounds = [int(f[2]) for line in ERRORS.read_text().splitlines()
              if len(f := line.split("\t")) >= 3 and f[0] == str(rel) and f[1] == "check"]
    return max(rounds, default=0) + 1


def check_readings(targets: list[Section], model: str | None) -> bool:
    """Check existing readings as drafts are checked; False if any fails.
    The places that may break the rules are listed but do not fail.  With
    a model ("" for none), the errors are logged in TMP/errors.tsv."""
    ok = True
    for sec in targets:
        if not sec.path.exists():
            print(f"{sec.rel}: missing")
            continue
        heading, _, body = sec.path.read_text().strip().partition("\n")
        _, errors = check(body.strip(), sec.verses, True)
        if heading != sec.heading:
            errors.insert(0, f"the first line is not the heading {sec.heading}")
        notes = [f for f in flags(body, sec.verses) if not f.startswith("- a Latin word not read")]
        print(f"{sec.rel}: {'error' if errors else 'ok'}")
        print("".join(f"  {e}\n" for e in errors) + "".join(f"  {n}\n" for n in notes), end="")
        if errors and model is not None:
            round_no = check_round(sec.rel)
            ERRORS.parent.mkdir(parents=True, exist_ok=True)
            with ERRORS.open("a") as f:
                f.writelines(f"{sec.rel}\tcheck\t{round_no}\t{model}\t{e}\n" for e in errors)
        ok = ok and not errors
    return ok


def next_missing(sections: list[Section]) -> Section | None:
    """The first section missing from the start; None if all are there."""
    return next((sec for sec in sections if not sec.path.exists()), None)


def run(clients: list[Client], models: list[str], ex: str, sections: list[Section], indices: list[int], rounds: int) -> bool:
    """Generate the missing sections among those given."""
    for i in indices:
        sec = sections[i]
        if sec.path.exists():
            print(f"Skipped (already exists): {sec.path}")
            continue
        if (ctx := context(sections, i)) is None:
            print(f"\nmissing {sections[i - 1].path}: generate it first", file=sys.stderr)
            return False
        if not generate(clients, models, sec, [ex, ctx] if ctx else [ex], rounds):
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
        "--lang",
        choices=sorted(LANGUAGES),
        default="ja",
        help="Language of the reading (default: ja); English uses tmp/en/ for drafts, prompt and logs",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--prompt",
        action="store_true",
        help="Write the messages of the next missing section to tmp/prompt.md (tmp/en/prompt.md for English) for a harness",
    )
    mode.add_argument(
        "--check",
        action="store_true",
        help="Check the existing readings instead of generating",
    )
    parser.add_argument(
        "--no-log",
        action="store_true",
        help="With --check, do not log the errors in tmp/errors.tsv (tmp/en/errors.tsv for English)",
    )
    parser.add_argument(
        "-m", "--model",
        help="Model of the draft, with optional vendor prefix (e.g. openai:gpt-5.6-terra)",
    )
    parser.add_argument(
        "-R", "--review-model",
        help="Model that reviews the draft; without it only a draft that leaves words unread is reviewed by MODEL",
    )
    parser.add_argument(
        "-r", "--rounds",
        type=int,
        default=3,
        help="Max attempts per step until every verse is quoted (default: 3)",
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
    set_language(args.lang)

    sections = read_sections(COMMENTARY)
    if not CONSTRUCTION.exists():
        parser.error(f"{CONSTRUCTION} not found: the example is needed")
    books = sorted({sec.book for sec in sections})
    if not (args.prompt or args.check or args.model):
        parser.error("-m/--model is required to generate")
    if args.check:
        if args.verse and not args.verse.isdigit():
            parser.error(f"--verse must be a number with --check: {args.verse}")
        if args.verse:
            targets = [sec for sec in sections if int(args.verse) in dict(sec.verses)]
        else:
            selected = set(select_books(args.books, books))
            targets = [sec for sec in sections if sec.book in selected]
        if not targets:
            parser.error("no section to check")
        sys.exit(0 if check_readings(targets, None if args.no_log else args.model or "") else 1)
    if args.prompt and args.books:
        selected = set(select_books(args.books, books))
        if (target := next((s for s in sections if s.book in selected and not s.path.exists()), None)) is None:
            print("Nothing to generate: all sections exist")
            return
        sys.exit(0 if write_prompt(sections, target) else 1)
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
    if args.prompt:
        sys.exit(0 if write_prompt(sections, target) else 1)

    models = [args.model] + ([args.review_model] if args.review_model else [])
    if any(m.startswith(("openai:", "gpt-")) for m in models) or args.save_usage:
        USAGE_PATH = find_usage_file()

    clients = [
        Client(
            model=model,
            include_thoughts=not args.no_think,
            show_params=False,
            keep_history=False,
            show_usage=True,
        )
        for model in models
    ]

    ex = example(sections)
    ok = True
    try:
        if target:
            if (ctx := context(sections, sections.index(target))) is None:
                print("No context: the previous section is not there yet")
                ctx = ""
            ok = generate(clients, models, target, [ex, ctx] if ctx else [ex], args.rounds)
        else:
            selected = set(select_books(args.books, books))
            indices = [i for i, sec in enumerate(sections) if sec.book in selected]
            ok = run(clients, models, ex, sections, indices, args.rounds)
    finally:
        # Record silently so an interrupted run still logs what it consumed;
        # the report below is printed only on normal completion
        if USAGE_PATH is not None:
            for client, model in zip(clients, models):
                if client.usages:
                    append_usage(sum(client.usages), model, USAGE_PATH)

    for client, model in zip(clients, models):
        if client.usages:
            print(f"\n--- Total Usage ({model}) ---\n{sum(client.usages)}")
    if USAGE_PATH is not None and any(client.usages for client in clients):
        print()
        print_today_totals(USAGE_PATH, models=models)

    # Reported after the usage, so that make can tell a run that gave up
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
