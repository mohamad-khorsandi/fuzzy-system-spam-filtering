import random

import numpy as np

from fuzzy_system.clause import Clause
from fuzzy_system.enums import Result, Features
import config


class Rule:
    def __init__(self):
        self._clause_list = list()
        self._result = None
        self._lock = False
        self._fitness = None

    def get_fitness(self):
        if self._lock:
            return self._fitness

        self._fitness = self._cal_fitness()
        self._lock = True

        return self._fitness

    def add_clause(self, clause):
        self._clause_list.append(clause)

    def set_result(self, result):
        self._result = result

    def get_result(self):
        return self._result

    def get_clause_count(self):
        return len(self._clause_list)

    def _cal_fitness(self):
        positive = 0
        negative = 0
        X = config.train_X
        Y = config.train_Y
        for i in range(len(X)):
            if Y[i] == self._result.label:
                positive += self.matching_rate(X[i])
            else:
                negative += self.matching_rate(X[i])

        if (positive + negative) == 0:
            return 0.0
        else:
            return (positive - negative) / (positive + negative)

    def matching_rate(self, x):
        result = 1
        for clause in self._clause_list:
            result *= clause.term_membership_function(x[clause.get_feature_index()])

        return result

    def copy(self):
        new_rule = Rule()
        for clause in self._clause_list:
            new_rule.add_clause(clause.copy())

        new_rule._result = self._result
        return new_rule

    @classmethod
    def random_rule(cls):
        rule = Rule()
        clause_count = Rule.random_clause_count()
        feature_list = random.sample(list(Features), k=clause_count)

        for feature in feature_list:
            clause = Clause.random_clause(feature)
            rule.add_clause(clause)

        rule.set_result(random.choice(list(Result)))
        return rule

    def __str__(self):
        res = 'if '
        for clause in self._clause_list:
            res += clause.__str__() + ' & '

        return res + f' then sms is {self._result.string}'

    @classmethod
    def random_clause_count(cls):
        return random.randint(1, 5)

    def has_feature(self, f):
        for c in self._clause_list:
            if c.get_feature() == f:
                print(c.get_feature, f)
                return c, True

        return None, False

    def clause_len(self):
        return len(self._clause_list)

    def get_copy_of_random_clause(self):
        return random.choice(self._clause_list).copy()

    def search_feature_in_rule(rule, feature_index):
        for clause in rule._clause_list:
            if clause.get_feature_index() == feature_index:
                return clause.copy()
        return None

