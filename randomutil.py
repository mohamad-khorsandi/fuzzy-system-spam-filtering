import random

from fuzzy_system.enums import Result


def bool_rand(probTrue):
    return random.choices([False, True], [1 - probTrue, probTrue])[0]


def random_result():
    return random.choice(list(Result))