#=================================================================
#宣告變數
#=================================================================
#所有人資料
Data = []
#寫入檔案的字串
str = ''

#(1)
#===============================
#讀檔(模式:唯讀)
#===============================
#讀取write_1.txt
FileObject = open('write_1.txt' , 'r' , encoding='utf-8')
#讀取檔案全部內容
InputFile = FileObject.read()
#印出檔案全部內容
print(InputFile)
#關閉檔案
FileObject.close()

#(2)
#===============================
#將換行符號 轉成 空格
#===============================
Line = InputFile.replace('\n' , ' ')
#===============================
#將InputFile的內容，依空格為單位進行分割，並存在Line
#===============================
Line = Line.split(' ')
#印出Line的內容
print('Line\n',Line)


#(3)
#===============================
#將分割的資料以3個為1組(名字、身高、體重)
#===============================
for i in range(0,len(Line),3):
    #用Temp存成1組資料
    Temp = [Line[i] , Line[i+1] , Line[i+2]]
    #將Temp放入Data成為1組資料
    Data.append(Temp)

#印出Data的內容
print('Data\n',Data)

#(4)
#===============================
#新增一筆資料
#===============================
Temp = ['Gerage' , '173' , '72']
#將Temp放入Data成為1組資料
Data.append(Temp)
#印出Data的內容
print('Data add new Data\n',Data)

#(5)
#===============================
#讀檔(模式:寫入)
#===============================
#讀取write_1.txt
FileObject = open('write_1.txt' , 'w' , encoding='utf-8')
#資料一筆一筆放入str
for i in range(0,len(Data),1):
    #如果不是最後1筆資料，則要加上換行符號
    if(i!=len(Data)-1):str = str + ('{Name} {Height} {Weight}\n'.format(Name=Data[i][0] , Height=Data[i][1] , Weight=Data[i][2]))
    # 如果是最後1筆資料，則要不加上換行符號
    else:str = str + ('{Name} {Height} {Weight}'.format(Name=Data[i][0] , Height=Data[i][1] , Weight=Data[i][2]))

#將str寫入檔案
FileObject.write(str)
#關閉檔案
FileObject.close()





