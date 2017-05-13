#!/usr/bin/env python3


def cycle (n):
    for i in range(2,n+1):
        if n%i==0:
            n/=i
            if n == 1:
                print(n,'OK')
            else:
                print(i)
                return(n)
	
cycle(200)