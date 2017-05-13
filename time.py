#!/usr/bin/env python3

import time

g=(x for x in range(1,11) if x % 2 ==0)

for n in g:
    print (n)
    time.sleep(1)



