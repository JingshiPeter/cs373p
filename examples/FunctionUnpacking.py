#!/usr/bin/env python3

# --------------------
# FunctionUnpacking.py
# --------------------

import collections

print("FunctionUnpacking.py")

def f (x, y, z) :
    return [x, y, z]

t = (3, 4)
assert t            == (3, 4)
assert t            != (4, 3)
assert f(2, t, 5)   == [2, (3, 4), 5]
assert f(2, 5, t)   == [2, 5, (3, 4)]
assert f(2, *t)     == [2, 3, 4]
assert f(z = 2, *t) == [3, 4, 2]
assert f(*t, z = 2) == [3, 4, 2]
#f(*t, 2)                              # SyntaxError: invalid syntax
#f(x = 2, *t)                          # f() got multiple values for argument 'x'
#f(*t)                                 # TypeError: f() takes exactly 3 arguments (2 given)
#f(2, 5, *t)                           # TypeError: f() takes exactly 3 arguments (4 given)

d1 = {"z" : 4, "y" : 3, "x" : 2}
assert f(**d1) == [2, 3, 4]
#f(2, **d1)                      # TypeError: f() got multiple values for keyword argument 'x'

d2 = {"z" : 4, "y" : 3}
assert f(2,     **d2) == [2, 3, 4]
assert f(x = 2, **d2) == [2, 3, 4]
#f(**d2, 2)                        # SyntaxError: invalid syntax
#f(**d2, x = 2)                    # SyntaxError: invalid syntax
#f(**d2)                           # TypeError: f() takes exactly 3 arguments (2 given)
#f(2, 5, **d2)                     # TypeError: f() got multiple values for keyword argument 'y'

d3 = {"y" : 3}
assert f(2, z = 4, **d3) == [2, 3, 4]
#f(2, 4, **d3)                        # TypeError: f() got multiple values for argument 'y'

d4 = {"z" : 4, "y" : 3, "t" : 5}
#f(2,     **d4)                  # TypeError: f() got an unexpected keyword argument 't'
#f(x = 2, **d4)                  # TypeError: f() got an unexpected keyword argument 't'
#f(**d4)                         # TypeError: f() got an unexpected keyword argument 't'

t = (2, 3)
d5 = {"z" : 4}
assert f(*t, **d5) == [2, 3, 4]
#f(**d5, *t)                    # SyntaxError: invalid syntax

print("Done.")
