from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='请输入验证码：')
        self.helloLabel.pack(side=LEFT)
        e=StringVar()
        self.Input = Entry(self,textvariable=e)
        self.Input.pack(side=LEFT)
        e.set('input your test here')

#        self.confirmButton = Button(self,test='Confirm',command=self.quit)
#        self.confirmButton.pack()

        self.ConfirmButton = Button(self, text='Confirm', command=self.hello)
        self.ConfirmButton.pack(side=LEFT)



    def hello(self):
        name = self.Input.get()
#        messagebox.showinfo('Message',name)
		return name

app=Application()

app.master.title('验证码：')

app.mainloop()
