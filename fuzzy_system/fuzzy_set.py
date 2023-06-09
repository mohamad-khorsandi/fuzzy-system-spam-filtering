import random
import numpy as np

from fuzzy_system.enums import SimpleTerms
from fuzzy_system.fuzzy_system_config import fuzzyset_init_rate, fuzzyset_init_sigma, distance_from_centers
from fuzzy_system.membership_functions import calculate_sigmoid, calculate_trapezium, calculate_gaussian, \
    calculate_triangular


class FuzzySet:
    def __init__(self, linguistic_term, m, s):
        self._s = s
        self._m = m
        self._membership_function = None
        assert type(linguistic_term) == SimpleTerms
        self._linguistic_term = linguistic_term

    def get_m(self):
        return self._m

    def get_s(self):
        return self._s

    def membership_function(self, x):
        return self._membership_function(x, m=self._m, s=self._s)

    @classmethod
    def create_random(cls, linguistic_term, m, s):
        constructor_function = random.choice(fuzzy_set_constructor_functions)
        return constructor_function(linguistic_term, m, s)

    @classmethod
    def create_triangular(cls, linguistic_term, m, s):
        f_set = FuzzySet(linguistic_term, m, s)
        f_set._membership_function = calculate_triangular
        return f_set

    @classmethod
    def create_gaussian(cls, linguistic_term, m, s):
        f_set = FuzzySet(linguistic_term, m, s)
        f_set._membership_function = calculate_gaussian
        return f_set

    @classmethod
    def create_trapezium(cls, linguistic_term, m, s):
        f_set = FuzzySet(linguistic_term, m, s)
        f_set._membership_function = calculate_trapezium
        return f_set

    @classmethod
    def create_sigmoid(cls, linguistic_term, m, s):
        f_set = FuzzySet(linguistic_term, m, s)
        f_set._membership_function = calculate_sigmoid
        return f_set

    def copy(self):
        fuzzyset = FuzzySet(linguistic_term=self._linguistic_term, m=self._m, s=self._s)
        fuzzyset._membership_function = self._membership_function
        return fuzzyset

    def plot(self, ax, lower_bound, upper_bound):
        x = np.linspace(lower_bound, upper_bound, 100)
        y = []
        for i in x:
            y.append(self.membership_function(i))

        ax.plot(x, y)

    def linguistic_term_is_equal_to(self, linguistic_term):
        return self._linguistic_term == linguistic_term

    @classmethod
    def random_fuzzyset(cls, feature, term, center):
        mean_of_s = (feature.max_value - feature.min_value) / (6 * fuzzyset_init_rate)
        s = random.gauss(mean_of_s, fuzzyset_init_sigma)
        random.gauss(mean_of_s, fuzzyset_init_sigma)
        m = random.gauss(center, distance_from_centers)
        return FuzzySet.create_random(m=m, s=s)


fuzzy_set_constructor_functions = [FuzzySet.create_triangular,
                                   # FuzzySet.create_trapezium,
                                   # FuzzySet.create_sigmoid,
                                   FuzzySet.create_gaussian]
