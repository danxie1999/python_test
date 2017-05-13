#!/usr/bin/env python3

def hanno (n,x,y,z):
    if n==1:
        print (x,'-->',z)
    else:
        hanno(n-1,x,z,y)
        hanno(1,x,y,z)
        hanno(n-1,y,x,z)

layer=int(input('Please input a number of layer for the hanno:'))

hanno(layer,'X','Y','Z')