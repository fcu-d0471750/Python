'''
選項鈕(Radio Button)、核取方塊(Check Boxes)
'''

# 載入tkinter
from tkinter import *

##==============================================================================================
## Function(Radio Button)
##==============================================================================================

# Radio Button 基本用法
def radio_to_base():
    # 印出資訊
    def printSelection():
        lab.config(text="您是 " + var.get() + "。")


    # 建立視窗，root可取其它名稱
    root = Tk()
    #  視窗標題
    root.title("radio_to_base")

    # Radio Button 的變數
    var = StringVar()
    # 預設為 尚未選擇性別
    var.set("尚未選擇性別")

    # 標籤
    lab = Label(root,text="尚未選擇性別")
    # 包裝元件
    lab.pack()

    # Radio Button 男性
    # value: 該 Radio Button 的代表值
    rbman = Radiobutton(root,text="男生",variable=var,value="男生",command=printSelection)
    # 包裝元件
    rbman.pack()

    #  Radio Button 女性
    rbwoman = Radiobutton(root, text="女生", variable=var, value="女生", command=printSelection)
    # 包裝元件
    rbwoman.pack()

    # 執行，放在最後一行
    root.mainloop()

# 多選項
def radio_to_multibutton():
    # 印出資訊
    def printSelection():
        print(cites[var.get()])

    # 建立視窗，root可取其它名稱
    root = Tk()
    #  視窗標題
    root.title("radio_to_multibutton")
    # 城市
    cites = {0:"東京",1:"紐約",2:"巴黎",3:"倫敦",4:"台中"}

    # Radio Button 的變數
    var = IntVar()
    # 預設為 0
    var.set(0)

    # 標籤
    lab = Label(root,text="選擇最喜歡的城市")
    # 包裝元件
    lab.pack()

    # 建立 Radio Button
    for val,cite in cites.items():
        Radiobutton(root,text=cite,variable=var,value=val,command=printSelection).pack()

    # 執行，放在最後一行
    root.mainloop()

# Radio Button 基本用法(box外觀)
def radio_to_boxbase():
    # 印出資訊
    def printSelection():
        lab.config(text="您是 " + var.get() + "。")


    # 建立視窗，root可取其它名稱
    root = Tk()
    #  視窗標題
    root.title("radio_to_boxbase")

    # Radio Button 的變數
    var = StringVar()
    # 預設為 尚未選擇性別
    var.set("尚未選擇性別")

    # 標籤
    lab = Label(root,text="尚未選擇性別")
    # 包裝元件
    lab.pack()

    # Radio Button 男性
    # indicatoron : Radio Button的外觀 0為box、1為圓形
    rbman = Radiobutton(root,text="男生",variable=var,value="男生",indicatoron=0,command=printSelection)
    # 包裝元件
    rbman.pack()

    #  Radio Button 女性
    rbwoman = Radiobutton(root, text="女生", variable=var, value="女生",indicatoron=0, command=printSelection)
    # 包裝元件
    rbwoman.pack()

    # 執行，放在最後一行
    root.mainloop()

# Radio Button 含 image
def radio_to_image():
    # 印出資訊
    def printSelection():
        lab.config(text="您是 " + var.get() + "。")

    # 建立視窗，root可取其它名稱
    root = Tk()
    #  視窗標題
    root.title("radio_to_image")

    # image
    imgstar = PhotoImage(file="../imgfolder/star.png")
    # image
    imgsun = PhotoImage(file="../imgfolder/sun.png")

    # Radio Button 的變數
    var = StringVar()
    # 預設為 0
    var.set(0)

    # 標籤
    lab = Label(root, text="尚未選擇")
    # 包裝元件
    lab.pack()

    #  Radio Button 星星
    rbstar = Radiobutton(root,image=imgstar,text="星星",variable=var,value="星星",command=printSelection)
    rbstar.pack()

    #  Radio Button 太陽
    rbsun = Radiobutton(root, image=imgsun, text="太陽", variable=var, value="太陽", command=printSelection)
    rbsun.pack()

    # 執行，放在最後一行
    root.mainloop()

##==============================================================================================
## Function(Check Boxes)
##==============================================================================================

# Check Boxes 基本用法
def check_to_base():
    # 印出資訊
    def printSelection():
        for i in checkboxes:
            # 如果被選取
            if checkboxes[i].get() == True:
                print(cites[i])

    # 建立視窗，root可取其它名稱
    root = Tk()
    #  視窗標題
    root.title("check_to_base")
    # 城市
    cites = {0: "東京", 1: "紐約", 2: "巴黎", 3: "倫敦", 4: "台中"}
    # 被選取的城市存放
    checkboxes = {}

    # 標籤
    lab = Label(root, text="選擇最喜歡的城市")
    # 包裝元件
    lab.grid(row=0)

    # 建立 Radio Button
    for  i in range(len(cites)):
        checkboxes[i] = BooleanVar()
        Checkbutton(root, text=cites[i], variable=checkboxes[i]).grid(row=i+1,sticky=W)

    # 確定 Button
    btn = Button(root,text="確定",command=printSelection)
    btn.grid(row=i+2)

    # 執行，放在最後一行
    root.mainloop()

##==============================================================================================
## Function(統合)
##==============================================================================================

# 簡單編輯程式
# 有1個Entry，3個 Radio Button，1個 Button，1個 Check Box
# Entry : 輸入文字
# Radio Button_01 : 選取 Entry 的文字
# Radio Button_02 : 取消選取 Entry 的文字
# Radio Button_03 : 清空 Entry 的文字
# Button : 關閉程式
# Check Box : 唯獨模式，無法更改 Entry 的文字
def editor():
    # 選取
    def selAll():
        entry.select_range(0,END)
    # 取消選取
    def deselAll():
        entry.select_clear()
    # 清空
    def clearAll():
        entry.delete(0,END)
    # 唯讀
    def readonly():
        if (chvar.get() == True):
            entry.config(state=DISABLED)
        else:
            entry.config(state=NORMAL)

    # 建立視窗，root可取其它名稱
    root = Tk()
    #  視窗標題
    root.title("editor")

    # ==============================================
    # 以下 row=0 建立 Entry
    # ==============================================
    entry = Entry(root)
    # 包裝元件
    entry.grid(row=0,column=0,columnspan=4,padx=5,pady=5,sticky=W)

    #==============================================
    #  以下 row=1 建立 Radio Button、Button
    # ==============================================
    # Radio Button 的變數
    rbvar = IntVar()
    # 預設為 0
    rbvar.set(0)

    # Radio Button 選取
    rbSel = Radiobutton(root, text="選取", variable=rbvar, value=1, indicatoron=0, command=selAll)
    # 包裝元件
    rbSel.grid(row=1,column=0,padx=5,pady=5,sticky=W)

    # Radio Button 取消選取
    rbDesel = Radiobutton(root, text="取消選取", variable=rbvar, value=2, indicatoron=0, command=deselAll)
    # 包裝元件
    rbDesel.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    # Radio Button 清空
    rbClr = Radiobutton(root, text="清空", variable=rbvar, value=3, indicatoron=0, command=clearAll)
    # 包裝元件
    rbClr.grid(row=1, column=2, padx=5, pady=5, sticky=W)

    # Button 結束
    btnQuit = Button(root, text="結束" ,command=root.destroy)
    # 包裝元件
    btnQuit.grid(row=1, column=3, padx=5, pady=5, sticky=W)

    # ==============================================
    #  以下 row=2 建立 CheckBox
    # ==============================================
    # CheckBox 的變數
    chvar = BooleanVar()
    # 預設為 False
    chvar.set(False)

    # CheckBox 唯讀
    chkReadonly = Checkbutton(root,text="唯讀",variable=chvar,command=readonly)
    # 包裝元件
    chkReadonly.grid(row=2,column=0)

    # 執行，放在最後一行
    root.mainloop()
##==============================================================================================
##==============================================================================================
## Main
##==============================================================================================

# Radio Button 基本用法
#radio_to_base()

# 多選項
#radio_to_multibutton()

# Radio Button 基本用法(box外觀)
#radio_to_boxbase()

# Radio Button 含 image
#radio_to_image()


# Check Boxes 基本用法
#check_to_base()

# 簡單編輯程式
#editor()