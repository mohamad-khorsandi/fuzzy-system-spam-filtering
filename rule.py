from enum import Enum


class Result(Enum):
    SPAM = 1
    NOT_SPAM = 0


class Rule:
    def __init__(self, feature_extractor):
        self._clause_list = list()
        self._result: Result
        self._lock = False
        self._fitness = float()

    def get_fitness(self):
        if self._lock:
            return self._fitness

        self._fitness = self._cal_fitness()
        self._lock = True
        return self._fitness

    def _cal_fitness(self):
        pass

    def copy(self):
        pass

    @classmethod
    def get_random_chromosome(cls):
        pass

    def show(self):
        pass
