'''
5.1 比大小
'''

'''
def max(a, b, c):
   # write your code here
  if a>b:
    tmp = a
    a = b
    b = tmp
  if b>c:
    tmp = b
    b = c
    c = tmp
  if a>b:
    tmp = b
    b = a
    a = tmp
  return c

# 以下勿改
x = eval(input())
y = eval(input()) 
z = eval(input()) 

r = max(x, y, z) 
print (r)

'''


'''
5.2 驗證身分證
'''

'''
trans = {'A':'10', 'B':'11', 'C':'12', 'D':'13', 'E':'14', 'F':'16', 'H':'17', 'J':'18', 'K':'19', 'L':'20', 'M':'21', 'N':'22',
'P':'23', 'Q':'24', 'R':'25', 'S':'26', 'T':'27', 'U':'28', 'V':'29', 'X':'30', 'Y':'31', 'W':'32', 'Z':'33', 'I':'34', 'O':'35'}

def checkSSN(ssn): # 此行勿改
  x = int(trans[ssn[0]][0])*1 + int(trans[ssn[0]][1])*9
  lst = [0,8,7,6,5,4,3,2,1,1]
  for i in range(1,len(ssn)):
    x = x + int(ssn[i])*lst[i]

  if x%10==0:
    return 'T'
  else:
    return 'F'

ssn = input('')
r = checkSSN(ssn)
print(r) # 此行勿改
'''

'''
5.3 幾Ａ幾Ｂ
'''

'''
def AB(s1,s2): # 此行勿改
  l1 = [];l2 = []
  c1 = 0;c2 = 0
  for i in str(s1):
    l1.append(int(i))

  for j in str(s2):
    l2.append(int(j))

  for k in range(5):
    if (l1[k] == l2[k]):
      c1 = c1 +1

    elif (l2.count(l1[k])!=0):
      if (l2.index(l1[k])!=k):
        c2 = c2 +1
  return c1,c2

# 以下程式勿改
s1, s2 = eval(input())
a, b = AB(s1,s2)
print (a, b)
'''


'''
5.4 星期幾
'''

'''
# Hint: 建立 md 這樣的 dict 來記錄每月的天數，用此資訊來計算星期幾
md = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
      7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def get_day(m, d):
    x = 0
    for i in range(1, m):
        x += md[i]
        #print(i, x)

    x = ((x + d - 1) + 3) % 7
    return x


# Hint: 建立 w 這樣的 dict 來對應輸出的星期幾英文
w = {1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu',
     5: 'Fri', 6: 'Sat', 0: 'Sun'}

month, date = eval(input())
print(w[get_day(month, date)])

'''

'''
5.5 電影推薦
'''

'''
import json
rank = json.loads(input())
p = input()
def dis(rank,p,q):
    rank_sum = 0
    commons = 0
    for m in rank[p]:
        if m in rank[q]:
            commons = commons + 1
            r1 = rank[p][m]
            r2 = rank[q][m]
            rank_sum = rank_sum + (r1-r2)*(r1-r2)
        if commons != 0:
            d = round((rank_sum)**0.5,2)
        else:
            d = 100
    return d
def nearest(rank,p):
    min_all = []
    min_dis = 8
    for people in rank:
        if people == p:
            continue

        d = dis(rank,p,people)

        if d <= min_dis:
            min_dis = d
            nearest_p = people
            min_all.append([d,people])
    min_sam = []
    for same in min_all:
        if same[0] == d:
            min_sam.append(same[1])

    if len(min_sam)>1:
        for nam in min_sam:
            if p[0] == nam[0]:
                nearest_p = nam
    return nearest_p

def my_favorite(rank,q):
    movie_dict = rank[q]
    movie_r_list = []
    for m in movie_dict:
        movie_r_list.append([m,rank[q][m]])
    movie_r_list = sorted(movie_r_list,key = lambda x:x[-1],reverse = True)
    movie_list = []
    for i in movie_r_list:
        movie_list.append(i[0])
    return movie_list

def recommend(rank, p):
    q = nearest(rank,p)
    like_list = my_favorite(rank,q)

    for m in like_list:
        if not(m in my_favorite(rank,p)):
            not_watch = m
            break
        else:
            not_watch = "None"
    return not_watch





m = recommend(rank, p)
print (m)
'''