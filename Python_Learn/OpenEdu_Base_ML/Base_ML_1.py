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
'''
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









