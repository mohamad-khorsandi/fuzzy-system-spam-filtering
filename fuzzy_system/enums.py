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
    POSITIVE_LOW = (SimpleTerms.LOW, False, 'low')
    POSITIVE_MEDIUM = (SimpleTerms.MEDIUM, False, 'medium')
    POSITIVE_HIGH = (SimpleTerms.HIGH, False, 'high')

    NEGATIVE_LOW = (SimpleTerms.LOW, True, 'not low')
    NEGATIVE_MEDIUM = (SimpleTerms.MEDIUM, True, 'not medium')
    NEGATIVE_HIGH = (SimpleTerms.HIGH, True, 'not high')

    def __init__(self, simple_term, is_negative, string):
        self.simple_term = simple_term
        self.is_negative = is_negative
        self.string = string
