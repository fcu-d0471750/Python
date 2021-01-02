# 導入excel管理
from Excel_Section import excel_Manage as EM
#=================================================================
#宣告變數
#=================================================================
# 要求區域
require_area = ['台中','中港','彰化','彰南','彰濱','雲林']

# 要求時間
require_date =['109-12-01','109-12-02','109-12-03','109-12-04']

# 要求門市
require_store  = [['鑫權勝~百祐~聯信~民主~權旺~鑫鑽~嶺寶~惠宇~遠百~富亦'],['雅典~生活~新學合~光輝~上楓樹'],['熊貓~鑫廣~墩正~校友會館~東海~瑞陽~墩陽~惠宇~遠百~富亦'],['瑞陽~墩陽']]

#EM.do_excel(require_area[0],require_date,require_store,'G2','G54','I2','I54')
EM.do_excel(require_area[0],require_date,require_store,('A2','A54','C2','C54'),('D2','D53','F2','F53'),('G2','G53','I2','I53'),('J2','J53','L2','L53'),('M2','M34','O2','O34'),('M36','M37','O36','O37'))


'''
def DES(*start):
    for i in range(len(start)):
        print(start[i][0], " ", start[i][1], " ", start[i][2], " ", start[i][3])

def plus(A,B,*name):
    DES(*name)
'''




'''
number = "5522145"
if(number[0:4]=="5523"): print("A")
else : print("B")
'''

#plus(2,1,('G2','G54','I2','I54'),('A2','A54','C2','C54'),('Z2','Z54','X2','X54'))