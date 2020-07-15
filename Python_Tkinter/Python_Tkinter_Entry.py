'''
文字方塊 Entry
'''

# 載入tkinter
from tkinter import *



##==============================================================================================
## Function
##==============================================================================================

# Entry 基本用法
def entry_to_base():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("entry_to_base")

    # 姓名標籤
    lab_name = Label(root,text="Name")
    # 地址標籤
    lab_address = Label(root, text="Address")
    # 姓名文字方塊
    entry_name = Entry(root)
    # 地址標籤
    entry_address = Entry(root)

    # 包裝元件
    lab_name.grid(row=0)
    lab_address.grid(row=1)
    entry_name.grid(row=0,column=1)
    entry_address.grid(row=1,column=1)

    # 執行，放在最後一行
    root.mainloop()

# Entry 使用 參數show隱藏輸入字元
def entry_to_show():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("entry_to_show")

    # 帳號標籤
    lab_account = Label(root, text="Account")
    # 密碼標籤
    lab_password = Label(root, text="Password")
    # 帳號文字方塊
    entry_account = Entry(root)
    # 密碼標籤(show="*"，輸入字元用'*'代替)
    entry_password = Entry(root,show="*")

    # 包裝元件
    lab_account.grid(row=0)
    lab_password.grid(row=1)
    entry_account.grid(row=0, column=1)
    entry_password.grid(row=1, column=1)

    # 執行，放在最後一行
    root.mainloop()

# Entry 建立一個登入畫面
def entry_to_login():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("entry_to_login")


    # Logo 訊息
    msg = "歡迎進入系統，請輸入"
    # Logo 圖片
    logophoto = PhotoImage(file="../imgfolder/sun.png")
    # Logo
    logo = Label(root,image=logophoto,text=msg,compound=BOTTOM)

    # 帳號標籤
    lab_account = Label(root, text="Account")
    # 密碼標籤
    lab_password = Label(root, text="Password")

    # 帳號文字方塊
    entry_account = Entry(root)
    # 密碼標籤(show="*"，輸入字元用'*'代替)
    entry_password = Entry(root, show="*")

    # 包裝元件
    logo.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
    lab_account.grid(row=1)
    lab_password.grid(row=2)
    entry_account.grid(row=1, column=1)
    entry_password.grid(row=2, column=1)

    # 執行，放在最後一行
    root.mainloop()

# Entry get()用法
# get():取得Entry裡的輸入資料
def entry_to_get():

    # 印出訊息
    def printinfo():
        print("Account: %s\nPassword: %s" %(entry_account.get(),entry_password.get()))

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("entry_to_get")

    # Logo 訊息
    msg = "歡迎進入系統，請輸入"
    # Logo 圖片
    logophoto = PhotoImage(file="../imgfolder/sun.png")
    # Logo
    logo = Label(root, image=logophoto, text=msg, compound=BOTTOM)

    # 帳號標籤
    lab_account = Label(root, text="Account")
    # 密碼標籤
    lab_password = Label(root, text="Password")

    # 帳號文字方塊
    entry_account = Entry(root)
    # 密碼標籤(show="*"，輸入字元用'*'代替)
    entry_password = Entry(root, show="*")

    # 包裝元件
    logo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    lab_account.grid(row=1)
    lab_password.grid(row=2)
    entry_account.grid(row=1, column=1)
    entry_password.grid(row=2, column=1)

    #加入Login和 Quit Button
    # Login
    btn_login = Button(root,text="Login",command=printinfo)
    # Quit
    btn_quit = Button(root, text="Quit", command=root.quit)
    # 包裝元件
    btn_login.grid(row=3,column=0,sticky=W,pady=5)
    btn_quit.grid(row=3, column=1, sticky=W, pady=5)

    # 執行，放在最後一行
    root.mainloop()

# Entry insert()用法
# insert(index,s):Entry裡預設文字
def entry_to_insert():
    # 印出訊息
    def printinfo():
        print("Account: %s\nPassword: %s" % (entry_account.get(), entry_password.get()))

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("entry_to_insert")

    # Logo 訊息
    msg = "歡迎進入系統，請輸入"
    # Logo 圖片
    logophoto = PhotoImage(file="../imgfolder/sun.png")
    # Logo
    logo = Label(root, image=logophoto, text=msg, compound=BOTTOM)

    # 帳號標籤
    lab_account = Label(root, text="Account")
    # 密碼標籤
    lab_password = Label(root, text="Password")

    # 帳號文字方塊
    entry_account = Entry(root)
    # 預設為Test
    entry_account.insert(0,"Acc")
    # 密碼標籤(show="*"，輸入字元用'*'代替)
    entry_password = Entry(root, show="*")
    # 預設為Test
    entry_password.insert(0, "Pwd")

    # 包裝元件
    logo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    lab_account.grid(row=1)
    lab_password.grid(row=2)
    entry_account.grid(row=1, column=1)
    entry_password.grid(row=2, column=1)

    # 加入Login和 Quit Button
    # Login
    btn_login = Button(root, text="Login", command=printinfo)
    # Quit
    btn_quit = Button(root, text="Quit", command=root.quit)
    # 包裝元件
    btn_login.grid(row=3, column=0, sticky=W, pady=5)
    btn_quit.grid(row=3, column=1, sticky=W, pady=5)

    # 執行，放在最後一行
    root.mainloop()

# Entry delete()用法
# delete(first,last=None)，刪除 first~last-1 的字元
# delete(0,END)，刪除 整個字元
def entry_to_delete():
    # 印出訊息
    def printinfo():
        print("Account: %s\nPassword: %s" % (entry_account.get(), entry_password.get()))
        # 清空 entry_account
        entry_account.delete(0,END)
        # 清空 entry_password
        entry_password.delete(0,END)

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("entry_to_delete")

    # Logo 訊息
    msg = "歡迎進入系統，請輸入"
    # Logo 圖片
    logophoto = PhotoImage(file="../imgfolder/sun.png")
    # Logo
    logo = Label(root, image=logophoto, text=msg, compound=BOTTOM)

    # 帳號標籤
    lab_account = Label(root, text="Account")
    # 密碼標籤
    lab_password = Label(root, text="Password")

    # 帳號文字方塊
    entry_account = Entry(root)
    # 密碼標籤(show="*"，輸入字元用'*'代替)
    entry_password = Entry(root, show="*")

    # 包裝元件
    logo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    lab_account.grid(row=1)
    lab_password.grid(row=2)
    entry_account.grid(row=1, column=1)
    entry_password.grid(row=2, column=1)

    # 加入Login和 Quit Button
    # Login
    btn_login = Button(root, text="Login", command=printinfo)
    # Quit
    btn_quit = Button(root, text="Quit", command=root.quit)
    # 包裝元件
    btn_login.grid(row=3, column=0, sticky=W, pady=5)
    btn_quit.grid(row=3, column=1, sticky=W, pady=5)

    # 執行，放在最後一行
    root.mainloop()

# Entry eval()用法
# eval(expression):python內建的數學算式，可將數學算式計算結果回傳答案
# result = eval(expression)，expression:是字串
def entry_to_eval():
    # 計算結果
    def cal():
        lab_out.configure(text="結果: " + str(eval(entry_input.get())))

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("entry_to_eval")

    # 標題標籤
    lab_title = Label(root, text="請輸入數學算式")
    # 輸入方塊
    entry_input = Entry(root)
    # 輸出標籤
    lab_out = Label(root)
    # 計算按扭
    btn_cal = Button(root,text="計算",command=cal)

    # 包裝元件
    lab_title.pack()
    entry_input.pack(pady=5)
    lab_out.pack()
    btn_cal.pack(pady=5)

    # 執行，放在最後一行
    root.mainloop()
##==============================================================================================
## Main
##==============================================================================================

# Entry 基本用法
#entry_to_base()

# Entry 使用 參數show隱藏輸入字元
#entry_to_show()

# Entry 建立一個登入畫面
#entry_to_login()

# Entry get()用法
#entry_to_get()

# Entry insert()用法
#entry_to_insert()

# Entry delete()用法
#entry_to_delete()

# Entry eval()用法
#entry_to_eval()




















