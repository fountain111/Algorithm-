import numpy as np
import matplotlib.pyplot as plt

from perceptron import *

class LinearSvm():
    def __init__(self):
        self.w = np.array([1.0,10000.0])
        self.b = np.float64(100.0)
        self.lr = 0.01
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
        x_list = []
        y_list = []

        for i in range(self.epoch):
            #pre = y*(w.dot(x.T)+b)
            #mask = pre<1
            self.w *= (1 - self.lr)
            x_, y_ = self.super_plane(-300, 300)
            print(i)
            x_list.append(x_)
            y_list.append(y_)

        return x_list,y_list

    def grdient_descent(self):
        self.w *=(1-self.r)
        return

    def super_plane(self, x_start, x_end):
        # 直线作为分界面。
        w = self.w
        b = self.b
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

    def plot_superplane_ani(self, x, y, fig, ax):
        # 动态展示
        line, = ax.plot([], [], 'k-')

        def init():
            line.set_data([], [])
            return line,

        def animate(i):
            # update the data
            try:
                line.set_xdata(x[i])
                line.set_ydata(y[i])
            except IndexError:
                print('already done')
                return line
            return line,

        ani = animation.FuncAnimation(
            fig, func=animate, init_func=init,
            interval=10, blit=True, save_count=50)

        plt.show()
        plt.plot(x[-1], y[-1])
        plt.savefig('./static/test.png')