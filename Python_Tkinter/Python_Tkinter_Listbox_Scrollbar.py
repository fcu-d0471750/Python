'''
表單(Listbox)
顯示一系列選項的元件，使用者可以單個項目、多個項目選擇。

卷軸(Scrollbar)
當 Listbox 的項目太多時，有些項目無法顯示，透過 Scrollbar 顯示這些項目。
'''


# 載入 tkinter
from tkinter import *


##==============================================================================================
## Function(Listbox)
##==============================================================================================

# Listbox 基本用法
def listbox_to_basic():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("listbox_to_basic")

    # Listbox 1
    lb1 = Listbox(root)
    lb1.pack(side=LEFT,padx=5,pady=10)

    # Listbox 2
    lb2 = Listbox(root,height=5,relief="raised")
    lb2.pack(anchor=N,side=LEFT, padx=5, pady=10)

    # 執行，放在最後一行
    root.mainloop()

# Listbox 建立項目
def listbox_to_insert():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("listbox_to_insert")

    # Listbox
    lb = Listbox(root)


    # 項目
    # insert(index,element)，END=放在最後面加入，如果都為END，則依先後排序
    lb.insert(END,"Banana")
    lb.insert(END,"Watermelon")
    lb.insert(END, "Apple")

    # 包裝
    lb.pack(side=LEFT, padx=5, pady=10)

    # 執行，放在最後一行
    root.mainloop()

# Listbox 取得項目
def listbox_to_curselection():
    # 印出選取的項目
    def callback():
        # 取得選取的項目的index
        indexs = lb.curselection()
        # 印出項目
        for i in indexs:
            print(lb.get(i))

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("listbox_to_curselection")

    # listbox項目
    fruits = ["Apple","Banana","Watermelon","Orange","Grapes","Mango"]

    # Listbox
    lb = Listbox(root,selectmode=MULTIPLE)

    # 建立項目
    for fruit in fruits:
        lb.insert(END,fruit)

    # 包裝
    lb.pack(padx=5, pady=10)

    # Button
    btn = Button(root,text="Print",command=callback)
    btn.pack(pady=5)

    # 執行，放在最後一行
    root.mainloop()

# Listbox 單一虛擬綁定
# 以前未使用虛擬綁定，是使用<<Double-Buton-1>>，連點兩下項目印出。
def listbox_to_singlebind():
    # 印出選取的項目
    def itemSelected(event):
       # 取得lb
       obj = event.widget
       # 取得索引
       index = obj.curselection()
       # 設定lab
       var.set(obj.get(index))

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("listbox_to_singlebind")

    # listbox項目
    fruits = ["Apple","Banana","Watermelon","Orange","Grapes","Mango"]

    # Label
    var = StringVar()
    lab = Label(root,text= " ",textvariable=var)
    lab.pack(pady=5)

    # Listbox
    lb = Listbox(root)
    # 建立項目
    for fruit in fruits:
        lb.insert(END,fruit)
    # 虛擬綁定
    lb.bind("<<ListboxSelect>>",itemSelected)
    # 包裝
    lb.pack(padx=5, pady=10)

    # 執行，放在最後一行
    root.mainloop()

# Listbox 多重虛擬綁定
# 將Listbox的 selectmode 改成 EXTENDED
def listbox_to_multibind():
    # 印出選取的項目
    def itemSelected(event):
       # 取得lb
       obj = event.widget
       # 取得索引
       indexs = obj.curselection()
       # 印出項目
       for index in indexs:
           print(obj.get(index))
       # 分隔線
       print("---------")

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("listbox_to_multibind")

    # listbox項目
    fruits = ["Apple","Banana","Watermelon","Orange","Grapes","Mango"]

    # Label
    var = StringVar()
    lab = Label(root,text= " ",textvariable=var)
    lab.pack(pady=5)

    # Listbox
    lb = Listbox(root,selectmode=EXTENDED)
    # 建立項目
    for fruit in fruits:
        lb.insert(END,fruit)
    # 虛擬綁定
    lb.bind("<<ListboxSelect>>",itemSelected)
    # 包裝
    lb.pack(padx=5, pady=10)

    # 執行，放在最後一行
    root.mainloop()

# Listbox 加入和刪除項目
def listbox_to_add_delete():
    # 加入項目
    def itemAdd():
        # 讀取Entry的項目
        varAdd = entry.get()
        # 沒有項目，則不執行
        if (len(varAdd.strip()) == 0):
            return
        # 如果有，加入到Listbox
        lb.insert(END,varAdd)
        # 清空Entry
        entry.delete(0,END)

     # 刪除項目
    def itemDelete():
        # 取得選擇的項目索引
        index = lb.curselection()
        # 沒有項目，則不執行
        if(len(index)==0):
            return
        # 刪除項目
        lb.delete(index)

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("listbox_to_add_delete")

    # Listbox
    lb = Listbox(root,selectmode=MULTIPLE)
    # 包裝
    lb.grid(row=1,column=0,padx=5, pady=10)

    # Entry
    entry = Entry(root)
    entry.grid(row=0,column=0,padx=5,pady=5)

    # Button(增加)
    btnAdd = Button(root,text="增加",width=10,command=itemAdd)
    btnAdd.grid(row=0,column=1,padx=5,pady=5)

    # Button(刪除)
    btnDel = Button(root, text="刪除", width=10, command=itemDelete)
    btnDel.grid(row=0, column=2, padx=5, pady=5)

    # 執行，放在最後一行
    root.mainloop()

# Listbox 項目排序
def listbox_to_sorted():
    # 排序
    def itemSorted():
        # 如果排序是由大到小
        if (var.get() == True):
            revBool = True
        #  如果排序是由小到大
        else :
            revBool = False

        # 取得項目
        listTmp = list(lb.get(0,END))
        # 排序
        sortedList = sorted(listTmp,reverse=revBool)
        # 清空Listbox原本的項目
        lb.delete(0,END)
        # 將排序後的內容放入Listbox
        for item in sortedList:
            lb.insert(END,item)

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("listbox_to_sorted")

    # listbox項目
    fruits = ["Apple","Banana","Watermelon","Orange","Grapes","Mango"]

    # Listbox
    lb = Listbox(root)

    # 建立項目
    for fruit in fruits:
        lb.insert(END,fruit)

    # 包裝
    lb.pack(padx=5, pady=10)

    # Button(排序)
    btn = Button(root,text="排序",command=itemSorted)
    btn.pack(side=LEFT,padx=10,pady=5)

    # CheckButton(排序)
    var = BooleanVar()
    cb = Checkbutton(root,text="由大到小排序",variable=var)
    cb.pack(side=LEFT)

    # 執行，放在最後一行
    root.mainloop()

# Listbox 拖拉項目
def listbox_to_nearest():
    # 選擇項目
    def getIndex(event):
        # 取得離y坐標最近的index
        lb.index = lb.nearest(event.y)

    # 拖拉項目
    def dragJob(event):
        # 新index位置，預設原本項目的index
        newindex = lb.nearest(event.y)
        # 往上拖拉
        if newindex < lb.index:
            # 取得新位置
            x = lb.get(newindex)
            # 刪除新位置的內容
            lb.delete(newindex)
            # 放回原本新位置的內容
            lb.insert(newindex+1,x)
            # 項目的新 index
            lb.index = newindex
        # 往下拖拉
        elif newindex > lb.index:
            # 取得新位置
            x = lb.get(newindex)
            # 刪除新位置的內容
            lb.delete(newindex)
            # 放回原本新位置的內容
            lb.insert(newindex - 1, x)
            # 項目的新 index
            lb.index = newindex

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("listbox_to_nearest")

    # listbox項目
    fruits = ["Apple","Banana","Watermelon","Orange","Grapes","Mango"]

    # Listbox
    lb = Listbox(root)
    # 建立項目
    for fruit in fruits:
        lb.insert(END,fruit)
        # 綁定 選擇項目
        lb.bind("<Button-1>",getIndex)
        # 綁定 拖拉項目
        lb.bind("<B1-Motion>", dragJob)

    # 包裝
    lb.pack(padx=5, pady=10)



    # 執行，放在最後一行
    root.mainloop()

##==============================================================================================
## Function(Scrollbar)
##==============================================================================================

# Scrollbar 基本用法
def scrollbar_to_basic():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("scrollbar_to_basic")

    # Scrollbar
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT,fill=Y)

    # Listbox
    # yscrollcommand = Listbox 和 Scrollbar 連結
    lb = Listbox(root,yscrollcommand=scrollbar.set)
    # 建立 50 筆項目
    for i in range(50):
        lb.insert(END,"Line" + str(i))
    # 包裝
    lb.pack(side=LEFT,fill=BOTH,expand=True)

    # 當移動Scrollbar時，執行 lb.yview
    scrollbar.config(command=lb.yview)

    # 執行，放在最後一行
    root.mainloop()

##==============================================================================================
## Main
##==============================================================================================

# ===============================
# Listbox
# ===============================

# Listbox基本用法
#listbox_to_basic()

# Listbox建立項目
#listbox_to_insert()

# Listbox 取得項目
#listbox_to_curselection()

# Listbox 單一虛擬綁定
#listbox_to_singlebind()

# Listbox 多重虛擬綁定
#listbox_to_multibind()

# Listbox 加入和刪除項目
#listbox_to_add_delete()

# Listbox 項目排序
#listbox_to_sorted()

# Listbox 拖拉項目
#listbox_to_nearest()

# ===============================
# Scrollbar
# ===============================

# Scrollbar 基本用法
#scrollbar_to_basic()




































































