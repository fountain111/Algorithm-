import numpy as np
#from scipy.stats import *


def _switch(base, p='e'):
    return {
        2: np.log2(p),
        'e': np.log(p)

    }[base]

def _entropy(pk, base):
    '''
    if  1 != sum all values that in all pk  ,then should normalize pk,for example,[0.2,0.3],will be 0.2/(0.2+0.3),
    0.3/(0.2+0.3)
    there is many ways to find a solution ,like H =- log(p^p)
    :param pk: probability array_like ,each from 0 to 1
    :return: entropy

    '''
    entropy_sum = 0
    pk = np.array(pk)
    pk = pk/np.sum(pk,axis=0)



    #power = 1
    for p in pk:
        entropy_sum += -p * (_switch(base, p))
        #power *= np.power(p,p)
    #entropy_sum = np.log2(power)
    return entropy_sum

def _cross_entropy(P,Q,base='e'):
    '''
    cross_entropy = H(P)+DKL(P||Q)
    or = plog(q)


    :return:
    '''
    cross_entropy = 0

    for index,p in enumerate(P):
        cross_entropy+=p*_switch(base,Q[index])



    return cross_entropy

def _relative_entropy(P,Q,base='e'):
    '''
    also knowns as the kullbakc-leibler divergence of q from p
    P:array_like
    Q:array_like
    :return:
    '''
    DKL = 0
    for index,p in enumerate(P):
        #print(p*_switch(base,p/(Q[index])))
        DKL+=p*_switch(base,p/(Q[index]))
        #print(DKL)

    return DKL


def _gradient_descent():
    '''
    gradient descent for cross entropy in binary case

    j(tha)  = (h(x) - y )*x
    :return:
    '''


def test():
    print('test in entropy package')
    return



def main():
    pk = [2/5,3/5]
    Q = [i/12 for i in range(1,10)]

    P = [0.333,0.333,0.333]
    Q = [0.36,0.48,0.16]
    #print(entropy(pk,base=2))
    print(_entropy(pk,base=2))
    #print(_relative_entropy(P,Q))

if __name__ == '__main__':
    main()