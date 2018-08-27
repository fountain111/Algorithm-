from flask import Flask
import  pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from flask import render_template
import sys
from flask import make_response
import math
app = Flask(__name__)

def generate_point(slope,b):
    rand_x = np.random.randint(1, 10)
    functional_margin = np.random.randint(-100, 100)
    rand_y = rand_x * slope + functional_margin + b
    if rand_y > b:
        mark = 'D'
    else:
        mark = 'o'

    return rand_x,rand_y,{'mark':mark},functional_margin

@app.route('/functional_margins')
def functional_margin():
    fun_name = sys._getframe().f_code.co_name

    x = np.array(range(1, 10))
    slope = 2
    b = 0
    y = x*(slope)+b
    normal_vector = [2,-1]
    plt.plot(x, y)
    for i in range(1,10):
        rand_x,rand_y,mark,functional_margin = generate_point(slope,b)
        plt.scatter(rand_x, rand_y, marker=mark.mark)

        if functional_margin > 0:
            functional_margin *= 1
        else:
            functional_margin *= -1
        plt.annotate('fun_r={margin}'.format(margin=functional_margin), [rand_x, rand_y])

    plt.title(fun_name+'_no_sclar')
    plt.savefig('./static/{fun_name}.png'.format(fun_name=fun_name))
    plt.savefig('./static/test.png')
    plt.clf()
    return render_template('test_plot.html')

@app.route('/geometric_margins')
def gemotric_margins():
    fun_name = sys._getframe().f_code.co_name
    b = 5
    normal_vector = [2,-1]
    normal_length = 0
    for value in normal_vector:
        normal_length += math.sqrt(value)
    unit_vector = normal_vector/normal_length
    for i in range(1,10):
        x,y,functional_margin,mark = generate_point(normal_vector[0],b)
        gemotric_margins = np.array(normal_vector/unit_vector).transpose()*x +b/unit_vector
        if gemotric_margins > 0:
            gemotric_margins *= 1
        else:
            gemotric_margins *= -1
        plt.annotate('fun_r={margin}'.format(margin=gemotric_margins), [x, y])
        plt.title(fun_name)
        plt.savefig('./static/{fun_name}.png'.format(fun_name=fun_name))
        plt.savefig('./static/test.png')
        plt.clf()
    return render_template('test_plot.html')
