# -*- coding: utf-8 -*-
'''
利用散点图（scatter）对数据进行分析

Created on May 19, 2015
@author: hatryliu
'''
from numpy import *
from utlis import *
import matplotlib.pyplot as plt

# 1）读取数据画图
plt.figure()
plt.subplot(2,2,1)

# 加载数据 
datingDataMat,datingLabels = file2matrix('data/datingTestSet.txt')

# 散点图,http://matplotlib.org/api/pyplot_api.html?highlight=scatter#matplotlib.pyplot.scatter
# 颜色和大小一样，默认值
# ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
# label不同，颜色和大小不一样
plt.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*array(datingLabels), 15.0*array(datingLabels))

# 设置x,y轴的范围
plt.axis([-2,25,-0.2,2.0])

plt.xlabel('Percentage of Time Spent Playing Video Games')
plt.ylabel('Liters of Ice Cream Consumed Per Week')

# 2）产生一些随机数据画图
n = 1000 #number of points to create
xcord1 = []; ycord1 = []
xcord2 = []; ycord2 = []
xcord3 = []; ycord3 = []
markers =[]
colors =[]

for i in range(n):
    [r0,r1] = random.standard_normal(2)
    myClass = random.uniform(0,1)
    if (myClass <= 0.16):
        fFlyer = random.uniform(22000, 60000)
        tats = 3 + 1.6*r1
        markers.append(20)
        colors.append(2.1)
        classLabel = 1 #'didntLike'
        xcord1.append(fFlyer); ycord1.append(tats)
    elif ((myClass > 0.16) and (myClass <= 0.33)):
        fFlyer = 6000*r0 + 70000
        tats = 10 + 3*r1 + 2*r0
        markers.append(20)
        colors.append(1.1)
        classLabel = 1 #'didntLike'
        if (tats < 0): tats =0
        if (fFlyer < 0): fFlyer =0
        xcord1.append(fFlyer); ycord1.append(tats)
    elif ((myClass > 0.33) and (myClass <= 0.66)):
        fFlyer = 5000*r0 + 10000
        tats = 3 + 2.8*r1
        markers.append(30)
        colors.append(1.1)
        classLabel = 2 #'smallDoses'
        if (tats < 0): tats =0
        if (fFlyer < 0): fFlyer =0
        xcord2.append(fFlyer); ycord2.append(tats)
    else:
        fFlyer = 10000*r0 + 35000
        tats = 10 + 2.0*r1
        markers.append(50)
        colors.append(0.1)
        classLabel = 3 #'largeDoses'
        if (tats < 0): tats =0
        if (fFlyer < 0): fFlyer =0
        xcord3.append(fFlyer); ycord3.append(tats)    

plt.subplot(224)
type1 = plt.scatter(xcord1, ycord1, s=20, c='red')
type2 = plt.scatter(xcord2, ycord2, s=30, c='green')
type3 = plt.scatter(xcord3, ycord3, s=50, c='blue')
# 添加图例
plt.legend([type1, type2, type3], ["Did Not Like", "Liked in Small Doses", "Liked in Large Doses"], loc=2)
# 设置x、y轴范围
plt.axis([-5000,100000,-2,25])

plt.xlabel('Frequent Flyier Miles Earned Per Year')
plt.ylabel('Percentage of Time Spent Playing Video Games')
plt.show()