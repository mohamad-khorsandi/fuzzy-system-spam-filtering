class Clause:
    def __init__(self, f_var, f_set):
        self._is_not = False
        self._variable = f_var
        self._fuzzy_set = f_set

    def get_feature(self):
        return self._variable.corresponding_feature

    def calculate_matching_rate(self, x, m, s):
        self._fuzzy_set.calculate_mem_degree(x, m, s)

