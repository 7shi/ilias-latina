help: ## Show this help
	@grep -hE '^[a-zA-Z0-9_ -]+:.*## ' $(MAKEFILE_LIST) | \
		awk -F ':.*## ' '{printf "  %-12s %s\n", $$1, $$2}'

commentary: COMMENTARY.md COMMENTARY-en.md COMMENTARY-ja.md ## Put the verses and commentaries side by side (COMMENTARY.md, -en, -ja)

iliad: iliad.md ## List the lines of the Iliad in Vollmer's margin (iliad.md)

# Derived from the files below and never corrected by hand, so it is
# rebuilt whenever they change.
EDITIONS = 2-lemaire 3-baehrens 4-plessis 6-vollmer
COMMENTARIES = $(foreach d,$(EDITIONS),$(d)/ilias.md $(d)/COMMENTARY.md)
COMMENTARY.md: commentary.py ilias.txt concordance.md $(COMMENTARIES)
	uv run python commentary.py . $@

COMMENTARY-%.md: commentary.py ilias.txt concordance.md $(COMMENTARIES) $(foreach d,$(EDITIONS),$(d)/COMMENTARY-%.md)
	uv run python commentary.py . $@ $*

# Derived from Vollmer's text and never corrected by hand.
iliad.md: iliad.py ilias.txt 6-vollmer/ilias.md
	uv run python iliad.py . $@

.PHONY: help commentary iliad
