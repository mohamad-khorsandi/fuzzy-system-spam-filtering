import random
import numpy as np
from fuzzy_system.membership_functions import calculate_sigmoid, calculate_trapezium, calculate_gaussian, \
    calculate_triangular


class FuzzySet:
    def __init__(self, name, m, s):
        self._s = s
        self._m = m
        self._membership_function = None
        self.name = name

    def get_m(self):
        return self._m

    def get_s(self):
        return self._s

    def membership_function(self, x):
        return self._membership_function(x, m=self._m, s=self._s)

    @classmethod
    def create_random(cls, name, m, s):
        constructor_function = random.choice(fuzzy_set_constructor_functions)
        return constructor_function(name, m, s)

    @classmethod
    def create_triangular(cls, name, m, s):
        f_set = FuzzySet(name, m, s)
        f_set._membership_function = calculate_triangular
        return f_set

    @classmethod
    def create_gaussian(cls, name, m, s):
        f_set = FuzzySet(name, m, s)
        f_set._membership_function = calculate_gaussian
        return f_set

    @classmethod
    def create_trapezium(cls, name, m, s):
        f_set = FuzzySet(name, m, s)
        f_set._membership_function = calculate_trapezium
        return f_set

    @classmethod
    def create_sigmoid(cls, name, m, s):
        f_set = FuzzySet(name, m, s)
        f_set._membership_function = calculate_sigmoid
        return f_set

    def copy(self):
        fuzzyset = FuzzySet(m=self._m, s=self._s)
        fuzzyset._membership_function = self._membership_function
        return fuzzyset

    def plot(self, ax, lower_bound, upper_bound):
        x = np.linspace(lower_bound, upper_bound)
        y = []
        for i in x:
            y.append(self.membership_function(i))

        ax.plot(x, y)


fuzzy_set_constructor_functions = [FuzzySet.create_triangular,
                                   FuzzySet.create_trapezium,
                                   FuzzySet.create_sigmoid,
                                   FuzzySet.create_gaussian]
