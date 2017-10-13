# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
import struct
from numpy import *
import matplotlib.pyplot as plt
from operator import itemgetter, attrgetter
import time
import cPickle as pickle

class mnistData(object):
    def __init__(self):
        startTime = time.time()
        trainfile_0 = open("C:\\Users\\bb\\PycharmProjects\\handwriting\\traindata\\obj_1.dat", "rb")
        trainfile_1 = open("C:\\Users\\bb\\PycharmProjects\\handwriting\\traindata\\obj_2.dat", "rb")
        traindatamat_0 = pickle.load(trainfile_0)
        traindatamat_1 = pickle.load(trainfile_1)
        self.traindataMat = np.vstack((traindatamat_0, traindatamat_1))
        self.traindataLabel = np.vstack((np.ones((100, 1), dtype='int32'), np.ones((100, 1), dtype='int32') * -1))

        testfile_0 = open("C:\\Users\\bb\\PycharmProjects\\handwriting\\testdata\\obj_1.dat", "rb")
        testfile_1 = open("C:\\Users\\bb\\PycharmProjects\\handwriting\\testdata\\obj_2.dat", "rb")
        testdatamat_0 = pickle.load(testfile_0)
        testdatamat_1 = pickle.load(testfile_1)
        self.testdataMat = np.vstack((testdatamat_0, testdatamat_1))
        self.testdataLabel = np.vstack((np.ones((50, 1), dtype='int32'), np.ones((50, 1) * -1, dtype='int32')))
        print 'Loading complete! Took %fs!' % (time.time() - startTime)

