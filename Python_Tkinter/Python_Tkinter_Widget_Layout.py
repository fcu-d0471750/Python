'''
視窗控件配置管理員Layout

pack - grid - place

'''

# 載入tkinter
from  tkinter import *

##==============================================================================================
## Function
##==============================================================================================

# pack -> side
# TOP : 預設，由上至下排列
# BOTTOM : 由下至上排列
# LEFT : 由左至右排列
# RIGHT : 由右至左排列
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
## Main
##==============================================================================================

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












