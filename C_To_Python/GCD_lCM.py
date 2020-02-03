'''
最大公因數 Greatest Common Divisor(GCD)

最小公倍數 Least Commoc Multiple(LCM)
'''

#====================================
#宣告方法: 最大公因數(輾轉相除法)
#====================================
def DO_GCD(input_1 , input_2):
    while( input_1!=0 and input_2!=0 ):
            if(input_1 >= input_2): input_1 = input_1 % input_2
            elif(input_2 >= input_1): input_2 = input_2 % input_1

    return input_1 + input_2

#====================================
#宣告方法: 最小公倍數
#====================================
def DO_LCM(input_1 , input_2 , GCD):
    return int(abs(input_1 * input_2) / GCD)
#====================================
#宣告變數
#====================================
#輸入1
Input_Number_1 = 0
#輸入2
Input_Number_2 = 0
#最大公因數
GCD = 0
#最小公倍數
LCM = 0

#====================================
#執行
#====================================
Input_Number_1 = eval(input('輸入第1個整數: '))
Input_Number_2 = eval(input('輸入第2個整數: '))

while(Input_Number_1 <= 0 or Input_Number_2 <=0):
    print('請輸入1(包含)以上的整數!!!')
    Input_Number_1 = eval(input('輸入第1個整數: '))
    Input_Number_2 = eval(input('輸入第2個整數: '))

else:
    GCD = DO_GCD(Input_Number_1 , Input_Number_2)
    print('最大公因數: {:4d}' .format(GCD))

    LCM = DO_LCM(Input_Number_1 , Input_Number_2 , GCD)
    print('最小公倍數: {:4d}' .format(LCM))



