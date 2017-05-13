#!/usr/bin/env python3

import math

def quadratic (a,b,c):
    q=b*b-4*a*c
    if q < 0:
#        return 'There is no result for your input'
        print('There is no result for your input %s %s %s' % (a,b,c))
        
    else:
        x1=(-b+math.sqrt(q))/(2*a)
        x2=(-b-math.sqrt(q))/(2*a)
        print('The result for the quadratic is %.2f and %.2f' % (x1,x2))
        

num1=input('Please input first number:')
num2=input('Please input second number:')
num3=input('Please input third number:')

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
	
try:
    num3=float(num3)
except ValueError:
    print ('%s is not a number.' % num3)
    exit()

quadratic(num1,num2,num3)
