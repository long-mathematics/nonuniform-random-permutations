.PHONY: all pdf check test verify

all: pdf

pdf:
	python3 scripts/build.py

check:
	python3 scripts/build.py --check

test:
	python3 -m unittest discover -s tests -v

verify:
	mkdir -p .build/thorp-audit
	g++ -std=c++17 -O2 scripts/thorp_moment_audit.cpp -o .build/thorp-audit/thorp_moment_audit
	.build/thorp-audit/thorp_moment_audit
