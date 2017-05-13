import socket,time,sys,msvcrt
from threading import Event,Timer
import threading

HOST="10.146.90.98"

PORT=12201



def readInput(caption,timeout=5):
	START=time.time()
	print("{},will close if no input in {} seconds:".format(caption,timeout),end="")
	sys.stdout.flush()
	INPUT=""
	while True:
		try:
			if msvcrt.kbhit():
				CHR=msvcrt.getche()
				CHR=CHR.decode('utf-8')
				if ord(CHR) == 13:
					break
				elif ord(CHR) >=32:
					INPUT+= CHR
		except:
			pass
		if len(INPUT) == 0 and time.time() - START >= timeout:
			break

	print('')

	if len(INPUT) > 0:
		return INPUT


def t20_handler():


	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((HOST,PORT))

#	T20=readInput("Please input T20 ")

	T20=input("Please input T20:")

#	T20="0002M004E0002024008201412292243251012SIH03E7A05DA000120150410NB224DDB02E5443E2"
	if T20:
		s.send(bytes(T20,encoding="utf-8"))
		print(s.recv(1024).decode('utf-8'))
	s.close()



while True:
	t=threading.Thread(target=t20_handler)
	t.start()
	t.join()





#while True:
#data=s.recv(2048)
#if data:
#	print (";{}".format(data.decode('utf-8')))

#s.send(bytes(T20,encoding="utf-8"))

#data=s.recv(2048)
#print(data)


#Idata=readInput("please input T20")
#if Idata:
#	s.send(bytes(Idata,encoding="utf-8"))
	
#s.close()

