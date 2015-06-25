#!/usr/bin/env python3

# ------------
# Iterators.py
# ------------

import types

class A :
    class B :
        def __init__ (self) :
            self.i = 2

        def __iter__ (self) :
            return self

        def __next__ (self) :
            if self.i == 5 :
                raise StopIteration
            j = self.i
            self.i += 1
            return j

    def __iter__ (self) :
        return A.B()

print("Iterators.py")

x = A()
assert type(x) is A
assert not hasattr(x, "__next__")
assert     hasattr(x, "__iter__")
assert(list(x) == [2, 3, 4])
assert(list(x) == [2, 3, 4])

p = iter(x)
assert type(p) is A.B
assert hasattr(p, "__next__")
assert hasattr(p, "__iter__")
assert(list(p) == [2, 3, 4])
assert(list(p) == [])

q = iter(p)
assert q is p

print("Done.")
