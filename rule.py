import random
from enum import Enum

import main
from clause import Clause


class Result(Enum):
    SPAM = 1
    NOT_SPAM = 0


class Rule:
    def __init__(self):
        self._clause_list: list[Clause]
        self._result: Result
        self._lock = False
        self._fitness: float()

    def get_fitness(self):
        if self._lock:
            return self._fitness

        self._fitness = self._cal_fitness()
        self._lock = True
        return self._fitness

    def _cal_fitness(self, input_list , lables):
        positive = 0
        negative = 0
        for i in range(len(input_list)):
            if lables[i] == self._result:
                positive += self.matching_rate(input_list[i])
            else:
                negative += self.matching_rate(input_list[i])

        CF = (positive - negative)/(positive + negative)

        return CF

    def matching_rate(self, x):  # ToDo how to match in input with clause
        gR = 1
        for clause in self._clause_list:
            gR *= clause.fuzzy_set.mem_func(x[clause.index])
        return gR

    def copy(self):
        pass

    @classmethod
    def get_random_chromosome(cls): # todo add some hioristic to random init
        main.main()
        clause_count = random.randint(1, 5)
        for i in range(clause_count):
            feature_index_list = random.sample(list(main.Features), k=clause_count)
            for i in range(feature_index_list):
                clause = Clause()
                clause.

    def show(self):
        pass

if __name__ == '__main__':
    Rule.get_random_chromosome()