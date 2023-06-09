import random

from matplotlib import pyplot as plt

from fuzzy_system.enums import Features, SimpleTerms, SignedTerms
from fuzzy_system.fuzzy_set import FuzzySet


class LinguisticVariable:
    def __init__(self, corresponding_feature):
        self.corresponding_feature = corresponding_feature
        self._fuzzy_sets = list()

    def get_random_m(self, s):
        return random.uniform(self.corresponding_feature.min_value + s, self.corresponding_feature.max_value - s)

    @classmethod
    def random_linguistic_variable(cls, feature: Features):
        linguistic_variable = LinguisticVariable(feature)

        unit = (feature.max_value - feature.min_value) / 6
        for counter, i in enumerate([1, 3, 5]):
            term = list(SimpleTerms)[counter]
            l_bound = (i - 1) * unit
            cen = i * unit
            u_bound = (i + 1) * unit
            fuzzyset = FuzzySet.random_fuzzyset(term=term, l_bound=l_bound, center=cen, u_bound=u_bound)
            linguistic_variable._fuzzy_sets.append(fuzzyset)

        return linguistic_variable

    @classmethod
    def get_random_signed_term(cls):
        return random.choice(list(SignedTerms))

    def copy(self):
        var = LinguisticVariable(self.corresponding_feature)

        for f_set in self._fuzzy_sets:
            var._fuzzy_sets.append(f_set)

        return var

    def plot(self):
        fig, ax = plt.subplots()
        for f_set in self._fuzzy_sets:
            f_set.plot(ax, self.corresponding_feature.min_value, self.corresponding_feature.max_value)
        plt.show()

    def mem_func_of_given_term(self, linguistic_term, x):
        for fset in self._fuzzy_sets:
            if fset.linguistic_term_is_equal_to(linguistic_term):
                return fset.membership_function(x)

        raise Exception()

    def mut(self):
        var = LinguisticVariable(self.corresponding_feature)
        for f_set in self._fuzzy_sets:
            var._fuzzy_sets.append(f_set.mut())
        return var
