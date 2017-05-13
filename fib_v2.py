#!/usr/bin/env python

i=int(input('Please input a number:\n'))

def fib (max):
    n,a,b=0,0,1
    while n < max:
        yield (b)
        a,b=b,a+b
        n+=1
    return 'done'

	
[ print(x) for x in fib(i)]