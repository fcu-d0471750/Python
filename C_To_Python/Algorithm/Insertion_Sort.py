import random

'''
插入排序法
Insertion Sort
'''


#=================================================================================
#宣告變數
#=================================================================================
#List: 要排序的資料
Initial_Data = []

#List: 排序後的資料
Sorted_Data = []

#int: 共幾筆資料
Number = 100

#int: 暫存亂數
Temp = 0

#=================================================================================
#宣告方法
#=================================================================================

#==============================
#方法: Insertion Sort(Initial_Data: 要排序的資料List)(小 -> 大)(無額外空間)
#==============================
def Insertion_Sort_To_Big(Initial_Data):
     #暫存要插入的數字
     Temp = 0

     for i in range(0,len(Initial_Data)):
         #暫存要插入的數字
         Temp = Initial_Data[i]
         #從Temp前1個數字往前比較找到第1個比Temp大的數字
         for j in range(i-1,-1,-1):
             #如果找到比Temp大的數字
            if(Initial_Data[j] > Temp):
                #原本Temp所在位置的Value變成比Temp大的Value
                Initial_Data[j+1] = Initial_Data[j]
                #比Temp大的位置的Value變成Temp的Value
                Initial_Data[j] = Temp

     return Initial_Data


# ==============================
# 方法: Insertion Sort(Initial_Data: 要排序的資料List)(大 -> 小)(無額外空間)
# ==============================
def Insertion_Sort_To_Small(Initial_Data):
    #暫存要插入的數字
    Temp = 0

    for i in range(0, len(Initial_Data)):
        #暫存要插入的數字
        Temp = Initial_Data[i]
        #從Temp前1個數字往前比較找到第1個比Temp小的數字
        for j in range(i - 1, -1, -1):
            #如果找到比Temp大的數字
            if (Initial_Data[j] < Temp):
                #原本Temp所在位置的Value變成比Temp小的Value
                Initial_Data[j + 1] = Initial_Data[j]
                #比Temp小的位置的Value變成Temp的Value
                Initial_Data[j] = Temp


    return Initial_Data


#==============================
#方法: Insertion Sort(Initial_Data: 要排序的資料List)(小 -> 大)(有額外空間)
#==============================
def Insertion_Sort_Space_To_Big(Initial_Data):
     #暫存要插入的數字
     Temp = 0
     #要插入的位置
     Min_Pos = 0
     #排序後的List
     Sorted_Data = [Initial_Data[0]]

     for i in range(1,len(Initial_Data)):
         #暫存要插入的數字
         Temp = Initial_Data[i]
         #從已排列的List最尾端開始
         Min_Pos = len(Sorted_Data)

         #從Temp前1個數字往前比較找到第1個比Temp大的數字
         for j in range(len(Sorted_Data)-1 , -1 , -1):
             #如果找到比Temp大的數字
            if(Sorted_Data[j] > Temp):
                #記錄比Temp大的數字的位置
                Min_Pos = j

         #插入Temp
         Sorted_Data.insert(Min_Pos , Temp)

     return Sorted_Data


#==============================
#方法: Insertion Sort(Initial_Data: 要排序的資料List)(大 -> 小)(有額外空間)
#==============================
def Insertion_Sort_Space_To_Small(Initial_Data):
     #暫存要插入的數字
     Temp = 0
     #要插入的位置
     Min_Pos = 0
     #排序後的List
     Sorted_Data = [Initial_Data[0]]

     for i in range(1,len(Initial_Data)):
         #暫存要插入的數字
         Temp = Initial_Data[i]
         #從已排列的List最尾端開始
         Min_Pos = len(Sorted_Data)

         #從Temp前1個數字往前比較找到第1個比Temp小的數字
         for j in range(len(Sorted_Data)-1 , -1 , -1):
             #如果找到比Temp小的數字
            if(Sorted_Data[j] < Temp):
                #記錄比Temp小的數字的位置
                Min_Pos = j

         #插入Temp
         Sorted_Data.insert(Min_Pos , Temp)

     return Sorted_Data


#=================================================================================
#執行
#=================================================================================

#==============================
#產生亂數，填滿要排序的資料
#==============================
#依照Number，產生幾次亂數
for i in range(0,Number):
    # Temp暫存亂數(0~9999)
    Temp = random.randint(0,9999)
    # 把Tepm加進Initial_Data儲存起來
    Initial_Data.append(Temp)

#印出排序前的資料
print('Before Insertion Sort: \n', Initial_Data)


#==============================
#執行Insertion Sort
#==============================

#Insertion Sort(小 -> 大)(無額外空間)
Sorted_Data = Insertion_Sort_To_Big(Initial_Data)
#印出排序後的資料
print('After Insertion Sort(Small -> Big)(In Space): \n', Sorted_Data)

#Insertion Sort(大 -> 小)(無額外空間)
Sorted_Data = Insertion_Sort_To_Small(Initial_Data)
#印出排序後的資料
print('After Insertion Sort(Big -> Small)(In Space): \n', Sorted_Data)

#換行
print()

#Insertion Sort(小 -> 大)(有額外空間)
Sorted_Data = Insertion_Sort_Space_To_Big(Initial_Data)
#印出排序後的資料
print('After Insertion Sort(Small -> Big): \n', Sorted_Data)

#Insertion Sort(大 -> 小)(有額外空間)
Sorted_Data = Insertion_Sort_Space_To_Small(Initial_Data)
#印出排序後的資料
print('After Insertion Sort(Big -> Small): \n', Sorted_Data)





