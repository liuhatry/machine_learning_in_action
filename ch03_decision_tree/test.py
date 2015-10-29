# -*- coding: utf-8 -*-

import trees
import treePlotter

if __name__ == "__main__":
    #1、单元测试
    # 创建数据集
    myDat, labels = trees.createDataSet()

    # 熵测试
    print trees.calcShannonEnt(myDat)
    # 数据集增加一个分类，熵变大
    myDat[0][-1] = 'maybe'
    print trees.calcShannonEnt(myDat)

    # 数据集划分测试
    print myDat
    print trees.splitDataSet(myDat, 0, 1)
    print trees.splitDataSet(myDat, 0, 0)

    # 选择最好的feature
    print trees.chooseBestFeatureToSplit(myDat)

    #2、整体测试
    # 创建树
    myDat, labels = trees.createDataSet()
    labels_bak = labels[:]
    myTree = trees.createTree(myDat, labels)
    print myTree

    # 评估
    print labels_bak
    print trees.classify(myTree, labels_bak, [1,0])
    print trees.classify(myTree, labels_bak, [1,1])

    #3、隐形眼镜推荐测试
    fr = open('lenses.txt')
    lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    lensesLabels = ['age', 'prescript', 'astigmatic', 'rearRate']
    lensesTree = trees.createTree(lenses, lensesLabels)
    print lensesTree
    treePlotter.createPlot(lensesTree)
