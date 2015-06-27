#!/usr/bin/env python3

def collatz_read (s) :
    a = s.split()
    return [int(a[0]), int(a[1])]

def collatz_eval (i, j) :
    return 1

def collatz_print (w, i, j, v) :
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

def collatz_solve (r, w) :
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
