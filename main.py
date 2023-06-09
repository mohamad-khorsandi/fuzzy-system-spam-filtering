from sklearn.model_selection import train_test_split

import config
from evolutionary_algorithm import EvolutionaryAlgorithm
from fuzzy_system.enums import Features
from fuzzy_system.fuzzy_system import FuzzySystem
from fuzzy_system.linguistic_variable import LinguisticVariable
from preprocess_utils import get_data


def main():
    temp_X, temp_Y = get_data(False)
    config.train_X, config.test_X, config.train_Y, config.test_Y =\
        train_test_split(temp_X, temp_Y, test_size = 0.33, random_state=42)

    evolutionary_algorithm = EvolutionaryAlgorithm(5, 10, 6, 0, .9, 0.9)
    evolutionary_algorithm.run()
    evolutionary_algorithm.show_statistics()

    fuzzy_system = FuzzySystem(evolutionary_algorithm.population)
    y_pred, accuracy = fuzzy_system.evaluate(config.test_X, config.test_Y)
    print(accuracy)


def test_plot():
    Features.TWO.min_value = 0
    Features.TWO.max_value = 100
    var = LinguisticVariable.random_linguistic_variable(Features.TWO)
    var.plot()


if __name__ == '__main__':
    main()

