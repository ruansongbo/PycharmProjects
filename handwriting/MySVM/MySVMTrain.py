#from MySVM.MySVM import *
from MySVM import MySVM
svm = MySVM()
svm.C = 100
svm.tol = 0.001
svm.maxIter = 10000
svm.kValue['Gaussian'] = 2.0
svm.loadMnistData()
svm.train()
print shape(svm.sptVects)[0]
print "b:",svm.b