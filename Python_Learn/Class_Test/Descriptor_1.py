'''
描述器(descriptor): 管理一個類別中，單一或全部屬性的取得、設定、刪除的實際邏輯。
也就是如果屬性的getter、setter都是做相同的事情，則可以透過描述器，統一規定getter、setter。
也可以新增條件來處理某些屬性的getter、setter。
'''



# 描述器
class Descriptor:

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
    number = Descriptor('number')

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


