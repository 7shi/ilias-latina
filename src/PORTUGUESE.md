# Portuguese translation

Notes on the line-by-line correspondence between the Portuguese
translation (Bébio Itálico, *A Ilíada Latina*, translated by Priscilla
A. F. Almeida, Coimbra University Press, 2021) and the Latin text of The
Latin Library, as paired in `tmp/ilias_la_pt.txt` (see
[README.md](README.md#verse-numbering) for the verse numbering).

## Quotations

The page of the book at Coimbra University Press, to which the DOI
leads ([doi:10.14195/978-989-26-2205-7](https://doi.org/10.14195/978-989-26-2205-7)),
gives its license as CC BY-NC-ND 4.0, which does not allow adaptations,
while the colophon of the PDF states CC-BY 3.0.  The quotations here do
not rely on either license: they are short quotations for discussion,
as allowed for any published work, limited to the lines under
discussion, unaltered, with the translator's notes paraphrased or
quoted in a few words.  The quoted Portuguese text remains under the
rights of its translator and is not covered by the CC0 dedication of
this repository ([LICENSE](../LICENSE)); the analysis around it is.
Neither license would allow material derived from the translation to be
released under CC0, which is why nothing of it is adapted here.

## Method

`check_pt.py` (`make check-pt MODEL=...`) sends the parallel text to an
LLM (gpt-5.6-terra) in chunks cut at the ends of Latin sentences once
a chunk exceeds 20 verses, and has it return the labels of the matching
(ok) and mismatching (ng) verses as structured output.  Words moved to the
adjacent line by enjambment count as ok.  The judgments are written to
`tmp/ilias_la_pt_check.json`.

Of the 1070 verses, 10 were judged ng:

    75 76 84 94 100 104 348 788 827a 864

Every ng verse was then checked by hand against its neighbors.  None of
them comes from an error in the numbering or in the pairing of the
lines: the translation is aligned throughout.

## Lines transposed by the translator

In two places the translator renders a pair of verses in the reverse
order, so each line carries the content of the other.  The pairing is
correct; the transposition belongs to the translation.  The translator's
note on the translation (p. 89) states that the version follows the
Latin line by line where possible, but that terms sometimes had to be
adapted "within the same verse or across more than one verse" (*dentro
de um mesmo verso ou em mais de um verso*), since Portuguese lacks the
freedom of Latin word order.

### 75-76

    75 tendit in Atriden et, ni sibi reddat honestae
       avança contra o Atrida e ameaça-o de morte cruel,
    76 munera militiae, letum crudele minatur,
       se não lhe restituísse os prêmios da honrada campanha,

"Threatens him with cruel death" (*letum crudele minatur*, 76) comes in
line 75, and the condition "if he did not give back the rewards of
honorable service" (*ni sibi reddat honestae / munera militiae*, 75-76)
in line 76.

### 100-101

    100 ut mihi quae coniunx dicor tua quaeque sororis
        que queiras derrotar os aquivos caros a mim,
    101 dulce fero nomen, dilectos fundere Achiuos
        que sou dita tua esposa e tenho o doce nome de irmã,

"That you want to rout the Achaeans dear to me" (*dilectos fundere
Achiuos*, 101) comes in line 100, and "I who am called your wife and
bear the sweet name of sister" (*quae coniunx dicor tua quaeque sororis
/ dulce fero nomen*, 100-101) in line 101.  Line 101 was judged ok but
belongs to the same transposition.

## Differences in the text

### 827a

    827 Patroclus redditque uices et, mutua dona,
        rápido; este paga na mesma moeda e retribui o presente,
    827a (none)
         atirando à frente uma pedra que arremessa com enorme força:

The verse is present in Scaffai's edition, on which the translation is
based, and absent from The Latin Library ("hurling forward a stone that
he throws with great force").  This is the known numbering difference.
The label 827a itself marks it as an addition to the traditional
numbering: it is the line *Obicit et saxum ... cum pondere missum*
transmitted by part of the manuscripts, which Plessis prints in square
brackets as 827 bis, Wernsdorf in the text (his 831), and Baehrens and
Vollmer only in the apparatus (see [texts/concordance.md](../texts/concordance.md)).

### 864

    862 Illic Ignipotens mundi caelauerat arcem
        Ali o Ignipotente gravara a abóbada celeste, as estrelas, e as terras rodeadas
    863 sideraque et liquidis redimitas undique nymphis
        por toda a parte pelas líquidas ninfas do Oceano.
    864 Oceani terras et cinctum Nerea circum
        [Fizera também, maravilhosamente, as líquidas cidadelas nereidas] e Nereu cingido ao redor;

The bracketed words ("he had also made, marvelously, the watery
citadels of the Nereids") have no counterpart in the Latin text.  They
are printed so in the PDF, so they are not an extraction error, and no
footnote comments on them.  Elsewhere the brackets serve two purposes:
at 936 a whole verse is bracketed, which note 142 explains as
suppressed because the editor regards it as a gloss on 947-950, and at
1060 a word is supplied (*[companheiras]*).  Which of these applies at
864, and what in Scaffai's text underlies the addition, is not
established.  Besides, *Oceani terras* of 864 is rendered in lines
862-863.

### 890

    890 quem diua poesis reliquae* circaque sedebant
        † Átropos † e ao redor se assentavam

This verse was judged ok, but its translation does not render the Latin
of The Latin Library.  Note 132 states that the verse is corrupt in
Scaffai's edition and that the translation follows Scaffai's own
translation of it, where the name Atropos is printed between cruces.  The manuscripts disagree here: *diua poesis reliquae*
is the reading of most of them, some add the gloss *atropos* to
*diua*, and one reads *Diua potens atropos*.  Baehrens and Plessis
print the conjecture *Post quem diua potens belli*, Vollmer marks
*poesis* with cruces, and Wernsdorf prints *Diva potens Atropos circa,
reliquaeque sedebant* (see the apparatus of the editions in
[texts/](../texts/README.md)).

## Enjambment (acceptable)

A word is carried over to the adjacent line; the main content of each
line corresponds.

    84 castraque Myrmidonum iuxta petit et monet armis
       vem para perto do acampamento dos mirmidões e o aconselha a manter
    85 abstineat dextram ac congressibus; inde per auras
       a destra afastada das armas e dos combates; de lá, pelos ares

*armis* (84) is rendered in line 85 (*das armas*).

    348 incidit et tunicam ferro squamisque rigentem
        nas costas e corta a túnica enrijecida com escamas
    349 dissecat. Excedit pugna gemebundus Atrides
        de ferro. O Atrida, gemendo, sai da batalha

*ferro* (348) is rendered in line 349 (*de ferro*), and *dissecat* (349)
in line 348 (*corta*).

    788 Boeotumque Acamas Promachum, quem sternit atrocis
        Acamante, o beócio Prômaco; mas Acamante é derrubado
    789 Penelei dextra; inde cadit Priameia pubes
        pela destra do atroz Peneleu; depois, a priameia juventude sucumbe.

*atrocis* (788) is rendered in line 789 (*do atroz*).

## Misjudged (correct)

    94 magni diua maris, mecum labor iste manebit.
       deusa do grande mar, chamarei a mim esta tarefa.

    104 Talibus incusat dictis irata Tonantem
        Irada, com tais palavras censura o Toante

Both lines render their Latin verse faithfully.
