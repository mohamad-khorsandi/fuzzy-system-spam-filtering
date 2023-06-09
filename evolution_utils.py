import random
from random import choices

from fuzzy_system.clause import Clause
from fuzzy_system.enums import Result, Features
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
        clause = Clause()
        c.add_clause()


def recombination(p1: Rule, p2: Rule, p_rec, p_increase_rate_rec):
    child_result = random.choice(list(Result))
    child_rule = Rule()
    if not bool_rand(p_rec):
        return p1.copy(), p2.copy()
    else:
        for features in Features:
            clause_p1 = search_feature_in_rule(p1, features.index)
            clause_p2 = search_feature_in_rule(p2, features.index)
            if bool_rand(p_increase_rate_rec):
                if clause_p1 is None and clause_p2 is None:
                    continue
                elif clause_p1 is not None and clause_p2 is not None:
                    tmp_rule = max_CF(p1, p2)
                    if tmp_rule.get_result() == child_result:
                        child_rule.add_clause(search_feature_in_rule(tmp_rule, features.index))
                    else:
                        tmp_clause: Clause
                        tmp_clause = search_feature_in_rule(tmp_rule, features.index)
                        tmp_clause.negative_term()
                        child_rule.add_clause(tmp_clause)

                elif clause_p1 is None:
                    if p2.get_result() == child_result:
                        child_rule.add_clause(clause_p2)
                    else:
                        tmp_clause: Clause
                        tmp_clause = search_feature_in_rule(p2, features.index)
                        tmp_clause.negative_term()
                        child_rule.add_clause(tmp_clause)
                else:
                    if p1.get_result() == child_result:
                        child_rule.add_clause(clause_p1)
                    else:
                        tmp_clause: Clause
                        tmp_clause = search_feature_in_rule(p1, features.index)
                        tmp_clause.negative_term()
                        child_rule.add_clause(tmp_clause)


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


def search_feature_in_rule(rule, feature_index):
    for clause in rule.get_clause_list():
        if clause.get_feature_index() == feature_index:
            return clause
    return None

def max_CF(rule1: Rule, rule2: Rule):
    cf1 = rule1.get_fitness()
    cf2 = rule2.get_fitness()
    if cf1 > cf2:
        return rule1
    else:
        return rule2
