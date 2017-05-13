import threading,os,time

def music(func):
	for i in range(2):
		print("I was listening to music {}. {},{}".format(func,time.ctime(),threading.current_thread()))
		time.sleep(1)

def move(func):
	for i in range(2):
		print("I was at the movies {}! {},{}".format(func,time.ctime(),threading.current_thread()))
		time.sleep(5)

threads=[]

t1= threading.Thread(target=music,args=('一生所爱',))
t2= threading.Thread(target=move,args=('大话西游',))
threads.append(t1)
threads.append(t2)

if __name__ == "__main__":
	for t in threads:
		t.setDaemon(True)
		t.start()
	t.join()
	print("Finished.{}".format(time.ctime()))
	input('END')