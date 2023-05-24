import numpy as np
# import torch
# import torch.nn as nn


x = np.array([[1000000000, 2.5, 0.67],
              [4.3, 0.78, -2.5],
              [-2.6, 1.56, -876]])
label = np.array([0,0,1])

# loss = nn.CrossEntropyLoss()
# correct_ce = loss(torch.tensor(x), torch.tensor(label))


def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    sum = np.sum(exp_x, axis=-1, keepdims=True)
    return exp_x / sum
print(softmax(x))

def cross_entropy(predictions, targets, epsilon=1e-12):
    predictions = np.clip(predictions, epsilon, 1.-epsilon)
    N = predictions.shape[0]
    ce = - np.sum(targets*np.log(predictions)) / N
    return ce


# def to_onehot(label, n_classes):
#     N = label.shape[0]
#     onehot = np.zeros((N, n_classes))
#     for i in range(N):
#         onehot[i][label[i]] = 1
#     return onehot
#
# # print(to_onehot(label, n_classes=3))
#
# def main():
#     n_classes = x.shape[1]
#     targets = to_onehot(label, n_classes)
#     predictions = softmax(x)
#     ce = cross_entropy(predictions, targets)
#     print("ce:", ce)
#     print("correct:", correct_ce)
#     print(np.isclose(correct_ce.data.item(), ce))
#
#
# if __name__ == '__main__':
#     main()