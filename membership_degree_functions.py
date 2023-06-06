import numpy as np


def create_triangular(self, x):
    res = np.maximum(np.minimum((x - self.m) / self.s, (self.m - x) / self.s), 0)
    return res


def create_trapezium(self, x):
    res = np.maximum(np.minimum((x - self.m) / self.s, 1), 0)
    return res


def create_gaussuan(self, x):
    res = np.exp((-1 / 2) * ((x - self.m) / self.s) ^ 2)
    return res


def create_sigmoid(self, x):
    res = 1 / (1 + np.exp(-(x - self.m) / self.s))
    return res
