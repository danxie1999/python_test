#!/usr/bin/env python3

h=0
import time
for i in range(101,201):
    if i % 2 ==0:
        print(i)
        h+=1
        if h % 10 ==0:
            print('')
            time.sleep(1)
