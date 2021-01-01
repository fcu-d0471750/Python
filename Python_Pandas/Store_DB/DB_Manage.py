





# 擴充門市資料(listdata=只有門市名稱和編號，area=地區)
def use_store_db(listdata,area):
    ini_listdata = []
    for index in range(len(listdata[0])):
        ini_listdata.append(['中彰投', area, str(listdata[0][index]),'109,06,30','國際牌-1853', str(listdata[1][index]),'0.21','1388','無',' ','無'])
    return ini_listdata