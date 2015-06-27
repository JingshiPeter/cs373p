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

p = f()
assert type(p) is GeneratorType
assert hasattr(p, "__next__")
assert hasattr(p, "__iter__")
assert(list(p) == [2, 3, 4])
assert(list(p) == [])

p = f()
assert next(p) == 2
assert next(p) == 3
assert next(p) == 4

try :
    assert next(p) == 5
    assert False
except StopIteration as e :
    assert type(e)      is StopIteration
    assert type(e.args) is tuple
    assert len(e.args)  == 0
else :
    assert False

q = iter(p)
assert q is p

print("Done.")
