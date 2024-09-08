MAKEFLAGS := -j 4

SHELL := /bin/bash

.DELETE_ON_ERROR:

PROBLEM_DESCRIPTIONS_MD := $(wildcard problems/*/description.md)
PROBLEM_DESCRIPTIONS_HTML := $(PROBLEM_DESCRIPTIONS_MD:%.md=%.html)

all: problems.pdf instructions.pdf

include $(wildcard problems/*/Makefile)

test-%:
	@for f in $(sort $(wildcard problems/$*/solutions/*.run)); do \
		for g in $(sort $(wildcard problems/$*/tests/*.in)); do \
			if /usr/bin/time -o/tmp/lucid-programming-time -f%E /usr/bin/timeout 10s colordiff -b "$${g/.in/.out}" <("$$f" < "$$g"); then \
				echo "Solution $$(basename $$f .run), Test $$(basename $$g .in): SUCCESS ($$(< /tmp/lucid-programming-time))"; \
			else \
				echo "Solution $$(basename $$f .run), Test $$(basename $$g .in): FAILURE ($$(< /tmp/lucid-programming-time))"; \
			fi \
		done \
	done

TESTS := $(shell echo problems/*/tests)
.PHONY: zip-tests
zip-tests: $(TESTS:=.zip)

%/tests.zip: zip-tests.py
	(echo $@: $*/tests/*.in $*/tests/*.out; echo $*/tests/*.in $*/tests/*.out :) > $@.dep
	shopt -s nullglob; ./$< --input $*/tests/*.in --output $*/tests/*.out > $@

-include $(wildcard problems/*/tests.zip.dep)

%.html: %.md convert.html.erb
	ruby -rerb -rnet/http -e 'puts ERB.new(File.read "convert.html.erb").result' < $< > $@

PDF_OPTIONS := -g -B 15mm -L 20mm -R 20mm -T 20mm -s Letter --print-media-type
