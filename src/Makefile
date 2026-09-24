URL = https://www.thelatinlibrary.com/ilias.html
PDF =
CHECK_PDF = @test -n "$(PDF)" || { echo 'usage: make $@ PDF="path/to/book.pdf"'; exit 1; }

help: ## Show this help
	@grep -hE '^[a-zA-Z0-9_ -]+:.*## ' $(MAKEFILE_LIST) | \
		awk -F ':.*## ' '{printf "  %-12s %s\n", $$1, $$2}'
	@echo
	@echo '  PDF: the Portuguese edition (A Ilíada Latina, Coimbra University'
	@echo '       Press, 2021), e.g. make pt PDF="tmp/book.pdf"'

all: tmp/ilias.txt ## Download the Latin text and extract numbered verses

text: ../texts/ilias.txt ## Add the book headings to the Latin text (texts/ilias.txt)

download: tmp/ilias.html ## Download the Latin text from The Latin Library

tmp/ilias.html:
	mkdir -p tmp
	curl -fsSL -o $@ $(URL)

tmp/ilias.txt: tmp/ilias.html extract.py
	uv run python extract.py $< $@

../texts/ilias.txt: tmp/ilias.txt books.py
	mkdir -p ../texts
	uv run python books.py $< $@

pt: tmp/ilias.txt extract_pt.py parallel.py ## Extract numbered translation and parallel text (PDF=...)
	$(CHECK_PDF)
	uv run python extract_pt.py "$(PDF)" tmp/ilias_pt.txt
	uv run python parallel.py tmp/ilias.txt tmp/ilias_pt.txt tmp/ilias_la_pt.txt

parts: split_pt.py ## Split the PDF text into sections in tmp/parts (PDF=...)
	$(CHECK_PDF)
	uv run python split_pt.py "$(PDF)" tmp/parts

.PHONY: help all text download pt parts
