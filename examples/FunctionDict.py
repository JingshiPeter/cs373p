#!/usr/bin/env python3

# ---------------
# FunctionDict.py
# ---------------

print("FunctionDict.py")

def f (x, y, **z) :
    return [x, y, z]

assert f(2, 3)               == [2, 3, {}]
assert f(2, 3, a = 4)        == [2, 3, {'a' : 4}]
assert f(2, 3, a = 4, b = 5) == [2, 3, {'a' : 4, 'b' : 5}]

#f(2, 3, {'b' : 5, 'a' : 4})   # TypeError: f() takes exactly 2 arguments (3 given)
#f(2, 3, [('b', 5), ('a', 4)]) # TypeError: f() takes exactly 2 arguments (3 given)

d1 = {"b" : 4, "a" : 3}
assert f(2, 5,     **d1)  == [2, 5, {'a' : 3, 'b' : 4}]
assert f(2, y = 5, **d1)  == [2, 5, {'a' : 3, 'b' : 4}]
u = (2,)
assert f(y = 5, *u, **d1) == [2, 5, {'a' : 3, 'b' : 4}]
assert f(*u, y = 5, **d1) == [2, 5, {'a' : 3, 'b' : 4}]
#f(2, **d1, y = 5)                                      # SyntaxError: invalid syntax

d2 = {"y" : 3, "x" : 2}
assert f(**d2) == [2, 3, {}]
#f(2, **d2)                   # TypeError: f() got multiple values for keyword argument 'x'

d3 = {"y" : 3}
assert f(2,     **d3) == [2, 3, {}]
assert f(x = 2, **d3) == [2, 3, {}]
#f(**d3)                            # TypeError: f() takes exactly 2 arguments (1 given)

d4 = {"y" : 3, "a" : 2}
assert f(2,     **d4) == [2, 3, {'a' : 2}]
assert f(x = 2, **d4) == [2, 3, {'a' : 2}]
#f(**d4)                                   # TypeError: f() takes exactly 2 arguments (1 given)

print("Done.")
