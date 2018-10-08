
#Author:
# License: BSD 3 clause
import numpy as np
import matplotlib.pyplot as plt

class Sammples():
    """


    """
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




