import random

from fuzzy_system.clause import Clause
from fuzzy_system.enums import Result, Features
from fuzzy_system.fuzzy_variable import FuzzyVariable


class Rule:
    def __init__(self):
        self._clause_list = list()
        self._result = None
        self._lock = False
        self._fitness = float()

    def get_fitness(self, features, labels):
        if self._lock:
            return self._fitness

        self._fitness = self._cal_fitness(features, labels)
        self._lock = True
        return self._fitness

    def add_clause(self, clause):
        self._clause_list.append(clause)

    def set_result(self, result):
        self._result = result

    def _cal_fitness(self, features, labels):
        positive = 0
        negative = 0
        for i in range(len(features)):
            if labels[i] == self._result.value:
                positive += self.matching_rate(features[i])
            else:
                negative += self.matching_rate(features[i])

        CF = (positive - negative) / (positive + negative)

        return CF

    def matching_rate(self, x):  # ToDo how to match in input with clause
        gR = 1
        for clause in self._clause_list:
            gR *= clause.calculate_matching_rate(x[clause.get_feature().index],
                                                 clause.fuzzy_set.get_m(),
                                                 clause.fuzzy_set.get_s())
        return gR

    def copy(self):
        pass

    @classmethod
    def get_random_chromosome(cls, fuzzyset_init_rate, fuzzyset_init_sigma):  # todo add some hioristic to random init
        rule = Rule()
        clause_count = random.randint(1, 5)
        feature_list = random.sample(list(Features), k=clause_count)
        for feature in feature_list:
            fuzzy_variable = FuzzyVariable.get_random_fuzzy_variable(feature, fuzzyset_init_rate,
                                                                     fuzzyset_init_sigma)
            fuzzy_set = fuzzy_variable.get_random_possible_fuzzyset()
            clause = Clause(fuzzy_variable, fuzzy_set)
            rule.add_clause(clause)

        rule.set_result(random.choice(list(Result)))
        return rule

    def show(self):
        pass


if __name__ == '__main__':
    Rule.get_random_chromosome()
