#!/usr/bin/env python3

a=[]

x,y,z=input('Please input three numbers: (ex 2 3 4)\n').strip().split()

a.extend([x,y,z])
	
a.sort()

print (a)

