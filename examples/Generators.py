#!/usr/bin/env python3

# -------------
# Generators.py
# -------------

# https://docs.python.org/3.5/library/stdtypes.html#generator-types
# https://docs.python.org/3.5/reference/simple_stmts.html#the-yield-statement

from types import GeneratorType

def f () :
    yield 2
    yield 3
    yield 4

print("Generators.py")

p1 = f()
assert type(p1) is GeneratorType
assert hasattr(p1, "__next__")
assert hasattr(p1, "__iter__")
assert(list(p1) == [2, 3, 4])
assert(list(p1) == [])

p2 = f()
assert next(p2) == 2
assert next(p2) == 3
assert next(p2) == 4

try :
    assert next(p2) == 5
    assert False
except StopIteration as e :
    assert type(e)      is StopIteration
    assert type(e.args) is tuple
    assert len(e.args)  == 0
else :
    assert False

p3 = f()
q = iter(p3)
assert q is p3

print("Done.")
