#!/usr/bin/env python3

import os
os.chdir('C:/python_test/test')
try:
    f=open('test.txt','r')
    if f.name == 'test.txt':
        raise NameError
    var='test'
except NameError:
    print('Name Error')
except FileNotFoundError as e:
    print(e)
else:
    print(f.read())
    f.close()

finally:
    print('print finally')
#print (f.read())
#f.close()

