import random

from matplotlib import pyplot as plt

from fuzzy_system.enums import Features, SimpleTerms, SignedTerms
from fuzzy_system.fuzzy_set import FuzzySet
from fuzzy_system.fuzzy_system_config import fuzzyset_init_sigma, fuzzyset_init_rate, distance_from_centers
from preprocess_utils import get_data


class LinguisticVariable:
    def __init__(self, corresponding_feature):
        self.corresponding_feature = corresponding_feature
        self._linguistic_terms: list[SignedTerms]
        self._linguistic_terms = list()
        self._fuzzy_sets = list()

    def get_random_m(self, s):
        return random.uniform(self.corresponding_feature.min_value + s, self.corresponding_feature.max_value - s)

    @classmethod
    def random_linguistic_variable(cls, feature: Features):
        linguistic_variable = LinguisticVariable(feature)

        tmp = (feature.max_value - feature.min_value) / 6
        centers = [tmp, 3*tmp, 5*tmp]
        for i, cen in enumerate(centers):
            term = list(SimpleTerms)[i]
            fuzzyset = FuzzySet.random_fuzzyset(feature=feature, term=term, center=cen)
            linguistic_variable._fuzzy_sets.append(fuzzyset)

        linguistic_variable._linguistic_terms = random.sample(list(SignedTerms), k=random.randint(3, 5))
        return linguistic_variable

    def get_one_of_terms(self):
        return random.choice(self._linguistic_terms)

    def copy(self):
        var = LinguisticVariable(self.corresponding_feature)
        for term in self._linguistic_terms:
            assert type(term) == SignedTerms
            var._linguistic_terms.append(term)

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
