#!/usr/bin/env python3

city=str(input('Please input the city you came from:'))

age=int(input('Please input your age:'))

if age > 18 and city == 'BeiJing':
    print ('You are a BeiJing adult')
elif age <= 18 and city == 'BeiJing':
    print ('You are a teenager in BeiJing')
else:
    print ('You are',age,'years old and live in',city )