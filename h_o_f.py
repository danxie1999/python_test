#!/usr/bin/env python3

def add(a,b,x):
    return x(a) + x(b)

print (add(3,-3,abs))