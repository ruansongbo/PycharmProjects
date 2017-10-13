import matplotlib.pyplot as plt

from MySVM.MySVM import *

svm = MySVM()
svm.C = 0.6
svm.tol = 0.001
svm.maxIter = 10000
svm.kValue['linear'] = 1.0
svm.loadDataSet('data3.txt')
svm.train()
print svm.svIndex
print shape(svm.sptVects)[0]
print "b:",svm.b
svm.scatterplot(plt)
plt.show()