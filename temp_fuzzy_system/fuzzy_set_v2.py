import numpy as np


class FuzzySet:

    def __init__(self, name, m, s):
        self.name = name
        self.m = m
        self.s = s
        self.min_domain = m - s
        self.max_domain = m + s
        self.domain = np.linspace(self.min_domain, self.max_domain, res)

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

    def min_scalar(self, val):
        result = FuzzySet(f'({self.name}) min ({val})', self.m, self.s)

        return result

    def union(self, f_set):
        result = FuzzySet(f'({self.name}) union ({f_set.name})', self.m, self.s)

        return result

    def intersection(self, f_set):
        result = FuzzySet(f'({self.name}) intersection ({f_set.name})', self.m, self.s)

        return result

    def complement(self):
        result = FuzzySet(f'not ({self.name})', self.m, self.s)
        return result

    def cog_defuzzify(self):
        num = np.sum(np.multiply(self._dom, self._domain))
        den = np.sum(self._dom)
        print(num)
        print(den)
