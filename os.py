#!/usr/bin/env python3

import os

from datetime import datetime

path=os.getcwd()

#print(os.listdir())

#os.makedirs('c:/python_test/test/DEMO')


#os.chdir('c:/python_test/test')

#print(os.listdir())

#os.rmdir('c:/python_test/test/DEMO')

#print(os.listdir())

#print (os.listdir())


#os.rename('test2.txt','test.txt')

#print (os.listdir())

#mod_time=os.stat('test.txt').st_mtime

#print (datetime.fromtimestamp(mod_time))

#for dirpath, dirnames, filenames in os.walk('c:/python_test'):
#    print ("dirpath: %s\ndirnames:%s\nfilenames:%s" % (dirpath, dirnames, filenames))


## os.environ

#print(os.environ.items())

## os.path()

#path_file=os.path.join(path,'test.txt')

#print(os.path.basename(path_file))

#print(os.path.dirname(path_file))

#print(os.path.split(path_file))

#print(os.path.exists(path_file))

#print(os.path.isdir(path_file))

print(os.path.isfile(path_file))

print(os.path.splitext(path_file))
