import numpy as np
import matplotlib.pyplot as plt

from perceptron import *

class LinearSvm():
    def __init__(self):
        self.w = np.array([10.0,10000.0])
        self.b = np.float64(2.0)
        self.lr = 0.1
        self.epoch = 10000
        self.bath_size = 10
        self.c = 0.1
        self.xi = 0
    def objective(self):
        #目标函数
        #带约束
        pass
        return
    def train(self,samples,hard_margin=True):
        # 损失函数只对分错的样本进行训练。如果要对每个分错的样本进行训练,那么梯度值要设计的很小,否则w应该会来回的在不同
        #的样本之间震荡,比较合理的方法是对一批样本的梯度取平均,
        #对于正确分类的样本没必要进行梯度下降,因为一般对w求偏导之后,正确分类的样本的偏导等于0,
        # 那么如果在各个维度上都采用一样的学习率,只是对w的线性组合,也没有其他依据能对w进行寻优。
        #if hard_margin:
         #   self.c = 1

        x = np.asarray(samples[0],np.float32)
        y = np.asarray(samples[1],np.float32)
        x_list = []
        y_list = []

        for i in range(self.epoch):
            pre = y*(self.w.dot(x.T)+self.b)
            mask = pre<1

            if np.min(pre) >=1:
                print(np.min(pre))
                continue

            self.grdient_descent_mean(x[mask],y[mask])
            #生成数据点,也就是生成分界面
            x_, y_ = self.super_plane(-300, 300)
            x_list.append(x_)
            y_list.append(y_)

        return x_list,y_list

    def grdient_descent_mean(self,x,y):
        #求梯度平均
        self.w *= 1-self.lr

        self.w +=  np.mean(self.c*y[:,None]*x,axis=0)
        self.b += np.mean(self.lr*self.c*y,axis=0)

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
            line.set_xdata(x[i])
            line.set_ydata(y[i])
            return line,

        ani = animation.FuncAnimation(
            fig, func=animate, init_func=init,
            interval=100, blit=True, save_count=50)

        plt.show()
        plt.plot(x[-1], y[-1])
        plt.savefig('./static/test.png')