from random import choices


def parent_selection(generation, count):
    prob_list = _get_weight_list(generation)
    return choices(generation, prob_list, k=count)


def mutation(parent, p_mut, mut_step):
    pass


def recombination(p1, p2, p_rec):
    pass


def _get_weight_list(chromosome_list: list, reverse=False):
    fittness_list = [c.get_fitness() for c in chromosome_list]

    fittness_sum = sum(fittness_list)
    assert fittness_sum != 0

    weight_list = [p / fittness_sum for p in fittness_list]

    assert any([0 <= p <= 1 for p in weight_list])
    if reverse:
        return [1 - p for p in weight_list]
    else:
        return weight_list