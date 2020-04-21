'''
pandas 基本操作

import pandas as pd
import numpy  as np

f = {"Name":["Apple" , "Banana" , "Cherry" , "Durian"]  ,
     "Price":[10 , 12 , 20 ,30] ,
     "Quantity":[90 , 87 , 23 , 45]
     }

df = pd.DataFrame(f)

print(df)
'''



'''
pandas 基本操作

import pandas as pd
import numpy  as np

f = {"Name":["Apple" , "Banana" , "Cherry" , "Durian"]  ,
     "Price":[10 , 12 , 20 ,30] ,
     "Quantity":[90 , 87 , 23 , 45]
     }

df = pd.DataFrame(f , index=f["Name"])

print(df,"\n")
print(df.Price,"\n")
print(df.loc["Apple"],"\n")

# By index
print("By index")
print(df.loc[["Apple", "Banana"]],"\n")

# By Position
print("By Position")
print(df.iloc[1:4],"\n")

# 前n筆資料
print("前n筆資料")
print(df.head(4),"\n")

# 後n筆資料
print("後n筆資料")
print(df.tail(3),"\n")

# 隨機n筆資料
print("隨機n筆資料")
print(df.sample(2),"\n")
'''

'''
pandas 資料過濾

import pandas as pd
import numpy  as np

f = {"Name":["Apple" , "Banana" , "Cherry" , "Durian"]  ,
     "Price":[10 , 12 , 20 ,30] ,
     "Quantity":[90 , 87 , 23 , 45]
     }

df = pd.DataFrame(f)

# 過濾條件
g = df.Price > 10
# 印出結果、等同df.loc[g]
print(df[g] , "\n")
'''

'''
讀檔


import pandas as pd

df = pd.read_csv("grade.csv")
print(df)
'''




'''
增加欄位


import pandas as pd


f = {"Name":["Apple" , "Banana" , "Cherry" , "Durian"]  ,
     "Price":[10 , 12 , 20 ,30] ,
     "Quantity":[90 , 87 , 23 , 45]
     }



df = pd.DataFrame(f)
print(df,"\n")

# Serious是一個一維table(one column)
q = pd.Series([-1,2,0,-1] )
# 新增欄位 品質
df["Quality"] = q
print(df,"\n")

# Serious是一個一維table(one column)
loc = pd.Series(["tw","usa","jpn","eu"])
# 新增欄位 品質
df["Loc"] = loc
print(df,"\n")
'''



'''
Append，新增一組資料


import pandas as pd


f = {"Name":["Apple" , "Banana" , "Cherry" , "Durian"]  ,
     "Price":[10 , 12 , 20 ,30] ,
     "Quantity":[90 , 87 , 23 , 45]
     }

f2 = {"Name":["Pear" , "Peach" ] ,
     "Price":[15 , 23] ,
     "Quantity":[88 , 56]
      }


df = pd.DataFrame(f)
print(df,"\n")

df2 = pd.DataFrame(f2 ,index=["4","5"])
# 新增一組資料(two column)
df = df.append(df2)
print(df,"\n")
'''



'''
排序


import pandas as pd


f = {"Name":["Apple" , "Banana" , "Cherry" , "Durian"]  ,
     "Price":[10 , 12 , 20 ,30] ,
     "Quantity":[90 , 87 , 23 , 45]
     }



df = pd.DataFrame(f)
print(df,"\n")

# 用Price遞減
print(df.sort_values(by="Price" , ascending=False))
'''




'''
資料遺失處理


import pandas as pd


def reset_data():
     f = {"Name": ["Apple", "Banana", "Cherry", "Durian"],
          "Price": [10, 12, 20, None],
          "Quantity": [90, 87, None, 45]
          }

     df = pd.DataFrame(f , index=f["Name"])
     return  (df)


df = reset_data()

# 把空值資料刪除
print(df,"\n")
print(df.dropna(),"\n")
print(df,"\n")

# 把空值填0
print(df.fillna(0),"\n")
print(df,"\n")

# 依欄位名稱，決定空值填甚麼資料
d = {"Price":10 , "Quantity":40}
print(df.fillna(d))
'''


'''
資料表合併(Meage，不同欄位)


import pandas as pd



f1 = {"Name": ["Apple", "Banana", "Cherry", "Durian"],
          "Price": [10, 12, 20, None],
          "Quantity": [90, 87, None, 45]
          }

f2 = {"Name": ["Apple", "Banana"],
     "Age": [10, 33],
      "Prod": ["tw", "jpn"]
          }


df1 = pd.DataFrame(f1)

df2 = pd.DataFrame(f2)

m_df = pd.merge(df1,df2,on="Name")
print(m_df)
'''


'''
圖表繪製
'''
import matplotlib.pyplot as plt
import pandas as pd
import random as r

g1 = r.sample(range(1,100),5)
g2 = r.sample(range(40,100),5)
g3 = r.sample(range(1,70),5)
gender = {"gril":[16,20,30],"boy":[34,30,20]}

# 產生dataframe物件
s1 = pd.DataFrame(g1)
s2 = pd.DataFrame(g2)
s = pd.DataFrame({"Eng":g1,"Math":g2,"Phy":g3})

sg = pd.DataFrame(gender , index=["c1","c2","c3"])

# 印出圖表(折線圖)
#s.plot(title="Student Grade")
plt.plot(s)
plt.show()










