'''
變數類別 Variable Classes
'''

# 載入tkinter
from tkinter import *

##==============================================================================================
## Function
##==============================================================================================

# Variable Classes 基本用法
# 按下Button，顯示的文字變成不顯示，不顯示的文字變成顯示
def var_to_base():
    # Button Function
    def btn_hit():
        global msg_on
        if msg_on == False:
            # 顯示文字
            msg_on = True
            # 設定文字
            x.set("I like Tkinter.")
        else:
            # 不顯示文字
            msg_on = False
            # 設定文字為空
            x.set(" ")

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("var_to_base")


    # Label的變數內容
    x = StringVar()

    # Label
    lab = Label(root,textvariable=x,fg="blue",bg="lightyellow",width=25,height=2)
    # Button
    btn = Button(root,text="Click",command=btn_hit)

    # 包裝元件
    lab.pack()
    btn.pack()

    # 執行，放在最後一行
    root.mainloop()

# Variable Classes trace() w模式
def var_to_trace_w():
    def callback(*args):
        # Python shell輸出
        print("data changed : " , x.get())

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("var_to_trace_w")

    # Entry的變數內容
    x = StringVar()

    # Entry，變數內容為 x
    entry = Entry(root,textvariable=x)
    # 包裝元件
    entry.pack(padx=10,pady=5)

    # 當Entry的內容發生改變，執行callback
    # w=write縮寫
    # 當有寫入動作，執行callback
    x.trace("w",callback)

    # 執行，放在最後一行
    root.mainloop()

# Variable Classes trace() w模式 with Label
def var_to_trace_w_with_label():
    def callback(*args):
        # 設定label內容
        xl.set(x.get())
        # Python shell輸出
        print("data changed : " , x.get())

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("var_to_trace_w_with_label")

    # Entry的變數內容
    x = StringVar()
    # Label的變數內容
    xl = StringVar()

    # Entry，變數內容為 x
    entry = Entry(root,textvariable=x)
    # 包裝元件
    entry.pack(padx=10,pady=5)

    # Label，變數內容為 xl
    lab = Label(root,textvariable=xl)
    # 預設
    xl.set("同步顯示")
    # 包裝元件
    lab.pack(padx=10,pady=5)

    # 當Entry的內容發生改變，執行callback
    # w=write縮寫
    # 當有寫入動作，執行callback
    x.trace("w",callback)

    # 執行，放在最後一行
    root.mainloop()

# Variable Classes trace() r模式
def var_to_trace_r():
    # 內容被修改時執行
    def callbackW(*args):
        xl.set(xe.get())

    # 內容被修改時執行
    def callbackR(*args):
        print("資料被讀取!")

    # 讀取資料
    def hit():
        print("讀取資料 : ",xe.get())

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("var_to_trace_r")

    # Entry的變數內容
    xe = StringVar()
    # Label的變數內容
    xl = StringVar()

    # Entry，變數內容為 xe
    entry = Entry(root, textvariable=xe)
    # 包裝元件
    entry.pack(padx=10, pady=5)

    # Label，變數內容為 xl
    lab = Label(root, textvariable=xl)
    # 預設
    xl.set("同步顯示")
    # 包裝元件
    lab.pack(padx=10, pady=5)

    # 讀取Button
    btn = Button(root,text="讀取",command=hit)
    # 包裝元件
    btn.pack(pady=5)

    # entry被修改時
    xe.trace("w",callbackW)
    # entry被讀取時
    xe.trace("r", callbackR)

    # 執行，放在最後一行
    root.mainloop()

# Variable Classes args
# 說明args
# args代替傳遞三個參數，name-tk變數名稱，index-索引，mode-模式
def var_to_trace_args():
    # 內容被修改時執行
    def callbackW(name,index,mode):
        xl.set(xe.get())
        # 印出參數
        print("name=%r,index=%r,mode=%r"%(name,index,mode))


    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("var_to_trace_args")

    # Entry的變數內容
    xe = StringVar()
    # Label的變數內容
    xl = StringVar()

    # Entry，變數內容為 xe
    entry = Entry(root, textvariable=xe)
    # 包裝元件
    entry.pack(padx=10, pady=5)

    # Label，變數內容為 xl
    lab = Label(root, textvariable=xl)
    # 預設
    xl.set("同步顯示")
    # 包裝元件
    lab.pack(padx=10, pady=5)

    # entry被修改時
    xe.trace("w", callbackW)

    # 執行，放在最後一行
    root.mainloop()

# Variable Classes Counter
def var_to_counter():
    # 計算結果
    def calculate():
        result = eval(equ.get())
        equ.set(equ.get() + "=\n" + str(result))

    # 更新顯示區
    def show(buttonString):
        content = equ.get()
        if content == "0":
            content = ""
        equ.set(content + buttonString)

    # 刪除前一個字元
    def backspace():
        equ.set(str(equ.get()[:-1]))

    # 清空顯示區，設置0
    def clear():
        equ.set("0")

     # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("var_to_counter")

    # 變數內容
    equ = StringVar()
    # 預設顯示0
    equ.set("0")

    # 設計顯示區
    lab = Label(root,width=25,height=2,relief="raised",anchor=SE,textvariable=equ)
    # 包裝元件
    lab.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

    # 清空顯示區 Button
    btn_clear = Button(root,text="C",fg="blue",width=5,command=clear)
    # 包裝元件
    btn_clear.grid(row=1,column=0)

    # 第一列數字鍵
    btn_del=Button(root,text="DEL",width=5,command=backspace)
    btn_del.grid(row=1,column=1)
    btn_pre = Button(root, text="%", width=5, command=lambda :show("%"))
    btn_pre.grid(row=1, column=2)
    btn_div = Button(root, text="/", width=5, command=lambda: show("/"))
    btn_div.grid(row=1, column=3)

    # 第二列數字鍵
    btn_7 = Button(root, text="7", width=5, command=lambda: show("7"))
    btn_7.grid(row=2, column=0)
    btn_8 = Button(root, text="8", width=5, command=lambda: show("8"))
    btn_8.grid(row=2, column=1)
    btn_9 = Button(root, text="9", width=5, command=lambda: show("9"))
    btn_9.grid(row=2, column=2)
    btn_mul = Button(root, text="*", width=5, command=lambda: show("*"))
    btn_mul.grid(row=2, column=3)

    # 第三列數字鍵
    btn_4 = Button(root, text="4", width=5, command=lambda: show("4"))
    btn_4.grid(row=3, column=0)
    btn_5 = Button(root, text="5", width=5, command=lambda: show("5"))
    btn_5.grid(row=3, column=1)
    btn_6 = Button(root, text="6", width=5, command=lambda: show("6"))
    btn_6.grid(row=3, column=2)
    btn_minus = Button(root, text="-", width=5, command=lambda: show("-"))
    btn_minus.grid(row=3, column=3)

    # 第四列數字鍵
    btn_1 = Button(root, text="1", width=5, command=lambda: show("1"))
    btn_1.grid(row=4, column=0)
    btn_2 = Button(root, text="2", width=5, command=lambda: show("2"))
    btn_2.grid(row=4, column=1)
    btn_3 = Button(root, text="3", width=5, command=lambda: show("3"))
    btn_3.grid(row=4, column=2)
    btn_add = Button(root, text="+", width=5, command=lambda: show("+"))
    btn_add.grid(row=4, column=3)

    # 第五列數字鍵
    btn_0 = Button(root, text="0", width=12, command=lambda: show("0"))
    btn_0.grid(row=5, column=0,columnspan=2)
    btn_p = Button(root, text=".", width=5, command=lambda: show("."))
    btn_p.grid(row=5, column=2)
    btn_cal = Button(root, text="=", width=5, command=lambda: calculate())
    btn_cal.grid(row=5, column=3)

    # 執行，放在最後一行
    root.mainloop()

# 貸款程式設計
def var_to_pay():
    # 計算結果
    def cal():
        monthrate = float(rateVar.get()) / (12*100)
        molecules = float(loanVar.get()) * monthrate
        denominator = 1 - (1/(1+monthrate)) ** (int(yearVar.get())*12 )
        monthlypay = int(molecules / denominator)
        monthlypayVar.set(monthlypay)
        totalpay = monthlypay * int(yearVar.get()) * 12
        totalpayVar.set(totalpay)

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("var_to_pay")

    lab_yearrate = Label(root,text="貸款年利率")
    lab_yearrate.grid(row=1,column=1,sticky=W)
    lab_year = Label(root, text="貸款年數")
    lab_year.grid(row=2, column=1, sticky=W)
    lab_total = Label(root, text="貸款金額")
    lab_total.grid(row=3, column=1, sticky=W)
    lab_mpay = Label(root, text="月付款金額")
    lab_mpay.grid(row=4, column=1, sticky=W)
    lab_tpay = Label(root, text="總付款金額")
    lab_tpay.grid(row=5, column=1, sticky=W)

    # 貸款年利率
    rateVar = StringVar()
    # Entry，貸款年利率
    entry_rateVar = Entry(root,textvariable=rateVar,justify=RIGHT)
    entry_rateVar.grid(row=1,column=2,padx=3)

    # 貸款年數
    yearVar = StringVar()
    # Entry，貸款年數
    entry_yearVar = Entry(root,textvariable=yearVar,justify=RIGHT)
    entry_yearVar.grid(row=2,column=2,padx=3)

    # 貸款金額
    loanVar = StringVar()
    # Entry，貸款金額
    entry_loanVar = Entry(root, textvariable=loanVar, justify=RIGHT)
    entry_loanVar.grid(row=3, column=2, padx=3)

    # 月付總金額
    monthlypayVar = StringVar()
    # Label，月付總金額
    label_monthlypayVar = Label(root,textvariable=monthlypayVar)
    label_monthlypayVar.grid(row=4, column=2,sticky=E, padx=3)

    # 總付總金額
    totalpayVar = StringVar()
    # Label，總付總金額
    label_totalpayVar = Label(root, textvariable=totalpayVar)
    label_totalpayVar.grid(row=5, column=2, sticky=E, padx=3)

    # 計算Button
    btn_cal = Button(root,text="計算貸款金額",command=cal)
    btn_cal.grid(row=6, column=2, sticky=E, padx=3, pady=3)

    # 執行，放在最後一行
    root.mainloop()
##==============================================================================================
## Main
##==============================================================================================

# Variable Classes 基本用法
# 預設False
# msg_on = False
# var_to_base()

# Variable Classes trace() w模式
# var_to_trace_w()

# Variable Classes trace() w模式 with Label
# var_to_trace_w_with_label()

# Variable Classes trace() r模式
# var_to_trace_r()

# Variable Classes args
# var_to_trace_args()

# Variable Classes Counter
# var_to_counter()

# 貸款程式設計
# var_to_pay()










