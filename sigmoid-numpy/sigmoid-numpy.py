import numpy as np

def sigmoid(x):
    x = np.array(x)
    y = 1/(1+np.exp(-x))
    return y