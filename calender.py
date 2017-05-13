#!/usr/bin/env

year,month,day=input('Please input the date, ex. 2016/12/25:').strip().split('/')

try:
    month=int(month)
except ValueError:
    print('%s is not a number' % month)

try:
    day=int(day)
except ValueError:
    print('%s is not a number' % day)
	
try:
    year=int(year)
except ValueError:
    print('%s is not a number' % year)

months = (0,31,59,90,120,151,181,212,243,273,304,334)

if 0 < month < 13:
    sum=months[month-1]
else:
    print('%s is not a number for month' % month)
    exit(1)

sum+=day

leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap=1
if (leap == 1) and (month > 2):
    sum+=1

print('%d/%d/%d is the %sth day for year %d' % (year,month,day,sum,year))
