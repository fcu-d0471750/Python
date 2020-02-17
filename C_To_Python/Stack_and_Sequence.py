import random

'''
Python Stack(堆疊) 和 Sequence(佇列)
'''

#=================================================================================
#宣告變數
#=================================================================================
#List: 堆疊測試用List
Stack_Number_list = []

#List: 佇列測試用List
Sequence_Number_list = []

#int: 共幾筆資料
Number = 10

#int: 暫存亂數
Temp = 0

#==============================
#(堆疊執行)
#==============================

#新增資料到Stack_Number_list
for i in range(0,Number):
    #依照Number，產生幾次亂數
    Temp = random.randint(0,100)
    #把Tepm加進Stack_Number_list儲存起來，像是push
    Stack_Number_list.append(Temp)

#印出Stack_Number_list
print(Stack_Number_list)

#==============================
#(堆疊 先進後出FILO)
#==============================

#拿出Stack_Number_list的內容，像是pop
print('pop: ' , Stack_Number_list.pop())
#印出拿出Stack_Number_list的內容的Number_list
print(Stack_Number_list)

#拿出Stack_Number_list的內容，像是pop
print('pop: ' , Stack_Number_list.pop())
#印出拿出Stack_Number_list的內容的Stack_Number_list
print(Stack_Number_list)


#==============================
#(換行)
#==============================
print()

#==============================
#(佇列執行)
#==============================

#新增資料到Sequence_Number_list
for i in range(0,Number):
    #依照Number，產生幾次亂數
    Temp = random.randint(0,100)
    #把Tepm加進Sequence_Number_list儲存起來，像是push
    Sequence_Number_list.append(Temp)

#印出Sequence_Number_list
print(Sequence_Number_list)


#==============================
#(序列 先進先出FIFO)
#==============================

#拿出Sequence_Number_list的內容，像是pop
print('pop: ' , Sequence_Number_list.pop(0))
#印出拿出Sequence_Number_list的內容的Sequence_Number_list
print(Sequence_Number_list)

#拿出Sequence_Number_list的內容，像是pop
print('pop: ' , Sequence_Number_list.pop(0))
#印出拿出Sequence_Number_list的內容的Sequence_Number_list
print(Sequence_Number_list)














