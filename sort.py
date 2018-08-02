import numpy as np
import random
def insertion_sort(list_):
    j = 1
    size = len(list_)
    for j in range(1,size):
        key = list_[j]
        i= j -1
        while i>=0:

            if key<list_[i]:
                list_[i+1],list_[i]  = list_[i],key
            i-=1
        j+=1
    return list_


list_ = [random.randint(1,9) for i in range(1,10)]

print(list_)

print(insertion_sort(list_))



def merge_sort():
    
