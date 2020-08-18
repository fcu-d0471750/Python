'''
數值卷軸(Scale)
自訂格(Spinbox)
'''

# 載入tkinter
from tkinter import *
# 載入顏色對話方塊
from tkinter.colorchooser import *

##==============================================================================================
## Function(Scale)
##==============================================================================================

# Scale 基本用法
def scale_to_base():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("scale_to_base")

    # slide1
    # from_ = 最小值，to = 最大值
    slide1 = Scale(root,from_=0,to=10)
    slide1.pack()

    # slide2
    slide2 = Scale(root,from_=0,to=20,orient=HORIZONTAL)
    slide2.pack()


    # 執行，放在最後一行
    root.mainloop()

# Scale 多個參數
def scale_to_multi():
    # 印出資訊
    def printinfo(source):
        print("現在數值: %d" %(slide.get()))

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("scale_to_multi")

    # slide
    # length = 長度，from_ = 最小值，to = 最大值，troughcolor，槽的顏色，tickinterval = 刻度，label = Scale標籤，orient = 方向
    slide = Scale(root,length=300,from_=0,to=20,troughcolor="yellow",tickinterval=2,label="My Scale",orient=HORIZONTAL,command=printinfo)
    slide.pack()



    # 執行，放在最後一行
    root.mainloop()

# Scale 改變背景顏色
def scale_to_bgcolor():
    # 改變背景顏色
    def bgupdate(source):
        # 讀取 red 值
        red = redslide.get()
        # 讀取 green 值
        green = greenslide.get()
        # 讀取 blue 值
        blue = blueslide.get()
        # 印出 RGB 值
        print("Red: %d , Green: %d , Blue: %d" %(red,green,blue))

        # 轉成16進位
        mycolor = "#%02x%02x%02x" %(red,green,blue)
        # 改變背景顏色
        root.config(bg=mycolor)

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("scale_to_bgcolor")
    # 視窗大小
    root.geometry("360x240")

    # redslide
    redslide = Scale(root, from_=0, to=255,label="red", command=bgupdate)
    redslide.grid(row=0,column=0)
    # greenslide
    greenslide = Scale(root, from_=0, to=255, label="green", command=bgupdate)
    greenslide.grid(row=0, column=1)
    # blueslide
    blueslide = Scale(root, from_=0, to=255, label="blue", command=bgupdate)
    blueslide.grid(row=0, column=2)

    # 執行，放在最後一行
    root.mainloop()

# Scale 改變背景顏色(使用對話方塊)
def scale_to_askcolor():
    # 改變背景顏色
    def bgupdate():
        # 呼叫對話方塊
        mycolor = askcolor()
        # 改變背景顏色
        root.config(bg=mycolor[1])

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("scale_to_askcolor")
    # 視窗大小
    root.geometry("360x240")

   # Button
    btn = Button(root,text = "Select Color" , command=bgupdate)
    btn.pack(pady=5)

    # 執行，放在最後一行
    root.mainloop()

##==============================================================================================
## Function(Spinbox)
##==============================================================================================

# Spinbox基本用法
def spinbox_to_base():
    # 印出資訊
    def printinfo():
        print(spin.get())

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("spinbox_to_base")

    # Spinbox
    # from_ = 最小值，to = 最大值，increment = 每次增加/減少的量
    spin = Spinbox(root,from_=0,to=30,increment=2,command = printinfo)
    spin.pack()


    # 執行，放在最後一行
    root.mainloop()

# Spinbox 使用list
def spinbox_to_list():
    # 印出資訊
    def printinfo():
        print(spin.get())

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("spinbox_to_list")

    # list
    inidata = [10,38,"上海",101]

    # Spinbox
    # values = 預設值
    spin = Spinbox(root,values=inidata,command = printinfo)
    spin.pack()


    # 執行，放在最後一行
    root.mainloop()

##==============================================================================================
## Main
##==============================================================================================

# ===============================
# Scale
# ===============================

# Scale基本用法
#scale_to_base()

# Scale多個參數
#scale_to_multi()

# Scale 改變背景顏色
#scale_to_bgcolor()

# Scale 改變背景顏色(使用對話方塊)
#scale_to_askcolor()


# ===============================
# Spinbox
# ===============================

# Spinbox基本用法
#spinbox_to_base()

# Spinbox 使用list
#spinbox_to_list()










































































