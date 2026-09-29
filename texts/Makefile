help: ## Show this help
	@grep -hE '^[a-zA-Z0-9_ -]+:.*## ' $(MAKEFILE_LIST) | \
		awk -F ':.*## ' '{printf "  %-12s %s\n", $$1, $$2}'

notes: notes.md notes-en.md notes-ja.md ## Put the verses, commentaries and indexes side by side (notes.md, -en, -ja)

iliad: iliad.md ## List the lines of the Iliad in Vollmer's margin (iliad.md)

# Derived from the files below and never corrected by hand, so it is
# rebuilt whenever they change.
EDITIONS = 2-lemaire 3-baehrens 4-plessis 6-vollmer
INDEXED = 4-plessis 6-vollmer
COMMENTARIES = $(foreach d,$(EDITIONS),$(d)/ilias.md $(d)/COMMENTARY.md)
notes.md: notes.py ilias.txt concordance.md $(COMMENTARIES) $(foreach d,$(INDEXED),$(d)/INDEX.tsv)
	uv run python notes.py . $@

notes-%.md: notes.py ilias.txt concordance.md $(COMMENTARIES) $(foreach d,$(EDITIONS),$(d)/COMMENTARY-%.md) $(foreach d,$(INDEXED),$(d)/INDEX-%.tsv)
	uv run python notes.py . $@ $*

# Derived from Vollmer's text and never corrected by hand.
iliad.md: iliad.py ilias.txt 6-vollmer/ilias.md
	uv run python iliad.py . $@

.PHONY: help notes iliad
