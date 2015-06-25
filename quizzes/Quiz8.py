#!/usr/bin/env python3

"""
CS373: Quiz #8 (14 pts)
"""

from functools import reduce
from numpy     import mean, sqrt, square, subtract
from operator  import sub

""" ----------------------------------------------------------------------
 1. In the paper, "Mariner 1", what was the software bug?
    (4 pts)

a. the conversion of a 16-bit number to a 64-bit number
b. the conversion of a 64-bit number to a 16-bit number
c. the ommission of a hyphen
d. the presence of a hyphen

c.
"""

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    (5 pts)

a. [[4, 9, 16]] [4, 9, 16, 25]
b. [[4, 9, 16]] [4, 9, 16]
c. [4, 9, 16] [4, 9, 16, 25]
d. [4, 9, 16] [4, 9, 16]

c.
"""

x = [2, 3, 4]
y = [v ** 2 for v in x]
z = (v ** 2 for v in x)
x += [5]
print(list(y), end = " ")
print(list(z))

""" ----------------------------------------------------------------------
 3. What is the output of the following?
    (5 pts)

a. [[4, 9, 16]] [4, 9, 16, 25]
b. [[4, 9, 16]] [4, 9, 16]
c. [4, 9, 16] [4, 9, 16, 25]
d. [4, 9, 16] [4, 9, 16]

d.
"""

x = (2, 3, 4)
y = [v ** 2 for v in x]
z = (v ** 2 for v in x)
x += (5,)
print(list(y), end = " ")
print(list(z))
