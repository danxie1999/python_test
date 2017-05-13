#!/usr/bin/env python3

n=0

#while n < 100:
#    if n > 10:
#        break
#    print(n)
#    n= n + 2
#print('END')

import time

while n < 30:
    n=n+1
    if n % 2 == 0:
        continue
    print(n)
    time.sleep(1)
print('END')	