import codecs
'''
FileObject = open('data.txt' , 'r' , encoding='utf-8')
content = 'Process finished with exit code 1'
print(content , file=open('data.txt' , 'a' , encoding='utf-8'))
FileObject.close()
'''

'''
Exercise 902
讀取read.txt，內容為整數，用空格分開
將所有整數加總，並印出加總結果

FileObject = open('read_1.txt' , 'r' , encoding='utf-8')
InputFile = FileObject.read()
FileObject.close()

#將InputFile的內容，依空格為單位進行分割
num = InputFile.split(' ')
#預設總和為0
Sum = 0

#加總
for i in range(0,len(num)):
 print(num[i] , end=' ')
 Sum = Sum + eval(num[i])

print('\n總和為: ' , Sum)
'''

'''
Exercise 904
讀取read.txt，內容為名字、身高、體重，用空格分開
印出所有人的平均身高、平均體重、最高者、最重者
*浮點數到小數點第2位

FileObject = open('read_2.txt' , 'r' , encoding='utf-8')
InputFile = FileObject.read()
FileObject.close()

#===============================
#宣告變數
#===============================
#所有人資料
Data = []
#名字List
Name = []
#身高List
Height = []
#體重List
Weight = []
#最高身高
Max_H = 0
#最重體重
Max_W = 0

#將換行符號 轉成 空格
Line = InputFile.replace('\n',' ')
#將InputFile的內容，依空格為單位進行分割
Line = Line.split(' ')

#將分割的資料以3個為1組(名字、身高、體重)
for i in range(0 , len(Line) , 3):
    #用Temp存成1組資料
    Temp = [Line[i] , eval(Line[i+1]) , eval(Line[i+2])]
    #將Temp放入Data成為1組資料
    Data.append(Temp)

print(Data , '\n')

#名字
for i in range(0 , len(Data)):
    Name.append(Data[i][0])
#身高
for i in range(0 , len(Data)):
    Height.append(Data[i][1])
#最高者
Max_H = max(Height)
#體重
for i in range(0 , len(Data)):
    Weight.append(Data[i][2])
#最重者
Max_W = max(Weight)


#平均身高
print('Average Height: {:.2f}' .format(sum(Height)/ len(Height)))

#平均體重
print('Average Weight: {:.2f}' .format(sum(Weight) / len(Weight)))

#最高者
print('Tallest: ' , Name[Height.index(Max_H)] , Max_H)

#最重者
print('Heaviest: ' , Name[Weight.index(Max_W)] , Max_W)

'''

'''
Exercise 906
輸入 檔名read_3.txt、字串s1、字串s2
將read_3.txt中的字串s1用字串s2取代

FileName = input('FileName: ')
s1 = input('字串1: ')
s2 = input('字串2: ')

FileObject = open(FileName , 'r' , encoding='utf-8')
InputFile = FileObject.read()
FileObject.close()

#將read_3.txt中的字串s1用字串s2取代
OutFile = InputFile.replace(s1 , s2)

#輸出檔案
print(OutFile , file=open(FileName , 'w' , encoding='utf-8'))
'''

'''
Exercise 908
輸入 檔名read_4.txt，以及出現次數(單字用空格隔開)
輸出 符合出現次數的單字，並依第1個字母排序

ex.
輸入
read_4.txt
3

輸出
a
is
program


#===============================
#宣告變數
#===============================
#單字和出現次數List
Word = []
#暫存單字和出現次數List
Temp = []
#計算相同單字出現次數，至少為1次
Temp_Number = 1
#儲存符合出現次數的單字
Out_Word = []
#是否有符合出現次數的單字，true:有符合 false:未符合
Appear = False


FileName = input('FileName: ')
Number = eval(input('出現次數: '))

FileObject = open(FileName , 'r' , encoding='utf-8')
InputFile = FileObject.read()
FileObject.close()

#將換行符號 轉成 空格
Line = InputFile.replace('\n',' ')
#將InputFile的內容，依空格為單位進行分割
Line = Line.split(' ')

print(Line)

#計算相同的單字出現次數
for i in range(0 , len(Line) , 1):
    #如果Line[i]=='@'，表示這個單字前面已經計算過，不在計算
    if(Line[i]=='@'):continue
    #一一比較單字是否相同
    for j in range(i+1 , len(Line) , 1):
        #如果碰到相同單字
        if(Line[i] == Line[j]):
            #則出現次數+1
           Temp_Number = Temp_Number + 1
            #並將該位置的單字改為'@'，表示這個單字已經計算過
           Line[j] = '@'
    #將單字和出現次數存成List
    Temp = [Line[i] , Temp_Number]
    #放入Word
    Word.append(Temp)
    #出現次數恢復成初始值
    Temp_Number = 1

#將符合出現次數的單字List放入Out_Word
for i in range(0 , len(Word)):
    if(Word[i][1] == Number):
        #有符合出現次數的單字
        Appear = True
        Temp = Word[i][0]
        Out_Word.append(Temp)

#印出Out_Word
if(Appear == True): print(sorted(Out_Word))
else: print('沒有符合出現次數的單字')
'''

'''
Exercise 910
讀取read_5.dat，第1列為欄位名稱，第2列為個人資料
輸出男生人數、女生人數(0:代表女生、1:代表男生)

學號 姓名 性別 科系
101  阿明  1    餐旅管理
202  阿忠  1    資工
303  小華  0    語文
404  篠美  0    應英
505  安凱  1    日文
'''

#===============================
#宣告變數
#===============================
#所有人資料List
Data = []
#暫存所有人資料List
Temp = []
#男生人數
Male_Number = 0
#女生人數
Female_Number = 0

FileObject = open('read_5.txt' , 'r' )
InputFile = FileObject.read()
FileObject.close()


#將換行符號 轉成 空格
Line = InputFile.replace('\n',' ')
#將InputFile的內容，依空格為單位進行分割
Line = Line.split(' ')

print(Line , '\n')

#將資料分隔成一個人一組('學號', '姓名', '性別', '科系')
for i in range(4 , len(Line) , 4):
    Temp = [eval(Line[i]) , Line[i+1] , eval(Line[i+2]) , Line[i+3]]
    Data.append(Temp);

#計算人數
for i in range(0,len(Data)):
    if(Data[i][2] == 0): Female_Number = Female_Number + 1
    else: Male_Number = Male_Number + 1

#輸出
print('學號', '姓名', '性別', '科系')

for i in range(0,len(Data)):
    print('{ID}  {Name}  {Sex}   {Department}' .format(ID=Data[i][0],Name=Data[i][1],Sex=Data[i][2],Department=Data[i][3]))

print()
print('Female_Number: ',Female_Number)
print('Male_Number: ' , Male_Number)