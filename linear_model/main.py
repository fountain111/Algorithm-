from sklearn import datasets
from perceptron import *

#from linear_model.stochastic_gradient import *
cancer = datasets.load_breast_cancer()
digits = datasets.load_digits()
#print(type(digits.target))
x = cancer.data
y = cancer.target

for i,value in enumerate(y):
    if value ==0:
        y[i]=-1
#perceptron = Perceptron()

perceptron = Perceptron()
perceptron.fit(x,y,epoch=100000,lr=0.1)

print("准确率：{:8.6} %".format((perceptron.predict(x) == y).mean() * 100))

