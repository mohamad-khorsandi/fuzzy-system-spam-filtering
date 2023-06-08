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
    SPAM = 1
    NOT_SPAM = 0


class TermName(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2
