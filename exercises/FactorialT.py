#!/usr/bin/env python3

# -------------
# FactorialT.py
# -------------

# https://docs.python.org/3.4/library/math.html

from functools import reduce
from math      import factorial
from operator  import mul
from timeit    import timeit
from unittest  import main, TestCase

# recursive procedure
# linear recursive process
def factorial_recursion (n) :
    assert n >= 0
    if n < 2 :
        return 1
    return n * factorial_recursion(n - 1)

# recursive procedure
# linear iterative process
def factorial_tail_recursion (n) :
    assert n >= 0
    def f (n, v) :
        assert n >= 0
        assert v >= 1
        if n < 2 :
            return v
        return f(n - 1 , n * v)
    return f(n, 1)

# iterative procedure
# linear iterative process
def factorial_while (n) :
    assert n >= 0
    v = 1
    while n > 1 :
        v *= n
        n -= 1
    return v

def factorial_range_for (n) :
    assert n >= 0
    v = 1
    for i in range(1, n + 1) :
        v *= i
    return v

def factorial_range_reduce (n) :
    assert n >= 0
    return reduce(mul, range(1, n + 1), 1)

def bind (f) :
    class MyUnitTests (TestCase) :
        def test_0 (self) :
            self.assertEqual(f(0), 1)

        def test_1 (self) :
            self.assertEqual(f(1), 1)

        def test_2 (self) :
            self.assertEqual(f(2), 2)

        def test_3 (self) :
            self.assertEqual(f(3), 6)

        def test_4 (self) :
            self.assertEqual(f(4), 24)

        def test_5 (self) :
            self.assertEqual(f(5), 120)

        def test_6 (self) :
            print()
            print(f.__name__)
            t = timeit(f.__name__ + "(100)", "from __main__ import " + f.__name__, number = 1000)
            print("{:.2f} milliseconds".format(t * 1000))
            print()

    return MyUnitTests

factorial_recursion_tests      = bind(factorial_recursion)
factorial_tail_recursion_tests = bind(factorial_tail_recursion)
factorial_while_tests          = bind(factorial_while)
factorial_range_for_tests      = bind(factorial_range_for)
factorial_range_reduce_tests   = bind(factorial_range_reduce)
factorial_tests                = bind(factorial)

if __name__ == "__main__" :
    main()

"""
......
factorial_range_for
7.99 milliseconds

.......
factorial_range_reduce
7.62 milliseconds

.......
factorial_recursion
19.46 milliseconds

.......
factorial_tail_recursion
25.24 milliseconds

.......
factorial
0.88 milliseconds

.......
factorial_while
12.64 milliseconds

.
----------------------------------------------------------------------
Ran 42 tests in 0.079s

OK
"""
