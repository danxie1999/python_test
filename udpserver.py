import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("127.0.0.1",9999))

print ("Bind UDP on port 9999...")

while True:
	data,addr=s.recvfrom(1024)
	print("Recieve data from {}:{}".format(addr[0],addr[1]))
	STR="Hello,{}".format(data.decode('utf-8'))
	s.sendto(bytes(STR,encoding='utf-8'),addr)