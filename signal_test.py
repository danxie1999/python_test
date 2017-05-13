from threading import Timer,Event
import time


def handler():
	print("will close in seconds")
	e.set()

t= Timer(3,handler)

e=Event()

t.start()

while not e.isSet():
	print("Hello")
	time.sleep(0.5)