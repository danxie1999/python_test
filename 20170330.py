from multiprocessing import Process, Pool
import os
import time, random

#def run_proc(name):
#	print("run child process {}, pid is {}".format(name,os.getpid()))

#if __name__=="__main__":
#	print("Parent process is running, process id is {}".format(os.getpid()))
#	p=Process(target=run_proc,args=('Test_Dan',))
#	p2=Process(target=run_proc,args=('Test_Tony',))
#	print("Child process will run")
#	p.start()
#	p2.start()
#	p.join()
#	p2.join()
#	print('Child process end')	

def time_task(name):
	print("Run task {} ({})...".format(name,os.getpid()))
	start=time.time()
	time.sleep(random.random()*2)
	end=time.time()
	print("Task {} runs {:.2f} seconds".format(name,(end-start)))

if __name__=="__main__":
	p=Pool(5)
	for i in ['Dan','Tony','Pit','Chris','Jack']:
		p.apply_async(time_task,args=(i,))
	print('wait for all subprocesses done..')
	p.close()
	p.join()
	input('All processes done')