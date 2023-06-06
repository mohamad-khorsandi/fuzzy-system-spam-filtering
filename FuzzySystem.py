import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np

class FuzzySystem:
    def __init__(self):
            self._input_variables = {}
            self._output_variables = {}
            self._rules = []

    def __str__(self):

        ret_str = 'Input: \n'
        for n, s in self._input_variables.items():
            ret_str = ret_str + f'{n}: ({s})\n'

        ret_str = ret_str + 'Output: \n'
        for n, s in self._output_variables.items():
            ret_str = ret_str + f'{n}: ({s})\n'

        ret_str = ret_str + 'Rules: \n'
        for rule in self._rules:
            ret_str = ret_str + f'{rule}\n'

        return ret_str

    def add_input_variable(self, variable):
        self._input_variables[variable.name] = variable

    def add_output_variable(self, variable):
        self._output_variables[variable.name] = variable

    def get_input_variable(self, name):
        return self._input_variables[name]

    def get_output_variable(self, name):
        return self._output_variables[name]

    def _clear_output_distributions(self):
        map(lambda output_var: output_var.clear_output_distribution(), self._output_variables.values())

    def add_rule(self, antecedent_clauses, consequent_clauses):
        '''
        adds a new rule to the system.
        TODO: add checks

        Arguments:
        -----------
        antecedent_clauses -- dict, having the form {variable_name:set_name, ...}
        consequent_clauses -- dict, having the form {variable_name:set_name, ...}
        '''
        # create a new rule
        # new_rule = FuzzyRule(antecedent_clauses, consequent_clauses)
        new_rule = FuzzyRule()

        for var_name, set_name in antecedent_clauses.items():
            # get variable by name
            var = self.get_input_variable(var_name)
            # get set by name
            f_set = var.get_set(set_name)
            # add clause
            new_rule.add_antecedent_clause(var, f_set)

        for var_name, set_name in consequent_clauses.items():
            var = self.get_output_variable(var_name)
            f_set = var.get_set(set_name)
            new_rule.add_consequent_clause(var, f_set)

        # add the new rule
        self._rules.append(new_rule)
