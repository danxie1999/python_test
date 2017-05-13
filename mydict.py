#!/usr/bin/env python3

class Dict(dict):
	def __init__(self,**kw):
		super(Dict,self).__init__(**kw)

	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			print("{} is not a key in the {}.".format(key,self))
	def __setattr__(self,key,value):
		self[key]=value


d=Dict(a=1,b=2)

d['c']=3
print(d.d)

