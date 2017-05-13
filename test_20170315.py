#!/usr/bin/env python3

import os

os.chdir('C:/python_test/test')

with open('test.txt','r') as f:
    print (f.read(1))
    f.seek(0)
    print (f.read(1))


for i in range(0,20):
	print(i)


    



