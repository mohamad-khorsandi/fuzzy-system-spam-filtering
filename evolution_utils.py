import random
from random import choices

import config
from fuzzy_system.clause import Clause
from fuzzy_system.enums import Result, Features
from fuzzy_system.rule import Rule
from randomutil import bool_rand


def parent_selection(generation, count):
    prob_list = _get_weight_list(generation)
    return choices(generation, prob_list, k=count)


def mutation(parent: Rule, p_mut):
    if not bool_rand(p_mut):
        return parent.copy()

    new_rule = Rule()
    new_rule.set_result(parent.get_result())
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
    if bool_rand(p_rec):
        return p1.copy(), p2.copy()
    c1 = single_recombination(p1, p2)

    c2 = single_recombination(p1, p2)
    return c1, c2


def single_recombination(p1: Rule, p2: Rule):
    child_result = random.choice(list(Result))
    child_rule = Rule()
    child_rule.set_result(child_result)

    for features in Features:
        clause_p1 = p1.search_feature_in_rule(features.index)
        clause_p2 = p2.search_feature_in_rule(features.index)

        if bool_rand(config.p_increase_rate_rec):
            if clause_p1 is None and clause_p2 is None:
                continue
            elif clause_p1 is not None and clause_p2 is not None:
                tmp_rule = max_CF(p1, p2)
                if tmp_rule.get_result() == child_result:
                    child_rule.add_clause(tmp_rule.search_feature_in_rule(features.index))
                else:
                    tmp_clause: Clause
                    tmp_clause = tmp_rule.search_feature_in_rule(features.index)
                    tmp_clause.negative_term()
                    child_rule.add_clause(tmp_clause)

            elif clause_p1 is None:
                if p2.get_result() == child_result:
                    child_rule.add_clause(clause_p2)
                else:
                    tmp_clause: Clause
                    tmp_clause = p2.search_feature_in_rule(features.index)
                    tmp_clause.negative_term()
                    child_rule.add_clause(tmp_clause)
            else:
                if p1.get_result() == child_result:
                    child_rule.add_clause(clause_p1)
                else:
                    tmp_clause: Clause
                    tmp_clause = p1.search_feature_in_rule(features.index)
                    tmp_clause.negative_term()
                    child_rule.add_clause(tmp_clause)

        better_parent = max_CF(p1, p2)

        if child_rule.clause_len() == 0:
            child_rule.add_clause(better_parent.get_copy_of_random_clause())
    return child_rule


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



def max_CF(rule1: Rule, rule2: Rule):
    cf1 = rule1.get_fitness()
    cf2 = rule2.get_fitness()
    if cf1 > cf2:
        return rule1
    else:
        return rule2
