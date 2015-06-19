#!/usr/bin/env python3

# --------
# RMSEt.py
# --------

from timeit   import timeit
from unittest import main, TestCase

from RMSE import            \
    rmse_while,             \
    rmse_range_for,         \
    rmse_zip_for,           \
    rmse_zip_reduce,        \
    rmse_map_sum,           \
    rmse_zip_list_sum,      \
    rmse_zip_generator_sum, \
    rmse_numpy

def bind (f) :
    class MyUnitTests (TestCase) :
        def test_0 (self) :
            self.assertEqual(f((2, 3, 4), (2, 3, 4)), 0)

        def test_1 (self) :
            self.assertEqual(f((2, 3, 4), (3, 2, 5)), 1)

        def test_2 (self) :
            self.assertEqual(f((2, 3, 4), (4, 1, 6)), 2)

        def test_3 (self) :
            self.assertEqual(f((2, 3, 4), (4, 3, 2)), 1.632993161855452)

        def test_r (self) :
            print()
            print(f.__name__)
            t = timeit(f.__name__ + "(10000 * [1], 10000 * [5]) == 4", "from __main__ import " + f.__name__, number = 100)
            print("{:.2f} milliseconds".format(t * 1000))
            print()

    return MyUnitTests

rmse_while_tests             = bind(rmse_while)
rmse_range_for_tests         = bind(rmse_range_for)
rmse_zip_for_tests           = bind(rmse_zip_for)
rmse_zip_reduce_tests        = bind(rmse_zip_reduce)
rmse_map_sum_tests           = bind(rmse_map_sum)
rmse_zip_list_sum_tests      = bind(rmse_zip_list_sum)
rmse_zip_generator_sum_tests = bind(rmse_zip_generator_sum)
rmse_numpy_tests             = bind(rmse_numpy)

if __name__ == "__main__" :
    main()

"""
% RMSEt
.....
rmse_while
460.85 milliseconds

.....
rmse_range_for
354.54 milliseconds

.....
rmse_zip_for
317.86 milliseconds

.....
rmse_zip_reduce
420.90 milliseconds

....
rmse_map_sum
347.00 milliseconds

.....
rmse_zip_list_sum
300.14 milliseconds

.....
rmse_zip_generator_sum
316.72 milliseconds

.....
rmse_numpy
98.81 milliseconds

.
----------------------------------------------------------------------
Ran 40 tests in 2.623s

OK
"""
