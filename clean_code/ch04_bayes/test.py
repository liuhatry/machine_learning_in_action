# -*- coding: utf-8 -*-

import bayes

if __name__ == "__main__":
    # 1、词表
    listOPosts, listClasses = bayes.loadDataSet()
    myVocabList = bayes.createVocabList(listOPosts)
    print myVocabList

    # 2、词向量
    print bayes.setOfWords2Vec(myVocabList, listOPosts[0])
    print bayes.setOfWords2Vec(myVocabList, listOPosts[1])

    # 3、训练算法，计算概率p0V, p1V, pAb
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(bayes.setOfWords2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = bayes.trainNB0(trainMat, listClasses)
    print p0V
    print p1V
    print pAb

    # 4、测试算法
    bayes.testingNB()

    # 5. 过滤垃圾邮件测试
    bayes.spamTest()

