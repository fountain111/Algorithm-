from entropy import *
import entropy
import numpy as np
import math

class ID3_trees():
    '''
    ID3

    '''
    def __init__(self):
        #self.label = label
        return

    def _create_dataSets(self):
        dataSet = [[1, 1, 'yes'],
                   [1, 1, 'yes'],
                   [1, 0, 'no'],
                   [0, 1, 'no'],
                   [0, 1, 'no']]
        fea_names = ['no surfacing', 'flippers']
        return dataSet, fea_names

    def createTrees(self,dataSet,fea_names):
        '''
        return tress or label value,

        :param dataSet:
        :param fea_name_list:
        :return:
        '''
        dataSet = np.asarray(dataSet)
        #print(dataSet[:,2])

        labels = dataSet[:,-1]
        unique_labels,counts = np.unique(labels,return_counts=True)
        if len(labels) == counts[0]:
            print('split done,return label=',unique_labels[0])
            return unique_labels[0]

        if dataSet.shape[1] == 1:
            print('stop return2 dataSet shape=1',)
            return self.majorityCnt(dataSet)
        #print(dataSet.shape)
        best_fea_index = self.chooseBestFeatureToSplit(dataSet)
        best_fea_name = fea_names[best_fea_index]
        print('best fea=',best_fea_index)
        #print('before',fea_names)
       # print('after',fea_names)

        bestValues =dataSet[:,best_fea_index]
        #print('bestValues',best_fea_index)
        tree = {best_fea_name:{}}
        del fea_names[best_fea_index]
        print('best fea name=',best_fea_name)  # best fea index 可能一直是0,但name会变。
        for value in np.unique(bestValues):
            #sub_fea_names = fea_names[:]
            sub_dataSet = self.splitDataSet(dataSet,best_fea_index,value)
            print('value=',value)
            print(sub_dataSet.shape)
            tree[best_fea_name][value] = self.createTrees(sub_dataSet,fea_names)

        return tree


    def splitDataSet(self,dataSet,index,value):
        '''


        :param dataSet:
        :param index:
        :param value:
        :return:  index是value的其他列的值，并删除Index列
        '''
        new_list = []
        for row in dataSet:
            if (row[index] == value):
             new_list.append(row)
        new_array = np.asarray(new_list)
        return np.delete(new_array,index,axis=1)



    def chooseBestFeatureToSplit(self,dataSet):
        '''
        Traversal all fea,find best information Gain
        :param dataSet:array_like,list
        :return: best fea index
        '''

        dataSet = np.asarray(dataSet)
        best_informationGain = 0
        best_index = None
        baseEntropy = self.calcEntropy(dataSet)
        #print('base entropy=',baseEntropy)
        fea_lens = dataSet.shape[1]-1
        for i in range(fea_lens):
            unique_feas = np.unique(dataSet[:,i])
            condition_entropy = 0
            #print('unique_feas=',unique_feas)
            for value in unique_feas:
                sub_dataSet = self.splitDataSet(dataSet,i,value)
              #  print('sub_dataSet shape =',sub_dataSet.shape)
                prob = sub_dataSet.shape[0]/dataSet.shape[0]  # 随机变量P（X）的概率
                condition_entropy += prob*self.calcEntropy(sub_dataSet)   # 条件熵概率
             #   print('condition entropy=',condition_entropy)
            information_gain = baseEntropy - condition_entropy
            #print(information_gain)
            if best_informationGain < information_gain:
                best_informationGain  = information_gain
                best_index = i
        return best_index

    def calcEntropy(self,dataSet):
        '''
        其实没必要带整个数据集进去，
        labels的信息熵
        :param dataSet:
        :return: entropy
        '''

        dataSet = np.asarray(dataSet)
        labels = dataSet[:,-1]
        _,counts = np.unique(labels,return_counts=True)
        #print(list(map(lambda x:x/dataSet.shape[0],counts)))

        return_entropy = entropy._entropy(list(map( lambda x:x/dataSet.shape[0],counts)),base=2)
        #print(return_entropy)
        return return_entropy


    def majorityCnt(self,dataSet):
        '''
        majority wins, if equal ,random choose,print warning,

        :param dataSet:
        :return:
        '''

        values,counts = np.unique(dataSet[:,-1],return_counts=True)

        indices = np.argmax(counts)
        if len(indices>1):
            print('majority euqal ,random pick ')
            indices = indices[0]

        label = values[indices]

        print('marjority vote=',label)



        return label


def main():
    model = ID3_trees()
    label = [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1,1, 0]
    #model._label_entropy(label,base=2)
    array = np.random.random((3,4))
   # for value in array.T:
    #    print(value)

    dataset,fea_names = model._create_dataSets()
    trees = model.createTrees(dataset,fea_names)
    #calcShannonEnt(dataset)
    #splitDataSet(dataset,1,'e')
    print(trees)
if __name__ == '__main__':
    main()







