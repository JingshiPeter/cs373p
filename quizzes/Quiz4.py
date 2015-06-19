#!/usr/bin/env python3

"""
CS373: Quiz #4 (14 pts)
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (2 pts)

a. 2 int type
b. int int type
c. int type type

c.
"""

print(type(2),   end = " ")
print(type(int), end = " ")
print(type(type))

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    (4 pts)

a. except finally g2
b. finally
c. g1 else finally g2
d. g1 else g2
e. g1 finally g2

c.
"""

def f (b) :
    if b :
        raise KeyError()
def g (b) :
    try :
        f(b)
        print("g1", end = " ")
    except KeyError :
        print("except", end = " ")
    else :
        print("else", end = " ")
    finally :
        print("finally", end = " ")
    print("g2")
g(False)

""" ----------------------------------------------------------------------
 3. What is the output of the following?
    (4 pts)

a. except finally g2
b. except g2
c. finally
d. finally g2
e. g1 else finally g2

a.
"""

def f (b) :
    if b :
        raise KeyError()
def g (b) :
    try :
        f(b)
        print("g1", end = " ")
    except KeyError :
        print("except", end = " ")
    else :
        print("else", end = " ")
    finally :
        print("finally", end = " ")
    print("g2")
g(True)

""" ----------------------------------------------------------------------
 4. What is the output of the following?
    (4 pts)

a. else
b. except finally g2
c. finally
d. finally g2
e. g1 else finally g2

c.
"""

def f (b) :
    if b :
        raise TypeError()
def g (b) :
    try :
        f(b)
        print("g1", end = " ")
    except KeyError :
        print("except", end = " ")
    else :
        print("else", end = " ")
    finally :
        print("finally", end = " ")
    print("g2")
g(True)
