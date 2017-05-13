import hashlib,os
import pymysql,base64
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from flask import Flask,request,render_template,url_for,redirect



## passowrd decode
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

## md5 encryption for the input passowrd 
def calc_md5(PASSWORD):
	PASSWORD=PASSWORD+' The salt'
	md5=hashlib.md5()
	md5.update(PASSWORD.encode('utf-8'))
	return md5.hexdigest()

## DB connection establish

def conn():
	global session
	engine= create_engine('mysql+pymysql://root:{}@localhost:3306/python_test'.format(PASS))
	DBSession = sessionmaker(bind=engine)
	session=DBSession()


## an instance of Flask class
app=Flask(__name__)

## route() decorator to tell Flask what URL should trigger our function and connect url with method.
@app.route('/',methods=['GET','POST'])

def home():
	return render_template('home.html')


## Register 

@app.route('/register/<Message>',methods=['GET','POST'])

def register(Message):
	if request.method == 'POST':
		username= request.form['username']
		password= request.form['password']
		password=calc_md5(password)
		conn()
		new_user=Users(name=username,password=password)
		try:
			session.add(new_user)
			session.commit()
		except:
			pass
		finally:
			session.close()
#		return redirect(url_for('signin'))
		return render_template('register.html',message='{} has successfully registered in the DB'.format(username))
	else:
		return render_template('new_user.html',message=Message)


@app.route('/register/success',methods=['POST'])

def register_post():
	return redirect(url_for('signin'))


## Sign in 

@app.route('/signin',methods=['GET','POST'])

def signin():

	if request.method=='POST':
		username= request.form['username']
		password= request.form['password']
		conn()
		try:
			user=session.query(Users).filter(Users.name==username).one()
		except:
			return redirect(url_for('register',Message='{} does not in DB, Pls register...'.format(username)))
		finally:
			session.close()
		PASSWORD=calc_md5(password)
		if user.password == PASSWORD:
			return render_template('signin-ok.html',username=username)
		return render_template('form.html',message='Bad username or Bad password!')
	else:
		return render_template('form.html') 


if __name__ == '__main__':
	app.run()
