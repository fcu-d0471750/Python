

'''
現在有一個List，裡面的數字都已經由小到大排序好，現在會隨機加入一個正整數，請寫出當這個整數放入List後進行排序。
'''

'''

original_list = [1 ,4, 5, 16, 23, 31, 48, 95, 123 ,1514] # 此行勿改

new_input = eval(input()) # 此行勿改


original_list.append(new_input)

original_list.sort()



print(original_list) # 此行勿改
'''





'''
現在有二個 List，請將兩個List合併成一個 List。
'''

'''
original_list_one = [1,5,3,9,12] # 此行勿改

original_list_two = [32,154,313,151,12] # 此行勿改

original_list_one.extend(original_list_two)

print(original_list_one) # 此行勿改
'''





'''
共有三門課，10位學生(S1~S10)，每位學生都有各自選的課程，請印出有選2門課以上(包含2門)的學生。
'''
'''
C1 = {'S2','S5','S8','S9'} # 此行勿改
C2 = {'S10','S6','S4','S5'} # 此行勿改
C3 = {'S2','S3','S4','S5'} # 此行勿改

list_set = [] # 此行勿改
list_print = [] # 此行勿改

list_set.extend(list(C1&C2))
list_set.extend(list(C1&C3))
list_set.extend(list(C2&C3))

for i in list_set:
    if len(list_print) == 0 : list_print.append(i)
    else:
        for j in  list_print:
            if(i == j): break
            else :
                list_print.append(i)
                break

list_print.sort()

print(list_print) # 此行勿改

'''


'''
每張股票都有各自的代號、價格和漲跌幅，因為投資人資金有限，需進行一定篩選，請依篩選條件(多少價格以下，漲幅多少以上)選出符合條件的股票，印出其股票代號。
'''

'''
# 此dict勿改
stock_dict = {
    "number":['1000','1011','1033','1054','1900'],
    "prices": [99, 50, 148, 245, 12],
    "gains": [15, 20,56,95,30]
}

stock_list = []  # 此行勿改

price = eval(input())  # 此行勿改
gain = eval(input())  # 此行勿改

for i in range(len(stock_dict["number"])):
    if(stock_dict["prices"][i] >= price and stock_dict["gains"][i] >= gain) : stock_list.append(stock_dict["number"][i])



print(stock_list)  # 此行勿改

'''






'''
輸入兩個正整數，並寫一個函式max(input1,input2)，來回傳較大的整數，如果兩者一樣大，則印出相等。
'''

'''
def max(input1,input2): # 此行勿改
    if (input1 > input2): return input1
    elif (input1 < input2): return input2
    return "相等"

input1 = eval(input()) # 此行勿改
input2 = eval(input()) # 此行勿改

output = max(input1,input2)

print(output) # 此行勿改
'''


'''
1個List會包含許多不同型態的資料，但我們只需要int型態的資料，寫一個函式把其他型態的資料剔除，還一個乾淨的List。
'''

'''
def filter(input_list): # 此行勿改
    temp = []
    for i in input_list:
        if(type(i) == int): temp.append(i)

    return  temp

input_list = [1,5,'A','jack',True,[],False] # 此行勿改

output = filter(input_list) # 此行勿改

print(output) # 此行勿改
'''







