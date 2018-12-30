from entropy import *
import entropy

import math
class ID3_trees():
    '''
    ID3

    '''
    def __init__(self):
        #self.label = label
        return

    def createTrees(self,dataSet,fea_name_list):
        '''
        return tress or label value,

        :param dataSet:
        :param fea_name_list:
        :return:
        '''
        class_list =
            return

        tree = {best_fea_name,{}}

        tree = createTree(dataSet,fea_name_list)

        return tree


    def _label_entropy(self,label,base=2):
        '''
        binary

        :param label: only support binary for now
        :return:
        '''
        total_len = len(label)
        positives = 0
        negatives = 0
        for value in label:
            if value == 1:
                positives+=1
            else:
                negatives+=1

        p_postive = positives/total_len
        p_negative = negatives/total_len
        entropy_label =entropy._entropy([p_postive,p_negative],base)
        print(entropy_label)
        print(positives,negatives,total_len)
        return  entropy_label

    def _ig(self):
        '''
        information gain,

        IG = H(T) - H(T/a)
        :return:
        '''


    def _condition_entropy(self):
        '''
        calculate condition entropy H(Y|X)


        :return:
        '''


    def _fit(self,array,label):
        ''''
        array:fea array

        '''

        for col in array:
            #every fea in fea_list,
            #cal ig for every fea,
            #find label in every fea
            print()
        return

def createDataSet():
    dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    dataSet = np.random.random_integers(1,10,(4,5)).tolist()
    print(dataSet)
    fea_list = ['no sufacing', 'flippers','ok','nook','r1']
    return dataSet, fea_list

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts.setdefault(currentLabel, 0)
        labelCounts[currentLabel] += 1
    #print(labelCounts)

    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt += prob * math.log2(1 / prob)
    return shannonEnt


def splitDataSet(dataSet, axis, value):
    #对一条条数据遍历，找到某条数据记录是否含有某个值（axis位置的value）
    #如果找到，就跳过这个值，重新拼装一条记录，最后把所有记录放在新的list里。
    retDataSet = []
    for featVec in dataSet:
        print(featVec)
        print(featVec[axis])
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet  #返回不含划分特征的子集

def chooseBestFeatureToSplit(dataSet):
    numFeature = len(dataSet[0]) - 1
    #print(numFeature)
    baseEntropy = calcShannonEnt(dataSet)
    bestInforGain = 0
    bestFeature = -1

    for i in range(numFeature):
        featList = [number[i] for number in dataSet] #得到某个特征下所有值
        uniqualVals = set(featList) #set无重复的属性特征值
        newEntrogy = 0

        #求和
        for value in uniqualVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet)) #即p(t)
            newEntrogy += prob * calcShannonEnt(subDataSet) #对各子集求香农墒

        infoGain = baseEntropy - newEntrogy #计算信息增益

        print(infoGain)

        # 最大信息增益
        if infoGain > bestInforGain:
            bestInforGain = infoGain
            bestFeature = i
    return bestFeature

def createTree(dataSet, fea_name_list):
    classList = [example[-1] for example in dataSet] #dataset的最后一个特征，一列
    # print(dataSet)
    # print(classList)
    # 类别相同，停止划分
    if classList.count(classList[0]) == len(classList):
        return classList[0]

    # 判断是否遍历完所有的特征,是，返回个数最多的类别
    #if len(dataSet[0]) == 1:
     #   return majorityCnt(classList)

    #按照信息增益最高选择分类特征属性
    bestFeat = chooseBestFeatureToSplit(dataSet) #分类编号
    bestFeatLabel = fea_name_list[bestFeat]  #该特征的name
    myTree = {bestFeatLabel: {}}
    del (fea_name_list[bestFeat]) #移除该label

    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = fea_name_list[:]  #子集合
        #构建数据的子集合，并进行递归
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree






def main():
    model = ID3_trees()
    label = [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1,1, 0]
    #model._label_entropy(label,base=2)
    array = np.random.random((3,4))
   # for value in array.T:
    #    print(value)

    dataset,labels = createDataSet()
    #calcShannonEnt(dataset)
    #splitDataSet(dataset,1,'e')
    tress = createTree(dataset,labels)
if __name__ == '__main__':
    main()







