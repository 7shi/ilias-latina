MODEL =
REVIEW_MODEL =
BOOKS =
VERSE =
CHECK_MODEL = @test -n "$(MODEL)" || { echo 'usage: make $@ MODEL="vendor:model"'; exit 1; }
CHECK_TARGET = @test -n "$(BOOKS)$(VERSE)" || { echo 'usage: make $@ BOOKS=... or VERSE=... (e.g. BOOKS=1-24 for all)'; exit 1; }

help: ## Show this help
	@grep -hE '^[a-zA-Z0-9_ -]+:.*## ' $(MAKEFILE_LIST) | \
		awk -F ':.*## ' '{printf "  %-12s %s\n", $$1, $$2}'
	@echo
	@echo '  MODEL: the LLM of the draft, e.g. make generate MODEL="gpt-6-luna"'
	@echo '  REVIEW_MODEL: the LLM that reviews the draft; without it the draft'
	@echo '         is the reading, reviewed by MODEL only if it leaves words unread'
	@echo '  BOOKS: the books to process, e.g. BOOKS=3 or BOOKS=1-3;'
	@echo '         BOOKS or VERSE is required'
	@echo '  VERSE: only the section of this verse, for testing, e.g. VERSE=9,'
	@echo '         or VERSE=NEXT for the first section missing from the start'

# Needs ../commentary/ja/, the example ja/01/0001.md and ja/ONESHOT.md.  With
# REVIEW_MODEL the drafts are kept in tmp/ and reviewed (without it, only
# those that leave words unread); tmp/models.tsv
# logs the model of each draft and review, tmp/errors.tsv the errors of
# each failed round.  Existing
# readings are skipped and existing drafts are not made again, so an
# interrupted run resumes where it left off.
generate: generate.py ## Read the Latin of the sections (MODEL=..., REVIEW_MODEL=..., BOOKS=..., VERSE=...)
	$(CHECK_MODEL)
	$(CHECK_TARGET)
	uv run python generate.py -m "$(MODEL)" $(if $(REVIEW_MODEL),-R "$(REVIEW_MODEL)") $(if $(BOOKS),-b "$(BOOKS)") $(if $(VERSE),--verse "$(VERSE)")

# For a harness that drafts in its own session: tmp/prompt.md gets the
# messages of the next missing section of BOOKS (or of VERSE) with the
# instruction to write the reading and run make check.
prompt: generate.py ## Write the messages of the next section for a harness (BOOKS=... or VERSE=...)
	$(CHECK_TARGET)
	uv run python generate.py --prompt $(if $(BOOKS),-b "$(BOOKS)") $(if $(VERSE),--verse "$(VERSE)")

check: generate.py ## Check the existing readings as drafts are checked (BOOKS=... or VERSE=...)
	$(CHECK_TARGET)
	uv run python generate.py --check $(if $(BOOKS),-b "$(BOOKS)") $(if $(VERSE),--verse "$(VERSE)")

.PHONY: help generate prompt check
