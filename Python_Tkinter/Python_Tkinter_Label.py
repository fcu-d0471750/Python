'''
標籤 Label
'''
# 載入tkinter
from  tkinter import *

'''
建立標籤

# 建立視窗，root可取其它名稱
root = Tk()
# 建立標籤(放在root底下)，label可取其它名稱
label = Label(root,text="I like tkinter.")
# 包裝和定位元件
label.pack()
# 執行，放在最後一行
root.mainloop()
'''

'''
標籤顏色

# 建立視窗，root可取其它名稱
root = Tk()
# 建立標籤(放在root底下,fg=文字顏色,bg=背景顏色)，label可取其它名稱
label = Label(root,text="I like tkinter.",fg="#ff0000",bg="yellow")
# 包裝和定位元件
label.pack()
# 執行，放在最後一行
root.mainloop()
'''

'''
標籤顏色、文字高度、文字寬度


# 建立視窗，root可取其它名稱
root = Tk()
# 建立標籤(放在root底下,fg=文字顏色,bg=背景顏色,height=標籤高度,width=標籤寬度)，label可取其它名稱
label = Label(root,text="I like tkinter.",fg="blue",bg="yellow",height=5,width=15)
# 包裝和定位元件
label.pack()
# 執行，放在最後一行
root.mainloop()
'''

'''
文字位置

# 建立視窗，root可取其它名稱
root = Tk()
# 建立標籤(放在root底下,fg=文字顏色,bg=背景顏色,height=標籤高度,width=標籤寬度,anchor=文字位置)，label可取其它名稱
label = Label(root,text="I like tkinter.",fg="blue",bg="yellow",height=5,width=15,anchor="nw")
# 包裝和定位元件
label.pack()
# 執行，放在最後一行
root.mainloop()
'''

'''
文字換行

# 建立視窗，root可取其它名稱
root = Tk()
# 建立標籤(放在root底下,fg=文字顏色,bg=背景顏色,height=標籤高度,width=標籤寬度,anchor=文字位置,wraplength=換行像素)，label可取其它名稱
# wraplength=40，40像素自動換行
label = Label(root,text="I like tkinter.",fg="blue",bg="yellow",height=5,width=15,anchor="nw",wraplength=40)
# 包裝和定位元件
label.pack()
# 執行，放在最後一行
root.mainloop()
'''

'''
字型


# 建立視窗，root可取其它名稱
root = Tk()
# 建立標籤(放在root底下,fg=文字顏色,bg=背景顏色,height=標籤高度,width=標籤寬度,font=字型)，label可取其它名稱
# wraplength=40，40像素自動換行
label = Label(root,text="I like tkinter.",fg="blue",bg="yellow",height=5,width=15,font=("Helvetica",20,"bold"))
# 包裝和定位元件
label.pack()
# 執行，放在最後一行
root.mainloop()
'''

'''
位元圖(Bitmap)


# 建立視窗，root可取其它名稱
root = Tk()
# 建立標籤(放在root底下,bitmap=位元圖)，label可取其它名稱
label = Label(root,bitmap="hourglass")
# 包裝和定位元件
label.pack()
# 執行，放在最後一行
root.mainloop()
'''

'''
位元圖(Bitmap)、文字並存


# 建立視窗，root可取其它名稱
root = Tk()
# 建立標籤(放在root底下,bitmap=位元圖,compound=bitmap位置)，label可取其它名稱
# compound只有在text和圖像一起存在時，才會有作用
label = Label(root,text="I like Tkinter.",bitmap="hourglass",compound="left")
# 包裝和定位元件
label.pack()
# 執行，放在最後一行
root.mainloop()
'''

'''
標籤邊框、文字和標籤間距


# 建立視窗，root可取其它名稱
root = Tk()
# 建立標籤(放在root底下,relief=邊框效果,padx=x軸間距,pady=y軸間距)，label可取其它名稱
label = Label(root,text="I like Tkinter.",relief="raised",padx=5,pady=20)
# 包裝和定位元件
label.pack()
# 執行，放在最後一行
root.mainloop()
'''

'''
顯示gif圖像

# 建立視窗，root可取其它名稱
root = Tk()
# gif圖像
html_gif = PhotoImage(file="../imgfolder/1.gif")
# 建立標籤(放在root底下,image=圖像)，label可取其它名稱
label = Label(root,image=html_gif)
# 包裝和定位元件
label.pack()
# 執行，放在最後一行
root.mainloop()
'''

'''
顯示png、jpg圖像

# 載入顯示png、jpg圖像的套件
from PIL import  Image,ImageTk

# 建立視窗，root可取其它名稱
root = Tk()
# 視窗大小
root.geometry("680x400")

# 讀取png圖像
image = Image.open("../imgfolder/link.png")
# 放到link
link = ImageTk.PhotoImage(image)
# 建立標籤(放在root底下,image=圖像)，label可取其它名稱
label = Label(root,image=link)
# 包裝和定位元件
label.pack()
# 執行，放在最後一行
root.mainloop()
'''


'''
png、jpg圖像和文字並存


# 載入顯示png、jpg圖像的套件
from PIL import  Image,ImageTk

# 建立視窗，root可取其它名稱
root = Tk()
# 視窗大小
root.geometry("680x400")

# 讀取png圖像
image = Image.open("../imgfolder/box.jpg")
# 放到link
link = ImageTk.PhotoImage(image)
# 建立標籤(放在root底下,image=圖像)，label可取其它名稱
label = Label(root,text="I like Tkinter.",image=link,compound="right")
# 包裝和定位元件
label.pack()
# 執行，放在最後一行
root.mainloop()
'''

'''
計數器


# 現在計數
counter = 0

# 副程式:計數器
def run_counter(digit):
    # 副程式:更動數字
    def counting():
        # 告知系統，此處counter是使用上面宣告的counter
        global counter
        counter  = counter + 1
        # 更改標籤文字
        digit.config(text=str(counter))
        # 每一秒執行一次
        digit.after(1000,counting)
    counting()


# 建立視窗，root可取其它名稱
root = Tk()
# 標題
root.title("Counter")

# 建立標籤(放在root底下,font=字型)
digit = Label(root,font=("Helvetic",20,"bold"))
# 包裝和定位元件
digit.pack()

# 執行計數器
run_counter(digit)
# 執行，放在最後一行
root.mainloop()
'''


'''
分隔線
'''

# 載入分隔線
from tkinter.ttk import Separator

# 建立視窗，root可取其它名稱
root = Tk()
# 視窗標題
root.title("Separator")
# 視窗大小
root.geometry("680x400")

# 內文標題
myTilte = "一個人的戲幕"
# 內文
myCntent = "台下人走過不見舊顏色，台上人唱著心碎離別歌。"

# 建立標籤(內文標題)
label_myTilte = Label(root,text=myTilte,font=("Helvetic",20,"bold"))
# 包裝和定位元件
label_myTilte.pack(padx=10,pady=10)

# 建立分隔線(放在root底下,orient=水平、垂直)
sep = Separator(root,orient=HORIZONTAL)
# 包裝和定位元件(fill=分隔線填滿X軸,左右間距50像素)
sep.pack(fill=X,padx=50)

# 建立標籤(內文)
label_myCntent = Label(root,text=myCntent)
# 包裝和定位元件
label_myCntent.pack(padx=10,pady=10)

# 執行，放在最後一行
root.mainloop()


























