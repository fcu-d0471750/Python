
#==============================================
#由於Python，沒有像Java一樣擁有abstract或interface這種機制來規範介面
#所以透過import ABCMeta, abstractmethod，將一個類別，抽像成一個抽像類別，當成一個介面來使用
#==============================================
from abc import ABCMeta, abstractmethod

#==============================================
#定義一個介面IUSB
#==============================================
class IUSB(metaclass=ABCMeta):

    #==============================================
    #方法(Methods)
    #==============================================
    @abstractmethod
    #檢查連接裝置(需實作)
    #使用pass來省略屬性或要實作的方法
    def Checkboot(self):
        pass

    #新增裝置(需實作)
    def Add_IUSB(self):
        pass

#==============================================
#定義一個類別Computer，實作介面IUSB
#==============================================
class Computer(IUSB):
    #名稱
    Name = ''
    #連接到Computer的裝置
    Driver_List = []

    #建構子(Constructor)
    def __init__(self , Name):
        self.Name = Name

    #實作Add_IUSB
    def Add_IUSB(self , IUSB):
        #Computer新增一個裝置
        self.Driver_List.append(IUSB)
        #裝置也連接到Computer
        IUSB.Add_IUSB(self)

    #實作Checkboot
    def Checkboot(self):
        #印出全部連接Computer的裝置名稱
        for i in range(0,len(self.Driver_List)):
            print(self.Driver_List[i].Name , ' ', end='')

#==============================================
#定義一個類別USBdriver，實作介面IUSB
#==============================================
class USBdriver(IUSB):
    #名稱
    Name = ''

    #建構子(Constructor)
    def __init__(self , Name):
        self.Name = Name

    #實作Add_IUSB
    def Add_IUSB(self , IUSB):
        #USBdriver新增一個裝置
        self.IUSB = IUSB

    #實作Checkboot
    def Checkboot(self):
        #印出連接USBdriver的裝置名稱
        print(self.IUSB.Name)

#==============================================
#執行
#==============================================

#生成一個Computer，名稱叫Com
Com = Computer('Com')
#生成二個USBdriver，名稱叫USBdriver_A、USBdriver_B
Udriver_A = USBdriver('USBdriver_A')
Udriver_B = USBdriver('USBdriver_B')

#Com新增裝置
Com.Add_IUSB(Udriver_A)
Com.Add_IUSB(Udriver_B)

#印出結果
print('連接Com的裝置: ' , end='')
Com.Checkboot()
print()

print('連接Udriver_A的裝置: ' , end='')
Udriver_A.Checkboot()
print('連接Udriver_B的裝置: ' , end='')
Udriver_B.Checkboot()