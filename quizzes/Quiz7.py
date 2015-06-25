#!/usr/bin/env python3

"""
CS373: Quiz #7 (14 pts)
"""

from functools import reduce
from numpy     import mean, sqrt, square, subtract
from operator  import sub

def rmse (a, p) :
    return sqrt(mean(square(subtract(a, p))))

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (4 pts)

a. ((2, 3), (4, 5), (6, 7))
b. ((2, 5), (3, 6), (4, 7))
c. [(2, 3), (4, 5), (6, 7)]
d. [(2, 5), (3, 6), (4, 7)]

d.
"""

print(list(zip((2, 3, 4), (5, 6, 7))))

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    (4 pts)

a. -5
b. -6
c. -8
d. -9

c.
"""

print(reduce(sub, (2, 3, 4), 1))

""" ----------------------------------------------------------------------
 3. What is the output of the following?
    (3 pts)

a. (-2, -3, -4)
b. (2, 3, 4)
c. [-2, -3, -4]
d. [2, 3, 4]

c.
"""

print(list(map(sub, (2, 3, 4), (4, 6, 8))))

""" ----------------------------------------------------------------------
 4. What is the output of the following?
    (3 pts)


a. 1.73205080757
b. 2.0
c. 2.38047614285

c.
"""

print(rmse((2, 3, 4), (4, 1, 7)))
