# 導入doc管理
from Docx_Section import docx_Manage as DM

#=================================================================
#宣告變數
#=================================================================
# 要求區域
require_area = ['台中','中港','彰化','彰南','彰濱','雲林']

# 要求時間
require_date =['109,09,01','109,09,02','109,09,03','109,09,04','109,09,05','109,09,07','109,09,08','109,09,09','109,09,10','109,09,11','109,09,14']

# 要求門市
require_store  = [['明城~彰基~源益~彰溪~儒林~欣二林~群茂'],['芳林~芳苑~挖子~二溪~新安可~王功~功湖'],['溪湖~美溪~溪東~湖北~湖貴~員鹿~向福'],
                  ['新斗中~新竹塘~光政~寶斗~明道站~新溪州~斗金~彰苑'],['梅州里~加吉利~佳嘉~二水~內安~中圳~田中'],['新員民~員昌~員農~員林~員東~大員山~惠明'],['田正~祿靖~永冠~永靖~順心~田尾~湳港~北園'],
                  ['新社頭~金佳旺~社員~社腳~員慶~員家~社集~家和'],['豐昌~員勝~新靜修~員成~易順~真愛~金東山~員大'],['新百川~埔成~埔新~員全~彰醫~新員高~員埔~品冠']]

# 執行
DM.do_doc(require_area[4],require_date,require_store)


'''
# 輸出doc的數量
doc_count = len(require_store)

# 符合 require_store 的門市資料
allow_store = []

#require_store  = [['中醫五權','新民高中'],['新德化','昌鴻','華太']]
#=================================================================
#執行
#=================================================================

# 共執行幾次
for count in range(0,doc_count):
  # 清空符合 require_store 的門市資料
  allow_store = []
  # doc恢復成預設
  doc = docx.Document('../pages/M.docx')
  # 表格設定(rows=多的列的數量,cols=固定的行數量)
  # rows=1表示不多新增列，也就是只依照records的列的數量
  table = doc.add_table(rows=1, cols=11)
  # doc的調整
  section = doc.sections[0]
  # 調整橫式紙張
  section.orientation = WD_ORIENTATION.LANDSCAPE
  new_width, new_height = Cm(29.7), Cm(21)
  section.page_width = new_width
  section.page_height = new_height
  # 調整文件左右上下邊界至 1.27 cm
  section.left_margin = Cm(1.27)
  section.right_margin = Cm(1.27)
  section.top_margin = Cm(1.27)
  section.bottom_margin = Cm(1.27)


  # 找出符合 require_store 的門市資料
  for bbb in require_store[count]:
        for j in range(0,len(use_store_db(require_area[3]))):
            if(bbb==use_store_db(require_area[3])[j][2]):
                allow_store.append(use_store_db(require_area[3])[j])

  # 寫入doc
  for Zone, cls, name,date,brand,number,radiation,power,Components_01,Components_02, question_01 in allow_store:
        row_cells = table.add_row().cells
        row_cells[0].text = Zone
        row_cells[1].text = cls
        row_cells[2].text = name
        row_cells[3].text = date
        row_cells[4].text = brand
        row_cells[5].text = number
        row_cells[6].text = ('%.2f'%random.uniform(0.11,0.29))#保留小數點第二位，並保留0
        row_cells[7].text = str(random.randrange(1250,1350))
        row_cells[8].text = Components_01
        row_cells[9].text = Components_02
        row_cells[10].text = question_01

  # 輸出的doc的名稱
  doc_name =  'AI 技術可以讓隱藏於暗處的物品現形' + str(count) + '.docx'
  # 輸出 docx
  doc.save(doc_name)

'''
