'''
容器控件(Container Widget)
'''

# 載入tkinter
from tkinter import *
# 載入 relief 給 Frame
from tkinter.ttk import Frame,Style
# 隨機數
import random


##==============================================================================================
## Function(Frame)
##==============================================================================================

# Frame 基本用法
def frame_to_base():

    # 建立視窗，root可取其它名稱
    root = Tk()
    #  視窗標題
    root.title("frame_to_base")

    # 建立3個不同底色的Frame
    for fm in ["red","green","blue"]:
        Frame(root,bg=fm,height=50,width=250).pack()

    # 執行，放在最後一行
    root.mainloop()

# Frame 基本用法(橫向)
def frame_to_cursor():

    # 建立視窗，root可取其它名稱
    root = Tk()
    #  視窗標題
    root.title("frame_to_cursor")

    # 建立字典儲存顏色和鼠標外觀
    fms = {"red":"cross","green":"boat","blue":"clock"}

    # 建立3個不同底色的Frame
    # cursor = 鼠標
    for fmColor in fms:
        Frame(root,bg=fmColor,cursor=fms[fmColor],height=50,width=200).pack(side=LEFT)

    # 執行，放在最後一行
    root.mainloop()

# Frame 內新增元件
def frame_to_add_object():

    # 建立視窗，root可取其它名稱
    root = Tk()
    #  視窗標題
    root.title("frame_to_add_object")

    # 上層Frame，父容器為root
    frameUpper = Frame(root,bg="lightyellow")
    frameUpper.pack()

    # btnRed，父容器為frameUpper
    btnRed = Button(frameUpper,text="Red",fg="red")
    btnRed.pack(side=LEFT,padx=5,pady=5)

    # btnGreen，父容器為frameUpper
    btnGreen = Button(frameUpper, text="Green", fg="green")
    btnGreen.pack(side=LEFT, padx=5, pady=5)

    # btnBlue，父容器為frameUpper
    btnBlue = Button(frameUpper, text="Blue", fg="blue")
    btnBlue.pack(side=LEFT, padx=5, pady=5)

    # 下層Frame
    frameLower = Frame(root, bg="lightblue")
    frameLower.pack()

    # btnPurple，父容器為frameLower
    btnPurple = Button(frameLower, text="Purple", fg="purple")
    btnPurple.pack(side=LEFT, padx=5, pady=5)

    # 執行，放在最後一行
    root.mainloop()

# Frame 新增 Check Box
def frame_with_checkbox():
    # 建立視窗，root可取其它名稱
    root = Tk()
    #  視窗標題
    root.title("frame_with_checkbox")

    # Frame
    fm = Frame(root,width=150,height=80,relief=RAISED,borderwidth=5)
    fm.pack(padx=10,pady=10)

    # Label
    lab = Label(fm,text="請選擇常用的程式語言")
    lab.pack()

    # check box(python)
    cbpython = Checkbutton(fm,text="Python")
    cbpython.pack(anchor=W)

    # check box(java)
    cbjava = Checkbutton(fm, text="java")
    cbjava.pack(anchor=W)

    # check box(javascript)
    cbjavascript = Checkbutton(fm, text="javascript")
    cbjavascript.pack(anchor=W)

    # 執行，放在最後一行
    root.mainloop()

# Frame with relief
def frame_with_relief():
    # 建立視窗，root可取其它名稱
    root = Tk()
    #  視窗標題
    root.title("frame_with_relief")

    # 改用 Style
    style = Style()
    # 改用 alt 支援 Style
    style.theme_use("alt")

    # frame 1
    fm1 = Frame(root,width=150,height=80,relief="flat")
    fm1.grid(row=0,column=0,padx=5,pady=5)

    # frame 2
    fm2 = Frame(root, width=150, height=80, relief="groove")
    fm2.grid(row=0, column=1, padx=5, pady=5)

    # frame 3
    fm3 = Frame(root, width=150, height=80, relief="raised")
    fm3.grid(row=0, column=2, padx=5, pady=5)

    # frame 4
    fm4 = Frame(root, width=150, height=80, relief="ridge")
    fm4.grid(row=1, column=0, padx=5, pady=5)

    # frame 5
    fm5 = Frame(root, width=150, height=80, relief="solid")
    fm5.grid(row=1, column=1, padx=5, pady=5)

    # frame 6
    fm5 = Frame(root, width=150, height=80, relief="sunken")
    fm5.grid(row=1, column=2, padx=5, pady=5)

    # 執行，放在最後一行
    root.mainloop()

##==============================================================================================
## Function(LabelFrame)
##==============================================================================================

# LabelFrame 基本用法
def labelframe_to_base():
    # 建立視窗，root可取其它名稱
    root = Tk()
    #  視窗標題
    root.title("labelframe_to_base")

    # 基本訊息
    msg = "歡迎進入Tkinter系統"
    # Logo
    boximg = PhotoImage(file="../imgfolder/sun.png")
    logo = Label(root,image=boximg,text=msg,compound=BOTTOM)
    logo.pack()

    # LabelFrame
    labFrame = LabelFrame(root,text="資料驗證")
    labFrame.pack(padx=10,pady=5,ipadx=5,ipady=5)

    # 標籤 account
    labaccount = Label(labFrame,text="Account")
    labaccount.grid(row=0,column=0)

    # 標籤 pwd
    labpwd = Label(labFrame, text="Password")
    labpwd.grid(row=1, column=0)

    # 文字方塊 account
    entryaccount = Entry(labFrame)
    entryaccount.grid(row=0, column=1)

    # 文字方塊 pwd
    entrypwd = Entry(labFrame,show="*")
    entrypwd.grid(row=1, column=1,pady=10)

    # 執行，放在最後一行
    root.mainloop()

# LabelFrame with check box
def labelframe_with_checkbox():
    # 印出資訊
    def printinfo():
        for i in checkboxes:
            if(checkboxes[i].get() == True):
                print(sports[i]);

    # 建立視窗，root可取其它名稱
    root = Tk()
    #  視窗標題
    root.title("labelframe_with_checkbox")

    # LabelFrame
    labFrame = LabelFrame(root,text="選擇最喜歡的運動")
    labFrame.pack(pady=10,ipadx=5,ipady=5)
    # 字典:運動
    sports = {0:"美式足球",1:"棒球",2:"籃球",3:"網球"}
    # 字典:用於被勾選的項目
    checkboxes = {}

    # 建立 check box
    for i in range(len(sports)):
        # Bool變數物件
        checkboxes[i] = BooleanVar()
        Checkbutton(labFrame,text=sports[i],variable=checkboxes[i]).grid(row=i+1,sticky=W)

    # 確定 Button
    btn = Button(root,text="確定",width=10,command=printinfo)
    btn.pack()

    # 執行，放在最後一行
    root.mainloop()

##==============================================================================================
## Function(Toplevel)
## Toplevel:產生新的視窗
##==============================================================================================

# Toplevel 基本用法
def toplevel_to_base():
    # 建立視窗，root可取其它名稱
    root = Tk()
    #  視窗標題
    root.title("toplevel_to_base")

    # Toplevel
    tl = Toplevel()
    # 設定視窗大小
    tl.geometry("300x180")
    # Label
    lab = Label(tl,text="I am a TopLevel")
    lab.pack()

    # 執行，放在最後一行
    root.mainloop()

# Toplevel 模擬對話
def toplevel_to_talk():
    # 對話字串
    msgYes = 1
    msgNo = 2
    msgExit = 3

    # 對話視窗
    def MessageBox():
        # 隨機產生對話
        msgType = random.randint(1,3)
        if msgType == msgYes:
            labtxt = "Yes"
        elif msgType == msgNo:
            labtxt = "No"
        elif msgType == msgExit:
            labtxt = "Exit"

        # Toplevel
        tl = Toplevel()
        # 視窗大小
        tl.geometry("300x180")
        # 視窗標題
        tl.title("Message Box")
        # Label
        Label(tl,text=labtxt).pack(fill=BOTH,expand=True)

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("toplevel_to_talk")

    # Button
    btn = Button(root,text="Click",command=MessageBox)
    btn.pack()

    # 執行，放在最後一行
    root.mainloop()

##==============================================================================================
## Function(統合)
##==============================================================================================

# Frame Project 1
def frame_project_one():
    # click_Radibutton
    def click_Radibutton():
        if v1.get() == 1:
            print("淺藍色")
        elif v1.get() == 2:
            print("淺綠色")

    # click_bold_box
    def click_bold_box():
        if v2.get() == 1:
            print("粗體")
        else:
            print("粗體無設定")

    # click_italic_box
    def click_italic_box():
        if v3.get() == 1:
            print("斜體")
        else:
            print("斜體無設定")

    # get_name
    def get_name():
        print("姓名: " + name.get())


    # 建立視窗，root可取其它名稱
    root = Tk()
    #  視窗標題
    root.title("frame_project_one")

    # frame 1，2 radio button、2 check box
    frame1 = Frame(root)
    frame1.pack()

    # radio button變數
    v1 = IntVar()
    v1.set(1)

    # radio button(blue)
    rb_blue = Radiobutton(frame1,text="淺藍",bg="lightblue",variable=v1,value=1,command =click_Radibutton)
    rb_blue.grid(row=1,column=1)

    # radio button(green)
    rb_green = Radiobutton(frame1, text="淺綠", bg="lightgreen", variable=v1, value=2, command=click_Radibutton)
    rb_green.grid(row=1, column=2)

    # chech box變數
    v2 = IntVar()
    # check box(Bold)
    cb_Bold = Checkbutton(frame1,text="粗體", variable=v2,command=click_bold_box)
    cb_Bold.grid(row=2, column=1)

    # chech box變數
    v3 = IntVar()
    # check box(Italic)
    cb_Italic = Checkbutton(frame1, text="斜體", variable=v3, command=click_italic_box)
    cb_Italic.grid(row=2, column=2)

    # frame 2，1 Label、1 Entry、1button
    frame2 = Frame(root)
    frame2.pack()

    # Label
    lab = Label(frame2,text="請輸入名字:")
    lab.grid(row=1,column=1)

    # Entry 變數
    name = StringVar()
    # Entry
    entry_name = Entry(frame2,textvariable=name)
    entry_name.grid(row=1,column=2)

    # Button
    btn_click = Button(frame2,text="執行",command=get_name)
    btn_click.grid(row=1,column=3,padx=3)

    # 輸出
    label_out = Label(root,text="控件組合應用")
    label_out.pack()

    # 執行，放在最後一行
    root.mainloop()

# Frame Project 2
def frame_project_two():
    # color_radiobutton
    def color_radiobutton():
        if var.get() == "blue_color":
            lab["fg"] = "blue"
        elif var.get() == "green_color":
            lab["fg"] = "green"
        elif var.get() == "red_color":
            lab["fg"] = "red"

    # new_text_btn
    def new_text_btn():
        lab["text"] = msg.get()

    # 建立視窗，root可取其它名稱
    root = Tk()
    #  視窗標題
    root.title("frame_project_two")

    # frame 1
    frame1 = Frame(root)
    frame1.pack()

    # Label
    lab = Label(frame1,text="Python Tkinter")
    lab.pack()

    # frame 2
    frame2 = Frame(root)
    frame2.pack()

    # Label(input)
    lab_input = Label(frame2,text="請輸入文字: ")
    lab_input.grid(row=1,column=1)

    # Entry 變數
    msg = StringVar()
    # Entry
    entry = Entry(frame2,textvariable = msg)
    entry.grid(row=1,column=2)

    # Button
    btn_change = Button(frame2,text="更改",command = new_text_btn)
    btn_change.grid(row=1,column=3)

    # Radio Button 變數
    var = StringVar()
    var.set(1)

    # Radio Button(blue)
    rb_blue = Radiobutton(frame2,text="藍色",bg="lightblue",variable=var,value="blue_color",command = color_radiobutton)
    rb_blue.grid(row=2,column=1)

    # Radio Button(green)
    rb_green = Radiobutton(frame2, text="綠色", bg="lightgreen", variable=var, value="green_color",command=color_radiobutton)
    rb_green.grid(row=2, column=2)

    # Radio Button(red)
    rb_red = Radiobutton(frame2, text="紅色", bg="red", variable=var, value="red_color",command=color_radiobutton)
    rb_red.grid(row=2, column=3)

    # 執行，放在最後一行
    root.mainloop()

# Frame Project 3
def frame_project_three():
    # 重新顯示
    def do_shuffle():
        random.shuffle(imglist)
        for i in range(len(imglist)):
            labelist[i]["image"] = imglist[i]

    # 建立視窗，root可取其它名稱
    root = Tk()
    #  視窗標題
    root.title("frame_project_three")

    # List:image
    imglist = []
    # 放入image
    imglist.append(PhotoImage(file="../imgfolder/sun.png"))
    imglist.append(PhotoImage(file="../imgfolder/star.png"))
    imglist.append(PhotoImage(file="../imgfolder/rain.png"))

    # Frame
    frame = Frame(root)
    frame.pack()

    # List:顯示 image
    labelist = []
    # 顯示3張圖片
    for i in range(3):
        labelist.append(Label(frame,image=imglist[i]))
        labelist[i].pack(side=LEFT)

    # Button
    btn = Button(root,text="重新顯示",command=do_shuffle)
    btn.pack(pady=5)

    # 執行，放在最後一行
    root.mainloop()
##==============================================================================================
## Main
##==============================================================================================

# ===============================
# Frame
# ===============================

# Frame 基本用法
#frame_to_base()

# Frame 基本用法(橫向)
#frame_to_cursor()

# Frame 內新增元件
#frame_to_add_object()

# Frame 新增 Check Box
#frame_with_checkbox()

# Frame with relief
#frame_with_relief()

# ===============================
# LabelFrame
# ===============================

# LabelFrame 基本用法
#labelframe_to_base()

# LabelFrame with check box
#labelframe_with_checkbox()


# ===============================
# TopFrame
# ===============================

# Toplevel 基本用法
#toplevel_to_base()

# Toplevel 模擬對話
#toplevel_to_talk()


# ===============================
# 統合
# ===============================

# Frame Project 1
#frame_project_one()

# Frame Project 2
#frame_project_two()

# Frame Project 3
#frame_project_three()














































