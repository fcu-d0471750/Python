'''
功能扭 Button
'''


# 載入tkinter
from tkinter import *

##==============================================================================================
## Function
##==============================================================================================

# Button 基本用法
def button_to_base():
    # 列印訊息
    def msgShow():
        label["text"] = "I love Python."
        label["bg"] = "lightyellow"
        label["fg"] = "blue"
        #此行的執行結果，和上面三行一樣
        #label.config(text="I love Python.",bg="lightyellow",fg="blue")

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("button_to_base")

    # 標籤
    label = Label(root)
    # 按扭(command=呼叫msgShow)
    btn = Button(root,text="列印訊息",command=msgShow)

    # 包裝元件
    label.pack()
    # 包裝元件
    btn.pack()

    # 執行，放在最後一行
    root.mainloop()

# Button 結束按扭
def button_to_destory():
    # 列印訊息
    def msgShow():
        label.config(text="I love Python.",bg="lightyellow",fg="blue")

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("button_to_destory")

    # 標籤
    label = Label(root)
    # 訊息按扭(command=呼叫msgShow)
    btn = Button(root,width=15, text="列印訊息", command=msgShow)
    # 結束按扭(command=關閉root)
    # destroy是將整個視窗結束，另一個相似的quit則是結束Python Shell裡的程式，而視窗還是存在
    btn_des = Button(root,width=15,text="結束", command=root.destroy)


    # 包裝元件
    label.pack()
    # 包裝元件
    btn.pack()
    # 包裝元件
    btn_des.pack()

    # 執行，放在最後一行
    root.mainloop()

# 計數器
def Do_Count():
    # 副程式:計數器
    def run_counter(digit):
        # 副程式:更動數字
        def counting():
            # 告知系統，此處counter是使用上面宣告的counter
            global counter
            counter = counter + 1
            # 更改標籤文字
            digit.config(text=str(counter))
            # 每一秒執行一次
            digit.after(1000, counting)

        counting()

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 標題
    root.title("Counter")

    # 建立標籤(放在root底下,font=字型)
    digit = Label(root, font=("Helvetic", 20, "bold"))
    # 包裝和定位元件
    digit.pack()

    # 結束按扭(command=關閉root)
    btn_des = Button(root,width=15,text="結束",command=root.destroy)
    # 包裝元件
    btn_des.pack()

    # 執行計數器
    run_counter(digit)
    # 執行，放在最後一行
    root.mainloop()

# Button 改變背景顏色
def button_to_changebg():
    # 設定背景顏色為黃色
    def bg_yellow():
        root.config(bg="yellow")
    # 設定背景顏色為藍色
    def bg_blue():
        root.config(bg="blue")


    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("button_to_changebg")
    # 視窗大小
    root.geometry("300x200")

    # 黃色Button
    btn_yellow = Button(root,text="Yellow",command=bg_yellow)
    # 藍色Button
    btn_blue = Button(root, text="Blue", command=bg_blue)
    # 結束Button
    btn_des = Button(root,text="Exit",command=root.destroy)

    # 包裝元件(右下角)，會先將btn_des放在右下角，然後是btn_blue，最後是btn_yellow
    btn_des.pack(anchor=S, side=RIGHT, padx=5, pady=5)
    btn_blue.pack(anchor=S, side=RIGHT, padx=5, pady=5)
    btn_yellow.pack(anchor=S,side=RIGHT,padx=5,pady=5)

    # 執行，放在最後一行
    root.mainloop()

# Button 使用lambda表達式
# button_to_changebg()每改變一個顏色，就要寫一個Function，用lambda簡化
def button_to_lambda():
    def bcolor(bgcolor):
        root.config(bg=bgcolor)

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("button_to_lambda")
    # 視窗大小
    root.geometry("300x200")

    # 黃色Button
    btn_yellow = Button(root, text="Yellow", command=lambda:bcolor("yellow"))
    # 藍色Button
    btn_blue = Button(root, text="Blue", command=lambda:bcolor("blue"))
    # 結束Button
    btn_des = Button(root, text="Exit", command=root.destroy)

    # 包裝元件(右下角)，會先將btn_des放在右下角，然後是btn_blue，最後是btn_yellow
    btn_des.pack(anchor=S, side=RIGHT, padx=5, pady=5)
    btn_blue.pack(anchor=S, side=RIGHT, padx=5, pady=5)
    btn_yellow.pack(anchor=S, side=RIGHT, padx=5, pady=5)

    # 執行，放在最後一行
    root.mainloop()

# 圖片Button
def button_to_imagebutton():
    # 列印訊息
    def msgShow():
        label.config(text="I love Python.", bg="lightyellow", fg="blue")

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("button_to_imagebutton")

    # 標籤
    label = Label(root)
    # Image
    photo = PhotoImage(file="../imgfolder/sun.png")
    # 訊息按扭(compound=圖片位置,command=呼叫msgShow)
    btn = Button(root, width=50,height=30,text="click",compound=LEFT,image=photo, command=msgShow)

    # 包裝元件
    label.pack()
    # 包裝元件
    btn.pack()

    # 執行，放在最後一行
    root.mainloop()

# 簡易計算器Button佈局
def button_to_counter():
    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("button_to_counter")

    # 顯示區域
    lab = Label(root,text="輸入...",bg="gray",width=20)

    # 數字、功能區域
    btn7 = Button(root,text="7",width=3)
    btn8 = Button(root,text="8",width=3)
    btn9 = Button(root, text="9", width=3)
    # 乘法符號
    btnM = Button(root, text="*", width=3)

    btn4 = Button(root, text="4", width=3)
    btn5 = Button(root, text="5", width=3)
    btn6 = Button(root, text="6", width=3)
    # 減法符號
    btnS = Button(root, text="-", width=3)

    btn1 = Button(root, text="1", width=3)
    btn2 = Button(root, text="2", width=3)
    btn3 = Button(root, text="3", width=3)

    # 加法符號
    btnP = Button(root, text="+", width=3)

    btn0 = Button(root, text="0", width=8)

    # 小數點符號
    btnD = Button(root, text=".", width=3)

    # 等號符號
    btnE = Button(root, text="=", width=3)

    # 包裝元件
    lab.grid(row=0,column=0,columnspan=4)

    btn7.grid(row=1,column=0,padx=5)
    btn8.grid(row=1, column=1, padx=5)
    btn9.grid(row=1, column=2, padx=5)

    btnM.grid(row=1, column=3, padx=5)

    btn4.grid(row=2, column=0, padx=5)
    btn5.grid(row=2, column=1, padx=5)
    btn6.grid(row=2, column=2, padx=5)

    btnS.grid(row=2, column=3, padx=5)

    btn1.grid(row=3, column=0, padx=5)
    btn2.grid(row=3, column=1, padx=5)
    btn3.grid(row=3, column=2, padx=5)

    btnP.grid(row=3, column=3, padx=5)

    btn0.grid(row=4, column=0, padx=5,columnspan=2)

    btnD.grid(row=4, column=2, padx=5)
    btnE.grid(row=4, column=3, padx=5)
    # 執行，放在最後一行
    root.mainloop()

# 進入Button時，改變鼠標
def button_to_cursor():
    # 列印訊息
    def msgShow():
        label.config(text="I love Python.", bg="lightyellow", fg="blue")

    # 建立視窗，root可取其它名稱
    root = Tk()
    # 視窗標題
    root.title("button_to_cursor")

    # 標籤
    label = Label(root)

    # Image
    photo = PhotoImage(file="../imgfolder/sun.png")
    # 訊息按扭(compound=圖片位置,command=呼叫msgShow,cursor=鼠標圖案)
    btn = Button(root, width=50, height=30, text="click", compound=LEFT, image=photo, command=msgShow,cursor="star")

    # 包裝元件
    label.pack()
    # 包裝元件
    btn.pack()

    # 執行，放在最後一行
    root.mainloop()
##==============================================================================================
## Main
##==============================================================================================

# Button 基本用法
#button_to_base()

# Button 結束按扭
#button_to_destory()

# 計數器
#counter = 0
#Do_Count()

# Button 改變背景顏色
#button_to_changebg()

# Button 使用lambda表達式
#button_to_lambda()

# 圖片Button
#button_to_imagebutton()

# 簡易計算器Button佈局
#button_to_counter()

# 進入Button時，改變鼠標
#button_to_cursor()








