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

#insert_info('Dan','123456')
#update_info('Dan','Nds')
print(select_name_pass('Dan'))