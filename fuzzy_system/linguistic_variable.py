import random

from matplotlib import pyplot as plt

from fuzzy_system.enums import Features
from fuzzy_system.fuzzy_set import FuzzySet
from fuzzy_system.fuzzy_system_config import fuzzyset_init_sigma, fuzzyset_init_rate


class LinguisticVariable:
    def __init__(self, corresponding_feature):
        self.corresponding_feature = corresponding_feature
        self._linguistic_terms = list()

    def add_linguistic_term(self, fuzzyset: FuzzySet):
        lower_bound = self.corresponding_feature.min_value + fuzzyset.get_s()
        upper_bound = self.corresponding_feature.max_value - fuzzyset.get_s()
        assert  lower_bound < fuzzyset.get_m() < upper_bound
        self._linguistic_terms.append(fuzzyset)

    def get_random_m(self, s):
        return random.uniform(self.corresponding_feature.min_value + s, self.corresponding_feature.max_value - s)

    @classmethod
    def random_linguistic_variable(cls, feature: Features):
        fuzzy_var = LinguisticVariable(feature)
        linguistic_term_count = random.randint(1, 5)

        for i in range(linguistic_term_count):
            mean_of_s = (feature.max_value - feature.min_value) / (linguistic_term_count * 2 * fuzzyset_init_rate)
            s = random.gauss(mean_of_s, fuzzyset_init_sigma)
            m = fuzzy_var.get_random_m(s)
            fuzzyset = FuzzySet.create_random(m=m, s=s)

            fuzzy_var.add_linguistic_term(fuzzyset)
        return fuzzy_var

    def get_one_of_terms(self):
        return random.choice(self._linguistic_terms)

    def copy(self):
        var = LinguisticVariable(self.corresponding_feature)
        for term in self._linguistic_terms:
            var._linguistic_terms.append(term.copy())

        return var

    def plot(self):
        fig, axs = plt.subplots(len(self._linguistic_terms), 1, figsize=(8, 10))
        for term in self._linguistic_terms:
            pass
            #todo
