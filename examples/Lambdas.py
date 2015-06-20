#!/usr/bin/env python3

# ----------
# Lambdas.py
# ----------

from functools import reduce
from types     import FunctionType, LambdaType

print("Lambdas.py")

def add (i, j) :
    return i + j

def f (bf, i, j, k) :
    return bf(bf(i, j), k)

def g () :
    return lambda i, j : i + j

def h (i) :
    return lambda j : i + j

assert add(2, 3)       == 5
assert f(add, 2, 3, 4) == 9

x = lambda i, j : i + j
assert type(x)       == LambdaType
assert x(2, 3)       == 5
assert f(x, 2, 3, 4) == 9

x = g()
assert type(x)       == LambdaType
assert x(2, 3)       == 5
assert f(x, 2, 3, 4) == 9

i = 2
x = lambda j : i + j
assert type(x) == LambdaType
assert x(3)    == 5

x = h(2)
assert type(x) == LambdaType
assert x(3)    == 5

print("Done.")
