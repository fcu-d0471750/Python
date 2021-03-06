'''
SVM

# 支援矩陣運算
import numpy as np
# 機器學習運算的函式，SVC
from sklearn.svm import SVC

# 範例的12組身高體重的組合(特徵)
X = np.array([[150,40], [152,40] , [155,45] , [155,46] , [160,50] , [160,48]
             ,[170,65],[175,70],[176,80],[178,75],[180,82],[182,80]])

# 前6個是女生 後6個是男生(標籤、1:女、2:男)
Y = np.array([1,1,1,1,1,1,2,2,2,2,2,2])

# 訓練模型
clf = SVC()
# 進行訓練
clf.fit(X,Y)

# 得出以下的測試資料，會是男生還是女生
print(clf.predict([[152,42]]))

# 得出以下的測試資料，會是男生還是女生
print(clf.predict([[176,70]]))
'''


'''
線性回歸
Linear Regression

import matplotlib.pyplot as plt
# 支援矩陣運算
import numpy as np
# 機器學習運算的函式，Linear
from sklearn import datasets,linear_model

# 克拉
X = [[0.31], [0.45] , [0.48] , [0.55] , [0.70] , [0.88]
             ,[0.98],[1.05],[1.11],[1.22]]

# 價格
Y =[10000,12000,14000,18000,22000,28000,32000,36000,40000,48000]

# 訓練模型
regr = linear_model.LinearRegression()
# 進行訓練
regr.fit(X,Y)

# 用於預測新價格，用舊資料去預測
y_pre = regr.predict(X)


# 預測1克拉的價格
# y_pre = regr.predict([[1.0]])
# print(y_pre)


# 原始資料，用黑點表示
plt.scatter(X , Y , color="black")
# 重新訓練出來的預測資料，用藍線來表示
plt.plot(X , y_pre , color="blue" , linewidth=3)

# X軸的座標就是克拉
plt.xlabel("carat")
# Y軸的座標就是價格
plt.ylabel("price")

# 印出圖形
plt.show()
'''


'''
K-means分群演算法(文字結果)
# 機器學習運算的函式，K-means
from sklearn.cluster import KMeans
# 支援矩陣運算
import numpy as np

X = np.array([[1,1], [1,2] , [2,1] , [2,2] , [3,3] , [2,4],[4,2],
              [10,10],[9,8],[8,9],[8,8],[7,7],[8,6],[6,8]])

# 進行K-means分群，預設的分群數設為2
clf = KMeans(n_clusters=2)
clf.fit(X)

# 印出分群的結果(前七個點分在第一群，後七個點是分在另外一群)
print(clf.labels_)
'''

'''
K-means分群演算法(圖形結果)
# 機器學習運算的函式，K-means
from sklearn.cluster import KMeans
# 支援矩陣運算
import numpy as np
# 圖形化
import matplotlib.pyplot as plt

X = np.array([[1,1], [1,2] , [2,1] , [2,2] , [3,3] , [2,4],[4,2],
              [10,10],[9,8],[8,9],[8,8],[7,7],[8,6],[6,8]])

# 進行K-means分群，預設的分群數設為2
clf = KMeans(n_clusters=2)
clf.fit(X)

# 分群完的資料，進行繪圖
plt.scatter(X[:,0] , X[:,1] , s=100 , c=clf.labels_)

# 印出圖形
plt.show()
'''


'''
K-means分群演算法(隨機、圖形結果)

# 機器學習運算的函式，K-means
from sklearn.cluster import KMeans
# 支援矩陣運算
import numpy as np
# 圖形化
import matplotlib.pyplot as plt

# 隨機產生100個點
X = np.random.rand(100,2)

# 進行K-means分群，預設的分群數設為2
clf = KMeans(n_clusters=2)
clf.fit(X)

# 分群完的資料，進行繪圖
plt.scatter(X[:,0] , X[:,1] , s=100 , c=clf.labels_)

# 印出圖形
plt.show()
'''

'''
Mnist練習

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

# 這個功能就是從外部的雲端空間
# 去下載一個 mnist 的資料集到我們的專案裡面
(x_train_image , y_train_label),(x_test_image , y_test_label) = mnist.load_data()

# 訓練資料60000個，28X28的維度
print("x_train_image" , x_train_image.shape)
# 對應的標籤個數也是剛好60000個
print("y_train_label" , y_train_label.shape)

# 測試的圖像也是有10000個
print("x_test_image" , x_test_image.shape)
# 測試資料中的標籤個數也10000個
print("y_test_label" , y_test_label.shape)


# 印出圖像的資料
def plot_image(image):
    # 得到整個畫面
    fig = plt.gcf()
    # 圖片大小
    fig.set_size_inches(2,2)
    # cmap="binary"，使用黑白圖像，不同色彩代碼: plasma、 magma、cool
    plt.imshow(image , cmap="binary")
    # 印出圖形
    plt.show()

plot_image(x_train_image[0])

print(y_train_label[0])
'''


'''
Mnist資料預先處理



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

# 這個功能就是從外部的雲端空間
# 去下載一個 mnist 的資料集到我們的專案裡面
(x_train_image , y_train_label),(x_test_image , y_test_label) = mnist.load_data()

# 第一步(輸入層) 原先的資料
# 訓練資料60000個，28X28的維度
print("x_train_image" , x_train_image.shape)
# 對應的標籤個數也是剛好60000個
print("y_train_label" , y_train_label.shape)

# 測試的圖像也是有10000個
print("x_test_image" , x_test_image.shape)
# 測試資料中的標籤個數也10000個
print("y_test_label" , y_test_label.shape)

# 第二步(隱藏層)
# 由於我們要將這些資料
# 丟進第一層的輸入層神經元中
# 所以我們要進行一些維度的變更
# 我們會把它改變成 一維的784
# 才能夠方便地丟進去輸入層的神經元裡面

#使用reshape的方式，就可以把原先的資料外觀，改成我們想要的資料外觀
x_train = x_train_image.reshape(60000 , 784).astype("float32")
x_test = x_test_image.reshape(10000 , 784).astype("float32")

print("X_Train" , x_train.shape)
print("X_Test" , x_test.shape)

# 正規化
x_train_normalize = x_train / 255
x_test_normalize = x_test / 255

print(x_train_image[0])
print(x_train_normalize[0])


# 第三層(輸出層)
# 在輸出層的部分
# 就會使用一個新的概念
# 叫做One hot encoding
# 為每個類別來新增一個對應的欄位
# 用0或1來代表它的特性

y_trainonehot = np_utils.to_categorical(y_train_label)
y_testonthot = np_utils.to_categorical(y_test_label)

# 印出單筆矩陣
print(y_trainonehot[0])
# 印出多筆矩陣
print(y_trainonehot[:10])
'''



'''
Mnist建立訓練模型

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

# 這個功能就是從外部的雲端空間
# 去下載一個 mnist 的資料集到我們的專案裡面
(x_train_image , y_train_label),(x_test_image , y_test_label) = mnist.load_data()


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
'''


'''
Mnist開始訓練模型

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

# 這個功能就是從外部的雲端空間
# 去下載一個 mnist 的資料集到我們的專案裡面
(x_train_image , y_train_label),(x_test_image , y_test_label) = mnist.load_data()

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
print("prediction label=" , prediction , "\n")
print("correct label=",y_test_label , "\n")
'''







'''
Mnist訓練模型，結果圖像化


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

# 預測結果圖像化
plot_images_labels_prediction(x_test_image , y_test_label , prediction , idx=0 , num=5)
'''






'''
Mnist訓練模型，結果圖像化(二)



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
#
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

# 輸入index來顯示圖像
def show_figure(index):
    plot_images_labels_prediction(x_test_image , y_test_label , prediction , idx=index , num=1)





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

# 預測結果圖像化
# index=(0,1000)，範圍0~1000
interact_manual(show_figure , index=(0,1000))
#plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=1, num=5)

'''


'''
CIFAR 基本

from keras.datasets import  cifar10
import numpy as np
import matplotlib.pyplot as plt
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation,Flatten
from keras.layers import Conv2D , MaxPooling2D , ZeroPadding2D

# 印出圖像
def show(x_img,i):
    plt.figure(figsize=(2,2))
    plt.imshow(x_img[i])
    plt.show()

# 印出圖像(顏色對調)
def show(x_img,i):
    plt.figure(figsize=(2,2))
    img_new = x_img[i].copy()
    # 紅色 -> 綠色
    img_new[:,:,0] = x_img[i][:,:,1]
    # 綠色 ->
    img_new[:,:,1] = x_img[i][:,:,2]
    # 藍色 -> 紅色
    img_new[:,:,2] = x_img[i][:,:,0]
    # 裁切圖像(32x32 -> 16x16 , 色彩不變)
    # plt.imshow(img_new[0:16,0:16,:])
    plt.imshow(img_new)
    plt.show()


# 這個功能就是從外部的雲端空間
# 去下載一個 CIFAR10 的資料集到我們的專案裡面
(x_img_train,y_label_train),(x_img_test , y_label_test) = cifar10.load_data()


# 看看訓練資料以及測試資料的總數是多少
print("train data:",x_img_train , y_label_train,"\n")
print("test data:" , x_img_test , y_label_test, "\n")

'''

'''
CIFAR 資料預先處理

from keras.datasets import  cifar10
import numpy as np
import matplotlib.pyplot as plt
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation,Flatten
from keras.layers import Conv2D , MaxPooling2D , ZeroPadding2D

# 印出圖像
def show(x_img,y_label,i):
    print("label:",label_dict[y_label[i][0]],"predict: ???")
    plt.figure(figsize=(2,2))
    plt.imshow(x_img[i])
    plt.show()


# 這個功能就是從外部的雲端空間
# 去下載一個 CIFAR10 的資料集到我們的專案裡面
(x_img_train,y_label_train),(x_img_test , y_label_test) = cifar10.load_data()

# 正規化
x_img_train_normalize = x_img_train.astype("float32") / 255.0
x_img_test_normalize = x_img_test.astype("float32") / 255.0

# OneHotEncoding
y_label_train_OneHot = np_utils.to_categorical(y_label_train)
y_label_test_OneHot = np_utils.to_categorical(y_label_test)

# 將圖片種類的數字編號 轉換成 可讀的字串
label_dict = {0:"airplane" , 1:"automobile" , 2:"bird" ,3:"cat" ,4:"deer" ,
              5:"dog" ,6:"frog" ,7:"horse" ,8:"ship" ,9:"truck" }

# 印出圖像
show(x_img_test,y_label_test,98)
'''

'''
CIFAR 卷積及池化運算說明、建立模型

from keras.datasets import  cifar10
import numpy as np
import matplotlib.pyplot as plt
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation,Flatten
from keras.layers import Conv2D , MaxPooling2D , ZeroPadding2D

# 印出圖像
def show(x_img,y_label,i):
    print("label:",label_dict[y_label[i][0]],"predict: ???")
    plt.figure(figsize=(2,2))
    plt.imshow(x_img[i])
    plt.show()


# 這個功能就是從外部的雲端空間
# 去下載一個 CIFAR10 的資料集到我們的專案裡面
(x_img_train,y_label_train),(x_img_test , y_label_test) = cifar10.load_data()

# 正規化
x_img_train_normalize = x_img_train.astype("float32") / 255.0
x_img_test_normalize = x_img_test.astype("float32") / 255.0

# OneHotEncoding
y_label_train_OneHot = np_utils.to_categorical(y_label_train)
y_label_test_OneHot = np_utils.to_categorical(y_label_test)

# 將圖片種類的數字編號 轉換成 可讀的字串
label_dict = {0:"airplane" , 1:"automobile" , 2:"bird" ,3:"cat" ,4:"deer" ,
              5:"dog" ,6:"frog" ,7:"horse" ,8:"ship" ,9:"truck" }


# 建立模型(線性堆疊)
model = Sequential()
# 設定一 二層的參數，輸入為32x32的彩色圖片
# 以及用來處理卷積運算的特徵值，是一個3乘3的矩陣
model.add(Conv2D(filters=32 , kernel_size=(3,3),
                 input_shape=(32,32,3),
                 activation="relu",
                 padding="same"))

# 設定二、三層的參數，設定每次池化的大小
# 一個2乘2的移動視窗
model.add(MaxPooling2D(pool_size=(2,2)))

# 再一次卷積、池化
# 設定三、四層的參數，輸入為32x32的彩色圖片
# 以及用來處理卷積運算的特徵值，是一個3乘3的矩陣
model.add(Conv2D(filters=64 , kernel_size=(3,3),
                 activation="relu",
                 padding="same"))

# 設定四、五層的參數，設定每次池化的大小
# 一個2乘2的移動視窗
model.add(MaxPooling2D(pool_size=(2,2)))


# 多維資料 -> 一維資料
model.add(Flatten())

# 接著就是加入下一層的神經網路
# 激發函數是使用線性整流函式
model.add(Dense(1024,activation="relu"))

# 只有十種的輸出類型
model.add(Dense(10, activation="softmax"))

'''

'''
CIFAR 訓練模型與分析效能

from keras.datasets import  cifar10
import numpy as np
import matplotlib.pyplot as plt
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation,Flatten
from keras.layers import Conv2D , MaxPooling2D , ZeroPadding2D

# 印出圖像
def show(x_img,y_label,i):
    print("label:",label_dict[y_label[i][0]],"predict: ???")
    plt.figure(figsize=(2,2))
    plt.imshow(x_img[i])
    plt.show()


# 這個功能就是從外部的雲端空間
# 去下載一個 CIFAR10 的資料集到我們的專案裡面
(x_img_train,y_label_train),(x_img_test , y_label_test) = cifar10.load_data()

# 正規化
x_img_train_normalize = x_img_train.astype("float32") / 255.0
x_img_test_normalize = x_img_test.astype("float32") / 255.0

# OneHotEncoding
y_label_train_OneHot = np_utils.to_categorical(y_label_train)
y_label_test_OneHot = np_utils.to_categorical(y_label_test)

# 將圖片種類的數字編號 轉換成 可讀的字串
label_dict = {0:"airplane" , 1:"automobile" , 2:"bird" ,3:"cat" ,4:"deer" ,
              5:"dog" ,6:"frog" ,7:"horse" ,8:"ship" ,9:"truck" }


# 建立模型(線性堆疊)
model = Sequential()
# 設定一 二層的參數，輸入為32x32的彩色圖片
# 以及用來處理卷積運算的特徵值，是一個3乘3的矩陣
model.add(Conv2D(filters=32 , kernel_size=(3,3),
                 input_shape=(32,32,3),
                 activation="relu",
                 padding="same"))

# 設定二、三層的參數，設定每次池化的大小
# 一個2乘2的移動視窗
model.add(MaxPooling2D(pool_size=(2,2)))

# 再一次卷積、池化
# 設定三、四層的參數，輸入為32x32的彩色圖片
# 以及用來處理卷積運算的特徵值，是一個3乘3的矩陣
model.add(Conv2D(filters=64 , kernel_size=(3,3),
                 activation="relu",
                 padding="same"))

# 設定四、五層的參數，設定每次池化的大小
# 一個2乘2的移動視窗
model.add(MaxPooling2D(pool_size=(2,2)))


# 多維資料 -> 一維資料
model.add(Flatten())

# 接著就是加入下一層的神經網路
# 激發函數是使用線性整流函式
model.add(Dense(1024,activation="relu"))

# 只有十種的輸出類型
model.add(Dense(10, activation="softmax"))


# 訓練模型
model.compile(loss="categorical_crossentropy" , optimizer="adam" , metrics=["accuracy"])

# 開始訓練
train_history = model.fit(x_img_train_normalize , y_label_train_OneHot,
                          validation_split=0.2,
                          epochs=10 , batch_size=128 , verbose=0)
# 訓練準確率
scores = model.evaluate(x_img_test_normalize , y_label_test_OneHot)

print(scores[1],"\n")

# 訓練結果
prediction = model.predict_classes(x_img_test_normalize)
# 預測答案
print(prediction[:10],"\n")
# 正確答案
print(y_label_test[:10],"\n")
'''





'''
CIFAR 結果圖像化
'''
from keras.datasets import  cifar10
import numpy as np
import matplotlib.pyplot as plt
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation,Flatten
from keras.layers import Conv2D , MaxPooling2D , ZeroPadding2D

# 印出圖像(圖像,標準答案,預測答案,ID)
def show(x_img,y_label,pre,i):
    print("label:",label_dict[y_label[i][0]],
          "predict:",label_dict[pre[i]])
    plt.figure(figsize=(2,2))
    plt.imshow(x_img[i])
    plt.show()

# 印出圖像(多筆)(圖像,標準答案,預測答案,起始位置,數量)
def plot_images_labels_prediction(images,labels,pre,idx,num):
    # 設定畫布
    fig = plt.gcf()
    # 設定畫布大小
    fig.set_size_inches(12,14)
    # 最大可印資料數
    if num>25: num=25
    # 印出圖像
    for i in range(0,num):
        ax = plt.subplot(5,5,1+i)
        ax.imshow(images[idx])

        title = str(idx) + ":" + label_dict[labels[idx][0]]
        title = title + label_dict[pre[idx]]

        ax.set_title(title,fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])

        idx = idx + 1

    plt.show()

# 預測資訊
def show_prediction_probability(images , labels , pre , pro , idx):
    print("label:", label_dict[labels[idx][0]],
          "predict:", label_dict[pre[idx]])
    plt.figure(figsize=(2, 2))
    plt.imshow(x_img_test[idx])
    plt.show()
    # 印出上面的圖像，10個種類的預測資訊
    for i in range(10):
        print(label_dict[i] + "probability:%1.9f"%(pro[idx][i]))

# 全部預測資訊
def show_all_prediction_probability():
    for i in range(10000):
        # 圖像實際為狗
        if y_label_test[i][0] == 5:
            # 預測卻為貓
            if prediction[i] == 3:
                print(i)

# 這個功能就是從外部的雲端空間
# 去下載一個 CIFAR10 的資料集到我們的專案裡面
(x_img_train,y_label_train),(x_img_test , y_label_test) = cifar10.load_data()

# 正規化
x_img_train_normalize = x_img_train.astype("float32") / 255.0
x_img_test_normalize = x_img_test.astype("float32") / 255.0

# OneHotEncoding
y_label_train_OneHot = np_utils.to_categorical(y_label_train)
y_label_test_OneHot = np_utils.to_categorical(y_label_test)

# 將圖片種類的數字編號 轉換成 可讀的字串
label_dict = {0:"airplane" , 1:"automobile" , 2:"bird" ,3:"cat" ,4:"deer" ,
              5:"dog" ,6:"frog" ,7:"horse" ,8:"ship" ,9:"truck" }


# 建立模型(線性堆疊)
model = Sequential()
# 設定一 二層的參數，輸入為32x32的彩色圖片
# 以及用來處理卷積運算的特徵值，是一個3乘3的矩陣
model.add(Conv2D(filters=32 , kernel_size=(3,3),
                 input_shape=(32,32,3),
                 activation="relu",
                 padding="same"))

# 設定二、三層的參數，設定每次池化的大小
# 一個2乘2的移動視窗
model.add(MaxPooling2D(pool_size=(2,2)))

# 再一次卷積、池化
# 設定三、四層的參數，輸入為32x32的彩色圖片
# 以及用來處理卷積運算的特徵值，是一個3乘3的矩陣
model.add(Conv2D(filters=64 , kernel_size=(3,3),
                 activation="relu",
                 padding="same"))

# 設定四、五層的參數，設定每次池化的大小
# 一個2乘2的移動視窗
model.add(MaxPooling2D(pool_size=(2,2)))


# 多維資料 -> 一維資料
model.add(Flatten())

# 接著就是加入下一層的神經網路
# 激發函數是使用線性整流函式
model.add(Dense(1024,activation="relu"))

# 只有十種的輸出類型
model.add(Dense(10, activation="softmax"))


# 訓練模型
model.compile(loss="categorical_crossentropy" , optimizer="adam" , metrics=["accuracy"])

# 開始訓練
train_history = model.fit(x_img_train_normalize , y_label_train_OneHot,
                          validation_split=0.2,
                          epochs=10 , batch_size=128 , verbose=0)

# 訓練結果
prediction = model.predict_classes(x_img_test_normalize)

# 印出圖像
show(x_img_test,y_label_test,prediction,185)

# 印出圖像(多筆)
#plot_images_labels_prediction(x_img_test , y_label_test , prediction , 10 ,8 )

# 進一步的訓練結果
#prediction_probability = model.predict(x_img_test_normalize)
#show_prediction_probability(x_img_test , y_label_test , prediction,prediction_probability , 0)































