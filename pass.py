import hashlib,os

os.chdir('C:\python_test')
DIR=os.getcwd()
FILE=os.path.join(DIR,'pass.txt')

db={}


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
	

def register(username,password):
	db[username]=calc_md5(password)


def login(username,password):
	if db[username] == password:
		return "Welcome {}!".format(username)
	else:
		return "Bad password!"


if __name__=="__main__":
	username=input('Please input your username:')
#	password=input('Please input your password:')
#	username='Jian'
	load_db()
	if username not in db:
		password=input('Please input your new password:')
#		password='12345678'
		password=calc_md5(password)
		with open(FILE,'a') as file:
			file.write("\n{},{}".format(username,password))
		input('Please relogin with your new password,')
		exit()
	password=input('Please input your password:')

	password=calc_md5(password)
#	print(password)
#	print(db)
	print(login(username,password))
	input('')

