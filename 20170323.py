## __iter__ is a method which can make a cycle

class iter:
	def __init__(self):
		self.a=1
	def __iter__(self):
		return self
	def __next__(self):
		self.a+=1
		if self.a>10:
			raise StopIteration()
		return self.a

#for n in iter():
#	print(n)

## __getitem__ is a method which can get a return in arbitrary cycle 

class iter_2:
	def __getitem__(self,n):
		a=1
		for x in range(n):
			a+=1
		return a

#print(iter_2()[2])

## __getattr__ is a method which can return an attribute

class test:
	def __init__(self,path=''):
		self._path=path
	def __getattr__(self,path):
		return test("{}/{}".format(self._path,path))
	def __repr__(self):
		return self._path
#	__repr__=__str__
#print(test().hello.again.list)

from enum import Enum

class weekday(Enum):
	sun=0
	mon=1
	tue=2
	wed=3
	ths=4
	fri=5
	sat=6


print(weekday['sun'])




