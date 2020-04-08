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

R = input()
P = input()
accuracy = 0

R = R.split(',')
P = P.split(',')
for i in range(0,len(R)):
    if(R[i] == P[i]): accuracy = accuracy + 1

print(accuracy*10)
'''
'''
有一個結構為 dict 的資料名為 rank, 記錄著一群人對電影的喜好程度，例如： Nick 對 Coco 的評價為 1, 對 Cold War 的評價為 5; John 對 Coco 的評價為 5, 對 Cold War 的評價為 1, 則可以表示為：
rank = {'Nick': {'Coco': 1, 'Cold War': 5}, 'John': {'Coco': 5, 'Cold War': 1}}
列出所有人的姓名在第一行，所有電影在第二行（不得重複），且必須由a到z排序。


rank = {'Nick': {'Coco': 1, 'Cold War': 5}, 'John': {'Coco': 5, 'Cold War': 1}}
dlist = []
ulist = []
nlist = []
mlist = []

for key,value in rank.items():
    temp = [key,value]
    dlist.append(temp)

for i in range (0,len(dlist)):
    #print(dlist[i][0],end=' ').
    ulist.append(dlist[i][0])

ulist.sort()

for i in range (0,len(ulist)):
    print(ulist[i],end=' ')

print()


for key,value in rank['Nick'].items():
    temp = [key,value]
    nlist.append(temp)

for i in range (0,len(nlist)):
    #print(nlist[i][0],end=' ')
    mlist.append(nlist[i][0])

mlist.sort()

for i in range (0,len(mlist)):
    print(mlist[i],end=' ')
'''

'''
import math
rank = {'Nick': {'Coco': 1, 'Cold War': 5}, 'John': {'Coco': 5, 'Cold War': 1}}
n1 = input()
n2 = input()
rank_sum = 0
Temp = 0


for i in rank[n1].keys():
    for j in rank[n2].keys():
        if(i==j):
            Temp = abs(rank[n1][i]-rank[n2][j])**2
            rank_sum = rank_sum + Temp

distance = round(math.sqrt(rank_sum),2)
print (distance)
'''

'''
for i,j in rank[n1].values(),rank[n2].values():
    Temp = abs(i-j)**2
    rank_sum = rank_sum + Temp
'''
'''
a = [[12,1,100],
     [34,90,22],
     [80,80,80]]

a.sort(key = lambda r: r[2])
print(a)
'''
#key = lambda k : s[k]
'''
max = lambda x,y: x if x > y else y
m = max(10,9)
print(m)
'''
'''
s1 = {"Nick": {"Coco": 1, "Cold War": 5}, 
      "John": {"Coco": 5, "Cold War": 1}, 
      "Leo": {"Coco": 3, "Cold War": 4}, 
      "Jie": {"Coco": 5} 
      }

s2 = {"Nick": {"Coco": 1, "Cold War": 5}, 
      "John": {"Coco": 5, "Cold War": 1}, 
      "Leo": {"Coco": 3, "Cold War": 4}, 
      "Jie": {"Coco": 5, "Cold War": 1} 
      } 

s3 = {"Nick": {"Coco": 1, "Cold War": 5}, 
      "John": {"Coco": 5, "Cold War": 1}, 
      "Leo": {"Tiger": 3, "Cold War": 4}, 
      "Jie": {"Cold War": 3} 
      } 

s4 = {"Nick": {"Coco": 1, "Cold War": 5, "Z": 1}, 
      "John": {"Coco": 5, "Cold War": 1, "Z": 1}, 
      "Leo": {"Tiger": 3, "Cold War": 4, "Z": 1}, 
      "Jie": {"Z": 1} 
      }
      
s1: Cold War
s2: None
s3: Tiger
s4: Coco      
      
'''

import math

def dis(rank,p,q):
    rank_sum = 0
    Temp = 0

    for i in rank[p].keys():
        for j in rank[q].keys():
            if (i == j):
                Temp = abs(rank[p][i] - rank[q][j]) ** 2
                rank_sum = rank_sum + Temp

    distance = round(math.sqrt(rank_sum), 2)

    return distance

def nearest(rank,p):
    # 預設極大值，用於比較
    min_dis = 100
    # Key排序，確保依照名稱進行
    name_list = sorted(rank.keys())

    for people in name_list:
        # 遇到自己，不比較
        if people == p:
            continue
        d = dis(rank,p,people)
        #
        if d < min_dis:
            min_dis = d
            nearest_p = people

    return nearest_p
    #依據rank找出和p最接近的人
    #先設一個極大值成最小距離，設100
    #跑迴圈找出和p之間距離最小的人
    # near = dis(rank,p,q)

def my_favorite(rank,q):
    movie_dict = rank[q]
    movie_r_list = []
    movie_list = []

    for m in movie_dict:
        movie_r_list.append([m,rank[q][m]])
    movie_r_list = sorted(movie_r_list,key= lambda  x: x[-1],reverse=True)

    for i in  movie_r_list:
        movie_list.append(i[0])

    return movie_list


def recommend(rank, p):
    # 1. 找出喜好最接近 p 的人，假設為 q
    #   q = nearest(rank,p)
    q = nearest(rank,p)
    #2. 找出q喜好的影片列表like_list
    #   like_list = my_favorite(rank,p)
    like_list = my_favorite(rank, q)
    #3. 從like_list找p還沒有評價的電影
    #   find_not_watched
    for m in like_list:
        if not (m in  my_favorite(rank,p)):
            not_watched = m
            break
        else:
            not_watched = "None"
    return not_watched





#recommend 會推薦和他喜好距離最短的人最喜歡的電影

#p = input()

#movie = recommend(rank, p)


s3 = {"Nick": {"Coco": 1, "Cold War": 5},
      "John": {"Coco": 5, "Cold War": 1},
      "Leo": {"Tiger": 3, "Cold War": 4},
      "Jie": {"Cold War": 3}
      }


p = "Jie"
movie = recommend(s3, p)

print(p , "-----" , movie)