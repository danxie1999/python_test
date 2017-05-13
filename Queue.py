from multiprocessing import Process,Queue,Pool
import time, os, random


def write(q):
	for value in ['A','B','C']:
		print("put {} to queue".format(value))
		q.put(value)
		time.sleep(random.random())

def read(q):
	while True:
		if not q.empty():
			value=q.get(True)
			print("Get {} from queue".format(value))
			time.sleep(random.random())
		else:
			break

if __name__ == "__main__":
	q=Queue()
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))
	pw.start()
	pw.join()
	pr.start()
	pr.join()
	print("all process done")
