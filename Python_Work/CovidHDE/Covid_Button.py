import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.animation as animation

'''
宣告變數
,usecols=['Country/Region', 'Date', 'Value']
'''

fig, ax = plt.subplots(figsize=(15, 4))

# 確診總人數list
list_tot_confirmed = []

list_date = []

'''
colors = dict(zip(
    ["香港", "中國大陸", "日本", "南韓", "馬來西亞", "新加坡", "印尼","菲律賓","泰國","越南","加拿大","美國","法國","德國","義大利","荷蘭","英國","澳大利亞","南非",'澳門'],
    ["#2E86AB", "#424B54", "#00A6A6", "#F24236", "#9E643C", "#f7bb5f", "#EDE6F2","#E9D985", "#8C4843", "#90d595", "#e48381", "#090446", "#f7bb5f", "#eafb50","#adb0ff",
     "#ffb3ff", "#90d595", "#e48381", "#aafbff",'#746D75']
))
'''
colors = dict(zip(
    ["Taiwan*", "Japan", "Korea, South", "南韓", "馬來西亞", "新加坡", "印尼","菲律賓","泰國","越南","加拿大","美國","法國","德國","義大利","荷蘭","英國","澳大利亞","南非",'澳門'],
    ["#2E86AB", "#424B54", "#00A6A6"]
))

# 讀資料
def ini_data():
    #url = "https://data.humdata.org/hxlproxy/data/download/time_series_covid19_confirmed_global_narrow.csv?dest=data_edit&filter01=merge&merge-url01=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2Fe%2F2PACX-1vTglKQRXpkKSErDiWG6ycqEth32MY0reMuVGhaslImLjfuLU0EUgyyu2e-3vKDArjqGX7dXEBV8FJ4f%2Fpub%3Fgid%3D1326629740%26single%3Dtrue%26output%3Dcsv&merge-keys01=%23country%2Bname&merge-tags01=%23country%2Bcode%2C%23region%2Bmain%2Bcode%2C%23region%2Bsub%2Bcode%2C%23region%2Bintermediate%2Bcode&filter02=merge&merge-url02=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2Fe%2F2PACX-1vTglKQRXpkKSErDiWG6ycqEth32MY0reMuVGhaslImLjfuLU0EUgyyu2e-3vKDArjqGX7dXEBV8FJ4f%2Fpub%3Fgid%3D398158223%26single%3Dtrue%26output%3Dcsv&merge-keys02=%23adm1%2Bname&merge-tags02=%23country%2Bcode%2C%23region%2Bmain%2Bcode%2C%23region%2Bsub%2Bcode%2C%23region%2Bintermediate%2Bcode&merge-replace02=on&merge-overwrite02=on&filter03=explode&explode-header-att03=date&explode-value-att03=value&filter04=rename&rename-oldtag04=%23affected%2Bdate&rename-newtag04=%23date&rename-header04=Date&filter05=rename&rename-oldtag05=%23affected%2Bvalue&rename-newtag05=%23affected%2Binfected%2Bvalue%2Bnum&rename-header05=Value&filter06=clean&clean-date-tags06=%23date&filter07=sort&sort-tags07=%23date&sort-reverse07=on&filter08=sort&sort-tags08=%23country%2Bname%2C%23adm1%2Bname&tagger-match-all=on&tagger-default-tag=%23affected%2Blabel&tagger-01-header=province%2Fstate&tagger-01-tag=%23adm1%2Bname&tagger-02-header=country%2Fregion&tagger-02-tag=%23country%2Bname&tagger-03-header=lat&tagger-03-tag=%23geo%2Blat&tagger-04-header=long&tagger-04-tag=%23geo%2Blon&header-row=1&url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv"
    #df = pd.read_csv(url, header=0)
    file_path = "Covid_confirmed.csv"
    df = pd.read_csv(file_path,usecols=['Country/Region', 'Date', 'Value'])
    df = df.fillna(value=0)
    # 刪掉第2列header
    df = df.drop(axis=0, index=0)
    # 將資料型別轉換為日期型別
    df["Date"] = pd.to_datetime(df["Date"])

    return df


# 資料過濾條件
def data_filiter(df):
    Region = df["Country/Region"].isin(["Taiwan*","Japan","Korea, South"])
    Start_Date = df["Date"] >= "2020/1/22"
    End_Date = df["Date"] <= "2020/4/26"
    Date = Start_Date & End_Date
    data_f = Region

    return data_f

def race_barchart(input_year):
    dff = done[done['Date'].eq(input_year)].sort_values(by='Value', ascending=True)
    dff['Country/Region'] = dff['Country/Region'].astype(str)
    dff['Value'] = dff['Value'].astype(float)

    ax.clear()
    ax.barh(dff['Country/Region'], dff['Value'], height=0.8,color=[colors[x] for x in dff['Country/Region']])


    for i, (value, name) in enumerate(zip(dff['Value'], dff['Country/Region'])):
        ax.text(0, i, name + ' ', size=16, weight=600, ha='right', va='center')  # 將每個國家名稱放到對應的長條旁邊
        ax.text(value, i,f'{value:,.0f}',  size=16, ha='left',  va='center') # 將確診人數放到對應的長條旁邊


    ax.text(0.9, 0.2, input_year, transform=ax.transAxes, color='#777777', size=12, ha='right', weight=1000)  # 增加日期
    ax.text(0, 1.06, 'confirmed', transform=ax.transAxes, size=14, color='#777777') # 小標題

    ax.tick_params(axis='x', colors='#777777', labelsize=12)  # 調整橫軸顏色、標籤大小
    ax.xaxis.set_ticks_position('top')  # 將橫軸放到頂端
    ax.set_yticks([])
    ax.margins(0, 0.01)

    ax.grid(which='major', axis='x', linestyle='-')  # 增加格線


# 執行
df = ini_data()

# 資料過濾
data_filter = data_filiter(df)
done = df[data_filter]


month = list(set(df.Date.values))
month.sort()

animator = animation.FuncAnimation(fig, race_barchart, frames=month,repeat=False)

plt.show()



























