# -*- coding: utf-8 -*-
'''
Created on Oct 27, 2010

@author: hatryliu
'''
from numpy import *
import utils
import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

# 加载数据 
datingDataMat,datingLabels = utils.file2matrix('data/datingTestSet2.txt')

# 散点图,http://matplotlib.org/api/pyplot_api.html?highlight=scatter#matplotlib.pyplot.scatter
# 颜色和大小一样，默认值
# ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
# label不同，颜色和大小不一样
ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*array(datingLabels), 15.0*array(datingLabels))

# 设置x,y轴的范围
ax.axis([-2,25,-0.2,2.0])

plt.xlabel('Percentage of Time Spent Playing Video Games')
plt.ylabel('Liters of Ice Cream Consumed Per Week')
plt.show()
