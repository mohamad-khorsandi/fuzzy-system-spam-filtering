from enum import Enum

from .clause import Clause


class Result(Enum):
    SPAM = 1
    NOT_SPAM = 0


class Rule:
    def __init__(self):
        self._clause_list = list[Clause]
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

    def matching_rate(self, x):  # ToDo how to match in input with clause
        gR = 1
        for i, clause in enumerate(self._clause_list):
            gR *= clause.fuzzy_set.mem_func(x[i])
        return gR

    def copy(self):
        pass

    @classmethod
    def get_random_chromosome(cls):
        pass

    def show(self):
        pass
