#!/usr/bin/env python 3

num=input('Please input a number:\n')


try:
    num=float(num)
except ValueError:
    print('Your input is not a number．')
    exit() 

if num > 0:
    print('The absolute value of',num,'is:',num)
else:
    print('The absolute value of',num,'is:',-num)