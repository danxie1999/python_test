import threading

global_dict= {}

def std_thread(score):
	global_dict[threading.current_thread().name] = score
	do_task_1()
	do_task_2()

def do_task_1():
	print("my name is {} and my score is {}".format(threading.current_thread().name,global_dict[threading.current_thread().name]) )

def do_task_2():
	print(global_dict)


t1=threading.Thread(target=std_thread,args=(98,),name="Dan")
t2=threading.Thread(target=std_thread,args=(89,),name="Tony")

t1.start()
t2.start()
t1.join()
t2.join()





