import json

class STUDENT:
	def __init__(self,name,age,score):
		self.name=name
		self.score=score
		self.age=age

std_1=STUDENT('Jack',18,98)


##Make an instance to dict and then change the dict to the json file.
J=json.dumps(std_1,default=lambda obj: obj.__dict__)

print(J)

def jsontoinstance(J):
	return STUDENT(J['name'],J['age'],J['score'])

#change the json file to dict file and then change it to class instance format 
C=json.loads(J,object_hook=jsontoinstance)

print(C.name)