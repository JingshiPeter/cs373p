#!/usr/bin/env python3

def collatz_read (r) :
    return ((int(v) for v in s.split()) for s in r)

def collatz_eval (a) :
    return ((i, j, 1) for i, j in a)

def collatz_print (a) :
    return (str(i) + " " + str(j) + " " + str(v) + "\n" for i, j, v in a)

def collatz_solve (r, w) :
    for s in collatz_print(collatz_eval(collatz_read(r))) :
        w.write(s)
