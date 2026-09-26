help: ## Show this help
	@grep -hE '^[a-zA-Z0-9_ -]+:.*## ' $(MAKEFILE_LIST) | \
		awk -F ':.*## ' '{printf "  %-12s %s\n", $$1, $$2}'

iliad: iliad.md ## List the lines of the Iliad in Vollmer's margin (iliad.md)

# Derived from Vollmer's text and never corrected by hand.
iliad.md: iliad.py ilias.txt 6-vollmer/ilias.md
	uv run python iliad.py . $@

.PHONY: help iliad
