from sklearn.metrics import accuracy_score

from enums import Result
from rule import Rule


class FuzzySystem:

    def __init__(self, rules: list[Rule]):
        self._rules = rules

    def add_rule(self, num_of_rules):
        for _ in range(num_of_rules):
            self._rules.append(Rule.random_rule())

    def evaluate(self, x_test, y_test):
        rule_spam = [Rule]
        rule_not_spam = [Rule]
        for r in self._rules:
            if r.get_result() == Result.SPAM:
                rule_spam.append(r)
            else:
                rule_not_spam.append(r)

        result_spam = 0
        result_not_spam = 0
        y_pred = []
        for i in range(len(x_test)):
            for rule in rule_spam:
                result_spam += rule.matching_rate(x_test[i])

            for rule in rule_not_spam:
                result_not_spam += rule.matching_rate(x_test[i])

            if result_spam > result_not_spam:
                y_pred[i] = 1
            else:
                y_pred[i] = 0

        accuracy = accuracy_score(y_test, y_pred)
        return y_pred, accuracy
