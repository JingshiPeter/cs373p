FILES :=       \
    IsPrime1T  \
    IsPrime2T  \
    FactorialT

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
    . downing@$(CS):cs/cs373/github/python/exercises/

test:
	for i in $(FILES);                      \
    do                                      \
        echo;                               \
        echo coverage3 run --branch $$i.py; \
             coverage3 run --branch $$i.py; \
        echo coverage3 report -m;           \
             coverage3 report -m;           \
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
	pip3 freeze
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
