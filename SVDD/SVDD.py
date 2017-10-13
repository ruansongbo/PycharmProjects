import numpy as np
from numpy import *
import time
import cPickle as pickle
from sklearn import svm
import matplotlib.pyplot as plt
import matplotlib.font_manager

def loadDataSet(filename):
    fr = open(filename)
    X = []
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        X.append([float(lineArr[0]), float(lineArr[1])])
    out = mat(X)
    return out
if __name__ == '__main__':
    ################## test svdd #####################
    xx, yy = np.meshgrid(np.linspace(-5, 5, 500), np.linspace(-5, 5, 500))
    ## step 1: load data
    print "step 1: load data..."
    A = loadDataSet('1082.txt');
    #B = loadDataSet('1082-1.txt');
    #C = loadDataSet('1082-2.txt');
    #D = loadDataSet('1082-3.txt');

    ## step 2: fit the model
    clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
    clf.fit(A)
    y_pred_train = clf.predict(A)
    n_error_train = y_pred_train[y_pred_train == -1].size
    print "n_error_train:", n_error_train

    # plot the line, the points, and the nearest vectors to the plane
    Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.title("Novelty Detection")
    plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.PuBu)
    a = plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='darkred')
    plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors='palevioletred')

    s = 40
    b1 = plt.scatter(A[:, 0], A[:, 1], c='white', s=s)
    #b2 = plt.scatter(X_test[:, 0], X_test[:, 1], c='blueviolet', s=s)
    #c = plt.scatter(X_outliers[:, 0], X_outliers[:, 1], c='gold', s=s)
    plt.axis('tight')
    plt.xlim((-5, 5))
    plt.ylim((-5, 5))
    plt.legend([a.collections[0], b1],
               ["learned frontier", "training observations",
                "new regular observations", "new abnormal observations"],
               loc="upper left",
               prop=matplotlib.font_manager.FontProperties(size=11))
    plt.xlabel(
        "error train: %d/200 "
        % (n_error_train))
    plt.show()