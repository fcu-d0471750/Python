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

print(seq.number)

seq.next()
print(seq.number)

seq.next()
print(seq.number)

'''


'''
使用迭代器，不斷拿下一個值。


class NumberSequence:

    def __init__(self):
        self.number = 0

    # 取下一個值
    def __next__(self):
        self.number = self.number + 1
        return self.number

seq = NumberSequence()

print(seq.number)

next(seq)
print(seq.number)

next(seq)
print(seq.number)
'''


'''
使用產生器，不斷拿下一個值。
'''


def NumberSequence(number):
    while True:
        yield number
        number = number + 1
        print(number)

seq = NumberSequence(0)

next(seq)
next(seq)
next(seq)
next(seq)
next(seq)

