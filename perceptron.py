
import numpy as np
import matplotlib.pyplot as plt

def generate_samples(start,end,size):
    samples = []
    w = np.array([2,2])
    b = 3

    for i in range(size):

        rand_x  = [np.float64(np.random.randint(start,end)) for  i in range(1,3)]
        if w.dot(np.array(rand_x)) +b  > 0:
            y = 1
        else:
            y = -1
        samples.append([rand_x,y])
    return samples

# w=<2,2> b = 3
samples = generate_samples(-300,300,100)
print(samples)

def plot_samples():
    for value in samples:
        if value[1] == 1:
            marker = 'D'

        else:
            marker = 'o'

        plt.scatter(value[0][0], value[0][1],marker=marker)
        print((value[0][0],value[0][1]))

    plt.title('samples')
    plt.savefig('./static/test.png')

def perceptron(samples):
    w = np.array([1.0,2.0])
    b = 1.0
    lr = 0.1



    for value in samples:
        x= value[0]
        y = value[1]

        if (y*(w.dot(x)+b)<=0):
            w+=lr*np.array(x)
            b+=lr
            print(w,b)

    return w,b
print(perceptron(samples))

