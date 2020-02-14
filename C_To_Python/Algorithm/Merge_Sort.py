import random

'''
合併排序法
Merge Sort
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
#方法: Merge (Initial_Data: 要排序的資料List , Ledt:左邊起始點 , Mid: 中間值 , Right:右邊起始點)(小 -> 大)
#==============================
def Merge_To_Big(Initial_Data , Left , Mid , Right):
    #拆分後的左半邊List
    Left_SubList = []
    #拆分後的右半邊List
    Right_SubList = []
    #左半邊List要比較的Value的位置
    Left_Pos = 0
    #右半邊List要比較的Value的位置
    Right_Pos = 0
    #用於將排序後的Value放入指定位置
    Initial_Pos = Left


    #將拆分後在左半邊的資料放入Left_SubList
    for i in range(Left , Mid+1):
        Left_SubList.append(Initial_Data[i])
    # 將拆分後在右半邊的資料放入Right_SubList
    for i in range(Mid+1 , Right+1):
        Right_SubList.append(Initial_Data[i])

    #==============================
    #(1)將左、右數列合併
    #==============================
    while(Left_Pos < len(Left_SubList) and Right_Pos < len(Right_SubList)):
        #如果左邊的Value <= 右邊的Value，<=是為了防止當左右Value相同的時候使用
        if(Left_SubList[Left_Pos] <= Right_SubList[Right_Pos]):
            #將比較小的Value放入
            Initial_Data[Initial_Pos] = Left_SubList[Left_Pos]
            #由於左半邊放入了Value，所以向後1個位置，以繼續比較
            Left_Pos = Left_Pos + 1

        #如果左邊的Value > 右邊的Value
        elif(Left_SubList[Left_Pos] > Right_SubList[Right_Pos]):
            #將比較小的Value放入
            Initial_Data[Initial_Pos] = Right_SubList[Right_Pos]
            #由於右半邊放入了Value，所以向後1個位置，以繼續比較
            Right_Pos = Right_Pos + 1

        #每放入1個排序後的Value，則向後1個新的位置
        Initial_Pos = Initial_Pos + 1

    #==============================
    #***下方兩個while，一次只會執行一個，另一個不會執行
    #==============================
    #==============================
    #由於上方(1)合併後，左右兩個其中一個數列可能已經都放入List中，而另一個數列還沒全部放入List，也沒有可以比較的Value，所以不會放入List，因此手動放入List
    #==============================
    while (Left_Pos < len(Left_SubList)):
            #將未放入的Value放入List
            Initial_Data[Initial_Pos] = Left_SubList[Left_Pos]
            #由於左半邊放入了Value，所以向後1個位置，以結束合併
            Left_Pos = Left_Pos + 1
            #每放入1個排序後的Value，則向後1個新的位置
            Initial_Pos = Initial_Pos + 1

    #==============================
    #由於上方(1)合併後，左右兩個其中一個數列可能已經都放入List中，而另一個數列還沒全部放入List，也沒有可以比較的Value，所以不會放入List，因此手動放入List
    #==============================
    while (Right_Pos < len(Right_SubList)):
            #將未放入的Value放入List
            Initial_Data[Initial_Pos] = Right_SubList[Right_Pos]
            #由於右半邊放入了Value，所以向後1個位置，以結束合併
            Right_Pos = Right_Pos + 1
            #每放入1個排序後的Value，則向後1個新的位置
            Initial_Pos = Initial_Pos + 1

    return Initial_Data



#==============================
#方法: Merge (Initial_Data: 要排序的資料List , Ledt:左邊起始點 , Mid: 中間值 , Right:右邊起始點)(大 -> 小)
#==============================
def Merge_To_Small(Initial_Data , Left , Mid , Right):
    #拆分後的左半邊List
    Left_SubList = []
    #拆分後的右半邊List
    Right_SubList = []
    #左半邊List要比較的Value的位置
    Left_Pos = 0
    #右半邊List要比較的Value的位置
    Right_Pos = 0
    #用於將排序後的Value放入指定位置
    Initial_Pos = Left


    #將拆分後在左半邊的資料放入Left_SubList
    for i in range(Left , Mid+1):
        Left_SubList.append(Initial_Data[i])
    # 將拆分後在右半邊的資料放入Right_SubList
    for i in range(Mid+1 , Right+1):
        Right_SubList.append(Initial_Data[i])

    #==============================
    #(1)將左、右數列合併
    #==============================
    while(Left_Pos < len(Left_SubList) and Right_Pos < len(Right_SubList)):
        #如果左邊的Value <= 右邊的Value，<=是為了防止當左右Value相同的時候使用
        if(Left_SubList[Left_Pos] <= Right_SubList[Right_Pos]):
            #將比較大的Value放入
            Initial_Data[Initial_Pos] = Right_SubList[Right_Pos]
            #由於右半邊放入了Value，所以向後1個位置，以繼續比較
            Right_Pos = Right_Pos + 1

        #如果左邊的Value > 右邊的Value
        elif(Left_SubList[Left_Pos] > Right_SubList[Right_Pos]):
            #將比較大的Value放入
            Initial_Data[Initial_Pos] = Left_SubList[Left_Pos]
            #由於左半邊放入了Value，所以向後1個位置，以繼續比較
            Left_Pos = Left_Pos + 1

        #每放入1個排序後的Value，則向後1個新的位置
        Initial_Pos = Initial_Pos + 1

    # ==============================
    # ***下方兩個while，一次只會執行一個，另一個不會執行
    # ==============================
    #==============================
    #由於上方(1)合併後，左右兩個其中一個數列可能已經都放入List中，而另一個數列還沒全部放入List，也沒有可以比較的Value，所以不會放入List，因此手動放入List
    #==============================
    while (Left_Pos < len(Left_SubList)):
            #將未放入的Value放入List
            Initial_Data[Initial_Pos] = Left_SubList[Left_Pos]
            #由於左半邊放入了Value，所以向後1個位置，以結束合併
            Left_Pos = Left_Pos + 1
            #每放入1個排序後的Value，則向後1個新的位置
            Initial_Pos = Initial_Pos + 1

    #==============================
    #由於上方(1)合併後，左右兩個其中一個數列可能已經都放入List中，而另一個數列還沒全部放入List，也沒有可以比較的Value，所以不會放入List，因此手動放入List
    #==============================
    while (Right_Pos < len(Right_SubList)):
            #將未放入的Value放入List
            Initial_Data[Initial_Pos] = Right_SubList[Right_Pos]
            #由於右半邊放入了Value，所以向後1個位置，以結束合併
            Right_Pos = Right_Pos + 1
            #每放入1個排序後的Value，則向後1個新的位置
            Initial_Pos = Initial_Pos + 1

    return Initial_Data


#==============================
#方法: Merge Sort(Initial_Data: 要排序的資料List , Ledt:左邊起始點 , Right:右邊起始點)(小 -> 大)
#==============================
def Merge_Sort_To_Big(Initial_Data , Left , Right):

    if (Left >= Right): return

    #中間值，用於決定從哪個位置Initial_Data拆分成2個數列，左邊數列、右邊數列
    Mid = (Left + Right) // 2

    #左邊數列
    Merge_Sort_To_Big(Initial_Data , Left , Mid)
    #右邊數列
    Merge_Sort_To_Big(Initial_Data, Mid+1 , Right)
    #合併
    Initial_Data = Merge_To_Big(Initial_Data , Left , Mid , Right)

    return Initial_Data


#==============================
#方法: Merge Sort(Initial_Data: 要排序的資料List , Ledt:左邊起始點 , Right:右邊起始點)(大 -> 小)
#==============================
def Merge_Sort_To_Small(Initial_Data , Left , Right):

    if (Left >= Right): return

    #中間值，用於決定從哪個位置Initial_Data拆分成2個數列，左邊數列、右邊數列
    Mid = (Left + Right) // 2

    #左邊數列
    Merge_Sort_To_Small(Initial_Data , Left , Mid)
    #右邊數列
    Merge_Sort_To_Small(Initial_Data, Mid+1 , Right)
    #合併
    Initial_Data = Merge_To_Small(Initial_Data , Left , Mid , Right)

    return Initial_Data

#=================================================================================
#執行
#=================================================================================

#==============================
#產生亂數，填滿要排序的資料
#==============================
#依照Number，產生幾次亂數
for i in range(0,Number):
    #Temp暫存亂數(0~9999)
    Temp = random.randint(0,9999)
    #把Tepm加進Initial_Data儲存起來
    Initial_Data.append(Temp)

#印出排序前的資料
print('Before Merge Sort: \n', Initial_Data)


#==============================
#執行Merge Sort
#==============================
#Merge Sort(小 -> 大)
Sorted_Data = Merge_Sort_To_Big(Initial_Data , 0 , Number-1)
#印出排序後的資料
print('After Merge Sort(Small -> Big): \n', Sorted_Data)

#Merge Sort(大 -> 小)
Sorted_Data = Merge_Sort_To_Small(Initial_Data , 0 , Number-1)
#印出排序後的資料
print('After Merge Sort(Big -> Small): \n', Sorted_Data)





