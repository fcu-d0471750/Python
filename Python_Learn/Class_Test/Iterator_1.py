'''
未使用產生器，不斷拿下一個值。


class NumberSequence:

    def __init__(self):
        self.number = 0

    # 取下一個值
    def next(self):
        self.number = self.number + 1
        return self.number

seq = NumberSequence()

for i in range(1,11):
    print(seq.next())
'''


'''
使用迭代器，不斷拿下一個值。




iter_obj = iter([3,4,5])

for  i  in  iter_obj:
  print(i)
'''
'''  
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
'''


'''
使用產生器，不斷拿下一個值。



def even(x):
    i = 0
    while(i!=len(x)):
        if x[i]%2==0:
            yield x[i]
        i = i + 1

list_n = [3,4,5,6,7]

for i in even(list_n):
    print(i)
'''




class Teacher:
    # 建構子
    def __init__(self,  name , age):
        self.name = name
        self.age = age


list_T = []

teacher_1 = Teacher("Niko" , 33)
teacher_2 = Teacher("Rom" , 60)
teacher_3 = Teacher("Jill" , 48)

list_T.append(teacher_1)
list_T.append(teacher_2)
list_T.append(teacher_3)

iter_obj = iter(list_T)

for  i  in  iter_obj:
  print("Name:" , i.name ,"Age:", i.age)












