#from multiprocessing import Process
#import os

#def run_proc(name):
#	print("Run child process {} ({})".format(name,os.getpid()))

#if __name__ == '__main__':
#	print("Parent process {}.".format(os.getpid()))
#	p=Process(target=run_proc,args=('test',))
#	print('Child process will start')
#	p.start()
#	p.join()
#	print('Child process end')

from multiprocessing import Process
import time
def f():
    print('hello world!')

if __name__ == '__main__':
#    freeze_support()
    Process(target=f).start()
    time.sleep(5)