import os, sqlite3

#' 返回指定分数区间的名字，按分数从低到高排序 '

db_file=os.path.join('C:\python_test\db_test','test.db')

if os.path.isfile(db_file):
	os.remove(db_file)

conn=sqlite3.connect(db_file)
cursor=conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001','Adam',95)")
cursor.execute(r"insert into user values ('A-002','Bart',62)")
cursor.execute(r"insert into user values ('A-003','Dan',79)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low,high):
	conn=sqlite3.connect(db_file)
	cursor=conn.cursor()
	L=[]
	L1=[]
	try:
		cursor.execute('select * from user')
		values=cursor.fetchall()
		for usr in values:
			if low <= usr[-1] <= high:
				L.append(usr)
		if L:
			L=sorted(L,key=lambda nu: nu[-1])
			for data in L:
				L1.append(data[1])
		if L1:
			print(L1)


	except:
		pass
	finally:
		cursor.close()
		conn.close()

get_score_in(70,99)
