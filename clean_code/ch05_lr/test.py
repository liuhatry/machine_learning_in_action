# -*- coding: utf-8 -*-
import logRegres

1、训练数据
dataArr, labelMat = logRegres.loadDataSet()
print dataArr
print labelMat

2、梯度下降
weights = logRegres.gradAscent(dataArr, labelMat)
print weights

3、画图
logRegres.plotBestFit(weights.getA())

4、随机梯度下降

