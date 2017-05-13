import threading,socket,time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',8888))

s.listen(5)
print('Waiting for connection...')

def tcplink(sock,addr):
	print('Accept new connection from {}...'.format(addr))
	sock.send(b'welcome')
	while True:
		data=sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		STR="Hello, {}".format(data.decode('utf-8'))
		sock.send(bytes(STR,encoding='utf-8'))
	sock.close()
	print('Connection closed for {}'.format(addr))

while True:
	sock,addr=s.accept()
	t=threading.Thread(target=tcplink,args=(sock,addr))
	t.start()
