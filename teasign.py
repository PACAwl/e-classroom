import socket
import threading
import pymysql
import datetime
import tkinter
# today=str(datetime.datetime.today())[0:10]
# app = tkinter.Tk()
def qiandao():
    server=socket.socket()
    server.bind(('192.168.10.165',8888))
    server.listen(100)

    # btn=tkinter.Button(app,text="开始签到",command=qiandao)
    # btn.place(x=30,y=50,width=50,height=20)
    # btn2=tkinter.Button(app,text="结束签到")
    # btn2.place(x=100,y=50,width=50,height=20)
    conn=pymysql.connect(host="localhost",port=3306,
                         user="root",password="admin123456",
                         database="test4",charset="utf8")
    cur=conn.cursor()
    # btn=tkinter.Button(app,text="开始签到",command=run)
    # btn.place(x=30,y=50,width=50,height=20)
    # btn2=tkinter.Button(app,text="结束签到")
    # btn2.place(x=100,y=50,width=50,height=20)
    # app = tkinter.Tk()
    iplist=[]

    def run(s,addr):

        while True:
            today = str(datetime.datetime.today())[0:10]
            data=s.recv(1024).decode("utf-8")
            print(data)
            id,name=data.split(" ")
            sql="select stu_name from stu_info where stu_id=%s"
            row=cur.execute(sql,(id))
            if row==0:
                s.send("notmath".encode("utf-8"))
            else:
                if cur.fetchone()[0]!=name:
                    s.send("notmath".encode("utf-8"))
                else:
                    if addr[0] in iplist:
                        s.send("repeat".encode("utf-8"))
                    else:
                        sql4="select timedate from stu_info where stu_id=%s"
                        cur.execute(sql4,(id))
                        if cur.fetchone()[0]!= today:
                            iplist.append(addr[0])
                            sql2="update stu_info set score=score+5 where stu_id=%s"
                            cur.execute(sql2,(id))
                            sql3 = "update stu_info set timedate=%s where stu_id=%s"
                            cur.execute(sql3, (today,id))
                            conn.commit()
                            s.send("success".encode("utf-8"))
                        else:
                            s.send("repeat".encode("utf-8"))


    while True:
        s,addr=server.accept()
        threading.Thread(target=run,args=(s,addr,)).start()


    server.close()
