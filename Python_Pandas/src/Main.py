# 導入excel管理
from Excel_Section import excel_Manage as EM
#=================================================================
#宣告變數
#=================================================================
# 要求區域
require_area = ['台中','中港','彰化','彰南','彰濱','雲林']

# 要求時間
require_date =['109,09,01','109,09,02','109,09,03','109,09,04','109,09,05','109,09,07','109,09,08','109,09,09','109,09,10','109,09,11','109,09,14']

# 要求門市
require_store  = [['嶺中~興福~南屯~東海'],['權貴~遊園']]

#EM.do_excel(require_area[0],require_date,require_store,'G2','G54','I2','I54')
EM.do_excel(require_area[0],require_date,require_store,('A2','A54','C2','C54'),('G2','G54','I2','I54'),('M2','M34','P2','P34'),('M36','M37','P36','P37'))


'''
def plus(A,B,*name):
    print(B)
    for i in range(len(name)):
     print(name[i][2]," ",name[i][3])

'''



#plus(2,1,('G2','G54','I2','I54'),('A2','A54','C2','C54'))