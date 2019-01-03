import entropy
import numpy as np

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
                   [0, 1, 'no'],

                   ]

        fea_names = ['fea1', 'fea2']


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
            #print('split done,return label=',unique_labels[0])
            return unique_labels[0]

        if dataSet.shape[1] == 1:
            print('stop return2 dataSet shape=1',)
            return self.majorityCnt(dataSet)
        #print(dataSet.shape)
        best_fea_index = self.chooseBestFeatureToSplit(dataSet)
        #best_fea_index = self.chooseBestFeatureToSplit_condition_entropy(dataSet)
        best_fea_name = fea_names[best_fea_index]
        #print('best fea=',best_fea_index)
        #print('before',fea_names)
       # print('after',fea_names)

        bestValues =dataSet[:,best_fea_index]
        #print('bestValues',best_fea_index)
        tree = {best_fea_name:{}}
        del fea_names[best_fea_index]
        #print('best fea name=',best_fea_name)  # best fea index 可能一直是0,但name会变。
        for value in np.unique(bestValues):
            #sub_fea_names = fea_names[:]
            sub_dataSet = self.splitDataSet(dataSet,best_fea_index,value)
         #   print('value=',value)
          #  print(sub_dataSet.shape)
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




    def chooseBestFeatureToSplit_condition_entropy(self,dataSet):
        '''
        Traversal all fea,find best information Gain
        :param dataSet:array_like,list
        :return: best fea index
        '''

        dataSet = np.asarray(dataSet)
        best_informationGain = 100000000
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
            information_gain = condition_entropy
            #print(information_gain)
            if best_informationGain > information_gain:
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
        if isinstance(indices,list):
            print('majority euqal ,random pick ')
            indices = indices[0]

        label = values[indices]

        print('marjority vote=',label)



        return label

    def fit(self,dataSet,fea_names):


        return self.createTrees(dataSet,fea_names)


    def _predict_example(self,trees,fea_names,test_row):
        '''
        predict a single example(row)

        :param trees:dict,
        :param fea_names:
        :param test_data: array_like
        :return: label of class
        '''
        #test_row = list(test_row)
       # print(test_row)

        first_key = list(trees.keys())[0]

        next_tree = trees[first_key]  # next tree or label

        fea_index = fea_names.index(first_key)
        #print(fea_index)
        #print(test_row)
        key = test_row[fea_index]

        valueInRow = next_tree[key]

        if isinstance(valueInRow,dict):
            class_label = self._predict_example(valueInRow,fea_names,test_row)
        else:
            class_label = valueInRow
        #print(class_label)
        return class_label


    def predict(self,trees,fea_names,test_data):
        '''


        :param trees:
        :param fea_names:
        :param test_data: array_like
        :return:
        '''

        test_data = np.asarray(test_data)
        try:
            test_data.shape[1]
        except IndexError:
            test_data = test_data.reshape(1,test_data.shape[0])
            print('reshape data',test_data)
            pass
        labels = list(map(lambda x: self._predict_example(trees, fea_names, x), test_data))
        #print(labels)
        return labels

def main():
    model = ID3_trees()
    #label = [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1,1, 0]
    #model._label_entropy(label,base=2)
    array = np.random.random((3,4))
   # for value in array.T:
    #    print(value)

    dataset,fea_names = model._create_dataSets()
    trees = model.fit(dataset,fea_names.copy())
    #calcShannonEnt(dataset)
    #splitDataSet(dataset,1,'e')
    #print('fea names',fea_names)
    #print('a',fea_names.index('no surfacing'))
    #print(dataset[0])
    labels = model.predict(trees,fea_names,np.asarray(dataset)[:,:-1])
    print(labels)

if __name__ == '__main__':
    main()







