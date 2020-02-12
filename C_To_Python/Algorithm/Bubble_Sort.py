import random

'''
氣泡排序法
Bubble Sort
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
#方法: Bubble Sort(Initial_Data: 要排序的資料List)(小 -> 大)
#==============================
def Bubble_Sort_To_Big(Initial_Data):
    #暫存最小值
    Min = 0

    for i in range(0,len(Initial_Data)):
        for j in range(i,len(Initial_Data)):
            if(Initial_Data[i] > Initial_Data[j]):
                Min = Initial_Data[j]
                Initial_Data[j] = Initial_Data[i]
                Initial_Data[i] = Min

    return Initial_Data

#==============================
#方法: Bubble Sort(Initial_Data: 要排序的資料List)(大 -> 小)
#==============================
def Bubble_Sort_To_Small(Initial_Data):
    #暫存最大值
    Max = 0

    for i in range(0,len(Initial_Data)):
        for j in range(i,len(Initial_Data)):
            if(Initial_Data[i] < Initial_Data[j]):
                Max = Initial_Data[j]
                Initial_Data[j] = Initial_Data[i]
                Initial_Data[i] = Max

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
print('Before Bubble Sort: \n', Initial_Data)

#==============================
#執行Bubble Sort
#==============================
#Bubble Sort(小 -> 大)
Sorted_Data = Bubble_Sort_To_Big(Initial_Data)
#印出排序後的資料
print('After Bubble Sort(Small -> Big): \n', Sorted_Data)

#Bubble Sort(大 -> 小)
Sorted_Data = Bubble_Sort_To_Small(Initial_Data)
#印出排序後的資料
print('After Bubble Sort(Big -> Small): \n', Sorted_Data)