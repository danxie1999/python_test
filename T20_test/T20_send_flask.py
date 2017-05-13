#!/usr/bin/env python3
import socket,time,sys
from flask import Flask,request,render_template,url_for,redirect

HOST="10.146.90.91"

PORT=12201


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])

def home():
    return render_template('home.html')


@app.route('/t20_send',methods=['GET','POST'])

def t20_send():
    if request.method=='POST':
        T20=request.form['t20_string']
        if T20:
            T20=T20.strip()
            try:
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((HOST,PORT))
                s.send(bytes(T20,encoding="utf-8"))
                data=s.recv(1024).decode('utf-8')
                data=data.strip()
            except:
                pass
            finally:
                s.close()
            return render_template('form.html',message='{}'.format(T20),Data=';{}'.format(data))
        else:
            return render_template('form.html')
    else:
        return render_template('form.html')


if __name__ == '__main__': 
    app.run(host="0.0.0.0",port=8888)
