from tkinter import *
import tkinter.messagebox as messagebox
import subprocess

top= Tk()

#child=subprocess.Popen('python pillow_test2.py',shell=True)
#child.wait()

li = ['Apple','Orange','Pineapple']

#li2= ['PC','laptop','watch']

listb = Listbox(top,height=30,width=100)
#listb2 = Listbox(top)

for item in li:
	listb.insert(10,item)

#for item in li2:
#	listb2.insert(0,item)

listb.pack()
#listb2.pack()
top.mainloop()

#def hello():
#	messagebox.showinfo("Hello World","Hello World")

#B = Button(top,text="Hello,world!hello",command=hello)

#var=PhotoImage(file='code.png')

#lable=Label(top,image=var,relief=RAISED)

#lable.pack()

#top.mainloop()

