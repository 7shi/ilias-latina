# Plan for the commentary

Notes for the next session.  Read README.md, this file,
commentary/README.md, texts/README.md and src/README.md first.

## Current state and next work

The English translation with a commentary in commentary/en/ is
finished in all 24 books: generated, checked against the Latin, the
notes of the editions, the Greek and the indexes of proper names, and
compared with the Portuguese.  The English of the indexes
(commentary/index-en.tsv and the editions' INDEX-en.tsv and
index-en.md) agrees with it.

For the Japanese, commentary/commentary-ja.tsv and
commentary/index-ja.tsv have been made, row for row with their English
counterparts, from the editions' Japanese drafts:

- commentary-ja.tsv takes, for each note of commentary-en.tsv, the
  Japanese of the same item in texts/notes-ja.md (374 notes).  The 122
  notes that commentary-en.tsv had adapted (joined across pages,
  excerpted with "…", Wernsdorf's verse numbers given in LL numbers,
  remarks on readings added) were adapted in the same way from the
  full Japanese in the edition's ilias-ja.md, by hand; all have now
  been read against the English rows. Their non-name draft meaning
  differences remain report-only, as listed below.
- index-ja.tsv takes, for each row of index-en.tsv, the Japanese
  headword and description of the same row of the edition's
  INDEX-ja.tsv.  Its names began as the drafts'; the forms reviewed
  for all 24 books have now been unified throughout the index.

The Japanese translation with a commentary in commentary/ja/ is
finished in all 24 books: translated section by section from the
English by Gemini without looking at commentary-ja.tsv and
index-ja.tsv (see [Translating into Japanese](#translating-into-japanese)),
mechanically checked against commentary/en/ (headings, Latin verses,
paragraph counts), with proper names recorded book by book in
[commentary/ja/proper_noun.md](commentary/ja/proper_noun.md).

Book 1 has been checked against the English sections and summary, all
162 index rows and 50 notes. Its translation and proper-name locators
have been corrected; the reviewed index headwords have been unified
throughout index-ja.tsv. Two draft gloss differences remain report-only:
verse 11, edition 2 (破滅 for "plague"), and verse 46, edition 2
(機知に富んでいる for "vivid"). All 24 books have now had their
semantic review; the corrections have not yet been carried over to
texts/.

Book 2 has also been checked: 61 sections and the summary, 298 index
rows and 91 notes. Verse wording, commentary and headings have been
corrected. Its proper-name table now distinguishes quoted verses from
commentary and summary occurrences, including same-name commanders;
unattested entries have been removed. Reviewed index headwords and
names in descriptions are consistent throughout index-ja.tsv, and
book 2 notes use the commentary's name forms. Two further draft
differences remain report-only, both in edition 2: verse 152 can place
the prediction in the tenth year instead of the previously predicted
toil; verse 195 uses 同胞 for "ally". The source confirms that 同写本 in
the adapted note at 156 correctly refers to manuscript G. 2.

Book 3 has been checked: 25 sections and the summary, 108 index rows
and 42 notes. Verse wording, commentary and headings have been
corrected, including displaced and repeated words and the shield at
297. The proper-name table distinguishes verse, commentary and
summary occurrences, Dardanian from Dardanus, and the Phrygian Paris
from the Phrygian army. Reviewed index headwords are unified
throughout index-ja.tsv; names in descriptions and book 3 notes agree
with the commentary. At 321 the Latin Ulysses of Ovid is ウリクセス.
Four draft differences remain report-only, all in edition 2: at 253
Medea is treated as a title and Troad as Troy; at 260 the adapted
fragment has incomplete Japanese syntax; at 293 the Japanese specifies
oxhide where the English has hide. The edition-specific readings at
305, 341 and 343 are preserved.

Book 4 has been checked: 14 sections and the summary, 62 index rows
and 36 notes. The Paeonian herbs refer to Paeon, not Paeonia; the
patronymics Amaryncides and Imbrasides are retained and explained,
words displaced between verses have been restored, and in armis at
375 is rendered as wearing armor. Leucus consistently uses レウコス,
with the Homeric spelling Leucos preserved in the commentary. The
proper-name table identifies Aeacides as Ajax, keeps the ambiguity of
Atrides at 372, and distinguishes names, patronymics and their actual
verse, commentary and summary occurrences. Reviewed index headwords
are unified throughout index-ja.tsv, with names in descriptions and
book 4 notes made consistent. Simoisius is シモイシオス in the index;
the Homeric Simoeisius remains シモエイシオス in the commentary.
Two draft differences remain report-only, both in edition 2: at 360
the added Japanese verse gloss includes 冷たい for rigido; at 364 the
Japanese narrows a hardened weapon to a spear with a hardened point
and adds a gloss of the quoted Latin. The different readings and
identifications at 360, 368 and 372 are preserved. Aetolia uses
アイトリア in the shared name table and the book 5 mentions.

Book 5 has been checked: 45 sections and the summary, all 149 verses
(389–537), 197 index rows and 73 notes. Words displaced between verses
have been restored, including the seeing at 389, the heavy spear at
406, Tydides at 459 and the fields at 531. Maeonides and Oenides are
retained as patronymics; Phaestus uses パイストス, Maeonia マイオニア,
and Paphlagonians パフラゴニア人. The missile at 478 is not restricted
to an arrow; at 479 the possessive belongs to the decapitated man,
not to the sword; at 535 ipsa refers to Pallas herself. The index
corrects Mavortian Hector to マウォルスのヘクトル, not a son of Mars.
Reviewed headwords are consistent throughout index-ja.tsv, and names
in book 5 descriptions and notes agree with the commentary. The
proper-name table has 111 rows with actual verse, commentary and
summary locators, separates names from patronymics and adjectives,
and corrects mistaken identifications and relationships. The different
identifications of Atrides at 510 remain unresolved as in the English.
Seven draft differences remain report-only, all in edition 2: at 414
下層の時代 renders a later age; at 443 praise and a description of
restoration are added; at 451 鼻 renders nostril; at 471 兄 specifies
an older brother; at 485 and 525 Japanese glosses of Latin quotations
are added; at 512 手元の狂い specifies a cause for the missed cast.
These non-name draft differences and the files in texts/ are unchanged.

Book 6 has been checked: 7 sections and the summary, all 26 verses
(538–563), 42 index rows and 10 notes. Iliades is retained as
イリアデス; the age added to the sacrificial sheep and the shield
added to the summary have been removed. Displaced words and the
repeated command and question have been corrected. The index uses
アイトリアの for Aetolian and マウォルスの for Mavortian, without
making Hector a son of Mars. Its 38 proper-name rows distinguish
names and adjectives and give actual verse, commentary and summary
locators. Three non-name draft differences remain report-only, all
in edition 2 notes: at 539 Japanese makes Adrastus fall from a horse
instead of his chariot; at 548 純潔 renders "unwed"; at 557 Japanese
adds translations of the quoted Latin examples.

Book 7 has been checked: 25 sections and the summary, all 86 verses
(564–649), 121 index rows and 21 notes. Holding the child, the hero
and the kisses at 565–567, the lot and helmet at 587–588, the neck at
603–604, and the speaker's verb at 620–622 have been restored to their
own verses. The helmet crest is not described as feathers; the oak
palisade is a fence. Hesione's unusual identification as Ajax's mother
in this poem and the differing treatments of Atrides at 640–643 are
preserved and explained in the 58-row name table. Names in the index
and notes agree with the commentary, including イダイオス, ヘシオネ
and アウロラ. Eight non-name draft differences remain report-only:
the edition 4 index description at 580 broadens "father's family" to
父祖の家柄; edition 2 notes at 574 strengthen "might" to 可能性が高い,
at 586 add a gloss of ferum amorem, at 587 obscure the "when" in the
opening gloss, at 591, 612 and 615 add Japanese translations of Latin
quotations, and at 630 add ［連形］ to the two-syllable explanation.

Book 8 has been checked: 16 sections and the summary, all 36 verses
(650–685), 53 index rows and 14 notes. Ilian uses イリオンの; Ajax's
arms in the summary are 武具, and the arrows go into backs, not merely
behind the enemy. The warning at 651, Hector at 674 and the turning
and fleeing at 679–681 are placed in their own verses. The table has
38 rows, with Phrygia, Phrygians, Tydeus and Tydides distinguished.
The Japanese commentary at 677 also corrects an English source error:
the English calls Hector's spear the weapon that just struck Teucer,
although 674–675 explicitly says a stone. The English is unchanged;
Japanese correctly refers to the spear of Hector, who has just struck
Teucer with a stone. Three non-name draft differences remain
report-only: edition 4 at 660 makes "seems to be taken" prescriptive
(解されるべき); edition 2 at 667 adds (Agelaus Phradmonides), and at
681 adds (pessulus). The edition-specific readings and interpretations
of armis at 658 and 660 remain as in the sources.

Book 9 has been checked: 6 sections and the summary, all 10 verses
(686–695), 14 index rows and 2 notes. The added qualification of fate
as harsh has been removed, and the flame metaphor retained. Briseis'
return in the summary is an offer, not a completed event; her being
untouched does not assert virginity. Ajax uses アイアス. The 16-row
name table separates Thetis from the designation テティスの子, which
follows the English "son of Thetis". No further non-name draft meaning
differences were found.

Book 10 has been checked: 11 sections and the summary, all 45 verses
(696–740), 48 index rows and 24 notes. Eumediades uses エウメディアデス,
Rhesus レソス and Pelopeian ペロプス家の. The young man, the affairs
of the people and the throat at 713–714, 726–727 and 728–729 have been
restored to their own verses. Plunder is carried, not worn; the
unspecified stripping is not restricted to armor, and 殺害官 has been
corrected to 殺害者. The 31-row name table separates Eumedes and his
son's patronymic, Pelops and Pelopeian, and Thracians and Thracian.
Latin Ulysses in the Ovid references at 719 and 727 uses ウリクセス.
Two non-name draft differences remain report-only, both in edition 2:
at 706 Japanese adds the Latin glosses consilia and judicium; at 732
極めて稀 strengthens "rather rarely".

Books 6–10 were checked as a range: 65 sections and five summaries,
203 Latin verses, 278 index rows and 71 notes. Reviewed index
headwords are unified throughout index-ja.tsv; description and note
changes are confined to names in this range. The exact first-column
keys of the shared proper-name table still have one Japanese rendering
each. The non-name draft differences listed above remain unchanged,
and the corrections have not been carried over to texts/.

Book 11 has been checked: 8 sections and the summary, all 17 verses
(741–757), 28 index rows and 10 notes. Daybreak and refreshed soldiers
are translated accurately; the missile cloud, blades and received
pain have been restored to their own verses. The summary correctly
makes Hippolochus, not Agamemnon, the man rushing into battle. Isus
uses イソス. The 32-row name table records actual occurrences and
preserves Vollmer's distinction between the father of Coon and the
Trojan elder at 237. Four non-name draft differences remain
report-only, all in edition 2 notes: at 743 投槍 narrows missiles;
at 748 ホメロス詩人 renders Homerist without clearly conveying the
imitation; at 752 兄 specifies an older brother; at 753 the Japanese
adds the manuscript siglum (H.).

Book 12 has been checked: 6 sections and the summary, all 14 verses
(758–771), 19 index rows and 4 notes. The massive bars are placed in
their own verses, warlike Hector uses 好戦的な, and loosening the
woodwork is not smashing it. Firebrands are 燃えさし; the Greeks
climb aboard ships, not specifically their sterns; the repeated
missiles are not restricted to spears. The 13-row name table separates
Mars from the adjective Martius. No further non-name draft meaning
differences were found.

Book 13 has been checked: 5 sections and the summary, all 7 verses
(772–778), 21 index rows and 3 notes. Fierce at 774 describes
Amphimachus, not Hector. The killing verb at 776 is restored to its
own verse, and great-hearted is not reduced to boldness. Rhytieus
uses リュティエウス, separately from the place Rhytion リュティオン
in the 23-row name table. Two non-name draft differences remain
report-only, both in edition 2 notes: at 774 戦列 renders battle;
at 776 the Japanese adds a gloss of the Latin Alcathous.

Book 14 has been checked: 8 sections and the summary, all 11 verses
(779–789), 28 index rows and 2 notes. Hector is laid out at full
length; vomiting at 782 does not anticipate the blood at 783. The
verbs at 784 and 788 are restored to their own verses. Antenorides
uses アンテノリデス and Telamonian テラモンの. The 23-row name
table separates fathers, patronymics and adjectives and distinguishes
Acamas from the Thracian namesake in book 6. The edition 6 index
at 788 corrects the named victim of Peneleus from Promachus to Acamas,
as confirmed by the commentary at 789. No further non-name draft
meaning differences were found.

Book 15 has been checked: 7 sections and the summary, all 15 numbered
verses (790–804), including the unchanged missing-verse marker at
791, 21 index rows and 3 notes. Tireless Hector is 疲れを知らぬ;
Ajax stands at the stern, without the contradictory 船尾の舳先.
The boarding spear is a weapon used in fighting aboard ships.
Mavortian Hector uses マウォルスのヘクトル in the index, not a son
of Mars. The 21-row name table separates Mavors and Mavortian, and
records Plessis' supplied Pelopea wording only in the commentary.
Four non-name draft differences remain report-only, all in edition 2
notes: at 790 自らの陣船 makes the possessive unclear, and
奮い立たされ renders revived as encouragement; at 800 アイアスの
語り手 misrepresents Ajax himself speaking; at 801 軍船 narrows
ships to warships.

Books 11–15 were checked as a range: 34 sections and five summaries,
64 numbered Latin verses including the missing 791, 117 index rows
and 22 notes. Reviewed index headwords are unified throughout
index-ja.tsv; description and note changes are confined to names in
this range. The exact first-column keys of the shared proper-name
table still have one Japanese rendering each. The non-name draft
differences listed above remain unchanged, and the corrections have
not been carried over to texts/.

Book 16 has been checked: 9 sections and the summary, all 31 verses
(805–835), 42 index rows and 4 notes. The dark water of the spring,
the roaring warriors and the huge armor are translated accurately.
Patroclus catches the spear with a swift stroke, not merely a bodily
movement, and the reply does not add an unspecified throwing verb.
The sword at 834 agrees with the English and commentary. The 23-row
name table separates Dardanides from Dardanus, Mars from Mavors, and
Trojan adjectives from the Trojan army. Verse 827a, absent from LL,
is not supplied. Two non-name draft entries remain report-only,
both edition 2 notes: at 827 Japanese adds idiotismus; at 834 Latin
Homerist becomes ホメロス受容者（われらの詩人）, obscuring both the
Latin work and the imitation of Homer.

Book 17 has been checked: 1 section and the summary, all 3 verses
(836–838), 8 index rows and no notes. Telamonian Ajax uses テラモンの
アイアス; champion is not a flag-bearer. The 12-row name table
separates Telamon and Telamonian, and Priam and Priameius, and records
actual verse, commentary and summary occurrences. No further non-name
draft meaning differences were found.

Book 18 has been checked: 16 sections and the summary, all 53 verses
(839–891), 65 index rows and 28 notes. Nestorides uses ネストリデス;
Nereids use ネレイス, Clotho クロト, Luna ルナ and Paean パエアン.
Nymphs use ニンフ, consistently with the index. Water, horses,
engraving, sitting and playing the lyre are restored to their own
verses; added brackets and repeated words are removed. The shield's
middle at 889 is not armor worn by Mars, and the goddesses sit around
him in the summary. Full moon, tambourines and vineyard agree with
the English; grime is not restricted to mud. Paean's interpretation
as hymn or god and the damaged verse at 890 remain undecided. The
49-row name table adds missing attested names and removes Dardanus,
Dardanians and Teucrians, which do not occur in this book. Five
edition 4 index descriptions (864, 872 twice, 873 and 874) correct
the named maker from ウルカヌスの子 to ウルカヌス.
Six non-name draft entries remain report-only, all edition 2 notes:
at 844 Japanese adds glosses of declamare, defatigare and detonare;
at 845 it adds a gloss of deformat; at 851 it changes the cited lemma
violentum to violentus and adds a gloss; at 857 it uses 業火 for fires
and adds a translation of the quoted Latin; at 868 早馬 adds speed
to the changing horse; at 869 忠実に adds a claim of faithful rendering.

Book 19 has been checked: 7 sections and the summary, all 19 verses
(892–910), 30 index rows and 8 notes. The hero is borne in a whirlwind;
the young man belongs to 898, and the rescue at 899 is not repeated
at 901. The goddesses' unmarried status does not assert virginity;
the named Iphition is not described as famous. Teucrians use
テウクロイ, Cytherean キュテラの and Iulus ユルス. The 41-row name
table separates Thetis from Thetideius, Augustus from Augustan, Rome
from Romans, and Cythera from Cytherean, with missing named ancestors
and goddesses added. The laetis/Latiis readings remain distinct.
Two non-name draft entries remain report-only, both edition 2 notes:
at 901 正当にも strengthens not without reason; at 902 Japanese
adds a gloss of clara and identifies the Julian star as カエサルの彗星.

Book 20 has been checked: 8 sections and the summary, all 20 verses
(911–930), 20 index rows and 9 notes. Water, waves and heart are
restored to their own verses; headlong flow does not mean upside down,
and Juno sustains Achilles rather than describing a completed escape.
Deadly lines are not desperate lines; the timber securing the gates
is not restricted to a sliding bar. The 26-row name table separates
Phrygia and Phrygian and gives actual locators. Three non-name draft
entries remain report-only: edition 2 at 917 changes praetardare to
praetardo; edition 4 at 921 turns Kooten's authority into a proposal;
edition 2 at 929 adds a gloss of absumpta salus.

Books 16–20 were checked as a range: 41 sections and five summaries,
126 Latin verses, 165 index rows and 49 notes. Reviewed index
headwords are unified throughout index-ja.tsv; description and note
changes are confined to names in this range. The exact first-column
keys of the shared proper-name table still have one Japanese rendering
each. The non-name draft differences listed above remain unchanged,
and the corrections have not been carried over to texts/.

Book 21 has been checked: 4 sections and the summary, all 13 verses
(931–943), 11 index rows and 8 notes. Hector is at hand, not advancing;
the fleeing and the shut gates are restored to their own verses.
Nereian uses ネレウスの, consistently with the adjectival English,
and the summary uses ネレイス for Thetis. The 15-row name table
separates Trojan from Troy and records the combined designation
Tritonia Pallas without conflating it with Pallas alone. One non-name
draft entry remains report-only: edition 2 at 942 turns pursuing flight
and pressing on in the race into pursuing another runner, and adds a
Japanese gloss of viam insistere.

Book 22 has been checked: 12 sections and the summary, all 60 verses
(944–1003), 73 index rows and 19 notes. The goddess's appearance,
Hector, the heart, strength and life, and the horses' master's success
are restored to their own verses. Achilles poises his spear rather
than aims it; his unyielding refusal is 頑な, not courage described as
不屈. Hector's limbs and body remain distinct, and his spirit's
pleasure and its conditional qualification occupy 994 and 995
respectively. Dragging by the feet is not dragging with the feet;
celebration in the summary does not add drinking. The 31-row name
table separates Priam and Priameius, uses Nereian ネレウスの and
Pyrrhus ピュロス, removes the unattested Nereus, and adds actual
Aeacus and Nereid references. Seven non-name draft entries remain
report-only: edition 4 index descriptions at 950 twice render favor
as 神威; edition 2 notes at 952 make the armor itself thunder,
at 963 restrict sword to its point and add decidisse, at 965 add
intensity and glosses of Latin expressions, at 982 add the Latin
rhetorical term グラダーティオー, and at 997 add glosses and weaken
the description of the horses' proud, haughty movement. The
interpretations of the leader of leaders at 983 remain as in the
English, including its differing emphasis in the summary.

Book 23 has been checked: 9 sections and the summary, all 11 verses
(1004–1014), 21 index rows and 6 notes. A mourned friend is not a
friend in tears. Fierce of foot remains different from swift; the
corrupt word at 1008 is not supplied. The heavy discus is not a
forceful throw, the unstated victory verb is not repeated at 1013,
and Achilles is accompanied by the crowds. The 30-row name table
separates Tydeus and Tydides, Laertes and Laertius, and records actual
verse, commentary and summary occurrences. Laertius is ラエルテスの子
in the verse, following the English; the Vollmer index headword is
ラエルテスの, preserving the different treatment. One non-name draft
entry remains report-only: edition 2 at 1011 adds a Japanese gloss
of Superavit Epeus.

Book 24 has been checked: 12 sections and the summary, all 56 verses
(1015–1070), 78 index rows and 29 notes. Troy, the falls, the old age,
the restraining verb, the trembling palms, the Dardanian youth and
the gifts are restored to their own verses. Bravest is most courageous,
not strongest; Priam's flesh is 我が肉体, not 我が身代. Four-footed
horses, loosened hair and lowering the sails agree with the English.
The poet, rather than the boat itself, skirts the coast and reaches
the harbor. Ilian and Ilion use イリオンの and イリオン; Homer's
Ilios remains イリオス. The 35-row name table separates those names,
Argive, Greek, Dardanian, Phoebus and Apollo, adds missing gods, peoples
and the work's title, and records Calliope カリオペー and Pierides
ピエリデス. Ten non-name draft entries remain report-only: the
edition 4 index at 1066 turns the goal into a turning point
(折り返し点); the other nine are edition 2 notes:
at 1028 Japanese adds a gloss of the Greek and strengthens inferior
to 遠く及ばない; at 1032 it adds a gloss of ad genua accidere;
at 1041 it strengthens the possibility of a common author;
at 1045 it adds Priam to the opening gloss and translates the
conjectured verses; at 1048 it narrows
living bodies to prisoners sacrificed; at 1061 it adds robora flammae
glosses; at 1064 the chariot and four-horse team become two-wheeled
and the title Testimonia is specified; at 1069 it strengthens not
Latin to 正統なラテン語ではない and adds glosses; at 1070 it
adds the poet and a nautical interpretation to the opening gloss.
Plessis' six bodies at 1048 and the different readings at 1050 remain
as in the sources. The recipient of the lyres at 1068–1069 remains
uncertain.

Books 21–24 were checked as a range: 37 sections and four summaries,
140 Latin verses, 183 index rows and 62 notes. Reviewed index
headwords are unified throughout index-ja.tsv; description and note
changes are confined to names in this range. The exact first-column
keys of the shared proper-name table still have one Japanese rendering
each. All 24 books have now been checked. Non-name draft differences
remain report-only, and carrying corrections over to texts/ is the
next separate task.

Next:

1. [Done] commentary/ja/: the Japanese translation of commentary/en/,
   finished in all 24 books, with proper names recorded book by book in
   [commentary/ja/proper_noun.md](commentary/ja/proper_noun.md).
2. [Done] commentary/ja/, commentary-ja.tsv and index-ja.tsv are checked
   against each other, and the TSVs corrected (the names above all,
   and the 122 adapted notes; see [Checking the Japanese](#checking-the-japanese)).
3. The corrections are fed back to texts/: the notes to the editions'
   ilias-ja.md and COMMENTARY-ja.md, the index rows to INDEX-ja.tsv and
   index-ja.md; then `make notes` in texts/.
4. When the Japanese is done, deploying the translation as a website
   is to be considered.

### Translating into Japanese

Each file of commentary/en/ is translated into Japanese and written to
commentary/ja/ under the same name: the sections `NN/VVVV.md` and the
summaries `NN/README.md`.

- Book by book, the files of a book in order.  A file that already
  exists in commentary/ja/ is skipped, so that an interrupted run
  resumes where it left off.
- The Japanese follows the policy in commentary/README.md, as the
  English does, and the forms of [The forms settled](#the-forms-settled).
- Not read: commentary/commentary-ja.tsv, commentary/index-ja.tsv and
  the Japanese files in texts/ (`*-ja.md`, `INDEX-ja.tsv`,
  notes-ja.md).  The Japanese is made from the English alone, so that
  it can be checked against them afterwards (step 2 above).
- Written only in commentary/ja/ (including commentary/ja/proper_noun.md); no other
  file is changed, and nothing is committed.

The form:

- The structure of each file is kept exactly: the heading, the
  quotation block with every verse, then the commentary, paragraph for
  paragraph.
- Heading: `### 1–8 (*Iliad* 1.1–7)` becomes `### 1–8（『イリアス』1.1–7）`.
- Verses: each `> N Latin` line is kept unchanged, and the English line
  under it, `> (…)`, is replaced by the Japanese in full-width
  parentheses, `> （…）`; the lines with `>` alone between the verses
  are kept.
- Each verse is translated from its English line with the words of
  that verse only, even where a sentence runs over and the Japanese
  becomes less natural; no word is moved to another verse.  Where the
  English is ambiguous, the Latin quoted above it decides.
- The commentary: every sentence is translated, nothing added and
  nothing left out, in plain written Japanese in the である style.
  “…” becomes 「…」 and titles 『…』 (*Iliad* 1.5 becomes 『イリアス』1.5);
  Latin words stay in Latin, in italics as in the English
  (*Mavortius*).

The names: heroes and peoples in the usual Japanese forms from the
Greek, the gods in their Roman forms, as the English does.  Long
vowels are generally left out (ホメロス, not ホメーロス; ヘクトル), but
where a form with a long vowel is the one in common use, it is
preferred (ムーサ, ユノー).  The same person is always written the same
way, in the verses and in the commentary.

- Gods, in the verses and wherever the commentary speaks of the Latin:
  Iuppiter ユピテル, Iuno ユノー, Venus ウェヌス, Mars マルス, Minerva
  ミネルウァ, Pallas パラス, Vulcan ウルカヌス, Neptune ネプトゥヌス,
  Apollo アポロ, Phoebus ポエブス, Titan ティタン, Iris イリス, Thetis
  テティス, Latona ラトナ, Nereus ネレウス, Doris ドリス,
  Nereid(s) ネレイス（たち）, Nymph(s) ニンフ（たち）, Aesculapius アエスクラピウス, Oceanus
  オケアヌス, Orcus オルクス, the Muse(s) ムーサ, the Thunderer 雷神.
- Where the commentary tells Homer's scene, the Greek names: Zeus
  ゼウス, Hera ヘラ, Athena アテナ, Hephaestus ヘパイストス, Poseidon
  ポセイドン, Ares アレス, Aphrodite アプロディテ, Odysseus オデュッセウス,
  Apollo アポロン, Phoebus ポイボス, Asclepius アスクレピオス,
  Enyalius エニュアリオス, Paeon パイオン, Hebe ヘーベー,
  Dawn 曙の女神.
- Names that the English keeps in Latin are katakana of the Latin, and
  the commentary explains them as the English does: Atrides アトリデス,
  Pelides ペリデス, Aeacides アエアキデス, Tydides テュディデス,
  Priamides プリアミデス, Thestorides テストリデス, Dardanides
  ダルダニデス, Laertiades ラエルティアデス, Thalysiades タリュシアデス,
  Imbrasides インブラシデス, Maeonides マエオニデス, Oenides オエニデス, Somnus
  ソムヌス, Aurora アウロラ, Mavors マウォルス, Ignipotens イグニポテンス,
  Mulciber ムルキベル, Tritonia トリトニア, Cytherea キュテレア,
  Cygneis キュグネイス, Ilion
  イリオン, Ilios イリオス, Pergama ペルガマ, Amaryncides アマリュンキデス,
  Eumediades エウメディアデス, Iliades イリアデス,
  Antenorides アンテノリデス, Rhytieus リュティエウス,
  Nestorides ネストリデス, Clotho クロト, Lachesis ラケシス,
  Calliope カリオペー,
  Luna ルナ, Paean パエアン,
  Eurus エウルス, Hesperus ヘスペルス, Pierides ピエリデス;
  the others of the kind (Arctos, Lucifer, Luna …) likewise.
- Adjectives of names as 「〜の」: Mavortian Hector マウォルスのヘクトル,
  Telamonian Ajax テラモンのアイアス, Dardanian ダルダニアの, Ilian
  イリオンの, Argive アルゴスの, Doric ドリスの, Pelopeian ペロプス家の,
  Ithacan イタケ人, Paeonian パイオンの, Calydonian カリュドンの,
  Libyan リビュアの, Nereian ネレウスの.
- Persons: Achilles アキレウス, Hector ヘクトル, Agamemnon アガメムノン,
  Menelaus メネラオス, Priam プリアモス, Paris パリス, Alexander
  アレクサンドロス, Helen ヘレネ, Hecuba ヘカベ, Andromache アンドロマケ,
  Astyanax アステュアナクス, Ulysses ウリクセス, Ajax アイアス, Diomedes
  ディオメデス, Nestor ネストル, Patroclus パトロクロス, Aeneas
  アイネイアス, Teucer テウクロス, Sarpedon サルペドン, Chryses
  クリュセス, Chryseis クリュセイス, Briseis ブリセイス, Calchas カルカス,
  Idomeneus イドメネウス, Pandarus パンダロス, Glaucus グラウコス,
  Thersites テルシテス, Dolon ドロン, Rhesus レソス, Antilochus
  アンティロコス, Deiphobus デイポボス, Peleus ペレウス, Atreus
  アトレウス, Tydeus テュデウス, Telamon テラモン, Aeacus アイアコス,
  Oileus オイレウス, Antenor アンテノル, Hercules ヘラクレス,
  Polypoetes ポリュポイテス, Amarynceus アマリュンケウス,
  Charopus カロプス, Clonius クロニオス, Phidippus ペイディッポス,
  Euhaemon エウアイモン, Echemmon エケムモン, Plisthenes プレイステネス,
  Eussorus エウソロス, Phaestus パイストス, Isus イソス, Iulus ユルス, Pyrrhus ピュロス,
  Neoptolemus ネオプトレモス, Laertes ラエルテス, Epeus エペイオス,
  Panopeus パノペウス, Euryalus エウリュアロス; the others
  in the same way, from the Greek, by the same rule for long vowels.
- Peoples: Greeks ギリシア人, Danaans ダナオイ, Achaeans アカイア人,
  Pelasgians ペラスゴイ, Phrygians プリュギア人, Trojans トロイア人,
  Teucrians テウクロイ, Myrmidons ミュルミドン, Lycians リュキア人,
  Thracians トラキア人, Halizones ハリゾネス, Ethiopians アイティオピア人,
  Boeotians ボイオティア人, Aetolians アイトリア人, Locrians ロクリス人,
  Cretans クレタ人, Magnesians マグネシア人, Carians カリア人,
  Mysians ミュシア人, Maeonians マイオニア人, Paeonians パイオニア人,
  Cicones キコネス, Epeans エペイオス人, Athenians アテナイ人.
- Places and works: Troy トロイア, Olympus オリュンポス, Ida イダ,
  Xanthus クサントス, Ithaca イタケ, Chryse クリュセ, Lemnos レムノス,
  Aspledon アスプレドン, Athens アテナイ, Mycenae ミュケナイ,
  Syme シュメ, Rhodes ロドス, Phylace ピュラケ, Cythera キュテラ島,
  Asia Minor 小アジア, Homer ホメロス, the *Iliad*
  『イリアス』, the *Ilias Latina* 『イリアス・ラティナ』; Plessis プレシス,
  Vollmer フォルマー (where the commentary gives the readings of both
  editions).

At the end of each book, its proper names are recorded in
commentary/ja/proper_noun.md in a section for that book, with their English or
Latin forms, Japanese katakana, category/explanation, and verse
numbers.  The files written are reported, with every name not in the
lists above and the Japanese form chosen for it, so that the forms can
be checked before the next book.

### Checking the Japanese

When Gemini has finished (or finished a range of books), the checking
is taken over here, steps 2 and 3 of Next:

1. The files are committed as Gemini wrote them ("Add commentary/ja/NN/,
   … as translated by Gemini"), before any correction, so that the
   history keeps the two apart.
2. **Against the English.**  A mechanical first pass: the same files,
   headings and verses as commentary/en/, each `> N Latin` line
   unchanged, one `> （…）` under each, the same number of paragraphs.
   Then each section is read against the English: nothing added or
   left out, each verse with its own words only, the headings and
   quotation marks as in [Translating into Japanese](#translating-into-japanese).
3. **The names.**  The names in commentary/ja/proper_noun.md and those found in
   the files are checked with their verses and files; each person or
   people has one form, following the rules and lists above and
   [The forms settled](#the-forms-settled).  A form not in the lists
   is decided with the user and added to them.
4. **Against the TSVs.**  commentary/ja/ is compared with
   commentary-ja.tsv and index-ja.tsv, as the English was with
   index-en.tsv (see [Checking](#6-checking), 2): the Japanese headwords
   and the names in the descriptions of index-ja.tsv are made to agree
   with the translation, not the other way round, all the rows of a
   headword getting the same Japanese; the 122 adapted notes of
   commentary-ja.tsv are read against their English rows.  A Japanese
   note or description whose sense differs from the English is
   reported, not corrected (the drafts are not reviewed), except for
   the names.

The problems are reported before anything is edited, as a table
(verse, file, the passage, the English or the TSV row, a proposed
correction), in a form agreed with the user first.  The corrections of
commentary/ja/ and of the TSVs they entail are committed by book or
range of books.

Then step 3 of Next, as the English was carried over (see
[Carrying the names over to texts/](#7-carrying-the-names-over-to-texts)):
the diff of index-ja.tsv goes to the editions' INDEX-ja.tsv (the
Japanese headwords and the names in the descriptions) and index-ja.md
(the names in the descriptions only), after checking that each
headword has one Japanese form; the corrections of commentary-ja.tsv
go to the edition's ilias-ja.md and COMMENTARY-ja.md; then `make notes`
in texts/, committed apart from commentary/.

## How the present state is built

Each step depends only on the ones before it.

### 1. The texts

- The Latin Library (LL, texts/ilias.txt) is the base text, with its
  numbering and book divisions (texts/books.tsv).
- The Portuguese translation (Almeida, Coimbra 2021, on Scaffai's
  edition), from a PDF the user has, is extracted and paired with LL
  line by line by `make pt` in src/ (src/tmp/ilias_la_pt.txt, not
  committed); `make check-pt` confirmed that the pairing holds
  throughout, and src/PORTUGUESE.md records the places where the
  translation departs from LL (75–76 and 100–101 transposed, 827a,
  864, 890).  The book divisions of texts/books.tsv follow it, except
  book 15 (see texts/README.md, Books).
- The four editions (Lemaire, Baehrens, Plessis, Vollmer) are
  extracted by the scripts in src/, once, into texts/, and proofread
  against the page images (texts/PROOFREADING.md).  texts/concordance.md
  relates their verses to LL.
- Their English and Japanese translations (`ilias-{en,ja}.md`,
  `COMMENTARY-{en,ja}.md`, `index-{en,ja}.md`, …) are drafts, not yet
  reviewed.

### 2. The indexes

- Plessis and Vollmer have indexes of proper names (Lemaire and
  Baehrens have none).  Their index.md is compared letter by letter
  with the page images (texts/PROOFREADING.md, step 8) and turned into
  INDEX.tsv: headword, verse, form and description (see the README of
  each edition).
- INDEX-en.tsv and INDEX-ja.tsv are made from INDEX.tsv and
  index-{en,ja}.md by texts/index_translations.py.
- `make notes` in texts/ places the verses of the editions, their
  commentaries and the rows of their indexes side by side, verse by
  verse, in texts/notes{,-en,-ja}.md.

### 3. The data for the commentary

In commentary/, made by hand or once from texts/notes-en.md and
corrected by hand from then on (see commentary/README.md):

- alignment.tsv: the lines of the *Iliad* each verse renders
  (`make homer` in src/ downloads the Greek, not committed); it has
  been reviewed book by book against the Greek;
- commentary-en.tsv: the notes of the editions that apply to the text of
  LL;
- index-en.tsv: the rows of the indexes of Plessis and Vollmer at their
  verses, with the headword, its English, the form and the
  description in columns of their own.

### 4. The sections

`make greek` in src/ builds src/tmp/greek.md from LL, alignment.tsv
and commentary-en.tsv: the sections of the poem, each with its verses,
the lines of the *Iliad* they render, the notes that apply and the
Greek.

### 5. Generation

The user runs `make generate MODEL=gpt-6-astra` in commentary/ (the
API key is in the user's shell, not here), and the generated files are
committed as they are ("Add commentary/en/NN/, … as generated by
gpt-6-astra").  generate.py is given the section from greek.md and
the previous section; the first section of a book is given the
summary of the previous book (`en/NN/README.md`), so it is checked
with the corrections of that summary in mind.  Giving it the rows of
index-en.tsv as well may be proposed, not implemented.

### 6. Checking

Every section and the summary `en/NN/README.md` of a book are checked,
and the problems reported before anything is edited.

1. **The Latin, the notes and the Greek.**  Against the section in
   greek.md (the verse ranges of the books are in
   texts/books.tsv): the accuracy of the translation, the glosses
   followed, no uncertain reading stated as fact, and agreement with
   the books before.  Frequent errors in the drafts:
   - a sentence that runs over into the next verse translated twice or
     garbled, or cut by a full stop and resumed with "and";
   - words moved to another verse: each verse is translated with its
     own words only, even if the English is less natural;
   - names in the Latin form (*Vlixes*, *Danai*) where the policy in
     commentary/README.md gives the English, and explanations that
     become circular once the name is in English ("the Danaans are the
     Danaans");
   - a claim that the Latin omits what comes in the next or the
     previous section;
   - genealogies; *Myrmidones* for the Greeks at large (23, 180).
2. **The names**, against the rows of the verse in index-en.tsv:
   - the name in the translation agrees with the English headword and
     the policy, and the same person or people is called the same way
     throughout, in the translation and in the commentary (see
     [The forms settled](#the-forms-settled));
   - the form the row cites is translated in its own verse, as a name,
     not only as a gloss;
   - the person meant is the one the headword gives, above all for
     patronymics, epithets and periphrases (Atrides, Aeacides, *Priami
     filius*, *Pelopea iuventus*, Cytherea) and for homonyms (Acamas 1
     and 2, Aiax Locrus and Telamonius);
   - what the commentary says of the person (descent, people, who
     kills whom) agrees with the description.
   The English headwords are made to agree with the translation, not
   the other way round.  Where the headword is the person (MINERVA),
   its English is the person's name, and the forms of the translation
   (Pallas, Tritonia) are not matched with it; where the headword is
   itself a name, patronymic or epithet kept in the translation
   (Tydides, Tritonia, Ignipotens), its English is the translation's
   form.  All the rows of a headword have the same English.  Rows on a
   reading that LL does not have (151 *Pelasgi*, 195 *Nireus*) are
   kept; whether a row applies is judged here.
3. **The Portuguese.**  The finished translation is compared with the
   Portuguese (src/tmp/ilias_la_pt.txt, the Latin and Portuguese line
   by line, minding the differences in src/PORTUGUESE.md), as an aid
   for checking the content only (see Rules).

A mechanical first pass is allowed (e.g. listing the verses whose
translation lacks the English headword of a row); its script stays in
the scratchpad unless the user wants it kept.  The problems are
reported as a table (verse, file, the passage, the index row or note,
the kind of problem, a proposed correction), and the form of a report
is agreed with the user before going on.  The corrections are made in
the translation, the commentary and index-en.tsv together.

### 7. Carrying the names over to texts/

When the checking is done, the diff of commentary/index-en.tsv is
carried over to the editions' INDEX-en.tsv (the English headwords and
the names in the descriptions) and index-en.md (the names in the
descriptions only; its headwords are Latin), after checking that each
headword has one English form; then `make notes` in texts/.  The
cross-references of an index, which have no verse and so no row in
index-en.tsv, get the English of the same word in the other index or in
index-en.tsv.  The rest of the wording of the descriptions is left
alone.

## The forms settled

To be kept in the Japanese and in any later correction.

- Kept in Latin in the translation, as the policy's Atrides and
  Cytherea: the patronymics (Aeacides, Tydides, Priamides,
  Thestorides, Thalysiades, Dardanides for Hector …) and Ignipotens,
  Mulciber, Tritonia, Mavors, Somnus, Aurora, Arctos, Auster, Eurus,
  Hesperus, Lucifer, Luna, Ilion, Pergama, Iliades; their English
  headwords are the same.
- Adjectives as "the X-ian hero" (Pelopeian, Nereian, Calydonian,
  Aetolian, Cytherean), "Mavortian Hector" (543, 797, *Mavortius*),
  "warlike Hector" (760, *Martius*), "Telamonian Ajax", "Dardanian",
  "Ilian", "Doric", "the hero, son of Thetis" (690, 892).
- A Greek accusative in *-on* is given in the nominative (748
  Antiphus, 369 Leucus), and a name from an oblique case in its right
  nominative (246 Arsinous); Peneleus, Archelochus, Odius, Echemmon,
  Hypiron, Polyidus as in the translation.
- The commentary identifies Pallas once per section as "Minerva, the
  Athena of Homer".  Where it tells Homer's scene it uses the Greek
  names (Athena, Zeus, Hera, Hephaestus, Poseidon, Ares, Odysseus,
  Dawn); where it speaks of the persons of the Latin, the Roman ones
  (Jupiter, Mars, Aesculapius).
- Where Plessis and Vollmer read or identify differently, the
  commentary gives both ("Plessis …; Vollmer …") without deciding
  between them: 195, 201, 246, 341, 372, 510, 640, 752, 791, 843, 880,
  900, 983, 1008, 1050.  At 565 and 631 they differ only in the
  reading, the person being the same.
- Left as they are in the originals: 182 Plessis "twenty ships", 305
  "Paride vulnerato", 601 Plessis putting *Aeacides* (Ajax) under
  ACHILLES, 614 "saxum levat", 1048 "six bodies"; 82 *Plistheniden*
  has no row in either index (Vollmer's cross-reference under
  Agamemnon is not in the original, PDF p. 221); Plessis LAERTIUS "son
  of Laertes" against Vollmer Laertius "of Laertes".

## Correcting the data

- A note in commentary-en.tsv that seems wrong is checked against the
  original in the edition's `ilias.md` (and the page images if the
  text itself is in doubt) before the translation follows or departs
  from it.  The notes are the English drafts of the editions' Latin
  (or French) notes, and the bracketed glosses of a lemma were added
  in the drafts, not by the editors (338, *suas*: "his own" for "her
  own").  A note is corrected only where its English or Japanese
  differs from the original; an original that is itself mistaken or
  open to question is left as it is, since the translation does not
  have to follow it.  When the user agrees, it is corrected in every
  copy: commentary-en.tsv, the edition's `ilias-{en,ja}.md` and
  `COMMENTARY-{en,ja}.md`; then `make notes` in texts/.  Sections
  translated after the wrong note are corrected too.
- An index row that seems wrong is checked in the edition's index.md
  and ilias.md (the page images as a last resort) and reported.  It is
  corrected in double braces in index.md and index-{en,ja}.md, without
  braces in INDEX*.tsv, and by hand in commentary/index-en.tsv; then
  `make notes` in texts/.
- The translations of the editions' files are drafts: an English
  that differs from the Latin is reported, not corrected, except for
  the names carried over as in step 7.

## Rules

- Files are written in English, conversation is in Japanese.  "book 1"
  for a book; a line of the *Ilias Latina* is a verse, a line of the
  *Iliad* a line.
- LL stays the base text, with its numbering and book divisions
  (texts/books.tsv is not changed).  Arranging the editions into a
  text of our own would make a new edition; their differences go into
  the notes.
- The Portuguese translation is not in the public domain: it is only a
  guide to the book divisions and an aid for checking the content, and
  of it only src/PORTUGUESE.md, with short quotations, is published.
  The translation is made without consulting it and is compared with
  it only when finished; an error found is corrected from the Latin
  and the notes, not from its wording.
- A script extracts a source only once; later corrections are made in
  the output files, never in the scripts, and `make` does not rebuild
  an existing file.  The exception is the derived files rebuilt by
  `make` in texts/ (notes.md, notes-en/ja.md, iliad.md), which are not
  corrected by hand.
- The translations (`-en.md`, `-ja.md`) follow their originals one for
  one; a correction to an original is made in its translations too.
- Notation: hands as each edition prints them; a literal `<` is `\<`,
  `|` in a table `\|`.  Ask the user before settling a notation.
- Check facts in the sources before writing them, and mark conjectures
  as such.  Modern editions and commentaries (Scaffai, Kennedy,
  Perkins, Falcone & Schubert, Green) may be cited, not copied.
- The spelling of the English is American.
- The root README does not mention src/tmp or download steps, and lists
  as requirements only uv, make, curl and poppler-utils.
- Page images are a last resort: `src/tmp/<number>-<id>/NNN.jpg` (150
  dpi, NNN = PDF page; Vollmer p. 1 = PDF 159), or render with
  `pdftoppm -r 300..600` and crop with Pillow.
- Problems are reported first; nothing is edited until the user asks.
  Commit only after the user has reviewed, with /commit (staged files
  only).  The generated files, the corrections of the translation and
  the commentary (with the corrections of index-en.tsv they entail), and
  the corrections of the data in texts/ are committed separately.
  Do not restore or fix tracked files that look changed or missing;
  ask first.
