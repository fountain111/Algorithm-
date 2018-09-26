from perceptron import *

from linearsvm import *


perceptron = Perceptron()
s = Sammples()

samples,x,y = s.generate_samples(-300,300,50)


fig,ax = s.plot_samples(samples)

x,y = perceptron.train(samples)

perceptron.plot_superplane_ani(x,y,fig,ax)

#liner = LinearSvm()
#liner.train(samples)
#liner.plot_superplane()
import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

