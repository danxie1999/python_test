import os

os.chdir('C:\python_test')
DIR=os.getcwd()
FILE=os.path.join(DIR,'pass.txt')

with open(FILE,'a') as file:
	file.write('Hello\n')
