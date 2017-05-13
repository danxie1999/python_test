#!/usr/bin/env python3


def get_info():
	command=input(":").split()
	if command[0] in verb_dict:
		verb=verb_dict[command[0]]
	else:
		print("{} is not a verb".format(command[0]))
		return
	if len(command) >= 2:
		noun_word=command[1]
		print(verb(noun_word))
	else:
		print(verb("nothing"))


class GameObject:
	class_name=""
	desc=""
	objects={}

	def __init__(self,name):
		self.name=name
		GameObject.objects[self.class_name]=self
	@property
	def desc(self):
		if self.health >=3:
			return self._desc
		elif self.health == 2:
			health_line="It has a wound on its knee."
		elif self.health == 1:
			health_line="It is dying."
		elif self.health <= 0:
			health_line="It is died."
		return "{}: {}".format(self.class_name,health_line)
	@desc.setter
	def desc(self,value):
		self._desc = value
	@classmethod
	def set_health(cls,value):
		cls.health=value

	def get_desc(self):
		return "{}\n{}".format(self.name,self.desc)

class Goblin(GameObject):
	health=3
	def __init__(self,name):
		self.class_name="goblin"
		self._desc="A foul creature"
		super(Goblin,self).__init__(name)

class Human(GameObject):
	health=3
	def __init__(self,name):
		self.class_name="human"
		self._desc="An advanced animal."
		super(Human,self).__init__(name)


class Something(GameObject):
	health=3
	def __init__(self,name):
		self.class_name="something"
		self._desc="You can examine each of them."
		super(Something,self).__init__(name)

goblin=Goblin("Gobbly")

human=Human("Human")

something=Something("found a goblin and an human hiding in the forest.")

#print(something.objects)

#print (goblin.objects)

def examine(noun):
	if noun in GameObject.objects:
		return GameObject.objects[noun].get_desc()
	else:
		return "There is no {} here.".format(noun)

def say(noun):
	return ("You said {}".format(noun))

def hit(noun):
	if noun in GameObject.objects:
		thing=GameObject.objects[noun]
#		assert thing != something, 'something is not valid'
		if thing != something:
			thing.health-=1
			if thing.health <=0:
				msg="You killed the creature."
			else:
				msg="You hit {}".format(thing.class_name)
		else:
			msg="there are a goblin and an human near you."
	else:
		msg="There is no {} here.".format(noun)
	return msg  

verb_dict={"say":say,"examine":examine,"hit":hit}

print ("Welcome to the VM world.")

while True:
	get_info()
