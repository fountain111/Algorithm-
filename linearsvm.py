import numpy as np
import matplotlib.pyplot as plt

from perceptron import *

class LinearSvm():
    def __init__(self):
        self.w = self.b = None
        self.lr = 0.5
        self.epoch = 1000
        self.bath_size = 10
    def train(self,samples):
        # 随机挑选一批分错的样本进行训练
        x = np.asarray(samples[0],np.float32)
        y = np.asarray(samples[1],np.float32)

        self.w = np.zeros(x.shape[1])
        self.b = 0

        for i in range(self.epoch):
            batch = np.random.choice(len(x),self.bath_size)
            predictors = []
            for value in samples:
                x = value[0]
                y = value[1]
                predictor = y*(w.dot(x)+b)
                if predictor <=1:
                    predictors.append(predictor)
            batchs = []
            for j in range(self.bath_size):
                batchs.append(predictors[np.random.randint(0,self.bath_size)])
            for x in batchs:


