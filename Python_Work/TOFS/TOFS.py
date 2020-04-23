import matplotlib.pyplot as plt
import pandas as pd
import numpy  as np

'''
轉檔
csv檔用記事本開啟 -> 另存新檔 -> 改utf-8格式 -> 存檔
'''

'''
宣告變數
'''

# 資料人數
data_list = []

# 資料過濾總合
data_filter = []

# 要取得人數的資料欄位
data_field = ["因病至學期底總休學人數", "因經濟困難至學期底總休學人數", "因學業成績至學期底總休學人數", "因志趣不合至學期底總休學人數", "因工作需求至學期底總休學人數", "因懷孕至學期底總休學人數",
     "因育嬰至學期底總休學人數", "因兵役至學期底總休學人數", "因出國至學期底總休學人數", "因論文至學期底總休學人數", "因適應不良至學期底總休學人數", "因家人傷病至學期底總休學人數", "因考試訓練至學期底總休學人數",
     "其他至學期底總休學人數"]

# x標籤
data_xlabel = ["生病","經濟困難" , "學業成績" , "興趣不合" , "工作需求" , "懷孕" , "育嬰" , "兵役" , "出國" , "論文" , "適應不良" , "家人傷病" , "考試訓練" , "其它"]

'''
宣告方法
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

# 計算人數
def cal(df , s , list_n , x):
   for i in x:
       temp = df.loc[s, i].sum()
       list_n.append(temp)
   return list_n

# 資料過濾條件
def data_filiter(df):
    school_year = df["學年度"] == "105"
    schoole_semester = df["學期"] == "1"
    school_name = df["學校名稱"].str.contains("逢甲")
    school_class = df["學制班別"] == "學士班(日間)"
    school_sex = df["性別"] == "男"

    data_f = school_year & schoole_semester & school_name & school_sex & school_class

    return data_f

# 柱狀圖(直向)
def show_bar_s():
    # (X軸編號,資料(人數),本體顏色,邊框顏色)
    plt.bar(data_xlabel, data_list, facecolor='#9999ff', edgecolor='white', width=0.8)
    # 標籤垂直
    plt.xticks(rotation='vertical')
    # 柱狀圖加上印出數值
    for x, y in zip(data_xlabel, data_list):
        plt.text(x, y, y,  va='bottom' , ha="center")
    plt.show()

# 柱狀圖(橫向)
def show_bar_h():
    # (X軸編號,資料(人數))
    plt.barh(data_xlabel, data_list)
    # 柱狀圖加上數值
    for x, y in zip(data_xlabel, data_list):
        plt.text(y + 2.0, x, y, va='center', fontsize=9)
    plt.show()

# 圓餅圖
def show_pie():
    data_list_pie = []
    data_xlabel_pie = []
    # 移除數值為0的資料
    for i in range(0,len(data_list)):
        if data_list[i] != 0:
            data_list_pie.append(data_list[i])
            data_xlabel_pie.append(data_xlabel[i])
    # (原始)圓餅圖
    #plt.pie(data_list, labels=data_xlabel , autopct="%1.1f%%" , shadow=True)
    # (移除數值0)圓餅圖
    plt.pie(data_list_pie, labels=data_xlabel_pie , autopct="%1.1f%%" , shadow=True)
    plt.show()


# 執行
setupFont_window()
df = init_data()

# 資料過濾
data_filter = data_filiter(df)

# 計算人數
data_list = cal(df , data_filter , data_list , data_field)

#圓餅圖
show_pie()

# 柱狀圖
# show_bar_h()

#number =  int(float(str(a.strip(",")).replace(",","")))






















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






























