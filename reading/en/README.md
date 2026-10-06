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
| 2 | Gemini 3.8 Flash (Antigravity CLI) | — | Claude Opus 5.5 |
| 3 | Gemini 3.8 Flash (Antigravity CLI) | — | Claude Opus 5.5 |
| 4 | Gemini 3.8 Flash (Antigravity CLI) | — | Claude Opus 5.5 |
| 5 | Gemini 3.8 Flash (Antigravity CLI) | — | Claude Opus 5.5 |
| 6 | Gemini 3.8 Flash (Antigravity CLI) | — | Claude Opus 5.5 |
| 7 | Gemini 3.8 Flash (Antigravity CLI) | — | Claude Opus 5.5 |
| 8 | Gemini 3.8 Flash (Antigravity CLI) | — | Claude Opus 5.5 |
| 9 | Gemini 3.8 Flash (Antigravity CLI) | — | Claude Opus 5.5 |
| 10 | Gemini 3.8 Flash (Antigravity CLI) | — | Claude Opus 5.5 |
| 11 | Gemini 3.8 Flash (Antigravity CLI) | — | Claude Opus 5.5 |

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

Book 2 (verses 111–251) was drafted in one batch; most of its sections
are the short entries of the catalogue of ships. The content of later
words was still told in advance (*quem* read as Thersites "confronted
by another" before *Vlixes*; the blow told at *sceptro*), and the
grammar came back into the sentences ("a comparison is drawn with
*quam*", "referred to again as *quos*"). Where a clause runs on into
the next section, as often in the catalogue, the words were misread:
*quos* in line 196, the two leaders whom Eumelus follows, was taken as
the men Tlepolemus commands. Other misreadings were *quo non deformior
alter*, read as no one surpassing Thersites; *correptum*, read as
seized; *uix telis caruere manus*, read as hands reaching for weapons;
and *alta*, Hector's long legs, read as greaves gleaming from on high.
An identification contradicted the commentary: "the glory of the
Myrmidons" was taken to make Schedius and Epistrophus Myrmidons, though
Homer makes them Phocians. Pandarus was identified before his name
came. Nearly every section was rewritten, in plainer sentences than the
draft.

Book 3 (verses 252–343) was drafted in one batch and again nearly every
section was rewritten. A new habit ran through it: Latin slotted into a
participial tag, "met as *X*" or "met *in armis*". The content of later
words was still told early, now at a subject or an adverb ("Paris also
moves himself away" at *seque*, before *recepit*), and color came from
the commentary's interpretation rather than the Latin ("sleek heifer",
"her sharp tone"). Asked about its readings, the model traced these to
the prompt: the rule against repeated endings led it to invent new
ones; it had taken the rule against telling later words early to apply
only to a word held back; it had read the commentary's interpretation
as material for the story; and "met as *X*", once in a reading, was
copied from the previous section in the prompt, so that a habit of the
draft spread through the batch. The rules were changed accordingly: a
few plain forms to bring in a word, the rule against telling later
words early applied to the whole clause, and the commentary kept to
identifications and to what each word does.

Book 4 (verses 344–388) was drafted in batches of five sections, each
corrected before the next, so that the previous section in the prompt
was always a corrected one. The readings followed the plain forms from
the first batch, with no misreading; the corrections were a few words
each: a subject or a verb told before its word came (*curat*, *petit*,
*ruit*), and participles brought in with "given as" or "called" rather
than "described as".

Book 5 (verses 389–537) was drafted in nine batches. Its long similes
and battle scenes needed more correction than book 4, though far less
than books 2 and 3. The forms were often mismatched to the words (a
verb "given as *sonat*", a participle "told with *deiectus*"), places
and times told the verb after them ("He heads into the midst, given as
*in medios*"), and in the last batches sentences made a verb its own
subject ("Being laid low is told with *sternuntur*"). A few words were
misread: *galeae* in *cerebrum galeae cum parte reuulsum*, read as a
brain belonging to the helmet; *comes* in *comes horrida turba canum*,
read as an attendant of its own rather than the pack attending the
shepherd; *Antilochique Mydon*, read with a verb of striking the Latin
does not give rather than with the weapons of the line before; and
*non aequis armis*, its denial taken into the adjective. The editorial
sign in *Crethona\<que>* was written unescaped and was restored as in
the commentary.

Book 6 (verses 538–563) was drafted in two batches. The instruction had
told the model to ask when unsure, yet it had asked nothing through
book 5. Asked why, it said that it had taken stopping to ask as a
fallback for a complete block rather than for doubt about the Latin,
that a passing check had seemed to confirm its guesses, and that the
instruction made finishing the batch the goal; it named the points it
had guessed, among them the misreadings of book 5. The instruction was
changed to list, before each section, the points of construction not
settled by the translation, and to say that asking is part of the work
and that a passing check does not show the Latin read correctly. The
model still asked nothing in the second batch. Its corrections were of
the usual kinds; the one misreading was in Diomedes' speech to Glaucus,
where what Glaucus is to do (*concurrere*, *Pone*, *coerce*) was told as
what Diomedes does.

Book 7 (verses 564–649) was drafted in five batches. The model was
asked to report with each batch the points it had guessed; its first
two lists were empty, and once told that guessing is what the list is
for, it named seventeen to fifty points a batch, mostly
which adjective goes with which noun and to whom a pronoun refers. Its
choices were right throughout, and no word was misconstrued in the
book. The corrections were of the usual kinds: the content of a later
word told at a subject, a pronoun or a connective (a gift at *et* and
*inque uicem*, a refusal at *neque*), a word given more than its own
sense (*bello* as renowned in war, *cum primum* as soon as possible),
and participles told as actions.

Book 8 (verses 650–685) was drafted in four batches. Since the same
kinds of correction had recurred batch after batch, the instruction
was given a table contrasting sentences of the drafts with their
corrections, with the reason for each, and rows were added to it from
each batch. The first batch brought a new habit, a sentence opening the
section that restated the previous one ("What he does with his mighty
hand begins here"); after the table, the corrections fell to a few
words a batch, mostly the form of bringing in a word ("called *muris*"
for a noun). No word was misconstrued, and the guessed points were
again all right.

Book 9 (verses 686–695), the shortest book, was drafted in two batches.
The corrections were again a few words: adjectives before their nouns
told without holding them back (*Thetideius* before *heros*, *intacta*
before *Briseis*), an identification placed before the word it
identifies, and the tense of held words. The guessed points were all
right.

Book 10 (verses 696–740), the night raid, was drafted in three
batches. Its long sentences led the model to hold three words in a
group, more than the rules allow, and in Dolon's plea the persons and
powers invoked (*uos*, *per numina*, *per mare*) were each told as the
appeal that comes only with *obtestor*. With a denial, the subject was
described by what the denial takes away: in *quos nec praecederet
Eurus*, Eurus was "the swift one" rather than the one who could not
outrun the horses. The guessed points were again all right.

Book 11 (verses 741–757) was drafted in two batches and needed only a
few words of correction: a second *ferrum* told as the ringing that
comes with *sonat*, a name said twice (*Priamides*), and the
identification of the brother at *frater*, where the commentary makes
it. No word was misconstrued.

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
