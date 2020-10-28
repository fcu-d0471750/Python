'''
4.1 重新排序的身高
'''

'''
tall_list = input().split(',')  # 此行勿改
new_tall = eval(input()) # 此行勿改
new_list = []

new_list = tall_list[:]
new_list.append(new_tall)
new_list = list(map(int, new_list))
new_list.sort()

# 以下勿改
for h in new_list:
   print(h, end=' ')

'''

'''
4.2 哪裡溫度高
'''

'''
c = input().split()
city = input().split()
# 以上勿改


# Write your code
c2 = [int(i)*9/5 + 32 for i in c]
hot_city = []

for i, t in enumerate(c2):
   if t > 100:
      hot_city.append(city[i])


# 以下勿改
for hc in hot_city:
   print(hc)
'''

'''
4.3 及格的學生
'''

'''
names = input().split()
eng = eval(input())
math = eval(input())
phy = eval(input())
# 以上勿改
# Write your code
g_pass = []
for i, name in enumerate(names):
  print(eng[i] + math[i] + phy[i])
  av = (eng[i] + math[i] + phy[i])/3
  if (av >= 60):
    g_pass.append(names[i])

# 以下勿改， g_pass 是有通過的學生的 list
print (' '.join(g_pass))
'''

'''
4.4 及格的學生
'''

'''
names = input().split()
eng = eval(input())
math = eval(input())
phy = eval(input())
# 以上勿改

# Write your code
eng_av = sum(eng)/len(eng)
math_av = sum(math)/len(math)
phy_av = sum(phy)/len(phy)

g_good = []
for i, name in enumerate(names):
  higher_grade = (eng[i] >= eng_av and math[i] >= math_av and phy[i] >= phy_av)
  if (higher_grade):
    g_good.append(name)


# 以下勿改， g_good 是高於平均的姓名的 list
print (' '.join(g_good))
'''



'''
4.5 OJ 去掉重複的
'''

'''
s = input() # 此行勿改
# Write Your Code
res = []  

b = list(s) 
res = sorted(set(b)) 

for count in range(len(res)): 
 print(res[count],end='') 
'''

'''
4.6  OJ 修課的學生
'''

'''
c1 = input().split(' ')  # 此行勿改
c2 = input().split(' ')  # 此行勿改
c3 = input().split(' ')  # 此行勿改

# 印出時請注意格式，避免有多餘的空格
# Write Your Code
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


'''
4.7 誰的 BMI 最高
'''

'''
import json
health = json.loads(input())
high_bmi = 0

for name, h in health.items():
 bmi = h['weight']/(h['height']/100)**2
 #print (bmi, name)
 if (bmi > high_bmi):
   high_bmi = bmi
   r = name

print (r)
'''


'''
4.8 中英字典
'''

'''
import json
myDic = json.loads(input())
find = input()  # 要查詢的中文字
# 以上區塊勿改

# Write Your Code
for eng,ch in myDic.items():
 if(ch == find):
   print(eng)
'''



c1 = input().split(' ')  # 此行勿改
c2 = input().split(' ')  # 此行勿改
c3 = input().split(' ')  # 此行勿改

# 印出時請注意格式，避免有多餘的空格
# Write Your Code
#sum_c=c1.extend(c2)

c1.extend(c2)
c1.extend(c3)

'''
s_all = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10']

t0 = [x for x in s_all if c1.count(x) == 0]
t1 = [x for x in s_all if c1.count(x) == 1]
t2 = [x for x in s_all if c1.count(x) == 2]
t3 = [x for x in s_all if c1.count(x) == 3]


print('-' if len(t0) == 0 else ' '.join(t0))
print('-' if len(t1) == 0 else ' '.join(t1))
print('-' if len(t2) == 0 else ' '.join(t2))
print('-' if len(t3) == 0 else ' '.join(t3),end='')

print(t0)
print(t1)
print(t2)
print(t3)
'''

target={'s1': 0, 's2': 0, 's3': 0, 's4': 0, 's5': 0, 's6': 0, 's7': 0, 's8': 0, 's9': 0, 's10': 0}
st=[]



#計數
for ci, cv in enumerate(c1):
  if c1[ci] in target:
    target[c1[ci]] = target[c1[ci]] + 1
  else:
    target[c1[ci]]=1
#分類
t0 =[]
t1 =[]
t2 =[]
t3 =[]
for (key, value) in target.items():
  if(value == 0) : t0.append(key)
  if (value == 1): t1.append(key)
  if (value == 2): t2.append(key)
  if (value == 3): t3.append(key)

#輸出、並處理0轉-的值
print('-' if len(t0) == 0 else ' '.join(t0))
print('-' if len(t1) == 0 else ' '.join(t1))
print('-' if len(t2) == 0 else ' '.join(t2))
print('-' if len(t3) == 0 else ' '.join(t3))



'''
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















