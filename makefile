clean:
	cd examples; make clean
	@echo
	cd exercises; make clean
	@echo
	cd projects/collatz; make clean
	@echo
	cd quizzes; make clean

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
	@echo
	@rsync -r -t -u -v --delete              \
    --include "collatz/"                     \
    --include "Collatz.py"                   \
    --include "gitignore.sample"             \
    --include "makefile"                     \
    --include "makefile.sample"              \
    --include "RunCollatz.in"                \
    --include "RunCollatz.py"                \
    --include "RunCollatz.sample.out"        \
    --include "TestCollatz.py"               \
    --include "TestCollatz.sample.out"       \
    --include "travis.sample.yml"            \
    --exclude "*"                            \
    ../../../projects/python/ projects

push:
	make clean
	@echo
	git add .travis.yml
	git add examples
	git add exercises
	git add makefile
	git add projects
	git add quizzes
	git commit -m "another commit"
	git push
	git status

status:
	make clean
	@echo
	git add examples
	git add exercises
	git add projects
	git add quizzes
	git branch
	git remote -v
	git status

sync:
	@echo `pwd`
	@rsync -r -t -u -v --delete \
    --include "makefile"        \
    --exclude "*"               \
    . downing@$(CS):cs/cs373/python/
	@echo
	cd examples; make sync
	@echo
	cd exercises; make sync
	@echo
	cd projects/collatz; make sync
	@echo
	cd quizzes; make sync

test:
	cd examples; make test
	@echo
	cd exercises; make test
	@echo
	cd projects/collatz; make test
	@echo
	cd quizzes; make test

versions:
	which pip3
	pip3 -V
	@echo
	pip3 freeze
	@echo
	which python3
	python3 -V
	@echo
	which coverage3
	coverage3 help
	@echo
	python3 -c "import numpy; print(numpy.__version__)"
