import math


# print(math.log(100, math.e) - math.log(100, 2))


import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

scores = [1, 3, 2]
print(softmax(scores))