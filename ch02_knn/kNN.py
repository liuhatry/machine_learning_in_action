# -*- coding: utf-8 -*-

'''
Created on Sep 16, 2010

本程序包含KNN分类器.

本程序包含两个测试：
    1、手写字识别测试；
    2、约会爱好测试

@author: hatryliu
'''
import operator
from numpy import *
from os import listdir
from utlis import *

def classify0(inX, dataSet, labels, k):
    """KNN分类器: k Nearest Neighbor
    
    Args:
       intX:输入(1xN)
       dataSet：训练数据(NxM)
       labels:训练数据label(1xM vector)
       k:  number of neighbors to use for comparison (should be an odd number)
       
    Return:
        the most popular class label
    """
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    # 将矩阵的每一行相加,得到一个列向量
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    # 返回从小到大排序的index
    sortedDistIndicies = distances.argsort()     
    classCount={}          
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def datingClassTest():
    # 将数据分为测试数据和训练数据两部分
    hoRatio = 0.50      #hold out 10%
    datingDataMat,datingLabels = file2matrix('data/datingTestSet.txt')       #load data setfrom file
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print "the total error rate is: %f" % (errorCount/float(numTestVecs))
    print errorCount
    
def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')           #load the training set
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]     #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        # 将一个数字文件转换成trainingMat的一行
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)

    testFileList = listdir('testDigits')        #iterate through the test set
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]     #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
        if (classifierResult != classNumStr): errorCount += 1.0
    print "\nthe total number of errors is: %d" % errorCount
    print "\nthe total error rate is: %f" % (errorCount/float(mTest))
    
if __name__ == '__main__':
    # 手写字识别测试
    handwritingClassTest()
    # 约会测试(对数据进行归一化) 1:didntLike 2:mallDoses 3:largeDoses
    datingClassTest()