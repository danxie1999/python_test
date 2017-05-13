#!/usr/bin/env python3
n=0
for x in range(100,1000):
    a=str(x)
    a=" ".join(a)
    a=a.split()
    b=int(a[0])
    c=int(a[1])
    d=int(a[2])
    if b**3 + c**3 + d**3 == x:
        print(x)
        n+=1
        if n % 10 ==0:
            print('')
	