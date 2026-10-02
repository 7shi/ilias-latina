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
  been read against the English rows. The reported non-name draft
  meaning differences have now been checked against the originals,
  corrected where necessary and recorded in the proofreading log.
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

All 24 books have been checked. Completed checks and corrections are
recorded in [commentary/ja/PROOFREADING.md](commentary/ja/PROOFREADING.md).
The finalized Japanese names have also been carried over to the editions'
files in texts/, and notes-ja.md has been rebuilt with `make notes`.

## Review of the reported draft differences

All the previously reported differences have been checked against the
editions' original notes and index entries. Corrections were made where
the translations changed the sense; valid lexical alternatives and
accurate explanatory glosses were retained. The decisions for all 69
notes, four index descriptions and the English commentary at 677 are in
[commentary/ja/PROOFREADING.md](commentary/ja/PROOFREADING.md#reviewing-the-reported-draft-differences).
No item from that list remains unresolved. This was a review of the
reported items, not of every translated file of the editions.

An additional divided page continuation at 1049 was corrected during
the final check. The English corrections include the stone that struck
Teucer at 674–675, damaged page continuations, the tenth-year prediction at 152,
the edition's restoration statement at 443, and the order of naming
Asius and Amphimachus at 774. Both curated TSVs and the corresponding
edition copies are updated; `make notes` rebuilds notes-en.md and
notes-ja.md. The local context in src/tmp/greek.md is also rebuilt from
the corrected English notes.

## Next

1. [Done] commentary/ja/: the Japanese translation of commentary/en/,
   finished in all 24 books, with proper names recorded book by book in
   [commentary/ja/proper_noun.md](commentary/ja/proper_noun.md).
2. [Done] commentary/ja/, commentary-ja.tsv and index-ja.tsv are checked
   against each other, and the TSVs corrected (the names above all,
   and the 122 adapted notes; see [Checking the Japanese](#checking-the-japanese)).
3. [Done] The corrections have been fed back to texts/: the notes to the editions'
   ilias-ja.md and COMMENTARY-ja.md, the index rows to INDEX-ja.tsv and
   index-ja.md; then `make notes` in texts/.
4. [Done] The reported draft meaning differences and the English
   discrepancy at 677 have been reviewed, resolved and recorded in
   commentary/ja/PROOFREADING.md.
5. Stop before website work. The user has further checks to make first;
   wait for those instructions before starting the website.

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
   the names. The user subsequently authorized a source-based review
   of the reported differences, including English errors; that pass is
   complete and recorded in commentary/ja/PROOFREADING.md. Unreviewed
   draft material outside those items keeps the original policy.

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
  `COMMENTARY-{en,ja}.md`, `index-{en,ja}.md`, …) remain drafts outside
  the names and individual items reviewed in commentary/ja/PROOFREADING.md.

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
- The translations of the editions' files remain drafts outside the
  checked items. The user authorized correction of the reported meaning
  differences and any English errors found during that review; the
  completed corrections and accepted variants are recorded in
  commentary/ja/PROOFREADING.md. Other draft differences are reported
  before correction, as in the original workflow.

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
