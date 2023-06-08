import random

from matplotlib import pyplot as plt

from fuzzy_system.enums import Features, TermName, LinguisticTerms
from fuzzy_system.fuzzy_set import FuzzySet
from fuzzy_system.fuzzy_system_config import fuzzyset_init_sigma, fuzzyset_init_rate, distance_from_centers


class LinguisticVariable:
    def __init__(self, corresponding_feature):
        self.corresponding_feature = corresponding_feature
        self._linguistic_terms = list()
        self._fuzzy_sets = list()

    def add_linguistic_term(self, fuzzyset: FuzzySet):
        lower_bound = self.corresponding_feature.min_value + fuzzyset.get_s()
        upper_bound = self.corresponding_feature.max_value - fuzzyset.get_s()
        assert lower_bound < fuzzyset.get_m() < upper_bound
        self._linguistic_terms.append(fuzzyset)

    def get_random_m(self, s):
        return random.uniform(self.corresponding_feature.min_value + s, self.corresponding_feature.max_value - s)

    @classmethod
    def random_linguistic_variable(cls, feature: Features):
        linguistic_variable = LinguisticVariable(feature)

        tmp = (feature.max_value - feature.min_value) / 6
        centers = [tmp, 3*tmp, 5*tmp]
        for i, cen in enumerate(centers):
            mean_of_s = (feature.max_value - feature.min_value) / (6 * fuzzyset_init_rate)
            s = random.gauss(mean_of_s, fuzzyset_init_sigma)
            random.gauss(mean_of_s, fuzzyset_init_sigma)
            m = random.gauss(cen, distance_from_centers)
            fuzzyset = FuzzySet.create_random(m=m, s=s)
            fuzzyset.name = list(TermName)[i]
            linguistic_variable._fuzzy_sets.append(fuzzyset)

        linguistic_variable._linguistic_terms = random.sample(list(LinguisticTerms), k=random.randint(3, 5))
        return linguistic_variable

    def get_one_of_terms(self):
        return random.choice(self._linguistic_terms)

    def copy(self):
        var = LinguisticVariable(self.corresponding_feature)
        for term in self._linguistic_terms:
            var._linguistic_terms.append(term.copy())

        return var

    def plot(self):
        fig, ax = plt.subplots(figsize=(8, 10))
        for term in self._linguistic_terms:
            term.plot(ax, self.corresponding_feature.min_value, self.corresponding_feature.max_value)
        plt.show()
