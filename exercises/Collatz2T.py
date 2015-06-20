#!/usr/bin/env python3

from io       import StringIO
from unittest import main, TestCase

from Collatz2 import collatz_solve

class TestCollatz (TestCase) :
    def test (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 1\n100 200 1\n201 210 1\n900 1000 1\n")

if __name__ == "__main__" :
    main()
