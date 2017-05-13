#!/usr/bin/env python3

weight=input('Please input your weight(kg):')
height=input('Please input your height(M, ex 1.75 M):')

try:
    weight=float(weight)
except ValueError:
    print('weight should be a number and %s is not a number.' % weight)
    exit (2)

try:
    height=float(height)
except ValueError:
    print('height should be a number and %s is not a number.' % height)
    exit (2)

bmi = weight/(height*height)

if bmi <= 18.5:
    print('Your weight is too loght, bmi value is %.2f' % bmi)
elif bmi <= 25:
    print('Your weight is normal, bmi value is %.2f' % bmi)
elif bmi <= 28:
    print('Your weight is sort of overweight, bmi value is %.2f' % bmi)
elif bmi <= 32:
    print('Your weight is overweight, bmi value is %.2f' % bmi)
elif bmi > 32:
    print('Obesity, Obesity, Obesity. bmi value is %.2f' % bmi)

