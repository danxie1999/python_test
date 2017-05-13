#!/usr/bin/env python3

import time
# this is how to format a date
date=time.strftime("%Y-%m-%d",time.localtime())

i=input('Please input a date: (ex %s)\n' % date)

while len(i) != 10:
    i=input('The format is wrong, Please input a date: ex %s\n' % date)

j=list(i)

for p in range(len(i)):
    if (p==4) or (p==7):
        if j[p] != '-':
            print ('The date format is wrong...')
            exit (2)
    else:
        try:
            j[p]=int(j[p])
        except ValueError:
            print('The date format is wrong...')
            exit (2)

year=i[:4]

#this is how to transform a list of int to string
year=int("".join(str(i) for i in year))


month=j[5:7]
month=int("".join(str(i) for i in month))

day=j[8:10]
day=int("".join(str(i) for i in day))


if month >= 13:
    print('%s cannot be a value for month.' % month)
    exit (2)

if day > 31:
    print ('%s cannot be a value for day in a month' % day)
    exit (2)


months = (0,31,59,90,120,151,181,212,243,273,304,334)

sum=months[month-1]

sum+=day	

leap=0

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap=1
if (leap==1) and (month>2):
    sum+=1 

print ('%s is the %s day in year %s' % (i,sum,year), end='')




