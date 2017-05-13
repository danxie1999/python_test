#!/usr/bin/python
import socket
import os,sys
#msg=sys.argv[1]
msg="0003M004A000203006420130410173154D652SIH034DC3EEV-ab0001703E3646642A2E86F8"

HOST = '10.146.90.98'    # The remote host
PORT = 12202             # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
#print("the send T20 is: ")
print(msg)
# msg=raw_input("input the T20:\n")
#msg=('0003M00440002024008201504101209091234SIN1DD17977YA9739473BBC748DE15B').strip()
s.sendall(bytes(msg,encoding='utf-8'))
data = s.recv(4096)
#print 'below is the response:'
print (';'+data.decode('utf-8'))
s.close()
