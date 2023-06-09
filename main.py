import config
from evolutionary_algorithm import EvolutionaryAlgorithm
from fuzzy_system.enums import Features
from fuzzy_system.linguistic_variable import LinguisticVariable
from preprocess_utils import get_data


def main():
    config.X, config.Y = get_data(False)
    evolutionary_algorithm = EvolutionaryAlgorithm(5, 10, 6, 0, 0, 2)
    evolutionary_algorithm.run()
    evolutionary_algorithm.show_statistics()


def test_plot():
    Features.TWO.min_value = 0
    Features.TWO.max_value = 100
    var = LinguisticVariable.random_linguistic_variable(Features.TWO)
    var.plot()


if __name__ == '__main__':
    pass

