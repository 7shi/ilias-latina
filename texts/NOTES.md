# Notes

Findings from checking the texts in this directory against each other
and against the page images.

## The Latin Library text

### The asterisks in ilias.txt

[ilias.txt](ilias.txt) has an asterisk (`*`) in four verses: after a
word in two of them, and on both sides of a word in the other two.

| LL | ilias.txt |
|---|---|
| 7 | protulerant\* ex quo discordia pectora pugnas, |
| 890 | quem diua poesis reliquae\* circaque sedebant |
| 1008 | Tydides \*tyrsin\* cursu pedibusque ferocem |
| 1037 | Nec uitam mihi nec magnos \*concedere\* honores, |

The four editions print these verses as follows (verse numbers and
pages as in [concordance.md](concordance.md)).

**LL 7**

- Wernsdorf ([7, p. 516](2-lemaire/ilias.md#p-516)): Ex quo
  contulerant discordi pectore pugnas.  The note gives Pertulerant ex
  quo discordia pectora pugnas from Guelf. 1.
- Baehrens ([7, p. 8](3-baehrens/ilias.md#p-8)): Ut primum tulerant
  discordi pectore pugnas (scripsi).
- Plessis ([7, p. 3](4-plessis/ilias.md#p-3)): Volverunt ex quo
  discordi pectore turbas, after Havet.
- Vollmer ([7, p. 1](6-vollmer/ilias.md#p-1)): † Protulerant ex quo
  discordia pectora turbas.  Protulerant is the reading of PW; the
  apparatus says "versus incipiebat ab V littera, emendatio incerta".

**LL 890**

- Wernsdorf ([895, p. 592](2-lemaire/ilias.md#p-592)): Diva potens
  Atropos circa, reliquaeque sedebant, from Guelf. 1.
- Baehrens ([890, p. 51](3-baehrens/ilias.md#p-51)): Post quem diua
  potens belli; circaque sedebant (belli scripsi).
- Plessis ([890, p. 70](4-plessis/ilias.md#p-70)): the same, after
  Baehrens.
- Vollmer ([890, p. 46](6-vollmer/ilias.md#p-46)): quem diva †poesis
  †reliquae circaque sedebant; he conjectures Diva potens bellique;
  Atropos c. q. s.

**LL 1008**

- Wernsdorf ([1013, p. 603](2-lemaire/ilias.md#p-603)): Tydides circi
  cursu, pedibusque ferorum, his own conjecture; the note calls the
  verse corrupt in all the books.
- Baehrens ([1008, p. 56](3-baehrens/ilias.md#p-56)): Tydides cunctos
  curru pedibusque feroces (cunctos scripsi), calling tyrsin and the
  like "monachale commentum".
- Plessis ([1008, p. 80](4-plessis/ilias.md#p-80)): Tydides cunctos
  curru pedibusque ferorum.
- Vollmer ([1008, p. 52](6-vollmer/ilias.md#p-52)): Tydides †tyrsin
  cursu pedibusque ferocem, followed by a row of dots; tyrsin is the
  reading of PE, and he conjectures Trosin (equis) and "post 1008 unum
  vel duos versus deesse puto".

**LL 1037**

- Wernsdorf ([1042, p. 605](2-lemaire/ilias.md#p-605)): Non vitam
  mihi, nec magnos concedere honores.
- Baehrens ([1037, p. 58](3-baehrens/ilias.md#p-58)): Non uitam mihi
  nec magnos concede fauores (fauores scripsi).
- Plessis ([1037, p. 83](4-plessis/ilias.md#p-83)): Non vitam mihi nec
  magnos concedere honores; concedere is the reading of LGA.
- Vollmer ([1037, p. 53](6-vollmer/ilias.md#p-53)): nec vitam mihi nec
  magnos concedere honores, without a dagger, followed by a row of
  dots: "post 1037 excidit versus ut opinor".

### Vollmer's daggers

On the page images of Vollmer (PDF pages 159, 204, 210 and 211) the
dagger stands once before each suspected word: †Protulerant (7),
†poesis †reliquae (890), †tyrsin (1008).  Verse 1037 has no dagger,
only the row of dots for a lost verse after it.  The transcription in
[6-vollmer/ilias.md](6-vollmer/ilias.md) agrees with the images in all
four verses, including the rows of dots after 1008 and 1037.

The asterisks of The Latin Library are not a copy of these daggers:

- Vollmer's text has daggers in 22 verses (7, 195, 200, 245, 308,
  325, 372, 424, 443, 548, 586, 688, 729, 766, 769, 841, 843, 846,
  890, 897, 943, 1008); ilias.txt marks only four.
- On the same page as 890, Vollmer prints Aeacidae nec †corpus erat
  (897), where ilias.txt has nec compar erat without a mark.
- LL 1037, which is marked in ilias.txt, has no dagger in Vollmer.
- The asterisks stand after the word (7, 890) or on both sides of it
  (1008, 1037), not before it as the daggers do.

### The base text

Each verse of ilias.txt was compared with the verse of the same LL
number in the four `ilias.md`, after normalizing case, u/v, i/j,
diacritics and punctuation.

| Edition | Verses identical to LL (of 1070) | Words differing |
|---|---|---|
| Vollmer | 938 (87.7%) | 175 |
| Baehrens | 752 (70.3%) | 483 |
| Plessis | 625 (58.4%) | 715 |
| Wernsdorf | 501 (46.8%) | 888 |

128 verses agree with Vollmer alone; no other edition agrees alone
with LL in more than 15.  Vollmer also omits LL 791 (Instaurantque
manus …), which ilias.txt leaves empty (`<>`).

The Latin Library's text is therefore based on Vollmer, but it is not
a copy of his text.  Most of the 131 verses that differ fall under
these kinds:

- **Spelling normalized**: assimilated prefixes (impune, irruit,
  immensa, collapsae for Vollmer's inpune, inruit, inmensa,
  conlapsae), exs- (exsistere, exsultat for existere, exultat), tunc
  for tum, aetherias for aethereas, Hecube and Palladis for Hecabe and
  Pallados.
- **Vollmer's emendations replaced by the manuscript reading (Ω)**:
  corpus for Higt's Pignus (90), teucer for Bondam's Nireus (195),
  uaria in certamina uis est for uario in certamine uirtus (262),
  pugnas for Havet's turbas (7).
- **Vollmer's conjectures from the apparatus put into the text**: mox
  Nestore pulsi (688), where Vollmer prints hoste repulso and writes
  "conieci mox Nestore pulsi" in the apparatus.
- **Another manuscript reading chosen**: captabant (PWBCDEFLV) for
  rimabant (MN) (300), argutaque (PWλ) for argiuaque (1050).

In the verses checked, the readings of ilias.txt that differ from
Vollmer's text are all found in his apparatus.

### Open questions

- Where the asterisks come from: the source of ilias.txt, or the
  person who entered it.  Verses 7, 890 and 1008 are the well-known
  cruces of the poem, so their agreement with Vollmer's daggers may be
  a coincidence.
- Whether ilias.txt reproduces a later edition built on Vollmer's
  apparatus rather than a revision of Vollmer made for The Latin
  Library; no such edition is organized in this repository.
