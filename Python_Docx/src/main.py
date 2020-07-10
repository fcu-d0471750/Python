import docx
from docx.shared import Cm  #加入可調整的 word 單位

# 從 名為Store_DB的package 中的 Yunlin_DB.py import Yunlin_Store 並叫做Store_Yun
# 雲林課
from Store_DB.Yunlin_DB import Yunlin_Store as Store_Yun


'''
宣告變數
'''

# 讀取預設格式
#doc = docx.Document('../pages/M.docx')

# 要求區域
require_area = ['台中','中港','彰化','彰南','彰濱','雲林']
# 要求門市
require_store  = [['斗苑','埤頭'],['路口厝','金順利','彰興']]

# 輸出doc的數量
doc_count = len(require_store)

# 符合 require_store 的門市資料
allow_store = []


'''
執行
'''

# 表格設定(rows=多的列的數量,cols=固定的行數量)
# rows=1表示不多新增列，也就是只依照records的列的數量



# 共執行幾次
for count in range(0,doc_count):
  # 清空符合 require_store 的門市資料
  allow_store = []
  # doc恢復成預設
  doc = docx.Document('../pages/M.docx')
  # 表格設定
  # rows=1表示不多新增列，也就是只依照records的列的數量
  table = doc.add_table(rows=1, cols=11)

  # 找出符合 require_store 的門市資料
  for bbb in require_store[count]:
        for j in range(0,len(Store_Yun)):
            if(bbb==Store_Yun[j][2]):
                allow_store.append(Store_Yun[j])

  # 寫入doc
  for Zone, cls, name,date,brand,number,radiation,power,Components_01,Components_02, question_01 in allow_store:
        row_cells = table.add_row().cells
        row_cells[0].text = Zone
        row_cells[1].text = cls
        row_cells[2].text = name
        row_cells[3].text = date
        row_cells[4].text = brand
        row_cells[5].text = number
        row_cells[6].text = radiation
        row_cells[7].text = power
        row_cells[8].text = Components_01
        row_cells[9].text = Components_02
        row_cells[10].text = question_01

  # 輸出的doc的名稱
  doc_name =  'AI 技術可以讓隱藏於暗處的物品現形' + str(count) + '.docx'
  # 輸出 docx
  doc.save(doc_name)


