import numpy as np

FUNC = "sqrt(1+x^2) + exp(-2x)"


def function(x):
    #return x**2 + np.cos(x) - x
    return np.sqrt(1+x**2) + np.exp(-2*x)