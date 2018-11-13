import socket
import pymysql
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import threading
import json
from stusign import qiandao


window=Tk()
window.title("学生端登录界面")
window.geometry("500x500")
canvas=Canvas(window,height="450",width="450",bg="white")
canvas.pack()

labeltitle=tkinter.Label(window,bg="white",text="欢迎进入学生端登录界面",font=("楷体",17))
labeltitle.place(x=100,y=20,height=80,width=300)

idlabel=tkinter.Label(window,bg="white",text="学号:",font=("楷体",15))
idlabel.place(x=80,y=100,width=80,height=50)

namelabel=tkinter.Label(window,bg="white",text="姓名:",font=("楷体",15))
namelabel.place(x=80,y=170,width=80,height=50)

identry=tkinter.Entry(window,bg="lightblue",font=("楷体",15))
identry.place(x=180,y=100,width=200,height=50)

nameentry=tkinter.Entry(window,bg="lightblue",font=("楷体",15))
nameentry.place(x=180,y=170,width=200,height=50)
nameentry['show']='*'#使用*显示输出内容

def login():  # 验证账号密码
    id1 = identry.get()
    name = nameentry.get()
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="admin123456", database="test4",
                           charset="utf8")
    cur = conn.cursor()
    sql = "select stu_name from stu_info where stu_id=%s"
    row = cur.execute(sql, (id1))
    name2, = cur.fetchone()
    if row == 0:
        tkinter.messagebox.showerror("登录失败", "此账号未注册！")
    elif name == name2:
        tkinter.messagebox.showinfo("登录成功", "开始考试！")
        window.destroy()
        studentmainwin()
    else:
        tkinter.messagebox.showerror("登录失败", "密码错误！")



button=tkinter.Button(window,bg="lightblue",text="登录",font=("楷体",15),command=login)
button.place(x=200,y=280,width=80,height=40)


def studentmainwin():
    window = Tk()
    window.title("学生主界面")
    window.geometry("500x500")
    canvas = Canvas(window, height=400, width=400, bg="white")
    canvas.pack()
    def exit2():
        qiandao()
        window.destroy()

    def exit3():
        zicewin()
        window.destroy()

    def exit4():
        window.destroy()
        threading.Thread(target=kaoshi).start()


    def exit5():
        jiaozuoye()
        window.destroy()


    labeltitle = tkinter.Label(window, bg="white", text="欢迎进入学生主界面", font=("楷体", 17))
    labeltitle.place(x=100, y=20, height=80, width=300)
    button1 = tkinter.Button(window, text="学生签到功能", bg="lightblue",font=("楷体",15),command=exit2)
    button1.place(x=150, y=120, height=50, width=200)
    button2 = tkinter.Button(window, text="学生自测功能", bg="lightblue",font=("楷体",15),command=exit3)
    button2.place(x=150, y=190, height=50, width=200)
    button3 = tkinter.Button(window, text="学生考试功能", bg="lightblue",font=("楷体",15),command=exit4)
    button3.place(x=150, y=260, height=50, width=200)
    button4 = tkinter.Button(window, text="学生交作业功能", bg="lightblue",font=("楷体",15),command=exit5)
    button4.place(x=150, y=330, height=50, width=200)


    window.mainloop()


def qiandaowin():
    qiandao()
    # window = Tk()
    # window.title("学生端界面")
    # window.geometry("500x500")
    # canvas = Canvas(window, height="450", width="450", bg="white")
    # canvas.pack()
    #
    # idlabel = tkinter.Label(window, bg="white", text="学号:", font=("楷体", 15))
    # idlabel.place(x=80, y=100, width=80, height=50)
    #
    # namelabel = tkinter.Label(window, bg="white", text="姓名:", font=("楷体", 15))
    # namelabel.place(x=80, y=170, width=80, height=50)
    #
    # identry = tkinter.Entry(window, bg="lightblue", font=("楷体", 15))
    # identry.place(x=180, y=100, width=200, height=50)
    #
    # nameentry = tkinter.Entry(window, bg="lightblue", font=("楷体", 15))
    # nameentry.place(x=180, y=170, width=200, height=50)

    # button = tkinter.Button(window, bg="lightblue", text="签到", font=("楷体", 15),command=qiandao)
    # button.place(x=200, y=280, width=80, height=40)

def zicewin():
    window = tkinter.Tk()
    window.title("随堂自测")
    window.geometry("650x600")
    canvas = Canvas(window, bg="white", height=600, width=590)
    canvas.pack()

    label1 = tkinter.Label(window, bg="white", text="欢迎使用随堂自测功能", font=("楷体", 15))
    label1.place(x=50, y=10, height=60, width=550)

    label2 = tkinter.Label(window, bg="lightblue", font=("楷体", 13), justify="left")
    label2.place(x=50, y=70, height=300, width=550)

    var1 = StringVar

    def select():
        content = var1.get()
        # var.set("你的性别为  " + content)
        # b=var1.get()

    radio1 = tkinter.Radiobutton(window, text="A", font=("楷体", 15), variable=var1, value="A", bg="white")
    radio1.pack()
    radio1.place(x=50, y=380, height=40, width=40)

    radio2 = tkinter.Radiobutton(window, text="B", font=("楷体", 15), variable=var1, value="B", bg="white")
    radio2.pack()
    radio2.place(x=220, y=380, height=40, width=40)

    radio3 = tkinter.Radiobutton(window, text="C", font=("楷体", 15), variable=var1, value="C", bg="white")
    radio3.pack()
    radio3.place(x=380, y=380, height=40, width=40)

    radio4 = tkinter.Radiobutton(window, text="D", font=("楷体", 15), variable=var1, value="D", bg="white")
    radio4.pack()
    radio4.place(x=550, y=380, height=40, width=40)

    label3 = tkinter.Label(window, bg="lightblue", text="yorf", font=("楷体", 15))
    label3.place(x=160, y=500, height=40, width=100)

    label4 = tkinter.Label(window, bg="lightblue", text="var", font=("楷体", 15))
    label4.place(x=400, y=500, height=40, width=100)

    button1 = tkinter.Button(window, bg="lightblue", text="开始自测", font=("楷体", 15))
    button1.place(x=50, y=430, height=40, width=100)

    button2 = tkinter.Button(window, bg="lightblue", text="确定", font=("楷体", 15))
    button2.place(x=280, y=430, height=40, width=100)

    button3 = tkinter.Button(window, bg="lightblue", text="下一题", font=("楷体", 15))
    button3.place(x=500, y=430, height=40, width=100)


#+++++++++++++++++++++++++++++++++++考试界面
num = 0  # 控制题号和题目
count = 0  # 避免点击下一题超出范围
score = 0
key = 0  # 控制next函数里BTN5的功能
mistakelist = []
falg = True

# qu = []  # 考试题库
# scorelist = []  # 分数库，与试题对应
# answerlist = []
# tiall = []  # 自测题库
b = ""
def kaoshi():#+++++++++++++++++++++++++++++++++++考试界面
    def srs():
        global qu
        global scorelist
        global answerlist

        s = socket.socket()
        s.connect(("localhost", 8888))
        list1=s.recv(1024).decode("utf-8")
        list=json.loads(list1)

        qu=list[0]
        scorelist = list[1]  # 分数库，与试题对应
        answerlist = list[2]

    # num = 0  # 控制题号和题目
    # count = 0  # 避免点击下一题超出范围
    # score = 0
    # key = 0  # 控制next函数里BTN5的功能
    # mistakelist = []
    # falg = True

    # qu = []  # 考试题库
    # scorelist = []  # 分数库，与试题对应
    # answerlist = []
    # tiall = []  # 自测题库
    b = ""
#+++++++++++++++++++++++++++++++++++++++++++++++移除此部分
    # conn = pymysql.connect(host="localhost", port=3306, user="root", password="admin123456", database="test1",
    #                        charset="utf8")
    # cur = conn.cursor()
    # sql = "select * from tiku order by rand() limit 5"  # 随机限制取题
    # cur.execute(sql)
    # list = cur.fetchall()
    #
    # for ti in list:
    #     ti1 = (ti[0], ti[1], "A." + ti[2], "B." + ti[3], "C." + ti[4], "D." + ti[5], ti[6])
    #     k = ti1[1:6]
    #     j = "\n".join(k)
    #     t = ti[6] + "." + str(j)
    #     qu.append(t)  # 考试题库
    #     scorelist.append(ti[7])  # 分数题库
    #     answerlist.append(ti[6])  # 答案题库
    #     tiall.append(t)#全部题目，自测题库
#+++++++++++++++++++++++++++++++++++++++++++++++++++
    def window2():
        window = Tk()
        window.title("python测试系统")
        window.geometry("1000x700")

        var = StringVar()
        var1 = StringVar()
        var2 = StringVar()

        # 首页空白显示
        p = (
            "---------------------------------------------------------------------\n欢迎参加python考试\n(下列选择题每题10分,请仔细查看题目并作出选择)\n点击下一题开始答题\n-----------------------------------------------------------------------------------")
        if falg == True:
            var = StringVar()
            var.set(p)

        def last():
            global key
            global num
            global falg
            falg = False
            num -= 1
            key -= 1
            a = str("试题%d%s" % (num, qu[num - 1][1:]))
            var.set(a)
            if num <= 0:
                num = 0
                key = 0
                a = ("欢迎参加考试!\n点击下一题开始做题！")
                var.set(a)

        def next():
            global key
            key += 1
            if key <= len(answerlist):
                btn5["state"] = "normal"
            global num
            global falg
            falg = False
            num += 1
            a = str("试题%d%s" % (num, qu[num - 1][1:]))
            var.set(a)
            if num > 4:  #
                num -= 1
                a = ("考试结束！\n" + b)
                var.set(a)  # ????????????????????????????????????????????分数有时候不显示

        def uppaper():  # 提交答案
            global score
            global b
            global count

            btn5["state"] = "disabled"
            content = var1.get()  # 显示答案
            if answerlist[num - 1] == content:
                score += int(scorelist[num - 1])
                b = str("您的分数是：%d" % score)
            else:
                count += 1
                rightanswer = answerlist[num - 1]
                tkinter.messagebox.showerror("错误", "正确答案为%s" % (rightanswer))  # 代码优化：显示正确答案

        def select():
            global score
            global b
            global count
            content = var1.get()  # 显示答案
            var2.set("您选择的答案是：" + content)

        def test():
            window.destroy()

        def ext():
            sys.exit()

        radioa = Radiobutton(window, text="A", font=("", 20), variable=var1, value="A", command=select)
        radioa.place(x=520, y=550)
        radioa = Radiobutton(window, text="B", font=("", 20), variable=var1, value="B", command=select)
        radioa.place(x=620, y=550)
        radioa = Radiobutton(window, text="C", font=("", 20), variable=var1, value="C", command=select)
        radioa.place(x=720, y=550)
        radioa = Radiobutton(window, text="D", font=("", 20), variable=var1, value="D", command=select)
        radioa.place(x=820, y=550)

        # 桌布
        show = Label(window, textvariable=var2, font=("", 20))
        show.place(x=50, y=450, width=900, height=50)
        option = Label(window, text="请在以下选项中勾选答案：", font=("", 20))
        option.place(x=50, y=550)
        ti = Label(window, bg="white", textvariable=var, font=("楷体", 20), justify="left", anchor=W)
        ti.place(x=50, y=50, width=900, height=400)

        btn1 = Button(window, text="上一题", bg="gray", font=("", 20), command=last)
        btn1.place(x=70, y=630)
        btn2 = Button(window, text="下一题", bg="gray", font=("", 20), command=next)
        btn2.place(x=230, y=630)
        btn3 = Button(window, text="提交试卷", bg="gray", font=("", 20), command=test)
        btn3.place(x=700, y=630)
        btn4 = Button(window, text="退出", bg="gray", font=("", 20), command=ext)
        btn4.place(x=850, y=630)
        btn5 = Button(window, state="disabled", text="提交答案", bg="gray", font=("", 20), command=uppaper)
        btn5.place(x=390, y=630)

        window.mainloop()

    threading.Thread(target=window2).start()#线程启动考试窗口
    threading.Thread(target=srs).start()

def jiaozuoye():#提交作业
    def fileupload():
        s = socket.socket()
        s.connect(("localhost", 8888))
        filename = tkinter.filedialog.askopenfilename(title="请选择路径")
        s.send(filename.encode("utf-8"))
        file = open(filename, "rb")
        while True:
            data = file.read(1024)
            s.send(data)
            if data == b"":
                tkinter.messagebox.showinfo("成功","文件上传成功")
                break
        file.close()
        s.close()

    window = Tk()
    window.title("导入试卷")
    window.geometry("350x350")
    canvas = Canvas(window, width="300", height="300", bg="white")
    canvas.pack()

    lable = Label(window, bg="white", text="欢迎使用试卷导入功能", font=("楷体", 15))
    lable.pack()
    lable.place(x=40, y=40, height=40, width=270)

    button = Button(window, bg="lightblue", text="导入试题", font=("楷体", 15),command=fileupload)
    button.pack()
    button.place(x=130, y=170, height=40, width=100)

    window.mainloop()


window.mainloop()