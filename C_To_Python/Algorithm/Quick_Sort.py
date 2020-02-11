import random

'''
快速排序法
Quick Sort
'''

#=================================================================================
#宣告變數
#=================================================================================
#List: 要排序的資料
Initial_Data = []

#List: 排序後的資料
Sorted_Data = []

#int: 共幾筆資料
Number = 10

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
#方法: Quick Sort(小 -> 大)
#==============================
def Quick_Sort_To_Big(Initial_Data , Left , Right):
    #基準點
    Pivot = 0
    #用於跟基準點比較
    i = 0
    #右邊基準點
    j = 0

    #==============================
    #如果沒有可交換的數字，則結束排序
    #==============================
    if(Left >= Right): return Initial_Data

    #==============================
    #如果有可交換的數字，則排序
    #==============================
    #基準點設為最左邊的數字
    Pivot = Initial_Data[Left]
    #i = 第二個數字
    i = Left + 1
    #j = 最右邊的數字
    j = Right

    #==============================
    #依照基準點排序(將List分成兩堆，左邊為比基準點小的數字，右邊為比基準點大的數字)
    #==============================
    while(True):
        #向右邊找比基準點大的數字
        while(i <= Right):
            #找到比基準點大的數字，停止搜尋
            if(Initial_Data[i] > Pivot): break
            #否則，再向右搜尋
            else: i = i + 1

        #向左邊找比基準點小的數字
        while(j > Left):
            #找到比基準點小的數字，停止搜尋
            if(Initial_Data[j] < Pivot): break
            #否則，再向左搜尋
            else: j = j - 1

        #如果搜尋位置交錯，則停止搜尋 和 交換位置
        if(i > j): break

        #交換數字的位置，改變Value，不改變 Address
        Initial_Data = Swap(Initial_Data , i , j)
        

    #將基準點跟最小的數字交換位置(j的位置正好為可以將List分為兩堆的位置，所以跟Left的Value交換)
    Initial_Data = Swap(Initial_Data , Left , j)

    #將分類好的左邊繼續進行QuickSort
    Quick_Sort_To_Big(Initial_Data , Left , j - 1)
    #將分類好的右邊繼續進行QuickSort
    Quick_Sort_To_Big(Initial_Data , j + 1 , Right)

    return Initial_Data

#==============================
#方法: Quick Sort(大 -> 小)
#==============================
def Quick_Sort_To_Small(Initial_Data , Left , Right):
    #基準點
    Pivot = 0
    #用於跟基準點比較
    i = 0
    #右邊基準點
    j = 0

    #==============================
    #如果沒有可交換的數字，則結束排序
    #==============================
    if(Left >= Right): return Initial_Data

    #==============================
    #如果有可交換的數字，則排序
    #==============================
    #基準點設為最左邊的數字
    Pivot = Initial_Data[Left]
    #i = 第二個數字
    i = Left + 1
    #j = 最右邊的數字
    j = Right

    #==============================
    #依照基準點排序(將List分成兩堆，左邊為比基準點大的數字，右邊為比基準點小的數字)
    #==============================
    while(True):
        #向右邊找比基準點小的數字
        while(i <= Right):
            #找到比基準點小的數字，停止搜尋
            if(Initial_Data[i] < Pivot): break
            #否則，再向右搜尋
            else: i = i + 1

        #向左邊找比基準點大的數字
        while(j > Left):
            #找到比基準點大的數字，停止搜尋
            if(Initial_Data[j] > Pivot): break
            #否則，再向左搜尋
            else: j = j - 1

        #如果搜尋位置交錯，則停止搜尋 和 交換位置
        if(i > j): break

        #交換數字的位置，改變Value，不改變 Address
        Initial_Data = Swap(Initial_Data , i , j)


    #將基準點跟最小的數字交換位置(j的位置正好為可以將List分為兩堆的位置，所以跟Left的Value交換)
    Initial_Data = Swap(Initial_Data , Left , j)

    #將分類好的左邊繼續進行QuickSort
    Quick_Sort_To_Small(Initial_Data , Left , j - 1)
    #將分類好的右邊繼續進行QuickSort
    Quick_Sort_To_Small(Initial_Data , j + 1 , Right)

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
print('Before Sort: \n', Initial_Data)

#==============================
#執行Quick Sort
#==============================
#Quick Sort(小 -> 大)
Sorted_Data = Quick_Sort_To_Big(Initial_Data , 0 , Number-1)
#印出排序後的資料
print('After Sort(Small -> Big): \n', Sorted_Data)

#Quick Sort(大 -> 小)
Sorted_Data = Quick_Sort_To_Small(Initial_Data , 0 , Number-1)
#印出排序後的資料
print('After Sort(Big -> Small): \n', Sorted_Data)






