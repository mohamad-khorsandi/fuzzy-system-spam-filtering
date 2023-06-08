import random

from fuzzy_system.linguistic_variable import LinguisticVariable


class Clause:
    def __init__(self, negative, var, term):
        self._negative = negative
        self._linguistic_variable = var
        self._linguistic_term = term

    def get_feature_index(self):
        return self._linguistic_variable.corresponding_feature.index

    def term_membership_function(self, x):
        result = self._linguistic_term.membership_function(x)
        if self._negative:
            return -1 * result + 1  # todo is this correct
        else:
            return result

    @classmethod
    def random_clause(cls, feature):
        negative = random.choice([True, False])  # ToDO increase the possibility of true?

        variable = LinguisticVariable.random_linguistic_variable(feature)
        term = variable.get_one_of_terms()
        return Clause(negative, variable, term)

    def copy(self):
        var = self._linguistic_variable.copy()
        term = self._linguistic_term.copy()
        assert var is not  None and term is not None
        return Clause(self._negative, var=var, term=term)

    def __str__(self):
        return 'if '