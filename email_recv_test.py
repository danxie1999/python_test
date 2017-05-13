import poplib,base64,os
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr



def print_info(msg,indent=0):
	if indent == 0:
		for header in ['From','To','Subject']:
			value=msg.get(header,'')
			if value:
				if header == 'Subject':
					value=decode_str(value)
				else:
					hdr,addr=parseaddr(value)
					name=decode_str(hdr)
					value="{} <{}>".format(name,addr)
			print("{}{}:{}".format(' '* indent,header,value))
	if (msg.is_multipart()):
		parts=msg.get_payload()
		for n,part in enumerate(parts):
			print("{}part{}".format(' ' * indent,n))
			print("{}----------------".format(" " * indent))
			print_info(part,indent+1)
	else:
		content_type=msg.get_content_type()
		if content_type=="text/plain" or content_type=="text/html":
			content= msg.get_payload(decode=True)
			charset= guess_charset(msg)
			if charset:
				content=content.decode(charset)
			print("{}Text:{}".format(' ' * indent,content +'...'))
		else:
			print("{}Attachment:{}".format(' '* indent, content_type))

def decode_str(s):
	value,charset=decode_header(s)[0]
	if charset:
		value=value.decode(charset)
	return value

def guess_charset(msg):
	charset= msg.get_charset()
	if charset is None:
		content_type=msg.get('Content-Type','').lower()
		pos=content_type.find('charset=')
		if pos >=0:
			charset = content_type[pos+8:].strip()
	return charset

def last_line(inputfile):
	filesize=os.path.getsize(inputfile)
	blocksize=1024
	if filesize > blocksize:
		seekpoint=(filesize // blocksize)
	with open(inputfile,'r') as f:
		if filesize > blocksize:
			seekpoint= (filesize //  blocksize)
			f.seek=((seekpoint -1) * blocksize)
		else:
			f.seek(0,0)
		lines=f.readlines()
		if lines:
			lastline=lines[-1].strip()
			return lastline

#print(decode_str(value))


#print(decode_header(value))

#print(parseaddr(value))
if __name__ == '__main__':
	#email= input('Email:')
	#email="570619058@qq.com"
	email="xiedan1999@163.com"
	#password=input('Password:')
	STRQQ=b'anBoa3lpaXFncWhkYmZmYQ==\n'
	STR163=b'd2FuZ3hpYTM0NjExOTE=\n'
	password=base64.decodestring(STR163).decode('utf-8')
	#password="jphkyiiqgqhdbffa"
	#pop3_server=input('POP3 server:')
	#pop3_server="pop.qq.com"
	pop3_server="pop.163.com"
	##connect to POP3 server
	server=poplib.POP3_SSL(pop3_server,'995')
	#enable debug info
	#server.set_debuglevel(1)
	#welcome banner
	print(server.getwelcome().decode('utf-8'))

	# identity authorization
	server.user(email)
	server.pass_(password)

	# stat() returns the number of the emails and size of the emails
	print("Messages:{}. Size:{}".format(server.stat()[0],server.stat()[1]))


	Mnu=server.stat()[0]
	#list() returns all the serial number of the emails
	resp,mails,octets=server.list()
#	print(mails)
	resp,lines,octets = server.retr(2282)
	#print(lines)
	msg_content=b'\r\n'.join(lines).decode('utf-8')
	print(msg_content)
	msg=Parser().parsestr(msg_content)
#	print(msg)
	print_info(msg)
	server.quit()


	#OMnu=int(last_line('mail_count.txt'))
	#if Mnu > OMnu:
	#	New_Mnu=Mnu - OMnu
	#	print("You have {} new mails".format(New_Mnu))
	#	index_end=len(mails)
	#	index_start=index_end - New_Mnu + 1
	#	for index in range(index_start,index_end+1):
	#		resp,lines,octets = server.retr(index)
			## lines stores every line of the orginal email text
	#		msg_content=b'\r\n'.join(lines).decode('utf-8')
			##parse the email
	#		msg=Parser().parsestr(msg_content)
	#		print_info(msg)
	#	server.quit()
	#	with open('mail_count.txt','a') as f:
	#		f.write("\n{}".format(Mnu))
	#elif Mnu == OMnu:
	#	print("No new mail found on {}".format(pop3_server))
	#else:
	#	print("{} mails were removed on {}".format(OMnu-Mnu,pop3_server))
	#	with open('mail_count.txt','a') as f:
	#		f.write("\n{}".format(Mnu))




















