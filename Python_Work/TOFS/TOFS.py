import matplotlib.pyplot as plt
import pandas as pd
import numpy  as np

'''
轉檔
csv檔用記事本開啟 -> 另存新檔 -> 改utf-8格式 -> 存檔
'''


# 設定字型，使得可以讀取中文(window)
def setupFont_window():
    import matplotlib as mpl
    mpl.rcParams["font.sans-serif"] = ["KaiTi"]
    mpl.rcParams["font.serif"] = ["KaiTi"]


# 讀檔
def init_data():
    file_path = "TOFSF.csv"
    # header = 0就是說我會有這筆資料，它是有表頭的欄位說明
    # sno，各位看到這個sno，這個地方是每一個站，它的一個序號，str是強制轉成str
    df = pd.read_csv(file_path , header=0  , dtype={"學年度":str , "學期":str , "學校統計處":str})

    return df

def cc(df , s , list_n):

   x = ["學期內新辦理休學人數小計" , "因病學期內新辦理休學人數" , "因經濟困難學期內新辦理休學人數"]
   for i in x:
       temp = df.loc[s, i].sum()

       list_n.append(temp)
   return list_n

# 執行
setupFont_window()
df = init_data()

# 長條圖呈現每一區
#g = df["學校名稱"].str.contains("高雄")

#df.groupby(df.loc[g,"學校名稱"]).count()["學校統計處代碼"].plot.bar(df.loc[g,"在學學生數"],figsize=(8,8))
#plt.show()

# 資料過濾條件
school_year = df["學年度"]  == "105"
schoole_semester = df["學期"]  == "1"
school_name = df["學校名稱"].str.contains("逢甲")
school_class = df["學制班別"]  == "學士班(日間)"
school_sex = df["性別"] == "男"

# 資料過濾
s = school_year & schoole_semester & school_name & school_sex & school_class

# 
a = df.loc[s, "在學學生數"].sum()

list_n = []
x = ["學期內新辦理休學人數小計" , "因病學期內新辦理休學人數" , "因經濟困難學期內新辦理休學人數"]



list_n = cc(df , s , list_n)
number =  int(float(str(a.strip(",")).replace(",","")))
xx = np.array(list_n)
plt.pie(list_n, labels=x)
plt.show()


#print(df.loc[school_year & schoole_semester & school_name & school_sex & school_class , "在學學生數"])

#plt.show()
#df["tot"] = df[df]


























# 排序
# stationCount = df.groupby("sarea").count()[["sno"]]
# 那我們是要把 sno，rename 成 count 就它的這個數量
# stationCount.rename(columns={"sno":"Count"} , inplace=True)
# 進行排序
# stationCount = stationCount.sort_values(by="Count")
#stationCount["Count"].plot.bar(title="新北各區Youbike數量" , figsize=(10,10))

# 圓餅圖呈現每一區
#stationCount.plot.pie(y="Count" , autopct="%.1f" , figsize=(10,10) , title="新北各區Youbike車占比率")


# 地理分布圖
# x軸設定是lng，y軸是lat
# df2 = df[["lng" , "lat"]]
# df2.plot.scatter(x="lng" , y="lat" , figsize=(10,10))
# plt.show()






























