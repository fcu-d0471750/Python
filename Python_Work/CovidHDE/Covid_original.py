import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import animation, rc
from IPython.display import HTML


'''
宣告變數
'''

# 畫布
fig, ax = plt.subplots(figsize=(15, 6))

# 長條圖顏色
colors = dict(zip(
    ["Taiwan*", "Japan", "Korea, South","Italy"],
    ["#FFE4E1", "#D8BFD8", "#BC8F8F", "#FFEFD5"]
))

# 讀資料(確診)
def ini_data_confirmed():
    #url = "https://data.humdata.org/hxlproxy/data/download/time_series_covid19_confirmed_global_narrow.csv?dest=data_edit&filter01=merge&merge-url01=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2Fe%2F2PACX-1vTglKQRXpkKSErDiWG6ycqEth32MY0reMuVGhaslImLjfuLU0EUgyyu2e-3vKDArjqGX7dXEBV8FJ4f%2Fpub%3Fgid%3D1326629740%26single%3Dtrue%26output%3Dcsv&merge-keys01=%23country%2Bname&merge-tags01=%23country%2Bcode%2C%23region%2Bmain%2Bcode%2C%23region%2Bsub%2Bcode%2C%23region%2Bintermediate%2Bcode&filter02=merge&merge-url02=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2Fe%2F2PACX-1vTglKQRXpkKSErDiWG6ycqEth32MY0reMuVGhaslImLjfuLU0EUgyyu2e-3vKDArjqGX7dXEBV8FJ4f%2Fpub%3Fgid%3D398158223%26single%3Dtrue%26output%3Dcsv&merge-keys02=%23adm1%2Bname&merge-tags02=%23country%2Bcode%2C%23region%2Bmain%2Bcode%2C%23region%2Bsub%2Bcode%2C%23region%2Bintermediate%2Bcode&merge-replace02=on&merge-overwrite02=on&filter03=explode&explode-header-att03=date&explode-value-att03=value&filter04=rename&rename-oldtag04=%23affected%2Bdate&rename-newtag04=%23date&rename-header04=Date&filter05=rename&rename-oldtag05=%23affected%2Bvalue&rename-newtag05=%23affected%2Binfected%2Bvalue%2Bnum&rename-header05=Value&filter06=clean&clean-date-tags06=%23date&filter07=sort&sort-tags07=%23date&sort-reverse07=on&filter08=sort&sort-tags08=%23country%2Bname%2C%23adm1%2Bname&tagger-match-all=on&tagger-default-tag=%23affected%2Blabel&tagger-01-header=province%2Fstate&tagger-01-tag=%23adm1%2Bname&tagger-02-header=country%2Fregion&tagger-02-tag=%23country%2Bname&tagger-03-header=lat&tagger-03-tag=%23geo%2Blat&tagger-04-header=long&tagger-04-tag=%23geo%2Blon&header-row=1&url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv"
    #df = pd.read_csv(url,usecols=['Country/Region', 'Date', 'Value'])
    # 檔案位置
    file_path = "Covid_confirmed.csv"
    # 讀檔，只讀取'Country/Region', 'Date', 'Value'三個column
    df = pd.read_csv(file_path,usecols=['Country/Region', 'Date', 'Value'])
    # 將空值填0
    df = df.fillna(value=0)
    # 刪掉第2列header
    df = df.drop(axis=0, index=0)
    # 將資料型別轉換為日期型別
    df["Date"] = pd.to_datetime(df["Date"])

    return df

# 讀資料(死亡)
def ini_data_deaths():
    # 檔案位置
    file_path = "Covid_deaths.csv"
    # 讀檔，只讀取'Country/Region', 'Date', 'Value'三個column
    df = pd.read_csv(file_path,usecols=['Country/Region', 'Date', 'Value'])
    # 將空值填0
    df = df.fillna(value=0)
    # 刪掉第2列header
    df = df.drop(axis=0, index=0)
    # 將資料型別轉換為日期型別
    df["Date"] = pd.to_datetime(df["Date"])

    return df

# 讀資料(康復)
def ini_data_recovered():
    # 檔案位置
    file_path = "Covid_recovered.csv"
    # 讀檔，只讀取'Country/Region', 'Date', 'Value'三個column
    df = pd.read_csv(file_path,usecols=['Country/Region', 'Date', 'Value'])
    # 將空值填0
    df = df.fillna(value=0)
    # 刪掉第2列header
    df = df.drop(axis=0, index=0)
    # 將資料型別轉換為日期型別
    df["Date"] = pd.to_datetime(df["Date"])

    return df


# 資料過濾條件(確診)
def data_filiter(df):
    Region = df["Country/Region"].isin(["Taiwan*","Japan","Korea, South","Italy"])
    data_f = Region

    return data_f



def race_barchart(input_day):

    # (確診)
    # 獲得符合input_day的資料
    dff = done[done['Date'].eq(input_day)].sort_values(by='Value', ascending=True)
    # 將Country/Region的值 轉成 str型態
    dff['Country/Region'] = dff['Country/Region'].astype(str)
    # 將Value的值 轉成 float
    dff['Value'] = dff['Value'].astype(float)

    # 由於第一次排序無法將資料完整排序，再進行排序
    dff = dff.sort_values(by="Value", ascending=True)

    # (死亡)
    # 獲得符合input_day的資料
    deaths = done_deaths[done_deaths['Date'].eq(input_day)].sort_values(by='Value', ascending=True)
    # 將Country/Region的值 轉成 str型態
    deaths['Country/Region'] = deaths['Country/Region'].astype(str)
    # 將Value的值 轉成 float
    deaths['Value'] = deaths['Value'].astype(float)

    # 由於第一次排序無法將資料完整排序，再進行排序
    deaths = deaths.sort_values(by="Value", ascending=True)

    # (康復)
    # 獲得符合input_day的資料
    recover = done_recovered[done_recovered['Date'].eq(input_day)].sort_values(by='Value', ascending=True)
    # 將Country/Region的值 轉成 str型態
    recover['Country/Region'] = recover['Country/Region'].astype(str)
    # 將Value的值 轉成 float
    recover['Value'] = recover['Value'].astype(float)

    # 由於第一次排序無法將資料完整排序，再進行排序
    recover = recover.sort_values(by="Value", ascending=True)



    # 清空畫布
    ax.clear()

    # 長條圖
    ax.barh(dff['Country/Region'] , dff['Value'], height=0.2,color=[colors[x] for x in dff['Country/Region']],edgecolor='#666666',hatch='/')
    ax.barh(np.arange(len(dff['Country/Region']))- 0.3 , deaths['Value'], height=0.2, color=[colors[x] for x in dff['Country/Region']],edgecolor='#666666', hatch='-')
    ax.barh(np.arange(len(dff['Country/Region'])) - 0.6, recover['Value'], height=0.2,color=[colors[x] for x in dff['Country/Region']], edgecolor='#666666', hatch='+')

    # 文字距離(確診)
    dis = dff['Value'].max() / 100.0
    # 更新每個長條圖文字訊息(確診)
    for i, (value, name) in enumerate(zip(dff['Value'], dff['Country/Region'])):

        # 將每個國家名稱放到對應的長條旁邊
        ax.text(0, i, name + ' ', size=12, weight=300, ha='right', va='center')
        # 將確診人數放到對應的長條旁邊
        ax.text(value + dis, i,f'{value:,.0f}',  size=8, ha='left',  va='center')

        # 計算確診人數比例
        percent  = value/float(dff['Value'].sum())
        percent = percent * 100.0
        # 將確診人數比例放到對應的長條旁邊
        ax.text(value + dis, i-0.1, f'{percent:.2f}%' , size=6, ha='left', va='center')

    # 文字距離(死亡)
    deaths_dis = dff['Value'].max() / 100.0
    # 更新每個長條圖文字訊息
    for i, (value, name) in enumerate(zip(deaths['Value'], deaths['Country/Region'])):
        # 將確診人數放到對應的長條旁邊
        ax.text(value + deaths_dis, i - 0.3,f'{value:,.0f}',  size=8, ha='left',  va='center')

        # 計算確診人數比例
        if float(deaths['Value'].sum()) == 0:
            deaths_percent = 0
        else:
            deaths_percent  = value/float(deaths['Value'].sum())
            deaths_percent = deaths_percent * 100.0
        # 將確診人數比例放到對應的長條旁邊
        ax.text(value + deaths_dis, i - 0.4, f'{deaths_percent:.2f}%' , size=6, ha='left', va='center')

    # 文字距離(康復)
    recover_dis = dff['Value'].max() / 100.0
    # 更新每個長條圖文字訊息
    for i, (value, name) in enumerate(zip(recover['Value'], recover['Country/Region'])):
         # 將確診人數放到對應的長條旁邊
         ax.text(value + recover_dis, i - 0.6, f'{value:,.0f}', size=8, ha='left', va='center')

         # 計算確診人數比例
         if float(recover['Value'].sum()) == 0:
             recover_percent = 0
         else:
             recover_percent = value / float(recover['Value'].sum())
             recover_percent = recover_percent * 100.0
         # 將確診人數比例放到對應的長條旁邊
         ax.text(value + recover_dis, i - 0.7, f'{recover_percent:.2f}%', size=6, ha='left', va='center')

    # 將input_day 轉成 str型態
    datetime_str = np.datetime_as_string(input_day)
    # 小標題 confirmed
    ax.text(0, 1.1, 'confirmed', transform=ax.transAxes, size=14, color='#777777')

    # 增加總確診人數
    ax.text(0.9, 0.1, 'Total: ' + '{:,.0f}'.format(dff['Value'].sum()), transform=ax.transAxes, size=12, color='#000000',ha='right')
    # 增加日期(只印出前10個字元)
    ax.text(0.9, 0.15, datetime_str[:10], transform=ax.transAxes, color='#777777', size=12, ha='right')


    # 調整橫軸顏色、標籤大小
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    # 將橫軸放到頂端
    ax.xaxis.set_ticks_position('top')
    # 將y軸隱藏
    ax.set_yticks([])

    # 增加格線
    ax.grid(which='major', axis='x', linestyle='-')
    # 取消邊界
    plt.box(False)


# 執行
df = ini_data_confirmed()
dd = ini_data_deaths()
dr = ini_data_recovered()


# 資料過濾
data_filter = data_filiter(df)
# done為過濾後的資料(確診)
done = df[data_filter]

# done_deaths為過濾後的資料(死亡)
done_deaths = dd[data_filter]

data_re_filter = data_filiter(dr)
# done_recovered為過濾後的資料(康復)
done_recovered  = dr[data_re_filter]


# 整理Frame數
month = list(set(df.Date.values))
# 排序時間
month.sort()

# 動畫
animator = animation.FuncAnimation(fig, race_barchart, frames=month,repeat=False)

# 執行動畫
plt.show()








