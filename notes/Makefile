
PANDOC := pandoc

PANDOC_OPTS_ALL :=  --toc \
                    -f markdown-smart \
					--top-level-division=chapter \
					--variable urlcolor=cyan \
					--filter pandoc-crossref \
					--citeproc \
					--number-sections \
					--toc-depth=2 \
					--highlight-style=kate

# PANDOC_OPTS_ALL :=  -S --toc --smart \
# 					--top-level-division=chapter \
# 					--filter pandoc-crossref \
# 					--filter pandoc-citeproc \
# 					--listings -H listings-setup.tex 


PANDOC_PDF_OPTS := $(PANDOC_OPTS_ALL) \
					--default-image-extension=pdf \
					--variable documentclass=scrbook \
					--include-in-header=header_extra.tex \
					--variable=geometry:a4paper
#					--template=latex_template.tex \
#    				--variable=fontfamily:arev
					# --variable links-as-notes \


PANDOC_EPUB_OPTS := $(PANDOC_OPTS_ALL) \
					--default-image-extension=png \
					-t epub3 --toc-depth=1 \
					--epub-cover-image=cover.png

all: prog_notes.pdf prog_notes.epub bioinf_notes.pdf bioinf_notes.epub pymol.pdf

#all: prog_notes.pdf prog_notes.epub bioinf_notes.pdf bioinf_notes.epub pymol.pdf 

#$(PROJECT_PDFS)

clean: 
	rm -f prog_notes.pdf prog_notes.epub bioinf_notes.pdf bioinf_notes.epub pymol.pdf $(PROJECT_PDFS)



# CHAPTERS := Header.yml \
# 1.md \
# preface.md \
# python/before_you_begin.md \
# python/appendix_conda_and_pymol.md \
# python/writing_a_program.md \
# python/dealing_with_values.md \
# 2.md \
# python/the_order_of_events.md \
# python/do_the_steps.md \
# bioinf/bioinf_resources.md \
# python/controlling_behavior.md \
# 3.md \
# python/organizing_your_code.md \
# python/testing_your_code.md \
# bioinf/gwas.md \
# python/python_values_are_objects.md \
# 4.md \
# python/iteration_over_values.md \
# bioinf/assembly_and_mapping.md \
# python/working_with_data_files.md \
# project/some_new_project_without_iteration.md \
# 5.md \
# python/lists.md \
# bioinf/procaryote_gene_fiding.md \
# project/folding_project.md \
# 6.md \
# python/gluing_values_in_sequence.md \
# python/using_code_from_other_files.md \
# python/on_the_shoulders_of_giants.md \
# project/orf_project.md \
# 7.md \
# python/dictionaries.md \
# bioinf/pairwise_alignment.md \
# python/your_own_types_of_objects.md \
# project/translation_project.md \
# 8.md \
# bioinf/protein_substitution_matrices.md \
# bioinf/database_searching.md \
# project/alignment_project.md \
# 9.md \
# python/unleash_your_functions.md \
# bioinf/multiple_alignment.md \
# bioinf/models_of_dna_evolution.md \
# project/hiv_project.md \
# 10.md \
# bioinf/clustering.md \
# bioinf/phylogenetics.md \
# project/seqdist_project.md \
# 11.md \
# bioinf/hidden_markov_models.md \
# bioinf/neural_networks.md \
# 12.md \
# bioinf/sequence_annnotation.md \
# 13.md \
# project/assembly_project.md \
# 14.md \
# bioinf/rna_structure.md \
# references.md

PROG_CHAPTERS := python/Header.yml \
python/preface.md \
python/before_you_begin.md \
python/appendix_conda_and_pymol.md \
python/writing_a_program.md \
python/dealing_with_values.md \
python/the_order_of_events.md \
python/course_tools.md \
python/controlling_behavior.md \
python/organizing_your_code.md \
python/python_values_are_objects.md \
python/lists.md \
python/dictionaries.md \
python/gluing_values_in_sequence.md \
python/iteration_over_values.md \
python/working_with_data_files.md \
python/data_structures.md \
python/unleash_your_functions.md \
python/testing_your_code.md \
project/translation_project.md \
python/your_own_types_of_objects.md \
project/folding_project.md \
project/alignment_project.md \
project/codonbias_project.md \
project/hiv_project.md \
project/seqdist_project.md \
python/using_code_from_other_files.md \
project/orf_project.md \
project/assembly_project.md \
python/on_the_shoulders_of_giants.md \
python/references.md


PROG_SOURCE_CHAPTERS := $(foreach chapter,$(PROG_CHAPTERS),chapters/$(chapter))

prog_notes.pdf: $(PROG_SOURCE_CHAPTERS) Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o prog_notes.pdf $(PROG_SOURCE_CHAPTERS)

prog_notes.epub: $(PROG_SOURCE_CHAPTERS) Makefile
	$(PANDOC) $(PANDOC_EPUB_OPTS) -o prog_notes.epub $(PROG_SOURCE_CHAPTERS)

prog_notes.mobi: prog_notes.epub
	./kindlegen prog_notes.epub -o prog_notes.mobi

prog_notes: prog_notes.pdf prog_notes.epub prog_notes.mobi


BIOINF_CHAPTERS := bioinf/Header.yml \
bioinf/preface.md \
bioinf/bioinf_resources.md \
bioinf/gwas.md \
bioinf/assembly_and_mapping.md \
bioinf/procaryote_gene_fiding.md \
bioinf/pairwise_alignment.md \
bioinf/protein_substitution_matrices.md \
bioinf/database_searching.md \
bioinf/multiple_alignment.md \
bioinf/models_of_dna_evolution.md \
bioinf/clustering.md \
bioinf/phylogenetics.md \
bioinf/hidden_markov_models.md \
bioinf/neural_networks.md \
bioinf/sequence_annnotation.md \
bioinf/rna_structure.md \
bioinf/references.md

BIOINF_SOURCE_CHAPTERS := $(foreach chapter,$(BIOINF_CHAPTERS),chapters/$(chapter))

bioinf_notes.pdf: $(BIOINF_SOURCE_CHAPTERS) Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o bioinf_notes.pdf $(BIOINF_SOURCE_CHAPTERS)

bioinf_notes.epub: $(BIOINF_SOURCE_CHAPTERS) Makefile
	$(PANDOC) $(PANDOC_EPUB_OPTS) -o bioinf_notes.epub $(BIOINF_SOURCE_CHAPTERS)

bioinf_notes.mobi: bioinf_notes.epub
	./kindlegen bioinf_notes.epub -o bioinf_notes.mobi

# PyMol installation howto
pymol.pdf: chapters/python/appendix_conda_and_pymol.md Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o pymol.pdf chapters/python/appendix_conda_and_pymol.md

# # PyMol installation howto
# pymol.pdf: chapters/pymol.md Makefile header_extra.tex
# 	$(PANDOC) $(PANDOC_PDF_OPTS) -o pymol.pdf chapters/pymol.md

pymol: pymol.pdf

master_in_bioinformatics.pdf: chapters/master_in_bioinformatics.md Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o master_in_bioinformatics.pdf chapters/master_in_bioinformatics.md

master: master_in_bioinformatics.pdf

# Individually compiled programming projects
translation_project.pdf: chapters/translation_project.md Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o translation_project.pdf chapters/translation_project.md

assembly_project.pdf: chapters/assembly_project.md Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o assembly_project.pdf chapters/assembly_project.md

alignment_project.pdf: chapters/alignment_project.md Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o alignment_project.pdf chapters/alignment_project.md

hiv_project.pdf: chapters/hiv_project.md Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o hiv_project.pdf chapters/hiv_project.md

seqdist_project.pdf: chapters/seqdist_project.md Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o seqdist_project.pdf chapters/seqdist_project.md

orf_project.pdf: chapters/orf_project.md Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o orf_project.pdf chapters/orf_project.md

folding_project.pdf: chapters/folding_project.md Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o folding_project.pdf chapters/folding_project.md
	
codonbias_project.pdf: chapters/codonbias_project.md Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o codonbias_project chapters/codonbias_project.md

PROJECT_PDFS := translation_project.pdf assembly_project.pdf alignment_project.pdf hiv_project.pdf \
	seqdist_project.pdf orf_project.pdf folding_project.pdf codonbias_project.pdf

projects: $(PROJECT_PDFS)

extra_material.pdf: $(EXTRA_CHAPTERS) Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o extra_material.pdf $(EXTRA_CHAPTERS)

general_exercises.pdf: $(GENERAL_EXERCISES) Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o general_exercises.pdf $(GENERAL_EXERCISES)

prog: prog_notes.pdf prog_notes.epub 

bioinf: bioinf_notes.pdf bioinf_notes.epub




