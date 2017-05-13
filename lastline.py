import os

def last_line(inputfile):
	filesize=os.path.getsize(inputfile)
	blocksize=1024
	if filesize > blocksize:
		seekpoint=(filesize // blocksize)
	with open(inputfile,'r') as f:
		if filesize > blocksize:
			seekpoint= (filesize //  blocksize)
			f.seek=((seekpoint -1) * blocksize)
		else:
			f.seek(0,0)
		lines=f.readlines()
		if lines:
			lastline=lines[-1].strip()
			return lastline

if __name__ == "__main__":
	line=last_line('mail_count.txt')
	print(line)
