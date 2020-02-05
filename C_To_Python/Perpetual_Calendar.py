'''
萬年曆
Perpetual calendar
'''

#=================================================================================
#宣告方法
#=================================================================================
#==============================
#方法: 印出日曆空格，(因為每年的1月1日的星期幾都不一樣，所以要在前面印出空格)
#==============================
def Print_Space(Week):
    for i in range(0 , Week , 1):
        print(' ' , end='')

#=================================================================================
#宣告變數
#=================================================================================

#tuple: 月份名稱(English)
Month_EName = ('January' , 'February', 'March','April','May','June','July','August','September', 'October', 'November', 'December')
#tuple: 月份名稱(Chinese)
Month_CName = ('一月' , '二月', '三月','四月','五月','六月','七月','八月','九月', '十月', '十一月', '十二月')

#tuple: 平年月份天數
Month_Day_Common_Year = (31,28,31,30,31,30,31,31,30,31,30,31)
#tuple: 閏年月份天數
Month_Day_Leap_Year = (31,29,31,30,31,30,31,31,30,31,30,31)

#int: 輸入年份
Input_Year = 0
#int: 計算星期幾
Week = 0
#int: 計算相差天數
Day = 0

#=================================================================================
#(執行)
#=================================================================================

#==============================
#輸入年份
#==============================
Input_Year = eval(input('輸入年份: '))

#==============================
#以2016年為基底，計算Input_Year和2016年相差幾天
#如果輸入2016則相差0天
#==============================
#2016年以後
if(Input_Year > 2016):
    for i in range(2016 , Input_Year , 1):
        if(i % 4 == 0): Day = Day + 366
        else: Day = Day + 365

#2016年以前
else:
    for i in range(Input_Year , 2016 , 1):
        if(i % 4 == 0): Day = Day + 366
        else: Day = Day + 365

#==============================
#計算Input_Year那一年的1月1日是星期幾(0~6，0表示星期日)
#==============================
if(Input_Year > 2016):
    #2016年的1月1日是星期五
    Week = 5 + (Day % 7)
    #一星期7天，超過則從頭計算
    if(Week > 7): Week = Week - 7
else:
    # 2016年的1月1日是星期五
    Week = 5 - (Day % 7)
    #一星期7天，超過則從頭計算
    if(Week < 0): Week = Week + 7


#==============================
#印出日曆
#==============================
for i in range(0 , 12 , 1):
    #印出月份名稱
    print(Month_EName[i] , '-' , Month_CName[i])
    #印出星期
    print(' Sun Mon Tue Wed Thu Fri Sat')
    #印出空格
    Print_Space(Week * 4)

    #閏年
    if(Input_Year % 4 == 0):
        for j in range(1 , Month_Day_Leap_Year[i]+1 , 1):
            # 印出日期
            print('{:4d}' .format(j) , end='')
            #每印1次，則星期幾 + 1
            Week = Week + 1
            #一星期7天，超過則從頭計算
            if(Week == 7):
                Week = Week - 7
                print()
        print()

    #平年
    else:
        for j in range(1 , Month_Day_Common_Year[i]+1 , 1):
            #印出日期
            print('{:4d}' .format(j) , end='')
            # 每印1次，則星期幾 + 1
            Week = Week + 1
            # 一星期7天，超過則從頭計算
            if(Week == 7):
                Week = Week - 7
                print()

        print()

    #換行
    print()


