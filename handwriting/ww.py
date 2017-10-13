from PIL import Image
import numpy as np
import struct
from numpy import *
import matplotlib.pyplot as plt
from operator import itemgetter, attrgetter
import time
from sklearn.decomposition import PCA
from sklearn import svm
from sklearn import datasets
import cPickle as pickle
from Data.mnistData import *
mnistData = mnistData()
print shape(mnistData.traindataMat)
print type(mnistData.traindataMat)
print type(mnistData.traindataMat[1])
print type(mnistData.traindataMat[1,2])
im = mnistData.traindataMat[1,:]
im = im.reshape(28, 28)
fig = plt.figure()
plotwindow = fig.add_subplot(111)
plt.imshow(im, cmap='gray')
plt.show()