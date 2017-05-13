#!/usr/bin/env python3

i=int(input('Please input a number:'))

try:
    i=int(i)
except ValueError:
    print('%s is not a number...' % i)
    exit (2)

arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]

r=0

for index in range(0,6):
    if i > arr[index]:
        p=(i-arr[index])*rat[index]
        k=i-arr[index]
        r+=(i-arr[index])*rat[index]
#        if i > arr[0]:
#            print('For part greater than %s: %s. The rate is %s. The profile is %s' % (arr[index],k,rat[index],p))
#        else:
        print('For part %s - %s. The rate is %s. The profile is %s' % (i,arr[index],rat[index],p))
        i=arr[index]

print ('The total profile is: %s' % r)		