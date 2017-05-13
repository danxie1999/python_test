import sys,time,msvcrt


def readInput(caption,default,timeout=5):
	START=time.time()
	print("{}".format(caption),end="")
	sys.stdout.flush()
	INPUT=""
	while True:
		try:
			if msvcrt.kbhit():
				CHR=msvcrt.getche()
				CHR=CHR.decode('utf-8')
				if ord(CHR) == 13:
					break
				elif ord(CHR) >=32:
					INPUT+= CHR
		except:
			pass
		if len(INPUT) == 0 and time.time() - START >= timeout:
			break

	print('')

	if len(INPUT) > 0:
		return INPUT
	else:
		return default


string=readInput('请输入：','xiexie')
print(string)