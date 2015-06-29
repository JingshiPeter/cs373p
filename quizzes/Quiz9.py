#!/usr/bin/env python3

"""
CS373: Quiz #9 (14 pts)
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (5 pts)

a. [6 8]
b. [7 9]
c. [7]
d. [8]

c.
"""

x = [2, 3, 4]
y = [4, 5]
z = (v + w for v in x if v % 2 for w in y if not w % 2)
print(list(z))

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    (5 pts)

a. {'ghi', 'abc', 'def'}
b. {(3, 'def'), (4, 'ghi'), (2, 'abc')}
c. {2, 3, 4}

c.
"""

x = {2 : "abc", 3 : "def", 4 : "ghi"}
y = {v for v in x}
print(y)

""" ----------------------------------------------------------------------
 3. What is the output of the following?
    (4 pts)

a. {'ghi': 4, 'def': 3, 'abc': 2}
b. {2 : "abc", 3 : "def", 4 : "ghi"}

a.
"""

x = {2 : "abc", 3 : "def", 4 : "ghi"}
y = {v : k for k, v in x.items()}
print(y)
