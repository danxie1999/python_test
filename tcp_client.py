import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',8888))

#s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com\r\nConnection: close\r\n\r\n')


print(s.recv(1024).decode('utf-8'))

for data in [b'Dan',b'Tony',b'Tracy']:
	s.send(data)
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')

s.close()
