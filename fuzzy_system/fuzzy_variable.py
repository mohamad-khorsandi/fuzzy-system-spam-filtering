import random

from fuzzy_system.enums import Features
from fuzzy_system.fuzzy_set import fuzzy_set_constructor_functions


class FuzzyVariable:
    def __init__(self, corresponding_feature):
        self.corresponding_feature = corresponding_feature
        self._possible_fuzzysets = list()

    def add_possible_fuzzyset(self, p_fset):
        self._possible_fuzzysets.append(p_fset)
    @classmethod
    def get_random_fuzzy_variable(cls, feature: Features, fuzzyset_init_rate,
                                  fuzzyset_init_sigma):  # todo fuzzyset_init_rate is about 1.5, and fuzzyset_init_sigma is about 1
        fuzzy_var = FuzzyVariable(feature)
        fuzzysets_count = random.randint(1, 5)
        for i in range(fuzzysets_count):
            contructor_fucntion = random.choice(fuzzy_set_constructor_functions)
            mean_of_s = (feature.max_value - feature.min_value) / (fuzzysets_count * 2 * fuzzyset_init_rate)
            s = random.gauss(mean_of_s, fuzzyset_init_sigma)

            m = random.uniform(feature.min_value + s, feature.max_value - s)
            is_not = random.choice([True, False])  # ToDO increase the possibility of true
            fuzzy_set = contructor_fucntion(is_not, m, s)
            fuzzy_var.add_possible_fuzzyset(fuzzy_set)
        return fuzzy_var

    def get_random_possible_fuzzyset(self):
        return random.choice(self._possible_fuzzysets)
