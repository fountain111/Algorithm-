import numpy as np
import matplotlib.pyplot as plt

from perceptron import *

class LinearSvm():
    def __init__(self):
        self.w =np.asarray([12,50],np.float32)
        self.b = 0
        self.lr = 0.5
        self.epoch = 1000
        self.bath_size = 10

    def objective(self):
        #目标函数
        #带约束
        pass
        return
    def train(self,samples):

        # 分错的样本,随机挑选一批分错的样本进行训练
        x = np.asarray(samples[0],np.float32)
        y = np.asarray(samples[1],np.float32)
        w = self.w
        b = self.b
        print(self.w.shape)


        for i in range(self.epoch):
            pre = y*(w.dot(x.T)+b)
            mask = pre<1
            print(pre[mask])
            idx =np.argmax(pre[mask])
            print(idx)
            print(pre[mask][idx])
            break

        return w,b

    def super_plane(self, x_start, x_end):
        # 直线作为分界面。
        w = self.w
        b = self.b
        print(w,b)
        x_list = []
        y_list = []
        slope = -w[0] / w[1]
        w_normal = np.sqrt(w.transpose().dot(w))
        b = b / w_normal
        for i in range(1, 100):
            x = np.random.randint(x_start, x_end)
            y = x * slope + b
            x_list.append(x)
            y_list.append(y)
        return x_list, y_list

    def plot_superplane(self, start=-300, end=300):
        # 画出分界面
        line_x_y = self.super_plane(start, end)
        plt.plot(line_x_y[0], line_x_y[1])
        plt.savefig('./static/test.png')