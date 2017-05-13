import cx_Oracle
db=cx_Oracle.connect('supervis/SuperviS123!@10.146.90.98/EMMG')

cr=db.cursor()
sql='select * from CARD where cardid = 61397134'
cr.execute(sql)
#rs=cr.fetchall()
rs=cr.fetchone()
#print("print all: {}".format(rs))

for x in rs:
	if type(x) is not bytes and x is not None:
		print(x)

cr.close()
db.close()