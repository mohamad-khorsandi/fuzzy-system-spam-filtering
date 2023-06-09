import numpy as np
from sklearn.metrics import accuracy_score

from fuzzy_system.enums import Result
from fuzzy_system.rule import Rule


class FuzzySystem:

    def __init__(self, rules: list[Rule]):
        self._rules = rules

    def add_rule(self, num_of_rules):
        for _ in range(num_of_rules):
            self._rules.append(Rule.random_rule())

    def evaluate(self, x_test, y_test):
        rule_spam = [Rule]
        rule_not_spam = [Rule]

        result_spam = 0
        result_not_spam = 0
        y_pred = np.zeros(len(x_test))

        for i in range(len(x_test)):
            for r in self._rules:
                if r.get_result() == Result.SPAM:
                    result_spam += r.matching_rate(x_test[i])
                else:
                    result_not_spam += r.matching_rate(x_test[i])
                    rule_not_spam.append(r)

            if result_spam > result_not_spam:
                y_pred[i] = Result.SPAM.label
            else:
                y_pred[i] = Result.NOT_SPAM.label

        accuracy = accuracy_score(y_test, y_pred)
        return y_pred, accuracy
