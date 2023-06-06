from fuzzy_system.fuzzy_set import FuzzySet
from fuzzy_variable import FuzzyVariable


class Clause:
    def __init__(self):
        self.variable: FuzzyVariable
        self.fuzzy_set: FuzzySet
