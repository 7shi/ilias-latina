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

1. Verse concordance: it is not yet known whether the editions number the
   verses in the same way.  Extract the text of the poem with its verse
   numbers from each edition (Lemaire [2], Baehrens [3], Plessis [4],
   Vollmer [6]) and align it with The Latin Library text, noting
   omitted, added and transposed verses (e.g. Vollmer prints 790 after
   794) and differences in the book divisions.  All other tables are
   keyed to The Latin Library numbering through this concordance.
2. From Vollmer [6]: extract the Iliad line numbers from the margin and
   build a table *Latin verse → Iliad lines*.  This also gives the list of
   passages with no Homeric counterpart.
3. From Plessis [4]: turn the index into a table *name → verses*.
4. From Lemaire [2]: split Wernsdorf's notes by the verse number or lemma
   they begin with, so they can be looked up per verse.
5. Publish these tables and the cleaned texts in the repository.  The
   sources are in the public domain, so processed texts derived from them
   can be published.

## Layout

`src/` holds only the scripts.  The work is done in separate directories:

- `texts/` — processed texts from the public-domain sources, one
  subdirectory per book of the Internet Archive list (e.g.
  `texts/6-vollmer/`), with the tables described above.  The Latin
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
2. Build the verse concordance (step 1 above) and compare the book
   divisions of the other editions; adjust the first verses in
   `src/books.py` and rebuild `texts/ilias.txt` if needed.
3. Build the Vollmer table (step 2 above) for book 1 and check it.
4. Write the notes for book 1 as a pilot and settle the format of the
   notes.
5. Build the remaining tables and proceed book by book.

## Open questions

- The names of the other directories in [Layout](#layout)
  (`commentary/`, the subdirectories of `texts/`).
- The output format of the commentary (one Markdown file per book, or
  data files plus a generator).
- The language of the notes.
