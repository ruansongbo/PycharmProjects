# -*- coding: utf-8 -*-
import numpy as np
from numpy import *
import time
import cPickle as pickle
import cv2
################## test svm #####################
## step 1: load data
print "step 1: load data..."
startTime = time.time()
trainfile_0 = open("traindata\\obj_1.dat","rb")
trainfile_1 = open("traindata\\obj_2.dat","rb")
traindatamat_0 = pickle.load(trainfile_0)
traindatamat_1 = pickle.load(trainfile_1)
traindataMat = np.vstack((traindatamat_0,traindatamat_1))
traindataLabel = np.vstack( (np.ones((1000,1), dtype='int32'), np.ones((1000,1)*-1, dtype='int32')))

testfile_0 = open("testdata\\obj_1.dat","rb")
testfile_1 = open("testdata\\obj_2.dat","rb")
testdatamat_0 = pickle.load(testfile_0)
testdatamat_1 = pickle.load(testfile_1)
testdataMat = np.vstack((testdatamat_0,testdatamat_1))
testdataLabel = np.vstack( (np.ones((500,1), dtype='int32'), np.ones((500,1), dtype='int32')*-1))
print 'Loading complete! Took %fs!' % (time.time() - startTime)
print shape(testdataMat)
print testdataLabel
print "step 2: training..."
svm = cv2.ml.SVM_create()
svm.setType(cv2.ml.SVM_C_SVC)  # SVM类型
svm.setKernel(cv2.ml.SVM_LINEAR) # 使用线性核
svm.setDegree(10.0)
svm.setGamma(0.01)
svm.setCoef0(1.0)
svm.setC(1.0)
svm.setNu(0.5)
svm.setP(0.1)
print type(traindataMat[1,1])
ret = svm.train(traindataMat, cv2.ml.ROW_SAMPLE, traindataLabel)
(ret, res) = svm.predict(testdataMat)




