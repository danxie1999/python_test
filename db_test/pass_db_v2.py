import hashlib,os
import pymysql,base64
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

PASS=b'TmRzMTIzNDU2\n'

PASS=base64.decodestring(PASS).decode('utf-8')


# create base class

Base=declarative_base()


class Users(Base):
	#table name
	__tablename__='users'
	# the structure of the table
	name = Column(String(255),primary_key=True)
	password = Column(String(255))


def conn():
	global session
	engine= create_engine('mysql+pymysql://root:{}@localhost:3306/python_test'.format(PASS))
	DBSession = sessionmaker(bind=engine)
	session=DBSession()

def query_db(username,PASSWORD):
	user=session.query(Users).filter(Users.name==username).one()

	if user.password == PASSWORD:
		return "Welcome {}!".format(username)
	else:
		return "Bad password!"


def calc_md5(PASSWORD):
	PASSWORD=PASSWORD+' The salt'
	md5=hashlib.md5()
	md5.update(PASSWORD.encode('utf-8'))
	return md5.hexdigest()


if __name__=="__main__":
	username=input('Please input your username:')
#	password=input('Please input your password:')
#	username='Shawn'
#	load_db()
	conn()
	try:
		user=session.query(Users).filter(Users.name==username).one()
	except:
		PASSWORD=input('Please input your new password:')
		#PASSWORD='12345678'
		PASSWORD=calc_md5(PASSWORD)
		try:
			new_user=Users(name=username,password=PASSWORD)
			session.add(new_user)
			session.commit()
			input('Please try to login with your new password...')
		except:
			pass
		finally:
			session.close()
			exit()	
	PASSWORD=input('Please input your password:')
#	PASSWORD='12345678'
	PASSWORD=calc_md5(PASSWORD)
#	print(password)
#	print(db)
	conn()
	try:
		print(query_db(username,PASSWORD))
	except:
		pass
	finally:
		session.close()

