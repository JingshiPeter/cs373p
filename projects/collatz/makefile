FILES :=                              \
    .gitignore                        \
    .travis.yml                       \
    collatz-tests/EID-RunCollatz.in   \
    collatz-tests/EID-RunCollatz.out  \
    collatz-tests/EID-TestCollatz.py  \
    collatz-tests/EID-TestCollatz.out \
    Collatz.html                      \
    Collatz.log                       \
    Collatz.py                        \
    RunCollatz.py                     \
    RunCollatz.in                     \
    RunCollatz.out                    \
    TestCollatz.py                    \
    TestCollatz.out

all:

check:
	@for i in $(FILES);                                         \
	do                                                          \
        [ -e $$i ] && echo "$$i found" || echo "$$i NOT FOUND"; \
    done

clean:
	rm -f .coverage
	rm -f *.pyc
	rm -f Collatz.html
	rm -f Collatz.log
	rm -f RunCollatz.out
	rm -f TestCollatz.out
	rm -rf __pycache__

config:
	git config -l

sync:
	make clean
	@echo `pwd`
	@rsync -r -t -u -v --delete \
    --include "*.in"            \
    --include "*.py"            \
    --include "makefile"        \
    --exclude "*"               \
    . downing@$(CS):cs/cs373/github/python/projects/collatz/

test: RunCollatz.out TestCollatz.out
	make collatz-tests
	@echo
	make Collatz.html
	@echo
	make Collatz.log
	@echo
	make check

collatz-tests:
	git clone https://github.com/cs373-summer-2015/collatz-tests.git

Collatz.html: Collatz.py
	pydoc3 -w Collatz

Collatz.log:
	git log > Collatz.log

RunCollatz.out: RunCollatz.py
	./RunCollatz.py < RunCollatz.in > RunCollatz.out

TestCollatz.out: TestCollatz.py
	coverage3 run    --branch TestCollatz.py >  TestCollatz.out 2>&1
	coverage3 report -m                      >> TestCollatz.out
