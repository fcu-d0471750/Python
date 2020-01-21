''''
顯示 數字0~9、大寫英文字母、小寫英文字母的ASCII Code
'''
#數字
for i in range(0,10,1):
    print('{:2d} ' .format(i) , end='')

#換行
print()

#ord:將字串轉成十進位整數ASCII，str:將i轉成字串型態
for i in range(0,10,1):
    print('{:2x} ' .format(ord(str(i))) , end='')

#換行##########################################################################
print('\n')

#大寫英文字母
for i in range(65,91,1):
    print('{:2} ' .format(chr(i)) , end='')

#換行
print()

for i in range(65,91,1):
    print('{:2X} ' .format(i) , end='')

#換行##########################################################################
print('\n')

#小寫英文字母
for i in range(97,123,1):
    print('{:2} ' .format(chr(i)) , end='')

#換行
print()

for i in range(97,123,1):
    print('{:2X} ' .format(i) , end='')