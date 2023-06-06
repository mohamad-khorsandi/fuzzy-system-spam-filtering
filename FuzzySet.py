import numpy as np


class FuzzySet:
    def __init__(self):
        self.is_not: bool
        self.name: str
        self.s: int
        self.m: int
        self.mem_func: None

    @classmethod
    def create_triangular_fset(cls, name, m, s):
        f_set = FuzzySet(name, m, s)
        f_set.mem_func = f_set.create_triangular
        return f_set

    def complement(self):
        result = FuzzySet(f'not ({self.name})', self.m, self.s)
        return result

    def cog_defuzzify(self):
        num = np.sum(np.multiply(self._dom, self._domain))
        den = np.sum(self._dom)
        print(num)
        print(den)
