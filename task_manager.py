import random, time, queue,platform
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager

SYS=[]

for i in platform.uname():
	SYS.append(i)

task_queue=queue.Queue()

result_queue=queue.Queue()

def return_task_queue():
    global task_queue
    return task_queue
def return_result_queue():
    global result_queue
    return result_queue


class QueueManager(BaseManager):
	pass


def test():

	QueueManager.register('get_task_queue',callable=return_task_queue)
	QueueManager.register('get_result_queue', callable=return_result_queue)

	manager= QueueManager(address=('10.146.90.77',5000),authkey=b'abc')

	manager.start()

	task=manager.get_task_queue()
	result=manager.get_result_queue()

	#for i in range(10):
	#	n=random.randint(0,10000)
	#	print("Put task {}...".format(n))
	
	for n in SYS:
		task.put(n)

	print('Try get result...')

	for i in range(10):
		try:
			r=result.get(timeout=10)
			print("Result:{}".format(r))
		except queue.Empty:
			break

	manager.shutdown()

	print('master exit')
	input('END')

if __name__ == '__main__':
	freeze_support()
	test()
