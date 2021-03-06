'''
#==============================================
#定義一個父類別Animal
#==============================================
class Animal():
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
    def __init__(self, Name, Fur_color):
        self.Name = Name
        self.Fur_color = Fur_color

    #==============================================
    #方法(Methods)
    #==============================================
    #吠叫
    def Bark(self):
        print('Animal 叫了一聲' )

#==============================================
#定義一個子類別類別Dog，繼承Animal
#==============================================
class Dog(Animal):

    #==============================================
    #建構子(Constructor)
    #==============================================
    #保留Animal的屬性Name、Fur_color
    def __init__(self , Name , Fur_color):
        self.Name = Name
        self.Fur_color = Fur_color

    #==============================================
    #方法(Methods)
    #==============================================
    #保留Animal的方法Bark(self)
    #吠叫
    def Bark(self):
        print('毛色為', self.Fur_color , '的' , self.Name , '叫了一聲')

    #衍生出新的方法
    #跑
    def Run(self):
        print(self.Name , '開始跑')

#==============================================
#執行
#==============================================
#生成一個物件Animal
animal = Animal('animal' , 'Dark')
#生成一個物件Dog
DD = Dog('DD' , 'White')

#animal叫了一聲
animal.Bark()
#DD叫了一聲
DD.Bark()
#DD開始跑
DD.Run()

'''

'''
#不使用繼承
'''




#==============================================
#定義一個父類別Person
#==============================================
class Person():
    #建構子(Constructor)
    def __init__(self, Name, ID):
        self.Name = Name
        self.ID = ID

    #方法(Methods)
    #走路
    def Walk(self):
        print(self.Name , '走路')

#定義一個子類別類別Engineer，繼承Person
class Engineer(Person):
    #建構子(Constructor)
    def __init__(self , Name, ID, Skill):
        #繼承Person的__init__
        super().__init__(Name, ID)
        #衍生出新的屬性
        #技能
        self.Skill = Skill

    #衍生出新的方法
    #修理
    def Do_Fix(self):
        print(self.Name , '修理東西')

#定義一個子類別類別Manager，繼承Person
class Manager(Person):
    #建構子(Constructor)
    def __init__(self , Name, ID):
        #繼承Person的__init__
        super().__init__(Name, ID)

    #衍生出新的方法
    #管理
    def Do_Manage(self):
        print(self.Name , '進行管理')


#新增一個Engineer
Engineer_1 = Engineer('Jack' ,'S123456789' ,'軟體工程')
#使用Engineer衍生出的新方法
Engineer_1.Do_Fix()

#新增一個Manager
Manager_1 = Manager('Mary' , 'S297415823')
#使用Manager衍生出的新方法
Manager_1.Do_Manage()

#Engineer_1使用父類別的方法
Engineer_1.Walk()
