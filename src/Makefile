URL = https://www.thelatinlibrary.com/ilias.html
ARCHIVE = https://archive.org/download
VOLLMER = p1poetaelatinimi02baeh
BAEHRENS = poetaelatinimino34baeh
PLESSIS = italiciiliaslati00plesuoft
LEMAIRE = poetaelatinimin00unkngoog
PDF =
CHECK_PDF = @test -n "$(PDF)" || { echo 'usage: make $@ PDF="path/to/book.pdf"'; exit 1; }
MODEL =
CHECK_MODEL = @test -n "$(MODEL)" || { echo 'usage: make $@ MODEL="vendor:model"'; exit 1; }

help: ## Show this help
	@grep -hE '^[a-zA-Z0-9_ -]+:.*## ' $(MAKEFILE_LIST) | \
		awk -F ':.*## ' '{printf "  %-12s %s\n", $$1, $$2}'
	@echo
	@echo '  PDF: the Portuguese edition (A Ilíada Latina, Coimbra University'
	@echo '       Press, 2021), e.g. make pt PDF="tmp/book.pdf"'
	@echo '  MODEL: the LLM for check-pt, e.g. make check-pt MODEL="gpt-5.6-terra"'

all: tmp/ilias.txt ## Download the Latin text and extract numbered verses

text: ../texts/ilias.txt ## Add the book headings to the Latin text (texts/ilias.txt)

vollmer: ../texts/6-vollmer/ilias.md ## Extract Vollmer's edition once (texts/6-vollmer)

baehrens: ../texts/3-baehrens/ilias.md ## Extract Baehrens's edition once (texts/3-baehrens)

plessis: ../texts/4-plessis/ilias.md ## Extract Plessis's edition once (texts/4-plessis)

lemaire: ../texts/2-lemaire/ilias.md ## Extract Lemaire's edition once (texts/2-lemaire)

concordance: ../texts/concordance.md ## Build the verse concordance once (texts/concordance.md)

commentary: ../texts/COMMENTARY.md ../texts/COMMENTARY-en.md ../texts/COMMENTARY-ja.md ## Put the verses and commentaries side by side (texts/COMMENTARY.md, -en, -ja)

download: tmp/ilias.html ## Download the Latin text from The Latin Library

tmp/ilias.html:
	mkdir -p tmp
	curl -fsSL -o $@ $(URL)

tmp/ilias.txt: tmp/ilias.html extract.py
	uv run python extract.py $< $@

../texts/ilias.txt: tmp/ilias.txt books.py
	mkdir -p ../texts
	uv run python books.py $< $@

tmp/6-$(VOLLMER).pdf:
	mkdir -p tmp
	curl -fsSL -o $@ $(ARCHIVE)/$(VOLLMER)/$(VOLLMER).pdf

# Generated once and then corrected by hand, so it is never rebuilt
# automatically (order-only prerequisites).
../texts/6-vollmer/ilias.md: | tmp/6-$(VOLLMER).pdf tmp/ilias.txt
	mkdir -p ../texts/6-vollmer
	uv run python vollmer.py tmp/6-$(VOLLMER).pdf tmp/ilias.txt ../texts/6-vollmer

tmp/3-$(BAEHRENS).pdf:
	mkdir -p tmp
	curl -fsSL -o $@ $(ARCHIVE)/$(BAEHRENS)/$(BAEHRENS).pdf

../texts/3-baehrens/ilias.md: | tmp/3-$(BAEHRENS).pdf tmp/ilias.txt
	mkdir -p ../texts/3-baehrens
	uv run python baehrens.py tmp/3-$(BAEHRENS).pdf tmp/ilias.txt ../texts/3-baehrens

tmp/4-$(PLESSIS).pdf:
	mkdir -p tmp
	curl -fsSL -o $@ $(ARCHIVE)/$(PLESSIS)/$(PLESSIS).pdf

../texts/4-plessis/ilias.md: | tmp/4-$(PLESSIS).pdf tmp/ilias.txt
	mkdir -p ../texts/4-plessis
	uv run python plessis.py tmp/4-$(PLESSIS).pdf tmp/ilias.txt ../texts/4-plessis

# The PDF of this scan has no text layer, so the OCR is read from the hOCR.
tmp/2-$(LEMAIRE)_hocr.html:
	mkdir -p tmp
	curl -fsSL -o $@ $(ARCHIVE)/$(LEMAIRE)/$(LEMAIRE)_hocr.html

../texts/2-lemaire/ilias.md: | tmp/2-$(LEMAIRE)_hocr.html tmp/ilias.txt
	mkdir -p ../texts/2-lemaire
	uv run python lemaire.py tmp/2-$(LEMAIRE)_hocr.html tmp/ilias.txt ../texts/2-lemaire

# Built from the texts above, then corrected by hand like them.
../texts/concordance.md: | ../texts/6-vollmer/ilias.md ../texts/3-baehrens/ilias.md ../texts/4-plessis/ilias.md ../texts/2-lemaire/ilias.md
	mkdir -p tmp
	uv run python concordance.py ../texts $@ tmp/concordance_check.txt

# Derived from the files below and never corrected by hand, so it is
# rebuilt whenever they change.
COMMENTARIES = $(foreach d,2-lemaire 3-baehrens 4-plessis 6-vollmer,../texts/$(d)/ilias.md ../texts/$(d)/COMMENTARY.md)
../texts/COMMENTARY.md: commentary.py ../texts/ilias.txt ../texts/concordance.md $(COMMENTARIES)
	uv run python commentary.py ../texts $@

../texts/COMMENTARY-%.md: commentary.py ../texts/ilias.txt ../texts/concordance.md $(COMMENTARIES) $(foreach d,2-lemaire 3-baehrens 4-plessis 6-vollmer,../texts/$(d)/COMMENTARY-%.md)
	uv run python commentary.py ../texts $@ $*

pt: tmp/ilias.txt extract_pt.py parallel.py ## Extract numbered translation and parallel text (PDF=...)
	$(CHECK_PDF)
	uv run python extract_pt.py "$(PDF)" tmp/ilias_pt.txt
	uv run python parallel.py tmp/ilias.txt tmp/ilias_pt.txt tmp/ilias_la_pt.txt

# Not a file target: the check resumes from the saved judgments, so it is
# run again until every verse is judged.
check-pt: check_pt.py ## Check with an LLM that the translation matches the verses (MODEL=...)
	$(CHECK_MODEL)
	uv run python check_pt.py -m "$(MODEL)" tmp/ilias_la_pt.txt tmp/ilias_la_pt_check.json

parts: split_pt.py ## Split the PDF text into sections in tmp/parts (PDF=...)
	$(CHECK_PDF)
	uv run python split_pt.py "$(PDF)" tmp/parts

.PHONY: help all text vollmer baehrens plessis lemaire concordance commentary download pt check-pt parts
