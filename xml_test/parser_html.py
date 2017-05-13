# - * - coding: utf-8 - * -
from html.parser import HTMLParser

from html.entities import name2codepoint


class MyHTMLParser(HTMLParser):
	def __init__(self):
		super(MyHTMLParser,self).__init__()
		self.li=False
		self.h3=False
		self.a=False
		self.p=False
		self.time=False
		self.span1=False
		self.span2=False
		self.event_dict={}
		self.count=0

	def handle_starttag(self,tag,attrs):
		if tag == 'li':
			self.li=True
		elif tag == 'h3':
			for k, v in attrs:
				if k=='class' and v == 'event-title':
					self.h3=True
		elif tag == 'a':
			self.a=True
		elif tag == 'p':
			self.p=True
		elif tag == 'time':
			self.time = True
		elif tag == 'span':
			for k, v in attrs:
				if k == 'class' and v == 'say-no-more':
					self.span1 = True
				elif k == 'class' and v == 'event-location':
					self.span2= True

	def handle_data(self,data):
		if self.li:
			if self.h3==True and self.a == True:
				self.count+= 1
				self.event_dict[self.count] = {}
				self.event_dict[self.count]['name'] = data
			elif self.p:
				if self.time:
					if not self.span1:
						self.event_dict[self.count]['time'] = data
#					else:
#						self.event_dict[self.count]['time']+ = (',' + data)
				else:
					if self.span2:
						self.event_dict[self.count]['site'] = data
	def handle_endtag(self,tag):
		if tag == 'a':
			self.a = False
		elif tag == 'h3':
			self.h3 = False
		elif tag == 'span':
			self.span1 = False
			self.span2 = False
		elif tag == 'time':
			self.time = False
		elif tag == 'li':
			self.li = False

parser = MyHTMLParser()

def parse_python_event(html_data):
	global parser
	parser = MyHTMLParser()
	parser.feed(html_data)
	return parser.event_dict

if __name__ == '__main__':
	with open('test.html','rb') as f:
		html_data=f.read()		
		#解决乱码
		html_data=html_data.decode('utf-8')
	event= parse_python_event(html_data)
	print("{}".format(event))
	for i in range(1,parser.count+1):
		print("{}\n{}\t{}".format(event[i]['name'],event[i]['time'],event[i]['site']))



