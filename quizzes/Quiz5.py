#!/usr/bin/env python3

"""
CS373: Quiz #5 (14 pts)
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (4 pts)

a. 2
b. 2.0
c. 2.5

c.
"""

print(5 / 2)

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    (4 pts)

a. 2
b. 2.0
c. 2.5

a.
"""

print(5 // 2)

""" ----------------------------------------------------------------------
 3. What is the output of the following?
    (6 pts)

a. A A 5
b. type A 5
c. type type 5
d. none of the above

b.
"""

def bind (n) :
    class A :
        def f (self, m) :
            return n + m
    return A
x = bind(2)
print(type(x), end = " ")
y = x()
print(type(y), end = " ")
print(y.f(3))
