# Author:gg

# License: BSD 3 clause

import numpy as np
import datetime
import matplotlib.pyplot as plt


def count_time(func):
    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()  # 程序开始时间
        func(*args,**kwargs)
        over_time = datetime.datetime.now()   # 程序结束时间
        total_time = (over_time-start_time).total_seconds()
        print('程序共计%s秒' % total_time)
    return int_time

class Perceptron():
    def __init__(self,):
        self._kernel =None
        self._x = None
        self._alpha = 0
        self._w = 0
        self._b = 0

    def _poly(self, x, y, p=4):
        # 使用poly核,默认+1,
        # 一搬用核的话,很多情况下是用对偶得出的形式
        return (x.dot(y.T) + 1) ** p

    @count_time
    def fit(self,x,y,kernel='poly',p=None,lr=0.1,epoch=10000,batch_size = 128,dual=True):

        x,y = np.asarray(x,np.float64),np.asarray(y,np.float64)
        self._w = np.zeros(x.shape[1])
        self._alpha = np.zeros(len(x))
        if kernel=='poly':
            p = 4 if p is None else p
            self._kernel = lambda x_, y_: self._poly(x_, y_, p)
        #print(k_mat.dot(self._alpha).shape)
        #dual loop
        if dual:
            k_mat = self._kernel(x, x)
            for epoch_index in range(epoch):
                #最好不要在这里判断是否是dual，否则每次循环都会带来开销
                indices =np.random.permutation(len(y))[:batch_size]
                y_batch,k_mat_batch = y[indices],k_mat[indices]
                err = y_batch*(k_mat_batch.dot(self._alpha)+self._b)
                if np.min(err) >0:
                    print('no missClass,epoch = {epoch}'.format(epoch=epoch_index))
                    continue
                mask = err <=0
                self._alpha += np.sum(y_batch[mask][:,None] *lr* (k_mat_batch[mask]),axis=0)
                self._b += np.sum(lr * y)
                #print(self._alpha)
                #print(self._b)
        else:
            #primal loop
            for epoch_index in range(epoch):
                indices = np.random.permutation(len(y))[:batch_size]
                y_batch, k_mat_batch = y[indices], x[indices]
                err = y_batch * (k_mat_batch.dot(self._alpha) + self._b)
                if np.min(err) > 0:
                    print('no missClass,epoch = {epoch}'.format(epoch=epoch_index))
                    continue
                mask = err <= 0
                self._alpha += np.sum(y_batch[mask][:, None] * lr * (k_mat_batch[mask]), axis=0)
                self._b += np.sum(lr * y)
                # print(self._alpha)
                # print(self._b)

    def predict(self,x):
        k_mat = self._kernel(x,x)
        y_pred = np.sign(self._alpha.dot(k_mat)+self._b).astype(np.float32)
        print(y_pred)
        return y_pred

    def _gd_dual(self,x,y,lr):
        self._alpha+=lr
        self._b += np.sum(lr*y)
        return

    def _gd_primal(self,x,y,lr):
        self._w += lr*x.dot(y)
        self._b += np.sum(lr*y)
        return





