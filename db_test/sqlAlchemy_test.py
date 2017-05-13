from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import base64
##change relational DB into object (ORM: Object-Relational Mapping)

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

## initiate DB connection
#'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine= create_engine('mysql+pymysql://root:{}@localhost:3306/python_test'.format(PASS))

#create DBsession

DBSession = sessionmaker(bind=engine)

#session= DBSession()

# create an object of the class User
#new_user=Users(name='Mike',password='Nds')

#add to session
#session.add(new_user)

#session.commit()

#session.close()


## query 

session=DBSession()
## 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:


try:
	user=session.query(Users).filter(Users.name=='M').one()
except:
	print('1')
	print('2')
	try:
		print(0/0)
	except:
		print('end')

#	print(user.one())


#.one()

#print('type:',type(user))
#print('Name:',user.name,user.password)

session.close()


