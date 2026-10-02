# Known-to-unknown method

A method of ordering information in a text so that the reader never
meets a new thing before the thing it hangs on.  It is meant for two
uses in this project, kept apart:

1. checking the existing commentary ([Checking the commentary](#1-checking-the-commentary));
2. reading the Latin text itself ([Reading the Latin](#2-reading-the-latin)).

Neither is applied yet.  This file fixes the method and the intended
uses; the procedures below are to be tried on a few sections and
adjusted before they are used on the whole poem.

## Source

The method is taken from the slides of Ayato Kanada (金田礼人,
University of Electro-Communications) for an academic lunch seminar at
the Robotics Society of Japan's 2026 conference (4 September 2026), on
writing papers in hardware research:

- Slides (Japanese): <https://speakerdeck.com/ayatokanada/hadowea-kenkyuu-de-kokusai-toppu-kaigi-o-mezasu-iros-2027-deno-ronbun-saitaku-o-mezashi-te>
- Related post: <https://x.com/AyatoKanada/status/2096017893330985012>

Most of the slides concern the conferences and the problems peculiar to
hardware research.  The part used here is the advice on writing with
generative AI: an AI is good at making sentences sound right but cannot
repair a text whose logic or order is broken, so the author builds the
skeleton first with the "known to unknown" rule and has the AI polish
it.  What follows is a reconstruction for this project, not a summary
of the slides.

## The method

**Rule.**  In each sentence the front carries what the reader already
knows and the back carries what is new.  The new thing at the back of
one sentence is the known thing at the front of the next:

> A (known) → B (new); B (known) → C (new); C (known) → D (new)

A text built so has a chain the reader can follow without looking back.

Three working rules go with it:

- **Two subjects at most.**  A sentence deals with no more than two
  principal things (persons, places, notions), and says how they are
  related.  A third is a sign that the sentence should be split.
- **Known to the reader, not to the writer.**  What matters is what
  this reader has in hand at this point.  A person named several pages
  or sections ago, or in another book, may have been forgotten, and is
  introduced again with a short description.
- **Skeleton first.**  The order of introduction is settled before the
  sentences are polished.  A model can improve wording; it cannot make
  up for a thing that is used before it is introduced.

**In this poem.**  The *Ilias Latina* is full of things a reader without
Homer does not know and which are named in a way that hides who or
what they are: patronymics (*Pelides*, *Atrides*), Roman names for Greek
figures (*Orcus* for Hades, *Iuppiter* for Zeus), peoples under several
names (*Grai*, *Danai*, *Achiui*).  Each is, to such a reader, a new
term; two or three of them in one sentence without anything to hang on
is the failure the method is meant to prevent.

The commentary of 1–8 shows the chain at work.  It begins from the
anger within an army, the ground the reader has from the first line;
the Greeks, sailing against Troy, bring in the army; their foremost
warrior Achilles, introduced as *Pelides*, "son of Peleus", is built on
the Greeks; his opponent, *Atrides*, "son of Atreus", on Achilles; and
only then is Atrides said to mean Agamemnon, the king who leads the
expedition.  Each new name is attached to a thing already given, and
the sentence says whom it means last.

## 1. Checking the commentary

The commentary is an essay on each section ([Policy](README.md#policy)),
so the check is on the order in which it brings things in, not on its
content.  For each sentence of a section, mark the known (front) and
the new (back) and look for:

- a sentence whose front is not given by what comes before it or by the
  verses the reader has just seen (the verses count as given for the
  names they show, but not as explained);
- a sentence with three or more principal things;
- a name, patronymic or periphrasis that is used and only explained
  later, or never explained;
- a person or place that comes back after a long gap, or in another
  book, with no short description to bring it to mind.

The result is a report, section by section, with the sentences marked
and the reason.  The report is made first; corrections are made
afterwards, in the section files, and are committed apart from the
report, as the corrections to the generated sections were
([README](README.md#commentary)).  The marking is made by a model and
is judgement, not proof: a flagged sentence may be right, and the
check is to be adjusted on a few sections before it is run on the
rest.

For new generation, the rule and the two-subject limit may be added to
the instructions of [generate.py](generate.py), but that changes how the
sections are made and is not part of this check.

## 2. Reading the Latin

A traditional commentary on the Latin takes the verse word by word and
explains each form and construction; it is a great labour and is
written for readers who already read Latin.  The method suggests
another form: take the sentence **in the order in which the Latin
gives it**, and at each step add one or two new elements to what is
already settled, saying what each new word does to the whole.

Verse 1, *Iram pande mihi Pelidae, Diua, superbi*, as a sketch:

| Step | Word | What the reader now holds |
|------|------|---------------------------|
| 1 | *Iram* | An accusative: "wrath", the object of something to come |
| 2 | *pande* | An imperative: "show"; the frame is "show the wrath" |
| 3 | *mihi* | Dative: shown "to me", the speaker |
| 4 | *Pelidae* | Genitive: whose wrath, "of Pelides" (the son of Peleus) |
| 5 | *Diua* | Vocative: who is asked, the goddess |
| 6 | *superbi* | Genitive agreeing with *Pelidae*: the proud Pelides |

The scattered order of verse poetry (hyperbaton, here *Pelidae* and
*superbi*) is resolved at the point where the second word comes in,
which is where the reader meets it, and not in a note outside the line.
The frame (verb and its object) is given first and the rest is hung on
it.

The form of such a reading, its unit (a verse or a group of verses) and
its place are not fixed: they are to be settled by trying it on a few
verses.  Its files are to be kept apart from the commentary and
organised under the same verse ranges, so that the commentary and the
reading of a passage can be shown side by side, as parallel views of
one text, for example as tabs.  The reading depends on the Latin text
only and is not made from the notes of the editions.
