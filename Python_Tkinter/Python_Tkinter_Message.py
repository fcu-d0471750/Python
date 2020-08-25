'''
短訊息(Message)
類似 Label 但彈性較大，針對一些不需再次編輯的短文。
'''

# 載入 tkinter
from tkinter import *
# 載入 Messagebox 模組
from tkinter import messagebox

##==============================================================================================
## Function(Message)
##==============================================================================================

# Message 基本用法
def message_to_basic():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("message_to_basic")

    # Message 的訊息
    mytest = "Hello World."

    # Message
    msg = Message(root,text = mytest,font="times 12 italic")
    # 包裝元件
    msg.pack(padx=10,pady=10)

    # 執行，放在最後一行
    root.mainloop()

##==============================================================================================
## Function(Messagebox)
##==============================================================================================

# Messagebox 基本用法
def messagebox_to_basic():
    # 顯示 Messagebox
    def myMsg():
        messagebox.showinfo("My Message Box","Python Tkinter Good Morning.")

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("messagebox_to_basic")

    # Button
    btn = Button(root,text="Good",command=myMsg)
    btn.pack()


    # 執行，放在最後一行
    root.mainloop()

# 取得使用者的回應
def messagebox_to_get():
    # 顯示 Messagebox
    def myMsg1():
        ret = messagebox.askretrycancel("myMsg1", "再試一次?")
        print(ret)

    # 顯示 Messagebox
    def myMsg2():
        ret = messagebox.askyesnocancel("myMsg2", "編輯完成，是或否或取消?")
        print(ret)

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("messagebox_to_get")

    # Button 1
    btn1 = Button(root, text="安裝失敗", command=myMsg1)
    btn1.pack()

    # Button 2
    btn2 = Button(root, text="編輯完成", command=myMsg2)
    btn2.pack()

    # 執行，放在最後一行
    root.mainloop()

##==============================================================================================
## Main
##==============================================================================================

# ===============================
# Message
# ===============================

# Message 基本用法
#message_to_basic()

# ===============================
# Messagebox
# ===============================

# Messagebox 基本用法
#messagebox_to_basic()

# 取得使用者的回應
#messagebox_to_get()








