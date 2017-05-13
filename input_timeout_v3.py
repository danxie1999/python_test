import _thread,sys,os
import threading,time 
from functools import wraps
from multiprocessing import Process, Queue

def decorator_func(func):
	@wraps(func)
	def wrapper_func(*args,**kwargs):
		print("\nTime\'s Up!!!")
		return func(*args,**kwargs)
	return wrapper_func

#@decorator_func

def Interrput(timeout,q):
	time.sleep(timeout)
	PID=q.get(True)
	print (PID)
	os.kill(PID,2)



def input_with_timeout(prompt,q):
#	print (prompt)
#	timer=threading.Timer(timeout,Interrput)
	PID=os.getpid()
	q.put(PID)	
	input('prompt')


#	except KeyboardInterrupt:
#		pass

#	return astring

if __name__ == '__main__':
	q=Queue()
#	p1=Process(target=Interrput,args=(3,q))
	p2=Process(target=input_with_timeout,args=('Please input something:',q))
#	p1.start()
	p2.start()
	p2.join()
#	PID=q.get(True)
#	time.sleep(3)
#	os.kill(PID,2)