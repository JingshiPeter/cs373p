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

#	@rsync -r -t -u -v --delete              \
#	--include "collatz/"                     \
#	--include "Collatz.py"                   \
#	--include "gitignore.sample"             \
#	--include "makefile.sample"              \
#	--include "RunCollatz.py"                \
#	--include "RunCollatz.sample.in"         \
#	--include "RunCollatz.sample.out"        \
#	--include "TestCollatz.py"               \
#	--include "TestCollatz.sample.out"       \
#	--exclude "*"                            \
#	../../projects/python/ projects
#	@rsync -r -t -u -v --delete              \
#	--include "netflix/"                     \
#	--include "gitignore.sample"             \
#	--include "makefile.sample"              \
#	--include "RunNetflix.sample.in"         \
#	--include "RunNetflix.sample.out"        \
#	--exclude "*"                            \
#	../../projects/python/ projects
#
#	--include "Equals.py"                    \
#	--include "Copy.py"                      \
#	--include "Complex.py"                   \
#	--include "Inheritance.py"               \
#	--include "Sequences.py"                 \
#	--include "Lists.py"                     \
#	--include "Strings.py"                   \
#	--include "Sets.py"                      \
#	--include "Dicts.py"                     \
#	--include "Builder.py"                   \
#	--include "Prototype.py"                 \
#	--include "Adapter.py"                   \
#	--include "Decorator.py"                 \
#	--include "Composite.py"                 \
#	--include "Visitor.py"                   \

push:
	git add .travis.yml
	git add *.py
	git add examples
	git add makefile
	git commit -m "another commit"
	git push
	git status

status:
	git add examples
	git branch
	git remote -v
	git status

sync:
	@echo `pwd`
	@rsync -r -t -u -v --delete      \
	--include "makefile"             \
	--exclude "*"                    \
	. downing@$(CS):cs/cs373/python/
