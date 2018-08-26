from flask import Flask
import  pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import io
import base64
from flask import render_template
import sys
from flask import make_response
app = Flask(__name__)

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
        rand_x = np.random.randint(1, 10)
        functional_margin = np.random.randint(-100, 100)
        rand_y = rand_x*slope+functional_margin+b
        if rand_y > b:
            mark = 'D'
        else:
            mark = 'o'

        plt.scatter(rand_x, rand_y, marker=mark)
        if functional_margin >0:
            functional_margin *=1
        else:
            functional_margin *=-1
        plt.annotate('fun_r={margin}'.format(margin=functional_margin),[rand_x,rand_y])
    plt.title(fun_name+'_no_sclar')
    plt.savefig('./static/{fun_name}.png'.format(fun_name=fun_name))
    plt.savefig('./static/test.png')
    plt.clf()
    return render_template('test_plot.html')

@app.route('/geometry_margins')
def ge