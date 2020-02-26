'''
#==============================================
#定義一個類別Dog
#==============================================
class Dog():
    #==============================================
    #屬性(Attribute)
    #==============================================
    #姓名
    Name = ''
    #毛色
    Fur_color = ''

    #==============================================
    #建構子(Constructor)
    #==============================================
    def __init__(self , Name , Fur_color):
        self.Name = Name
        self.Fur_color = Fur_color

    #==============================================
    #方法(Methods)
    #==============================================
    #吠叫
    def Bark(self):
        print(self.Name , '叫了一聲')


#==============================================
#執行
#==============================================
#生成一個物件Dog
DD = Dog('DD' , 'White')

#DD叫了一聲
DD.Bark()
'''



'''

#定義一個類別Person
class Person():
    def __init__(self , ID , Name , Gender , Address):
        self.ID = ID
        self.Name = Name
        #self.Father = Father
        #self.Mother = Mother
        self.Gender = Gender
        self.Address = Address

#執行
#一個Person，Jack
Jack = Person('S123456789' , 'Jack' , 'M' , 'Taichung')
#一個Person，Mary
Mary = Person('S274851392' , 'Mary' , 'F' , 'Taipei')
#一個Person，Mildred
Mildred = Person('S297415823' , 'Mildred' , 'F' , 'Changhua')


#取得Jack的ID
print('Jack\'s ID:', Jack.ID)

#取得Mary的Address
print('Mary\'s Address:', Mary.Address)

#取得Mildred的Gender
print('Mildred\'s Gender:', Mildred.Gender)

'''

'''
#一組個人資料
Person_Data = [['Jack','S123456789' , 'M' , 'Taichung'] , ['Mary' , 'S274851392' ,  'F' , 'Taipei'] , ['Mildred' , 'S297415823' ,  'F' , 'Changhua']]

#取得Jack的ID
print('Jack\'s ID:', Person_Data[0][1])

#取得Mary的Address
print('Mary\'s Address:', Person_Data[1][3])

#取得Mildred的Gender
print('Mildred\'s Gender:', Person_Data[2][2])
'''

'''
#Jack的電話號碼
Jack_phone = ['0428451668','0974851224']
#Jack的個人資料
Jack_data = ['Jack','S123456789' , 'M' , 'Taichung' , Jack_phone]

#Mary的個人資料
Mary_data = ['Mary' , 'S274851392' ,  'F' , 'Taipei']


#將Jack、Mary的個人資料存在person_data
person_data = [Jack_data , Mary_data]

print('Jack\'s ID:', person_data[0][1])
print('Jack\'s phone number:', person_data[0][4][1])
'''

'''
#定義一個類別Person
class Person():
    #建構子
    def __init__(self , ID , Name , Gender , Address):
        self.ID = ID
        self.Name = Name
        self.Gender = Gender
        self.Address = Address
        self.PhoneNumber = []

    #方法:新增PhoneNumber
    def addPhoneNumber(self,PhoneNumber):
        self.PhoneNumber.append(PhoneNumber)

#一個Person，Jack
Jack = Person('S123456789' , 'Jack' , 'M' , 'Taichung')
#一個Person，Mary
Mary = Person('S274851392' , 'Mary' , 'F' , 'Taipei')

#Jack增加PhoneNumber
Jack.addPhoneNumber('0428451668')

#取得Jack的ID
print('Jack\'s ID:', Jack.ID)
#取得Jack的PhoneNumber
print('Jack\'s PhoneNumber:', Jack.PhoneNumber)

#取得Mary的Address
print('Mary\'s Address:', Mary.Address)
'''

'''
#Jack父親的個人資料
Jack_father = ['Bill' , 'S274851392' ,  'M' , 'Taipei']

#Jack母親的個人資料
Jack_mother = ['Mary' , 'S297415823' ,  'F' , 'Taipei']

#Jack的個人資料
Jack = ['Jack','S123456789' , 'M' , 'Taichung' ,  Jack_father , Jack_mother]

#Jack的ID
print('Jack\'s ID',Jack[1])

#Jack父親的address
print('Jack\'sfather address',Jack[4][3])
'''


'''
#定義一個類別Person
class Person():
    #建構子
    def __init__(self , ID , Name , Gender , Address , Father , Mother):
        self.ID = ID
        self.Name = Name
        self.Gender = Gender
        self.Address = Address
        self.Father = Father
        self.Mother = Mother


#新增一個Person，Jack的父親
Jack_father = Person('S274851392' , 'Bill' , 'M' , 'Taipei' , 'Aaron' , 'Astrid')

#新增一個Person，Jack的母親
Jack_mother = Person('S297415823' , 'Mary' , 'F' , 'Taipei' , 'Basil' , 'Audrey')

#新增一個Person，Jack
Jack = Person('S123456789' , 'Jack', 'M' , 'Taichung' ,  Jack_father , Jack_mother)

#Jack的ID
print('Jack\'s ID',Jack.ID)

#Jack父親的address
print('Jack\'sfather address',Jack.Father.Address)
'''

'''
#Getter、Setter
class Person():
    #建構子
    def __init__(self , Name):
      self.__Name = Name

    #Getter
     #取得Person的Name
    def GetName(self):
        return self.__Name

    #Setter
    #設定Person的Name
    def SetName(self , Name):
        self.__Name = Name

#新增一個Person
person = Person('Jack')

#Name不使用Getter、Setter
print('Name不使用Getter、Setter')
print(person.__Name)
'''


'''
#多重建構子
#定義一個類別Person
class Person():
    #建構子(全部屬性)
    def __init__(self, ID=None , Name=None , Gender=None , Address=None , Father=None , Mother=None):
        self.ID = ID
        self.Name = Name
        self.Gender = Gender
        self.Address = Address
        self.Father = Father
        self.Mother = Mother


#只給Name和Address
Jack = Person(Name='Jack',Address='Taichung')

#印出名字，而Father會顯示None
print(Jack.Name,' ',Jack.Father)
'''