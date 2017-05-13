#!/usr/bin/env python3

import string
dig=0
spa=0
cha=0
other=0

s=input('Please input something:\n')

for i in s:
    if i.isalpha():
        cha+=1
    elif i.isspace():
        spa+=1
    elif i.isdigit():
        dig+=1
    else:
        other+=1

print ('Character number is {}, Space number is {}, digital number is {}, other number is {}'.format(cha,spa,dig,other))