#!/usr/bin/env python3

"""
CS373: Quiz #3 (14 pts)
"""

""" ----------------------------------------------------------------------
 1. Which of the following is NOT one of the four elements of the Circle of Life?
    [XP: Ch.2, Pg. 16]
    (5 pts)

a. build
b. choose
c. define
d. design
e. estimate

d.
"""

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    [Collatz]
    (5 pts)

a. 10
b. 11
c. 21
d. 22

b.

For odd n it's computing (3n + 1) / 2.
(3n + 1) / 2
3n/2 + 1/2
n + n/2 + 1/2
n + n/2 + 1, because n is odd
n + (n >> 1) + 1
"""

def f (n) :
    return n + (n << 1) + 1
print(f(7))

""" ----------------------------------------------------------------------
 3. Given positive integers, [math]b[/math] and [math]e[/math],
    let [math]m = (e / 2) + 1[/math].
    If [math]b < m[/math], then
    [math]max\_cycle\_length(b, e) = max\_cycle\_length(m, e)[/math].
    [Collatz]
    (4 pts)

a. False
b. True

Consider b = 10, e = 100.
Then m = (100 / 2) + 1 = 51.
max_cycle_length(10, 100) = max_cycle_length(51, 100)
All the numbers in the range [10, 50] can be mapped to numbers in the
range [51, 100] by one or more doublings, so none of the numbers in the
range [10, 50] could have a larger cycle length than the numbers in the
range [51, 100].
"""
