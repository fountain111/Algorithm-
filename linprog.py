
import numpy as np
def pivot(N,B,A,b,c,v,l,e):
    '''

    :param N: None basic 的下标变量
    :param B: Basic 的下标变量
    :param A: A 是约束方程矩阵
    :param b: 等式右边的b
    :param c: 目标函数的系数
    :param v: 目标函数的可选常数项
    :param l: 替出变量的下标,basic ->Non basic
    :param e: 替入变量的下标,Non basic ->basic
    :return:  N_,B_,A_,b_,c_,v_
    '''
    A_ = [[1,2]] #create matrix


    def _pivot(self, mat, B, row, col):
        mat[row] /= mat[row][col]
        ids = np.arange(mat.shape[0]) != row
        mat[ids] -= mat[row] * mat[ids, col:col + 1]  # for each i!= row do: mat[i]= mat[i] - mat[row] * mat[i][col]
        B[row] = col