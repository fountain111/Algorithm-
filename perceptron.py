
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

'''
    Perceptron完成感知机的训练、画出分界面

    Samples完成样本点的生成和绘制。

'''

class Perceptron():
    def __init__(self):
        self.w = np.array([-1.0,10000.0])
        self.b = np.float64(100.0)
        self.lr = 0.001
        self.epoch = 10000
    def train(self,samples):
        x_list= []
        y_list = []
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
                    self.w += self.lr*y*x
                    self.b = self.b + self.lr * y
            x_,y_ = self.super_plane(-300,300)
            print(i)
            x_list.append(x_)
            y_list.append(y_)
        return x_list,y_list


    def poly(self,x,y,p):
        #使用poly核,默认+1,
        #一搬用核的话,很多情况下是用对偶对的

        return ((x.dot(y) + 1) )**p

    def rbf(self,x,y,gamma):

        return

        # perceptron的对偶形式可以凑成kernel出来,这是个很强的技巧
        # 使用rbf核



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

    def plot_superplane_ani(self,x,y,fig,ax):
        #动态展示
        line, = ax.plot([], [], 'k-')

        def init():
            line.set_data([],[])
            return line,
        def animate(i):
            # update the data
            try:
                line.set_xdata(x[i])
                line.set_ydata(y[i])
            except IndexError:
                print('already done')
                return line
            return  line,
        ani = animation.FuncAnimation(
            fig, func=animate,init_func=init,
              interval=10, blit=True, save_count=50)

        plt.show()
        plt.plot(x[-1],y[-1])
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
        x_list= []
        y_list = []
        w = np.mat('1,1')
        b = 10

        for i in range(size):

            rand_x  = [np.float64(np.random.randint(start,end)) for  i in range(0,dimm)]
            y_ =  w.dot(np.array(rand_x))+b
            if y_ > 1:
                y = 1
            elif y_<-1:
                y = -1
            else:
                continue
            samples.append([rand_x,y])
            x_list.append(rand_x)
            y_list.append(y)
        return samples,x_list,y_list

    def plot_samples(self,samples):
        fig, ax = plt.subplots()
        # 注意,只实现二维平面,默认是样本维度中的第一、二维度展现,标签只能是两类,正负样本。
        for value in samples:
            if value[1] == 1:
                marker = 'D'

            else:
                marker = 'o'

            ax.scatter(value[0][0], value[0][1],marker=marker)
            #print((value[0][0],value[0][1]))
        plt.title('samples')
        plt.savefig('./static/test.png')
        return fig,ax




