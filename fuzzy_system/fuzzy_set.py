import numpy as np
from fuzzy_system.membership_degree_functions import create_sigmoid, create_trapezium, create_gaussian, create_triangular


class FuzzySet:
    def __init__(self, is_not, m, s):
        self._is_not = is_not
        self._s = s
        self._m = m
        self._mem_func = None

    def get_m(self):
        return self._m

    def get_s(self):
        return self._s

    def calculate_mem_degree(self, x):
        return self._mem_func(x)

    @classmethod
    def get_triangular(cls, is_not, m, s):
        f_set = FuzzySet(is_not, m, s)
        f_set.mem_func = create_triangular
        return f_set

    @classmethod
    def get_gaussian(cls, is_not, m, s):
        f_set = FuzzySet(is_not, m, s)
        f_set.mem_func = create_gaussian
        return f_set

    @classmethod
    def get_trapezium(cls, is_not, m, s):
        f_set = FuzzySet(is_not, m, s)
        f_set.mem_func = create_trapezium
        return f_set

    @classmethod
    def get_sigmoid(cls, is_not, m, s):
        f_set = FuzzySet(is_not, m, s)
        f_set.mem_func = create_sigmoid
        return f_set

    # def cog_defuzzify(self):
    #     num = np.sum(np.multiply(self._dom, self._domain))
    #     den = np.sum(self._dom)
    #     print(num)
    #     print(den)


fuzzy_set_constructor_functions = [FuzzySet.get_triangular, FuzzySet.get_trapezium, FuzzySet.get_sigmoid,
                                   FuzzySet.get_gaussian]
