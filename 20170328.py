#!/usr/bin/env python3

from io import StringIO

f=StringIO('Hello, this is not \ntrue!')
read=f.readlines()

#for line in read:
#	print(line,end='')

#f.write(' world!')

#print(f.getvalue())