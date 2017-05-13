import time

def consumer():
	r=''
	while True:
		n= yield r
		if not n:
			return
		print('[CONSUMER] Consuming {}...'.format(n))
		r='200 OK'

def produce(c):
	c.send(None)
	n=0
	while n < 5:
		n=n+1
		print('[PRODUCER] Producing {}...'.format(n))
		r=c.send(n)
		print('[PRODUCER] Consumer return: {}'.format(r))
	c.close()

c= consumer()

produce(c)


#def test():
#	r=''
#	while True:
#		n=yield r
#		print(n)
#		r=n+1
#c=test()

#print(c.send(None))
#print(c.send(1))
#c.close()



	