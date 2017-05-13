import time,sys,queue,platform
from multiprocessing.managers import BaseManager

SYS=[]

for i in platform.uname():
	SYS.append(i)


class QueueManager(BaseManager):
	pass
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#server_addr='127.0.0.1'
server_addr='10.146.90.33'

print('Connect to server{}.'.format(server_addr))

m=QueueManager(address=(server_addr,5000),authkey=b'abc')

m.connect()

task=m.get_task_queue()
result=m.get_result_queue()

for i in SYS:
#for i in range(10):
	try:
		n=task.get(timeout=1)
		print(n)
#		print("processing {}".format(n))
#		r="{}*{}={}".format(n,n,n*n)
		time.sleep(1)
		result.put(i)
	except queue.Empty:
		print('task queue is empty.')
print('worker exit')
input('END')