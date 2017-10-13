# -*- coding: utf-8 -*-
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import cPickle as pickle
class MySVM(object):
    def __init__(self):
        self.X = []
        self.labelMat = []
        self.C = 0
        self.tol = 0
        self.b = 0
        self.kValue = {}
        self.maxIter = 100
        self.svIndex = []
        self.sptVects = []
    def loadDataSet(self,filename):
        fr = open(filename)
        for line in fr.readlines():
            lineArr = line.strip().split(',')
            self.X.append([float(lineArr[0]),float(lineArr[1])])
            self.labelMat.append(float(lineArr[2]))
        self.initparam()
    def loadMnistData(self):
        trainfile_0 = open("traindata\\obj_0.dat", "rb")
        trainfile_1 = open("traindata\\obj_1.dat", "rb")
        traindatamat_0 = pickle.load(trainfile_0)
        traindatamat_1 = pickle.load(trainfile_1)
        trainlabel_0 = mat(ones((1000, 1)))
        trainlabel_1 = mat(ones((1000, 1))) * -1
        self.X = np.vstack((traindatamat_0, traindatamat_1))
        self.labelMat = np.vstack((trainlabel_0, trainlabel_1))
        self.initparam()
    def initparam(self):
        self.X = mat(self.X)
        self.labelMat = mat(self.labelMat).T
        self.m = shape(self.X)[0]
        self.lambdas = mat(zeros((self.m,1)))
        self.eCache = mat(zeros((self.m,2)))
        self.K = mat(zeros((self.m,self.m)))
        for i in xrange(self.m):
            self.K[:,i] = self.kernels(self.X,self.X[i,:])

    def scatterplot(self,plt):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for i in xrange(shape(self.X)[0]):
            if self.lambdas[i] != 0:
                ax.scatter(self.X[i, 0], self.X[i, 1], c='green', marker='s')
            elif self.labelMat[i] == 1:
                ax.scatter(self.X[i, 0], self.X[i, 1], c='blue', marker='s')
            elif self.labelMat[i] == -1:
                ax.scatter(self.X[i, 0], self.X[i, 1], c='red', marker='s')

    def kernels(self,dataMat,A):
        m,n = shape(dataMat)
        K = mat(zeros((m,1)))
        if self.kValue.keys()[0] == 'linear':
            K = dataMat * A.T
        elif self.kValue.keys()[0] == 'Gaussian':
            for j in xrange(m):
                deltaRow = dataMat[j,:] - A
                K[j] = deltaRow*deltaRow.T
            K = exp(K/(-1*self.kValue['Gaussian']**2))
        else: raise NameError('无法识别的核函数')
        return K

    def chooseJ(self,i,Ei):
        maxK = -1;maxDeltaE = 0;Ej = 0
        self.eCache[i] = [1,Ei]
        validEcacheList = nonzero(self.eCache[:,0].A)[0]
        if(len(validEcacheList))>1:
            for k in validEcacheList:
                if k == i: continue
                Ek = self.calcEk(k)
                deltaE = abs(Ei - Ek)
                if(deltaE > maxDeltaE):
                    maxK = k; maxDeltaE = deltaE; Ej = Ek
            return maxK,Ej
        else:
            j = self.randJ(i)
            Ej = self.calcEk(j)
        return j,Ej

    def randJ(self,i):
        j = i
        while(j == i):
            j = int(random.uniform(0,self.m))
        return j

    def calcEk(self,k):
        output_k = float(multiply(self.lambdas,self.labelMat).T * self.K[:,k] + self.b)
        error_k = output_k - float(self.labelMat[k])
        return error_k
        #return float(multiply(self.lambdas,self.labelMat).T*self.K[:,k]+self.b)-float(self.labelMat[k])

    def cliplambda(self,aj,H,L):
        if aj > H: aj = H
        if L > aj: aj = L
        return aj

    def train(self):
        step = 0
        entireflag = True; lambdaPairsChanged = 0
        while (step < self.maxIter) and ((lambdaPairsChanged > 0) or (entireflag)):
            lambdaPairsChanged = 0
            if entireflag:
                for i in xrange(self.m):
                    lambdaPairsChanged += self.innerLoop(i)
                step += 1
            else:
                nonBoundIs = nonzero((self.lambdas.A > 0) * (self.lambdas.A < self.C))[0]
                for i in nonBoundIs:
                    lambdaPairsChanged += self.innerLoop(i)
                step += 1
            if entireflag: entireflag = False
            elif (lambdaPairsChanged == 0): entireflag = True
        self.svIndex = nonzero(self.lambdas.A>0)[0]
        self.sptVects = self.X[self.svIndex]
        self.SVlabel = self.labelMat[self.svIndex]

    def innerLoop(self,i):
        Ei = self.calcEk(i)
        if((self.labelMat[i]*Ei < -self.tol) and (self.lambdas[i] < self.C)) or ((self.labelMat[i]*Ei > self.tol) and self.lambdas[i] > 0):
            j,Ej = self.chooseJ(i,Ei)
            lambdaIold = self.lambdas[i].copy()
            lambdaJold = self.lambdas[j].copy()
            if (self.labelMat[i] != self.labelMat[j]):
                L = max(0,self.lambdas[i] - self.lambdas[j])
                H = min(self.C,self.C + self.lambdas[j] - self.lambdas[i])
            else:
                L = max(0,self.lambdas[j] + self.lambdas[i] - self.C)
                H = min(self.C,self.lambdas[j] + self.lambdas[i])
            if L == H: return 0
            eta = 2.0 * self.K[i,j] - self.K[i,i] - self.K[j,j]
            if eta >= 0: return 0
            self.lambdas[j] -= self.labelMat[j]*(Ei - Ej)/eta
            self.lambdas[j] = self.cliplambda(self.lambdas[j],H,L)
            self.eCache[j] = [1,self.calcEk(i)]
            if(abs(self.lambdas[j] - lambdaJold) < 0.00001):  return 0
            self.lambdas[i] += self.labelMat[j]*self.labelMat[i]*(lambdaJold - self.lambdas[j])
            self.eCache[i] = [1,self.calcEk(i)]
            b1 = self.b - Ei - self.labelMat[i] * (self.lambdas[i] - lambdaIold) * self.K[i, i] - self.labelMat[j] * (self.lambdas[j] - lambdaJold) * self.K[i, j]
            b2 = self.b - Ej - self.labelMat[i] * (self.lambdas[i] - lambdaIold) * self.K[i, j] - self.labelMat[j] * (self.lambdas[j] - lambdaJold) * self.K[j, j]
            if (0 < self.lambdas[i]) and (self.C > self.lambdas[i]): self.b = b1
            elif (0 < self.lambdas[j]) and (self.C > self.lambdas[j]): self.b = b2
            else: self.b = (b1+b2)/2.0
            return 1
        else: return 0
    def classify(self,testSet,testLabel):
        errorCount = 0;
        testMat = mat(testSet)
        m,n = shape(testMat)
        for i in xrange(m):
            kernelEval = self.kernels(self.sptVects,testMat[i,:])
            predict = kernelEval.T*multiply(self.SVlabel,self.lambdas[self.svIndex]) + self.b
            if sign(predict) != sign(testLabel[i]): errorCount += 1
        return float(errorCount)/float(m)
