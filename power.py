#!/usr/bin/env python3

def power(x,n):
    s=1
    while n >0:
        n=n-1
        s=s*x
    return s

num1=input('Please input a number:')
num2=input('Please input power you want to add:')

try:
    num1=float(num1)
except ValueError:
    print('%s is not a number' % num1)
    exit()

try:
    num2=float(num2)
except ValueError:
    print('%s is not a number' % num2)
    exit()

print('The result is %s' % power(num1,num2))