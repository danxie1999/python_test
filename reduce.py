#!/usr/bin/env python3

from functools import reduce

def str2int(s):
    def fn (x,y):
        return x*10 + y
    def char2num(n):
	    return {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}[n]
    return reduce(fn,map(char2num,s))

n=input('Please input a string:')
	
print(str2int(n))