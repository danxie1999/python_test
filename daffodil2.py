#!/usr/bin/env
n=0
for x in range(100,3000):
    a=str(x)
    a=" ".join(a)
    a=a.split()
    a[0]=int(a[0])
    a[1]=int(a[1])
    a[2]=int(a[2])
    if a[0]**3 + a[1]**3 + a[2]**3==x:
        print(x)
        n+=1
        if n % 10 ==0:
            print('')