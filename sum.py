#!/usr/bin/env python3

def sum_calc (*args):
    def sum ():
        ax=0
        for i in args:
            ax+=i
        return ax
    return sum

f=sum_calc(2,3,4,5)

print(f())

print (__locals__)


