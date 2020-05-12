"""完整程式碼"""

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
