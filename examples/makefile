FILES :=       \
	Hello      \
	UnitTests3 \
	Coverage1  \
	Coverage2  \
	Coverage3

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
    . downing@$(CS):cs/cs373/github/python/examples/

test:
	for i in $(FILES);                      \
    do                                      \
        echo;                               \
        echo coverage3 run --branch $$i.py; \
             coverage3 run --branch $$i.py; \
        echo coverage3 report -m;           \
             coverage3 report -m;           \
    done
