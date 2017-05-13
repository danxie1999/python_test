#!/usr/bin/env python3

def myabs(x):
    if not isinstance (x,(int,float)):
        raise TypeError('bad operand')
    if x >= 0:
        return x
    else:
        return -x

#num=input('Please input a number:')		
		
		
print ('The absolute value of %s is %s' % ('A', myabs('A')))