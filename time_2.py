#!/usr/bin/env python3

import datetime

import pytz
##naive daytime

#dt=datetime.datetime(2017,3,12,18,2,31,100000)

#dt_now=datetime.datetime.now()

#print(dt_now.date())

tday= datetime.date.today()

tdelta=datetime.timedelta(days=7)

#print (tday)

#print(tdelta)

date2=tday + tdelta

#print(date2)

#print(date2 - tday)


bday= datetime.date(2017,11,19)

till_bday= bday - tday

print (till_bday)

##Timezoneaware daytime

#China_tz=pytz.timezone('Asia/Hong_Kong')

#dt_now=China_tz.localize(dt_now)

#dt_utc=dt_now.astimezone(pytz.timezone('UTC'))

#print(dt_utc)

#dt_utcnow=datetime.datetime.now(tz=pytz.UTC)

#dt=datetime.datetime(2017,3,12,18,7,31,tzinfo=pytz.UTC)
#print(dt)

#for i in pytz.all_timezones:
#    print (i)

#dt_China= dt_utcnow.astimezone(pytz.timezone('Asia/Hong_Kong'))
#print(dt_China)

dt_China=datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong'))

# convert datetime to string
#print(dt_China.strftime('%B %d %Y'))


# convert string to datetime
dt_str='2007/03/11'
dt=datetime.datetime.strptime(dt_str,'%Y/%m/%d')
#print(dt)

