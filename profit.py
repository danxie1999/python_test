#!/usr/bin/env python3

i=input('Please input your company\'s profit for this year:')

try:
    i=int(i)
except ValueError:
    print('%s is not a number' % i)
    exit(1)

arr=[1000000,600000,400000,200000,100000,0]
rat=[0.01,0.015,0.03,0.05,0.075,0.1]

r=0

for x in range(0,6):
    if i > arr[x]:
        p=(i-arr[x])*rat[x]
        r+=(i-arr[x])*rat[x]		
        print('%s is greater than %s and the profit for %s - %s is: %s' % (i,arr[x],arr[x],i,p))
        i=arr[x]

print('Total profile is: %s' % r)
 