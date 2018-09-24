from flask import Flask
import matplotlib.pyplot as plt
import numpy as np
from flask import render_template
from scipy.linalg import solve
app = Flask(__name__)
plt.switch_backend('agg') # solve main loop
import sympy as sp



def dual(y,total_samples):
    #min dual 的形式，
    a = []*total_samples
    for  i in range(total_samples):
        for j in range(total_samples):
            a[i]*a[j]*


def generate_point(start,end):

    rand_x_y  = [np.random.randint(start,end) for  i in range(1,3)]

    return rand_x_y

def generate_line(x_start,x_end,slope,b):

    x_list = []
    y_list = []
    for i in range(1,100):
        x = np.random.randint(x_start,x_end)
        y = x *slope+b
        x_list.append(x)
        y_list.append(y)
    return x_list,y_list

def dual(y,size):
    ## 无松弛情况下的对偶的最终形式
    a = []
    for i in size:
        for j in size:
            pass
        pass
    return



def plot_margins(margin_name):
    normal_vector = [-2, 1]
    slope = -normal_vector[0]
    b = 0
    normal_length = 0
    for value in normal_vector:
        normal_length += value*value
    normal_unit_vector = np.array(normal_vector)/normal_length

    line_x_y = generate_line(-200,200,slope,b)

    for i in range(1, 5):
        rand_x_y = generate_point(-300,300)

        if margin_name == 'functional_margins':
            margin = np.dot(normal_vector,np.array(rand_x_y).T)+b


        elif margin_name == 'geometric_margins':
            margin = np.dot(normal_unit_vector ,np.array(rand_x_y).T) + b/ normal_length
        if margin >0:
            marker = 'D'
        else:
            marker = 'o'
        plt.scatter(x=rand_x_y[0],y=rand_x_y[1], marker=marker)

        if margin > 0:
            class_ = 'positive'
            margin *= 1
        else:
            class_ = 'negative'
            margin *= -1

        plt.annotate('fun_r={margin}'.format(margin=margin), rand_x_y)
        print('{class_},{margin_name}:{value}'.format(margin_name=margin_name,
                                             value=margin,class_=class_))
    plt.plot(line_x_y[0],line_x_y[1])

    plt.title(margin_name)
    plt.savefig('./static/{fun_name}.png'.format(fun_name=margin_name))
    plt.savefig('./static/test.png')
    plt.clf()
    return 0





@app.route('/functional_margins')
def functional_margin():
    plot_margins('functional_margins')
    return render_template('test_plot.html')

@app.route('/geometric_margins')
def gemotric_margins():
    plot_margins('geometric_margins')
    return render_template('test_plot.html')

