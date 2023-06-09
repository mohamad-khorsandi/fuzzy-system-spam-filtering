import random
from random import choices

from fuzzy_system.enums import Result
from fuzzy_system.rule import Rule


def parent_selection(generation, count):
    prob_list = _get_weight_list(generation)
    return choices(generation, prob_list, k=count)


def mutation(parent: Rule, p_mut, mut_step):
    c = parent.copy()
    if not bool_rand(p_mut):
        return c

    c.result = parent.get_result()
    result_changed = False
    if bool_rand(mut_step):
        c.result = random_result()
        if c.result != parent.get_result():
            result_changed = True


    clause_count = parent.get_clause_count()
    if bool_rand(mut_step):
        clause_count = Rule.random_clause_count()

    for i in range(clause_count):



def recombination(p1: Rule, p2: Rule, p_rec):
    if not bool_rand(p_rec):
        return p1.copy(), p2.copy()


def _get_weight_list(chromosome_list: list, reverse=False):
    fittness_list = [c.get_fitness() for c in chromosome_list]
    min_fitness = min(fittness_list)

    if min_fitness < 0:
        fittness_list = [fittness - min_fitness for fittness in fittness_list]

    fittness_sum = sum(fittness_list)
    assert fittness_sum != 0

    weight_list = [p / fittness_sum for p in fittness_list]

    assert any([0 <= p <= 1 for p in weight_list])
    if reverse:
        return [1 - p for p in weight_list]
    else:
        return weight_list


def bool_rand(probTrue):
    return random.choices([False, True], [1 - probTrue, probTrue])[0]


def random_result():
    return random.choice(list(Result))

