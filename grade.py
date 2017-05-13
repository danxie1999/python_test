#!/usr/bin/env python3

num=input('Please input grade of Xiaoming for last semester:')
num1=input('Please input grade of Xiaoming for this semester:')

try:
    num=float(num)
except ValueError:
    print('%s is not a number' % num)
    exit()

try:
    num1=float(num1)
except ValueError:
    print('%s is not a number' % num1)
    exit()

Per=float((num1-num)/num1*100)

if Per > 0:
    print('Xiaoming\'s Academic achievement is imporving, his grade increased %.2f %% than last semester' % Per)
else:
    print ('Xiaoming\'s Academic achievement is falling behind, his grade decreased %.2f %% than last semester' % -Per)
