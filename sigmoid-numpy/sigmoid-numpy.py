import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.asarray(x, dtype=float)   # handles scalar, list, array
    return 1 / (1 + np.exp(-x))