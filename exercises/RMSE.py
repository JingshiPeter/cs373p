#!/usr/bin/env python3

# -------
# RMSE.py
# -------

from functools import reduce
from math      import sqrt
from numpy     import mean, sqrt, square, subtract

def rmse_while (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert hasattr(a, "__len__")
    assert hasattr(p, "__len__")
    assert hasattr(a, "__getitem__")
    assert hasattr(p, "__getitem__")
    i = 0
    v = 0
    while i != len(a) :
        v += (a[i] - p[i]) ** 2
        i += 1
    return sqrt(v / len(a))

def rmse_range_for (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert hasattr(a, "__len__")
    assert hasattr(p, "__len__")
    assert hasattr(a, "__getitem__")
    assert hasattr(p, "__getitem__")
    v = 0
    for i in range(len(a)) :
        v += (a[i] - p[i]) ** 2
    return sqrt(v / len(a))

def rmse_zip_for (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert hasattr(a, "__len__")
    assert hasattr(p, "__len__")
    assert hasattr(a, "__iter__")
    assert hasattr(p, "__iter__")
    z = zip(a, p)
    v = 0
    for x, y in z :
        v += (x - y) ** 2
    return sqrt(v / len(a))

def rmse_zip_reduce (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert hasattr(a, "__len__")
    assert hasattr(p, "__len__")
    assert hasattr(a, "__iter__")
    assert hasattr(p, "__iter__")
    z = zip(a, p)
    v = reduce(lambda v, a : v + (a[0] - a[1]) ** 2, z, 0)
    return sqrt(v / len(a))

def rmse_map_sum (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert hasattr(a, "__len__")
    assert hasattr(p, "__len__")
    assert hasattr(a, "__iter__")
    assert hasattr(p, "__iter__")
    v = sum(map(lambda x, y : (x - y) ** 2, a, p))
    return sqrt(v / len(a))

def rmse_zip_list_sum (a, p) :
    """
    O(n) in space
    O(n) in time
    """
    assert hasattr(a, "__len__")
    assert hasattr(p, "__len__")
    assert hasattr(a, "__iter__")
    assert hasattr(p, "__iter__")
    z = zip(a, p)
    v = sum([(x - y) ** 2 for x, y in z])
    return sqrt(v / len(a))

def rmse_zip_generator_sum (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert hasattr(a, "__len__")
    assert hasattr(p, "__len__")
    assert hasattr(a, "__iter__")
    assert hasattr(p, "__iter__")
    z = zip(a, p)
    v = sum((x - y) ** 2 for x, y in z)
    return sqrt(v / len(a))

def rmse_numpy (a, p) :
    """
    O(n) in space
    O(n) in time
    """
    return sqrt(mean(square(subtract(a, p))))
