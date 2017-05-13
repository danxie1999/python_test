import _thread,sys
import threading,time 
from functools import wraps

def decorator_func(func):
	@wraps(func)
	def wrapper_func(*args,**kwargs):
		print("\nTime\'s Up!!!")
		return func(*args,**kwargs)
	return wrapper_func

@decorator_func

def Interrput():
	return _thread.interrupt_main()


def input_with_timeout(prompt,timeout=5):
#	print (prompt)
	timer=threading.Timer(timeout,Interrput)
	astring = None
	try:
		timer.start()
		input(prompt)

#		for i in range(10):
#			print (i)
#			time.sleep(1)
	except KeyboardInterrupt:
		pass
	timer.cancel()

	return astring


input_with_timeout('Please input something:')