from tkinter import *
import tkinter.messagebox as messagebox
from multiprocessing import Pool
import threading, queue,os
import subprocess, time


top = Tk()

top.minsize(300,240)

SLabel=Label(top,text='请输入网段的起始IP:',anchor='nw')
SLabel.pack()
SINPUT=Entry()
SINPUT.pack()

ELabel=Label(top,text='请输入网段的结束IP:')
ELabel.pack()
EINPUT=Entry()
EINPUT.pack()




def PING(iq,oq):
    while True:
        try:
            ip=iq.get(block=False)
#            print(ip)
        except queue.Empty:
            break
        try:
            child=subprocess.check_output("{} {}".format("ping -n 1",ip),shell=True,universal_newlines=True)
            if child.find('unreachable') >0:
                pass
            else:
                child1=subprocess.Popen("{} {}".format("nbtstat -a",ip),shell=True,stdout=subprocess.PIPE)
                child2=subprocess.Popen("find /i \"Registered\"",shell=True,universal_newlines=True, stdin=child1.stdout,stdout=subprocess.PIPE)
                out=child2.communicate()[0]
                oq.put("{} UP\n{}".format(ip,out))
        except subprocess.CalledProcessError:
            pass
        iq.task_done()

def test(p):
    print(p)


def callback():
    global IPSTART
    global IPEND
    global in_queue
    global out_queue
    out_queue=queue.Queue()
    in_queue=queue.Queue()

    L=[]
    IPS=[]
    IPSTART=SINPUT.get()
    IPEND=EINPUT.get()
    NETWORK1=os.path.splitext(IPSTART)[0]
    NETWORK2=os.path.splitext(IPEND)[0]
    START=int(os.path.splitext(IPSTART)[1].strip('.'))
    END=int(os.path.splitext(IPEND)[1].strip('.'))+1
    for i in range(START,END):
        IPS.append("{}.{}".format(NETWORK1,i))
    for ip in IPS:
        in_queue.put(ip)

    for i in range(30):
        t=threading.Thread(target=PING,args=(in_queue,out_queue))
        t.setDaemon(True)
        t.start()
    in_queue.join()
#   out_queue.join()
    t.join()

#   L.append(out_queue.get())
#   print(L)
#   print(out_queue.empty())
    


    while not out_queue.empty():
        L.append(out_queue.get())

    L=sorted(L,key=lambda nu: int(nu.split()[0].split('.')[-1]))
#    print(L)
    if L:

        listb=Listbox(top,height=20,width=130)
        for item in L:
            listb.insert(L.index(item)+1,item)
    else:
        listb=Listbox(top,width=30)
        listb.insert(0,"{} ~ {}".format(IPSTART,IPEND))
        listb.insert(1,"Does not contain any live IPs !!!")

    listb.pack()
        

    
#    print("time: {:.02f}".format(end-start))

START=Button(top,text='start',command=callback)
START.pack()






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

#app=Application()



#app.master.title('验证码：')

top.title('IP查询器')

top.mainloop()
