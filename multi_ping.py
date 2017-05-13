#!/usr/bin/env python3
from multiprocessing import Pool
import subprocess, os

DIR=os.getcwd()



def Ping(nu,P):
	try:
		subprocess.check_call("{} {}".format('ping -n 1',nu),shell=True,stdout=subprocess.PIPE)
	except subprocess.CalledProcessError:
		L.append('OK')
		print(L)

if __name__=="__main__":
#	while True:
#		NETWORK=str(input("Please input a network you want to check:"))
	NETWORK="10.146.90"
	L=[]
	p=Pool(4)
	for i in range(1,5):
		nu="{}.{}".format(NETWORK,i)
		p.apply_async(Ping,args=(nu,L))
	p.close()
	p.join()
	
			

#	print(LIST)
#	sorted(LIST)
#	for i in LIST:
#		print(i)








