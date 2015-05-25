FILES :=

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
    . downing@$(CS):cs/cs373/python/examples/

test:
	for i in $(FILES);                     \
    do                                     \
        echo;                              \
        echo coverage run --branch $$i.py; \
             coverage run --branch $$i.py; \
        echo coverage report -m;           \
             coverage report -m;           \
    done
