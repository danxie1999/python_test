import os

IPSTART=str(input("Please input the start ip of ip range you want to check:"))
IPEND=str(input("Please input the end ip of the ip range you want to check:"))

#IPSTART='10.146.90.1'
#IPEND='10.146.90.3'


NETWORK1=os.path.splitext(IPSTART)[0]
NETWORK2=os.path.splitext(IPEND)[0]
START=int(os.path.splitext(IPSTART)[1].strip('.'))
END=int(os.path.splitext(IPEND)[1].strip('.'))+1

IPS=[]

for i in range(START,END):
	IPS.append("{}.{}".format(NETWORK1,i))
print(IPS)
input('END')
