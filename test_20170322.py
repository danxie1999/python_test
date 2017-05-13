class student:
##__slots__ is a class varible which is to control atrributes of the class
	__slots__=('first','__name','__score','gender','age')
	def __init__(self,name,score):
		self.__score=score
		self.__name=name
		self.gender='male'

#	def __str__(self):
#		return "class student's object: {}".format(self.__name)

	def __repr__(self):
		return "student({},{})".format(self.__name,self.__score)

	def get_name(self):
		return self.__name


std_1=student('Dan',90)

print(std_1._student__name)

#print(type(std_1))

#if type(std_1) == student:
#	print('OK')

#print(dir(std_1))

#print(hasattr(std_1,'_student__name'))

#setattr(std_1,'x',9)

#print(std_1.x)

#print(hasattr(std_1,'get_name'))

#fn=getattr(std_1,'get_name')

#print (fn())

#std_1.age=31

#print(std_1.age)

## added a method to a class
#def set_age(self,age):
#	self.age=age

#student.set_age=set_age

#std_1.set_age(30)

std_1