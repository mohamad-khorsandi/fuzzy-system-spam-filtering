import random
from random import choices

import config
from fuzzy_system.clause import Clause
from fuzzy_system.enums import Result, Features
from fuzzy_system.rule import Rule


def parent_selection(generation, count):
    prob_list = _get_weight_list(generation)
    return choices(generation, prob_list, k=count)


def mutation(parent: Rule, p_mut):
    if not bool_rand(p_mut):
        return parent.copy()

    new_rule = Rule()
    for feature in Features:
        parent_clause, has_feature = parent.has_feature(feature)
        if has_feature:
            if not bool_rand(config.mut_remove_clause_rate):
                new_rule.add_clause(parent_clause.mut())

        elif not has_feature:
            if bool_rand(config.mut_add_clause_rate):
                new_clause = Clause.random_clause(feature=feature)
                new_rule.add_clause(new_clause)

    # avoid having rule with no clause
    if new_rule.clause_len() == 0:
        new_rule.add_clause(parent.get_copy_of_random_clause())

    return new_rule


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

