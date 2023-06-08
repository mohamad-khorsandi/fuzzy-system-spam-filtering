import random

from fuzzy_system.linguistic_variable import LinguisticVariable


class Clause:
    def __init__(self, var, term):
        self._linguistic_variable = var
        self._linguistic_term = term

    def get_feature_index(self):
        return self._linguistic_variable.corresponding_feature.index

    def term_membership_function(self, x):
        return self._linguistic_term.membership_function(x)

    @classmethod
    def random_clause(cls, feature):
        variable = LinguisticVariable.random_linguistic_variable(feature)
        term = variable.get_one_of_terms()
        return Clause(var=variable, term=term)

    def copy(self):
        var = self._linguistic_variable.copy()
        term = self._linguistic_term.copy()
        assert var is not  None and term is not None
        return Clause(var=var, term=term)

    def __str__(self):
        index = self._linguistic_variable.corresponding_feature.index
        return f'if {index} is {self._linguistic_term}'
