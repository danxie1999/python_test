#!/usr/bin/env python3

from functools import reduce
def str2float (s):
    return {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}[s]

def fn (L):
    try:
        L1,L2=L.split('.')
        return reduce(lambda x,y: x*10 +y, map(str2float,L1+L2) )/10**(len(L2))
    except:
        return reduce(lambda x,y:x*10+y, map(str2float,L))

	
F=input('Please input a float:\n')

print (fn(F))