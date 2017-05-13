#!/usr/bin/env python3

for i in range(1,5):
    for j in range(1,5):
        for p in range(1,5):
            if (i!=j) and (j!=p) and (i!=p):
                print(i,j,p)
