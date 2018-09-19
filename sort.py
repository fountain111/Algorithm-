import numpy as np
from flask import Flask
import  pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from flask import render_template
import sys
from flask import make_response
import math
app = Flask(__name__)
plt.switch_backend('agg') # solve main loop
class Sort():
    def insertion_sort(self,list_):
        j = 1
        size = len(list_)
        for j in range(1,size):
            key = list_[j]
            i= j -1
            while i>=0 and key<list_[i]:
                list_[i+1]  = list_[i]
                i-=1
            list_[i + 1] = key
            j+=1
        return list_


def simple_smo(dataset, labels, C, max_iter):
    ''' 简化版SMO算法实现，未使用启发式方法对alpha对进行选择.
    :param dataset: 所有特征数据向量
    :param labels: 所有的数据标签
    :param C: 软间隔常数, 0 <= alpha_i <= C
    :param max_iter: 外层循环最大迭代次数
    '''
    dataset = np.array(dataset)
    m, n = dataset.shape
    labels = np.array(labels)
    # 初始化参数
    alphas = np.zeros(m)
    b = 0
    it = 0

    def f(x):
        "SVM分类器函数 y = w^Tx + b"
        # Kernel function vector.
        x = np.matrix(x).T
        data = np.matrix(dataset)
        ks = data * x
        # Predictive value.
        wx = np.matrix(alphas * labels) * ks
        fx = wx + b
        return fx[0, 0]

    while it < max_iter:
        pair_changed = 0
        for i in range(m):
            a_i, x_i, y_i = alphas[i], dataset[i], labels[i]
            fx_i = f(x_i)
            E_i = fx_i - y_i
            j = select_j(i, m)
            a_j, x_j, y_j = alphas[j], dataset[j], labels[j]
            fx_j = f(x_j)
            E_j = fx_j - y_j
            K_ii, K_jj, K_ij = np.dot(x_i, x_i), np.dot(x_j, x_j), np.dot(x_i, x_j)
            eta = K_ii + K_jj - 2 * K_ij
            if eta <= 0:
                print('WARNING  eta <= 0')
                continue
            # 获取更新的alpha对
            a_i_old, a_j_old = a_i, a_j
            a_j_new = a_j_old + y_j * (E_i - E_j) / eta
            # 对alpha进行修剪
            if y_i != y_j:
                L = max(0, a_j_old - a_i_old)
                H = min(C, C + a_j_old - a_i_old)
            else:
                L = max(0, a_i_old + a_j_old - C)
                H = min(C, a_j_old + a_i_old)
            a_j_new = clip(a_j_new, L, H)
            a_i_new = a_i_old + y_i * y_j * (a_j_old - a_j_new)
            if abs(a_j_new - a_j_old) < 0.00001:
                # print('WARNING   alpha_j not moving enough')
                continue
            alphas[i], alphas[j] = a_i_new, a_j_new
            # 更新阈值b
            b_i = -E_i - y_i * K_ii * (a_i_new - a_i_old) - y_j * K_ij * (a_j_new - a_j_old) + b
            b_j = -E_j - y_i * K_ij * (a_i_new - a_i_old) - y_j * K_jj * (a_j_new - a_j_old) + b
            if 0 < a_i_new < C:
                b = b_i
            elif 0 < a_j_new < C:
                b = b_j
            else:
                b = (b_i + b_j) / 2
            pair_changed += 1
            print('INFO   iteration:{}  i:{}  pair_changed:{}'.format(it, i, pair_changed))
        if pair_changed == 0:
            it += 1
        else:
            it = 0
        print('iteration number: {}'.format(it))
    return alphas, b


import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def qd_function(start,stop,step):
    x_y_list = [np.arange(start=start,stop=stop,step=step) for i in range(2)]
    X,Y= np.meshgrid(x_y_list[0], x_y_list[1])
    Z1 = -(X ** 2)
    Z2 = -(Y ** 2)
    Z = 1.0 * (Z1 + 3 * Z2 + 2 * X * Y) + 6.0
    return X,Y,Z

def coordinate_ascent(iters,init_coor):
    x1 = []
    x2 = []
    x1.append(init_coor)
    x2.append(init_coor)
    j = 1
    for i in range(iters):
        #fix x2 ,update x1
        x1_tmp = x2[j-1]
        x1.append(x1_tmp)
        x2.append(x2[j-1])

        j = j+1 #数组上升
        # fix x1 ,update x2
        x2_tmp = x1[j-1]/3
        x1.append(x1[j-1])
        x2.append(x2_tmp)
        j=j+1

    return x1,x2

a = []*100
a[12]=1
print(len(a))

plt.figure()
X,Y,Z=qd_function(-3,3,0.025)

CS = plt.contour(X, Y, Z)

a,b = coordinate_ascent(10000,1.5)

Z1 = a.pop()**2
print(Z1)
Z2 = b.pop()**2
print(Z2)
Z = 1.0 * (Z1 + 3 * Z2 + 2 * 0 * 0) + 6.0

print('max=',Z)
plt.plot(a,b)

plt.title('Coordinate Ascent')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
plt.savefig('./static/n.png')


#gradL = [sp.diff(L,c) for c in [x,y]] +[g]
#print(gradL)

# 解的情况分两种
# 1 内部解,interior solution ,u=0,g(x)<0,约束是inactivate的
# 2 边界解,boundary solution ,u>=0,约束是activate,
# 先求出b和u的关系,再根据b的情况,分别解出关于w1,w2关于b的解,

'''
如果是内部解的话,u1,u2,u3都等于0,g(x)都是小于0的,约束是inactive的,
这时候不等式约束无效,
solutio : w1=0,w2=0,

边界解,u=0
'''

'''
使用拉格朗日对偶求解,

对原问题的拉个朗日函数求解,如果不违反任何约束,对拉个朗日函数求极大就会回到原问题f,如果违反约束则拉格朗日函数的值
会变成无穷大。所以对原问题最小化就是对拉个朗日函数的求极大,然后再求极小,具体参考cs229 svm章节,
先对拉个拉个朗日函数a,b求极大,然后对w求极小(MIN MAX),对偶问题就是先对 w求极小,再对a,b求极大(MAX MIN)

'''


'''
对拉个朗日函数 w求偏导,w是矢量,每个w对应一个等式w=sum(ayx)
'''




