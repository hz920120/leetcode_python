
import numpy as np

def softmax(x, axis=1):
    # 计算每行的最大值
    row_max = x.max(axis=axis)

    # 每行元素都需要减去对应的最大值，否则求exp(x)会溢出，导致inf情况
    row_max=row_max.reshape(-1, 1)
    x = x - row_max

    # 计算e的指数次幂
    x_exp = np.exp(x)
    x_sum = np.sum(x_exp, axis=axis, keepdims=True)
    s = x_exp / x_sum
    return s

A = [[-1, 3.0, 2.0]]
A= np.array(A)

print(softmax(A))




# 2-D array: 2 x 3
a = np.array([[1, 1, 1, 0, 0], [1, 1, 1, 1, 1],[1, 1, 1, 0, 1],[0, 1, 0, 1, 1],[0, 1, 1, 1, 1]])
# 2-D array: 3 x 2
b = np.array([[0.8, -0.6, 1.1], [0.1, 0.2, 1.2], [-1.2, -1.6, -0.7],[1.8, 0.1, -2.1],[2.1, -0.2, 1.0]])

print(a.dot(b))