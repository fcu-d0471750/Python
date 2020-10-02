

'''
現在有一個List，裡面的數字都是字串形態，現在會隨機加入一個正整數，請寫出當這個整數放入List後進行排序。
'''


#original_list = [1,4,5,16,23,31,48,95,123,1514] # 此行勿改
'''
input_string = input()  # 此行勿改

original_list = input_string.split(',')  # 此行勿改

new_list = []  # 此行勿改

new_input = eval(input()) # 此行勿改


original_list.append(new_input)

for i in original_list:
    new_list.append(int(i))

new_list.sort()

for count in range(len(new_list)): # 此行勿改
    print(new_list[count],end=' ') # 此行勿改

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
#C1 = {'S2','S5','S8','S9'} # 此行勿改
#C2 = {'S10','S6','S4','S5'} # 此行勿改
#C3 = {'S2','S3','S4','S5'} # 此行勿改

input_string  = input()  # 此行勿改
original_list = input_string.split(' ')  # 此行勿改
C1 = set(original_list) # 此行勿改

input_string  = input()  # 此行勿改
original_list = input_string.split(' ')  # 此行勿改
C2 = set(original_list) # 此行勿改

input_string  = input()  # 此行勿改
original_list = input_string.split(' ')  # 此行勿改
C3 = set(original_list) # 此行勿改

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

'''
set去重，一個字串裡面包含著重複的英文字母，請印出這個字串包含的英文字母。ajldjlajfdljfddd  dsgsdgdfasfsdgmhm
'''

'''
input_string  = input() # 此行勿改
res = [] # 此行勿改

b = list(input_string)

res = sorted(set(b))

for count in range(len(res)): # 此行勿改
    print(res[count],end='') # 此行勿改

'''

'''
tall_list = input().split(',')  # 此行勿改
new_tall = eval(input()) # 此行勿改
tall_list = list(map(int,tall_list)) # 此行勿改

new_list = tall_list[:]
new_list.append(new_tall)
new_list.sort()

# 以下勿改
for h in new_list:
   print(h, end=' ')
'''


'''
c = "25 40 15 36 42"
city = 'taoyuan taichung hsinchu tainan changhua'

c = c.split()
city = city.split()

c2 = [int(i)*9/5 + 32 for i in c]
hot_city = []

for i, t in enumerate(c2):
   if t > 100:
      hot_city.append(city[i])

for ht in hot_city:
   print (ht)
'''

'''
names = 'mary joe evo robert'
eng = '25,33,39,66'
math = '78,44,70,67'
phy = '90,60,45,40'

names = names.split()
eng = eval(eng)
math = eval(math)
phy = eval(phy)

g_pass = []
for i, name in enumerate(names):
  av = (eng[i] + math[i] + phy[i])/3
  if (av >= 60):
    g_pass.append(names[i])

print (' '.join(g_pass))
'''
'''
names = 'x f q e'
eng = '45, 70, 85, 55'
math = '19, 85, 65, 36'
phy = '99, 100, 50, 99'

names = names.split()
eng = eval(eng)
math = eval(math)
phy = eval(phy)

eng_av = sum(eng)/len(eng)
math_av = sum(math)/len(math)
phy_av = sum(phy)/len(phy)

g_good = []
for i, name in enumerate(names):
  higher_grade = (eng[i] >= eng_av and math[i] >= math_av and phy[i] >= phy_av)
  if (higher_grade):
    g_good.append(name)

print (' '.join(g_good))

'''



'''
health = input()
#{"John": {"height": 171, "weight": 50}, "Nick": {"height": 175, "weight": 65}}
#{"Mary": {"height": 154, "weight": 40}, "Nicolas": {"height": 180, "weight": 85}, "Nei": {"height": 168, "weight": 55}, "Gold": {"height": 175, "weight": 75}}
import json
health = json.loads(health)
high_bmi = 0

for name, h in health.items():
  bmi = h['weight']/(h['height']/100)**2
  if (bmi > high_bmi):
    high_bmi = bmi
    r = name

print (r)
'''

'''
myDic = '{"seagull":"海鷗", "pigeon":"鴿子", "crane":"鶴", "eagle":"老鷹", "sparrow":"麻雀"}'
find = input()
import json
myDic = json.loads(myDic)



myDic2 = {}
for eng, ch in myDic.items():
   if(ch == find):
    print (eng)

'''

'''
import traceback
s = "import time;print(time.localtime())"
try:
    code = compile(s, '<string>', 'exec')
    exec(code)
except Exception as e:
    print(traceback.format_exc())

'''


'''
修課學生
'''

'''
c1 = input().split(' ')  # 此行勿改
c2 = input().split(' ')  # 此行勿改
c3 = input().split(' ')  # 此行勿改

c_all = []
c_all.extend(c1)
c_all.extend(c2)
c_all.extend(c3)

s_all = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10']

t0 = [x for x in s_all if c_all.count(x) == 0]
t1 = [x for x in s_all if c_all.count(x) == 1]
t2 = [x for x in s_all if c_all.count(x) == 2]
t3 = [x for x in s_all if c_all.count(x) == 3]

print('-' if len(t0) == 0 else ' '.join(t0))
print('-' if len(t1) == 0 else ' '.join(t1))
print('-' if len(t2) == 0 else ' '.join(t2))
print('-' if len(t3) == 0 else ' '.join(t3))
'''
#print('-' if len(t1) == 0 else ' '.join(t1))
#print('-' if len(t2) == 0 else ' '.join(t2))
#print('-' if len(t3) == 0 else ' '.join(t3))







