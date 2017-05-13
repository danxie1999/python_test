#!/usr/bin/env python3

def myabs(x):
    if x >= 0:
        return x
    else:
        return -x

num=input('Please input a number:')

try:
    num=float(num)
except ValueError:
    print('%s is not a number.' % num)
    exit (2)

print('The absolute value of %s is %s' % (num,myabs(num)))