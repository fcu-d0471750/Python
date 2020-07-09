import docx
from docx.shared import Cm  #加入可調整的 word 單位

doc = docx.Document('../pages/M.docx')

#門市資料
records = (
    ('中彰投', '雲林', '斗苑','109,06,30','國際牌-NE-1853','552249508','0.11','1295','無',' ','無'),
    ('中彰投', '雲林', '埤頭','109,06,30','國際牌-NE-1853','552249508','0.12','1294','無',' ','無'),
    ('中彰投', '雲林', '埤頭','109,06,22','國際牌-NE-1853','5525548','0.12','1294','無',' ','無'),
    ('中彰投', '雲林', '路口厝','109,06,30','國際牌-NE-1853','552249508','0.13','1293','葉片',' ','破損'),
    ('中彰投',	'雲林','金順利','109,06,30','國際牌-NE-1853','FC0255172','0.13'	,'1281'	,'無',' ','無')
)

# 要的門市
aaa = ['斗苑','埤頭']

last = []

# 表格設定(rows=多的列的數量,cols=固定的行數量)
# rows=1表示不多新增列，也就是只依照records的列的數量
table = doc.add_table(rows=1, cols=11)

#區Zone	區課	門市	查核日期	查核廠牌	財產編號	微波外洩	微波功率	1	2	1	2

for bbb in aaa:
   for j in range(0,len(records)):
       if(bbb==records[j][2]):
           last.append(records[j])





for Zone, cls, name,date,brand,number,radiation,power,Components_01,Components_02, question_01 in last:
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


'''
for i in range(0,len(aaa)):
    # 生成docx
    for Zone, cls, name,date,brand,number,radiation,power,Components_01,Components_02, question_01 in records:
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
'''


doc.save('AI 技術可以讓隱藏於暗處的物品現形.docx')