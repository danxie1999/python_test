import hashlib,os
import pymysql,base64


PASS=b'TmRzMTIzNDU2\n'

PASS=base64.decodestring(PASS).decode('utf-8')



def insert_info(NAME,PASSWORD):

	conn=pymysql.connect(user='root',password=PASS,database='python_test')

	cursor=conn.cursor()

	try:
		cursor.execute('insert into users values (%s,%s)', [NAME,PASSWORD])
		conn.commit()
	except:
		pass
	finally:
		cursor.close()
		conn.close()

def select_name_pass(NAME):
	conn=pymysql.connect(user='root',password=PASS,database='python_test')
	cursor=conn.cursor()

	try:
		cursor.execute('select * from users where name = %s',[NAME])
		values=cursor.fetchall()
		return values[0][-1]
	except:
		pass
	finally:
		cursor.close()
		conn.close()


def update_info(NAME,PASSWORD):
	conn=pymysql.connect(user='root',password=PASS,database='python_test')
	cursor=conn.cursor()

	try:
		cursor.execute('update users set password=%s where name=%s',[PASSWORD,NAME])
		conn.commit()
	except:
		pass
	finally:
		cursor.close()
		conn.close()

def load_db():
	with open(FILE,'r') as file:
		for line in file.readlines():
			line=line.strip('\n')
			db[line.split(',')[0]]=line.split(',')[-1]

def calc_md5(password):
	password=password+' The salt'
	md5=hashlib.md5()
	md5.update(password.encode('utf-8'))
	return md5.hexdigest()


def login(username,password):
	if select_name_pass(username) == password:
		return "Welcome {}!".format(username)
	else:
		return "Bad password!"


if __name__=="__main__":
	username=input('Please input your username:')
#	password=input('Please input your password:')
#	username='Jian'
#	load_db()
	if not select_name_pass(username):
#	if username not in db:
		password=input('Please input your new password:')
#		password='12345678'
		password=calc_md5(password)
		insert_info(username,password)


#		with open(FILE,'a') as file:
#			file.write("\n{},{}".format(username,password))
		input('Please relogin with your new password,')
		exit()
	password=input('Please input your password:')
#	password='12345678'
	password=calc_md5(password)
#	print(password)
#	print(db)
	print(login(username,password))
	input('')

