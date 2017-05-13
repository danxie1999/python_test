class SpamException(Exception):
	pass

def writer():
	while True:
		try:
			w= yield
		except SpamException:
			print('***')
		else:
			print('>> ',w)

w= writer()

wrap= writer_wrapper(w)

wrap.send(None)

for i in [0,1,2,'spam',4]:
	if i =='spam':
		wrap.throw(SpamException)
	else:
		wrap.send(i)



