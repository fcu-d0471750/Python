'''
描述
輸入直徑計算出面積與周長,
並輸出至小數點下二位
輸入
利用 input 得到一個浮點數
輸出
輸出面積與周長


radius = float(input())
PI = 3.14

area = (radius//2) * (radius//2) * PI
perimeter =  radius * PI

print('{:.2f}\n{:.2f}'.format(area,perimeter))


'''


'''
描述

輸入兩個座標，輸出距離


輸入
以四次input取得四個數字，

透過平面公式求得兩點距離，

並將其結果顯示出來。


輸出
以print("".format())顯示計算結果，

輸出至小數點後兩位數。


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

d = (pow( (x1-x2) , 2) + pow((y1-y2) , 2)) **0.5
print('{:.2f}'.format(d))
'''





'''
描述

輸入兩個座標，輸出距離。


輸入
以兩次input取得兩組座標，

透過平面公式求得兩點距離，

並將其結果顯示出來。


輸出
以print("".format())顯示計算結果，

輸出至小數點後兩位數。



point_1 = []
point_2 = []

input_1 = input()
input_2 = input()

point_1 = input_1.split(',')
point_2 = input_2.split(',')

x1 = int(point_1[0])
y1 = int(point_1[1])
x2 = int(point_2[0])
y2 = int(point_2[1])

d = (pow( (x1-x2) , 2) + pow((y1-y2) , 2)) **0.5
print('{:.2f}'.format(d))
'''

'''
某學生各科成績為  10,30,40,90,100,62

計算結果

1.計算平均：

a. 四捨五入 , 取到整數位
b. 無條件進入 , 取到整數位
c. 無條件捨去 , 取到整數位
2.計算成績標準差


輸入
透過input取得以逗號隔開的各科成績。

由於目前尚未教到迴圈，本題限定為六筆資料。


輸出
輸出三種平均結果與成績的標準差

import math

grade = input()

grade_point = grade.split(',')

sum = (float(grade_point[0]) + float(grade_point[1]) + float(grade_point[2]) + float(grade_point[3]) + float(grade_point[4]) + float(grade_point[5]))/6.0

a = round(sum)
b = math.ceil(sum)
c = int(sum)

d = ((pow(float(grade_point[0])-sum , 2) + pow(float(grade_point[1])-sum , 2) + pow(float(grade_point[2])-sum , 2) + pow(float(grade_point[3])-sum , 2) + pow(float(grade_point[4])-sum , 2) + pow(float(grade_point[5])-sum , 2))/6.0)**0.5

print('{:.2f}\n{:.2f}\n{:.2f}\n{:.2f}'.format(a,b,c,d))
'''


'''
描述
請讓使用者輸入兩個數字 a,b(兩行 input )
接著利用迴圈計算 a 加到 b(包含 a,b )是多少。例如 1,10 則計算 1+2+3+...10, 則結果為 55。
注意:題目保證 a < b

輸入
兩個數字 a,b (兩行 input )

輸出
計算 a 加到 b 是多少


a = 0
b = 0
sum = 0
a = eval(input())
b = eval(input())

for i in range(a,b+1,1):
    sum = sum + i
print(sum)
'''

'''
描述
請讀入一串數字到一個 list 中
接著用 for 迴圈計算他們的總和
注意：你可以自己想辦法處理輸入
或者直接寫 x = InputList() 即可
不過 return 前翻方的縮排必須要空四格唷!

InputList 為助教幫妳寫好的程式碼
原始碼如下
def InputList():
    return list(map(int,input().split(' ')))
    
輸入
一串數字
如果不會處理的話
使用x = InputList() 即可
InputList 為助教幫妳寫好的程式碼
Python 內並無內建此函式

輸出
總和

def InputList():
    return list(map(int,input().split(' ')))

sum = 0
x = InputList()

for i in range(0,len(x)):
    sum = sum + x[i]
print(sum)
'''

'''
描述
請讓使用者先輸入性別( F/M )後
再輸入年齡(一個數字)
並依照下表輸出對應的稱呼
           F            M
0~12   little girl   little boy
13~18     girl         boy
19~      woman         man

輸入
先輸入性別( F/M )後
再輸入年齡(一個數字)

輸出
依照下表輸出對應的稱呼
           F            M
0~12    little girl   little boy
13~18     girl         boy
19~      woman         man


Gender = input()
Age = eval(input())

if(Gender == 'F'):
    if(Age >= 19): print('woman')
    elif(Age <= 18 and Age>=13): print('girl')
    else:print('little girl')
else:
    if (Age >= 19):
        print('man')
    elif (Age <= 18 and Age >= 13):
        print('boy')
    else:
        print('little boy')
'''


'''
某班微積分成績如下：
67,84,40,49,57,74,90,84,69,52,33,96,28,67,85,75,53,88,80,73,71,70,54,65,77,62,81,40,69,34
請依此為輸入值，幫忙授課教師完成次數分配表


輸入
以 input 取得成績
67,84,40,49,57,74,90,84,69,52,33,96,28,67,85,75,53,88,80,73,71,70,54,65,77,62,81,40,69,34

輸出
輸出 8 個組距的人數

SP = [0,0,0,0,0,0,0,0]

Score = input()
Score = Score.split(',')

for i in range(0,len(Score)):
    Score[i] = int(Score[i])

for i in range(0,len(Score)):
    if(Score[i]>=20 and Score[i]<30): SP[0] = SP[0] + 1
    elif(Score[i]>=30 and Score[i]<40): SP[1] = SP[1] + 1
    elif(Score[i]>=40 and Score[i]<50): SP[2] = SP[2] + 1
    elif(Score[i]>=50 and Score[i]<60): SP[3] = SP[3] + 1
    elif(Score[i]>=60 and Score[i]<70): SP[4] = SP[4] + 1
    elif(Score[i]>=70 and Score[i]<80): SP[5] = SP[5] + 1
    elif(Score[i]>=80 and Score[i]<90): SP[6] = SP[6] + 1
    elif(Score[i]>=90 and Score[i]<=100): SP[7] = SP[7] + 1

for i in range(0,len(SP)):
    print(SP[i])
'''
'''
R 是一筆記錄病人是否患得乳癌的真實資料; 
P 是某個人工智慧方法預估是否罹癌的預估資料。
如果 P 和 R 越相近，我們會說 P 的預估方法是好的。
通常評估有三個指標：正確率 ( accuracy )、精準度 ( precision )、召回度 ( recall )。

「正確率」：正確的/所有的資料。

以下是一個範例，其中 T 表示罹癌，F 表示無。

R = ['T', 'F', 'T', 'T', 'F', 'T', 'F', 'T', 'F', 'F'] 
P = ['T', 'F', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T']

accuracy = 6/10 
'''
R = input()
P = input()
accuracy = 0

R = R.split(',')
P = P.split(',')
for i in range(0,len(R)):
    if(R[i] == P[i]): accuracy = accuracy + 1

print(accuracy*10)




