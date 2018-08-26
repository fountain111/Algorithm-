from flask import Flask
import  pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import io
import base64
from flask import render_template
from flask import make_response
app = Flask(__name__)


@app.route('/test')
def plot():
    x = list(range(1,100))
    print(x)
    y = [ i*2 for i in x]
    print(x,y)
    plt.plot(x,y)
    plt.savefig('./static/test.png')
    return render_template('test_plot.html')


@app.route("/")
def index():
    return "index"
@app.route("/hello")
def hello():
    return 'hello'
@app.route('/user/<username>')
def show_user_profile(username):
    return 'username:{username}'.format(username=username)
