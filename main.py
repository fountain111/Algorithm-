from perceptron import *

from linearsvm import *

from samples import *

perceptron = Perceptron()
linearsvm = LinearSvm()

s = Sammples()

samples,x,y = s.generate_samples(-300,300,100)


fig,ax = s.plot_samples(samples)

x,y = perceptron.train(samples)

perceptron.plot_superplane_ani(x,y,fig,ax)



#x,y = linearsvm.train([x,y])
#linearsvm.plot_superplane_ani(x,y,fig,ax)


