'''
視窗控件配置管理員Layout

pack - grid - place

'''

# 載入tkinter
from  tkinter import *

##==============================================================================================
## Function(pack)
##==============================================================================================

# pack -> side
# TOP : 預設，由上至下排列
# BOTTOM : 由下至上排列
# LEFT : 由左至右排列
# RIGHT : 由右至左排列

# pack基本用法
def pack_to_side():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("pack_to_side")

    # 標籤1
    lab1 = Label(root, text="lab1", bg="lightyellow")
    # 標籤2
    lab2 = Label(root, text="lab2", bg="lightgreen")
    # 標籤3
    lab3 = Label(root, text="lab3", bg="lightblue")

    # 包裝元件
    lab1.pack(side=TOP)
    # 包裝元件
    lab2.pack(side=RIGHT)
    # 包裝元件
    lab3.pack(side=LEFT)

    # 執行，放在最後一行
    root.mainloop()


# (第1種方式)pack -> anchor
def pack_to_anchor_one():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("pack_to_anchor_one")
    # 視窗大小
    root.geometry("300x180")

    # 標籤
    OKlabel = Label(root, text="OK", bg="lightblue")

    # 包裝和定位元件
    OKlabel.pack(anchor="se", side=RIGHT)

    # 執行，放在最後一行
    root.mainloop()

# (第2種方式)pack -> anchor
def pack_to_anchor_two():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("pack_to_anchor_two")
    # 視窗大小
    root.geometry("300x180")

    # OK標籤
    OKlabel = Label(root, text="OK", bg="lightblue")
    # NO標籤
    NOlabel = Label(root, text="NO", bg="lightblue")

    # 包裝和定位元件(從右開始在南方配置)
    OKlabel.pack(anchor="s", side=RIGHT, padx=5)
    # 包裝和定位元件(從右開始在東南方配置)
    NOlabel.pack(anchor="se", side=RIGHT, padx=5)

    # 執行，放在最後一行
    root.mainloop()

# pack -> fill
def pack_to_fill():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("pack_to_fill")
    # 視窗大小
    root.geometry("300x180")

    # 標籤1
    lab1 = Label(root, text="lab1", bg="lightblue")
    # 標籤2
    lab2 = Label(root, text="lab2", bg="lightblue")

    # 包裝和定位元件
    lab1.pack(fill=X)
    # 包裝和定位元件
    lab2.pack(fill=Y, side=RIGHT)

    # 執行，放在最後一行
    root.mainloop()

# pack -> expand
def pack_to_expand():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("pack_to_expand")
    # 視窗大小
    root.geometry("300x180")

    # 標籤1
    lab1 = Label(root, text="lab1", bg="lightblue")
    # 標籤2
    lab2 = Label(root, text="lab2", bg="lightblue")
    # 標籤3
    lab3 = Label(root, text="lab3", bg="lightgreen")

    # 包裝和定位元件
    lab1.pack(fill=X)
    # 包裝和定位元件
    lab2.pack(fill=Y, side=RIGHT)
    # 包裝和定位元件(填滿X、Y軸)
    lab3.pack(fill=BOTH, expand=True)

    # 執行，放在最後一行
    root.mainloop()


##==============================================================================================
## Function(grid)
##==============================================================================================

##==============================================================================================
##  |row=0,column=0| |row=0,column=1| **** |row=0,column=n|
##  |row=1,column=0| |row=1,column=1| **** |row=1,column=n|
##                      ******
##  |row=n,column=0| |row=n,column=1| **** |row=n,column=n|
##==============================================================================================

# grid 基本用法
def grid_to_base():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("grid_to_base")

    # 標籤顏色=淺黃色，標籤寬度=15
    lab1 = Label(root , text="逢甲大學" , bg="lightyellow" , width=15)
    # 標籤顏色=淺綠色，標籤寬度=15
    lab2 = Label(root, text="東海大學", bg="lightgreen", width=15)
    #標籤顏色=淺藍色，標籤寬度=15
    lab3 = Label(root, text="中興大學", bg="lightblue", width=15)

    # 分配位置
    lab1.grid(row=0, column=0)
    lab2.grid(row=1, column=1)
    lab3.grid(row=2, column=2)

    # 執行，放在最後一行
    root.mainloop()

# grid -> columnspan(未使用)
def grid_to_columnspan_not():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("grid_to_columnspan_not")

    #標籤寬度=15，加上邊框
    lab1 = Label(root , text="lab1" , width=15 , relief="raised")
    #標籤寬度=15，加上邊框
    lab2 = Label(root , text="lab2" , width=15 , relief="raised")
    #標籤寬度=15，加上邊框
    lab3 = Label(root , text="lab3" , width=15 , relief="raised")
    # 標籤寬度=15，加上邊框
    lab4 = Label(root, text="lab4", width=15, relief="raised")
    # 標籤寬度=15，加上邊框
    lab5 = Label(root, text="lab5", width=15, relief="raised")
    # 標籤寬度=15，加上邊框
    lab6 = Label(root, text="lab6", width=15, relief="raised")
    # 標籤寬度=15，加上邊框
    lab7 = Label(root, text="lab7", width=15, relief="raised")
    # 標籤寬度=15，加上邊框
    lab8 = Label(root, text="lab8", width=15, relief="raised")

    # 分配位置
    lab1.grid(row=0, column=0)
    lab2.grid(row=0, column=1)
    lab3.grid(row=0, column=2)
    lab4.grid(row=0, column=3)

    lab5.grid(row=1, column=0)
    lab6.grid(row=1, column=1)
    lab7.grid(row=1, column=2)
    lab8.grid(row=1, column=3)

    # 執行，放在最後一行
    root.mainloop()

# grid -> columnspan(使用)
def grid_to_columnspan():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("grid_to_columnspan")

    #標籤寬度=15，加上邊框
    lab1 = Label(root , text="lab1" , width=15 , relief="raised")
    #標籤寬度=15，加上邊框
    lab2 = Label(root , text="lab2" , width=15 , relief="raised")

    # 標籤3的空間被標籤2占用

    # 標籤寬度=15，加上邊框
    lab4 = Label(root, text="lab4", width=15, relief="raised")
    # 標籤寬度=15，加上邊框
    lab5 = Label(root, text="lab5", width=15, relief="raised")
    # 標籤寬度=15，加上邊框
    lab6 = Label(root, text="lab6", width=15, relief="raised")
    # 標籤寬度=15，加上邊框
    lab7 = Label(root, text="lab7", width=15, relief="raised")
    # 標籤寬度=15，加上邊框
    lab8 = Label(root, text="lab8", width=15, relief="raised")

    # 分配位置
    lab1.grid(row=0, column=0)
    # 標籤2占用2個標籤位置
    lab2.grid(row=0, column=1,columnspan=2)

    lab4.grid(row=0, column=3)

    lab5.grid(row=1, column=0)
    lab6.grid(row=1, column=1)
    lab7.grid(row=1, column=2)
    lab8.grid(row=1, column=3)

    # 執行，放在最後一行
    root.mainloop()

# grid -> rowspan(使用)
def grid_to_rowspan():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("grid_to_rowspan")

    #標籤寬度=15，加上邊框
    lab1 = Label(root , text="lab1" , width=15 , relief="raised")
    #標籤寬度=15，加上邊框
    lab2 = Label(root , text="lab2" , width=15 , relief="raised")
    # 標籤寬度=15，加上邊框
    lab3 = Label(root, text="lab3", width=15, relief="raised")

    # 標籤寬度=15，加上邊框
    lab4 = Label(root, text="lab4", width=15, relief="raised")
    # 標籤寬度=15，加上邊框
    lab5 = Label(root, text="lab5", width=15, relief="raised")

    # 標籤6的空間被標籤2占用

    # 標籤寬度=15，加上邊框
    lab7 = Label(root, text="lab7", width=15, relief="raised")
    # 標籤寬度=15，加上邊框
    lab8 = Label(root, text="lab8", width=15, relief="raised")

    # 分配位置
    lab1.grid(row=0, column=0)
    # 標籤2占用2個標籤位置
    lab2.grid(row=0, column=1,rowspan=2)
    lab3.grid(row=0, column=2)
    lab4.grid(row=0, column=3)

    lab5.grid(row=1, column=0)

    lab7.grid(row=1, column=2)
    lab8.grid(row=1, column=3)

    # 執行，放在最後一行
    root.mainloop()

# grid -> colortable
def grid_to_colortable():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("grid_to_colortable")
    # 色碼
    colors = ["red","orange","yellow"]

    # row
    r = 0

    for color in colors:
        Label(root,text=color,relief="groove",width=20).grid(row=r,column=0)
        Label(root,bg=color,relief="ridge",width=20).grid(row=r,column=1)
        r = r + 1


    # 執行，放在最後一行
    root.mainloop()

# grid -> configure
# 讓元件隨視窗大小改變
# rowconfigure(n,weight=x) : 第n列row,隨視窗改變比例為x
# columnconfigure(n,weight=x) : 第n行column,隨視窗改變比例為x
def grid_to_configure():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("grid_to_configure")

    # 第1列row,隨視窗改變比例為1
    root.rowconfigure(1,weight=1)
    # 第0行column,隨視窗改變比例為1
    root.columnconfigure(0,weight=1)

    lab1 = Label(root,text="lab1",bg="pink")
    # sticky=左右對齊
    lab1.grid(row=0,column=0,padx=5,pady=5,sticky=W+E)

    lab2 = Label(root, text="lab2", bg="lightblue")
    lab2.grid(row=0, column=1, padx=5, pady=5)

    lab3 = Label(root, text="lab3", bg="yellow")
    # sticky=頂端、底部、左右對齊
    lab3.grid(row=1, column=0,columnspan=2, padx=5, pady=5, sticky=N+S+W+E)

    # 執行，放在最後一行
    root.mainloop()



##==============================================================================================
## Function(place)
##==============================================================================================

##==============================================================================================
## 以像素來控制元件
##==============================================================================================

# place基本用法
def place_to_base():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("place_to_base")

    # 標籤顏色=淺黃色，標籤寬度=15
    lab1 = Label(root, text="逢甲大學", bg="lightyellow", width=15)
    # 標籤顏色=淺綠色，標籤寬度=15
    lab2 = Label(root, text="東海大學", bg="lightgreen", width=15)
    # 標籤顏色=淺藍色，標籤寬度=15
    lab3 = Label(root, text="中興大學", bg="lightblue", width=15)

    # 分配位置
    lab1.place(x=0, y=0)
    lab2.place(x=30, y=50)
    lab3.place(x=60, y=100)

    # 執行，放在最後一行
    root.mainloop()

# place -> 控制圖片位置、大小(絕對)
def place_to_imagesize():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("place_to_imagesize")
    # 視窗大小
    root.geometry("640x480")

    # box圖片
    image_box = PhotoImage(file="../imgfolder/box.jpg")
    lab_box = Label(root,image=image_box)
    # x=距離左上角的水平距離、y=距離左上角的垂直距離、width=圖片最大顯示的寬、height=圖片最大顯示的高
    lab_box.place(x=20,y=20,width=320,height=240)

    # link圖片
    image_link = PhotoImage(file="../imgfolder/link.png")
    lab_link = Label(root, image=image_link)
    lab_link.place(x=300, y=200, width=320, height=240)

    # 執行，放在最後一行
    root.mainloop()

# place -> 控制圖片位置、大小(相對)
def place_to_imagesize_rel():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("place_to_imagesize")
    # 視窗大小
    root.geometry("640x480")

    # box圖片
    image_box = PhotoImage(file="../imgfolder/box.jpg")
    lab_box = Label(root, image=image_box)
    # relx=圖片相對視窗的水平距離、rely=圖片相對視窗的垂直距離、relwidth=圖片相對視窗的最大顯示的寬、relheight=圖片相對視窗的最大顯示的高
    lab_box.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    # 執行，放在最後一行
    root.mainloop()
##==============================================================================================
## Main
##==============================================================================================

##==============================================================================================
### pack

# pack -> side
#pack_to_side()

# (第1種方式)pack -> anchor
#pack_to_anchor_one()

# (第2種方式)pack -> anchor
#pack_to_anchor_two()

# pack -> fill
#pack_to_fill()

# pack -> expand
#pack_to_expand()

##==============================================================================================
### grid

# grid 基本用法
#grid_to_base()

# grid -> columnspan(未使用)
#grid_to_columnspan_not()

# grid -> columnspan(使用)
#grid_to_columnspan()

# grid -> rowspan
#grid_to_rowspan()

# grid -> colortable
#grid_to_colortable()

# grid -> configure
#grid_to_configure()

##==============================================================================================
### place

# place基本用法
#place_to_base()

# place -> 控制圖片位置、大小(絕對)
#place_to_imagesize()

# place -> 控制圖片位置、大小(相對)
#place_to_imagesize_rel()








