import hashlib,os
import pymysql,base64
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from flask import Flask,request,render_template


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

def calc_md5(PASSWORD):
	PASSWORD=PASSWORD+' The salt'
	md5=hashlib.md5()
	md5.update(PASSWORD.encode('utf-8'))
	return md5.hexdigest()


#app=Flask(__name__)

#@app.route('/',methods=['GET','POST'])

#def home():
#	return render_template('home.html')

#@app.route('/signin',methods=['GET'])

#def signin_form():
#	return render_template('form.html')


engine= create_engine('mysql+pymysql://root:{}@localhost:3306/python_test'.format(PASS))
DBSession = sessionmaker(bind=engine)
session=DBSession()
username='dAn'
user=session.query(Users).filter(Users.name==username).one()
print(user.name,user.password)
session.close()


#@app.route('/signin',methods=['POST'])

#def signin():
#	username= request.form['username']
#	password= request.form['password']
#	engine= create_engine('mysql+pymysql://root:{}@localhost:3306/python_test'.format(PASS))
#	DBSession = sessionmaker(bind=engine)
#	session=DBSession()

#	try:
#	except:
#		return render_template('new_user.html',message='Cannot find username {} in the DB'.format(username))
#		username=request.new_user['username']
#		PASSWORD=request.new_user['password']
#		PASSWORD=calc_md5(PASSWORD)
#		try:
#			new_user=Users(name=username,password=PASSWORD)
#			session.add(new_user)
#			session.commit()
#			return render_template('form.html',message='Please sign in with your new user,')
#		except:
#			pass
#		finally:
#			session.close()
#			exit()
#	finally:
#		session.close()
#	
#	PASSWORD=calc_md5(password)
#	if user.password == PASSWORD:
#		return render_template('signin-ok.html',username=username)
#	return render_template('form.html',message='Bad username or Bad password!')
#	session.close() 


#if __name__ == '__main__':
#	app.run()