# -*- coding: utf-8 -*-

import common_util

if __name__ == "__main__":
    myDat, labels = common_util.createDataSet()
    print common_util.calcShannonEnt(myDat)
    # 数据集增加一个分类，熵变大
    myDat[0][-1] = 'maybe'
    print common_util.calcShannonEnt(myDat)

