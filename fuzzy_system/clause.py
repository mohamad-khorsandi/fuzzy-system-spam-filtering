import random

import config
from fuzzy_system.enums import SignedTerms
from fuzzy_system.linguistic_variable import LinguisticVariable
from randomutil import bool_rand


class Clause:
    def __init__(self, var, term):
        self._linguistic_variable = var
        self._signed_linguistic_term = term

    def get_feature_index(self):
        return self._linguistic_variable.corresponding_feature.index

    def get_feature(self):
        return self._linguistic_variable.corresponding_feature.index

    def term_membership_function(self, x):
        term = self._signed_linguistic_term.simple_term
        result = self._linguistic_variable.mem_func_of_given_term(term, x)

        if self._signed_linguistic_term.is_negative:
            return -1 * result + 1
        else:
            return result

    @classmethod
    def random_clause(cls, feature):
        variable = LinguisticVariable.random_linguistic_variable(feature)
        term = variable.get_random_signed_term()
        return Clause(var=variable, term=term)

    def copy(self):
        var = self._linguistic_variable.copy()
        assert type(self._signed_linguistic_term) == SignedTerms
        term = self._signed_linguistic_term
        return Clause(var=var, term=term)

    def mut(self):
        var = self._linguistic_variable.mut()
        term = self._signed_linguistic_term()

        if bool_rand(config.mut_step):
            term = LinguisticVariable.get_random_signed_term()

        return Clause(var=var, term=term)

    def __str__(self):
        index = self._linguistic_variable.corresponding_feature.index
        return f' x{index + 1} is {self._signed_linguistic_term.string}'

    def negative_term(self):
        term: SignedTerms
        term = self._signed_linguistic_term
        negative_index = term.negative_index
        for signedterm in SignedTerms:
            if signedterm.index == negative_index:
                self._signed_linguistic_term = signedterm
                break
