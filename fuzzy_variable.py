from fuzzy_system.fuzzy_set import FuzzySet


class FuzzyVariable:
    def __init__(self):
        name: str
        possible_fuzzysets: list[FuzzySet]  # ToDo limit
