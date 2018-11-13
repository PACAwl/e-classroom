import socket
import pymysql
from tkinter import *
import tkinter.messagebox
import threading
import json
from teasign import qiandao

server=socket.socket()
server.bind(("localhost",8888))
server.listen(100)

iplist=[]

qu = []  # 考试题库
scorelist = []  # 分数库，与试题对应
answerlist = []
tiall = []  # 自测题库
b = ""
def exam():
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="admin123456", database="test1",
                           charset="utf8")
    cur = conn.cursor()
    sql = "select * from tiku order by rand() limit 5"  # 随机限制取题
    cur.execute(sql)
    list = cur.fetchall()

    for ti in list:
        ti1 = (ti[0], ti[1], "A." + ti[2], "B." + ti[3], "C." + ti[4], "D." + ti[5], ti[6])#代码可优化成抽大量题目
        k = ti1[1:6]
        j = "\n".join(k)
        t = ti[6] + "." + str(j)
        qu.append(t)  # 考试题库
        scorelist.append(ti[7])  # 分数题库
        answerlist.append(ti[6])  # 答案题库
        tiall.append(t)#全部题目，自测题库

    list=[qu,scorelist,answerlist]
    list_js = json.dumps(list)


    def trs():#接收上线学生用户
        while True:
            s, addr = server.accept()
            s.send(list_js.encode("utf-8"))

    threading.Thread(target=trs).start()

def windowall():
    def login():  # 验证账号密码
        id1 = identry.get()
        name = nameentry.get()
        conn = pymysql.connect(host="localhost", port=3306, user="root", password="admin123456", database="test3",
                               charset="utf8")
        cur = conn.cursor()
        sql = "select tea_name from teacher where tea_id=%s"
        row = cur.execute(sql, (id1))
        if row == 0:
            tkinter.messagebox.showerror("登录失败", "此账号未注册！")
        else:
            name2, = cur.fetchone()
            if name == name2:
                tkinter.messagebox.showinfo("登录成功", "开始考试！")
                window.destroy()
                teschermainwin()

            else:
                tkinter.messagebox.showerror("登录失败", "密码错误！")

    window=Tk()
    window.title("教师端登录界面")
    window.geometry("500x500")
    canvas=Canvas(window,height="450",width="450",bg="white")
    canvas.pack()

    labeltitle=tkinter.Label(window,bg="white",text="欢迎进入教师端登录界面",font=("楷体",17))
    labeltitle.place(x=100,y=20,height=80,width=300)

    idlabel=tkinter.Label(window,bg="white",text="工号:",font=("楷体",15))
    idlabel.place(x=80,y=100,width=80,height=50)

    namelabel=tkinter.Label(window,bg="white",text="密码:",font=("楷体",15))
    namelabel.place(x=80,y=170,width=80,height=50)

    identry=tkinter.Entry(window,bg="lightblue",font=("楷体",15))
    identry.place(x=180,y=100,width=200,height=50)

    nameentry=tkinter.Entry(window,bg="lightblue",font=("楷体",15))
    nameentry.place(x=180,y=170,width=200,height=50)
    nameentry['show']='*'#使用*显示输出内容

    button=tkinter.Button(window,bg="lightblue",text="登录",font=("楷体",15),command=login)
    button.place(x=200,y=280,width=80,height=40)


    def teschermainwin():
        window = Tk()
        window.title("教师主界面")
        window.geometry("500x500")
        canvas = Canvas(window, height=400, width=400, bg="white")
        canvas.pack()
        def exit2():
            # dianmingwin()
            threading.Thread(target=dianmingwin).start()

        def exit3():
            threading.Thread(target=kaishikaoshiwin).start()

        def exit4():
            threading.Thread(target=shouzuoye).start()

        labeltitle = tkinter.Label(window, bg="white", text="欢迎进入教师主界面", font=("楷体", 17))
        labeltitle.place(x=100, y=20, height=80, width=300)
        button1 = tkinter.Button(window, text="教师点名功能", bg="lightblue",font=("楷体",15),command=exit2)
        button1.place(x=150, y=120, height=50, width=200)
        button2 = tkinter.Button(window, text="教师开启考试功能", bg="lightblue",font=("楷体",15),command=exit3)
        button2.place(x=150, y=190, height=50, width=200)
        button3 = tkinter.Button(window, text="教师收作业功能", bg="lightblue",font=("楷体",15),command=exit4)
        button3.place(x=150, y=260, height=50, width=200)

        window.mainloop()


    def dianmingwin():
        window = Tk()
        window.title("开始点名界面")
        window.geometry("400x400")
        canvas = Canvas(window, height="350", width="350", bg="white")
        canvas.pack()

        button = tkinter.Button(window, bg="lightblue", text="开始签到", font=("楷体", 15),command=run)
        button.place(x=150, y=100, width=100, height=50)
        window.mainloop()
    def run():
        threading.Thread(target=qiandao).start()
    def beginexam():
        threading.Thread(target=exam).start()

    def kaishikaoshiwin():
        window = Tk()
        window.title("开始考试界面")
        window.geometry("400x400")
        canvas = Canvas(window, height="350", width="350", bg="white")
        canvas.pack()

        button = tkinter.Button(window, bg="lightblue", text="开始考试", font=("楷体", 15),command=beginexam)
        button.place(x=150, y=100, width=100, height=50)
        window.mainloop()

    def shouzuoye():
        def save():
            # window1.destroy()
            def savefile(s):
                filename = s.recv(1024).decode("utf-8").split("/")[-1]
                file = open(r"E:" + "\\" + filename, "wb")
                while True:
                    data = s.recv(1024)
                    if data == b'':
                        tkinter.messagebox.showinfo("成功", "接收一个文件")
                        #代码优化：共接收多少文件添加
                        break
                    else:
                        file.write(data)
                file.close()
            while True:
                s, addr = server.accept()
                threading.Thread(target=savefile, args=(s,)).start()

        window1 = Tk()
        window1.title("开始收作业界面")
        window1.geometry("400x400")
        canvas = Canvas(window1, height="350", width="350", bg="white")
        canvas.pack()

        def usesave():
            threading.Thread(target=save).start()
        button = tkinter.Button(window1, bg="lightblue", text="开始收作业", font=("楷体", 15),command=usesave)
        button.place(x=150, y=100, width=100, height=50)
        window1.mainloop()

    window.mainloop()

if __name__=="__main__":
    threading.Thread(target=windowall).start()
