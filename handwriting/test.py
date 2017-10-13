# -*- coding: utf-8 -*-
from numpy import *
import numpy as np
from SVM import SVM

################## test svm #####################
## step 1: load data
print "step 1: load data..."
# dataSet = []
# labels = []
# fileIn = open('data.txt')
# for line in fileIn.readlines():
#     lineArr = line.strip().split(',')
#     dataSet.append([float(lineArr[0]), float(lineArr[1])])
#     labels.append(float(lineArr[2]))
#
# dataSet = mat(dataSet)
# labels = mat(labels).T
# train_x = dataSet[0:81, :]
# train_y = labels[0:81, :]
# test_x = dataSet[80:101, :]
# test_y = labels[80:101, :]


# 训练的点数
train_pts = 30

# 创建测试的数据点，2类
# 以(-1.5, -1.5)为中心
rand1 = np.ones((train_pts, 2)) * (-2) + np.random.rand(train_pts, 2)
print('rand1：')
print(rand1)

# 以(1.5, 1.5)为中心
rand2 = np.ones((train_pts, 2)) + np.random.rand(train_pts, 2)
print('rand2:')
print(rand2)

# 合并随机点，得到训练数据
train_data = np.vstack((rand1, rand2))
train_x = np.array(train_data, dtype='float32')
train_y = np.vstack((np.ones((train_pts, 1), dtype='int32'), np.ones((train_pts, 1), dtype='int32')*-1))
#train_y = np.vstack((np.zeros((train_pts, 1), dtype='int32'), np.ones((train_pts, 1), dtype='int32')))
print shape(train_x)
print shape(train_y)
## step 2: training...
print "step 2: training..."
C = 100
toler = 0.001
maxIter = 10000
svmClassifier = SVM.trainSVM(train_x, train_y, C, toler, maxIter, kernelOption=('rbf', 3.0))
## step 3: testing
print "step 3: testing..."
# # 测试数据，20个点[-2,2]
test_x = np.array(np.random.rand(20,2) * 4 - 2, dtype='float32')
predict = SVM.testSVM(svmClassifier, test_x)
print test_x
print predict

## step 4: show the result
print "step 4: show the result..."
#print 'The classify accuracy is: %.3f%%' % (accuracy * 100)
SVM.showSVM(svmClassifier)