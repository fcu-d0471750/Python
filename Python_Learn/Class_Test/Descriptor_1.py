'''
描述器(descriptor): 管理一個類別中，單一或全部屬性的取得、設定、刪除的實際邏輯。
也就是如果屬性的getter、setter都是做相同的事情，則可以透過描述器，統一規定getter、setter。
也可以新增條件來處理某些屬性的getter、setter。




# 描述器
class Clientdesc:

    def __init__(self , name):
        # 設定欄位名稱
        self.name = name

    def __get__(self, instance, owner):
        # 檢查instance是否為None
        if instance is None:
            return self

        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        # 檢查value是否為int
        if not isinstance(value , int):
            raise TypeError(value , "is not int.")

        # 找出instance中self.name的欄位，將值改為value
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        instance.__dict__[self.name] = None


# 使用描述器的類別
class Clientclass:
    number = Clientdesc('number')

    def __init__(self , value):
        self.number = value

# 執行
# 實體化
client = Clientclass(15)

print("使用 __get__")
print("client.number: " , client.number)

print("使用 __set__")
client.number = 55
print("client.number: " , client.number)

print("使用 __delete__")
del client.number
print("client.number: " , client.number)

'''

'''
描述器(descriptor): 管理一個類別中，單一或全部屬性的取得、設定、刪除的實際邏輯。
也就是如果屬性的getter、setter都是做相同的事情，則可以透過描述器，統一規定getter、setter。
也可以新增條件來處理某些屬性的getter、setter。




# 描述器
class Descriptor:

    def __init__(self , name):
        # 設定欄位名稱
        self.name = name

    def __get__(self, instance, owner):
        # 檢查instance是否為None
        if instance is None:
            return self

        # 印出屬性的型態
        print(type(instance.__dict__[self.name]))
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        # 如果value的型態不是int也不是string
        if (type(value) != int) and (type(value) != str):
            raise ValueError('Value can be int or string.')

        # value型態為int
        if type(value) == int :
          #  value 小於 0
          if value < 0:
              print("Value cannot be negative.")

          # 找出instance中self.name的欄位，將值改為value
          else:
              instance.__dict__[self.name] = value

        # value型態為String
        if type(value) == str :
          # 找出instance中self.name的欄位，將值改為value
          instance.__dict__[self.name] = value


    def __delete__(self, instance):
        instance.__dict__[self.name] = None


# 使用描述器的類別
class Clientclass:
    number = Descriptor('number')
    sentence = Descriptor('sentence')

    def __init__(self):
        self.number = 0
        self.sentence = "Nothing"


# 執行
# 實體化
client = Clientclass()



print("使用 __get__")
print("client.number: " , client.number , '\n')

print("使用 __set__")
client.number = 55
print("client.number: " , client.number , '\n')

print("使用 __set__")
client.number = -10
print("client.number: " , client.number , '\n')

print("使用 __delete__")
del client.number
print("client.number: " , client.number , '\n')

print("-------------------------------------------" , '\n')


print("使用 __get__")
print("client.sentence: " , client.sentence , '\n')

print("使用 __set__")
client.sentence = "This is sentence"
print("client.sentence: " , client.sentence , '\n')

print("使用 __delete__")
del client.sentence
print("client.sentence: " , client.sentence , '\n')
'''

'''
class Area:
    def __init__(self, area):
            self._area = area
    def __set__(self, obj, val):
            raise AttributeError('Cannot Set')
    def __get__(self, obj, objtype):
            return self._area

class A:
    x = Area(233)

a = A()
a.x

a.x = 222
'''




# 描述器
class radious_des:

    # 新建欄位
    def __init__(self , name):
        # 設定欄位名稱
        self.name = name

    # 取得半徑、周長、面積
    def __get__(self, instance, owner):
        # 檢查instance是否為None
        if instance is None:
            return self

        else:
         # 半徑
         if(self.name == "radious"):
             print("Your radious is : ", end='')

             return instance.__dict__["radious"]
         # 周長
         elif(self.name == "circumference"):
             print("Your circumference is : ", end='')
             instance.__dict__["circumference"] = round(instance.__dict__["radious"] * 2.0 * 3.14 , 2)

             return instance.__dict__["circumference"]
         # 面積
         elif(self.name == "area"):
             print("Your area is : ", end='')
             instance.__dict__["area"] = instance.__dict__["radious"] * instance.__dict__["radious"] * 3.14

             return instance.__dict__["area"]

        # 其它
        return instance.__dict__[self.name]

    # 設定半徑
    def __set__(self, instance, value):
        # 如果value的型態不是float
        if (type(value) != float):
            raise ValueError('Value can be float.')

        #  value 小於 0.0 或 大於100.0
        if (value <= 0) or (value > 100):
            print("Value is from 1.0 to 100.0")
        # 找出instance中self.name的欄位，將值改為value
        else:
            instance.__dict__[self.name] = value

    # 刪除欄位
    def __delete__(self, instance):
        instance.__dict__[self.name] = None


# 使用描述器的類別
class Circle:
    # 半徑
    radious = radious_des('radious')
    # 周長
    circumference = radious_des('circumference')
    # 面積
    area = radious_des('area')


    def __init__(self,radious):
        self.radious = radious




# 執行
# 實體化
circle = Circle(10.0)



print("使用 __get__，取得半徑")
print("client.radious: " , circle.radious , '\n')

print("使用 __get__，取得周長")
print("client.circumference: " , circle.circumference , '\n')

print("使用 __get__，取得面積")
print("client.area: " , circle.area , '\n')

print("---------------------------------------------")

print("使用 __set__，設定半徑")
circle.radious = 12.0
print("client.radious: " , circle.radious , '\n')

print("使用 __get__，取得周長")
print("client.circumference: " , circle.circumference , '\n')

print("使用 __get__，取得面積")
print("client.area: " , circle.area , '\n')

print("---------------------------------------------")

print("使用 __delete__")
del circle.radious
print("client.radious: " , circle.radious , '\n')


























































