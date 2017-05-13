#!/usr/bin/env python3

def power (a,b):
    s=1
    while b>0:
        b=b-1
        s=s*a
    return s

num1=input('Please input a number:')
num2=input('Please input the number of power:')

try:
    num1=float(num1)
except ValueError:
    print ('%s is not a number.' % num1)
    exit()

try:
    num2=float(num2)
except ValueError:
    print ('%s is not a number.' % num2)
    exit()

print ('%.0f powers %.0f equal to %.2f' % (num1,num2,power(num1,num2)))
	