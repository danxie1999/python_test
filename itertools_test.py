import itertools

natuals=itertools.count(1)



#def proc(x):
#	if x <=15:
#		return x

#ns = itertools.takewhile(proc, natuals)

#print(list(ns))

#for i in natuals:
#	print(i)

for key, group in itertools.groupby('AaABCcCABCabc',lambda c: c.upper()):
	print(key,list(group))