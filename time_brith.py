import datetime,time

#now=datetime.datetime.now()

#print(now)
#print(type(now))

#dt=datetime.datetime(2017,4,10,12,20)

#print(dt)
#print(dt.timestamp())
#t=time.time()
#print(t)
#print(datetime.datetime.utcfromtimestamp(t))
#print('')
## string converts to datetime
#STR="1986/03/10"
#T=datetime.datetime.strptime(STR,"%Y/%m/%d")
#print(T)
##datetime converts to string
#print(dt.strftime("%Y/%m/%d"))

## Calculate datetime

#now=datetime.datetime.now()

#print (now)

#print(now + datetime.timedelta(hours=20))

while True:
	STR=input("Please input your birthday(1986/10/11):")

	y=STR.split('/')[0]

	Y=datetime.datetime.now()
	Y=Y.strftime("%Y")

	STR=STR.replace(y,Y)

	BD=datetime.datetime.strptime(STR,"%Y/%m/%d")

	now=datetime.datetime.now()

	if BD < now:
		print('You birthday has passed for {}'.format(now-BD))
	else:
		print('You birthday will start in {}'.format(BD-now))
#datetime.datetim.strptime(STR,"")



