import random

'''
選擇排序法
Selection Sort
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
#方法:兩個List中的數字交換(List，位置1，位置2)
#==============================
def Swap(Initial_Data , Pos_1 , Pos_2):

    Temp = 0

    Temp = Initial_Data[Pos_1]
    Initial_Data[Pos_1] = Initial_Data[Pos_2]
    Initial_Data[Pos_2] = Temp

    return Initial_Data

#==============================
#方法: Selection Sort(Initial_Data: 要排序的資料List)(小 -> 大)
#==============================
def Selection_Sort_To_Big(Initial_Data):
    #依照順序一一比較數字
    for i in range(0 , len(Initial_Data)):
        for j in range(i+1 , len(Initial_Data)):
            #找出未排序中的資料中最小值
            if(Initial_Data[i] > Initial_Data[j]):
                #交換位置
                Initial_Data = Swap(Initial_Data , i , j)

    return Initial_Data

#==============================
#方法: Selection Sort(Initial_Data: 要排序的資料List)(大 -> 小)
#==============================
def Selection_Sort_To_Small(Initial_Data):
    #依照順序一一比較數字
    for i in range(0 , len(Initial_Data)):
        for j in range(i+1 , len(Initial_Data)):
            #找出未排序中的資料中最大值
            if(Initial_Data[i] < Initial_Data[j]):
                #交換位置
                Initial_Data = Swap(Initial_Data , i , j)

    return Initial_Data

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
print('Before Selection Sort: \n', Initial_Data)

#==============================
#執行Selection Sort
#==============================
#Quick Sort(小 -> 大)
Sorted_Data = Selection_Sort_To_Big(Initial_Data)
#印出排序後的資料
print('After Selection Sort(Small -> Big): \n', Sorted_Data)

#Quick Sort(大 -> 小)
Sorted_Data = Selection_Sort_To_Small(Initial_Data)
#印出排序後的資料
print('After Selection Sort(Big -> Small): \n', Sorted_Data)