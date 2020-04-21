'''
新北 YourBike 分析
所有plot.XXX表示要視覺化的資料
在下方加上plt.show()
一次只能選一行plot.XXX，不然會前面的蓋掉後面的
'''
import matplotlib.pyplot as plt
import pandas as pd
import numbers as np


# 設定字型，使得可以讀取中文(mac)
def setupFont_mac():
    import matplotlib as mpl
    from matplotlib.font_manager import _rebuild
    _rebuild()
    mpl.rcParams["font.sans-serif"] = [u"SimHei"]
    mpl.rcParams["axes.unicode_minus"] = False

# 設定字型，使得可以讀取中文(window)
def setupFont_window():
    import matplotlib as mpl
    mpl.rcParams["font.sans-serif"] = ["KaiTi"]
    mpl.rcParams["font.serif"] = ["KaiTi"]

# 讀檔
def init_data():
    file_path = "YouBike.csv"
    # header = 0就是說我會有這筆資料，它是有表頭的欄位說明
    # sno，各位看到這個sno，這個地方是每一個站，它的一個序號，str是強制轉成str
    df = pd.read_csv(file_path , header=0 , dtype={"sno":str})

    return df

# 執行
setupFont_window()
df = init_data()

# 長條圖呈現每一區
#df.groupby("sarea").count()["sno"].plot.bar(figsize=(10,10))

# 排序
stationCount = df.groupby("sarea").count()[["sno"]]
# 那我們是要把 sno，rename 成 count 就它的這個數量
stationCount.rename(columns={"sno":"Count"} , inplace=True)
# 進行排序
stationCount = stationCount.sort_values(by="Count")
#stationCount["Count"].plot.bar(title="新北各區Youbike數量" , figsize=(10,10))

# 圓餅圖呈現每一區
#stationCount.plot.pie(y="Count" , autopct="%.1f" , figsize=(10,10) , title="新北各區Youbike車占比率")


# 地理分布圖
# x軸設定是lng，y軸是lat
df2 = df[["lng" , "lat"]]
df2.plot.scatter(x="lng" , y="lat" , figsize=(10,10))
plt.show()



# 借出率
# 只計算有營運的
#df2 = df[df.act == 1]
#df2["rate"] = (1 - (df2["sbi"] / df["tot"])) * 100.0
#print(df2["bemp"])
#df2["rate"] = round(df2["rate"] , 1)
#df2["rate"].describe()
#df2[["rate"]].boxplot()












