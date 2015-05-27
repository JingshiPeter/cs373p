clean:
	cd examples; make clean
	@echo
	cd exercises; make clean
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

#   @rsync -r -t -u -v --delete              \
#   --exclude "*"                            \
#   ../../exercises/python/ python

#   @rsync -r -t -u -v --delete              \
#   --include "netflix/"                     \
#   --include "gitignore.sample"             \
#   --include "makefile.sample"              \
#   --include "RunNetflix.sample.in"         \
#   --include "RunNetflix.sample.out"        \
#   --exclude "*"                            \
#   ../../../projects/python/ projects

#   --include "Exceptions.py"                \
#   --include "Types.py"                     \
#   --include "Operators.py"                 \
#   --include "Generators.py"                \
#   --include "Iteration.py"                 \
#   --include "Iterables.py"                 \
#   --include "Variables.py"                 \
#   --include "Cache.py"                     \
#   --include "FunctionKeywords.py"          \
#   --include "FunctionDefaults.py"          \
#   --include "FunctionUnpacking.py"         \
#   --include "FunctionTuple.py"             \
#   --include "FunctionDict.py"              \
#   --include "GlobalVariables.py"           \
#   --include "ClassVariables.py"            \
#   --include "InstanceVariables.py"         \
#   --include "Closures.py"                  \
#   --include "Methods.py"                   \
#   --include "Functions.py"                 \
#   --include "RegExps.py"                   \
#   --include "Store9.py"                    \
#   --include "Copy.py"                      \
#   --include "Equals.py"                    \
#   --include "Complex.py"                   \
#   --include "Inheritance.py"               \
#   --include "Sequences.py"                 \
#   --include "Lists.py"                     \
#   --include "Strings.py"                   \
#   --include "Sets.py"                      \
#   --include "Dicts.py"                     \
#   --include "Builder.py"                   \
#   --include "Prototype.py"                 \
#   --include "Adapter.py"                   \
#   --include "Decorator.py"                 \
#   --include "Composite.py"                 \
#   --include "Visitor.py"                   \

#   --include "IsPrimeT.py"                  \
#   --include "IsPrimeT2.py"                 \
#   --include "Factorial.py"                 \
#   --include "Factorial2.py"                \
#   --include "RMSE.py"                      \
#   --include "RMSE2.py"                     \
#   --include "Reduce.py"                    \
#   --include "Reduce2.py"                   \
#   --include "Map.py"                       \
#   --include "Map2.py"                      \
#   --include "Collatz2.py"                  \
#   --include "Collatz3.py"                  \
#   --include "Decorators.py"                \
#   --include "Decorators2.py"               \
#   --include "Select.py"                    \
#   --include "Select2.py"                   \
#   --include "Project.py"                   \
#   --include "Project2.py"                  \
#   --include "CrossJoin.py"                 \
#   --include "CrossJoin2.py"                \
#   --include "ThetaJoin.py"                 \
#   --include "ThetaJoin2.py"                \
#   --include "NaturalJoin.py"               \
#   --include "NaturalJoin2.py"              \
#   --include "CreationalPatterns.py"        \
#   --include "FactoryMethodPattern.py"      \
#   --include "AbstractFactoryPattern.py"    \
#   --include "PrototypePattern.py"          \

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
	cd quizzes; make sync

test:
	cd examples; make test
	@echo
	cd exercises; make test
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
