#!/usr/bin/env python3

import os

DIR=os.getcwd()

DIR_2=os.path.join(DIR,"test")

os.chdir(DIR_2)

#file=open ("test.txt","r")

#read=file.readlines()

#print(read)

#for line in file:
 #   print(line)

#file.close()

## context manager

#with open ('test.txt','r') as file:
#    size_to_read=5
#    file_content=file.read(size_to_read)
#    print (file_content,end='')
##read from the 0 position
#    file.seek(0)

#    file_content=file.read(size_to_read)
#    print (file_content)

    
#    while len(file_content) >0:
#        print (file_content,end='')
#        file_content=file.read(size_to_read)


with open ('test2.txt','w') as file2:
    file2.write('test')
    file2.seek(0)
    file2.write('P ')
    wcontent=file2.write('Hello this is just a test')
    print (wcontent)
	
	
#with open ('Your Electronic Ticket Receipt_yixuan.pdf','rb') as file3:
#    with open ('Receipt_yixuan_copy.pdf','wb') as file4:
#        size_of_chunk=4096
#        file3_content=file3.read(size_of_chunk)
#        while len(file3_content) > 0:
#            file4.write(file3_content)            
#            file3_content=file3.read(size_of_chunk)
	


    
    