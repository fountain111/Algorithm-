
import numpy as np
import matplotlib.pyplot as plt

'''
    Perceptron完成感知机的训练、画出分界面

    Samples完成样本点的生成和绘制。

'''

class Perceptron():
    def __init__(self):
        self.w = np.array([0.0,0.0])
        self.b = np.float64(1.0)
        self.lr = 0.5
        self.epoch = 1000
    def train(self,samples):
        w = self.w
        b= self.b
        for i in range(self.epoch):

            for value in samples:
                x = np.array(value[0])
                y = value[1]
                predict = self.w.dot(x) + self.b
                if predict > 0:
                    predict = 1
                else:
                    predict = -1
                if (y * predict <= 0):
                    w += self.lr*y*x
                    b = b + self.lr * y
                    print(i, w, b)

        return w, b

    def super_plane(self,x_start, x_end):
        #直线作为分界面。
        w = self.w
        b = self.b
        x_list = []
        y_list = []
        slope = -w[0]/w[1]
        w_normal = np.sqrt(w.transpose().dot(w))
        b = b/w_normal
        for i in range(1, 100):
            x = np.random.randint(x_start, x_end)
            y = x * slope + b
            x_list.append(x)
            y_list.append(y)
        return x_list, y_list

    def plot_superplane(self,start=-300,end=300):
        #画出分界面
        line_x_y = self.super_plane(start,end)
        plt.plot(line_x_y[0], line_x_y[1])
        plt.savefig('./static/test.png')


class Sammples():
    def generate_samples(self,start,end,size,dimm = 2):
        '''
        默认生成二维平面样本点
        :param start: 维度起始值
        :param end:
        :param size:
        :param dimm :维度
        :return: [[coordinate],label]
        '''

        samples = []
        w = np.mat('1,1')
        b = 10

        for i in range(size):

            rand_x  = [np.float64(np.random.randint(start,end)) for  i in range(0,dimm)]
            if w.dot(np.array(rand_x)) +b  > 0:
                y = 1
            else:
                y = -1
            samples.append([rand_x,y])
        return samples

    def plot_samples(self,samples):
        # 注意,只实现二维平面,默认是样本维度中的第一、二维度展现,标签只能是两类,正负样本。
        for value in samples:
            if value[1] == 1:
                marker = 'D'

            else:
                marker = 'o'

            plt.scatter(value[0][0], value[0][1],marker=marker)
            #print((value[0][0],value[0][1]))
        plt.title('samples')
        plt.savefig('./static/test.png')




