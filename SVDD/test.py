# -*- coding: utf-8 -*-
import numpy as np
from numpy import *
import time
import cPickle as pickle
from sklearn import svm
################## test svdd #####################
## step 1: load data
print "step 1: load data..."
trainfile_0 = open("traindata\\obj_0.dat","rb")
trainfile_1 = open("traindata\\obj_1.dat","rb")
traindatamat_0 = pickle.load(trainfile_0)
traindatamat_1 = pickle.load(trainfile_1)
trainlabel_0 = mat(ones((1000,1)))
trainlabel_1 = mat(ones((1000,1)))*-1
traindataMat = np.vstack((traindatamat_0,traindatamat_1))
traindataLabel = np.vstack((trainlabel_0,trainlabel_1))

testfile_0 = open("testdata\\obj_0.dat","rb")
testfile_1 = open("testdata\\obj_1.dat","rb")
testdatamat_0 = pickle.load(testfile_0)
testdatamat_1 = pickle.load(testfile_1)
testlabel_0 = mat(ones((1000,1)))
testlabel_1 = mat(ones((1000,1)))*-1
testdataMat = np.vstack((testdatamat_0,testdatamat_1))
testdataLabel = np.vstack((testlabel_0,testlabel_1))

## step 2: fit the model
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1, tol=0.001)
clf.fit(traindatamat_0)
y_pred_train = clf.predict(traindatamat_0)
y_pred_test = clf.predict(testdatamat_0)
y_pred_outliers = clf.predict(testdatamat_1)
n_error_train = y_pred_train[y_pred_train == -1].size
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
print "n_error_train:",n_error_train
print "n_error_test:",n_error_test
print "n_error_outliers:",n_error_outliers