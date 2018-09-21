from perceptron import *




perceptron = Perceptron()

samples = Sammples()

g_samples = samples.generate_samples(-300,300,50)

perceptron.train(g_samples)

samples.plot_samples(g_samples)

perceptron.plot_superplane()