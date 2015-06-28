#!/usr/bin/env python3

# ----------------
# FunctionTuple.py
# ----------------

print("FunctionTuple.py")

def f (x, y, *z) :
    return [x, y, z]

assert f(2, 3)       == [2, 3, ()]
assert f(2, 3, 4)    == [2, 3, (4,)]
assert f(2, 3, 4, 5) == [2, 3, (4, 5)]

t = (3, 4)
assert f(2, 5,  t)  == [2, 5, ((3, 4),)]
assert f(2, 5, *t)  == [2, 5, (3, 4)]
assert f(2, *t)     == [2, 3, (4,)]
assert f(*t)        == [3, 4, ()]
#f(2, y = 5, *t)                          # TypeError: f() got multiple values for argument 'y'
#f(x = 2, y = 5, *t)                      # TypeError: f() got multiple values for argument 'x'

u = (2,)
assert f(y = 3, *u) == [2, 3, ()]
assert f(*u, y = 3) == [2, 3, ()]

d1 = {"y" : 3, "x" : 2}
assert f(**d1) == [2, 3, ()]
#f(2, **d1)                   # TypeError: f() got multiple values for keyword argument 'x'

d2 = {"z" : 4, "y" : 3}
#f(2, **d2)             # TypeError: f() got an unexpected keyword argument 'z'
#f(**d2)                # TypeError: f() got an unexpected keyword argument 'z'

d3 = {"y" : 3}
assert f(2,     **d3) == [2, 3, ()]
assert f(x = 2, **d3) == [2, 3, ()]
#f(**d3)                             # TypeError: f() takes at least 2 arguments (1 given)

d4 = {"y" : 3, "t" : 5}
#f(2,     **d4)         # TypeError: f() got an unexpected keyword argument 't'
#f(x = 2, **d4)         # TypeError: f() got an unexpected keyword argument 't'
#f(**d4)                # TypeError: f() got an unexpected keyword argument 't'

print("Done.")
