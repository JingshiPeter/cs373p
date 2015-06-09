clean:
	cd examples; make --no-print-directory clean
	@echo
	cd exercises; make --no-print-directory clean
	@echo
	cd quizzes; make --no-print-directory clean

config:
	git config -l

init:
	touch README
	git init
	git add README
	git commit -m 'first commit'
	git remote add origin git@github.com:gpdowning/cs373p.git
	git push -u origin master

pull:
	@rsync -r -t -u -v --delete              \
    --include "Hello.py"                     \
    --include "Assertions.py"                \
    --include "UnitTests1.py"                \
    --include "UnitTests2.py"                \
    --include "UnitTests3.py"                \
    --include "Coverage1.py"                 \
    --include "Coverage2.py"                 \
    --include "Coverage3.py"                 \
    --exclude "*"                            \
    ../../../examples/python/ examples

push:
	make clean
	@echo
	git add .travis.yml
	git add examples
	git add exercises
	git add makefile
	git add quizzes
	git commit -m "another commit"
	git push
	git status

status:
	make clean
	@echo
	git add examples
	git add exercises
	git add quizzes
	git branch
	git remote -v
	git status

sync:
	@echo `pwd`
	@rsync -r -t -u -v --delete \
    --include "makefile"        \
    --exclude "*"               \
    . downing@$(CS):cs/cs373/github/python/
	@echo
	cd examples; make sync
	@echo
	cd exercises; make sync
	@echo
	cd quizzes; make sync

test:
	cd examples; make --no-print-directory test
	@echo
	cd exercises; make --no-print-directory test
	@echo
	cd quizzes; make test

versions:
	uname -a
	@echo
	printenv
	@echo
	which pip3
	@echo
	pip3 -V
	@echo
	pip3 freeze
	@echo
	which python3
	@echo
	python3 -V
	@echo
	which coverage3
	@echo
	coverage3 help | grep version
	@echo
	python3 -c "import numpy; print(numpy.__version__)"
