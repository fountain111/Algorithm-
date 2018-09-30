from sklearn import datasets
from perceptron import *
iris = datasets.load_iris()
digits = datasets.load_digits()
#print(type(digits.target))
x = digits.data
y = digits.target
perceptron = Perceptron()

perceptron.fit(x,y)