from multiprocessing import Pool
import threading, queue,os
import subprocess, time

in_queue=queue.Queue()
out_queue=queue.Queue()

def PING(iq,oq):
	while True:
		try:
			ip=iq.get(block=False)
		except queue.Empty:
			break
		try:
			child=subprocess.check_output("{} {}".format("ping -n 1",ip),shell=True,universal_newlines=True)
			if child.find('unreachable') >0:
				pass
			else:
				child1=subprocess.Popen("{} {}".format("nbtstat -a",ip),shell=True,stdout=subprocess.PIPE)
				child2=subprocess.Popen("find /i \"Registered\"",shell=True,universal_newlines=True, stdin=child1.stdout,stdout=subprocess.PIPE)
				out=child2.communicate()[0]
				oq.put("{} UP\n{}".format(ip,out))
		except subprocess.CalledProcessError:
			pass
		iq.task_done()

#	print("Run task {}({})".format(name,os.getpid()))
#	start=time.time()
#	time.sleep(random.random()*3)
#	end=time.time()
#	print("Task {} rans {:.02f} seconds".format(name,(end-start)))


if __name__=="__main__":
	while True:
		L=[]
		IPSTART=str(input("Please input the start ip of ip range you want to check:"))
		IPEND=str(input("Please input the end ip of the ip range you want to check:"))

#	IPSTART='10.146.90.33'
#	IPEND='10.146.90.40'

		start=time.time()
		NETWORK1=os.path.splitext(IPSTART)[0]
		NETWORK2=os.path.splitext(IPEND)[0]
		if NETWORK1 != NETWORK2:
			input('{} and {} must have same network ip!!!'.format(IPSTART,IPEND))
			exit()
		START=int(os.path.splitext(IPSTART)[1].strip('.'))
		END=int(os.path.splitext(IPEND)[1].strip('.'))+1
		if START+1 > END:
			input("{} must be greater than {}".format(IPEND,IPSTART))
			exit()
		IPS=[]

		for i in range(START,END):
			IPS.append("{}.{}".format(NETWORK1,i))

		for ip in IPS:
			in_queue.put(ip)

		for i in range(30):
			t=threading.Thread(target=PING,args=(in_queue,out_queue))
			t.setDaemon(True)
			t.start()
		in_queue.join()
#	out_queue.join()
		t.join()

#	L.append(out_queue.get())
#	print(L)
#	print(out_queue.empty())

		while not out_queue.empty():
			L.append(out_queue.get())

		L=sorted(L,key=lambda nu: int(nu.split()[0].split('.')[-1]))

		for i in L:
			print(i)
		end=time.time()
		print("time: {:.02f}".format(end-start))
#	input('END')
