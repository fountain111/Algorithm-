import numpy as np
from scipy.stats import *

def _entropy(p_list,base):
    '''

    :param p_list: probability list ,each from 0 to 1
    :return: entropy

    '''
    entropy_sum = 0

    def switch(base, p='e'):
        return {
             2: np.log2(p),
            'e': np.log(p)

        }[base]
    for p in p_list:
        entropy_sum += -p * (switch(base, p))

    return entropy_sum


print(entropy([1/3,2/3],base=2))
print(_entropy([1/3,2/3],base=2))