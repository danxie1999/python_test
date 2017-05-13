import xml.etree.ElementTree as ET

from contextlib import contextmanager,closing

from urllib.request import urlopen



#tree=ET.ElementTree(file='xml_test3.xml')

#root=tree.getroot()

#print(root[0].text)

#print(root.tag,root.attrib)

#for i in root:
#	print ("tag:{}\nattrib:{}\ncontent:{}".format(i.tag,i.attrib,i.text

#for elem in tree.iter(tag='title'):
#	print (elem.tag,elem.attrib,elem.text)


#tree=ET.parse('xml_test3.xml')
#利用iterparse解析XML流
for event,elem in ET.iterparse('xml_test3.xml'):
	print(event,elem.tag)

