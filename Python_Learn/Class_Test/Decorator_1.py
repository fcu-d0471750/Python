'''
裝飾器(Decorator):
主要用於多個方法的內部邏輯十分接近，所以透過裝飾器將共同的邏輯給拿出來做成裝飾器，而這些方法只要將不同的邏輯給寫在自身就可以了。
盡量在整體程式有一定開發程度時再使用裝飾器。

主要分成3個寫法方法無參數、方法有1個參數、方法有多個參數、裝飾器有參數。
'''

'''
# 方法無參數
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
# 方法有1個參數
def printHello(function):
    def wrapper(arg):
        print("Hello")
        return function(arg)
    return wrapper

@printHello
def printWorld(arg):
    print(arg)

printWorld("Decorator")
'''

'''
# 方法有多個參數
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
'''

## 裝飾器也有參數
def print_decorator_arg(decorator_arg):
    def decorator(function):
        def wrapper(*args, **kwargs):
            print(decorator_arg)
            return function(*args, **kwargs)
        return wrapper
    return decorator

@print_decorator_arg("Hi")
def sayHi_printArg(arg):
    print(arg)


sayHi_printArg("World")
