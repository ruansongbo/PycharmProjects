# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
import struct
from numpy import *
import matplotlib.pyplot as plt
from operator import itemgetter, attrgetter
import time
from sklearn.decomposition import PCA
from sklearn import svm
import cPickle as pickle

#读取图片到dataMat
def read_image(filename):
    f = open(filename, 'rb')
    index = 0
    buf = f.read()
    f.close()
    magic, images, rows, columns = struct.unpack_from('>IIII' , buf , index)
    #images = 10
    index += struct.calcsize('>IIII')
    dataMat = np.zeros((images, rows*columns))
    for i in xrange(images):
        temp = struct.unpack_from('>784B', buf, index)
        dataMat[i] = temp
        index += 784

    #dataMat = np.round(dataMat/255)
    return dataMat

def read_label(filename):
    f = open(filename, 'rb')
    index = 0
    buf = f.read()
    f.close()
    magic, labels = struct.unpack_from('>II', buf, index)
    #labels = 10
    index += struct.calcsize('>II')
    datalabel = [0] * labels
    for x in xrange(labels):
        datalabel[x] = int(struct.unpack_from('>B', buf, index)[0])
        index += struct.calcsize('>B')
    return datalabel

# 读取训练数据
def read_all_data():
    dataMat = read_image('C:\\Users\\bb\\PycharmProjects\\handwriting\\Data\\t10k-images.idx3-ubyte')
    dataLabel = read_label('C:\\Users\\bb\\PycharmProjects\\handwriting\\Data\\t10k-labels.idx1-ubyte')
    data = zip(dataMat, dataLabel)
    sortdata = sorted(data,key=lambda x:x[1])
    return sortdata

if __name__ == '__main__':
    #testdataMat = read_image('C:\\Users\\bb\\PycharmProjects\\handwriting\\train-images.idx3-ubyte')
    #testdataLabel = read_label('C:\\Users\\bb\\PycharmProjects\\handwriting\\train-labels.idx1-ubyte')
    traindataMat = read_image('C:\\Users\\bb\\PycharmProjects\\handwriting\\Data\\t10k-images.idx3-ubyte')
    traindataLabel = read_label('C:\\Users\\bb\\PycharmProjects\\handwriting\\Data\\t10k-labels.idx1-ubyte')
    datasize = 50
    imageMat_0 = []
    index_0 = 0
    flag_0 = True
    imageMat_1 = []
    index_1 = 0
    flag_1 = True
    imageMat_2 = []
    index_2 = 0
    flag_2 = True
    imageMat_3 = []
    index_3 = 0
    flag_3 = True
    imageMat_4 = []
    index_4 = 0
    flag_4 = True
    imageMat_5 = []
    index_5 = 0
    flag_5 = True
    imageMat_6 = []
    index_6 = 0
    flag_6 = True
    imageMat_7 = []
    index_7 = 0
    flag_7 = True
    imageMat_8 = []
    index_8 = 0
    flag_8 = True
    imageMat_9 = []
    index_9 = 0
    flag_9 = True
    for i in xrange(10000):
        if traindataLabel[i] == 0:
            if flag_0:
                if index_0 > datasize-1:
                    image = mat(imageMat_0, dtype='float32')
                    print "finish 0"
                    file = open("..\\testdata\\obj_0.dat","wb")
                    pickle.dump(image,file)
                    file.close()
                    flag_0 = False
                else:
                    temp = traindataMat[i].copy()
                    imageMat_0.append(temp)
                    index_0 += 1
        elif traindataLabel[i] == 1:
            if flag_1:
                if index_1 > datasize-1:
                    image = mat(imageMat_1, dtype='float32')
                    print "finish 1"
                    file = open("..\\testdata\\obj_1.dat","wb")
                    pickle.dump(image,file)
                    file.close()
                    flag_1 = False
                else:
                    temp = traindataMat[i].copy()
                    imageMat_1.append(temp)
                    index_1 += 1
        elif traindataLabel[i] == 2:
            if flag_2:
                if index_2 > datasize-1:
                    image = mat(imageMat_2, dtype='float32')
                    print "finish 2"
                    file = open("..\\testdata\\obj_2.dat","wb")
                    pickle.dump(image,file)
                    file.close()
                    flag_2 = False
                else:
                    temp = traindataMat[i].copy()
                    imageMat_2.append(temp)
                    index_2 += 1
        elif traindataLabel[i] == 3:
            if flag_3:
                if index_3 > datasize-1:
                    image = mat(imageMat_3, dtype='float32')
                    print "finish 3"
                    file = open("..\\testdata\\obj_3.dat","wb")
                    pickle.dump(image,file)
                    file.close()
                    flag_3 = False
                else:
                    temp = traindataMat[i].copy()
                    imageMat_3.append(temp)
                    index_3 += 1
        elif traindataLabel[i] == 4:
            if flag_4:
                if index_4 > datasize-1:
                    image = mat(imageMat_4, dtype='float32')
                    print "finish 4"
                    file = open("..\\testdata\\obj_4.dat","wb")
                    pickle.dump(image,file)
                    file.close()
                    flag_4 = False
                else:
                    temp = traindataMat[i].copy()
                    imageMat_4.append(temp)
                    index_4 += 1
        elif traindataLabel[i] == 5:
            if flag_5:
                if index_5 > datasize-1:
                    image = mat(imageMat_5, dtype='float32')
                    print "finish 5"
                    file = open("..\\testdata\\obj_5.dat","wb")
                    pickle.dump(image,file)
                    file.close()
                    flag_5 = False
                else:
                    temp = traindataMat[i].copy()
                    imageMat_5.append(temp)
                    index_5 += 1
        elif traindataLabel[i] == 6:
            if flag_6:
                if index_6 > datasize-1:
                    image = mat(imageMat_6, dtype='float32')
                    print "finish 6"
                    file = open("..\\testdata\\obj_6.dat","wb")
                    pickle.dump(image,file)
                    file.close()
                    flag_6 = False
                else:
                    temp = traindataMat[i].copy()
                    imageMat_6.append(temp)
                    index_6 += 1
        elif traindataLabel[i] == 7:
            if flag_7:
                if index_7 > datasize-1:
                    image = mat(imageMat_7, dtype='float32')
                    print "finish 7"
                    file = open("..\\testdata\\obj_7.dat","wb")
                    pickle.dump(image,file)
                    file.close()
                    flag_7 = False
                else:
                    temp = traindataMat[i].copy()
                    imageMat_7.append(temp)
                    index_7 += 1
        elif traindataLabel[i] == 8:
            if flag_8:
                if index_8 > datasize-1:
                    image = mat(imageMat_8, dtype='float32')
                    print "finish 8"
                    file = open("..\\testdata\\obj_8.dat","wb")
                    pickle.dump(image,file)
                    file.close()
                    flag_8 = False
                else:
                    temp = traindataMat[i].copy()
                    imageMat_8.append(temp)
                    index_8 += 1
        elif traindataLabel[i] == 9:
            if flag_9:
                if index_9 > datasize-1:
                    image = mat(imageMat_9, dtype='float32')
                    print "finish 9"
                    file = open("..\\testdata\\obj_9.dat","wb")
                    pickle.dump(image,file)
                    file.close()
                    flag_9 = False
                else:
                    temp = traindataMat[i].copy()
                    imageMat_9.append(temp)
                    index_9 += 1