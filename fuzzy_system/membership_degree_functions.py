import numpy as np


def create_triangular(x, m, s):
    res = np.maximum(np.minimum((x - m + s) / s, (m - x + s) / s), 0)
    return res


def create_trapezium(x, m, s):
    res = np.maximum(np.minimum((x - m + s) / s, 1), 0)
    return res


def create_gaussian(x, m, s):
    res = np.exp((-1 / 2) * ((x - m) / s) ** 2)
    return res


def create_sigmoid(x, m, s):
    res = 1 / (1 + np.exp(-(x - m) / s))
    return res
