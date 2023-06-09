import random
import numpy as np

import config
from config import neg_initial_overlap_rate, sigma_for_changing_s
from fuzzy_system.membership_functions import membership_function_list
from randomutil import bool_rand


class FuzzySet:
    def __init__(self, term, l_bound, u_bound, mem_func):
        self._lower_bound = l_bound
        self._upper_bound = u_bound
        self._membership_function = mem_func
        self._linguistic_term = term
        self._m = None
        self._s = None

    def set_m(self, m):
        if self._lower_bound < m < self._upper_bound:
            self._m = m
            return True
        else:
            return False

    def set_s(self, s):
        if s >= 0:
            self._s = s
            return True
        else:
            return False

    def set_random_m(self, mu, sigma):
        counter = 0
        while True:
            counter += 1
            if counter > 4:
                print("warn warn")  # todo remove
            tmp_m = random.gauss(mu, sigma)
            m_was_in_range = self.set_m(tmp_m)
            if m_was_in_range:
                break

    def set_random_s(self, mu, sigma):
        counter = 0
        while True:
            counter += 1
            if counter > 4:
                print("warn warn")  # todo remove
            tmp_s = random.gauss(mu, sigma)
            s_was_in_range = self.set_s(tmp_s)
            if s_was_in_range:
                break

    def membership_function(self, x):
        return self._membership_function(x, m=self._m, s=self._s)

    def copy(self):
        f_set = FuzzySet(term=self._linguistic_term, u_bound=self._upper_bound,
                         l_bound=self._lower_bound, mem_func=self._membership_function)

        f_set.set_m(self._m)
        f_set.set_s(self._s)
        return f_set

    def plot(self, ax, lower_bound, upper_bound):
        x = np.linspace(lower_bound, upper_bound, 100)
        y = []
        for i in x:
            y.append(self.membership_function(i))

        ax.plot(x, y)

    def linguistic_term_is_equal_to(self, linguistic_term):
        return self._linguistic_term == linguistic_term

    def mut(self):
        mem_func = self._membership_function
        if bool_rand(config.mut_step):
            mem_func = random.choice(membership_function_list)

        f_set = FuzzySet(term=self._linguistic_term, u_bound=self._upper_bound
                         , l_bound=self._lower_bound, mem_func=mem_func)

        f_set.set_random_m(self._m, config.sigma_for_changing_m)
        f_set.set_random_s(self._s, config.sigma_for_changing_s)

        return f_set

    @classmethod
    def random_fuzzyset(cls, term, center, u_bound, l_bound):
        mem_func = random.choice(membership_function_list)
        f_set = FuzzySet(u_bound=u_bound, l_bound=l_bound, mem_func=mem_func, term=term)

        mean_of_s = (u_bound - l_bound) / (6 * neg_initial_overlap_rate)
        f_set.set_random_s(mean_of_s, sigma_for_changing_s)

        f_set.set_random_m(center, config.sigma_for_changing_m)

        return f_set
