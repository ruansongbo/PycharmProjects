# -*- coding: utf-8 -*-
from numpy import *
import numpy as np
from SVM import SVM
from Data.mnistData import *

################## test svm #####################
## step 1: load data
print "step 1: load data..."
mnistData = mnistData()
print shape(mnistData.traindataMat)
print shape(mnistData.traindataLabel)
## step 2: training...
print "step 2: training..."
C = 1.0
toler = 0.1
maxIter = 1000
svmClassifier = SVM.trainSVM(mnistData.traindataMat, mnistData.traindataLabel, C, toler, maxIter, kernelOption=('rbf', 0.01))
## step 3: testing
print "step 3: testing..."
print shape(mnistData.testdataMat)
predict = SVM.testSVM(svmClassifier, mnistData.testdataMat)
print predict

## step 4: show the result
print "step 4: show the result..."
#print 'The classify accuracy is: %.3f%%' % (accuracy * 100)
SVM.showSVM(svmClassifier)