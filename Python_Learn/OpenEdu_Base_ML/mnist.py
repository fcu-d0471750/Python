"""完整程式碼"""

# 支援矩陣運算
import numpy as np
# 數據分析套件
import pandas as pd
# 圖形化
import matplotlib.pyplot as plt
# 機器學習套件
from keras.utils import np_utils
# 機器學習套件
from keras.datasets import mnist
# Model套件
from keras.models import Sequential
from keras.layers import Dense, Activation
# colab tool bar
from ipywidgets import interact_manual

# 這個功能就是從外部的雲端空間
# 去下載一個 mnist 的資料集到我們的專案裡面
(x_train_image , y_train_label),(x_test_image , y_test_label) = mnist.load_data()

# 預測結果圖像化，(images = 圖片、labels = 標籤 、prediction=預測結果、idx=從第幾筆資料開始、num=一次印幾筆資料)
def plot_images_labels_prediction(images , labels , prediction , idx , num):
    # 設定畫布
    fig = plt.gcf()
    # 畫布大小
    fig.set_size_inches(12,14)
    # 最大可印資料數
    if num > 25:
        num = 25
    #
    for i in  range(0 , num):
        # 最多25筆資料，從 5*5，第i+1個項目開始
        ax = plt.subplot(5,5,1+i)
        # idx=從第幾筆資料開始，顏色為灰階
        ax.imshow(images[idx] , cmap="binary")
        # 圖像上方印出相對應的labels
        title = "label=" + str(labels[idx])
        # 圖像上方印出相對應的預測結果
        title = title + ",predict=" + str(prediction[idx])
        # 設定字體大小
        ax.set_title(title,fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        # 下一筆資料
        idx = idx + 1
    plt.show()





#使用reshape的方式，就可以把原先的資料外觀，改成我們想要的資料外觀
x_train = x_train_image.reshape(60000 , 784).astype("float32")
x_test = x_test_image.reshape(10000 , 784).astype("float32")

# 正規化
x_train_normalize = x_train / 255
x_test_normalize = x_test / 255

# one hot
y_trainonehot = np_utils.to_categorical(y_train_label)
y_testonthot = np_utils.to_categorical(y_test_label)

# 線性堆疊模型
model = Sequential()

# 設定輸入層、隱藏層之間的數值，units=隱藏層數量、input_dim=輸入層數量
# 權重和偏差 使用kernel_initializer = 常態分佈
# 神經元激活函數 使用activation = 線性整流函數
model.add(Dense(units=256,input_dim=784,kernel_initializer="normal",activation="relu"))

# 設定隱藏層、輸出層之間的數值，units=輸出層數量
# 由於隱藏層在上一行已經設定，所以不需再次設定
# 神經元激活函數 使用activation = softmax函數
model.add(Dense(units=10,kernel_initializer="normal",activation="softmax"))

# Model的資訊
# Param = 參數總量
# 200960 = 輸入層神經元(784) * 隱藏層神經元(256) + 隱藏層神經元(256)
# 2570 = 隱藏層神經元(256) * 輸出層神經元(10) + 輸出層神經元(10)
print(model.summary())


# 開始訓練Model
# loss(loss function) = 用來計算輸出值與答案之間的差距
# optimizer = 優化與訓練的方法
# metrics = 模型的評估方法
model.compile(loss="categorical_crossentropy" , optimizer="adam" , metrics=["accuracy"])

# x = 圖像經過維度轉換以及正規化之後的結果
# y = 是用來比對最終的答案，也就是之前標籤經過 one hot encoding
train_history = model.fit(x = x_train_normalize , y=y_trainonehot , validation_split=0.2 , epochs=10 , batch_size=200 , verbose=0)


# 訓練結果
# evaluate用於計算準確率
scores = model.evaluate(x_test_normalize , y_testonthot)
print("accuracy=" , scores[1])

# 測試
prediction = model.predict_classes(x_test_normalize)

# 預測結果圖像化(一)
plot_images_labels_prediction(x_test_image , y_test_label , prediction , idx=0 , num=5)

# 預測結果圖像化(二)
# index=(0,1000)，範圍0~1000
interact_manual(show_figure , index=(0,1000))
