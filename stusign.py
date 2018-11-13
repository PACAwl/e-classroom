import socket
import tkinter
import tkinter.messagebox
def qiandao():
    window = tkinter.Tk()
    window.title("学生端界面")
    window.geometry("500x500")
    canvas = tkinter.Canvas(window, height="450", width="450", bg="white")
    canvas.pack()
    idlabel = tkinter.Label(window, bg="white", text="学号:", font=("楷体", 15))
    idlabel.place(x=80, y=100, width=80, height=50)

    namelabel = tkinter.Label(window, bg="white", text="姓名:", font=("楷体", 15))
    namelabel.place(x=80, y=170, width=80, height=50)

    identry = tkinter.Entry(window, bg="lightblue", font=("楷体", 15))
    identry.place(x=180, y=100, width=200, height=50)

    nameentry = tkinter.Entry(window, bg="lightblue", font=("楷体", 15))
    nameentry.place(x=180, y=170, width=200, height=50)
    # idlabel=tkinter.Label(app,text="学号",width=80)
    # idlabel.place(x=10,y=5,width=80,height=20)
    # identry=tkinter.Entry(app,width=80)
    # identry.place(x=100,y=5,width=80,height=20)
    #
    # namelabel=tkinter.Label(app,text="姓名",width=80)
    # namelabel.place(x=10,y=30,width=80,height=20)
    # nameentry=tkinter.Entry(app,width=80)
    # nameentry.place(x=100,y=30,width=80,heigh=20)

    s=socket.socket()
    s.connect(('192.168.10.165',8888))
    try:
        def check():
            id=identry.get()
            name=nameentry.get()
            print(id+name)
            s.send((id+" "+name).encode("utf-8"))
            mess=s.recv(1024).decode("utf-8")
            if mess=="notmath":
                tkinter.messagebox.showerror("失败","学号或者姓名输入错误")
            elif mess=="repeat":
                tkinter.messagebox.showerror("不允许重复签到")
            elif mess=="success":
                tkinter.messagebox.showinfo("签到成功")
    except ConnectionRefusedError:
        tkinter.messagebox.showerror("错误","还未开启签到功能")
    # btn=tkinter.Button(window,text="签到",command=check)
    # btn.place(x=30,y=90,width=80,height=20)
    button = tkinter.Button(window, bg="lightblue", text="签到", font=("楷体", 15), command=check)
    button.place(x=200, y=280, width=80, height=40)
    window.mainloop()