FILES :=  \
    Quiz3 \
    Quiz5 \
    Quiz6 \
    Quiz7 \
    Quiz8 \
    Quiz9

%.pyx: %.py
	$<

%.pyy: %.py
	make clean
	coverage3 run --branch $<
	coverage3 report -m

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__

sync:
	make clean
	@echo `pwd`
	@rsync -r -t -u -v --delete \
    --include "*.py"            \
    --include "makefile"        \
    --exclude "*"               \
    . downing@$(CS):cs/cs373/github/python/quizzes/

test:
	for i in $(FILES);                                \
    do                                                \
        echo;                                         \
        echo make --no-print-directory clean $$i.pyx; \
             make --no-print-directory clean $$i.pyx; \
    done

versions:
	uname -a
	@echo
	printenv
	@echo
	which pip3
	@echo
	pip3 --version
	@echo
	pip3 list
	@echo
	which python3
	@echo
	python3 --version
	@echo
	which coverage3
	@echo
	coverage3 --version
	@echo
	python3 -c "import numpy; print(numpy.__version__)"
