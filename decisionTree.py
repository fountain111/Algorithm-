from entropy import *
import entropy
class ID3_trees():
    '''
    ID3

    '''
    def __init__(self):
        #self.label = label
        return


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

def main():
    model = ID3_trees()
    label = [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1,1, 0]
    #model._label_entropy(label,base=2)
    array = np.random.random((3,4))
    for value in array.T:
        print(value)
if __name__ == '__main__':
    main()




