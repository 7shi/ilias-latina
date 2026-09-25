# Plan for the commentary

How the verse-by-verse commentary on the *Ilias Latina* will be prepared.
Background on the poem as a whole (date, author, transmission) belongs in
the Background section of [README.md](README.md), not in the notes.
Numbers in brackets refer to the Internet Archive list there.

## Base text

- The Latin text of The Latin Library, numbered 1–1070, with headings
  for the 24 books (`texts/ilias.txt`).
- Its editorial signs are kept and explained in the notes where they
  occur: `<que>`, `<et>` (words supplied by the editor, 517, 582, 685),
  `<>` (missing verse, 791) and the asterisks at 7, 890, 1008 and 1037.
- Where the numbering differs from Scaffai's edition (597, 791, 827a; see
  [src/README.md](src/README.md)), the note says so.

## Units

- The commentary is arranged by the 24 books (see the table in
  [texts/README.md](texts/README.md)), each book introduced by a short
  summary of what it keeps from the *Iliad* and what it leaves out.
- Notes are attached to a verse or a range of verses.

## Layers of each note

1. **Homer**: which lines of the *Iliad* the verse renders, and whether it
   follows, compresses, changes or adds to Homer.
   - Source: the Iliad line numbers in the margin of Vollmer's text [6];
     parallels cited by Plessis [4].
2. **Latin models**: echoes of Vergil, Ovid and other Latin poets.
   - Source: Wernsdorf's notes, reprinted by Lemaire [2]; Plessis on
     Vergilian and Ovidian imitation [4].
3. **Names and myth**: who the persons are and where else they appear in
   the poem.
   - Source: Plessis's index of names and subjects [4].
4. **Text**: only where it matters for the sense, e.g. the editorial signs
   above, or a place where the major editions disagree (Baehrens [3],
   Plessis [4], Vollmer [6]).  No full apparatus.
5. **Language**: grammar and vocabulary that a reader needs, kept short.

## Preparing the sources

The OCR texts are noisy, so the sources are first turned into per-verse
data and checked by hand against the page images on archive.org.

1. Verse concordance: the editions do not all number the verses in the
   same way.  Extract the text of the poem with its verse numbers from
   each edition (Lemaire [2], Baehrens [3], Plessis [4], Vollmer [6])
   and align it with The Latin Library text, noting omitted, added and
   transposed verses and differences in the book divisions.  Known so
   far: Vollmer prints 597 after 601, as Scaffai does, and 790 after
   794; Baehrens omits 69, counts a lacuna as 80 (so his 69–79 are
   70–80 here), and exchanges 107 and 109 and 873 and 874; Plessis keeps
   the numbers, prints the verses he rejects below the text, puts 108
   after 110 and 874 before 873, and adds 245 bis, 827 bis and a lacuna
   869 bis; Wernsdorf (Lemaire) counts 1075 verses, adding six (among
   them 827 bis) and one in place of 957, joining 84–85 in one verse,
   and putting 597 before 595 and 936 before 935.  All other tables
   are keyed to The Latin Library numbering through this concordance.
2. From Vollmer [6]: extract the Iliad line numbers from the margin and
   build a table *Latin verse → Iliad lines*.  This also gives the list of
   passages with no Homeric counterpart.
3. From Plessis [4]: turn the index into a table *name → verses*.
4. From Lemaire [2]: Wernsdorf's notes are split by the verse number they
   begin with (his own numbering) in `texts/2-lemaire/ilias.md`; key them
   to The Latin Library numbering and supply the labels that the OCR
   could not read, so they can be looked up per verse.
5. Publish these tables and the cleaned texts in the repository.  The
   sources are in the public domain, so processed texts derived from them
   can be published.

### Handling of the sources

- Organized for reference: Lemaire [2], Baehrens [3], Plessis [4] and
  Vollmer [6].  The pages on the *Ilias Latina* are first turned into
  structured text from the OCR (see [Order of work](#order-of-work) and
  [Editing the processed texts](#editing-the-processed-texts)).  The
  PDFs of [3], [4] and [6] also have a text layer that can be searched
  page by page; [2] has none, and its OCR is read from the hOCR file of
  the scan on archive.org.
- OCR text only: Spondanus [1] (text without notes, cited only as
  evidence of the attribution) and Butler [5] (a few pages on the poem).
- [3] and [6] contain several volumes or fascicles, so the pages of the
  *Ilias Latina* are located first.
- Pages are cited as printed in the book, not by the page number of the
  PDF.

### Editing the processed texts

- A script in `src/` extracts each source from its OCR only once (e.g.
  `make vollmer` for `texts/6-vollmer/`).  The OCR is left as it is, so
  the first version is uncorrected.
- From then on the files are corrected by hand, directly in place, and
  the corrections are committed.  Corrections are not kept in the
  scripts, and `make` does not rebuild a file that exists: running the
  script again would overwrite the corrections.
- A passage is corrected when it is used, or when an error is noticed,
  by reading the page image: at 150 dpi, or rendered again at 300–600
  dpi where small type (sigla, superscripts, punctuation) is unclear.
  Quotations, verse numbers, *Iliad* line numbers and sigla are always
  checked before they are used.
- Conventions for the corrected text: the sigla as printed, with Greek
  letters for the editions and the archetype (Ω, α β δ φ λ); the hands
  of a manuscript as each edition prints them (superscript numerals in
  Vollmer, G¹, W²; *m. 2* in Baehrens; *m 2* in Plessis); `|` for the
  separator between readings; abbreviation marks of a manuscript kept
  where printed (e.g. *Aptũ*).  A literal `<` (angle brackets for
  supplied words, `<que>`) is written `\<` and `|` in a table `\|`, so
  that they are not taken for markup.  Signs particular to one edition
  are described in its README (e.g. Baehrens's bold 0 for the
  manuscripts together, written as a plain 0, and ς for the later
  manuscripts, in `texts/3-baehrens/README.md`).

## Layout

`src/` holds only the scripts.  The work is done in separate directories:

- `texts/` — processed texts from the public-domain sources, one
  subdirectory per book of the Internet Archive list, named by its
  number and the editor (e.g. `texts/6-vollmer/`), with the tables
  described above.  The Latin
  Library text is published here as `texts/ilias.txt`: one continuous
  file with a heading for each book, so that the divisions can still be
  adjusted.
- `commentary/` — the commentary itself, arranged by book.

Downloads and intermediate files stay in `src/tmp/`, which is not
committed.  The Portuguese translation is not in the public domain, so
nothing derived from it is published; it was consulted for the book
divisions and is used only as an aid for checking the content.

## Other aids

- The Portuguese translation is used only to check the understanding of
  the Latin, through the parallel text built by the tools.
- Butler [5] and Plessis's introduction [4] supply the points for the book
  summaries (e.g. the uneven proportions of the books).
- Modern editions and commentaries (Scaffai, Kennedy, Perkins, Falcone &
  Schubert, Green) may be consulted and cited, but not copied.

## Order of work

1. Mark the 24 books in The Latin Library text with headings, using the
   divisions in `texts/README.md` (based on the Portuguese translation
   and checked against the Latin).  Done: `texts/ilias.txt`.
2. Organize the sources for reference, one at a time: Vollmer [6],
   Baehrens [3], Plessis [4], Lemaire [2].  The pages on the *Ilias
   Latina* are turned into structured text in `texts/` (e.g.
   `texts/6-vollmer/`), arranged by printed page and keyed to the
   verse numbers of The Latin Library: the text, the *Iliad* line
   numbers in the margin, the apparatus and notes split by verse, the
   preface, and the indexes.  The OCR text is the basis and is corrected
   by hand afterwards (see
   [Editing the processed texts](#editing-the-processed-texts)).
   Done for Vollmer (`texts/6-vollmer/`), Baehrens
   (`texts/3-baehrens/`), Plessis (`texts/4-plessis/`) and Lemaire
   (`texts/2-lemaire/`).
3. Collate the sources (steps 1–4 of
   [Preparing the sources](#preparing-the-sources)): the verse
   concordance, the book divisions of the editions (adjusting
   `src/books.py` if needed) and the tables keyed to The Latin Library
   numbering.
4. Write the notes for book 1 as a pilot and settle the format of the
   notes.
5. Proceed book by book.

## Open questions

- The name of the commentary directory in [Layout](#layout)
  (`commentary/`).
- The output format of the commentary (one Markdown file per book, or
  data files plus a generator).
- The language of the notes.
