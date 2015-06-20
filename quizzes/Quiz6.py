#!/usr/bin/env python3

"""
CS373: Quiz #6 (14 pts)
"""

""" ----------------------------------------------------------------------
 1. Which of the following practices demonstrates effective pair programming?
    [All I Really Needed to Know about Pair Programming I Learned in Kindergarten]
    (2 pts)

a. Each partner writing separate parts.
b. Each partner writing both parts and then submitting the best.
c. Each partner writing both parts and then submitting the best combination.
d. Sharing a monitor and keyboard while coding.
e. One partner writing the interface and tests, the other the implementation.

d.
"""

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    (6 pts)

a. False True False False
b. False True True False
c. True False False True
d. True False True True

b.
"""

a = [2, 3, 4]
b = [v ** 2 for v in a]
print(hasattr(b, "__next__"),    end = " ")
print(hasattr(b, "__getitem__"), end = " ")
p = iter(b)
print(hasattr(p, "__iter__"),    end = " ")
print(p is b)

""" ----------------------------------------------------------------------
 3. What is the output of the following?
    (6 pts)

a. False True False False
b. False True True False
c. True False False True
d. True False True True

d.
"""

a = [2, 3, 4]
b = map(lambda v : v ** 2, a)
print(hasattr(b, "__next__"),    end = " ")
print(hasattr(b, "__getitem__"), end = " ")
p = iter(b)
print(hasattr(p, "__iter__"),    end = " ")
print(p is b)
