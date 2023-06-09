from enum import Enum


class Features(Enum):
    ONE = 0
    TWO = 1
    THREE = 2
    FOUR = 3
    FIVE = 4

    def __init__(self, index):
        self.min_value = None
        self.max_value = None
        self.index = index


class Result(Enum):
    SPAM = (0, 'spam')
    NOT_SPAM = (1, 'not spam')

    def __init__(self, label, string):
        self.label = label
        self.string = string


class SimpleTerms(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2


class SignedTerms(Enum):
    POSITIVE_LOW = (SimpleTerms.LOW, False, 'low', 3, 0)
    POSITIVE_MEDIUM = (SimpleTerms.MEDIUM, False, 'medium', 4, 1)
    POSITIVE_HIGH = (SimpleTerms.HIGH, False, 'high', 5, 2)

    NEGATIVE_LOW = (SimpleTerms.LOW, True, 'not low', 0, 3)
    NEGATIVE_MEDIUM = (SimpleTerms.MEDIUM, True, 'not medium', 1, 4)
    NEGATIVE_HIGH = (SimpleTerms.HIGH, True, 'not high', 2, 5)

    def __init__(self, simple_term, is_negative, string, negative_index, index):
        self.simple_term = simple_term
        self.is_negative = is_negative
        self.string = string
        self.index = index
        self.negative_index = negative_index
