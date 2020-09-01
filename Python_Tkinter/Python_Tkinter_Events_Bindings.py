'''
事件(Events)
元件要處理的程序。

綁定(Bindings)
將元件和事件綁在一起。

'''

# 載入 tkinter
from tkinter import *
# Messagebox
from tkinter import messagebox

##==============================================================================================
## Function(Events)
##==============================================================================================

# 滑鼠綁定
# 當滑鼠在 frame 的範圍裡，點擊左鍵時將執行 callback
def event_to_cursor():
    # 事件
    def callback(event):
        # 印出滑鼠左鍵點擊時的座標
        print("Clicked at",event.x,event.y)

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("event_to_cursor")

    # Frame
    frame = Frame(root,width=300,height=180)
    # 綁定
    # <Button-1> : 滑鼠左鍵點擊
    frame.bind("<Button-1>",callback)
    # 包裝
    frame.pack()

    # 執行，放在最後一行
    root.mainloop()

# 滑鼠綁定(進入、離開)
def event_to_enter_leave():
    # 事件(進入)
    def enter(event):
        x.set("滑鼠進入Exit")

    # 事件(離開)
    def leave(event):
        x.set("滑鼠離開Exit")

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("event_to_enter_left")

    # exit按鈕
    btn = Button(root,text="Exit",command=root.destroy)
    # 包裝
    btn.pack(pady=30)
    # 綁定事件(進入)
    btn.bind("<Enter>",enter)
    # 綁定事件(離開)
    btn.bind("<Leave>", leave)

    x = StringVar()
    # 標籤
    lab = Label(root,textvariable = x,bg="yellow",fg="blue",height=4,width=15)
    # 包裝
    lab.pack(pady=30)

    # 執行，放在最後一行
    root.mainloop()

# 鍵盤綁定
# 當按下按鍵時，顯示按鍵
def event_to_keyboard():
    # 處理按鍵
    def key(event):
        keyvar.set("按下" + repr(event.char) + "鍵")

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("event_to_keyboard")

    # 綁定鍵盤
    root.bind("<Key>",key)
    # StringVar
    keyvar = StringVar()
    keyvar.set("按下任意鍵")
    # 標籤
    lab = Label(root,textvariable = keyvar,height=4,width=15)
    # 包裝
    lab.pack(padx=30,pady=30)


    # 執行，放在最後一行
    root.mainloop()

# 鍵盤綁定(ESC)
# 當按下esc時，顯示對話方塊
def event_to_keyboard_esc():
    # 事件
    def leave(event):
        # Messagebox
        ret = messagebox.askyesno("要離開嗎?","請選擇")
        if ret == True:
            root.destroy()
        else:
            return

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("event_to_keyboard_esc")

    # 綁定esc
    root.bind("<Escape>",leave)
    # 標籤
    lab = Label(root,text="測試ESC",height=4,width=15)
    # 包裝
    lab.pack(padx=30,pady=30)


    # 執行，放在最後一行
    root.mainloop()

##==============================================================================================
## Function(Bindings)
##==============================================================================================

# 取消綁定
# 當 Button 和 核取方塊 有綁定時，按下 Button 會顯示 "I like tkinter."
def bind_to_unbinding():
    # Button 事件
    def buttonclick(event):
        print("I like tkinter.")

    # 核取方塊 事件
    # onoff 代表 btn
    def toggle(onoff):
        # 如果cbtn勾選，btn 綁定 buttonclick()
        if var.get() == True:
            onoff.bind("<Button-1>",buttonclick)
        # 如果cbtn不勾選，btn 不綁定 buttonclick()
        else:
            onoff.unbind("<Button-1>")

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("bind_to_unbinding")

    # Button
    btn = Button(root,text="Tkinter")
    btn.pack(anchor=W,padx=10,pady=10)

    # 核取方塊
    var = BooleanVar()
    cbtn = Checkbutton(root,text="bind/unbind",variable=var,command=lambda:toggle(btn))
    cbtn.pack(anchor=W,padx=10)

    # 執行，放在最後一行
    root.mainloop()

# 多項綁定
# 一個 Button 綁定兩個事件
# 先執行 bind綁定事件 再執行 command綁定事件
def bind_to_multibind():
    # Button 事件1
    def buttonclick_1():
        print("command")

    # Button 事件2
    def buttonclick_2(event):
        print("bind")

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("bind_to_multibind")

    # Button
    # 先用 command 綁定 buttonclick_1()
    btn = Button(root,text="Tkinter",command = buttonclick_1)
    btn.pack(anchor=W,padx=10,pady=10)
    # 再綁定 buttonclick_2()
    btn.bind("<Button-1>",buttonclick_2,add="+")

    # 執行，放在最後一行
    root.mainloop()

# 使用Protocol
# 可以按右上角的X結束視窗
def bind_to_protocol():
    def callback():
        res = messagebox.askokcancel("Ok Chancel","結束或消失?")
        if res == True:
            root.destroy()
        else:
            return

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("bind_to_protocol")

    # protocol
    root.protocol("WM_DELETE_WINDOW",callback)

    # 執行，放在最後一行
    root.mainloop()

##==============================================================================================
## Main
##==============================================================================================

# ===============================
# Events
# ===============================

# 滑鼠綁定
#event_to_cursor()

# 滑鼠綁定(進入、離開)
#event_to_enter_leave()

# 鍵盤綁定
#event_to_keyboard()

# 鍵盤綁定(ESC)
#event_to_keyboard_esc()

# ===============================
# Bindings
# ===============================

# 取消綁定
#bind_to_unbinding()

# 多項綁定
#bind_to_multibind()

# 使用Protocol
#bind_to_protocol()






















































