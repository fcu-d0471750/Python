"""完整程式碼"""

import urllib.request
import os
import tarfile
from keras.datasets import imdb
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation,Flatten
from keras.layers import Conv1D, MaxPooling1D, Embedding
import re

# 外部雲端下載資料集
! wget http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz
# 解壓縮aclImdb
! tar zxf aclImdb_v1.tar.gz

# 字典:正面評價、負面評價
SentimentDict = {1:"正面評價" , 0:"負面評價"}

# 過濾掉符號或常用的表情符號
def rm_tags(text):
  re_tag = re.compile(r"<[^>]+>")
  return re_tag.sub("",text)

# 從解壓縮的資料夾中，獲取資料
def read_files(filetype):
  # 解壓縮的資料夾
  path = "/content/aclImdb/"
  # 資料
  file_list = []

  # 正面的評價資料，路徑組合成/content/aclImdb/filetype/pos/
  # filetype的概念 = 訓練資料 和 測試資料
  postive_path = path + filetype + "/pos/"
  for f in os.listdir(postive_path):
    file_list = file_list + [postive_path + f]

  # 負面的評價資料，路徑組合成/content/aclImdb/filetype/neg/
  negative_path = path + filetype + "/neg/"
  for f in os.listdir(negative_path):
    file_list = file_list + [negative_path + f] 


  print("read", filetype,"files:",len(file_list))

  all_labels = ([1] * 12500 + [0] * 12500)

  all_texts = []
  # 將解壓縮的資料進行過濾
  for fi in file_list:
    with open(fi,encoding='utf8') as file_input:
      all_texts = all_texts + [rm_tags(" ".join(file_input.readlines()))]

  # 回傳過濾後的資料
  return all_labels,all_texts   

# 顯示 評論、標籤、預測資料
def display_test_Sentiment(i):
  print(test_text[i])
  print("標籤:",SentimentDict[y_test[i]],
        "預測:",SentimentDict[predict_classes[i]])

# 自行輸入評價，分析語意
def predict_review(input_text):
  # 進行字數排序
  input_seq = token.texts_to_sequences([input_text])

  #　影評資料太長就裁切，太短就補0
  pad_input_seq = sequence.pad_sequences(input_seq , maxlen= 100)

  # 用已訓練的模型進行分析
  predict_result = model.predict_classes(pad_input_seq)

  # 印出評價
  print(SentimentDict[predict_result[0][0]])

# 建立一個字典，儲存單字，並依出現次數排序
# token = 字典，預設儲存2000個單字，出現次數前2000
token = Tokenizer(num_words = 2000)
token.fit_on_texts(train_text)

y_train, train_text = read_files("train")

y_test , test_text = read_files("test")

# 將文字轉成出現次數排行(訓練資料)
x_train_seq = token.texts_to_sequences(train_text)
# 將文字轉成出現次數排行(測試資料)
x_test_seq = token.texts_to_sequences(test_text)

# 影評資料太長就裁切，太短就補0(訓練資料)
x_train_seq = sequence.pad_sequences(x_train_seq,maxlen = 100)
# 影評資料太長就裁切，太短就補0(測試資料)
x_test_seq = sequence.pad_sequences(x_test_seq,maxlen = 100)


# 建立模型(線性堆疊)
model = Sequential()

# 設定神經元
# 透過Embedding，減少one hot encoding浪費的0位元
model.add(Embedding(output_dim = 32 , input_dim = 2000 , input_length = 100))

# 使用平坦層轉換
model.add(Flatten())

# 隱藏層(256個神經元，激發函數 = relu)
model.add(Dense(units = 256 , activation = "relu"))

# 輸出層(1個神經元，激發函數 = sigmoid)，輸出只有正面或負面其中之一
model.add(Dense(units = 1 , activation = "sigmoid"))

# 開始訓練模型
model.compile(loss = 'binary_crossentropy' , optimizer = "adam" , metrics = ["accuracy"])

# 訓練結果
train_history = model.fit(x_train_seq , y_train , batch_size = 100 , epochs = 10 , verbose = 0 , validation_split = 0.2)

# 準確率
scores = model.evaluate(x_test_seq , y_test , verbose = 1)

# 預測結果(直)
predict = model.predict_classes(x_test_seq)

# 進行維度變化(橫)
predict_classes = predict.reshape(-1)

# 印出 評論、標籤、預測資料
display_test_Sentiment(50)

# 自行輸入評論
predict_review("This is the worst movie I have seen")
