MODEL =
BOOKS =
VERSE =
CHECK_MODEL = @test -n "$(MODEL)" || { echo 'usage: make $@ MODEL="vendor:model"'; exit 1; }

help: ## Show this help
	@grep -hE '^[a-zA-Z0-9_ -]+:.*## ' $(MAKEFILE_LIST) | \
		awk -F ':.*## ' '{printf "  %-12s %s\n", $$1, $$2}'
	@echo
	@echo '  MODEL: the LLM, e.g. make generate MODEL="gpt-5.6-terra"'
	@echo '  BOOKS: the books to process, e.g. BOOKS=1-3 (default: all)'
	@echo '  VERSE: only the section of this verse, for testing, e.g. VERSE=9,'
	@echo '         or VERSE=NEXT for the first section or summary missing from the start'

# Needs ../src/tmp/greek.md (make greek in src/).  Existing files are
# skipped, so an interrupted run resumes where it left off.
generate: generate.py ## Translate and comment on the sections (MODEL=..., BOOKS=..., VERSE=...)
	$(CHECK_MODEL)
	uv run python generate.py -m "$(MODEL)" $(if $(BOOKS),-b "$(BOOKS)") $(if $(VERSE),--verse "$(VERSE)")

.PHONY: help generate
