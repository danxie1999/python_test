from urllib.request import urlopen

import urllib.request

url="https://www.python.org/events/python-events/"

FILE='test.html'

resp=urlopen(url).read().decode('utf-8')

with open (FILE,'w',encoding='utf-8') as file:
	file.write(resp)
 
#import xml.etree.ElementTree as ET

#print(FILE)

#tree=ET.ElementTree(file=FILE)
#for Elem in tree.iter():
#	print(Elem.tag)