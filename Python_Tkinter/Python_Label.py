'''
標籤 Label
'''

# 載入tkinter
from  tkinter import *

# 印出tkinter版本
# print(tkinter.TkVersion)

'''
建立視窗

# 建立視窗，root可取其它名稱
root = Tk()
# 執行，放在最後一行
root.mainloop()
'''

'''
建立視窗(自定標題、大小、背景顏色、icon)

# 建立視窗，root可取其它名稱
root = Tk()
# 標題
root.title = "MyWindow"
# 視窗大小(寬 x 高)
root.geometry("300x160")
# 背景顏色
root.configure(bg="#D2B48C")
# icon
root.iconbitmap(r"../icon/python_icon.ico")
# 執行，放在最後一行
root.mainloop()
'''

'''
視窗位置(變數控制)

# 建立視窗，root可取其它名稱
root = Tk()
# 視窗位置(寬 x 高 + 距離左上角(400,200))
#root.geometry("300x160+400+200")
# 視窗本身寬
w = 300
# 視窗本身高
h = 160
# 距離左上角x軸
x = 400
# 距離左上角y軸
y = 200
# 視窗位置(同上)
root.geometry("%dx%d+%d+%d" %(w,h,x,y))
# 執行，放在最後一行
root.mainloop()
'''

'''
視窗位置(螢幕中間)

# 建立視窗，root可取其它名稱
root = Tk()
# 螢幕寬
screenWidth = root.winfo_screenwidth()
# 螢幕高
screenHeight = root.winfo_screenheight()
# 視窗本身寬
w = 300
# 視窗本身高
h = 160
# 距離左上角x軸
x = (screenWidth - w) / 2
# 距離左上角y軸
y = (screenHeight - h) / 2
# 視窗位置
root.geometry("%dx%d+%d+%d" %(w,h,x,y))
# 執行，放在最後一行
root.mainloop()
'''






















