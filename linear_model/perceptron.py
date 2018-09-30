# Author:

# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt

class Perceptron():
    def __init__(self,):
        self._kernel =None
        self._x = None

    def _poly(self, x, y, p=4):
        # 使用poly核,默认+1,
        # 一搬用核的话,很多情况下是用对偶对的

        return (x.dot(y.T) + 1) ** p

    def fit(self,x,y,kernel='poly',p=None,lr=0.001,epoch=10000):

        x,y = np.asarray(x,np.float64),np.asarray(y,np.float64)

        if kernel=='poly':
            p = 4 if p is None else p
            self._kernel = lambda x_, y_: self._poly(x_, y_, p)
        k_mat = self._kernel(x, x)
        print(k_mat.shape,x.shape)



