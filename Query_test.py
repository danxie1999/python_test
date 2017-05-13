from contextlib import contextmanager, closing

#from string import *
from urllib.request import urlopen


urlopen('https://www.baidu.com')

#class Query():
#	def __init__(self,name):
#		self.name=name

#	def __enter__(self):
#		print('Begin')
#		return self

#	def __exit__(self, exc_type,exc_value,traceback):
#		if exc_type:
#			print('Error')
#		else:
#			print('End')

#	def query(self):
#		print("Query info about {}".format(self.name))


#with Query('Bob') as q:
#	q.query()


## contextmanager for adding context for the code

#class Query():

#	def __init__(self,name):
#		self.name=name

#	def query(self):
#		print("Query info about {}".format(self.name))


#@contextmanager

#def add_context(name):
#	print('Begin')
#	q=Query(name)
#	yield q
#	print('End')

#with add_context('Bob') as p:
#	p.query()


## contextmanager for adding fixed context for the code


#@contextmanager

#def fix_context(var):
#	print("<{}>".format(var))
#	yield
#	print("<\{}>".format(var))

#with fix_context('h'):
#	print("This is a test")
print('OK')
#print(urlopen('https://www.baidu.com'))

#input('')

#with closing(urlopen('https://baidu.com')) as page:
#	for line in page:
#		print(line)