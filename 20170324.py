import logging
import os
path=os.getcwd()
logging.basicConfig(level=logging.INFO,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',  
                    filename=os.path.join(path,'test.log'),  
                    filemode='w') 

s = '0'
n = int(s)
assert n!=0,'n cannot be 0'
logging.info('info message')
print(10 / n)