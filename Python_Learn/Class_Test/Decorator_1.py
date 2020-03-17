'''
裝飾器(Decorator、@):
主要用於多個方法的內部邏輯十分接近，所以透過裝飾器將共同的邏輯給拿出來做成裝飾器，而這些方法只要將不同的邏輯給寫在自身就可以了。
盡量在整體程式有一定開發程度時再使用裝飾器。

主要分成3個寫法無參數、有1個參數、有多個參數。
'''

'''
# 無參數
def printHello(function):
    def wrapper():
        print("Hello")
        return function()
    return wrapper

@printHello
def printWorld():
    print("World")

printWorld()
'''

'''
# 有1個參數
def printHello(function):
    def wrapper(str):
        print("Hello")
        return function(str)
    return wrapper

@printHello
def printWorld(str):
    print(str)

printWorld("Decorator")
'''

# 有多個參數
def printHello(function):
    def wrapper(*args , **kwargs):
        print("Hello")
        return function(*args , **kwargs)
    return wrapper

##1個參數
@printHello
def printsinglearg(str):
    print(str)

##多個參數
@printHello
def printmularg(str1 , number):
    print(str1 , number)

printsinglearg("Decorator")
print("---------")
printmularg("Decorator" , 15)
