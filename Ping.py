from multiprocessing import Pool
import subprocess, time


def Ping(nu):
	try:
		child=subprocess.check_output("{} {}".format("ping -n 1",nu),shell=True,universal_newlines=True)
		if child.find('unreachable') >0:
			return "{} Destination unreachable".format(nu)
		else:
			child1=subprocess.Popen("{} {}".format("nbtstat -a",nu),shell=True,stdout=subprocess.PIPE)

			child2=subprocess.Popen("find /i \"Registered\"",shell=True,universal_newlines=True, stdin=child1.stdout,stdout=subprocess.PIPE)
			out=child2.communicate()[0]
			return "{} UP\n{}".format(nu,out)
#			return "{} UP".format(nu)
	except subprocess.CalledProcessError:
		pass
#	print("Run task {}({})".format(name,os.getpid()))
#	start=time.time()
#	time.sleep(random.random()*3)
#	end=time.time()
#	print("Task {} rans {:.02f} seconds".format(name,(end-start)))


if __name__=="__main__":
	while True:
		L=[]
		p=Pool(10)
		NETWORK=str(input("请输入网段:"))
		start=time.time()
#		NETWORK="10.146.90"
		for i in range(1,20):
			nu="{}.{}".format(NETWORK, i)
			L.append(p.apply_async(Ping,args=(nu,)))
		p.close()
		p.join()
		for i in L:
			if i.get() is not None:
				print(i.get())
		end=time.time()
		print("time: {:.02f}".format(end-start))
