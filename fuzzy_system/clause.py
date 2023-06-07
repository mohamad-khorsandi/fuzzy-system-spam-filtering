class Clause:
    def __init__(self, f_var, f_set):
        self.is_not = False
        self.variable = f_var
        self.fuzzy_set = f_set
