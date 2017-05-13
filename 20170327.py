#!/usr/bin/env python3

import os

#DIR=os.getcwd()


os.chdir('c:/python_test/test/')

DIR=os.getcwd()


FILE=os.path.join(DIR,'Your Electronic Ticket Receipt_yixuan.pdf')

#with open(FILE,'r') as file:
#	size_to_read=5
#	file_content=file.read(size_to_read)
#	while len(file_content) >0:
#		print(file_content,end="")
#		file_content=file.read(size_to_read)


with open(FILE,'rb') as file:
	with open ('recipt_copy.pdf','wb') as file2:
		size_of_chunk=4096
		file_content=file.read(size_of_chunk)
		while len(file_content) >0:
			file2.write(file_content)
			file_content=file.read(size_of_chunk)
#	read=file.readlines()
#	for line in read:
#		print(line,end="")
#	for line in file:
#		print (line,end='')