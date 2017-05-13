import csv,os,xlsxwriter,time

def convert_xlsx(nu):
	global DIR2
	global L1
	global L2
	if nu == 'A':
		L=L1
	else:
		L=L2
	global OUTPUT
	workbook= xlsxwriter.Workbook(OUTPUT)

	for i in L:
		row=0
		col=0
		NAME=i.split('.')[0]
		FILE=os.path.join(DIR2,i)
		worksheet=workbook.add_worksheet(NAME)
		with open (FILE,'r') as F:
			reader=csv.reader(F)
			for time,card,status in reader:
				worksheet.write(row,col,time)
				worksheet.write(row,col+1,card)
				worksheet.write(row,col+2,status)
				row+=1

	workbook.close()


		
if __name__=="__main__":
	DIR1=os.getcwd()
	DIR2=os.path.join(DIR1,'data')
	if os.path.exists(DIR2):
		pass
	else:
		input('Cannot find data folder!!!')
		exit()
	L1=[]
	L2=[]
	os.chdir(DIR2)
	FILES=os.listdir()
	if FILES == []:
		input('Cannot find any data in {} !'.format(DIR2))
		time.sleep(5)
		exit()
	for F in FILES:
		if F.find('dulcard') == -1:
			L1.append(F)
		else:
			L2.append(F)
	S=L1[0]
	NAME=[s for s in S.replace('.','_').split('_') if s.isdigit()][0][:6]
	OUTPUT="{}\\Unicom_message_{}.xlsx".format(DIR1,NAME)
	convert_xlsx('A')
	if L2 == []:
		print('Did NOT find any data for duplicated Messages in {} !'.format(DIR2))
	else:
		OUTPUT="{}\\Unicom_message_duplicated_{}.xlsx".format(DIR1,NAME)
		convert_xlsx('B')
	input('Mission completed. Please check xlsx files in {}'.format(DIR1))
			
