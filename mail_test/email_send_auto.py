from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import base64,smtplib

def _format_addr(s):
	name,addr=parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))


def send_email(arg,LOG,content_email):

	#from_addr=input('From:')
	from_addr="xiedan1999@163.com"
	#from_addr="570619058@qq.com"
	#password=input('Password:')
	#password="jphkyiiqgqhdbffa"
	STRQQ=b'anBoa3lpaXFncWhkYmZmYQ==\n'
	STR163=b'd2FuZ3hpYTM0NjExOTE=\n'
	password=base64.decodestring(STR163).decode('utf-8')
	#to_addr=input('To:')
	#to_addr="570619058@qq.com"
	to_addr="danxie@cisco.com"
	#to_addr="xiedan1999@163.com"
	#smtp_server=input('SMTP server:')
	smtp_server="smtp.163.com"
#	smtp_server="123.125.50.149"
#	smtp_server='smtp.qq.com'
	recv_name=to_addr.split('@')[0]

	#object of the email
	#msg=MIMEText('Hello, this is just a text...','plain','utf-8')
	msg=MIMEText("{}\n\n{}\n\n{}".format(arg,LOG,content_email),'plain','utf-8')
	#msg=MIMEMultipart()
	#msg=MIMEText("Hello, this is a test for python...",'plain','utf-8')
	msg['From']=_format_addr('Python_prompt <{}>'.format(from_addr))
	msg['To']=_format_addr('{} <{}>'.format(recv_name,to_addr))
	msg['Subject']=Header('a prompt from the {}'.format(smtp_server),'utf-8').encode()


	# The content of the email
	#msg.attach(MIMEText('<html><body><h1>Hello again</h1>'+'<p><img src="cid:0"></p>'+'</body></html>','html','utf-8'))


	#add an MIMEBase

	#with open('c:\python_test\code.jpg','rb') as f:
	#
	#	mime=MIMEBase('image','jpg',filename='test.jpg')
		#add header
	#	mime.add_header('Content-Disposition','attachment',filename='test.jpg')
	#	mime.add_header('Content-ID','<0>')
	#	mime.add_header('X-Attachment-Id','0')
		#load attachment content
	#	mime.set_payload(f.read())
		#encode with Base64
	#	encoders.encode_base64(mime)
	#	msg.attach(mime)


	server=smtplib.SMTP_SSL(smtp_server,465)
	#server.set_debuglevel(1)
	#server.login(from_addr,password)
	server.login(from_addr,password)
	server.sendmail(from_addr,[to_addr],msg.as_string())
	print('Sent email from {} to {}...'.format(from_addr,to_addr))
	server.quit()	