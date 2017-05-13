#!/usr/bin/env python3

def fib(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    fibs=[1,1]
    for i in range(2,n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

NU=int(input ('Please input a number:'))

print(fib(NU))




