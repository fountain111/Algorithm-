
import numpy as np
import matplotlib.pyplot as plt

def generate_samples(start,end,size):
    samples = []
    w = np.array([1,1])
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
plot_samples()
def perceptron(samples):
    w = np.array([0.0,0.0])
    b = 1.0
    lr = 0.5
    epoch = 1000
    for i in range(epoch):

        for value in samples:
            x1= value[0][0]
            x2 =value[0][1]
            y = value[1]
            predict = w[0]*x1+w[1]*x2+b
            if predict >0:
                predict = 1
            else:
                predict=-1
            if (y*predict<=0):
                w[0] = w[0] +lr*y*x1
                w[1] = w[1]+lr*y*x2
                b= b + lr*y
                print(w,b)


    return w,b

def generate_line(x_start,x_end,slope,b):

    x_list = []
    y_list = []
    for i in range(1,100):
        x = np.random.randint(x_start,x_end)
        y = x *slope+b
        x_list.append(x)
        y_list.append(y)
    return x_list,y_list

w,b = perceptron(samples)
line_x_y = generate_line(-300,300,-w[0]/w[1],b)
plt.plot(line_x_y[0], line_x_y[1])
plt.savefig('./static/test.png')
