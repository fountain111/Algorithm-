import numpy as np
import random
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


    list_ = [random.randint(1,9) for i in range(1,10)]



print(list(range(1,100)))


#def merge_sort():
    
