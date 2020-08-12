'''
資料庫管理
'''

# 從 名為Store_DB的package 中的 Yunlin_DB.py import Yunlin_Store 並叫做Store_Yun
# 雲林課
from Store_DB.Yunlin_DB import Yunlin_Store as Store_Yun
# 彰南課
from Store_DB.Changnan_DB import Changnan_Store as Store_nan
# 台中課
from Store_DB.Taichung_DB import Taichung_Store as Store_chung
# 中港課
from Store_DB.ChungGang_DB import ChungGang_Store as Store_gang
# 彰化課
from Store_DB.Changhua_DB import Changhua_Store as Store_hua
# 彰濱課
from Store_DB.Changbin_DB import Changbin_Store as Store_bin

#'台中','中港','彰化','彰南','彰濱','雲林'

# 回傳門市資料(area=地區)
def use_store_db(area):
    if(area == '台中'):
        return Store_chung
    elif(area == '中港'):
        return Store_gang
    elif (area == '彰化'):
        return Store_hua
    elif (area == '彰南'):
        return Store_nan
    elif (area == '彰濱'):
        return Store_bin
    elif (area == '雲林'):
        return Store_Yun