import numpy as np

def reshape_matrix(a, new_shape):
    a = np.array(a)

    if np.prod(a.shape) != np.prod(new_shape):
        return []

    return a.reshape(new_shape).tolist()